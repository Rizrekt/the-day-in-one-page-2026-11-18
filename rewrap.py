"""One-shot helper: collapse the wrapped PNG_B64 payload onto a single line."""

import ast
import pathlib

TARGET = pathlib.Path(__file__).resolve().parent / "main.py"


def main() -> None:
    source = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(source)

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
        raise SystemExit("PNG_B64 assignment not found in %s" % TARGET)

    payload = ast.literal_eval(node.value)
    if not isinstance(payload, str):
        raise SystemExit("PNG_B64 is not a string literal")

    lines = source.splitlines(keepends=True)
    replacement = 'PNG_B64 = "%s"\n' % payload
    new_lines = lines[: node.lineno - 1] + [replacement] + lines[node.end_lineno :]

    TARGET.write_text("".join(new_lines), encoding="utf-8")
    print("rewrapped %d base64 chars onto one line" % len(payload))


if __name__ == "__main__":
    main()
