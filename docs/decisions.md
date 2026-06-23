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
