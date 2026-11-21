# 来源与设计依据

以下来源于 2026-11-18 查阅，模板于 2026-11-21 根据用户偏好精简。内容是设计归纳，不是官方统一标准；没有全文复制第三方规则或要求安装其工具。

## 官方来源

| 来源 | 借鉴 |
| --- | --- |
| [OpenAI：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 仓库规则及目录、全局、override 的发现差异 |
| [OpenAI：Harness engineering](https://openai.com/index/harness-engineering/) | 仓库保存可导航的项目知识，入口简洁 |
| [GitHub：仓库自定义指令](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)及[支持矩阵](https://docs.github.com/en/copilot/reference/custom-instructions-support) | 提供 Copilot 入口，区分客户端和功能支持 |
| [VS Code：Custom instructions reference](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference) | 链接不保证内容被加载，需检查实际指令与读取记录 |
| [Anthropic：Claude Code best practices](https://code.claude.com/docs/en/best-practices) | 精简常驻指令，给出验证方法，区分提示与强制约束 |

客户端行为可能变化。项目规则由客户端发现，不由模型名称决定；需要时明确读取文档和局部规则，不把文件存在视为已经生效。

## 开源与第三方实践

| 来源 | 借鉴与取舍 |
| --- | --- |
| [sammcj/agentic-coding](https://github.com/sammcj/agentic-coding) | 工具无关规则、小步执行与交接；不照搬插件、模型和多代理偏好 |
| [github/spec-kit](https://github.com/github/spec-kit) | 需求、方案、任务和验证衔接；不强制完整工具链 |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 分离需求、示例、资料与验证上下文；不照搬固定行数和效果倍数 |
| [Simon Willison：First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/) | 先建立相关测试基线，按风险调整范围 |
| [HumanLayer：Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) | 常驻规则简洁，详细资料按需读取；不采用固定规则数量阈值 |

## 本模板的选择

- AI 默认填写并更新相关项目文档，用户通过对话提供需求和确认；不要求手工编辑 Markdown。
- 根规则为唯一维护源，生成完整 Copilot 副本，避免依赖跨文件引用展开；AI 改规则后同步，CI 只检查一致性。
- 流程函数、禁止嵌套函数、Python main()、按复杂度选择单文件或多文件，来自用户的代码组织偏好；不是所有官方文档要求的统一规范。
- 按需使用 class 与抽象类，不绑定框架、模型 ID、覆盖率或文件行数。
- 项目需求、实际命令、结构决策、具体任务各有位置；流程说明合并到提示词，决策合并到架构文档，减少重复文件。
- 高影响动作明确授权，已有授权不重复询问；规则不能替代沙箱、客户端权限、秘密管理和 CI。

## CI 来源与许可证

工作流使用只读权限，固定到此前已核对的上游提交：

- [actions/checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1)：`3d3c42e5aac5ba805825da76410c181273ba90b1`。
- [actions/setup-python v7.1.0](https://github.com/actions/setup-python/releases/tag/v7.1.0)：`6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`。

本模板使用 [MIT](../LICENSE)。后续直接复用第三方代码时应遵守其原许可证；新增项目内容可选择合适许可证并保留所复用内容的声明。
