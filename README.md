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

## Project Introduction

A general-purpose GitHub starter template. New repos come pre-wired with runtime-neutral
Agent configuration, the lailai-skill cyber-twin as a submodule, and the usual Git hygiene.

## Project Features

🧠 **lailai-skill built in** — the cross-project style twin ships under
`.agents/skills/` as a submodule; `AGENTS.md` defers to it instead of copying rules.

🗂️ **Multi-Agent scaffold** — `AGENTS.md` is the canonical project guide,
`.agents/rules/` and `.agents/skills/` are portable sources, and `.claude/` contains only
constant-size compatibility pointers plus Claude-specific settings.

📮 **GitHub templates** — bilingual issue forms, a PR checklist, and a private
vulnerability-reporting policy.

🧹 **Sensible defaults** — `.gitattributes`, `.gitignore`, and an MIT `LICENSE`.

## Getting Started

Click **Use this template**, then:

```bash
# Initialize the lailai-skill submodule
git submodule update --init

# Rewrite README.md / README.zh-Hans.md for your own project
```

## Project Structure

```bash
lailai-template/
├── .github/                        # GitHub collaboration templates
│   ├── ISSUE_TEMPLATE/             # Bilingual issue forms
│   ├── PULL_REQUEST_TEMPLATE.md    # Pull request checklist
│   └── SECURITY.md                 # Private vulnerability reporting
└── docs/                           # Project documentation placeholder
```

The template copies no style rules of its own. lailai-skill is the single source, pulled in
as a submodule and deferred to from `AGENTS.md`; each repo's `.agents/rules/` holds only its
own project-specific layer. Runtime adapters never copy rules or skills per item.

## License

This project's code is licensed under [MIT License](https://github.com/lailai0916/tools/blob/main/LICENSE).
