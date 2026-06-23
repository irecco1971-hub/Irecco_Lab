# Data-access layer for the beta_program module.

import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.beta_program.models import WaitlistEntry


class WaitlistRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all_for_product(self, product_id: uuid.UUID) -> list[WaitlistEntry]:
        result = await self.db.execute(
            select(WaitlistEntry).where(WaitlistEntry.product_id == product_id)
        )
        return list(result.scalars().all())

    async def get_by_id(self, entry_id: uuid.UUID) -> WaitlistEntry | None:
        return await self.db.get(WaitlistEntry, entry_id)

    async def get_by_email_and_product(
        self, email: str, product_id: uuid.UUID
    ) -> WaitlistEntry | None:
        result = await self.db.execute(
            select(WaitlistEntry).where(
                WaitlistEntry.email == email,
                WaitlistEntry.product_id == product_id,
            )
        )
        return result.scalar_one_or_none()

    async def create(self, entry: WaitlistEntry) -> WaitlistEntry:
        self.db.add(entry)
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def update(self, entry: WaitlistEntry) -> WaitlistEntry:
        await self.db.commit()
        await self.db.refresh(entry)
        return entry
