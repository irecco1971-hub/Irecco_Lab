import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from backend.modules.products.models import Product, ProductStatus
from backend.modules.products.schemas import ProductCreate, ProductUpdate
from backend.modules.products.service import ProductService
from backend.shared.exceptions import ConflictError, NotFoundError


def _make_repo(
    *,
    all_products: list[Product] | None = None,
    existing: Product | None = None,
    by_slug: Product | None = None,
) -> MagicMock:
    repo = MagicMock()
    repo.get_all = AsyncMock(return_value=all_products or [])
    repo.get_by_id = AsyncMock(return_value=existing)
    repo.get_by_slug = AsyncMock(return_value=by_slug)
    repo.create = AsyncMock(side_effect=lambda p: p)
    repo.update = AsyncMock(side_effect=lambda p: p)
    repo.delete = AsyncMock()
    return repo


def _make_product(**kwargs) -> Product:
    defaults = dict(
        id=uuid.uuid4(),
        name="MillWork",
        slug="millwork",
        status=ProductStatus.active,
        description="CNC plugin for woodworkers.",
    )
    return Product(**{**defaults, **kwargs})


class TestList:
    async def test_returns_all_products(self):
        products = [_make_product(), _make_product(slug="other")]
        repo = _make_repo(all_products=products)
        result = await ProductService(repo).list()
        assert result == products


class TestGet:
    async def test_returns_product_when_found(self):
        product = _make_product()
        repo = _make_repo(existing=product)
        result = await ProductService(repo).get(product.id)
        assert result == product

    async def test_raises_not_found_when_missing(self):
        repo = _make_repo(existing=None)
        with pytest.raises(NotFoundError):
            await ProductService(repo).get(uuid.uuid4())


class TestCreate:
    async def test_creates_product_with_unique_slug(self):
        repo = _make_repo(by_slug=None)
        data = ProductCreate(name="MillWork", slug="millwork")
        result = await ProductService(repo).create(data)
        repo.create.assert_awaited_once()
        assert result.slug == "millwork"

    async def test_raises_conflict_for_duplicate_slug(self):
        repo = _make_repo(by_slug=_make_product())
        data = ProductCreate(name="MillWork", slug="millwork")
        with pytest.raises(ConflictError):
            await ProductService(repo).create(data)
        repo.create.assert_not_awaited()


class TestUpdate:
    async def test_updates_allowed_fields(self):
        product = _make_product()
        repo = _make_repo(existing=product)
        data = ProductUpdate(name="MillWork Pro", status=ProductStatus.beta)
        result = await ProductService(repo).update(product.id, data)
        assert result.name == "MillWork Pro"
        assert result.status == ProductStatus.beta

    async def test_raises_not_found_for_missing_product(self):
        repo = _make_repo(existing=None)
        with pytest.raises(NotFoundError):
            await ProductService(repo).update(uuid.uuid4(), ProductUpdate(name="X"))

    async def test_ignores_none_fields(self):
        product = _make_product(description="original")
        repo = _make_repo(existing=product)
        await ProductService(repo).update(product.id, ProductUpdate(description=None))
        assert product.description == "original"


class TestDelete:
    async def test_deletes_existing_product(self):
        product = _make_product()
        repo = _make_repo(existing=product)
        await ProductService(repo).delete(product.id)
        repo.delete.assert_awaited_once_with(product)

    async def test_raises_not_found_when_missing(self):
        repo = _make_repo(existing=None)
        with pytest.raises(NotFoundError):
            await ProductService(repo).delete(uuid.uuid4())
