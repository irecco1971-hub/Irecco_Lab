# Business logic for the support module.

import uuid

from backend.modules.support.models import Ticket, TicketMessage, TicketStatus
from backend.modules.support.repository import SupportRepository
from backend.modules.support.schemas import (
    TicketCreate,
    TicketMessageCreate,
    TicketStatusUpdate,
)
from backend.shared.exceptions import NotFoundError


class SupportService:
    def __init__(self, repo: SupportRepository) -> None:
        self.repo = repo

    async def list_tickets(self) -> list[Ticket]:
        return await self.repo.get_all()

    async def get_ticket(self, ticket_id: uuid.UUID) -> Ticket:
        ticket = await self.repo.get_by_id(ticket_id)
        if not ticket:
            raise NotFoundError(f"Ticket {ticket_id} not found.")
        return ticket

    async def open_ticket(self, user_id: uuid.UUID, data: TicketCreate) -> Ticket:
        ticket = Ticket(
            user_id=user_id,
            product_id=data.product_id,
            subject=data.subject,
            status=TicketStatus.open,
        )
        ticket = await self.repo.create_ticket(ticket)
        message = TicketMessage(ticket_id=ticket.id, author_id=user_id, body=data.body)
        await self.repo.create_message(message)
        return ticket

    async def update_status(self, ticket_id: uuid.UUID, data: TicketStatusUpdate) -> Ticket:
        ticket = await self.get_ticket(ticket_id)
        ticket.status = data.status
        return await self.repo.update_ticket(ticket)

    async def list_messages(self, ticket_id: uuid.UUID) -> list[TicketMessage]:
        await self.get_ticket(ticket_id)
        return await self.repo.get_messages(ticket_id)

    async def add_message(
        self, ticket_id: uuid.UUID, author_id: uuid.UUID, data: TicketMessageCreate
    ) -> TicketMessage:
        await self.get_ticket(ticket_id)
        message = TicketMessage(ticket_id=ticket_id, author_id=author_id, body=data.body)
        return await self.repo.create_message(message)
