import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from backend.modules.support.models import Ticket, TicketMessage, TicketStatus
from backend.modules.support.schemas import (
    TicketCreate,
    TicketMessageCreate,
    TicketStatusUpdate,
)
from backend.modules.support.service import SupportService
from backend.shared.exceptions import NotFoundError


def _make_repo(
    *,
    tickets: list[Ticket] | None = None,
    ticket: Ticket | None = None,
    messages: list[TicketMessage] | None = None,
) -> MagicMock:
    repo = MagicMock()
    repo.get_all = AsyncMock(return_value=tickets or [])
    repo.get_by_id = AsyncMock(return_value=ticket)
    repo.create_ticket = AsyncMock(side_effect=lambda t: t)
    repo.update_ticket = AsyncMock(side_effect=lambda t: t)
    repo.get_messages = AsyncMock(return_value=messages or [])
    repo.create_message = AsyncMock(side_effect=lambda m: m)
    return repo


def _make_ticket(**kwargs) -> Ticket:
    defaults = dict(
        id=uuid.uuid4(),
        product_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        subject="Plugin crashes on export",
        status=TicketStatus.open,
    )
    return Ticket(**{**defaults, **kwargs})


def _make_message(**kwargs) -> TicketMessage:
    defaults = dict(
        id=uuid.uuid4(),
        ticket_id=uuid.uuid4(),
        author_id=uuid.uuid4(),
        body="Please describe the issue.",
    )
    return TicketMessage(**{**defaults, **kwargs})


USER_ID = uuid.uuid4()


class TestListTickets:
    async def test_returns_all_tickets(self):
        tickets = [_make_ticket(), _make_ticket(subject="Other issue")]
        repo = _make_repo(tickets=tickets)
        result = await SupportService(repo).list_tickets()
        assert result == tickets


class TestGetTicket:
    async def test_returns_ticket_when_found(self):
        ticket = _make_ticket()
        repo = _make_repo(ticket=ticket)
        result = await SupportService(repo).get_ticket(ticket.id)
        assert result == ticket

    async def test_raises_not_found_when_missing(self):
        repo = _make_repo(ticket=None)
        with pytest.raises(NotFoundError):
            await SupportService(repo).get_ticket(uuid.uuid4())


class TestOpenTicket:
    async def test_creates_ticket_and_first_message(self):
        repo = _make_repo(ticket=None)
        data = TicketCreate(subject="Export crash", body="Crashes every time.")
        ticket = await SupportService(repo).open_ticket(USER_ID, data)
        repo.create_ticket.assert_awaited_once()
        repo.create_message.assert_awaited_once()
        assert ticket.subject == "Export crash"
        assert ticket.status == TicketStatus.open
        assert ticket.user_id == USER_ID

    async def test_first_message_body_matches_input(self):
        repo = _make_repo(ticket=None)
        data = TicketCreate(subject="Bug", body="Detailed description.")
        await SupportService(repo).open_ticket(USER_ID, data)
        created_message = repo.create_message.call_args[0][0]
        assert created_message.body == "Detailed description."


class TestUpdateStatus:
    async def test_updates_status(self):
        ticket = _make_ticket(status=TicketStatus.open)
        repo = _make_repo(ticket=ticket)
        data = TicketStatusUpdate(status=TicketStatus.in_progress)
        result = await SupportService(repo).update_status(ticket.id, data)
        assert result.status == TicketStatus.in_progress

    async def test_raises_not_found_for_missing_ticket(self):
        repo = _make_repo(ticket=None)
        with pytest.raises(NotFoundError):
            await SupportService(repo).update_status(
                uuid.uuid4(), TicketStatusUpdate(status=TicketStatus.resolved)
            )


class TestListMessages:
    async def test_returns_messages_for_existing_ticket(self):
        ticket = _make_ticket()
        messages = [_make_message(ticket_id=ticket.id)]
        repo = _make_repo(ticket=ticket, messages=messages)
        result = await SupportService(repo).list_messages(ticket.id)
        assert result == messages

    async def test_raises_not_found_for_missing_ticket(self):
        repo = _make_repo(ticket=None)
        with pytest.raises(NotFoundError):
            await SupportService(repo).list_messages(uuid.uuid4())


class TestAddMessage:
    async def test_adds_message_to_existing_ticket(self):
        ticket = _make_ticket()
        repo = _make_repo(ticket=ticket)
        data = TicketMessageCreate(body="Follow-up question.")
        msg = await SupportService(repo).add_message(ticket.id, USER_ID, data)
        repo.create_message.assert_awaited_once()
        assert msg.body == "Follow-up question."
        assert msg.author_id == USER_ID

    async def test_raises_not_found_for_missing_ticket(self):
        repo = _make_repo(ticket=None)
        with pytest.raises(NotFoundError):
            await SupportService(repo).add_message(
                uuid.uuid4(), USER_ID, TicketMessageCreate(body="Hello.")
            )
