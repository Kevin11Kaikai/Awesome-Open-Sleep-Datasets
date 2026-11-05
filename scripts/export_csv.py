#!/usr/bin/env python3
"""Write datasets/datasets.csv from datasets/datasets.json."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_catalog import CSV_PATH, JSON_PATH, REQUIRED, as_cell

def main() -> None:
    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED, lineterminator="\n")
        writer.writeheader()
        for row in payload["datasets"]:
            writer.writerow({key: as_cell(row[key]) for key in REQUIRED})
    print(f"Wrote {CSV_PATH}")


if __name__ == "__main__":
    main()
