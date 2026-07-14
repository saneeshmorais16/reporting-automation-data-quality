import pandas as pd

from reporting_automation.column_standardiser import clean_values, standardise_columns


def test_column_standardisation_maps_aliases():
    raw = pd.DataFrame({"Report Date": ["2026-01-01"], "Sales": ["$1,200"], "Dept": ["Sales"], "Area": ["North"], "Report Status": ["Complete"], "Report Owner": ["Avery"]})
    standardised = clean_values(standardise_columns(raw, "sample.csv"))
    assert list(standardised.columns) == ["date", "revenue", "department", "region", "status", "owner", "source_file"]
    assert standardised.loc[0, "revenue"] == 1200
    assert standardised.loc[0, "department"] == "sales"
