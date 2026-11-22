# 任务：更新快捷键、中文标点和提示词格式

状态为已实现并完成本地验证。记录于 2026-11-22。

## 目标与验收

- [x] 删除 U。E 替换草稿末段，R 重新请求最近一次提交，保留后来录制的草稿，长按 R 不重复发请求。
- [x] 中文转写根据 Whisper 标点示例和词时间戳补标点。保留已有标点、技术词和否定词的文字。
- [x] DeepSeek 只输出固定五个 Markdown 标题，标题不符可用 R 重新生成。
- [x] 验证后移除用户指定的三个测试文件，调整 GitHub 工作流。

## 计划与授权

- [x] 查现有实现、缓存和电脑配置，比较原项目的模型文档。
- [x] 完成快捷键、标点和提示词修改，运行原有及本轮回归验证。
- [x] 删除已验证的三个独立测试文件及其缓存。
- 授权范围为本地修改、测试与删除指定测试文件。模型切换仍是可选方案。本轮保留已有模型及运行时依赖。

## 模型选择

实测机器具备 RTX 4060 Laptop GPU（约 8 GiB 显存）和约 15.2 GiB 系统内存。缺标点可能影响长句的边界和限制词的作用范围。优先使用缓存中的 Whisper large-v3-turbo，在解码中提供带标点的中文示例，松键后依据词间较长停顿保守补逗号及缺失的句号。[faster-whisper 源码](https://github.com/SYSTRAN/faster-whisper/blob/v1.2.1/faster_whisper/transcribe.py)

- 若中文词本身识别准确，仍只有标点不满意，可对比专门给中英文文本补标点的 FunASR CT-Transformer。它会引入独立权重和运行环境。[FunASR 标点模型](https://github.com/modelscope/FunASR/blob/main/funasr/models/ct_transformer/model.py)
- 若中文和英文技术词本身也经常识别错，可以优先试 Qwen3-ASR-0.6B，在这台机器上用同一录音对比标点、限制词和松键后的等待。其 Transformers 后端需要验证 Windows 依赖和资源占用。上游支持中文和英文，实机质量仍未知。[Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) · [0.6B 模型卡](https://huggingface.co/Qwen/Qwen3-ASR-0.6B-hf)

## 验证与交接

| 检查 | 实际结果 |
| --- | --- |
| `python -m unittest discover -s tests -v` | 删除前 23 项通过，覆盖 R 的提交来源和防重复、E、U 已移除、标题响应校验、标点规则与模拟 HTTP |
| 完整 Whisper 模型、同一段合成普通话、本机离线 CPU int8 | 旧版 0 个标点，新版输出 4 个句号，分别耗时约 14.00 和 13.82 秒。两版均误识别「重试」为「重视」 |
| 依赖、编译、CLI 诊断、CI 内存 WAV 解码、规则一致性与文档差异检查 | 本机通过。GitHub 托管执行和付费请求未运行 |

- 识别效果仅来自一段合成音频。本轮未用用户真实录音，也未调用真实 DeepSeek 服务。
- [开发说明](../DEVELOPMENT.md)记录快捷键和检查命令。
