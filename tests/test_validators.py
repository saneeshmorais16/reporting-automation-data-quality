import pandas as pd

from reporting_automation.validators import validate_duplicate_rows, validate_missing_values, validate_negative_revenue, validate_unexpected_categories


def sample_frame():
    return pd.DataFrame(
        [
            {"date": pd.NaT, "revenue": -10, "department": "unknown", "region": "north", "status": "complete", "owner": "avery"},
            {"date": pd.Timestamp("2026-01-01"), "revenue": 100, "department": "sales", "region": "north", "status": "complete", "owner": "avery"},
            {"date": pd.Timestamp("2026-01-01"), "revenue": 100, "department": "sales", "region": "north", "status": "complete", "owner": "avery"},
        ]
    )


def test_missing_value_detection():
    assert any(issue.column_name == "date" for issue in validate_missing_values(sample_frame()))


def test_duplicate_detection():
    assert len(validate_duplicate_rows(sample_frame())) == 2


def test_negative_revenue_detection():
    assert validate_negative_revenue(sample_frame())[0].severity == "critical"


def test_unexpected_category_detection():
    issues = validate_unexpected_categories(sample_frame())
    assert issues[0].issue_type == "unexpected_category"
