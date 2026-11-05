#!/usr/bin/env python3
"""Validate datasets/datasets.json against datasets/datasets.csv.

Link health is intentionally out of scope. The GitHub Actions workflow reports
broken links and does not delete catalog rows.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "datasets" / "datasets.json"
CSV_PATH = ROOT / "datasets" / "datasets.csv"

REQUIRED = [
    "id",
    "name",
    "version",
    "year",
    "subjects",
    "recordings",
    "modalities",
    "sampling_rate",
    "annotations",
    "clinical_text",
    "access_tier",
    "license",
    "research_use",
    "official_url",
    "download_url",
    "paper",
    "doi",
    "last_verified",
    "verification_sources",
    "categories",
    "waveform_included",
    "multi_expert",
    "timed_events",
    "claim_evidence_labels",
    "cover_stage2",
    "notes",
]
TIERS = {"A", "B", "C", "Unverified"}
URL_FIELDS = ("official_url", "download_url")
URL_RE = re.compile(r"^https?://[^\s]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def as_cell(value: object) -> str:
    if isinstance(value, list):
        return " | ".join(str(item) for item in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value)


def main() -> int:
    errors: list[str] = []
    if not JSON_PATH.is_file():
        print(f"Missing {JSON_PATH}", file=sys.stderr)
        return 1
    if not CSV_PATH.is_file():
        print(f"Missing {CSV_PATH}", file=sys.stderr)
        return 1

    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    rows = payload.get("datasets")
    if not isinstance(rows, list) or not rows:
        errors.append("datasets.json must contain a non-empty datasets list")
        rows = []

    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    json_index: dict[str, dict] = {}

    for index, row in enumerate(rows):
        where = f"json row {index}"
        if not isinstance(row, dict):
            errors.append(f"{where} is not an object")
            continue
        missing = [key for key in REQUIRED if key not in row or row[key] in ("", None, [])]
        if missing:
            errors.append(f"{where} missing {', '.join(missing)}")
        dataset_id = str(row.get("id", ""))
        where = dataset_id or where
        if not ID_RE.match(dataset_id):
            errors.append(f"{where} has an invalid id")
        if dataset_id in seen_ids:
            errors.append(f"duplicate id {dataset_id}")
        seen_ids.add(dataset_id)
        name_key = str(row.get("name", "")).strip().lower()
        if name_key in seen_names:
            errors.append(f"duplicate name {row.get('name')}")
        seen_names.add(name_key)
        tier = row.get("access_tier")
        if tier not in TIERS:
            errors.append(f"{where} access_tier {tier!r} is not one of {sorted(TIERS)}")
        if not DATE_RE.match(str(row.get("last_verified", ""))):
            errors.append(f"{where} last_verified must be YYYY-MM-DD")
        for field in URL_FIELDS:
            if not URL_RE.match(str(row.get(field, ""))):
                errors.append(f"{where} {field} is not an http(s) URL")
        sources = row.get("verification_sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{where} verification_sources must be a non-empty list")
        else:
            for source in sources:
                if not URL_RE.match(str(source)):
                    errors.append(f"{where} verification source is not an http(s) URL: {source}")
        categories = row.get("categories")
        if not isinstance(categories, list) or not categories:
            errors.append(f"{where} categories must be a non-empty list")
        if not isinstance(row.get("waveform_included"), bool):
            errors.append(f"{where} waveform_included must be a boolean")
        if tier == "A" and "controlled-access" in (categories or []):
            errors.append(f"{where} is Tier A but categorized as controlled-access")
        if tier == "C" and "controlled-access" not in (categories or []):
            errors.append(f"{where} is Tier C but missing the controlled-access category")
        json_index[dataset_id] = row

    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED:
            errors.append(
                "CSV header mismatch.\n"
                f"expected: {REQUIRED}\n"
                f"found: {reader.fieldnames}"
            )
            csv_rows = []
        else:
            csv_rows = list(reader)

    if len(csv_rows) != len(json_index):
        errors.append(f"row count differs: json {len(json_index)} csv {len(csv_rows)}")

    csv_ids: set[str] = set()
    for row in csv_rows:
        dataset_id = row.get("id", "")
        if dataset_id in csv_ids:
            errors.append(f"duplicate CSV id {dataset_id}")
        csv_ids.add(dataset_id)
        source = json_index.get(dataset_id)
        if source is None:
            errors.append(f"CSV id {dataset_id} is absent from JSON")
            continue
        for key in REQUIRED:
            expected = as_cell(source[key])
            found = row[key]
            if found != expected:
                errors.append(f"{dataset_id} field {key} differs between JSON and CSV")

    missing_in_csv = sorted(set(json_index) - csv_ids)
    if missing_in_csv:
        errors.append("JSON ids missing from CSV: " + ", ".join(missing_in_csv))

    tier_counts: dict[str, int] = {tier: 0 for tier in sorted(TIERS)}
    for row in json_index.values():
        tier_counts[str(row["access_tier"])] += 1

    if errors:
        print(f"{len(errors)} catalog error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Catalog OK: "
        f"{len(json_index)} datasets; "
        + ", ".join(f"Tier {tier}={count}" for tier, count in tier_counts.items())
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
