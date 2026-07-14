import pandas as pd
import streamlit as st

from reporting_automation.column_standardiser import consolidate_reports
from reporting_automation.config import OUTPUT_DIR
from reporting_automation.data_loader import load_reports
from reporting_automation.quality_score import calculate_quality_scores
from reporting_automation.validators import validate_dataframe


@st.cache_data
def load_dashboard_data():
    cleaned = consolidate_reports(load_reports())
    issues = validate_dataframe(cleaned)
    scores = calculate_quality_scores(cleaned, issues)
    return cleaned, issues, scores


def main():
    st.set_page_config(page_title="Reporting Automation Data Quality", layout="wide")
    st.title("Reporting Automation Data Quality")
    st.caption("Synthetic sample reports only. No real company, customer or financial records are included.")

    cleaned, issues, scores = load_dashboard_data()
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows processed", len(cleaned))
    col2.metric("Errors found", len(issues))
    col3.metric("Quality score", scores["overall_quality_score"])

    st.subheader("Quality score breakdown")
    st.dataframe(pd.DataFrame([scores]), use_container_width=True)

    st.subheader("Issues by type")
    if issues.empty:
        st.success("No validation issues found.")
    else:
        st.bar_chart(issues["issue_type"].value_counts())
        st.subheader("Issues by severity")
        st.bar_chart(issues["severity"].value_counts())
        st.dataframe(issues, use_container_width=True)

    st.subheader("Cleaned dataset preview")
    st.dataframe(cleaned, use_container_width=True)
    st.caption(f"Pipeline exports are written locally to {OUTPUT_DIR}. Generated outputs are ignored by Git.")


if __name__ == "__main__":
    main()
