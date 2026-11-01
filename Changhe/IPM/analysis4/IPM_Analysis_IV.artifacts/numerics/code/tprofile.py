"""Lead request: evaluate the t-polynomials of the canonical log series at given t = log r in ball arithmetic:
F_n(t) = sum_k t^k f_{n,k}(theta) -> l1 norm over frequencies, with rigorous enclosure (cancellation visible in the radius),
same for the stream G_n(t). usage: tprofile.py CKPT n1,n2,... t1,t2,..."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logff import *
L = LogFarField.load(sys.argv[1]); R = L.R
ns = [int(x) for x in sys.argv[2].split(',')]; ts = [float(x) for x in sys.argv[3].split(',')]
def l1_at_t(cols, t):
    """cols: list over k of coefficient lists; returns (log10 l1 of midpoint vector, log10 of the l1 of radii, log10 l1 of the t^0 column)"""
    K = max(len(c) for c in cols); tv = arb(t); acc = [arb(0)] * K
    tp = arb(1)
    for k, c in enumerate(cols):
        for i, x in enumerate(c): acc[i] = acc[i] + x * tp
        tp = tp * tv
    s_mid = sum(abs(x.mid()) for x in acc); s_rad = sum(x.rad() for x in acc)
    lg = lambda v: float((v.log() / arb(10).log()).str(12, radius=False)) if v != 0 else -float('inf')
    return lg(s_mid), lg(arb(s_rad)) if s_rad != 0 else -float('inf')
print(f"{'n':>4} {'t':>6} {'log10 ||F_n(t)||':>16} {'log10 rad':>10} {'log10 c_0':>10} {'cancel(decades)':>15} {'log10 ||G_n(t)||':>16} {'log10 rad g':>11}")
for n in ns:
    if n not in L.f: print(n, 'not in checkpoint (max', max(L.f), ')'); continue
    c0 = L.stats[n]['log10_col_l1'][0]
    for t in ts:
        lf, rf = l1_at_t(L.f[n], t); lgg, rg = l1_at_t(L.g[n], t)
        # cancellation: log10 of sum_k |t|^k ||f_{n,k}|| minus log10 ||F_n(t)||
        cols = L.stats[n]['log10_col_l1']; big = max(c + k * math.log10(abs(t)) for k, c in enumerate(cols) if c > -1e9)
        tot = math.log10(sum(10 ** (c + k * math.log10(abs(t)) - big) for k, c in enumerate(cols) if c > -1e9)) + big
        print(f"{n:4d} {t:6.1f} {lf:16.4f} {rf:10.2f} {c0:10.4f} {tot - lf:15.2f} {lgg:16.4f} {rg:11.2f}")
