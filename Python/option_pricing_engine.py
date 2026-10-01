import numpy as np
from scipy.stats import norm

def simulate_gbm_terminal(S0, r, sigma, T, n_paths, seed=42):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n_paths)
    return S0*np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T)*z)

def black_scholes_price(S0,K,r,sigma,T,option_type="call"):
    d1=(np.log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    if option_type=="call":
        return S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    return K*np.exp(-r*T)*norm.cdf(-d2)-S0*norm.cdf(-d1)

def monte_carlo_price(S0,K,r,sigma,T,n_paths=100000,seed=42,option_type="call"):
    st=simulate_gbm_terminal(S0,r,sigma,T,n_paths,seed)
    payoff=np.maximum(st-K,0) if option_type=="call" else np.maximum(K-st,0)
    discounted=np.exp(-r*T)*payoff
    price=discounted.mean()
    se=discounted.std(ddof=1)/np.sqrt(n_paths)
    return price,se,(price-1.96*se,price+1.96*se)
