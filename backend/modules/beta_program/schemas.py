# Pydantic schemas for the beta_program module.

import uuid
from pydantic import BaseModel, EmailStr

from backend.modules.beta_program.models import WaitlistStatus


class WaitlistJoin(BaseModel):
    email: EmailStr


class WaitlistStatusUpdate(BaseModel):
    status: WaitlistStatus


class WaitlistEntryRead(BaseModel):
    id: uuid.UUID
    product_id: uuid.UUID
    email: EmailStr
    status: WaitlistStatus

    model_config = {"from_attributes": True}
