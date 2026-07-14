import pandas as pd

from reporting_automation.config import EXPECTED_DEPARTMENTS, EXPECTED_REGIONS, EXPECTED_STATUSES
from reporting_automation.schemas import ValidationIssue


def _issue(row_number: int, column_name: str, issue_type: str, severity: str, suggested_fix: str) -> ValidationIssue:
    return ValidationIssue(row_number, column_name, issue_type, severity, suggested_fix)


def validate_missing_values(df: pd.DataFrame) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for index, row in df.iterrows():
        for column in ["date", "revenue", "department", "region", "status", "owner"]:
            if pd.isna(row[column]):
                issues.append(_issue(index + 2, column, "missing_value", "high", f"Provide a value for {column}."))
    return issues


def validate_duplicate_rows(df: pd.DataFrame) -> list[ValidationIssue]:
    duplicate_mask = df.duplicated(subset=["date", "revenue", "department", "region", "status", "owner"], keep=False)
    return [
        _issue(index + 2, "row", "duplicate_row", "medium", "Review duplicate row and keep one trusted record.")
        for index in df[duplicate_mask].index
    ]


def validate_invalid_dates(df: pd.DataFrame) -> list[ValidationIssue]:
    return [
        _issue(index + 2, "date", "invalid_date", "high", "Use a valid ISO-style date such as 2026-03-31.")
        for index, value in df["date"].items()
        if pd.isna(value)
    ]


def validate_negative_revenue(df: pd.DataFrame) -> list[ValidationIssue]:
    return [
        _issue(index + 2, "revenue", "negative_revenue", "critical", "Confirm whether revenue should be positive or reclassify as adjustment.")
        for index, value in df["revenue"].items()
        if pd.notna(value) and value < 0
    ]


def validate_unexpected_categories(df: pd.DataFrame) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    category_rules = {
        "department": EXPECTED_DEPARTMENTS,
        "region": EXPECTED_REGIONS,
        "status": EXPECTED_STATUSES,
    }
    for column, expected in category_rules.items():
        for index, value in df[column].items():
            if pd.notna(value) and str(value).lower() not in expected:
                issues.append(
                    _issue(index + 2, column, "unexpected_category", "medium", f"Use one of: {', '.join(sorted(expected))}.")
                )
    return issues


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    issues = []
    issues.extend(validate_missing_values(df))
    issues.extend(validate_duplicate_rows(df))
    issues.extend(validate_invalid_dates(df))
    issues.extend(validate_negative_revenue(df))
    issues.extend(validate_unexpected_categories(df))
    return pd.DataFrame(
        [issue.__dict__ for issue in issues],
        columns=["row_number", "column_name", "issue_type", "severity", "suggested_fix"],
    )
