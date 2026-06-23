# ORM models for the products module.
# Owns: product registry — name, slug, status, description.

import uuid
from enum import Enum

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.shared.base_model import Base


class ProductStatus(str, Enum):
    active = "active"
    beta = "beta"
    archived = "archived"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default=ProductStatus.active)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
