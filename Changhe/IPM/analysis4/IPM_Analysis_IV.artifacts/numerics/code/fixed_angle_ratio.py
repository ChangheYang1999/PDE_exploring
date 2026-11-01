"""Scalar power series at fixed angles: c_n(theta0) = f_n(theta0); ratio c_{n+1}/c_n and Domb-Sykes fit
c_{n+1}/c_n = (1/z0)(1 - (1+beta)/n) over the last half of the orders. Signed ratio -> location of the dominant singularity
(negative ratio = singularity on the negative z axis). usage: fixed_angle_ratio.py CKPT [theta0,...]"""
import sys, os, math, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
ff = FarField.load(sys.argv[1]); R = ff.R; N = max(ff.f)
ths = [float(x) for x in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['0.4', '0.8', '1.2', '1.5'])]
print(f"{sys.argv[1]}: N={N}")
for th in ths:
    # evaluate f_n(theta0) in scaled arithmetic: use arb for the sum (rigorous mid), then float of log-magnitude and sign
    vals = []
    for n in range(1, N + 1):
        a = ff.f[n]
        if R.name == 'arb':
            s = arb(0)
            for k, x in enumerate(a): s += x * arb((2 * k + 1) * th).sin()
            m = s.mid(); sign = 1 if m > 0 else (-1 if m < 0 else 0)
            lg = float((abs(m).log() / arb(10).log()).str(15, radius=False)) if sign != 0 else -float('inf')
        else:
            v = sum(float(x) * math.sin((2 * k + 1) * th) for k, x in enumerate(a)); sign = np.sign(v); lg = math.log10(abs(v)) if v != 0 else -float('inf')
        vals.append((sign, lg))
    ratios = []
    for n in range(1, N):
        s1, l1 = vals[n - 1]; s2, l2 = vals[n]
        ratios.append(s1 * s2 * 10 ** (l2 - l1) if s1 and s2 else float('nan'))
    ratios = np.array(ratios); ns = np.arange(1, N)
    half = ns >= N // 2; rr = ratios[half]; nn = ns[half]
    ok = np.isfinite(rr)
    A = np.vstack([np.ones(ok.sum()), 1 / nn[ok]]).T; (c0, c1), *_ = np.linalg.lstsq(A, rr[ok], rcond=None)
    rms = np.sqrt(np.mean((rr[ok] - (c0 + c1 / nn[ok])) ** 2))
    signs = ''.join('+' if s > 0 else ('-' if s < 0 else '0') for s, _ in vals[-40:])
    print(f"  theta0={th:.2f}: ratio fit c_(n+1)/c_n = {c0:+.5f} (1 - {(-c1/c0):.3f}/n), rms {rms:.1e}; |1/z0| = {abs(c0):.5f}; last ratios {np.round(ratios[-6:],4).tolist()}; signs(last 40) {signs}")
