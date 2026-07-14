from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SAMPLE_REPORTS_DIR = DATA_DIR / "sample_reports"
OUTPUT_DIR = DATA_DIR / "outputs"
DATABASE_PATH = BASE_DIR / "reporting_automation.db"

CANONICAL_COLUMNS = ["date", "revenue", "department", "region", "status", "owner"]
EXPECTED_DEPARTMENTS = {"sales", "marketing", "operations", "support", "finance"}
EXPECTED_REGIONS = {"north", "south", "east", "west", "central"}
EXPECTED_STATUSES = {"complete", "pending", "cancelled"}

COLUMN_ALIASES = {
    "date": "date",
    "report date": "date",
    "period": "date",
    "transaction_date": "date",
    "revenue": "revenue",
    "sales": "revenue",
    "amount": "revenue",
    "total revenue": "revenue",
    "department": "department",
    "dept": "department",
    "business unit": "department",
    "region": "region",
    "area": "region",
    "market": "region",
    "status": "status",
    "report status": "status",
    "owner": "owner",
    "report owner": "owner",
    "responsible": "owner",
}
