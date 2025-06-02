import pandas as pd

# Load the dataset
df = pd.read_csv("data/shift_offers.csv")
# Convert relevant columns to datetime
df["SHIFT_CREATED_AT"] = pd.to_datetime(df["SHIFT_CREATED_AT"])
df["OFFER_VIEWED_AT"] = pd.to_datetime(df["OFFER_VIEWED_AT"])
df["CLAIMED_AT"] = pd.to_datetime(df["CLAIMED_AT"])

# Calculate time delay in hours between shift posting and worker viewing
df["hours_after_posted"] = (df["OFFER_VIEWED_AT"] - df["SHIFT_CREATED_AT"]).dt.total_seconds() / 3600

# Determine 90th percentile threshold for high pay
p90_pay = df["PAY_RATE"].quantile(0.9)

# Filter to high-paying shift offers
high_pay_df = df[df["PAY_RATE"] >= p90_pay].copy()

# Bucket delays into human-readable categories
def categorize_delay(hours):
    if hours < 3:
        return "<3 hrs"
    elif 3 <= hours < 6:
        return "3–6 hrs"
    elif 6 <= hours < 12:
        return "6–12 hrs"
    else:
        return "12+ hrs"

high_pay_df["view_delay_bucket"] = high_pay_df["hours_after_posted"].apply(categorize_delay)

# Group by view delay and calculate claim rates
result = (
    high_pay_df.groupby("view_delay_bucket")
    .agg(
        total_offers=("SHIFT_ID", "count"),
        claimed_offers=("CLAIMED_AT", lambda x: x.notnull().sum())
    )
)

result["claim_rate_percent"] = round(100 * result["claimed_offers"] / result["total_offers"], 2)

print("Claim Rates for High-Pay Shift Offers by View Delay:")
print(result)

result.to_csv("data/high_pay_claim_rate_summary.csv")
