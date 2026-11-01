"""One-paragraph summary of a tuned ball run (tuned_c3 / tuned_cQ / tuned_general logs): root tests at selected orders, fitted growth
constant A (least squares of log10 ||f_n||_l1 on n >= n_fit), |H_n|^(1/n) at the last tuned harmonic, sigma_k first three / minimum / last,
obstruction radii (absolute) against the coefficient scale, norm-relative radius at the end, and the apparent exterior radius A^(1/delta).
usage: tuned_summary.py TAG [orders=50,100,...] [n_fit=150]"""
import json, sys, os, math
from fractions import Fraction
import numpy as np
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag = sys.argv[1]
rows = [json.loads(l) for l in open(os.path.join(LANE, 'logs', tag + '.jsonl')) if l.strip()]
hdr = rows[0]; st = {r['n']: r for r in rows if 'n' in r and 'log10_l1' in r}
H = json.load(open(os.path.join(LANE, 'ckpt', tag + '_H.json')))
N = max(st); delta = Fraction(hdr['delta']); inv = 1 / delta
orders = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [k for k in (36, 50, 72, 100, 108, 144, 150, 180, 200, 216, 250, 252, 288, 300) if k <= N]
n_fit = int(sys.argv[3]) if len(sys.argv) > 3 else 150
rt = [(k, 10 ** (st[k]['log10_l1'] / k)) for k in orders if k in st]
ns = sorted(n for n in st if n >= n_fit)
# three-parameter fit used in all posted values: log10 ||f_n||_l1 = n log10 A + beta log10 n + C on n >= n_fit (geometric with a power correction)
X = np.vstack([np.array(ns, float), np.log10(np.array(ns, float)), np.ones(len(ns))]).T
(la, beta, C), *_ = np.linalg.lstsq(X, np.array([st[n]['log10_l1'] for n in ns]), rcond=None) if len(ns) > 20 else ((float('nan'),) * 3,)
A = 10 ** la
A_line = 10 ** np.polyfit(np.array(ns, float), np.array([st[n]['log10_l1'] for n in ns]), 1)[0] if len(ns) > 20 else float('nan')
Hs = {int(k): v for k, v in H['H'].items()}; sig = {int(k): v for k, v in H['sigma'].items()}; obs = {int(k): v for k, v in H['obstruction'].items()}
def _f(s): return float(s.strip('[').split(' +/-')[0])
nH = max(Hs); hroot = abs(Hs[nH]['mid']) ** (1.0 / nH) if Hs[nH]['mid'] else float('nan')
sk = sorted(sig); sv = {k: _f(sig[k]) for k in sk}; kmin = min(sk, key=lambda k: abs(sv[k]))
ob_rad = [obs[k]['log10_num_rad'] for k in sorted(obs) if obs[k]['log10_num_rad'] > -1e300]
last = st[N]; scale = last['log10_maxabs']; relrad = last.get('log10_rad_over_max')
b = hdr['b_enclosure'].split(' +/-')[0].strip('[')
print(f"delta = {hdr['delta']} (c = {hdr['c_l']}, period {H.get('period', hdr.get('Q'))}), root b = {b[:36]}... ({tag}, N = {N}): root tests "
      + ', '.join(f'{v:.4f} ({k})' for k, v in rt) + f"; fit A = {A:.4f} (n >= {n_fit}; power exponent {beta:+.1f}; straight-line slope {A_line:.4f}); |H_n|^(1/n) = {hroot:.4f} at {nH}; sigma: "
      + ', '.join(f'{sv[k]:+.4e} (n = {k})' for k in sk[:3]) + f", minimum |sigma| = {abs(sv[kmin]):.4e} at n = {kmin}, last {sv[sk[-1]]:+.4e} (n = {sk[-1]}); "
      + f"obstruction radii (absolute) 10^{min(ob_rad):.0f} .. 10^{max(ob_rad):.0f} against coefficient scale 10^{scale:.0f}; norm-relative radius 10^{relrad:.0f} at {N}; "
      + f"z = r^(-{hdr['delta']}), apparent radius r > A^({inv.numerator}/{inv.denominator}) = {A ** float(inv):.3g}.")
