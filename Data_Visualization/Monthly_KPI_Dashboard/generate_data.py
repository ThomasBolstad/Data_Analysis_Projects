import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate monthly labels (use 'ME' for month-end to avoid the FutureWarning)
months=pd.date_range(start='2023-01-01',periods=12, freq='ME').strftime('%Y-%m')

# Create dummy business KPI data
data = {
    "Month": months,
    "Total_Customers": np.random.randint(800, 1200, size=12),
    "New_Customers": np.random.randint(100, 300, size=12),
    "Churned_Customers": np.random.randint(50, 150, size=12),
    "Revenue": np.random.randint(80000, 120000, size=12)
}

# Build DataFrame
df = pd.DataFrame(data)

# Add churn rate
df["Churn_Rate"] = (df["Churned_Customers"] / df["Total_Customers"]).round(3)

# Preview in terminal
print(df.head())

# Save CSV to the same folder as the script
file_path = "monthly_kpi_data.csv"
df.to_csv(file_path, index=False)

print(f"\n✅ CSV file saved as: {file_path}")
