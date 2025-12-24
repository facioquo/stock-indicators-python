"""Equivalence checks across DateOf* CSV datasets.

Ensures all non-date columns are identical across variants.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parents[2] / "test_data" / "quotes"

# All DateOf* datasets created by the generator; ensure they are present
DATASETS = [
    "DateOfUTCDate",
    "DateOfUTCZDate",
    "DateOfUTCFracZDate",
    "DateOfOffsetDate",
    "DateOfOffsetFracDate",
    "DateOfOffsetBasicDate",
    "DateOfNaiveMinDate",
    "DateOfNaiveSecDate",
    "DateOfNaiveMsDate",
    "DateOfNaiveBasicDate",
    "DateOfDateOnly",
    "DateOfDateOnlyBasic",
    "DateOfDateOnlyDMY",
    "DateOfDateOnlyUS",
    "DateOfRFC1123Date",
    "DateOfIANAZoneDate",
]


def _load_csv(name: str):
    path = BASE / f"{name}.csv"
    with path.open("r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    return header, rows


@pytest.mark.parametrize("name", DATASETS)
def test_equivalent_non_date_columns(name: str):
    # Load reference (first dataset) and compare all others to it
    ref_header, ref_rows = _load_csv(DATASETS[0])
    header, rows = _load_csv(name)

    # Headers match exactly
    assert header == ref_header

    # Same number of rows
    assert len(rows) == len(ref_rows)

    # For each row, all columns except the date column (index 1) should match
    for ref_row, row in zip(ref_rows, rows):
        assert ref_row[0] == row[0]  # index
        assert ref_row[2:] == row[2:]  # all non-date price/volume columns
