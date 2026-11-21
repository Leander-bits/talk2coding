"""修改 AGENTS.md 后由 AI 生成 Copilot 副本；--check 只检查，不写文件。"""

import argparse
import difflib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "AGENTS.md"
TARGET = ROOT / ".github" / "copilot-instructions.md"
HEADER = (
    "<!-- 由 AGENTS.md 自动生成，请勿直接修改。 -->\n"
    "<!-- 下方路径均相对仓库根目录。 -->\n\n"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="只检查一致性，不一致时失败。")
    args = parser.parse_args()

    source = SOURCE.read_text(encoding="utf-8")
    if not source.strip():
        print("错误：AGENTS.md 为空。", file=sys.stderr)
        return 1
    expected = HEADER + source.rstrip() + "\n"

    if args.check:
        actual = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if actual != expected:
            print("错误：Copilot 规则副本与 AGENTS.md 不一致。", file=sys.stderr)
            print("请由 AI 执行：python scripts/sync_instructions.py", file=sys.stderr)
            sys.stdout.writelines(
                difflib.unified_diff(
                    actual.splitlines(keepends=True),
                    expected.splitlines(keepends=True),
                    fromfile=".github/copilot-instructions.md（当前）",
                    tofile=".github/copilot-instructions.md（预期）",
                )
            )
            return 1
        print("通过：Codex 与 Copilot 的核心规则一致。")
        return 0

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(expected, encoding="utf-8", newline="\n")
    print("已根据 AGENTS.md 更新 .github/copilot-instructions.md。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
