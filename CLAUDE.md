# Irecco Lab — Claude Code Project Context

## What & Why
Irecco Lab is an umbrella product studio for multiple distinct software products created by one independent developer.
The goal is to build a reusable open-source-first platform foundation that supports many products, while shipping one revenue-focused product at a time.
MillWork is the first anchor product.

## Stack
- Backend: Python modular monolith
- Primary languages: Python, JavaScript/TypeScript, Markdown
- Version control: Git
- Docs: Markdown files in `docs/`
- Product delivery workflow: Chat planning -> Claude Code implementation
- Philosophy: open-source-first, low-cost, self-hosted where practical

## Modules
- Core platform: users, roles, products, docs, beta access, support, notifications
- Product modules: each product has its own domain, terminology, UI, and workflows
- First product: MillWork
- Future model: modular monolith now, service extraction later only if justified

## Git Rules
- Commit automatically at session-close or end-of-task checkpoint
- Do not auto-push
- Commit only when there are actual file changes
- Prefer conventional commit prefixes: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`
- Commit message should briefly describe what changed and why

## Working Rules
- One clear task per session
- Do not redesign the whole platform in one pass
- Build the smallest reusable foundation that helps the current product ship faster
- Reuse only what is truly cross-product
- Keep product-specific logic out of the shared core unless reuse is proven
- Prefer separate `.md` files with one responsibility each
- Update `docs/current-state.md` after meaningful progress
- Update `docs/decisions.md` when an architectural or workflow decision is made

## What NOT to do
- Do not start with microservices
- Do not build a giant all-purpose platform before the first product earns money
- Do not mix product-specific terminology into global core modules
- Do not create hidden cross-module dependencies
- Do not allow direct cross-module SQL reads as a shortcut
- Do not auto-push commits
- Do not make large multi-topic sessions when a smaller scoped session is possible

## Context Files
- `docs/architecture.md`
- `docs/product-map.md`
- `docs/core-vs-product.md`
- `docs/backend-structure.md`
- `docs/current-state.md`
- `docs/decisions.md`
- `docs/claude-code-workflow.md`
