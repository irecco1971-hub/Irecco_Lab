# Irecco Lab

Umbrella product studio platform. Open-source-first, Python modular monolith.

**First product:** [MillWork](https://github.com/irecco1971-hub/Irecco_Lab) — SketchUp plugin for CNC woodworkers.

## Quick start

```bash
cp .env.example .env
docker compose up -d
```

API docs available at `http://localhost:8000/docs`.

## Structure

```
backend/        # FastAPI modular monolith
  modules/      # identity, products, beta_program, support, docs, notifications
  shared/       # base models, dependencies, exceptions
docs/           # project documentation and architecture decisions
frontend/       # placeholder
```

## Development docs

See [`docs/`](docs/) for architecture, decisions, and workflow guides.
