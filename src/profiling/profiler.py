import pandas as pd
import json
import os

def infer_column_type(column_name):
    name = column_name.lower()

    if "email" in name:
        return "EMAIL"

    elif "name" in name:
        return "NAME"

    elif "phone" in name:
        return "PHONE"

    elif "date" in name:
        return "DATE"

    elif "id" in name:
        return "ID"

    elif "amount" in name:
        return "NUMERIC"

    else:
        return "UNKNOWN"

# Load dataset
df = pd.read_csv("data/raw/banking_transactions_505k.csv")

# Semantic types
column_types = {}

for column in df.columns:
    column_types[column] = infer_column_type(column)

# PII Detection
pii_columns = []

for column in df.columns:
    name = column.lower()

    if any(
        keyword in name
        for keyword in ["name", "email", "phone", "id"]
    ):
        pii_columns.append(column)

# Data Quality Score
total_cells = df.shape[0] * df.shape[1]

missing_cells = df.isnull().sum().sum()

quality_score = round(
    (1 - (missing_cells / total_cells)) * 100,
    2
)

# Unique Values & Cardinality

unique_values = {}
cardinality = {}

for column in df.columns:

    unique_count = df[column].nunique()

    unique_values[column] = int(unique_count)

    cardinality[column] = round(
        (unique_count / len(df)) * 100,
        2
    )

    # Suspicious Columns

suspicious_columns = []

for column in df.columns:

    if df[column].isnull().sum() > 0:
        suspicious_columns.append(column)


# Inconsistent Formats

inconsistent_formats = {}

gender_values = (
    df["gender"]
    .dropna()
    .unique()
    .tolist()
)

inconsistent_formats["gender"] = gender_values


# Report

report = {
    "rows": int(df.shape[0]),
    "columns": int(df.shape[1]),
    "duplicates": int(df.duplicated().sum()),
    "data_quality_score": quality_score,

    "unique_values": unique_values,
    "cardinality": cardinality,

    "missing_values": df.isnull().sum().to_dict(),
    "data_types": df.dtypes.astype(str).to_dict(),

    "semantic_types": column_types,
    "pii_columns": pii_columns,

    "suspicious_columns": suspicious_columns,
    "inconsistent_formats": inconsistent_formats
}


# Create folder

os.makedirs(
    "reports/profiling",
    exist_ok=True
)


# Save report

with open(
    "reports/profiling/profiling_report.json",
    "w"
) as file:
    json.dump(
        report,
        file,
        indent=4
    )


print("✅ Profiling report created successfully!")