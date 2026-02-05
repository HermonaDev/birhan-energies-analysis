import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from data_loader import load_and_clean_data
from data_loader import load_and_clean_data

def run_eda(df: pd.DataFrame):
    # 1. Visualize the series
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Prices (1987-2022)')
    plt.ylabel('USD per Barrel')
    plt.grid(True)
    plt.savefig('notebooks/oil_price_raw.png')
    
    # 2. Stationarity Test
    print("--- ADF Test Results ---")
    result = adfuller(df['Price'])
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    if result[1] > 0.05:
        print("Data is NON-STATIONARY. We should model Log Returns for Task 2.")
    else:
        print("Data is STATIONARY.")

def transform_data(df):
    # Calculate Log Returns
    df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))
    df = df.dropna() # Remove the first row which becomes NaN
    
    # Plot Log Returns
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Log_Return'], color='orange', alpha=0.7)
    plt.title('Brent Oil Log Returns (1987-2022)')
    plt.savefig('notebooks/oil_log_returns.png')
    
    # Re-test ADF
    print("--- ADF Test on Log Returns ---")
    result = adfuller(df['Log_Return'])
    print(f'p-value: {result[1]}')
    return df

if __name__ == "__main__":
    df = load_and_clean_data("data/raw/BrentOilPrices.csv")
    run_eda(df)
    df = transform_data(df)