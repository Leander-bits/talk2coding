# talk2coding

简体中文 | [English](README.en.md)

在 VS Code 的 PowerShell 中按住 **F7** 口述开发需求，终端会显示本地 Whisper 实时转写预览。松开后输出本段完整转写。按 **E** 替换最后一段草稿，按 **Enter** 让 DeepSeek 生成可复制到 Codex 的 prompt，按 **R** 用最近一次提交的文字重新生成。

```powershell
.\.venv\Scripts\python.exe talk2coding.py
```

首次运行会自动下载约 1.62 GB 的 Whisper 模型，已有完整缓存时直接载入。DeepSeek 整理使用项目根目录的 `.env` 或当前进程中的配置，示例见 [.env.example](.env.example)。完整安装、换键和选择麦克风的命令见[开发说明](docs/DEVELOPMENT.md)。

| 路径 | 用途 |
| --- | --- |
| `talk2coding.py` | 终端会话、录音、转写和 DeepSeek 请求 |
| `requirements.txt`、`constraints.txt` | Python 依赖与版本约束 |
| `.github/workflows/` | CI 检查 |
| `docs/` | [需求](docs/PROJECT.md)、[架构](docs/ARCHITECTURE.md)和[验证](docs/DEVELOPMENT.md) |

[MIT 许可证](LICENSE)
