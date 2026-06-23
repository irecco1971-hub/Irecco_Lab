# Pydantic schemas for the notifications module.

import uuid
from pydantic import BaseModel

from backend.modules.notifications.models import NotificationChannel


class NotificationCreate(BaseModel):
    user_id: uuid.UUID
    channel: NotificationChannel
    subject: str
    body: str


class NotificationRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    channel: NotificationChannel
    subject: str
    body: str
    is_read: bool

    model_config = {"from_attributes": True}
