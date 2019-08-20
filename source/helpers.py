import numpy as np
from scipy.special import comb


def binom_calc(n, m, p):
    return comb(n, m) * np.power(p, m) * np.power(1 - p, n - m)



