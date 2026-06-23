# Pydantic schemas for the support module.

import uuid
from pydantic import BaseModel, Field

from backend.modules.support.models import TicketStatus


class TicketCreate(BaseModel):
    product_id: uuid.UUID | None = None
    subject: str = Field(min_length=1, max_length=255)
    body: str = Field(min_length=1)


class TicketStatusUpdate(BaseModel):
    status: TicketStatus


class TicketMessageCreate(BaseModel):
    body: str = Field(min_length=1)


class TicketMessageRead(BaseModel):
    id: uuid.UUID
    ticket_id: uuid.UUID
    author_id: uuid.UUID | None
    body: str

    model_config = {"from_attributes": True}


class TicketRead(BaseModel):
    id: uuid.UUID
    product_id: uuid.UUID | None
    user_id: uuid.UUID | None
    subject: str
    status: TicketStatus

    model_config = {"from_attributes": True}
