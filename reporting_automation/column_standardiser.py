import re

import pandas as pd

from reporting_automation.config import CANONICAL_COLUMNS, COLUMN_ALIASES


def normalise_column_name(name: object) -> str:
    text = str(name).strip().lower()
    text = re.sub(r"[_\-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return COLUMN_ALIASES.get(text, text.replace(" ", "_"))


def standardise_columns(df: pd.DataFrame, source_file: str = "") -> pd.DataFrame:
    standardised = df.rename(columns={column: normalise_column_name(column) for column in df.columns}).copy()
    for column in CANONICAL_COLUMNS:
        if column not in standardised.columns:
            standardised[column] = pd.NA
    standardised = standardised[CANONICAL_COLUMNS]
    standardised["source_file"] = source_file
    return standardised


def clean_values(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")
    cleaned["revenue"] = (
        cleaned["revenue"]
        .astype(str)
        # Reports often mix symbols and text labels, so clean both before numeric parsing.
        .str.replace(r"(gbp|usd|pounds|£|\$|,)", "", regex=True, flags=re.IGNORECASE)
        .str.strip()
        .replace({"": pd.NA, "nan": pd.NA})
    )
    cleaned["revenue"] = pd.to_numeric(cleaned["revenue"], errors="coerce")
    for column in ["department", "region", "status", "owner"]:
        cleaned[column] = cleaned[column].astype("string").str.strip().str.lower()
        cleaned[column] = cleaned[column].replace({"": pd.NA, "nan": pd.NA})
    return cleaned


def consolidate_reports(reports: list[tuple[str, pd.DataFrame]]) -> pd.DataFrame:
    frames = [standardise_columns(frame, source_file=name) for name, frame in reports]
    return clean_values(pd.concat(frames, ignore_index=True))
