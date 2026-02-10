from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# --- Path Intelligence ---
# This finds the absolute path of the directory this script is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to find the project root, then into data/
DATA_FILE = os.path.join(BASE_DIR, "../../data/raw/BrentOilPrices.csv")
EVENTS_FILE = os.path.join(BASE_DIR, "../../data/raw/external_events.csv")

print(f"DEBUG: Looking for Prices at: {os.path.abspath(DATA_FILE)}")
print(f"DEBUG: Looking for Events at: {os.path.abspath(EVENTS_FILE)}")

@app.route('/api/prices')
def get_prices():
    try:
        df = pd.read_csv(DATA_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format='mixed')
        df = df[df['Date'] >= '2005-01-01']
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        print(f"ERROR loading prices: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/analysis')
def get_analysis():
    return jsonify({
        "date": "2010-12-16",
        "price_shift": "+31.23%",
        "risk_delta": "+116.42%",
        "mu1": 71.54,
        "mu2": 110.98,
        "event": "Arab Spring Onset"
    })

@app.route('/api/events')
def get_events():
    try:
        if not os.path.exists(EVENTS_FILE):
            print(f"CRITICAL: {EVENTS_FILE} NOT FOUND")
            return jsonify([{"Date": "Error", "Event": f"File not found at {EVENTS_FILE}"}])
            
        df_events = pd.read_csv(EVENTS_FILE)
        print(f"SUCCESS: Loaded {len(df_events)} events")
        return jsonify(df_events.to_dict(orient='records'))
    except Exception as e:
        print(f"ERROR loading events: {e}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, port=5000)