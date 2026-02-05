import pandas as pd
import numpy as np

def quantify_impact(df, change_date, event_name):
    # 1. Define windows (90 days before and after)
    before = df[df['Date'] < change_date].tail(90)
    after = df[df['Date'] >= change_date].head(90)
    
    mu_before = before['Price'].mean()
    mu_after = after['Price'].mean()
    
    vol_before = before['Price'].std()
    vol_after = after['Price'].std()
    
    perc_change = ((mu_after - mu_before) / mu_before) * 100
    vol_change = ((vol_after - vol_before) / vol_before) * 100
    
    print(f"\n--- Impact Report: {event_name} ---")
    print(f"Detected Date: {change_date.date()}")
    print(f"Average Price Shift: {mu_before:.2f} -> {mu_after:.2f} ({perc_change:+.2f}%)")
    print(f"Volatility (Risk) Shift: {vol_before:.2f} -> {vol_after:.2f} ({vol_change:+.2f}%)")
    
    return {
        'Event': event_name,
        'Date': change_date,
        'Price_Change_%': perc_change,
        'Vol_Change_%': vol_change
    }

if __name__ == "__main__":
    # Load data and events
    from data_loader import load_and_clean_data
    df = load_and_clean_data("data/raw/BrentOilPrices.csv")
    events = pd.read_csv("data/raw/external_events.csv")
    events['Date'] = pd.to_datetime(events['Date'])
    
    # Let's test our detected point: 2010-12-16
    detected_tau = pd.Timestamp('2010-12-16')
    
    # Find the closest event in our list
    events['diff'] = (events['Date'] - detected_tau).abs()
    closest_event = events.sort_values('diff').iloc[0]
    
    result = quantify_impact(df, detected_tau, closest_event['Event'])