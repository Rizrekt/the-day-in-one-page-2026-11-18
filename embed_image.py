"""Build helper: embed ../entry-candidate-v4.png into main.py as base64."""

import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-v4.png"
TARGET = REPO_DIR / "main.py"

PLACEHOLDER = "__PAYLOAD__"


def main() -> None:
    encoded = base64.b64encode(SOURCE_PNG.read_bytes()).decode("ascii")
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
    print("embedded %d base64 chars from %s into %s" % (len(encoded), SOURCE_PNG, TARGET))


if __name__ == "__main__":
    main()
