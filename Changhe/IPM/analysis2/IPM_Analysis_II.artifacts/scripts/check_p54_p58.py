"""Third computation for verification topics 54 (d2) and 58 (Mpen2): global W3 derivative tests at rational points.

Written from the statements of topics 54 and 58 only; no verifier code is imported. The canonical coefficients are read
from the audited source records through check_jet_distance.source (with their hashes). At each point the seventh order
Cartesian Taylor jet of the potential chi is formed in interval arithmetic (check_jet_distance.chi_jet; a finite jet, so
no remainder enters) and the partial derivatives are chi_(a,b) = (jet coefficient) a! b!. With rho = -chi_xxy - chi_yyy
and U = (-chi_xyy, chi_xxy):
    D^3 U:   u_(1,i) = -chi_(i+1,5-i), u_(2,i) = chi_(i+2,4-i), i = 0..3,
    D^3 rho: d_(3,i) = -chi_(i+2,4-i) - chi_(i,6-i), i = 0..3,
    D^4 rho: d_(4,i) = -chi_(i+2,5-i) - chi_(i,7-i), i = 0..4,
and the squared weighted Frobenius norms are S_U = (1+r^2) sum binom(3,i)(u_(1,i)^2 + u_(2,i)^2),
S_3 = (1+r^2)^2 sum binom(3,i) d_(3,i)^2, S_4 = (1+r^2)^2 sum binom(4,i) d_(4,i)^2. The exact lower endpoint of each S
(sum of squared exact lower bounds of |d|) is compared with the square of the stated bound and with the contract value.

Usage: python3 check_p54_p58.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sys.argv = [sys.argv[0], str(ROOT)]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_jet_distance as cj
from mpmath import iv
iv.prec = 400
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I, lo, hi, mig = cj.I, cj.lo, cj.hi, cj.mig
t_start = time.monotonic()

# (reference, point, quantity, stated strict lower bound, contract bound)
CLAIMS = [('nb_d2_exact', ('7/16', '7/64'), 'S_4', Q(592), 512), ('nb_d2_exact', ('27/64', '7/64'), 'S_4', Q(578), 512),
          ('nb_d2_exact', ('7/16', '3/32'), 'S_4', Q(513), 512),
          ('nb_Mpen2_exact', ('19/64', '7/16'), 'S_U', Q(1612, 100), 16),
          ('nb_Mpen2_exact', ('19/64', '7/16'), 'S_3', Q(3923, 100), 32),
          ('nb_Mpen2_exact', ('21/64', '29/64'), 'S_3', Q(3930, 100), 32),
          ('nb_Mpen2_exact', ('1/4', '15/32'), 'S_4', Q(133312, 100), 512),
          ('nb_Mpen2_exact', ('17/64', '29/64'), 'S_4', Q(125040, 100), 512)]
out = {'inputs': {}, 'claims': []}
cache = {}
for name, (xs, ys), qty, bound, contract in CLAIMS:
    if name not in cache:
        pth, shs, c, a0, terms = cj.source(name); cache[name] = (c, terms)
        out['inputs'][str(pth.relative_to(ROOT))] = shs
    c, terms = cache[name]
    key = (name, xs, ys)
    if key not in cache:
        X, Y = I(Q(xs)), I(Q(ys)); J = cj.Jets(7)
        jet = cj.chi_jet(J, terms, c, X, Y)
        cache[key] = {(a, b): jet[J.pos[a, b]] * factorial(a) * factorial(b) for (a, b) in J.idx}
    ch = cache[key]
    r2 = Q(xs) ** 2 + Q(ys) ** 2
    if qty == 'S_U':
        comps = [(comb(3, i), [-ch[i + 1, 5 - i], ch[i + 2, 4 - i]]) for i in range(4)]; wt = 1 + r2
    elif qty == 'S_3':
        comps = [(comb(3, i), [-ch[i + 2, 4 - i] - ch[i, 6 - i]]) for i in range(4)]; wt = (1 + r2) ** 2
    else:
        comps = [(comb(4, i), [-ch[i + 2, 5 - i] - ch[i, 7 - i]]) for i in range(5)]; wt = (1 + r2) ** 2
    Slo = wt * sum((m * mig(d) ** 2 for m, ds in comps for d in ds), Q(0))
    Shi = wt * sum((m * max(abs(lo(d)), abs(hi(d))) ** 2 for m, ds in comps for d in ds), Q(0))
    rec = {'reference': name, 'point': [xs, ys], 'quantity': qty, 'value_lower': float(iv.sqrt(I(Slo)).a),
           'value_upper': float(iv.sqrt(I(Shi)).b), 'stated_lower': str(bound), 'contract': contract,
           'exceeds_stated': Slo > bound ** 2, 'exceeds_contract': Slo > contract ** 2,
           'seconds': round(time.monotonic() - t_start, 1)}
    out['claims'].append(rec); print(rec, flush=True)
assert all(r['exceeds_stated'] and r['exceeds_contract'] for r in out['claims'])
out['all_pass'] = True
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
