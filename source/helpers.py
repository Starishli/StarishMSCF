import numpy as np
from scipy.special import comb


def binom_calc(n, m, p):
    return comb(n, m) * np.power(p, m) * np.power(1 - p, n - m)


def calc_spot_rate(discount_factor, term, m=2):
    """
    Calculate spot rate, default by semiannual compounding
    :param discount_factor: discount factor
    :param term: term
    :param m: compounding freq
    :return: spot rate
    """
    r_hat = m * (np.power(1 / discount_factor, 1 / (m * term)) - 1)
    return r_hat


def calc_forward_rate(eta, t, r_eta, r_t, m=2):
    """
    Calculate forward rate, default by semiannual compounding
    :param eta: eta
    :param t: t
    :param r_eta: r_eta
    :param r_t:  r_t
    :param m: compounding freq
    :return: forward rate
    """
    part_eta = np.power(1 + r_eta / m, eta * m)
    part_t = np.power(1 + r_t / m, t * m)
    r_forward = m * (np.power(part_t / part_eta, 1 / ((t - eta) * m)) - 1)
    return r_forward


if __name__ == "__main__":
    print(calc_spot_rate(0.86322, 3.75, 4))
    print(calc_forward_rate(3, 3.75, 0.0394577, 0.0394158, 4))
