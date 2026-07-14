import pandas as pd

from reporting_automation.exporter import export_outputs
from reporting_automation.quality_score import calculate_quality_scores
from reporting_automation.validators import validate_dataframe


def test_export_generation(tmp_path):
    cleaned = pd.DataFrame(
        [{"date": pd.Timestamp("2026-01-01"), "revenue": 100, "department": "sales", "region": "north", "status": "complete", "owner": "avery", "source_file": "sample.csv"}]
    )
    issues = validate_dataframe(cleaned)
    scores = calculate_quality_scores(cleaned, issues)
    outputs = export_outputs(cleaned, issues, scores, output_dir=tmp_path, database_path=tmp_path / "test.db")
    assert outputs["cleaned_csv"].exists()
    assert outputs["validation_csv"].exists()
    assert outputs["summary_md"].exists()
    assert outputs["database"].exists()
