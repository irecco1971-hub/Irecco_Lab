.PHONY: up down build logs shell migrate revision lint test test-local

# ── Docker ────────────────────────────────────────────────────────────────────

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f backend

shell:
	docker compose exec backend bash

# ── Database / Alembic ────────────────────────────────────────────────────────

migrate:
	docker compose exec backend alembic upgrade head

revision:
	@read -p "Message: " msg; \
	docker compose exec backend alembic revision --autogenerate -m "$$msg"

# ── Quality ───────────────────────────────────────────────────────────────────

lint:
	docker compose exec backend ruff check .

test:
	docker compose exec backend pytest

test-local:
	cd backend && python -m pytest
