"""Build helper: embed ../entry-candidate-DENSE18-v1.png into main.py as base64."""

import base64
import pathlib
import re

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-DENSE18-v1.png"
TARGET = REPO_DIR / "main.py"
PLACEHOLDER = "__PAYLOAD__"


def main() -> None:
    source_bytes = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(source_bytes).decode("ascii")

    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    matches = [index for index, line in enumerate(lines) if PLACEHOLDER in line]
    if not matches:
        raise SystemExit(
            f"no line containing {PLACEHOLDER!r} in {TARGET}; restore the marker line to re-embed"
        )
    if len(matches) > 1:
        raise SystemExit(
            f"{len(matches)} lines contain {PLACEHOLDER!r} in {TARGET}, expected exactly one"
        )

    lines[matches[0]] = f'PNG_B64 = "{encoded}"\n'
    TARGET.write_text("".join(lines), encoding="utf-8")

    found = re.search(
        r'^PNG_B64 = "([^"]*)"$', TARGET.read_text(encoding="utf-8"), re.MULTILINE
    )
    verified = found is not None and base64.b64decode(found.group(1)) == source_bytes

    print(f"Embedded {len(encoded)} base64 chars")
    print(f"Source: {SOURCE_PNG}")
    print(f"Target: {TARGET}")
    print(f"Verified: {verified}")
    if not verified:
        raise SystemExit("verification failed: embedded payload does not match the source PNG")


if __name__ == "__main__":
    main()
