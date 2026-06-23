# Business logic for the identity module.
# Depends on UserRepository; must not import FastAPI or SQLAlchemy directly.

from backend.modules.identity.models import User
from backend.modules.identity.repository import UserRepository
from backend.modules.identity.schemas import UserCreate
from backend.shared.exceptions import ConflictError


class IdentityService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    async def register(self, data: UserCreate) -> User:
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise ConflictError("Email already registered.")
        user = User(
            email=data.email,
            hashed_password=self._hash(data.password),
        )
        return await self.repo.create(user)

    def _hash(self, password: str) -> str:
        # Placeholder — replace with passlib or bcrypt before production.
        return f"hashed:{password}"
