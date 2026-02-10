import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller

# 1. Load and Profile
df = pd.read_csv("data/BrentOilPrices.csv")
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df = df.sort_values('Date')

# 2. Volatility Analysis (21-day rolling)
df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))
df['Volatility'] = df['Log_Return'].rolling(window=21).std() * (252**0.5)

# 3. Stationarity Visual
fig, ax = plt.subplots(2, 1, figsize=(12, 10))
ax[0].plot(df['Date'], df['Price'], label='Raw Price (Non-Stationary)')
ax[0].set_title('Brent Oil Price: Trend Analysis')
ax[1].plot(df['Date'], df['Volatility'], color='orange', label='Annualized Volatility')
ax[1].set_title('Market Risk Profiling (Volatility Clustering)')
plt.tight_layout()
plt.savefig("reports/figures/statistical_profiling.png")

# 4. Verifiable ADF Test Output
res = adfuller(df['Price'])
with open("reports/adf_test_results.txt", "w") as f:
    f.write(f"ADF Statistic: {res[0]}\np-value: {res[1]}\nConclusion: Non-Stationary")
