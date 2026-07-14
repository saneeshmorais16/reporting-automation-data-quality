import pandas as pd


def generate_summary_markdown(cleaned: pd.DataFrame, issues: pd.DataFrame, scores: dict[str, float]) -> str:
    issue_count = 0 if issues.empty else len(issues)
    severity_counts = {} if issues.empty else issues["severity"].value_counts().to_dict()
    issue_type_counts = {} if issues.empty else issues["issue_type"].value_counts().to_dict()

    lines = [
        "# Reporting Automation Summary",
        "",
        "This summary was generated from safe synthetic sample reports.",
        "",
        f"- Total rows processed: {len(cleaned)}",
        f"- Validation issues found: {issue_count}",
        f"- Overall quality score: {scores['overall_quality_score']}",
        f"- Completeness score: {scores['completeness_score']}",
        f"- Consistency score: {scores['consistency_score']}",
        f"- Duplicate score: {scores['duplicate_score']}",
        "",
        "## Issues By Severity",
    ]
    if severity_counts:
        lines.extend([f"- {severity}: {count}" for severity, count in severity_counts.items()])
    else:
        lines.append("- No issues found")
    lines.append("")
    lines.append("## Issues By Type")
    if issue_type_counts:
        lines.extend([f"- {issue_type}: {count}" for issue_type, count in issue_type_counts.items()])
    else:
        lines.append("- No issues found")
    return "\n".join(lines) + "\n"
