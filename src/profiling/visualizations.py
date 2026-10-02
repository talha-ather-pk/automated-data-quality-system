import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/banking_transactions_505k.csv")

# Missing values heatmap
plt.figure(figsize=(12, 6))

sns.heatmap(
    df.isnull(),
    cbar=False
)

plt.title("Missing Values Heatmap")

plt.savefig(
    "reports/profiling/missing_values_heatmap.png"
)

plt.close()

print("✅ Missing values heatmap created!")

# Correlation Heatmap

numeric_cols = [
    "age",
    "transaction_amount",
    "credit_score",
    "account_balance",
    "loan_amount"
]

corr = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "reports/profiling/correlation_heatmap.png"
)

plt.close()

print("✅ Correlation heatmap created!")
