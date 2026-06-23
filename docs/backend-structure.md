# Irecco Lab — Backend Structure

## Architecture Style
Use a Python modular monolith.
Keep domain logic separated from transport and persistence.
Design modules as future extraction candidates, but keep deployment monolithic for now.

## Proposed Structure

```text
irecco-lab/
├── CLAUDE.md
├── docs/
├── app/
│   ├── main.py
│   ├── config/
│   ├── shared/
│   ├── modules/
│   │   ├── identity/
│   │   ├── products/
│   │   ├── docs/
│   │   ├── beta_access/
│   │   ├── support/
│   │   ├── notifications/
│   │   ├── admin/
│   │   └── millwork/
│   └── tests/
├── scripts/
├── .claude/
└── .git/
```

## Rules for Modules
Each module should contain:
- domain models
- use cases / services
- repository layer
- API adapters / routers
- tests

## Dependency Rules
- A module may depend on shared utilities only if they are truly generic
- A module must not read another module’s tables directly as a shortcut
- Cross-module interaction should happen through public functions, service interfaces, or explicit application services
- Avoid a giant `shared` folder full of business logic

## Persistence Rules
- Logical data ownership belongs to one module
- Other modules should access that data through the owner module
- Prefer clear boundaries over clever shortcuts

## Extraction Readiness Rules
To keep future microservice extraction possible:
- avoid leaking ORM models between modules
- use DTOs or explicit service contracts
- keep transport-specific code near the edge
- keep business rules in plain Python where possible
