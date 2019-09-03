from math import factorial as fac


def ii_c_26(x):
    nominator = fac(14) * fac(10) * fac(6 + x) * fac(17 - x)
    denominator = fac(6) * fac(7) * fac(24) * fac(x) * fac(10 - x)
    return nominator / denominator


print(1 - ii_c_26(0) - ii_c_26(1) - ii_c_26(2) - ii_c_26(3))