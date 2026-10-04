# Project 10 — Transaction Monitoring Workbench (Working)

This version is deliberately functional rather than a static dashboard mockup.

## Working features in the browser

- Filters and live recalculation
- Alert search
- Transaction search
- Country/channel filters
- Transaction drill-down modal
- Account-level aggregation
- Local CSV upload
- CSV schema validation
- Recalculation of dashboard data after upload
- Alert queue sorting
- Case export to CSV
- Severity and risk-score logic
- Synthetic transaction dataset included

## Run

Open `index.html` directly in Chrome/Safari.

For the Python pipeline:

```bash
pip install -r requirements.txt
python src/monitoring_pipeline.py
python tests/test_data.py
```

No server is required for the browser demo.

## Important

All data is synthetic and the risk rules are illustrative. Alerts are prioritisation signals, not evidence of criminal activity.
