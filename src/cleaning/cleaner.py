import pandas as pd
import json


# Load dataset
df = pd.read_csv(
    "data/raw/banking_transactions_505k.csv"
)

print("Original Shape:")
print(df.shape)

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_removed = duplicates_before

print("\nDuplicates Removed:")
print(duplicates_removed)

print("\nNew Shape:")
print(df.shape)

# Fill missing age values

age_missing_before = df["age"].isnull().sum()

df["age"] = df["age"].fillna(
    df["age"].median()
)

age_missing_after = df["age"].isnull().sum()

# Fill missing credit score values

credit_missing_before = df["credit_score"].isnull().sum()

df["credit_score"] = df["credit_score"].fillna(
    df["credit_score"].median()
)

credit_missing_after = df["credit_score"].isnull().sum()

print("\nAge Missing Before:")
print(age_missing_before)

print("Age Missing After:")
print(age_missing_after)

print("\nCredit Score Missing Before:")
print(credit_missing_before)

print("Credit Score Missing After:")
print(credit_missing_after)
# Standardize Gender Values

print("\nUnique Gender Values Before:")
print(df["gender"].unique())

df["gender"] = (
    df["gender"]
    .astype(str)
    .str.upper()
)

df["gender"] = df["gender"].replace({
    "M": "MALE",
    "MALE": "MALE",
    "F": "FEMALE",
    "FEMALE": "FEMALE"
})

print("\nUnique Gender Values After:")
print(df["gender"].unique())
# Email Validation

email_missing_before = df["email"].isnull().sum()

invalid_email_mask = ~df["email"].astype(str).str.contains(
    "@",
    na=False
)

invalid_emails = invalid_email_mask.sum()

df.loc[
    invalid_email_mask,
    "email"
] = pd.NA

email_missing_after = df["email"].isnull().sum()

print("\nInvalid Emails Found:")
print(invalid_emails)

print("\nEmail Missing After Cleaning:")
print(email_missing_after)

# Phone Validation

phone_missing_before = df["phone"].isnull().sum()

invalid_phone_mask = (
    df["phone"]
    .astype(str)
    .str.len() < 10
)

invalid_phones = invalid_phone_mask.sum()

df.loc[
    invalid_phone_mask,
    "phone"
] = pd.NA

phone_missing_after = df["phone"].isnull().sum()

print("\nInvalid Phones Found:")
print(invalid_phones)

print("\nPhone Missing After Cleaning:")
print(phone_missing_after)

# Create cleaned data folder

import os

os.makedirs(
    "data/cleaned",
    exist_ok=True
)

# Save cleaned dataset

df.to_csv(
    "data/cleaned/cleaned_data.csv",
    index=False
)

print("\n✅ Cleaned dataset saved!")
# Cleaning Log

cleaning_log = {
    "duplicates_removed": int(duplicates_removed),
    "age_missing_filled": int(age_missing_before),
    "credit_score_missing_filled": int(credit_missing_before),
    "invalid_emails_found": int(invalid_emails),
    "invalid_phones_found": int(invalid_phones)
}
with open(
    "reports/cleaning_log.json",
    "w"
) as file:
    json.dump(
        cleaning_log,
        file,
        indent=4
    )

print("✅ Cleaning log created!")