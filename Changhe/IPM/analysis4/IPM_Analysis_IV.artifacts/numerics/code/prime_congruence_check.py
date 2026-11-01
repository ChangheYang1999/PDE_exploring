"""Independent arithmetic check of the verifier's claim (topic 31): for delta = a/p, p an odd prime >= 5, a even with 4 <= a < p,
the first stream resonance is at n0 = p (j0 = a/2 - 1) and kappa = a_{p, j0-1} satisfies kappa == alpha_1 (-1)^((a-4)/2) (mod p),
where alpha_1 is the sin(theta) coefficient of f_1 (for f_1 = sin theta: alpha_1 = 1). 'mod p' for a rational r = u/v with
p not dividing v means u v^{-1} mod p. Exact fmpq recursion. usage: prime_congruence_check.py [pmax] [profile: sin1|cand007]"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpq
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60; prof = sys.argv[2] if len(sys.argv) > 2 else 'sin1'
R = RingQ()
if prof == 'sin1': f1 = [R.scalar(1)]
else: f1 = [R.scalar(x) for x in json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))['f1_sine_coefficients_exact']]
alpha1 = f1[0]
def residue(r, p):
    u, v = int(r.p), int(r.q)
    if v % p == 0: return None
    return (u * pow(v, -1, p)) % p
primes = [p for p in range(5, pmax + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
out = []; ok = 0; bad = 0; skipped = 0
for p in primes:
    for a in range(4, p, 2):
        if not (0.25 < a / p < 0.75): continue
        delta = fmpq(a, p); cl = 1 / (1 - delta); j0 = a // 2 - 1
        ff = FarField(R, cl, f1)
        for n in range(2, p + 1): ff.step()
        fp = ff.f[p]; kappa = fp[j0 - 1] if j0 - 1 < len(fp) else fmpq(0)
        res = ff.stats[p].get('resonances'); assert res and res[0]['j'] == j0, (p, a, res)
        rk = residue(kappa, p); ra = residue(alpha1, p)
        if rk is None or ra is None: skipped += 1; status = 'skipped (p divides a denominator)'
        else:
            pred = (ra * (-1) ** ((a - 4) // 2)) % p
            status = 'OK' if rk == pred else 'MISMATCH'
            if status == 'OK': ok += 1
            else: bad += 1
        out.append({'p': p, 'a': a, 'delta': a / p, 'n0': p, 'j0': j0, 'kappa_residue_mod_p': rk, 'predicted': (None if rk is None else pred), 'status': status, 'kappa_float': float(kappa), 'kappa_is_zero': kappa == 0})
        print(f'p={p:3d} a={a:3d} delta={a/p:.4f} j0={j0:2d} kappa mod p = {rk} predicted {None if rk is None else pred}  {status}  kappa={float(kappa):.3e}')
        sys.stdout.flush()
json.dump({'profile': prof, 'alpha1': str(alpha1), 'cases': out, 'ok': ok, 'mismatch': bad, 'skipped': skipped}, open(os.path.join(LANE, 'notes', f'prime_congruence_{prof}.json'), 'w'), indent=1)
print(f'profile {prof}: {ok} OK, {bad} MISMATCH, {skipped} skipped, of {len(out)} cases (primes 5..{pmax}, delta in (0.25, 0.75))')
