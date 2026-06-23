# FastAPI router for the support module. Mounts at /support.
# Opening tickets and adding messages requires auth.
# Listing all tickets and changing status requires superuser.

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.identity.models import User
from backend.modules.support.repository import SupportRepository
from backend.modules.support.schemas import (
    TicketCreate,
    TicketMessageCreate,
    TicketMessageRead,
    TicketRead,
    TicketStatusUpdate,
)
from backend.modules.support.service import SupportService
from backend.shared.dependencies import get_current_user, get_db
from backend.shared.exceptions import NotFoundError

router = APIRouter(prefix="/support", tags=["support"])


def _service(db: AsyncSession = Depends(get_db)) -> SupportService:
    return SupportService(SupportRepository(db))


def _superuser(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Superuser required.")
    return current_user


@router.get("/tickets", response_model=list[TicketRead])
async def list_tickets(
    svc: SupportService = Depends(_service),
    _: User = Depends(_superuser),
):
    return await svc.list_tickets()


@router.post("/tickets", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
async def open_ticket(
    data: TicketCreate,
    svc: SupportService = Depends(_service),
    current_user: User = Depends(get_current_user),
):
    return await svc.open_ticket(current_user.id, data)


@router.patch("/tickets/{ticket_id}", response_model=TicketRead)
async def update_ticket_status(
    ticket_id: uuid.UUID,
    data: TicketStatusUpdate,
    svc: SupportService = Depends(_service),
    _: User = Depends(_superuser),
):
    try:
        return await svc.update_status(ticket_id, data)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.get("/tickets/{ticket_id}/messages", response_model=list[TicketMessageRead])
async def list_messages(
    ticket_id: uuid.UUID,
    svc: SupportService = Depends(_service),
    _: User = Depends(get_current_user),
):
    try:
        return await svc.list_messages(ticket_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post(
    "/tickets/{ticket_id}/messages",
    response_model=TicketMessageRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_message(
    ticket_id: uuid.UUID,
    data: TicketMessageCreate,
    svc: SupportService = Depends(_service),
    current_user: User = Depends(get_current_user),
):
    try:
        return await svc.add_message(ticket_id, current_user.id, data)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
