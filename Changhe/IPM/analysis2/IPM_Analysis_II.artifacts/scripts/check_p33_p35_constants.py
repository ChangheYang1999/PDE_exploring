"""Third computation of the family bounds with the recursive dilation constant (verification topics 33 and 35).

mpmath interval arithmetic (independent of python-flint). For n powers the cylinder constant is Q_n = 4 c_n^2 + 4/3,
c_n = n - 1/2 + log(2n - 1)/8, and the Route U lower bound is
    B = (1 - 34*2^-18) 512 sqrt(20/21) D sqrt((pi/2) sum_m e_m^2/(m^2 + Q_n)),
with D = (2a*+1)^(-1/2) prod_(a != a*) |a - a*|/(a + a* + 1) over the remaining exponents.

Six branches (topic 33): exponents l delta/2 + k - 2, 1 <= l <= 12, 0 <= k <= 2K+4, those >= a* = 7 delta/2 - 2
(the eight smaller ones are removed); e_m from the shipped leading sine coefficients of the fixed sector.
Seven branches (topic 35): 1 <= l <= 14, (l,0) for l <= 7 and (1,1), (2,1) removed, (3,1) removed if eps = 1;
a* = 4 delta - 2; e_m = the exact (7,0) sine coefficients of the seventh stationary order.

Every interval endpoint is stored exactly as [signed mantissa, binary exponent]; comparisons with the decimal
thresholds are exact rational comparisons.

Usage: python3 check_p33_p35_constants.py ANNULAR_JSON RECUR_SINE_JSON [OUTPUT_JSON]
"""
import json, sys, hashlib
from fractions import Fraction as Q
from pathlib import Path
from mpmath import iv, mp
sys.set_int_max_str_digits(0)
iv.prec = 400; mp.prec = 400
ann, rec = Path(sys.argv[1]), Path(sys.argv[2])
OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(__file__).with_suffix('.json')
c = Q(4076476460239181, 2251799813685248); g = 1/c; d = 1-g
I = lambda q: iv.mpf(q.numerator)/q.denominator
def frac(t):
    """exact value of a raw mpf tuple (sign, mantissa, exponent, bitcount); man_exp alone drops the sign."""
    sign, man, e, bc = t
    if not man:
        assert not e, 'infinite or undefined endpoint'
        return Q(0)
    v = Q(int(man)) * Q(2)**int(e)
    return -v if sign else v
L = lambda x: frac(x._mpi_[0]); U = lambda x: frac(x._mpi_[1])
ex = lambda x: [[(-1 if t[0] else 1) * int(t[1]), int(t[2])] for t in x._mpi_]   # signed mantissa, exponent
e6 = {int(m): Q(v) for m, v in json.loads(ann.read_text())['leading_sine_coefficients'].items()}
e7 = {int(m): Q(v) for m, v in json.loads(rec.read_text())['order8_fixed_defect']['sine_coefficients'].items()}

def bound(exps, astar, es):
    n = len(exps)
    Dv = 1/iv.sqrt(I(2*astar+1))
    for a in exps:
        if a != astar: Dv *= I(abs(a-astar))/I(a+astar+1)
    cn = n - iv.mpf(1)/2 + iv.log(iv.mpf(2*n-1))/8
    Qn = 4*cn**2 + iv.mpf(4)/3
    H = Dv*iv.sqrt(iv.pi/2*sum((I(e*e)/(m*m+Qn) for m, e in es.items()), iv.mpf(0)))
    N = (1-iv.mpf(34)/2**18)*512*iv.sqrt(iv.mpf(20)/21)*H
    return n, Dv, N*1572864

def six(K):
    astar = 7*d/2-2
    exps = [l*d/2+k-2 for l in range(1, 13) for k in range(2*K+5) if l*d/2+k-2 >= astar]
    assert len(exps) == 12*(2*K+5)-8 and astar in exps
    return bound(exps, astar, e6)

def seven(K, eps):
    astar = 4*d-2
    removed = {(l, 0) for l in range(1, 8)} | {(1, 1), (2, 1)} | ({(3, 1)} if eps else set())
    exps = [l*d/2+k-2 for l in range(1, 15) for k in range(2*K+5) if (l, k) not in removed]
    assert len(set(exps)) == len(exps) == 14*(2*K+5)-9-eps and astar in exps and min(exps) > Q(-1, 2)
    return bound(exps, astar, e7)

out = {'annular_sha256': hashlib.sha256(ann.read_bytes()).hexdigest(),
       'recur_sine_sha256': hashlib.sha256(rec.read_bytes()).hexdigest(),
       'e7_full_circle_norm_squared_over_pi': str(sum(v*v for v in e7.values())), 'rows': []}
res = {}
for label, f, args in [('six', six, (75,)), ('six', six, (3675,)), ('six', six, (3676,)),
                       ('seven', seven, (69, 0)), ('seven', seven, (69, 1)), ('seven', seven, (92, 0)), ('seven', seven, (92, 1))]:
    n, Dv, r = res[(label,) + args] = f(*args)
    row = {'family': label, 'args': list(args), 'n': n, 'D_approx': mp.nstr(Dv.mid, 12), 'ratio_approx': mp.nstr(r.mid, 15),
           'ratio_exact_endpoints_man_exp': ex(r)}
    out['rows'].append(row); print(row['family'], row['args'], n, row['D_approx'], row['ratio_approx'], flush=True)
assert L(res['six', 75][2]) > 22986 and L(res['six', 3675][2]) > Q('1.0004726') and U(res['six', 3676][2]) < Q('0.9997658')
assert U(res['seven', 69, 0][2]) < Q('7e-13') and U(res['seven', 69, 1][2]) < Q('3e-12') and L(res['seven', 69, 0][2]) > 0
out['topic33_K75_gt_22986_K3675_gt_1.0004726_K3676_lt_0.9997658'] = True
out['topic35_K69_eps0_lt_7e-13_eps1_lt_3e-12'] = True
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2)+'\n'); print('DONE')
