from pathlib import Path
import pandas as pd
from option_pricing_engine import monte_carlo_price, black_scholes_price

# Set output directory and ensure it exists
OUT = Path(__file__).resolve().parents[1] / "Data"
OUT.mkdir(parents=True, exist_ok=True)

S0, K, r, sigma, T = 100, 100, 0.05, 0.20, 1.0
rows = []

for n in [1000, 5000, 10000, 50000, 100000]:
    for typ in ["call", "put"]:
        mc, se, ci = monte_carlo_price(S0, K, r, sigma, T, n, 20260925, typ)
        bs = black_scholes_price(S0, K, r, sigma, T, typ)
        rows.append([n, typ, mc, bs, mc - bs, se, *ci])

df = pd.DataFrame(rows, columns=["Paths", "Option", "MC Price", "Black-Scholes", "Error", "Std Error", "CI Lower", "CI Upper"])
df.to_csv(OUT / "mc_convergence_live_run.csv", index=False)
print("Saved MC convergence output successfully to Data/mc_convergence_live_run.csv.")