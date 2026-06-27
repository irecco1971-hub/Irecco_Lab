# Irecco Lab — Git Session-Close Automation

## Goal
Automatically create a local Git checkpoint at the end of a Claude Code session.
Do not auto-push.

## Intent
The repository should always preserve meaningful progress without requiring manual commit discipline after every session.

## Expected Behavior
- run only when the task or session ends
- commit only if there are file changes
- avoid empty commits
- never push automatically

## Suggested Implementation Direction
Use Claude Code project rules plus a local hook in `.claude/settings.json` or an equivalent session-end command.
The hook should:
1. detect changes
2. run `git add -A`
3. create a conventional commit message
4. skip commit if nothing changed

## Suggested Message Pattern
`type: short summary`

Examples:
- `docs: add initial Irecco Lab architecture package`
- `feat: add beta access module skeleton`
- `refactor: separate product shell from core routes`

## Safety Rule
If the working tree contains broken experimental code that should not be checkpointed yet, the session should stop before commit or the commit should be manually overridden.
