import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


df = pd.read_csv('monthly_kpi_data.csv')

sns.set_style(style="whitegrid")
df['Month'] = pd.to_datetime(df['Month'])

df['Month_Label'] = df['Month'].dt.strftime("%B '%y")

# Revenue Line Chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Month_Label', y='Revenue', marker='o', linewidth=2.5, color='royalblue')

plt.title('Monthly Revenue', fontsize=16, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=12)
plt.xlabel('Month', fontsize=12)

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.savefig('revenue_trend.png')
plt.close()

# New vs Churned Bar Chart
df_bar = df[["Month_Label", "New_Customers", "Churned_Customers"]].melt(id_vars='Month_Label', var_name='Customer_Type', value_name='Count')

plt.figure(figsize=(10,5))
sns.barplot(data=df_bar, x='Month_Label', y='Count', hue='Customer_Type', palette='pastel')
plt.title('New vs Churned Customers', fontsize=16, fontweight='bold')
plt.ylabel('Number of Customers', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend(title='Customer Type', fontsize=10, title_fontsize='11')
plt.tight_layout()
plt.savefig('customer_turnover.png')
plt.close()

# Churn Rate Line Chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Month_Label', y='Churn_Rate', marker='o', linewidth=2.5, color='firebrick')

plt.title('Monthly Churn Rate', fontsize=16, fontweight='bold')
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.xlabel('Month', fontsize=12)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.savefig('churn_rate_trend.png')
plt.close()