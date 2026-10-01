import sys
sys.path.insert(0, "Python")
from option_pricing_engine import black_scholes_price, monte_carlo_price

def test_put_call_parity():
    c=black_scholes_price(100,100,.05,.20,1,"call")
    p=black_scholes_price(100,100,.05,.20,1,"put")
    assert abs((c-p)-(100-100*__import__("math").exp(-.05)))<1e-10

def test_mc_confidence_interval():
    mc,se,ci=monte_carlo_price(100,100,.05,.20,1,100000,42,"call")
    assert ci[0] <= mc <= ci[1]
    assert se > 0

if __name__=="__main__":
    test_put_call_parity()
    test_mc_confidence_interval()
    print("ALL TESTS PASSED")
