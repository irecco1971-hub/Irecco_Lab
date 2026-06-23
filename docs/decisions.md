# Irecco Lab — Decisions

## 2026-06-22 — Umbrella brand model
Decision: Irecco Lab is the umbrella studio brand, while products can have their own positioning.
Why: Products may serve very different audiences and should not be forced into one marketing voice.

## 2026-06-22 — First product anchor
Decision: MillWork is the first anchor product.
Why: The platform needs one real product to validate decisions and drive early revenue.

## 2026-06-22 — Architecture style
Decision: Start with a Python modular monolith.
Why: It is more realistic for a solo developer and keeps future service extraction possible without paying the cost of distributed systems now.

## 2026-06-22 — Documentation-first workflow
Decision: Project context is maintained in Markdown files designed for Claude Code.
Why: This improves continuity, reduces ambiguity, and supports incremental implementation sessions.

## 2026-06-22 — Git workflow
Decision: Use Git with automatic session-close commits, but no automatic push.
Why: This preserves history and checkpoints without risking accidental remote publication.

## 2026-06-23 — Auth via JWT (not external provider yet)
Decision: Identity module uses passlib/bcrypt + python-jose JWT — no external auth provider (e.g. Keycloak/authentik) in session 1.
Why: Keeps the platform self-contained and runnable without external services. External auth can be layered on later when multi-product SSO becomes a real need.

## 2026-06-23 — Superuser flag as first authorization mechanism
Decision: `User.is_superuser` is the only authorization gate for admin operations in session 1.
Why: Roles and permissions can be added in a dedicated session once MillWork drives a concrete use case. Premature role design risks building the wrong model.

## 2026-06-23 — NotificationService.send() has no HTTP endpoint
Decision: Notifications are dispatched by calling `NotificationService.send()` directly from other services, not via a public API.
Why: Prevents external callers from sending arbitrary notifications. Only internal platform events (ticket status change, beta invite, etc.) should trigger notifications.

## 2026-06-23 — docs/ folder moved out of project root
Decision: All Markdown context files moved from project root to `docs/`.
Why: Keeps the root clean — only `CLAUDE.md`, `README.md`, and config files at top level.

## 2026-06-23 — .tmp.driveupload/ added to .gitignore
Decision: Google Drive temp upload folder excluded from git tracking.
Why: Project directory is synced via Google Drive, which creates temp files that must not enter the repo.
