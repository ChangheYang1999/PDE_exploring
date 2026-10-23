"""radial_projections.py -- angular Fourier projections of the residual, R(r, th) = sum_{k odd} R_k(r) sin(k th) (R is odd in y, even in x), k = 1, 3, 5, 7
(lead 01:50Z item 2 / 01:24Z item 4): profiles R_k(r)/Nbar(r) with Nbar(r) = max_th N_f(r, th), at log-spaced radii, and sup over r.  Quadrature: 256
angles in (0, pi) (midpoint rule, exact for the trigonometric degree of the representation).  usage: python3 src/radial_projections.py states... [rmin rmax]"""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
files = [a for a in sys.argv[1:] if not a.replace('.', '').replace('e', '').replace('-', '').isdigit()]
nums = [float(a) for a in sys.argv[1:] if a not in files]; rmin = nums[0] if nums else 1e-3; rmax = nums[1] if len(nums) > 1 else 1e3
rr = np.exp(np.linspace(np.log(rmin), np.log(rmax), 61)); Mth = 256; th = (np.arange(Mth) + 0.5) * math.pi / Mth
for f in files:
    S = qdiag.State(f); RR, TT = np.meshgrid(rr, th, indexing='ij'); o = S.ev(RR, TT)
    Nbar = o['Nf'].max(axis=1); prof = {}
    for k in [1, 3, 5, 7]:
        Rk = (2 / Mth) * (o['R'] * np.sin(k * TT)).sum(axis=1); prof[k] = Rk / Nbar
    print(f"{f.split('/')[-1]} (N={S.N}, a0={S.a0:.5f}): sup_r |R_k|/Nbar over [{rmin:g}, {rmax:g}]: " + "  ".join(f"k={k}: {np.max(np.abs(prof[k])):.2e} at r={rr[np.argmax(np.abs(prof[k]))]:.3g}" for k in [1, 3, 5, 7]))
    idx = [0, 10, 20, 25, 30, 35, 40, 50, 60]
    print("    r:        " + " ".join(f"{rr[i]:9.2e}" for i in idx))
    for k in [1, 3, 5, 7]: print(f"    R_{k}/Nbar: " + " ".join(f"{prof[k][i]:+9.1e}" for i in idx))
