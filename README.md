<div align="center">
  <h1>lailai-template</h1>
  <p><strong>English</strong> · <a href="README.zh-Hans.md">简体中文</a></p>
  <p>
    <img src="https://img.shields.io/github/last-commit/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/languages/top/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/repo-size/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/license/lailai0916/lailai-template?style=flat-square" />
  </p>
</div>

## Project Introduction

A ready-to-use GitHub repository template with bilingual documentation, runtime-neutral Agent
guidance, collaboration forms, and strict initialization checkpoints.

## Project Features

📄 **Bilingual README** — Centered project identity, language navigation, real badges, mirrored
English and Simplified-Chinese content, and a deterministic structure tree.

🗺️ **Agent Project Map** — One canonical `AGENTS.md`, scoped local rules, and constant-size
runtime adapters without duplicated instructions.

📮 **GitHub Collaboration** — Bilingual issue forms, a pull-request checklist, and private
vulnerability-reporting guidance.

🧹 **Repository Defaults** — Git attributes, ignore rules, an MIT license, and explicit cleanup
checks for placeholders and GitHub About metadata.

## Getting Started

Click **Use this template**, then complete the initialization in order:

```bash
# Replace all template placeholders and old repository paths.
rg -n 'TODO|<owner>|<repo>|One paragraph|Replace with' .

# Confirm that no template identity remains accidentally.
rg -n 'lailai-template|lailai0916/lailai-template' . --glob '!README*'

# Run the new project's documented check gate.
```

Rewrite `README.md` and `README.zh-Hans.md` as exact mirrors. Replace badge paths, complete
`AGENTS.md`, remove unused templates, then set the GitHub About description, homepage, and
$3\sim8$ accurate lowercase topics. These are completion requirements, not optional cleanup.

## Project Structure

```bash
lailai-template/
├── .github/                    # Collaboration and security forms
└── docs/                       # Project documentation placeholder
```

## License

This project's code is licensed under [MIT License](https://github.com/lailai0916/tools/blob/main/LICENSE).
