# Automated Data Quality & Validation System

## Overview

An end-to-end Automated Data Quality & Validation System built using Python and Pandas for banking transaction datasets.

The system performs:

- Data Profiling
- Data Cleaning
- Data Validation
- Automated Pipeline Execution
- Reporting & Logging

---

## Project Architecture

Raw Data
↓
Profiling
↓
Cleaning
↓
Validation
↓
Reports

---

## Folder Structure

```text
data/
├── raw
└── cleaned

reports/
├── profiling
├── validation
└── cleaning_log.json

src/
├── profiling
├── cleaning
├── validation
└── pipeline

logs/
└── pipeline.log
```

---

## Outputs

### Profiling

- profiling_report.json
- missing_values_heatmap.png
- correlation_heatmap.png
- transaction_outliers.png

### Cleaning

- cleaned_data.csv
- cleaning_log.json

### Validation

- validation_report.json

---

## Example Health Score

```json
{
    "data_health_score": 97.62
}
```

---

## Run Pipeline

```bash
python src/pipeline/pipeline.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Git
- GitHub

---

## Author

Talha Ather