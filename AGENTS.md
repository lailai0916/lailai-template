# Repository instructions

Runtime-neutral guidance for AI coding agents in this repo. This file is the always-loaded
**map**; deep per-area detail lives in `.agents/rules/*.md`. Before editing a path, read the
rules whose `paths` glob matches it.

## Personal style — defer to lailai.skill

lailai's **general, cross-project** style — Chinese voice and wording, Markdown, LaTeX math,
OI C++, design principles (统一·简约·现代), who he is and how he decides — lives in the
**lailai.skill** submodule at [`.agents/skills/lailai-skill/`](.agents/skills/lailai-skill/SKILL.md).
Read its `SKILL.md`, then the relevant `references/` / `profile/`, for any task touching voice,
writing, code, or design.

**This repo's `.agents/` holds portable project config.** It does not duplicate the general
rules; where `.agents/rules/*.md` covers only the project-specific slice, it points to the
skill for the rest. Runtime-specific directories are compatibility adapters only.

Init the submodule after cloning: `git submodule update --init`. Update it later with
`git submodule update --remote .agents/skills/lailai-skill`.

## Project

<!-- One paragraph: what this is, stack, runtime versions, how it's deployed. -->
<!-- e.g. Source for X — Node >=20, deployed to Y via GitHub Actions. -->

## Commands

```bash
# The commands a contributor actually runs. Delete this block if trivial.
# npm run dev      # dev server
# npm run build    # production build
# npm run check    # the gate before every commit
```

## Rules index

<!--
  Path-scoped detail — read each file whose paths glob matches the files being changed.
  Add a row per .agents/rules/*.md. Delete this table if the repo has no project-specific rules yet.
-->

| Rule                              | Scope           | Covers                   |
| --------------------------------- | --------------- | ------------------------ |
| <!-- .agents/rules/example.md --> | <!-- src/** --> | <!-- what it governs --> |

## Conventions

<!-- Project-specific rules only. General taste (精益求精, edit-don't-rewrite, comment the *why*, no AI-tells) lives in the skill's profile/ and references/. -->

- **Verify before committing** — the project's check gate must exit clean.
- **Small changes go straight to `main`.** Reserve branches / PRs for substantial multi-file work.

## Keep Agent guidance current

Update `AGENTS.md` and applicable `.agents/rules/` in the same change that invalidates them.
Record **durable** conventions, not transient task state; verify against the actual code before
writing, since stale guidance is worse than none. `CLAUDE.md`, `.claude/rules`, and
`.claude/skills` are compatibility pointers, not additional sources of truth.
