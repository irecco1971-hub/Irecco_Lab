import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from backend.modules.identity.models import User
from backend.modules.identity.schemas import UserCreate
from backend.modules.identity.service import IdentityService
from backend.shared.exceptions import ConflictError, PermissionDeniedError
from backend.shared.security import hash_password


def _make_repo(*, existing_user: User | None = None) -> MagicMock:
    repo = MagicMock()
    repo.get_by_email = AsyncMock(return_value=existing_user)
    repo.get_by_id = AsyncMock(return_value=existing_user)
    repo.create = AsyncMock(side_effect=lambda u: u)
    return repo


def _make_user(*, is_active: bool = True) -> User:
    return User(
        id=uuid.uuid4(),
        email="test@example.com",
        hashed_password=hash_password("secret123"),
        is_active=is_active,
        is_superuser=False,
    )


class TestRegister:
    async def test_creates_user_when_email_is_new(self):
        repo = _make_repo(existing_user=None)
        svc = IdentityService(repo)

        user = await svc.register(UserCreate(email="new@example.com", password="pass"))

        repo.create.assert_awaited_once()
        assert user.email == "new@example.com"
        assert user.hashed_password != "pass"

    async def test_raises_conflict_when_email_exists(self):
        repo = _make_repo(existing_user=_make_user())
        svc = IdentityService(repo)

        with pytest.raises(ConflictError):
            await svc.register(UserCreate(email="test@example.com", password="pass"))

        repo.create.assert_not_awaited()


class TestLogin:
    async def test_returns_token_for_valid_credentials(self):
        user = _make_user()
        repo = _make_repo(existing_user=user)
        svc = IdentityService(repo)

        token = await svc.login("test@example.com", "secret123")

        assert isinstance(token, str)
        assert len(token) > 0

    async def test_raises_for_wrong_password(self):
        user = _make_user()
        repo = _make_repo(existing_user=user)
        svc = IdentityService(repo)

        with pytest.raises(PermissionDeniedError):
            await svc.login("test@example.com", "wrongpassword")

    async def test_raises_for_unknown_email(self):
        repo = _make_repo(existing_user=None)
        svc = IdentityService(repo)

        with pytest.raises(PermissionDeniedError):
            await svc.login("nobody@example.com", "pass")

    async def test_raises_for_inactive_user(self):
        user = _make_user(is_active=False)
        repo = _make_repo(existing_user=user)
        svc = IdentityService(repo)

        with pytest.raises(PermissionDeniedError):
            await svc.login("test@example.com", "secret123")
