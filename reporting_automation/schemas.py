from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationIssue:
    row_number: int
    column_name: str
    issue_type: str
    severity: str
    suggested_fix: str
