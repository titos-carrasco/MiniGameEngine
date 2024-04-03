# https://orthallelous.wordpress.com/2020/06/21/pure-python-bezier-curve/
from math import comb as r


def bz(c, n=10, t=False):
    m, q, p, s = list(zip(*c)), len(c), [], (n - 1 if t else n) / 1.0
    for i in range(n):
        b = [
            r(q - 1, v) * (i / s) ** v * (1 - (i / s)) ** (q - 1 - v) for v in range(q)
        ]
        p += [(tuple(sum(j * k for j, k in zip(d, b)) for d in m))]
    return p
