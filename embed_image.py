"""Build helper: embed ../entry-candidate-DENSE-v2.png into main.py as base64.
The embedded payload is verified against the source bytes before the run succeeds.
"""

import argparse
import base64
import hashlib
import pathlib
import sys

ASSIGNMENT = "PNG_B64 = "
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

HERE = pathlib.Path(__file__).resolve().parent


def default_source() -> pathlib.Path:
    return HERE.parent / "entry-candidate-DENSE-v2.png"


def default_target() -> pathlib.Path:
    return HERE / "main.py"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inline a PNG into main.py as a single-line base64 literal."
    )
    parser.add_argument(
        "--source",
        type=pathlib.Path,
        default=default_source(),
        help="PNG to embed (default: %(default)s)",
    )
    parser.add_argument(
        "--target",
        type=pathlib.Path,
        default=default_target(),
        help="Python file holding the PNG_B64 line (default: %(default)s)",
    )
    return parser.parse_args(argv)


def read_png(path: pathlib.Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise SystemExit(f"cannot read source PNG {path}: {exc}") from exc


def replace_payload(text: str, literal: str, target: pathlib.Path) -> str:
    lines = text.splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.startswith(ASSIGNMENT)]
    if not hits:
        raise SystemExit(f"{target}: no line beginning with {ASSIGNMENT!r}")
    if len(hits) > 1:
        raise SystemExit(
            f"{target}: {len(hits)} lines begin with {ASSIGNMENT!r}, expected exactly one"
        )

    index = hits[0]
    ending = lines[index][len(lines[index].rstrip("\r\n")):] or "\n"
    lines[index] = f'{ASSIGNMENT}"{literal}"{ending}'
    return "".join(lines)


def extract_payload(text: str, target: pathlib.Path) -> str:
    for line in text.splitlines():
        if line.startswith(ASSIGNMENT):
            body = line[len(ASSIGNMENT):].strip()
            if len(body) < 2 or body[0] != '"' or body[-1] != '"':
                raise SystemExit(f"{target}: PNG_B64 line is not a plain string literal")
            return body[1:-1]
    raise SystemExit(f"{target}: embedded PNG_B64 line vanished during verification")


def verify(target: pathlib.Path, expected: bytes) -> None:
    try:
        text = target.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"cannot re-read {target}: {exc}") from exc

    try:
        actual = base64.b64decode(extract_payload(text, target), validate=True)
    except ValueError as exc:
        raise SystemExit(f"{target}: embedded payload is not valid base64: {exc}") from exc

    if actual != expected:
        raise SystemExit(
            f"{target}: embedded payload does not match source bytes "
            f"({len(actual)} vs {len(expected)} bytes)"
        )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    data = read_png(args.source)
    if not data.startswith(PNG_MAGIC):
        raise SystemExit(f"{args.source}: not a PNG (bad magic bytes)")

    literal = base64.b64encode(data).decode("ascii")
    try:
        text = args.target.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"cannot read target {args.target}: {exc}") from exc

    args.target.write_text(replace_payload(text, literal, args.target), encoding="utf-8")
    verify(args.target, data)

    print(f"source:   {args.source}")
    print(f"target:   {args.target}")
    print(f"bytes:    {len(data)}")
    print(f"base64:   {len(literal)} chars")
    print(f"sha256:   {hashlib.sha256(data).hexdigest()}")
    print("verified: embedded payload matches source bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
