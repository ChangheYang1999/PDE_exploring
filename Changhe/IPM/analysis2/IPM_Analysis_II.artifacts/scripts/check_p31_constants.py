"""Second recomputation of the P31 constants (B_K of P31.1 and Bnew_K of P31.2) with mpmath interval arithmetic.

Independent of python-flint: exponent sums in closed form, D_K as an interval product, C_K from the compressed
Volterra bound (B_K, P31.1), Q_n from the exponential derivative bound (Bnew_K, P31.2), e_m read from the shipped
leading sine coefficients. Writes check_p31_constants.json next to this file. Every interval endpoint is stored
exactly as [signed mantissa, binary exponent]; the decimal fields are rounded outward (lo down, hi up) to 15 digits.
The threshold comparisons are made against exact rational decimals.

Usage: python3 check_p31_constants.py certificates/P25_admissible_tail_gap/nb_stableA2_exact.annular.json
"""
import json, sys, hashlib
from fractions import Fraction as Q
from pathlib import Path
from mpmath import iv, mp
sys.set_int_max_str_digits(0)
iv.prec = 400
mp.prec = 400
def frac(t):
    """exact value of a raw mpf tuple (sign, mantissa, exponent, bitcount); man_exp alone drops the sign."""
    sign, man, e, bc = t
    if not man:
        assert not e, 'infinite or undefined endpoint'
        return Q(0)
    v = Q(int(man)) * Q(2)**int(e)
    return -v if sign else v
def dec(q, up):
    # 15 significant digits, rounded down (up=False) or up (up=True)
    if q == 0: return '0'
    k = len(str(abs(q.numerator))) - len(str(q.denominator))   # 10^(k-1) <= |q| < 10^k after the adjustment below
    while abs(q) >= Q(10)**k: k += 1
    while abs(q) < Q(10)**(k-1): k -= 1
    e = k - 15
    n = q / Q(10)**e if e >= 0 else q * Q(10)**(-e)
    n = -((-n.numerator)//n.denominator) if up else n.numerator//n.denominator
    return f"{n}e{e}"
lo = lambda x: dec(frac(x._mpi_[0]), False)
hi = lambda x: dec(frac(x._mpi_[1]), True)
ex = lambda x: [[(-1 if t[0] else 1) * int(t[1]), int(t[2])] for t in x._mpi_]   # signed mantissa, exponent
ann = Path(sys.argv[1])
c = Q(4076476460239181, 2251799813685248); g = 1/c; d = 1-g; astar = 7*d/2-2
es = {int(m): Q(v) for m, v in json.loads(ann.read_text())['leading_sine_coefficients'].items()}
I = lambda q: iv.mpf(q.numerator)/q.denominator
def S_closed(K):
    n = 2*K+5
    full = 78*d*n + 12*(n-1)*n - 36*n          # sum over l=1..12, k=0..2K+4 of (l*delta+2k-3)
    return full - (24*d-20)                    # remove the eight exponents below a_star
def B(K):
    exps = []
    for l in range(1, 13):
        for k in range(2*K+5):
            a = l*d/2+k-2
            if a > astar: exps.append(a)
    assert len(exps) == 12*(2*K+5)-9
    S = S_closed(K)
    assert S == sum((2*a+1 for a in exps), Q(0)) + 2*astar+1
    Dv = 1/iv.sqrt(I(2*astar+1))
    for a in exps: Dv *= I(a-astar)/I(a+astar+1)
    C = iv.sqrt(4*I(S)**2/iv.pi**2 + iv.mpf(1)/4)
    H = Dv*iv.sqrt(iv.pi/2*sum((I(e*e)/(m*m+(1+2*C)**2) for m, e in es.items()), iv.mpf(0)))
    N = (1-iv.mpf(34)/2**18)*512*iv.sqrt(iv.mpf(20)/21)*H
    n = len(exps)+1; assert n == 12*(2*K+5)-8
    Qn = Q(2*n*(n*n+2)+1, 3)
    H2 = Dv*iv.sqrt(iv.pi/2*sum((I(e*e)/(m*m+I(Qn)) for m, e in es.items()), iv.mpf(0)))
    N2 = (1-iv.mpf(34)/2**18)*512*iv.sqrt(iv.mpf(20)/21)*H2
    return N*1572864, Dv, C, N2*1572864
out = {'annular_sha256': hashlib.sha256(ann.read_bytes()).hexdigest(), 'rows': {}}
R = {}
for K in [59, 75, 349, 350, 779, 780]:
    r, Dv, C, r2 = R[K] = B(K)
    out['rows'][K] = {'B_ratio_lo': lo(r), 'B_ratio_hi': hi(r), 'Bnew_ratio_lo': lo(r2), 'Bnew_ratio_hi': hi(r2),
                      'D_lo': lo(Dv), 'D_hi': hi(Dv), 'C_lo': lo(C), 'C_hi': hi(C),
                      'exact_endpoints_man_exp': {'B_ratio': ex(r), 'Bnew_ratio': ex(r2), 'D': ex(Dv), 'C': ex(C)}}
    print(K, out['rows'][K], flush=True)
L = lambda x: frac(x._mpi_[0]); U = lambda x: frac(x._mpi_[1])
assert L(R[349][0]) > Q('1.0019782') and U(R[350][0]) < Q('0.9917770') and L(R[75][0]) > 233
assert L(R[779][3]) > Q('1.0035179') and U(R[780][3]) < Q('0.9995471') and L(R[75][3]) > 1308
D10 = lambda a: Q(a.split('e')[0]) * Q(10)**int(a.split('e')[1])
for K in R:
    row = out['rows'][K]
    for name, x in zip(['B_ratio', 'D', 'C', 'Bnew_ratio'], R[K]):
        assert D10(row[name + '_lo']) <= L(x) <= U(x) <= D10(row[name + '_hi'])   # decimals enclose the interval
out['decimal_fields'] = 'outward rounded: lo <= exact lower endpoint, hi >= exact upper endpoint'
out['P31_1_K349_lower_gt_1.0019782_K350_upper_lt_0.9917770_K75_gt_233'] = True
out['P31_2_K779_lower_gt_1.0035179_K780_upper_lt_0.9995471_K75_gt_1308'] = True
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n'); print('DONE')
