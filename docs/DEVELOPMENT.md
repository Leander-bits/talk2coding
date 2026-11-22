# 环境、命令与验证

更新于 2026-11-22。默认命令进入按键录音会话。诊断命令和模型准备可单独运行。

## 环境与依赖

本机为 Windows 11 x64、CPython 3.13.2，项目虚拟环境位于 `.venv`。直接依赖是 `sounddevice 0.5.6`、`faster-whisper 1.2.1` 和 `openai 3.57.0`。PyAV 固定 18.1.1，避免 PyAV 19 删除 `metadata_errors` 后与 faster-whisper 1.2.1 的 WAV 解码冲突。GPU 推理待验证。

从仓库根目录运行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip --disable-pip-version-check install --no-cache-dir --only-binary=:all: -r requirements.txt
.\.venv\Scripts\python.exe talk2coding.py
```

已有 `.venv` 时直接运行安装命令即可升级当前清单。启动后等待“已就绪”。按住 F7 并在看到“录音中”后说话，终端会显示预览。松开后输出有标点的完整转写。可以重复录制补充，录音中可用 Esc 取消该段。

| 键 | 作用 |
| --- | --- |
| Enter | 提交当前草稿并生成 prompt |
| E | 整段替换草稿的最后一段。输入正确全文后按 Enter 确认编辑，留空保留，其他段不动 |
| R | 用最近一次提交的转写重新请求 DeepSeek。每次按下发起一次新请求，后录的草稿可继续编辑 |
| C | 清空草稿和内存中最近一次提交的转写 |
| Q 或 Ctrl+C | 退出 |

## 配置与诊断

Enter 提交和 R 重新生成时读取项目根目录的 `.env`。录音和本地转写可独立运行。使用已有 `.env` 或当前进程环境变量。进程环境覆盖同名配置。配置文件应为 UTF-8，按每行 `名称=值` 书写，可用普通单引号和双引号。示例见 [.env.example](../.env.example)。

| 配置 | 用途 |
| --- | --- |
| `DEEPSEEK_API_KEY` | 整理请求所需凭证 |
| `DEEPSEEK_BASE_URL` | 默认 `https://api.deepseek.com`。SDK 从 HTTPS 根地址追加 `/chat/completions` |
| `MODEL_NAME` | 默认 `deepseek-flash`。设置时使用该 HTTPS 服务接受的模型标识 |

```powershell
.\.venv\Scripts\python.exe talk2coding.py --check
.\.venv\Scripts\python.exe talk2coding.py --list-devices
.\.venv\Scripts\python.exe talk2coding.py --help
.\.venv\Scripts\python.exe talk2coding.py --prepare-model
```

`--check` 和 `--list-devices` 只做本机诊断。默认启动会先检查缓存，缺少权重时自动从 Hugging Face 下载约 1.62 GB 到 `.local/whisper/`。看到“已就绪”后即可录音。`--prepare-model` 适合提前下载并验证加载，是可选命令。下载中断后可重跑，已完整缓存的文件会重用，当前环境的下载库不保证跨进程续传未完成的文件。若本机已备好同格式的完整 CTranslate2 模型，可加 `--model-dir "路径"` 直接载入。可使用 `--device N` 选择列表编号。有快捷键冲突时可加 `--key F8` 或其他 F1–F12 功能键。

重定向文件和管道的标准输出及错误使用 UTF-8。Windows PowerShell 5.1 接收管道时，可在当前 PowerShell 会话设置 `[Console]::OutputEncoding = [Text.Encoding]::UTF8`。

## 检查命令

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m compileall -q talk2coding.py
.\.venv\Scripts\python.exe talk2coding.py --check
.\.venv\Scripts\python.exe scripts/sync_instructions.py --check
git diff --check
```

Windows CI 运行依赖、编译、内存 WAV 解码和 `--check`。解码检查内联于工作流，因此项目目录只保留应用的 Python 文件和既有规则维护脚本。检查无需交互终端、录音、Whisper 权重或付费 API。

## 证据与待验证项

OpenAI SDK 已安装到项目虚拟环境。已使用 SDK 实例和模拟 HTTP 响应验证请求路径、凭证头、模型名、仅提交当前文字和固定指令，以及 API 错误与截断处理。本机音频设备枚举、默认输入格式检查、F7 Win32 状态查询通过。合成 WAV 解码与重采样、录音回调和热键会话逻辑通过本地检查或模拟测试。

本机 Whisper 权重已完整缓存。使用 Windows 合成普通话做离线 CPU 对照时，旧版在同一段音频中无标点，新版分出四句。两次都把「重试」转录成「重视」，可在提交前用 E 修正。这是一条合成语音记录，用户实际讲话的标点覆盖率仍待抽样。原三个独立测试文件删除前，共运行 23 项验证，涉及快捷键、标题校验、标点、实时预览和模拟请求。

详细记录见 [快捷键、标点和提示词任务](tasks/2026-11-22-punctuation-and-repeat.md)、[实时转写任务](tasks/2026-11-22-live-transcript.md)和[录音与 DeepSeek 功能任务](tasks/2026-11-22-record-and-generate.md)。真实人声、焦点切换、准确率和付费 API 请求仍待单独验收。
