# Reporting Automation Data Quality

A portfolio-ready reporting automation and data quality prototype that cleans recurring synthetic business reports, validates data, detects errors, consolidates files and exports a clean dataset with validation and summary reports.

## What This Project Does

The pipeline loads recurring CSV and Excel reports, standardises inconsistent columns, cleans common business fields, validates data quality issues and produces export-ready outputs for review.

## Why It Matters

Recurring reports often arrive in slightly different formats. Manual cleanup is slow and error-prone. This project demonstrates how Python, pandas and validation logic can automate repeatable data quality checks before reporting.

## Problem Statement

Business reporting files can contain inconsistent column names, invalid dates, missing fields, duplicate rows, negative revenue values and unexpected categories. A reliable reporting workflow needs to catch those problems before analysis or dashboarding.

## Tech Stack

- Python
- pandas
- SQL and SQLite
- openpyxl
- Streamlit optional dashboard
- pytest
- GitHub Actions

## Core Features

- Load recurring CSV and Excel files
- Standardise report columns
- Clean dates, revenue, department, region, status and owner fields
- Handles common revenue currency symbols and text labels before numeric parsing
- Consolidate multiple files into one dataset
- Generate row-level validation issues
- Calculate completeness, consistency, duplicate and overall quality scores
- Export cleaned CSV, validation report CSV, summary Markdown and local SQLite tables
- Optional Streamlit dashboard

## Data Quality Checks

- Missing values
- Duplicate rows
- Invalid dates
- Negative revenue
- Unexpected departments, regions and statuses
- Inconsistent column names

## Example Input/Output Flow

1. Place safe recurring reports in `data/sample_reports/`.
2. Run `python run_pipeline.py`.
3. The pipeline reads CSV and Excel files, standardises schemas and validates records.
4. Outputs are written to `data/outputs/` and a local SQLite database.

Generated outputs are ignored by Git.

## Example Validation Report

| row_number | column_name | issue_type | severity | suggested_fix |
| --- | --- | --- | --- | --- |
| 6 | date | invalid_date | high | Use a valid ISO-style date such as 2026-03-31. |
| 7 | revenue | negative_revenue | critical | Confirm whether revenue should be positive or reclassify as adjustment. |

## Setup Steps

```bash
pip install -r requirements.txt
```

## Run The Pipeline

```bash
python run_pipeline.py
```

## Run The Optional Dashboard

```bash
streamlit run app/dashboard.py
```

## Run Tests

```bash
pytest
```

## Data Privacy And Synthetic Data Note

The bundled reports are synthetic demo files. This repository must not include real company reports, customer data, private financial records, generated PDFs, credentials or application packets.

## Limitations

- Validation rules are intentionally simple and transparent.
- Category lists are fixed in code for the starter version.
- The dashboard is a local review tool, not a production deployment.
- The sample reports are small and not intended to represent a real business.

## Future Improvements

- Add configurable validation rules.
- Add Excel workbook exports with formatted validation tabs.
- Add automated anomaly detection for unusual revenue changes.
- Add richer dashboard filters and trend charts.
- Add support for folder-level batch scheduling.

## No-Secrets Note

Do not commit `.env` files, API keys, tokens, credentials, real reports, private data, customer data, financial records, logs, generated PDFs, application packets, databases or generated outputs.
