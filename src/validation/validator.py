import pandas as pd
import json
import os

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# Load cleaned dataset

df = pd.read_csv(
    "data/cleaned/cleaned_data.csv"
)

print("Dataset Shape:")
print(df.shape)

# Age Validation

invalid_age_count = (
    (df["age"] < 18)
    |
    (df["age"] > 100)
).sum()

print("\nInvalid Ages:")
print(invalid_age_count)

# Credit Score Validation

invalid_credit_score_count = (
    (df["credit_score"] < 300)
    |
    (df["credit_score"] > 850)
).sum()

print("\nInvalid Credit Scores:")
print(invalid_credit_score_count)

# Transaction Amount Validation

invalid_transaction_amount_count = (
    df["transaction_amount"] < 0
).sum()

print("\nInvalid Transaction Amounts:")
print(invalid_transaction_amount_count)

# Email Validation

invalid_email_count = (
    ~df["email"]
    .fillna("")
    .astype(str)
    .str.contains("@")
).sum()

print("\nInvalid Emails:")
print(invalid_email_count)

# Phone Validation

invalid_phone_count = (
    df["phone"]
    .fillna("")
    .astype(str)
    .str.len() < 10
).sum()

print("\nInvalid Phones:")
print(invalid_phone_count)

# Numeric Columns

numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
)

# Replace NaN values for ML models

numeric_cols_no_nan = numeric_cols.fillna(
    numeric_cols.median()
)

# Isolation Forest

isolation_forest = IsolationForest(
    contamination=0.01,
    random_state=42
)

anomaly_predictions = (
    isolation_forest.fit_predict(
        numeric_cols_no_nan
    )
)

anomaly_count = (
    anomaly_predictions == -1
).sum()

print("\nAnomalies Detected:")
print(anomaly_count)

# Local Outlier Factor

lof = LocalOutlierFactor(
    n_neighbors=20,
    contamination=0.01
)

lof_predictions = lof.fit_predict(
    numeric_cols_no_nan
)

lof_anomaly_count = (
    lof_predictions == -1
).sum()

print("\nLOF Anomalies Detected:")
print(lof_anomaly_count)

# Data Health Score

total_records = len(df)

total_issues = (
    invalid_age_count
    + invalid_credit_score_count
    + invalid_transaction_amount_count
    + invalid_email_count
    + invalid_phone_count
)

health_score = round(
    (1 - (total_issues / (total_records * 5))) * 100,
    2
)

print("\nData Health Score:")
print(health_score)

# Validation Report

validation_report = {
    "dataset_rows": int(total_records),

    "invalid_ages": int(invalid_age_count),

    "invalid_credit_scores":
        int(invalid_credit_score_count),

    "invalid_transaction_amounts":
        int(invalid_transaction_amount_count),

    "invalid_emails":
        int(invalid_email_count),

    "invalid_phones":
        int(invalid_phone_count),

    "anomalies_detected":
        int(anomaly_count),

    "lof_anomalies":
        int(lof_anomaly_count),

    "data_health_score":
        float(health_score)
}

os.makedirs(
    "reports/validation",
    exist_ok=True
)

with open(
    "reports/validation/validation_report.json",
    "w"
) as file:
    json.dump(
        validation_report,
        file,
        indent=4
    )

print("\n✅ Validation report created!")