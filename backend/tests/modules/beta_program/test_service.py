import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from backend.modules.beta_program.models import WaitlistEntry, WaitlistStatus
from backend.modules.beta_program.schemas import WaitlistJoin, WaitlistStatusUpdate
from backend.modules.beta_program.service import BetaProgramService
from backend.shared.exceptions import ConflictError, NotFoundError


def _make_repo(
    *,
    entries: list[WaitlistEntry] | None = None,
    by_id: WaitlistEntry | None = None,
    by_email: WaitlistEntry | None = None,
) -> MagicMock:
    repo = MagicMock()
    repo.get_all_for_product = AsyncMock(return_value=entries or [])
    repo.get_by_id = AsyncMock(return_value=by_id)
    repo.get_by_email_and_product = AsyncMock(return_value=by_email)
    repo.create = AsyncMock(side_effect=lambda e: e)
    repo.update = AsyncMock(side_effect=lambda e: e)
    return repo


def _make_entry(**kwargs) -> WaitlistEntry:
    defaults = dict(
        id=uuid.uuid4(),
        product_id=uuid.uuid4(),
        email="tester@example.com",
        status=WaitlistStatus.pending,
    )
    return WaitlistEntry(**{**defaults, **kwargs})


PRODUCT_ID = uuid.uuid4()


class TestListEntries:
    async def test_returns_entries_for_product(self):
        entries = [_make_entry(), _make_entry(email="other@example.com")]
        repo = _make_repo(entries=entries)
        result = await BetaProgramService(repo).list_entries(PRODUCT_ID)
        assert result == entries
        repo.get_all_for_product.assert_awaited_once_with(PRODUCT_ID)


class TestJoin:
    async def test_creates_entry_for_new_email(self):
        repo = _make_repo(by_email=None)
        data = WaitlistJoin(email="new@example.com")
        entry = await BetaProgramService(repo).join(PRODUCT_ID, data)
        repo.create.assert_awaited_once()
        assert entry.email == "new@example.com"
        assert entry.status == WaitlistStatus.pending

    async def test_raises_conflict_for_duplicate_email(self):
        repo = _make_repo(by_email=_make_entry())
        data = WaitlistJoin(email="tester@example.com")
        with pytest.raises(ConflictError):
            await BetaProgramService(repo).join(PRODUCT_ID, data)
        repo.create.assert_not_awaited()


class TestUpdateStatus:
    async def test_updates_status_to_invited(self):
        entry = _make_entry(status=WaitlistStatus.pending)
        repo = _make_repo(by_id=entry)
        data = WaitlistStatusUpdate(status=WaitlistStatus.invited)
        result = await BetaProgramService(repo).update_status(entry.id, data)
        assert result.status == WaitlistStatus.invited
        repo.update.assert_awaited_once()

    async def test_updates_status_to_rejected(self):
        entry = _make_entry(status=WaitlistStatus.pending)
        repo = _make_repo(by_id=entry)
        data = WaitlistStatusUpdate(status=WaitlistStatus.rejected)
        result = await BetaProgramService(repo).update_status(entry.id, data)
        assert result.status == WaitlistStatus.rejected

    async def test_raises_not_found_for_missing_entry(self):
        repo = _make_repo(by_id=None)
        with pytest.raises(NotFoundError):
            await BetaProgramService(repo).update_status(
                uuid.uuid4(), WaitlistStatusUpdate(status=WaitlistStatus.invited)
            )
