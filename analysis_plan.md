# Analysis Plan: Brent Oil Structural Break Analysis
**Client:** Birhan Energies  
**Analyst:** Hermona Addisu

## 1. Workflow Objectives
To identify significant geopolitical and economic "Change Points" in Brent Crude oil prices (1987-2022) using Bayesian Inference.

## 2. Methodology Steps
1. **Data Profiling:** Transformation of raw prices into Log Returns to stabilize variance and ensure stationarity (Validated via ADF Test, p < 0.05).
2. **Change Point Modeling (PyMC):**
   - Implement a Bayesian model using a **Discrete Uniform prior** for the switch point ($\tau$).
   - Use **Normal distributions** for the means before ($\mu_1$) and after ($\mu_2$) the break.
   - Employ the **MCMC (NUTS sampler)** to generate posterior distributions.
3. **Causal Attribution:** Cross-reference detected change points with the `external_events.csv` timeline.
4. **Impact Quantification:** Measure the standard deviation shifts and mean price changes across different regimes.

## 3. Expected Outputs
- **Posterior Plots:** Visualizing the probability of *exactly when* a shift happened.
- **Regime Classification:** Categorizing periods as "Low Volatility/Stable" vs "High Volatility/Crisis."
- **Interactive Dashboard:** A Flask-React tool for stakeholders to "scrub" through the timeline and see event highlights.

## 4. Assumptions and Limitations
# Birhan Energies: Strategic Framework

## 4.1. Explicit Assumptions & Limitations
*   **Linear Mean Assumption:** Our model assumes a "step function" change in price levels. It may miss subtle non-linear drifts between regimes.
*   **Data Caveats:** The dataset does not account for the **US Dollar Index (DXY)** or **Global Inventory levels**, which are major latent variables in oil pricing.

## 4.2. Correlation vs. Causality
*   **The Model's Role:** Bayesian Change Point Analysis identifies *when* the distribution shifted. It does not "know" why.
*   **Association Logic:** We associate the 2010 shift with the Arab Spring due to temporal proximity. We define this as a **Probabilistic Association**, acknowledging that while the war was the primary driver, macro-demand also contributed to the final price level.

## 4.3. Communication Strategy
*   **Investors:** Bi-weekly volatility risk summaries.
*   **Policymakers:** Annual regime stability reports.
