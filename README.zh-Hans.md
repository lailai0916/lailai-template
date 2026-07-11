<div align="center">
  <h1>lailai-template</h1>
  <p><a href="README.md">English</a> | 简体中文</p>
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

通用 GitHub 起步模板。用它新建的仓库开箱自带 `.claude/` 配置、以 submodule 引入的 lailai-skill 赛博分身，以及常用的编辑器 / git 卫生文件。

## 特性

🧠 **内置 lailai-skill** —— 跨项目风格分身以 submodule 引入，`CLAUDE.md` 直接 defer 过去，而非复制规则。

🗂️ **`.claude/` 脚手架** —— 共享 `settings.json`、项目级 `CLAUDE.md` 骨架，以及一个路径限定的规则模板。

📮 **GitHub 模板** —— 中英双语的 issue 表单与 PR 清单。

🧹 **合理默认** —— `.editorconfig`、`.gitattributes`、`.gitignore`、MIT `LICENSE`。

## 快速开始

点 **Use this template**，然后：

```bash
# 初始化 lailai-skill 子模块
git submodule update --init

# 为你自己的项目重写 README.md / README.zh-Hans.md
```

## 结构

```text
.claude/
├── skills/lailai-skill/         # submodule，指向 lailai0916/lailai-skill
├── rules/example.md.template    # 项目专属规则的骨架
├── settings.json                # 共享权限 / hooks
└── CLAUDE.md                    # 项目指引，风格 defer 到 lailai-skill
.github/
├── ISSUE_TEMPLATE/              # bug_report · feature_request
└── PULL_REQUEST_TEMPLATE.md     # PR 清单
```

模板不复制任何自己的风格规则。lailai-skill 是单一来源，以 submodule 引入、由 `CLAUDE.md` defer 过去；各仓库的 `.claude/rules/` 只留自己的项目专属层。

## 许可

采用 [MIT License](LICENSE)。
