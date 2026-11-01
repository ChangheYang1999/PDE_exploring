"""Independent check of the lead's odd-numerator claim (theory 10.1; a4-lead code/oddnum): for delta = a/p, p >= 5 prime, 3 <= a < p odd, f_1 = sin theta,
the first stream resonance is at n0 = 2p, j0 = a - 1, and the compatibility coefficient kappa_odd = coefficient of sin((2a-3) theta) in f_(2p) (exact
rationals, lane recursion ffcore.FarField with RingQ). Prints kappa_odd, v_p(kappa_odd) and the p-adic digits at valuations -4..1 in the lead's format.
usage: kappa_odd_check.py pmax"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpq, fmpz
def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def padic_digits(x, p, vmin=-4, vmax=1):
    """digits d_v, v = vmin..vmax, of the p-adic expansion of the rational x (requires v_p(x) >= vmin)"""
    y = x * fmpq(p) ** (-vmin); digits = []
    for _ in range(vmax - vmin + 1):
        num, den = int(y.p), int(y.q); assert den % p != 0, 'valuation below vmin'
        d = (num * pow(den, -1, p)) % p; digits.append(d); y = (y - d) / p
    return digits
def vp(x, p):
    if x == 0: return None
    num, den = int(x.p), int(x.q); v = 0
    while num % p == 0: num //= p; v += 1
    while den % p == 0: den //= p; v -= 1
    return v
pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 23
R = RingQ(); cnt = 0; zeros = 0
for p in [q for q in range(5, pmax + 1) if is_prime(q)]:
    for a in range(3, p, 2):
        delta = fmpq(a, p); cl = 1 / (1 - delta); ff = FarField(R, cl, [R.scalar(1)]); n0 = 2 * p
        for n in range(2, n0 + 1): ff.step()
        f = ff.f[n0]; k = a - 2; kappa = f[k] if k < len(f) else fmpq(0); cnt += 1
        if kappa == 0: zeros += 1; print(f'p={p} a={a} KAPPA = 0'); continue
        print(f'p={p} a={a} digits(v=-4..1)={padic_digits(kappa, p)} v_p={vp(kappa, p)} kappa={float(kappa):.6e}')
        sys.stdout.flush()
print(f'{cnt} pairs, {zeros} with kappa = 0')
