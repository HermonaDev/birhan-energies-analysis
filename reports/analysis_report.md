# Birhan Energies: Technical Analysis Framework

## 1. Assumptions & Limitations
### Technical Assumptions
*   **Stationarity:** We assume that while raw prices are non-stationary, Log Returns provide a stable variance for Bayesian Switch-point modeling.
*   **Likelihood:** We assume a Normal distribution for prices within a regime. Future iterations may test Student-T distributions to better handle "fat-tail" price shocks.

### Correlation vs. Causality
*   **Association:** Our model identifies statistical "Change Points" where the price distribution shifts. While these often align with geopolitical events (e.g., Arab Spring), the model identifies *correlation* in time.
*   **Causal Limitation:** We acknowledge that Brent prices are influenced by a web of factors (USD strength, interest rates, inventory levels). We define events as "Associated Triggers" rather than isolated causes.

## 2. Stakeholder Communication Plan
To ensure actionable intelligence, results will be communicated via the following channels:

| Stakeholder | Channel | Format | Frequency |
| :--- | :--- | :--- | :--- |
| **Investors** | Interactive Dashboard | Risk-Volatility Heatmaps & Sharpe Ratio Analysis | Daily/Real-time |
| **Policymakers** | Executive Summary Reports | Policy Briefs on Energy Security & Sanction Impacts | Quarterly |
| **Energy Companies** | Direct API Access | JSON Feeds of Change Point Probabilities for Supply Chain Ops | Real-time |

## 3. Communication Formats
1.  **Technical Blog:** Deep-dive into Bayesian math and MCMC convergence for the Data Science team.
2.  **Executive Memo:** 2-page summary highlighting % shifts in price and risk for C-suite decision-makers.
3.  **Live Dashboard:** React-based tool for "What-If" scenario scrubbing.
