import pandas as pd

from reporting_automation.validators import validate_duplicate_rows, validate_missing_values, validate_unexpected_categories


def _bounded(score: float) -> float:
    return round(max(0.0, min(100.0, score)), 2)


def calculate_quality_scores(df: pd.DataFrame, issues: pd.DataFrame | None = None) -> dict[str, float]:
    if df.empty:
        return {"completeness_score": 0.0, "consistency_score": 0.0, "duplicate_score": 0.0, "overall_quality_score": 0.0}

    total_cells = len(df) * 6
    missing_count = len(validate_missing_values(df))
    completeness = _bounded(100 - (missing_count / total_cells * 100))

    category_count = len(validate_unexpected_categories(df))
    consistency = _bounded(100 - (category_count / max(len(df), 1) * 25))

    duplicate_count = len(validate_duplicate_rows(df))
    duplicate_score = _bounded(100 - (duplicate_count / max(len(df), 1) * 100))

    if issues is None:
        critical_count = 0
    elif issues.empty:
        critical_count = 0
    else:
        critical_count = int((issues["severity"] == "critical").sum())
    critical_penalty = min(20, critical_count * 5)

    overall = _bounded((completeness * 0.4) + (consistency * 0.3) + (duplicate_score * 0.3) - critical_penalty)
    return {
        "completeness_score": completeness,
        "consistency_score": consistency,
        "duplicate_score": duplicate_score,
        "overall_quality_score": overall,
    }
