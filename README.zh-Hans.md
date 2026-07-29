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

## 项目简介

通用 GitHub 起步模板。用它新建的仓库开箱自带跨 Agent 通用配置、以 submodule 引入的
lailai-skill 赛博分身，以及常用的 Git 基础文件。

## 项目特性

🧠 **内置 lailai-skill** —— 跨项目风格分身以 submodule 引入 `.agents/skills/`，
`AGENTS.md` 直接 defer 过去，而非复制规则。

🗂️ **多 Agent 脚手架** —— `AGENTS.md` 是项目规则真源，`.agents/rules/` 与
`.agents/skills/` 保存通用内容。`.claude/` 只保留常数个兼容入口与 Claude 专属设置。

📮 **GitHub 模板** —— 中英双语的 issue 表单、PR 清单与私密漏洞报告策略。

🧹 **合理默认** —— `.gitattributes`、`.gitignore` 与 MIT `LICENSE`。

## 快速开始

点 **Use this template**，然后：

```bash
# 初始化 lailai-skill 子模块
git submodule update --init

# 为你自己的项目重写 README.md / README.zh-Hans.md
```

## 项目结构

```bash
lailai-template/
├── .github/                        # GitHub 协作模板
│   ├── ISSUE_TEMPLATE/             # 双语 Issue 表单
│   ├── PULL_REQUEST_TEMPLATE.md    # PR 检查清单
│   └── SECURITY.md                 # 私密漏洞报告策略
└── docs/                           # 项目文档占位目录
```

模板不复制任何自己的风格规则。lailai-skill 是单一来源，以 submodule 引入、由
`AGENTS.md` defer 过去；各仓库的 `.agents/rules/` 只留自己的项目专属层。
Runtime 兼容层不会按 rule 或 skill 逐项复制。

## 许可协议

本项目代码采用 [MIT 许可协议](https://github.com/lailai0916/tools/blob/main/LICENSE)。
