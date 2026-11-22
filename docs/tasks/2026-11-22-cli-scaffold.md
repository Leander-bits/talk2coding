# 任务：建立 talk2coding 的 CLI 骨架

状态：骨架已实现并完成本地验证。日期为 2026-11-22。

## 目标与验收

- 要解决的问题、期望行为：将已确认的单文件架构落为可安装、可启动、可检查的 Windows CLI。
- 本次范围为骨架与检查配置。按住录音、模型推理和 DeepSeek 请求属于首版功能阶段。
- [x] 正常流程：项目虚拟环境可安装 wheel，CLI 能启动、显示帮助和枚举输入设备，双语 README 可切换。
- [x] 边界与失败情况：无依赖可看帮助，实际运行时缺依赖返回失败，设备筛选保留原编号，内存 WAV 解码可验证。

## 计划与授权

- [x] 检查仓库状态、架构和环境，确认当前没有应用代码或项目虚拟环境。
- [x] 建立单文件入口、固定两项直接依赖、添加兼容约束和标准库测试，配置 Windows CI。
- [x] 核对实际运行结果、差异与文档。
- 用户确认本地实施并授权安装方案列明的必要依赖。安装在项目 `.venv` 内。PyAV 为已有传递依赖，本次只限制其版本。
- 后续实际付费请求与远端写入按 AGENTS.md 确认范围。

## 验证与交接

| 命令或检查 | 环境与前提 | 实际结果 |
| --- | --- | --- |
| `python -m venv .venv`、`pip install --only-binary=:all: -r requirements.txt` | Windows 11 x64 / Python 3.13.2 | 成功安装本地依赖。首次解析的 PyAV 19.0.2 解码失败，约束为 18.1.1 后实测通过 |
| `talk2coding.py`、`--help`、`--list-devices` | 项目虚拟环境 | 均成功退出，枚举 10 个输入设备条目 |
| `unittest discover -s tests -v` | 项目虚拟环境 | 4 项通过 |
| `pip check`、`compileall`、规则一致性与 Git 差异检查 | 项目虚拟环境、仓库根目录 | 通过 |

- 已完成内容和关键文件：[应用入口](../../talk2coding.py)、[依赖清单](../../requirements.txt)、[兼容约束](../../constraints.txt)、[开发说明](../DEVELOPMENT.md)、[架构](../ARCHITECTURE.md)及双语 README。
- 尚未验证 VS Code 焦点切换、麦克风采集、模型推理、付费 API 或 GitHub 托管作业。后续以 [项目验收条件](../PROJECT.md) 为准。
- 后续验收复查见 [A1–A14 检查与修复记录](2026-11-22-scaffold-acceptance-audit.md)。
