#!/usr/bin/env python3

import os
import re
import subprocess
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_REPOSITORY = "lailai0916/lailai-template"


def repository_slug() -> Optional[str]:
    slug = os.environ.get("GITHUB_REPOSITORY") or os.environ.get("REPOSITORY_SLUG")
    if slug:
        return slug.removesuffix(".git").strip("/")

    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    remote = result.stdout.strip()
    match = re.search(r"github\.com(?::|/)([^/]+/[^/]+?)(?:\.git)?$", remote)
    return match.group(1) if match else None


def check_readme(path: Path, slug: str, chinese: bool) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    language_nav = (
        '<p><a href="README.md">English</a> · <strong>简体中文</strong></p>'
        if chinese
        else '<p><strong>English</strong> · <a href="README.zh-Hans.md">简体中文</a></p>'
    )
    required = (
        '<div align="center">',
        language_nav,
        f"github/actions/workflow/status/{slug}/ci.yml?branch=main",
        f"github/last-commit/{slug}",
        f"github/languages/top/{slug}",
        f"github/repo-size/{slug}",
        f"github/license/{slug}",
    )
    for marker in required:
        if marker not in text:
            errors.append(f"{path.name}: missing {marker}")

    heading = "## 项目结构" if chinese else "## Project Structure"
    if heading not in text:
        errors.append(f"{path.name}: missing {heading}")
        return errors
    section = text.split(heading, 1)[1]
    match = re.search(r"```bash\n(.*?)\n```", section, re.DOTALL)
    if not match:
        errors.append(f"{path.name}: missing bash structure tree")
        return errors
    for line in match.group(1).splitlines():
        if "#" in line and line.index("#") != 32:
            errors.append(f"{path.name}: structure comment is not at index 32: {line}")
    return errors


def tracked_text() -> list[tuple[str, str]]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    files = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        rel = raw.decode()
        try:
            files.append((rel, (ROOT / rel).read_text(encoding="utf-8")))
        except (UnicodeDecodeError, IsADirectoryError):
            pass
    return files


def main() -> int:
    errors = []
    required_files = (
        ".github/workflows/ci.yml",
        "AGENTS.md",
        "CLAUDE.md",
        "LICENSE",
        "README.md",
        "README.zh-Hans.md",
        "scripts/check_repository.py",
    )
    for rel in required_files:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    if (ROOT / "CLAUDE.md").read_text(encoding="utf-8").strip() != "@AGENTS.md":
        errors.append("CLAUDE.md must contain only @AGENTS.md")

    slug = repository_slug()
    if not slug:
        errors.append("cannot determine owner/repository; set REPOSITORY_SLUG")
    else:
        errors.extend(check_readme(ROOT / "README.md", slug, False))
        errors.extend(check_readme(ROOT / "README.zh-Hans.md", slug, True))

        if slug == TEMPLATE_REPOSITORY:
            if not (ROOT / ".agents/rules/example.md.template").exists():
                errors.append("missing template rule example")
        else:
            for rel in ("README.md", "README.zh-Hans.md", "AGENTS.md"):
                if "lailai-template" in (ROOT / rel).read_text(encoding="utf-8"):
                    errors.append(f"{rel}: template identity was not replaced")
            if (ROOT / ".agents/rules/example.md.template").exists():
                errors.append("remove or rename .agents/rules/example.md.template")
            agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
            for marker in ("<!-- One paragraph", "<!-- Add one row"):
                if marker in agents:
                    errors.append(f"AGENTS.md: unresolved placeholder: {marker}")

    forbidden = (
        "Co-" + "Authored-By",
        "Generated " + "with",
        "Generated " + "by",
        "AI-" + "generated",
    )
    for rel, text in tracked_text():
        for marker in forbidden:
            if marker.lower() in text.lower():
                errors.append(f"{rel}: forbidden attribution: {marker}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"Repository template checks passed for {slug}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
