from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Standardized Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "../../data/BrentOilPrices.csv")
EVENTS_FILE = os.path.join(BASE_DIR, "../../data/external_events.csv")

@app.route('/api/prices')
def get_prices():
    try:
        # Check if file exists (Defensive check)
        if not os.path.exists(DATA_FILE):
            raise FileNotFoundError(f"Missing data file at {DATA_FILE}")
            
        df = pd.read_csv(DATA_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format='mixed')
        df = df[df['Date'] >= '2005-01-01']
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        
        # Validate data is not empty
        if df.empty:
            return jsonify({"error": "Price dataset is empty"}), 404
            
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analysis')
def get_analysis():
    # Return quantified impact narrative
    return jsonify({
        "date": "2010-12-16",
        "price_shift": "+31.23%",
        "risk_delta": "+116.42%",
        "mu1": 71.54,
        "mu2": 110.98,
        "interpretation": "Regime shift triggered by Arab Spring geopolitical shocks."
    })

@app.route('/api/events')
def get_events():
    try:
        if not os.path.exists(EVENTS_FILE):
            return jsonify([]) # Return fallback empty list
        df_events = pd.read_csv(EVENTS_FILE)
        return jsonify(df_events.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": "Failed to load events"}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000) # Set debug=False for production readiness
