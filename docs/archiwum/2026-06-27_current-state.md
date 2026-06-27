# Irecco Lab — Current State

## Current Phase
Core platform implementation — sesja 1 (1.1–1.15) zakończona.
Wszystkie moduły core backendu mają działający kod, migracje i testy jednostkowe.

## Immediate Goal
Ukończyć moduł `docs` (sesja 1.17–1.18), a następnie przejść do sesji 2 — moduł MillWork.

## Current Product Priority
MillWork jest pierwszym produktem kotwiczącym.
Core platform jest gotowy do przyjęcia pierwszego modułu produktowego.

## Zrealizowane (sesja 1)

### Infrastruktura
- Python modular monolith (FastAPI + SQLAlchemy async + PostgreSQL)
- Docker Compose z healthcheck na bazie danych
- Alembic — migracje (0001–0005)
- pyproject.toml, Makefile (`make up`, `make migrate`, `make test`, `make lint`)
- `.gitattributes` (LF), `.gitignore` (w tym `.tmp.driveupload/`)
- `.claude/settings.json` — hook Stop → auto-commit

### Moduły core (każdy: models, schemas, repository, service, router, testy)
| Moduł | Endpointy | Testy |
|---|---|---|
| `identity` | `/identity/register`, `/login`, `/me` | ✅ 6 testów |
| `products` | CRUD `/products/` | ✅ 10 testów |
| `beta_program` | `/products/{id}/beta/join`, list, status | ✅ 7 testów |
| `support` | tickety + wiadomości | ✅ 11 testów |
| `notifications` | list, mark-read | ⬜ testy pending |
| `docs` | — | ⬜ do zaimplementowania |

### Shared
- `base_model.py` — Base SQLAlchemy
- `dependencies.py` — `get_db`, `get_current_user`
- `exceptions.py` — `NotFoundError`, `PermissionDeniedError`, `ConflictError`
- `security.py` — `hash_password`, `verify_password`, `create_access_token`, `decode_access_token`

### Migracje
| # | Tabela |
|---|---|
| 0001 | `users` |
| 0002 | `products` |
| 0003 | `waitlist_entries` |
| 0004 | `support_tickets`, `support_ticket_messages` |
| 0005 | `notifications` |

## Następne kroki
1. Testy `NotificationService` (sesja 1.16)
2. Moduł `docs` — model, service, router, migracja (sesja 1.17)
3. Testy `DocsService` (sesja 1.18)
4. Zamknięcie sesji 1, aktualizacja decisions.md
5. Sesja 2 — moduł MillWork (plugin SketchUp dla stolarzy CNC)
