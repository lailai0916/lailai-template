# Repository instructions

Runtime-neutral guidance for AI coding agents in this repository. This file is the always-loaded
project map; path-specific detail belongs in `.agents/rules/*.md`.

## Template initialization

This repository is a ready-to-use template, not a source of broad personal or organization-wide
policy. After creating a repository from it, complete these items before feature work:

1. Replace the project description, commands, rules index, and conventions below.
2. Rewrite both READMEs, including the centered title, language navigation, real badges,
   introduction, features, copyable setup, aligned structure tree, and license section.
3. Replace every badge owner/repository path and remove every placeholder or unused template.
4. Set the GitHub About description, homepage, and $3\sim8$ accurate lowercase topics.
5. Add only durable project-specific rules under `.agents/rules/`; delete the example if unused.
6. Run `python3 scripts/check_repository.py`, then the project's actual check gate recorded below.

Internal Agent guidance in the generated repository has priority for that repository's local
behavior. Keep runtime-specific files as constant-size compatibility adapters, not duplicate
instruction sources.

## Project

<!-- One paragraph: what this is, stack, supported runtime versions, and deployment target. -->

## Commands

```bash
python3 scripts/check_repository.py # Validate template initialization and repository identity.
# Replace with commands contributors actually run. Delete unused lines.
# npm run dev
# npm run build
# npm run check
```

## Rules index

<!-- Add one row per active .agents/rules/*.md; delete the table if none exist. -->

| Rule | Scope | Covers |
| --- | --- | --- |
| <!-- .agents/rules/example.md --> | <!-- src/** --> | <!-- durable local behavior --> |

## Conventions

- Verify changes with the project's documented check gate before committing.
- Keep `scripts/check_repository.py` in the initial CI gate; extend the workflow with project checks.
- Preserve unrelated user changes and keep each change coherent.
- Update `AGENTS.md` and matching path rules in the same change that invalidates them.

`AGENTS.md` is canonical. `CLAUDE.md` is only a compatibility import; `.claude/` may hold
runtime-specific settings but never a second copy of these rules.
