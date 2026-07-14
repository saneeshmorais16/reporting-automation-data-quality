from pathlib import Path

import pandas as pd

from reporting_automation.config import SAMPLE_REPORTS_DIR


def load_report_file(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported report file type: {path.suffix}")


def load_reports(directory: Path = SAMPLE_REPORTS_DIR) -> list[tuple[str, pd.DataFrame]]:
    files = sorted(
        path for path in directory.iterdir() if path.suffix.lower() in {".csv", ".xlsx", ".xls"}
    )
    if not files:
        raise FileNotFoundError(f"No CSV or Excel files found in {directory}")
    return [(path.name, load_report_file(path)) for path in files]
