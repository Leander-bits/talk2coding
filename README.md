# Agentic Coding 通用模板

简体中文 | [English](README.en.md)

## 介绍

供 Codex 与 GitHub Copilot 共用的项目模板：统一开发规则、代码组织、验证和授权边界。你用对话提出需求和确认方案，AI 负责代码及相关文档的填写与维护。

通用规则适用于不同技术栈；Python 项目额外遵循流程函数、禁止嵌套函数、`main()` 入口及按复杂度拆文件的约定。两种工具使用同一份核心规则，由脚本生成 Copilot 副本。

开始项目及后续改动，按 [分步提示词](docs/PROMPTS.md) 操作。上传与复用见 [GitHub 指南](docs/GITHUB.md)，设计依据见 [参考资料](docs/REFERENCES.md)。模板采用 [MIT 许可证](LICENSE)。规则是工作约定，不能替代客户端权限、沙箱和 CI。

## 结构

```text
.
├── AGENTS.md                         # 核心规则的唯一维护源
├── README.md / README.en.md          # 中文 / 英文介绍，链接切换
├── LICENSE                          # MIT
├── .editorconfig                    # 编码、缩进和换行
├── .gitattributes                   # Git 文本换行
├── .gitignore                       # 本地秘密和生成文件
├── .github/
│   ├── copilot-instructions.md      # AI 从 AGENTS.md 生成
│   ├── pull_request_template.md     # PR 目的、验证和风险
│   └── workflows/template-checks.yml # 检查两份规则一致
├── scripts/sync_instructions.py     # 改规则时由 AI 执行
└── docs/
    ├── PROMPTS.md                   # 新项目、测试、修复和迭代提示词
    ├── PROJECT.md                   # 项目目标、范围和约束
    ├── DEVELOPMENT.md               # 实际命令、环境和验证
    ├── ARCHITECTURE.md              # 入口、结构和重要决策
    ├── TASK_TEMPLATE.md             # 复杂任务记录模板
    ├── GITHUB.md                    # 上传与创建新项目
    └── REFERENCES.md                # 来源与设计取舍
```

尚未预设应用目录或技术栈。AI 在实现项目时确定单文件或多文件结构，必要时创建 `docs/tasks/` 保存任务记录。
