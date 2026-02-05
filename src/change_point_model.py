import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
from data_loader import load_and_clean_data

def run_bayesian_model():
    # 1. Load data and filter for the 2005-2012 window (The 2008 Crisis)
    df = load_and_clean_data("data/raw/BrentOilPrices.csv")
    df_window = df[(df['Date'] >= '2005-01-01') & (df['Date'] <= '2012-12-31')].copy()
    
    # We use Price or Log_Price. For mean-shifts, Price is easier to visualize.
    data = df_window['Price'].values
    n_data = len(data)
    idx = np.arange(n_data)

    print(f"Running model on {n_data} days of data...")

    # 2. Build the Model
    with pm.Model() as model:
        # Prior for the switch point (tau): could be any day in the sequence
        tau = pm.DiscreteUniform("tau", lower=0, upper=n_data - 1)
        
        # Priors for the mean prices before and after
        mu_1 = pm.Normal("mu_1", mu=data.mean(), sigma=data.std())
        mu_2 = pm.Normal("mu_2", mu=data.mean(), sigma=data.std())
        
        # Standard deviation of the price (assumed constant for simplicity here)
        sigma = pm.HalfNormal("sigma", sigma=data.std())
        
        # The Switch logic: if index < tau, use mu_1, else use mu_2
        mu = pm.math.switch(tau > idx, mu_1, mu_2)
        
        # Likelihood: connect the model to the actual data
        observation = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)
        
        # 3. Sampling (MCMC)
        trace = pm.sample(2000, tune=1000, chains=2, return_inferencedata=True)

    # 4. Results & Visualization
    print(az.summary(trace, var_names=["mu_1", "mu_2", "tau"]))
    
    # Plot the posterior for tau (The Change Point)
    az.plot_posterior(trace, var_names="tau")
    plt.title("Posterior Distribution of Change Point (Index)")
    plt.savefig("notebooks/tau_posterior.png")
    
    return trace, df_window
def plot_regimes(df_window, trace):
    tau_samples = trace.posterior['tau'].values.flatten()
    mu1_samples = trace.posterior['mu_1'].values.flatten()
    mu2_samples = trace.posterior['mu_2'].values.flatten()
    
    tau_idx = int(np.median(tau_samples))
    
    plt.figure(figsize=(12, 6))
    plt.plot(df_window['Date'], df_window['Price'], label='Actual Price', alpha=0.5)
    
    # Draw the regimes
    plt.hlines(np.median(mu1_samples), df_window['Date'].min(), df_window.iloc[tau_idx]['Date'], 
               colors='r', linestyles='--', label='Regime 1 Mean')
    plt.hlines(np.median(mu2_samples), df_window.iloc[tau_idx]['Date'], df_window['Date'].max(), 
               colors='g', linestyles='--', label='Regime 2 Mean')
    
    plt.axvline(df_window.iloc[tau_idx]['Date'], color='k', label='Detected Change Point')
    plt.title('Oil Price Regimes: Pre vs Post Arab Spring')
    plt.legend()
    plt.savefig("notebooks/regime_shift_2010.png")

if __name__ == "__main__":
    # 1. Run the sampling
    trace, df_window = run_bayesian_model()
    
    # 2. Extract results for printing
    tau_samples = trace.posterior['tau'].values.flatten()
    most_likely_idx = int(np.median(tau_samples))
    change_date = df_window.iloc[most_likely_idx]['Date']
    print(f"\nDetected Change Point Date: {change_date}")
    
    # 3. CALL THE PLOT FUNCTION (Crucial step)
    print("Generating regime shift visualization...")
    plot_regimes(df_window, trace)
    print("Plot saved to notebooks/regime_shift_2010.png")