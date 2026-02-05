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
- **Assumption of Single/Multiple Breaks:** Our initial model assumes a structural break, but global markets may have dozens. We will start with a single switch-point model and evaluate if a multi-break model (Markov Switching) is required.
- **Lag Effect:** We assume events have an immediate impact, though policy changes (OPEC cuts) often have a 30-60 day transmission lag into actual prices.
- **Correlation vs. Causality:** A detected change point occurring on the same day as a Geopolitical event (e.g., 9/11) suggests a high correlation. However, without controlling for other variables (GDP, Dollar Strength, Inventory levels), we identify these as "Associated Causes" rather than "Proven Causality."