# talk2coding

[简体中文](README.md) | English

Hold **F7** in VS Code's PowerShell terminal and speak to see a live local Whisper preview. Release the key for the complete transcript of that segment. Press **E** to replace the last draft segment, **Enter** to generate a DeepSeek prompt for Codex, or **R** to generate again using the last submission.

```powershell
.\.venv\Scripts\python.exe talk2coding.py
```

The first run automatically downloads about 1.62 GB of Whisper model files and later runs reuse the complete cache. DeepSeek settings come from the project-root `.env` file or the current process environment. See the [configuration example](.env.example) and the [development guide](docs/DEVELOPMENT.md) for installation, hotkey selection, and microphone selection.

| Path | Purpose |
| --- | --- |
| `talk2coding.py` | Terminal session, recording, transcription, and DeepSeek requests |
| `requirements.txt`, `constraints.txt` | Python dependencies and version constraints |
| `.github/workflows/` | CI checks |
| `docs/` | [Requirements](docs/PROJECT.md), [architecture](docs/ARCHITECTURE.md), and [verification](docs/DEVELOPMENT.md) in Chinese |

[MIT license](LICENSE)
