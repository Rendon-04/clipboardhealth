# Clipboard Health Shift Claim Analysis

This project explores behavioral patterns in Clipboard Health's two-sided marketplace,
specifically looking at how the *delay between shift posting and offer view* impacts 
whether high-paying shifts get claimed.

## Key Insight

Even for the top 10% highest-paying shifts, workers were far less likely to claim shifts
viewed 12+ hours after posting. Early visibility dramatically increases claim rates.

## Tools

- Python
- pandas

## Output

The script calculates claim rates by delay time frames:

| Delay Bucket | Claim Rate |
|--------------|------------|
| `<3 hrs`     | 22.98%     |
| `3–6 hrs`    | 10.20%     |
| `6–12 hrs`   | 10.01%     |
| `12+ hrs`    | 5.08%      |

## 📌 Recommendation

Introduce urgency features in the app: "Newly Posted" filters, push alerts for higer pay,
and visibility expiration to improve early match speeds.
