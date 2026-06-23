# Data-access layer for the notifications module.

import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.notifications.models import Notification


class NotificationRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_for_user(self, user_id: uuid.UUID) -> list[Notification]:
        result = await self.db.execute(
            select(Notification).where(Notification.user_id == user_id)
        )
        return list(result.scalars().all())

    async def get_by_id(self, notification_id: uuid.UUID) -> Notification | None:
        return await self.db.get(Notification, notification_id)

    async def create(self, notification: Notification) -> Notification:
        self.db.add(notification)
        await self.db.commit()
        await self.db.refresh(notification)
        return notification

    async def mark_read(self, notification: Notification) -> Notification:
        notification.is_read = True
        await self.db.commit()
        await self.db.refresh(notification)
        return notification
