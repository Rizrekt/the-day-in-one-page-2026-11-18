"""Build helper: embed ../entry-candidate-PJ-v1.png into main.py as base64."""

import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-PJ-v1.png"
TARGET = REPO_DIR / "main.py"
PLACEHOLDER = "__PAYLOAD__"


def main():
    raw = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(raw).decode("ascii")

    lines = TARGET.read_text(encoding="utf-8").splitlines()
    hits = [i for i, line in enumerate(lines) if PLACEHOLDER in line]
    if len(hits) != 1:
        raise SystemExit(
            "expected exactly one placeholder line in %s, found %d" % (TARGET, len(hits))
        )
    lines[hits[0]] = 'PNG_B64 = "%s"' % encoded
    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")

    embedded = None
    for line in TARGET.read_text(encoding="utf-8").splitlines():
        if line.startswith("PNG_B64 = "):
            embedded = line[len("PNG_B64 = "):].strip()
            break

    ok = False
    if embedded is not None and len(embedded) >= 2:
        ok = base64.b64decode(embedded[1:-1]) == raw

    print("embedded base64 chars: %d" % len(encoded))
    print("source: %s" % SOURCE_PNG)
    print("target: %s" % TARGET)
    print("verification: %s" % ("PASSED" if ok else "FAILED"))
    if not ok:
        raise SystemExit("verification failed: embedded payload does not match source PNG")


if __name__ == "__main__":
    main()