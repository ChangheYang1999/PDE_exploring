"""p-adic digits of kappa (first compatibility coefficient) at delta=a/p, a odd; f1 = sin theta (or given profile).
Usage: kappa_odd_digits.py pmin pmax [profile]"""
import sys
from fractions import Fraction as Fr
from kappa_odd import run, is_prime


def digits(x, p, lo=-4, hi=1):
    # p-adic digits of x from valuation lo to hi
    out = []
    y = x * Fr(p) ** (-lo)
    if y.denominator % p == 0:
        return 'val<%d' % lo
    for k in range(lo, hi + 1):
        num, den = y.numerator, y.denominator
        d = (num * pow(den, -1, p)) % p
        out.append(d)
        y = (y - d) / p
    return out


if __name__ == '__main__':
    pmin, pmax = int(sys.argv[1]), int(sys.argv[2])
    prof = sys.argv[3] if len(sys.argv) > 3 else 'sin1'
    f1 = {1: Fr(1)} if prof == 'sin1' else {int(t.split(':')[0]): Fr(t.split(':')[1]) for t in prof.split(',')}
    for p in range(pmin, pmax + 1):
        if not is_prime(p):
            continue
        for a in range(3, p, 2):
            f, g = run(a, p, f1, 2 * p)
            kap = f[2 * p].get(2 * a - 3, Fr(0))
            print(f"p={p} a={a} digits(v=-4..1)={digits(kap, p)}", flush=True)
