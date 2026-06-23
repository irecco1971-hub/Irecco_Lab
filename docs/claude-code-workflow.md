# Irecco Lab — Claude Code Workflow

## Principle
Claude Code should work on one focused task per session.
Documentation defines the task boundaries.

## Session Pattern
1. Read `CLAUDE.md`
2. Read relevant docs in `docs/`
3. Work on one scoped task only
4. Update affected docs if architecture or state changed
5. Create a session-close Git commit if files changed

## Task Scope Rule
A good session:
- touches one small feature
- updates only the relevant files
- ends with a testable result
- produces a clean commit checkpoint

A bad session:
- changes many unrelated modules
- rewrites architecture and implementation together
- mixes planning, backend, UI, and deployment in one pass

## Documentation Update Rule
Update these files when needed:
- `docs/current-state.md` after meaningful progress
- `docs/decisions.md` after decisions
- `docs/architecture.md` when boundaries change
- `docs/core-vs-product.md` when a feature is reclassified

## Git Rule
At session-close:
- check whether files changed
- stage all relevant changes
- create one meaningful commit
- do not auto-push

## Suggested Commit Prefixes
- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation changes
- `refactor:` code restructuring without behavior change
- `chore:` maintenance or tooling

## Auto-Commit Intent
Claude Code should be configured so that session-close creates a commit checkpoint automatically if there are local changes.
This should happen only after the task is coherent enough to preserve in history.
