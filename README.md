<div align="center">
  <h1>lailai-template</h1>
  <p>English | <a href="README.zh-Hans.md">简体中文</a></p>
  <p>
    <img
      src="https://img.shields.io/github/last-commit/lailai0916/lailai-template?style=flat-square"
    />
    <img
      src="https://img.shields.io/github/languages/top/lailai0916/lailai-template?style=flat-square"
    />
    <img
      src="https://img.shields.io/github/repo-size/lailai0916/lailai-template?style=flat-square"
    />
    <img
      src="https://img.shields.io/github/license/lailai0916/lailai-template?style=flat-square"
    />
  </p>
</div>

A general-purpose GitHub starter template. New repos come pre-wired with runtime-neutral
Agent configuration, the lailai-skill cyber-twin as a submodule, and the usual editor / git
hygiene.

## Features

🧠 **lailai-skill built in** — the cross-project style twin ships under
`.agents/skills/` as a submodule; `AGENTS.md` defers to it instead of copying rules.

🗂️ **Multi-Agent scaffold** — `AGENTS.md` is the canonical project guide,
`.agents/rules/` and `.agents/skills/` are portable sources, and `.claude/` contains only
constant-size compatibility pointers plus Claude-specific settings.

📮 **GitHub templates** — bilingual issue forms, a PR checklist, and a private
vulnerability-reporting policy.

🧹 **Sensible defaults** — `.editorconfig`, `.gitattributes`, `.gitignore`, MIT `LICENSE`.

## Getting started

Click **Use this template**, then:

```bash
# Initialize the lailai-skill submodule
git submodule update --init

# Rewrite README.md / README.zh-Hans.md for your own project
```

## Structure

```text
AGENTS.md                         # canonical project instructions
CLAUDE.md                         # Claude compatibility import → AGENTS.md
.agents/
├── skills/lailai-skill/         # submodule → lailai0916/lailai-skill
└── rules/example.md.template    # skeleton for a project-scoped rule
.claude/
├── skills -> ../.agents/skills  # one compatibility pointer
├── rules -> ../.agents/rules    # one compatibility pointer
└── settings.json                # Claude-specific permissions / hooks
.github/
├── ISSUE_TEMPLATE/              # bug_report · feature_request
├── PULL_REQUEST_TEMPLATE.md     # PR checklist
└── SECURITY.md                  # private vulnerability reporting
```

The template copies no style rules of its own. lailai-skill is the single source, pulled in
as a submodule and deferred to from `AGENTS.md`; each repo's `.agents/rules/` holds only its
own project-specific layer. Runtime adapters never copy rules or skills per item.

## License

Licensed under the [MIT License](LICENSE).
