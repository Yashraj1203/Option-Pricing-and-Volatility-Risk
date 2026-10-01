# Options Pricing & Volatility Risk Engine

A robust, production-grade Python framework for quantitative finance, designed to price European derivatives, simulate terminal stock paths via Monte Carlo, evaluate price sensitivity through Greeks, and perform rigorous pricing error and convergence analysis.

---

## Project Overview

A quantitative pricing and risk analytics engine built to bridge theoretical derivatives pricing models with practical simulation and error analysis. It supports:
- **Analytical Pricing**: Closed-form Black-Scholes valuations for European call and put options.
- **Monte Carlo Simulation**: Terminal Geometric Brownian Motion (GBM) path simulation with configurable random seed reproducibility.
- **Statistical & Error Analytics**: Standard errors, 95% confidence intervals, and pricing discrepancies against benchmark solutions.
- **Automated Verification**: Put-Call parity validation and Monte Carlo convergence stability checks.

---

## Project Directory Structure

```text
Options_Pricing_Engine/
│
├── Python/
│   ├── option_pricing_engine.py      
│   └── run_research.py               
│
├── Tests/
│   └── test_option_pricing.py        
│
├── Data/
│   ├── mc_convergence.csv           
│   └── mc_convergence_live_run.csv    
│                            
│
├── requirements.txt                  
└── README.md                         
```

---

## Mathematical Framework

### 1. Black-Scholes Analytical Pricing
The analytical price for European options under the Black-Scholes model is given by:

$$C(S_0, K, r, \sigma, T) = S_0 N(d_1) - K e^{-rT} N(d_2)$$

$$P(S_0, K, r, \sigma, T) = K e^{-rT} N(-d_2) - S_0 N(-d_1)$$

Where:
- $d_1 = \frac{\ln(S_0 / K) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}}$
- $d_2 = d_1 - \sigma \sqrt{T}$
- $S_0$: Initial spot price
- $K$: Strike price
- $r$: Risk-free interest rate
- $\sigma$: Volatility
- $T$: Time to maturity (years)
- $N(\cdot)$: Cumulative standard normal distribution function

### 2. Monte Carlo Simulation (Geometric Brownian Motion)
Terminal stock prices $S_T$ are simulated under risk-neutral pricing using:

$$S_T = S_0 \exp\left( \left(r - \frac{1}{2}\sigma^2\right)T + \sigma\sqrt{T} Z \right)$$

Where $Z \sim \mathcal{N}(0, 1)$. Discounted payoffs converge to the analytical Black-Scholes price at a rate of $O(1/\sqrt{N})$, where $N$ is the number of simulation paths.

---

## Developed by
[Yashraj1203](https://github.com/Yashraj1203)

---


