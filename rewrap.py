"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py onto one line.

It exists only to repair a payload that was split across several lines and is not
needed to run the entry.
"""

import ast
import base64
import hashlib
import pathlib
import sys

NAME = "PNG_B64"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

HERE = pathlib.Path(__file__).resolve().parent


def read_source(path: pathlib.Path) -> tuple[str, ast.Module]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"cannot read {path}: {exc}") from exc
    try:
        return text, ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        raise SystemExit(f"{path}: will not parse: {exc}") from exc


def find_assignment(tree: ast.Module, path: pathlib.Path) -> ast.Assign:
    found = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == NAME for t in node.targets)
    ]
    if not found:
        raise SystemExit(f"{path}: no top-level {NAME} = ... assignment")
    if len(found) > 1:
        raise SystemExit(f"{path}: {len(found)} top-level {NAME} assignments, expected one")
    return found[0]


def literal_payload(node: ast.Assign, path: pathlib.Path) -> str:
    try:
        value = ast.literal_eval(node.value)
    except (ValueError, SyntaxError) as exc:
        raise SystemExit(f"{path}: {NAME} value is not a literal: {exc}") from exc
    if not isinstance(value, str):
        raise SystemExit(f"{path}: {NAME} is a {type(value).__name__}, not a string")
    return value


def decode_payload(value: str, path: pathlib.Path) -> bytes:
    try:
        data = base64.b64decode(value, validate=True)
    except ValueError as exc:
        raise SystemExit(f"{path}: {NAME} is not valid base64: {exc}") from exc
    if not data.startswith(PNG_MAGIC):
        raise SystemExit(f"{path}: {NAME} does not decode to a PNG (bad magic bytes)")
    return data


def collapse(text: str, node: ast.Assign, payload: str) -> str:
    lines = text.splitlines(keepends=True)
    start = node.lineno - 1
    ending = lines[start][len(lines[start].rstrip("\r\n")):] or "\n"
    lines[start:node.end_lineno] = [f'{NAME} = "{payload}"{ending}']
    return "".join(lines)


def main() -> int:
    path = HERE / "main.py"
    text, tree = read_source(path)
    node = find_assignment(tree, path)
    payload = literal_payload(node, path)
    data = decode_payload(payload, path)

    print(f"target:    {path}")
    print(f"bytes:     {len(data)}")
    print(f"sha256:    {hashlib.sha256(data).hexdigest()}")

    rewritten = collapse(text, node, payload)
    try:
        ast.parse(rewritten, filename=str(path))
    except SyntaxError as exc:
        raise SystemExit(f"{path}: rewrite would not parse, nothing written: {exc}") from exc

    path.write_text(rewritten, encoding="utf-8")
    print(f"rewrapped: {len(payload)} base64 chars on one line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
