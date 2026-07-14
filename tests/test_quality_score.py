import pandas as pd

from reporting_automation.quality_score import calculate_quality_scores
from reporting_automation.validators import validate_dataframe


def test_quality_score_calculation_returns_expected_keys():
    df = pd.DataFrame(
        [
            {"date": pd.Timestamp("2026-01-01"), "revenue": 100, "department": "sales", "region": "north", "status": "complete", "owner": "avery"},
            {"date": pd.NaT, "revenue": 100, "department": "sales", "region": "north", "status": "complete", "owner": "avery"},
        ]
    )
    scores = calculate_quality_scores(df, validate_dataframe(df))
    assert set(scores) == {"completeness_score", "consistency_score", "duplicate_score", "overall_quality_score"}
    assert scores["overall_quality_score"] < 100
