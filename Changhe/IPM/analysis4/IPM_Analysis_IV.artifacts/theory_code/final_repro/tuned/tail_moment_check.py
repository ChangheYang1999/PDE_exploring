"""Independent check of the moment identity of the explicit tail bounds:
sum_{k>=K} (m+Qk)^(d-1) t^k = (m + Q t d/dt)^(d-1) [t^K/(1-t)], and the d = 0 bound, in exact rationals."""
from fractions import Fraction as Fr

def op(poly_num, Kpow, m, Q):
    # represent f(t) = sum_j c_j t^j / (1-t)^p as dict {(j,p): c}; apply m + Q t d/dt
    out = {}
    for (j, p), c in poly_num.items():
        # t d/dt [t^j (1-t)^-p] = j t^j (1-t)^-p + p t^(j+1) (1-t)^-(p+1)
        for key, v in (((j, p), (m + Q * j) * c), ((j + 1, p + 1), Q * p * c)):
            out[key] = out.get(key, 0) + v
    return out

def A(d, m, K, t, Q):
    if d == 0:
        return t ** K / ((m + Q * K) * (1 - t))
    f = {(K, 1): Fr(1)}
    for _ in range(d - 1):
        f = op(f, K, m, Q)
    return sum(c * t ** j / (1 - t) ** p for (j, p), c in f.items())

bad = 0
for Q in (5, 9):
    for m in (19, 27, 36):
        for K in (0, 1, 3):
            for t in (Fr(1, 2), Fr(1, 512), Fr(3, 7)):
                for d in range(0, 5):
                    S = sum(Fr(m + Q * k) ** (d - 1) * t ** k for k in range(K, K + 400))
                    a = A(d, m, K, t, Q)
                    tail = a - S
                    # truncated sum is below the closed form; the remainder is tiny for 400 terms
                    ok = tail >= 0 and (d == 0 or tail < Fr(1, 10 ** 30) * a)
                    bad += not ok
print('checks', 2 * 3 * 3 * 3 * 5, 'bad', bad)
