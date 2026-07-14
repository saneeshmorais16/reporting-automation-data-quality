import sqlite3
from pathlib import Path

import pandas as pd

from reporting_automation.config import DATABASE_PATH, OUTPUT_DIR
from reporting_automation.report_generator import generate_summary_markdown


def export_outputs(
    cleaned: pd.DataFrame,
    issues: pd.DataFrame,
    scores: dict[str, float],
    output_dir: Path = OUTPUT_DIR,
    database_path: Path = DATABASE_PATH,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    cleaned_csv = output_dir / "cleaned_report_dataset.csv"
    validation_csv = output_dir / "validation_report.csv"
    summary_md = output_dir / "summary_report.md"

    cleaned.to_csv(cleaned_csv, index=False)
    issues.to_csv(validation_csv, index=False)
    summary_md.write_text(generate_summary_markdown(cleaned, issues, scores), encoding="utf-8")

    with sqlite3.connect(database_path) as connection:
        cleaned.to_sql("cleaned_reports", connection, if_exists="replace", index=False)
        issues.to_sql("validation_issues", connection, if_exists="replace", index=False)

    return {
        "cleaned_csv": cleaned_csv,
        "validation_csv": validation_csv,
        "summary_md": summary_md,
        "database": database_path,
    }
