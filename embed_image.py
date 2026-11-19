"""Build helper: embed ../entry-candidate-DENSE-v2.png into main.py as base64.
The embedded payload is verified against the source bytes.
"""

import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-DENSE-v2.png"
TARGET = REPO_DIR / "main.py"

PLACEHOLDER = "__PAYLOAD__"


def main() -> None:
    source_bytes = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(source_bytes).decode("ascii")
    literal = 'PNG_B64 = "%s"\n' % encoded

    source_lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    output_lines = []
    replaced = False
    for line in source_lines:
        if PLACEHOLDER in line and not replaced:
            output_lines.append(literal)
            replaced = True
        else:
            output_lines.append(line)

    if not replaced:
        raise SystemExit("placeholder line not found in %s" % TARGET)

    TARGET.write_text("".join(output_lines), encoding="utf-8")

    embedded = literal[len('PNG_B64 = "') : -len('"\n')]
    verified = base64.b64decode(embedded) == source_bytes

    print("embedded %d base64 chars" % len(encoded))
    print("source: %s" % SOURCE_PNG)
    print("target: %s" % TARGET)
    print(
        "verification: %s (%d source bytes)"
        % ("passed" if verified else "FAILED", len(source_bytes))
    )

    if not verified:
        raise SystemExit("verification failed: embedded payload mismatch")


if __name__ == "__main__":
    main()
