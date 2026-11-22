"""Deterministic copier for the make.fun news-image entry."""

import os
import shutil
from pathlib import Path


SOURCE_NAME = "entry.png"

# A fixed chunk size makes the copy deterministic: every read/write boundary
# is identical for the same source, independent of host or filesystem defaults.
CHUNK = 64 * 1024


def copy_entry(source: Path, output_dir: Path) -> int:
    destination = output_dir / SOURCE_NAME
    with source.open("rb") as src, destination.open("wb") as dst:
        while chunk := src.read(CHUNK):
            dst.write(chunk)
    return destination.stat().st_size


def main() -> None:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"{SOURCE_NAME} not found next to {__file__}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)

    size = copy_entry(source, output_dir)
    print(f"{SOURCE_NAME} copied: {size} bytes")


if __name__ == "__main__":
    main()
