"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py onto a single line."""

import ast
import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
TARGET = REPO_DIR / "main.py"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    text = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(text)

    node = None
    for stmt in tree.body:
        if (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and isinstance(stmt.targets[0], ast.Name)
            and stmt.targets[0].id == "PNG_B64"
        ):
            node = stmt
            break
    if node is None:
        raise SystemExit("no PNG_B64 assignment found in %s" % TARGET)

    payload = ast.literal_eval(node.value)
    decoded = base64.b64decode(payload)
    if not decoded.startswith(PNG_MAGIC):
        raise SystemExit("decoded payload does not start with the PNG magic bytes")

    lines = text.splitlines()
    lines[node.lineno - 1:node.end_lineno] = ['PNG_B64 = "%s"' % payload]
    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("rewrapped base64 chars: %d" % len(payload))
    print("decoded bytes: %d" % len(decoded))


if __name__ == "__main__":
    main()