# FastAPI router for the notifications module. Mounts at /notifications.
# Users can only access their own notifications.

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.identity.models import User
from backend.modules.notifications.repository import NotificationRepository
from backend.modules.notifications.schemas import NotificationRead
from backend.modules.notifications.service import NotificationService
from backend.shared.dependencies import get_current_user, get_db
from backend.shared.exceptions import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/notifications", tags=["notifications"])


def _service(db: AsyncSession = Depends(get_db)) -> NotificationService:
    return NotificationService(NotificationRepository(db))


@router.get("/", response_model=list[NotificationRead])
async def list_notifications(
    svc: NotificationService = Depends(_service),
    current_user: User = Depends(get_current_user),
):
    return await svc.list_for_user(current_user.id)


@router.patch("/{notification_id}/read", response_model=NotificationRead)
async def mark_as_read(
    notification_id: uuid.UUID,
    svc: NotificationService = Depends(_service),
    current_user: User = Depends(get_current_user),
):
    try:
        return await svc.mark_read(notification_id, current_user.id)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except PermissionDeniedError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc))
