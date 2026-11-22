"""Deterministic copier for the make.fun news-image entry."""

import os
import shutil
from pathlib import Path


SOURCE_NAME = "entry.png"


def main() -> None:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"{SOURCE_NAME} not found next to {__file__}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)

    destination = output_dir / SOURCE_NAME
    shutil.copyfile(source, destination)
    size = destination.stat().st_size
    print(f"{SOURCE_NAME} written: {size} bytes")


if __name__ == "__main__":
    main()
