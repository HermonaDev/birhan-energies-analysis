import pandas as pd
import os

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data not found at {file_path}")
    
    df = pd.read_csv(file_path)
    
    # format='mixed' handles the multiple date formats in your CSV automatically
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False)
    
    # Sort and Clean
    df = df.sort_values('Date').reset_index(drop=True)
    df = df.rename(columns={'Price': 'Price'})
    
    # Interpolate missing values (e.g., weekends/holidays if gaps exist)
    df['Price'] = df['Price'].interpolate(method='linear')
    
    return df

if __name__ == "__main__":
    DATA_PATH = "data/raw/BrentOilPrices.csv"
    try:
        data = load_and_clean_data(DATA_PATH)
        print(f"Success! Data covers {data['Date'].min()} to {data['Date'].max()}")
        print(data.sample(5)) # Check random rows to see if parsing worked everywhere
    except Exception as e:
        print(f"Error: {e}")