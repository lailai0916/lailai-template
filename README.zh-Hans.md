<div align="center">
  <h1>lailai-template</h1>
  <p><a href="README.md">English</a> · <strong>简体中文</strong></p>
  <p>
    <img src="https://img.shields.io/github/actions/workflow/status/lailai0916/lailai-template/ci.yml?branch=main&style=flat-square" />
    <img src="https://img.shields.io/github/last-commit/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/languages/top/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/repo-size/lailai0916/lailai-template?style=flat-square" />
    <img src="https://img.shields.io/github/license/lailai0916/lailai-template?style=flat-square" />
  </p>
</div>

## 项目简介

开箱即用的 GitHub 仓库模板，内含双语文档、runtime-neutral Agent 项目说明、协作表单与
严格的初始化检查点。

## 项目特性

📄 **双语 README** —— 居中的项目标识、语言导航与真实徽章。中英文内容完整对等，
项目结构树确定性对齐。

🗺️ **Agent 项目地图** —— 以 `AGENTS.md` 为单一真源，局部规则按路径拆分，runtime 只保留
常数大小的兼容入口。

📮 **GitHub 协作** —— 中英双语 Issue 表单、PR 自查清单与私密漏洞报告说明。

🧹 **仓库默认项** —— Git 属性、忽略规则、MIT 许可协议，以及占位内容与 GitHub About
元数据的显式清理检查。

🧪 **初始化检查** —— 无依赖检查仓库身份、README 徽章与 Agent 入口。
同时拦截未替换的占位内容和生成式署名。

## 快速开始

点击 **Use this template**，再按顺序完成初始化：

```bash
# 替换全部模板占位符与旧仓库路径。
rg -n 'TODO|<owner>|<repo>|One paragraph|Replace with' .

# 确认没有误留模板身份。
rg -n 'lailai-template|lailai0916/lailai-template' . --glob '!README*'

# 验证初始化结果与仓库身份。
python3 scripts/check_repository.py

# 运行新项目在 AGENTS.md 中记录的检查命令。
```

将 `README.md` 与 `README.zh-Hans.md` 重写为严格镜像，替换徽章路径，补完
`AGENTS.md`，删除无用模板，再设置 GitHub About 的 description、homepage 与
$3\sim8$ 个准确的小写 topics。这些是完成条件，不是可选善后。

## 项目结构

```bash
lailai-template/
├── .github/                    # 协作与安全表单
├── docs/                       # 项目文档占位目录
└── scripts/                    # 初始化完整性检查
```

## 许可协议

本项目代码采用 [MIT 许可协议](https://github.com/lailai0916/tools/blob/main/LICENSE)。
