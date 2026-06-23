# Business logic for the products module.

import uuid

from backend.modules.products.models import Product
from backend.modules.products.repository import ProductRepository
from backend.modules.products.schemas import ProductCreate, ProductUpdate
from backend.shared.exceptions import ConflictError, NotFoundError


class ProductService:
    def __init__(self, repo: ProductRepository) -> None:
        self.repo = repo

    async def list(self) -> list[Product]:
        return await self.repo.get_all()

    async def get(self, product_id: uuid.UUID) -> Product:
        product = await self.repo.get_by_id(product_id)
        if not product:
            raise NotFoundError(f"Product {product_id} not found.")
        return product

    async def create(self, data: ProductCreate) -> Product:
        if await self.repo.get_by_slug(data.slug):
            raise ConflictError(f"Slug '{data.slug}' is already taken.")
        product = Product(**data.model_dump())
        return await self.repo.create(product)

    async def update(self, product_id: uuid.UUID, data: ProductUpdate) -> Product:
        product = await self.get(product_id)
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(product, field, value)
        return await self.repo.update(product)

    async def delete(self, product_id: uuid.UUID) -> None:
        product = await self.get(product_id)
        await self.repo.delete(product)
