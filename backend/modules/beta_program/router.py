# FastAPI router for the beta_program module. Mounts at /products/{product_id}/beta.
# Join is public. List and status update require superuser.

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.identity.models import User
from backend.modules.beta_program.repository import WaitlistRepository
from backend.modules.beta_program.schemas import (
    WaitlistEntryRead,
    WaitlistJoin,
    WaitlistStatusUpdate,
)
from backend.modules.beta_program.service import BetaProgramService
from backend.shared.dependencies import get_current_user, get_db
from backend.shared.exceptions import ConflictError, NotFoundError

router = APIRouter(prefix="/products/{product_id}/beta", tags=["beta_program"])


def _service(db: AsyncSession = Depends(get_db)) -> BetaProgramService:
    return BetaProgramService(WaitlistRepository(db))


def _superuser(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Superuser required.")
    return current_user


@router.post("/join", response_model=WaitlistEntryRead, status_code=status.HTTP_201_CREATED)
async def join_waitlist(
    product_id: uuid.UUID,
    data: WaitlistJoin,
    svc: BetaProgramService = Depends(_service),
):
    try:
        return await svc.join(product_id, data)
    except ConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))


@router.get("/", response_model=list[WaitlistEntryRead])
async def list_entries(
    product_id: uuid.UUID,
    svc: BetaProgramService = Depends(_service),
    _: User = Depends(_superuser),
):
    return await svc.list_entries(product_id)


@router.patch("/{entry_id}", response_model=WaitlistEntryRead)
async def update_entry_status(
    product_id: uuid.UUID,
    entry_id: uuid.UUID,
    data: WaitlistStatusUpdate,
    svc: BetaProgramService = Depends(_service),
    _: User = Depends(_superuser),
):
    try:
        return await svc.update_status(entry_id, data)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
