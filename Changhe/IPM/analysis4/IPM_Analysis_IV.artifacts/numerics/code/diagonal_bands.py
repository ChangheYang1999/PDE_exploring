# 09:15Z: density offset corrected from 3 to 4 (modes m = 2k+1 give s = 2k+4 - n delta); the stream offset 2 was correct (verifier V225).
"""Lead request (05:38Z): decomposition of each log column by distance to the resonant diagonal.
Density column q of f_n: odd modes m = 2k+1, s = m + 3 - n delta; stream column q of g_n: even modes m = 2j, s = m + 2 - n delta.
Bands: |s| <= q/4, q/4 < |s| <= q, |s| > q for q >= 1; for q = 0: |s| <= 2 and |s| > 2. Fractions of the column's l1 mass.
usage: diagonal_bands.py CKPT n1,n2,... [qlist|'all'] -> prints fractions; also the interior-maximum column k*."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logff import *
def _fl(x):
    try: return float(x)
    except TypeError: return int(x.p) / int(x.q)
L = LogFarField.load(sys.argv[1]); R = L.R
ns = [int(x) for x in sys.argv[2].split(',')]; qsel = sys.argv[3] if len(sys.argv) > 3 else '0,1,10,20,30,40,45,50,60,70,80'
def bands(col, q, nd, offset, step):
    """col: coefficient list over index i with mode m = step*i + offset; returns (f_near, f_mid, f_far, total_log10)"""
    l2a = [R.log2abs(x) for x in col]
    if not col or max(l2a) == -float('inf'): return None
    im = int(np.argmax(l2a)); mx = col[im]; w = np.array([abs(R.to_float(x / mx)) for x in col]); tot = w.sum()
    m = step * np.arange(len(col)) + offset; s = np.abs(m - nd)
    if q == 0: near = w[s <= 2].sum(); mid = 0.0; far = w[s > 2].sum()
    else: near = w[s <= q / 4].sum(); mid = w[(s > q / 4) & (s <= q)].sum(); far = w[s > q].sum()
    return near / tot, mid / tot, far / tot, math.log10(tot) + R.log10abs(mx)
for n in ns:
    if n not in L.f: print(n, 'not in checkpoint (max', max(L.f), ')'); continue
    nd = n * _fl(L.delta_exact); F = L.f[n]; G = L.g[n]; cols = L.stats[n]['log10_col_l1']
    kc = [c + math.log10(math.factorial(k)) - cols[0] for k, c in enumerate(cols)]; kstar = max(range(1, len(kc)), key=lambda k: kc[k])
    qs = sorted(set([int(x) for x in qsel.split(',') if int(x) < len(F)] + [kstar])) if qsel != 'all' else range(len(F))
    print(f"n = {n}: n delta = {nd:.3f}, density resonant mode m = {nd-3:.1f}, stream resonant mode m = {nd-2:.1f}, log degree {len(F)-1}, k* = {kstar}")
    print(f"  {'q':>3} | density: near(|s|<=q/4)  mid  far  | stream: near  mid  far   (q = 0: |s| <= 2 vs > 2)")
    for q in qs:
        bf = bands(F[q], q, nd, 4, 2); bg = bands(G[q], q, nd, 2, 2) if q < len(G) else None
        sf = f"{bf[0]:.3f} {bf[1]:.3f} {bf[2]:.3f}" if bf else '  -  '; sg = f"{bg[0]:.3f} {bg[1]:.3f} {bg[2]:.3f}" if bg else '  -  '
        print(f"  {q:3d} | {sf:>22} | {sg:>20}" + ("   <-- k*" if q == kstar else ''))
