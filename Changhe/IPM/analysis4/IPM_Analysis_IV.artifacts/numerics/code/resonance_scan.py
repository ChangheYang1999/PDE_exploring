"""Lead request (Theorem C hypothesis H): exact compatibility coefficient kappa = a_{n0, j0-1} at the FIRST stream resonance
for rationals delta = A/B in (lo, hi) with first resonance order n0 <= NMAX, f_1 = sin(theta) (unit) or the 007 profile.
First resonance: n0 = B m with m minimal such that m A is even and m A >= 4; j0 = n0 delta / 2 - 1.
Output: notes/resonance_scan_<f1>.json and a printed table. Exact rational arithmetic (fmpq)."""
import sys, os, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpq
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def first_resonance(A, B):
    for m in range(1, 5):
        if (m * A) % 2 == 0 and m * A >= 4: return B * m, (m * A) // 2 - 1
    return None, None
def main():
    f1spec = sys.argv[1] if len(sys.argv) > 1 else 'sin1'; NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    lo, hi = 0.40, 0.50
    R = RingQ()
    if f1spec == 'sin1': f1 = [R.scalar(1)]
    else: f1 = [R.scalar(x) for x in json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))['f1_sine_coefficients_exact']]
    rats = set()
    for B in range(2, NMAX + 1):
        for A in range(1, B):
            if math.gcd(A, B) != 1 or not (lo < A / B < hi): continue
            n0, j0 = first_resonance(A, B)
            if n0 is None or n0 > NMAX: continue
            rats.add((A, B, n0, j0))
    rats = sorted(rats, key=lambda t: (t[2], t[0] / t[1]))
    out = []; t0 = time.time()
    print(f'f_1 = {f1spec}: {len(rats)} rationals delta = A/B in ({lo}, {hi}) with first resonance n0 <= {NMAX}')
    print(f"{'delta':>8} {'A/B':>7} {'c_l':>9} {'n0':>4} {'j0':>3} {'kappa = a_(n0,j0-1)':>22} {'alpha_n0':>10} {'kappa/alpha':>11}  exact kappa (truncated)")
    for A, B, n0, j0 in rats:
        delta = fmpq(A, B); cl = 1 / (1 - delta)
        ff = FarField(R, cl, f1)
        try:
            for n in range(2, n0 + 1): ff.step()
        except Exception as e:
            print('ERR', A, B, e); continue
        a = ff.f[n0]; kappa = a[j0 - 1] if j0 - 1 < len(a) else fmpq(0)
        alpha = sum(abs(float(x)) for x in a)
        rec = {'delta': f'{A}/{B}', 'delta_float': A / B, 'c_l': str(cl), 'n0': n0, 'j0': j0, 'kappa_exact': str(kappa), 'kappa_float': float(kappa), 'alpha_n0': alpha,
               'kappa_is_zero': kappa == 0, 'f1': f1spec, 'poisson_record': ff.stats[n0].get('resonances')}
        out.append(rec)
        ks = str(kappa); print(f"{A/B:8.5f} {A:>3d}/{B:<3d} {float(cl):9.6f} {n0:4d} {j0:3d} {float(kappa):22.6e} {alpha:10.3e} {float(kappa)/alpha:11.3e}  {ks[:50]}{'...' if len(ks)>50 else ''}{'   <<< KAPPA = 0' if kappa == 0 else ''}")
        sys.stdout.flush()
    json.dump(out, open(os.path.join(LANE, 'notes', f'resonance_scan_{f1spec}.json'), 'w'), indent=1)
    zeros = [r for r in out if r['kappa_is_zero']]
    print(f'done in {time.time()-t0:.0f}s; rationals with kappa = 0: {len(zeros)}', [z['delta'] for z in zeros])
if __name__ == '__main__': main()
