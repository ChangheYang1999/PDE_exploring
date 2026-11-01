"""Exact resonance / compatibility report from fmpq checkpoints.
For each rational c_l run: lists the chi-level special orders (n delta = 2: value f_n(pi/2) = sum (-1)^k a_{n,k});
the psi-level resonant orders n delta = 2(j+1): exact a_{n,j-1} (compatibility coefficient; must vanish) and the
exact forcing coefficient of sin(2j theta) in p cos f - sin f' which is -2j a_{n,j-1}. Only the FIRST psi resonance
is a statement about the pure ansatz; later orders in the checkpoint are the b_{n,j} = 0 continuation."""
import sys, os, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpq
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = []
for ck in sorted(glob.glob(os.path.join(LANE, 'ckpt', 'res_*.pkl')) + glob.glob(os.path.join(LANE, 'ckpt', 'sin1_cl2_exact.pkl'))):
    ff = FarField.load(ck)
    if ff.R.name != 'fmpq': continue
    cl = ff.c_l; delta = ff.delta; N = max(ff.f)
    rec = {'checkpoint': os.path.relpath(ck, LANE), 'c_l': str(cl), 'delta': str(delta), 'N': N, 'f1': [str(x) for x in ff.f[1]], 'chi_special': [], 'psi_resonances': []}
    first = None
    for n in range(1, N + 1):
        nd = n * delta
        if nd == 2:
            a = ff.f[n]; val = sum(((-1) ** k) * a[k] for k in range(len(a)))
            rec['chi_special'].append({'n': n, 'f_n(pi/2)': str(val), 'float': float(val), 'alpha_n': float(sum(abs(float(x)) for x in a))})
        if nd.q == 1 and int(nd.p) % 2 == 0 and int(nd.p) >= 4:
            j = int(nd.p) // 2 - 1; a = ff.f[n]
            comp = a[j - 1] if j - 1 < len(a) else fmpq(0)
            rec['psi_resonances'].append({'n': n, 'j': j, 'a_{n,j-1}': str(comp), 'float': float(comp), 'forcing_sin2j': str(-2 * j * comp),
                                          'alpha_n': float(sum(abs(float(x)) for x in a)), 'first_resonance': first is None,
                                          'note': 'pure ansatz obstructed' if (first is None and comp != 0) else ('compatible (free multipole)' if comp == 0 else 'after first failure: b=0 continuation only')})
            if first is None: first = n
    out.append(rec)
    print(f"{rec['checkpoint']}: c_l={rec['c_l']} delta={rec['delta']} f1={rec['f1']} N={N}")
    for c in rec['chi_special']: print(f"   chi-level n={c['n']} (n delta = 2): f_n(pi/2) = {c['f_n(pi/2)']} = {c['float']:.6e}  (alpha_n={c['alpha_n']:.3e}) -> r^2 log r term in chi needed: {c['float'] != 0}")
    for r in rec['psi_resonances']: print(f"   psi-level n={r['n']} j={r['j']}: a_(n,j-1) = {r['float']:.6e} exact {r['a_{n,j-1}'][:60]}{'...' if len(r['a_{n,j-1}'])>60 else ''}  [{r['note']}]")
json.dump(out, open(os.path.join(LANE, 'notes', 'resonance_report.json'), 'w'), indent=1)
