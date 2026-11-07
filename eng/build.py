"""Build the Liuli archive and its release checksum."""

import argparse
import hashlib
import json
from pathlib import Path
import re

from pack import pack


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Require this Git tag to match the manifest version")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    source = root / "theme"
    manifest = json.loads((source / "theme.json").read_text(encoding="utf-8"))
    version = manifest.get("version")
    if manifest.get("id") != "nexa.liuli" or not isinstance(version, str) or not re.fullmatch(
        r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version
    ):
        parser.error("Expected the nexa.liuli ID and an X.Y.Z manifest version.")
    if args.tag is not None and args.tag != f"v{version}":
        parser.error(f"Expected tag v{version}, got {args.tag!r}.")

    output = root / "dist" / f"NexaCL-Liuli-{version}.ntp"
    pack(source, output)
    with output.open("rb") as archive:
        checksum = hashlib.file_digest(archive, "sha256").hexdigest()
    (output.parent / "SHA256SUMS").write_text(
        f"{checksum}  {output.name}\n", encoding="ascii", newline="\n"
    )


if __name__ == "__main__":
    main()
