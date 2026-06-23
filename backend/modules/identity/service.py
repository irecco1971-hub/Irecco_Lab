# Business logic for the identity module.
# Depends on UserRepository; must not import FastAPI or SQLAlchemy directly.

from backend.modules.identity.models import User
from backend.modules.identity.repository import UserRepository
from backend.modules.identity.schemas import UserCreate
from backend.shared.exceptions import ConflictError, PermissionDeniedError
from backend.shared.security import create_access_token, hash_password, verify_password


class IdentityService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    async def register(self, data: UserCreate) -> User:
        if await self.repo.get_by_email(data.email):
            raise ConflictError("Email already registered.")
        user = User(email=data.email, hashed_password=hash_password(data.password))
        return await self.repo.create(user)

    async def login(self, email: str, password: str) -> str:
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise PermissionDeniedError("Invalid credentials.")
        if not user.is_active:
            raise PermissionDeniedError("Account is inactive.")
        return create_access_token(subject=str(user.id))
