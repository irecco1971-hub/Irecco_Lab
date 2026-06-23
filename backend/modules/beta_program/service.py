# Business logic for the beta_program module.

import uuid

from backend.modules.beta_program.models import WaitlistEntry, WaitlistStatus
from backend.modules.beta_program.repository import WaitlistRepository
from backend.modules.beta_program.schemas import WaitlistJoin, WaitlistStatusUpdate
from backend.shared.exceptions import ConflictError, NotFoundError


class BetaProgramService:
    def __init__(self, repo: WaitlistRepository) -> None:
        self.repo = repo

    async def list_entries(self, product_id: uuid.UUID) -> list[WaitlistEntry]:
        return await self.repo.get_all_for_product(product_id)

    async def join(self, product_id: uuid.UUID, data: WaitlistJoin) -> WaitlistEntry:
        existing = await self.repo.get_by_email_and_product(data.email, product_id)
        if existing:
            raise ConflictError("This email is already on the waitlist for this product.")
        entry = WaitlistEntry(
            product_id=product_id,
            email=data.email,
            status=WaitlistStatus.pending,
        )
        return await self.repo.create(entry)

    async def update_status(
        self, entry_id: uuid.UUID, data: WaitlistStatusUpdate
    ) -> WaitlistEntry:
        entry = await self.repo.get_by_id(entry_id)
        if not entry:
            raise NotFoundError(f"Waitlist entry {entry_id} not found.")
        entry.status = data.status
        return await self.repo.update(entry)
