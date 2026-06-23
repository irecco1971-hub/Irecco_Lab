# Pydantic schemas for the products module.

import uuid
from pydantic import BaseModel, Field

from backend.modules.products.models import ProductStatus


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    slug: str = Field(min_length=1, max_length=128, pattern=r"^[a-z0-9-]+$")
    status: ProductStatus = ProductStatus.active
    description: str | None = None


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=128)
    status: ProductStatus | None = None
    description: str | None = None


class ProductRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    status: ProductStatus
    description: str | None

    model_config = {"from_attributes": True}
