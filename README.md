# Brent Oil Price - Bayesian Change Point Analysis
**Birhan Energies | Data Science Workflow**

## 📌 Project Overview
This project analyzes structural breaks in Brent Crude Oil prices (1987-2022). Using Bayesian Inference (PyMC), we detect "Change Points" where market regimes shifted due to geopolitical and economic shocks, providing Birhan Energies with actionable intelligence on price volatility.

## 📁 Project Documentation
*   [Technical Workflow & Assumptions](./analysis_plan.md): Detailed look at stationarity, causality, and stakeholder communication.
*   [Events Dataset](./data/external_events.csv): 15 global shocks used for model validation.

## 🛠️ Repository Structure
- `data/`: Raw Brent Oil prices and researched external events CSV.
- `src/`: Data loading, statistical profiling (ADF tests), and Bayesian modeling.
- `notebooks/`: Visualization outputs and statistical reports.
- `reports/`: Documented analysis plan and methodology.

## 📈 Key Findings (Task 1 & 2)
### 1. Data Stationarity
- **Raw Price:** Non-stationary (ADF p-value: 0.29).
- **Log Returns:** Stationary (ADF p-value: 2.5e-29).
- **Inference:** Modeling structural breaks on mean price levels requires piecewise regression to handle non-stationarity.

### 2. Bayesian Model Discovery
- **Detected Change Point:** 2010-12-16.
- **Event Association:** Closely linked to the onset of the **Libyan Civil War / Arab Spring**.
- **Regime Shift Impact:**
    - **Price Level:** Shifted from ~$81.70 to ~$107.22 (+31.23%).
    - **Volatility (Risk):** Increased by +116.42%.
- **Model Convergence:** Sampling achieved an **R-hat of 1.0**, indicating high reliability.

## 🚀 Setup and Installation
1. Clone the repository.
2. Create virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run EDA: `python3 src/eda_profiler.py`
5. Run Bayesian Model: `python3 src/change_point_model.py`