# FastAPI router for the products module. Mounts at /products.
# All write operations require a superuser.

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.identity.models import User
from backend.modules.products.repository import ProductRepository
from backend.modules.products.schemas import ProductCreate, ProductRead, ProductUpdate
from backend.modules.products.service import ProductService
from backend.shared.dependencies import get_current_user, get_db
from backend.shared.exceptions import ConflictError, NotFoundError

router = APIRouter(prefix="/products", tags=["products"])


def _service(db: AsyncSession = Depends(get_db)) -> ProductService:
    return ProductService(ProductRepository(db))


def _superuser(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Superuser required.")
    return current_user


@router.get("/", response_model=list[ProductRead])
async def list_products(svc: ProductService = Depends(_service)):
    return await svc.list()


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: uuid.UUID, svc: ProductService = Depends(_service)):
    try:
        return await svc.get(product_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(
    data: ProductCreate,
    svc: ProductService = Depends(_service),
    _: User = Depends(_superuser),
):
    try:
        return await svc.create(data)
    except ConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))


@router.patch("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: uuid.UUID,
    data: ProductUpdate,
    svc: ProductService = Depends(_service),
    _: User = Depends(_superuser),
):
    try:
        return await svc.update(product_id, data)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: uuid.UUID,
    svc: ProductService = Depends(_service),
    _: User = Depends(_superuser),
):
    try:
        await svc.delete(product_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
