from reporting_automation.column_standardiser import consolidate_reports
from reporting_automation.data_loader import load_reports
from reporting_automation.exporter import export_outputs
from reporting_automation.quality_score import calculate_quality_scores
from reporting_automation.validators import validate_dataframe


def main() -> None:
    reports = load_reports()
    cleaned = consolidate_reports(reports)
    issues = validate_dataframe(cleaned)
    scores = calculate_quality_scores(cleaned, issues)
    outputs = export_outputs(cleaned, issues, scores)

    print(f"Processed rows: {len(cleaned)}")
    print(f"Issues found: {len(issues)}")
    print(f"Overall quality score: {scores['overall_quality_score']}")
    for label, path in outputs.items():
        print(f"{label}: {path}")


if __name__ == "__main__":
    main()
