# Project Status

## Current Build Status

Working starter version for local portfolio review. The pipeline runs with safe synthetic CSV and Excel reports and exports local generated outputs that are ignored by Git.

## Completed Features

- CSV report loading
- Excel report loading
- Column standardisation
- Data cleaning for dates, revenue and categories
- Missing value validation
- Duplicate row validation
- Invalid date detection
- Negative revenue detection
- Unexpected category detection
- Data quality scoring
- Cleaned dataset export
- Validation report export
- Summary Markdown export
- SQLite output tables
- Optional Streamlit dashboard
- pytest test suite
- GitHub Actions workflow

## Remaining Improvements

- Add configurable validation rules.
- Add formatted Excel output workbook.
- Add anomaly detection for unusual revenue movement.
- Add dashboard filters by source file, region and issue severity.
- Add screenshots after local dashboard review.

## Testing Status

Tests cover column standardisation, missing value detection, duplicate detection, quality score calculation and export generation.

Run:

```bash
pytest
```

## What Must Be Checked Before Making Public

- No `.env` files or credentials are present.
- No real company reports are present.
- No customer data, personal data or private financial records are present.
- No database files, logs, PDFs or generated outputs are committed.
- README does not claim production use or real business deployment.

## Files That Must Never Be Committed

- `.env` or `.env.*`
- API keys, tokens, credentials or passwords
- real company reports
- customer data
- personal data
- private financial records
- database files
- logs
- generated PDFs
- application packets
- generated outputs
- private data
