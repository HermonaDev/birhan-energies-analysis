# Birhan Energies: Strategic Framework

## 1. Event Dataset & Workflow Attribution
This analysis is anchored by the `data/external_events.csv` artifact, containing 15 high-impact geopolitical shocks. These events are used in the `Master_Analysis.ipynb` notebook to validate Bayesian Change Point detection results.

## 2. Assumptions & Limitations
*   **Stationarity:** We assume Log Returns represent a stationary process for volatility analysis.
*   **Causality:** We identify **Associated Triggers**. While the Bayesian model identifies a structural break on Dec 16, 2010, we define the Arab Spring as the primary *association* based on temporal proximity, acknowledging that global inventory levels also contribute to variance.

## 3. Error Handling & Code Quality
*   **Backend:** Flask APIs include `try/except` blocks to handle missing data or empty datasets gracefully.
*   **Validation:** Input CSVs are parsed with `mixed` date formats to prevent runtime crashes.
