"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py onto a single line."""

import ast
import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
TARGET = REPO_DIR / "main.py"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(text)

    assignment = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "PNG_B64" for target in node.targets
        ):
            assignment = node
            break
    if assignment is None:
        raise SystemExit(f"no PNG_B64 assignment found in {TARGET}")

    value = ast.literal_eval(assignment.value)
    payload = value if isinstance(value, str) else "".join(value)
    decoded = base64.b64decode(payload)
    if not decoded.startswith(PNG_MAGIC):
        raise SystemExit("decoded payload does not start with the PNG magic bytes")

    lines = text.splitlines(keepends=True)
    lines[assignment.lineno - 1 : assignment.end_lineno] = [f'PNG_B64 = "{payload}"\n']
    TARGET.write_text("".join(lines), encoding="utf-8")

    print(f"Rewrapped {len(payload)} base64 chars onto a single line")
    print(f"Decoded {len(decoded)} bytes")


if __name__ == "__main__":
    main()
