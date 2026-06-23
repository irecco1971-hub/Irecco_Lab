# Data-access layer for the support module.

import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.modules.support.models import Ticket, TicketMessage


class SupportRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all(self) -> list[Ticket]:
        result = await self.db.execute(select(Ticket))
        return list(result.scalars().all())

    async def get_by_id(self, ticket_id: uuid.UUID) -> Ticket | None:
        return await self.db.get(Ticket, ticket_id)

    async def create_ticket(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        await self.db.commit()
        await self.db.refresh(ticket)
        return ticket

    async def update_ticket(self, ticket: Ticket) -> Ticket:
        await self.db.commit()
        await self.db.refresh(ticket)
        return ticket

    async def get_messages(self, ticket_id: uuid.UUID) -> list[TicketMessage]:
        result = await self.db.execute(
            select(TicketMessage).where(TicketMessage.ticket_id == ticket_id)
        )
        return list(result.scalars().all())

    async def create_message(self, message: TicketMessage) -> TicketMessage:
        self.db.add(message)
        await self.db.commit()
        await self.db.refresh(message)
        return message
