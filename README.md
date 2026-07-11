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

A general-purpose GitHub starter template. New repos come pre-wired with `.claude/` config, the lailai-skill cyber-twin as a submodule, and the usual editor / git hygiene.

## Features

🧠 **lailai-skill built in** — the cross-project style twin ships as a submodule; `CLAUDE.md` defers to it instead of copying rules.

🗂️ **`.claude/` scaffold** — shared `settings.json`, a project `CLAUDE.md` skeleton, and a path-scoped rule template.

📮 **GitHub templates** — bilingual issue forms and a PR checklist.

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
.claude/
├── skills/lailai-skill/         # submodule → lailai0916/lailai-skill
├── rules/example.md.template    # skeleton for a project-scoped rule
├── settings.json                # shared permissions / hooks
└── CLAUDE.md                    # project guide; style defers to lailai-skill
.github/
├── ISSUE_TEMPLATE/              # bug_report · feature_request
└── PULL_REQUEST_TEMPLATE.md     # PR checklist
```

The template copies no style rules of its own. lailai-skill is the single source, pulled in as a submodule and deferred to from `CLAUDE.md`; each repo's `.claude/rules/` holds only its own project-specific layer.

## License

Licensed under the [MIT License](LICENSE).
