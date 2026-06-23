# Business logic for the notifications module.
# Other modules dispatch notifications by calling NotificationService.send().

import uuid

from backend.modules.notifications.models import Notification, NotificationChannel
from backend.modules.notifications.repository import NotificationRepository
from backend.modules.notifications.schemas import NotificationCreate
from backend.shared.exceptions import NotFoundError, PermissionDeniedError


class NotificationService:
    def __init__(self, repo: NotificationRepository) -> None:
        self.repo = repo

    async def list_for_user(self, user_id: uuid.UUID) -> list[Notification]:
        return await self.repo.get_for_user(user_id)

    async def send(self, data: NotificationCreate) -> Notification:
        notification = Notification(
            user_id=data.user_id,
            channel=data.channel,
            subject=data.subject,
            body=data.body,
            is_read=False,
        )
        return await self.repo.create(notification)

    async def mark_read(self, notification_id: uuid.UUID, requesting_user_id: uuid.UUID) -> Notification:
        notification = await self.repo.get_by_id(notification_id)
        if not notification:
            raise NotFoundError(f"Notification {notification_id} not found.")
        if notification.user_id != requesting_user_id:
            raise PermissionDeniedError("Cannot mark another user's notification as read.")
        return await self.repo.mark_read(notification)
