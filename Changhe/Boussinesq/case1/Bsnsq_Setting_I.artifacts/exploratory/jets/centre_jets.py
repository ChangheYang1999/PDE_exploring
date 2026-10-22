"""Diagnostic: centre Taylor jets of LM (Omega-basis) states and the hydrostatic-regime test.
From the modal radial profiles at small r: f_0 = a0 r + (b1 + 3 b2)/4 r^3, f_1 = (b1 - b2)/4 r^3 (Theta modes sin phi,
sin 3phi), g_1 = (g/2) r^2 (Omega mode sin 2phi), psi_1 = -r^2 + (d1 + d2)/4 r^4, psi_2 = (d1 - d2)/8 r^4 (Psi modes
sin 2phi, sin 4phi). Polynomial fits in r^2 on r/L in [r1, r2]. Prints the jet relations
(2b+4) b1 + 3 a0 d1 = 0, 2 b b2 + a0 d2 = 0, (2beta+1) g = 2 b1, g = -6 (d1 + d2) as relative defects, and the
horizontal-curvature fraction -6 d1 / g (equals C_beta/a0 for exact jets; hydrostatic regime needs it << 1)."""
import sys, torch, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'scripts_polar_char'))
from polarlib import *; from evalfields import load_coefs, radial_profiles
args = [a for a in sys.argv[1:] if not a.startswith('--')]
r1, r2 = 2e-3, 4e-2
for a in sys.argv[1:]:
    if a.startswith('--r1='): r1 = float(a[5:])
    if a.startswith('--r2='): r2 = float(a[5:])
def fit(r, y, p0, deg=3):
    # y = sum_k c_k r^(p0 + 2k), k = 0..deg-1 ; returns c
    A = np.stack([r ** (p0 + 2 * k) for k in range(deg)], 1)
    return np.linalg.lstsq(A, y, rcond=None)[0]
for f in args:
    P, cT, cO, NT, NO, K = load_coefs(f); cT = cT.cpu(); cO = cO.cpu()
    beta = float(P.beta); b = beta - 2; Cb = 2 * (beta + 2) * (2 * beta + 1)
    r = torch.logspace(np.log10(r1), np.log10(r2), 60, dtype=DT) * P.L
    pr = radial_profiles(P, cT, cO, r, NT, NO, K)
    rn = (r / P.L).numpy(); L = float(P.L)
    f0 = pr['f'][0].numpy(); f1 = pr['f'][1].numpy(); g1 = pr['g'][0].numpy(); p1 = pr['psi'][0].numpy(); p2 = pr['psi'][1].numpy()
    # work in units of L: x = L xn ; coefficients converted back to physical units
    c0 = fit(rn, f0 / L, 1); c1 = fit(rn, f1 / L, 3); cg = fit(rn, g1, 2); cp1 = fit(rn, p1 / L ** 2, 2); cp2 = fit(rn, p2 / L ** 2, 4)
    a0 = c0[0]; S = 4 * c0[1] / L ** 2; Dd = 4 * c1[0] / L ** 2         # S = b1 + 3 b2, Dd = b1 - b2
    b2 = (S - Dd) / 4; b1 = Dd + b2
    g = 2 * cg[0] / L ** 2; c = cp1[0]
    sp = 4 * cp1[1] / L ** 2; dm = 8 * cp2[0] / L ** 2                 # sp = d1 + d2, dm = d1 - d2
    d1 = (sp + dm) / 2; d2 = (sp - dm) / 2
    rel = lambda u, v: abs(u + v) / max(abs(u), abs(v))
    print(f"{f.split('/')[-1]:34s} beta {beta:.4f} a0 {a0:.4f} c {c:.6f}  b1 {b1:.4e} b2 {b2:.4e} g {g:.4e} d1 {d1:.4e} d2 {d2:.4e} (units L=1: x L^-2)")
    print(f"   relations (rel. defect): (2b+4)b1+3a0d1 {rel((2*beta+4)*b1, 3*a0*d1):.3e}  2b b2+a0 d2 {rel(2*b*b2, a0*d2):.3e}  "
          f"(2beta+1)g-2b1 {rel((2*beta+1)*g, -2*b1):.3e}  g+6(d1+d2) {rel(g, 6*(d1+d2)):.3e}")
    print(f"   horizontal fraction -6 d1/g = {-6*d1/g:.4f}   C_beta/a0 = {Cb/a0:.4f}   vertical -6 d2/g = {-6*d2/g:.4f}   "
          f"b2 predicted g(a0-C)/(12b) = {g*(a0-Cb)/(12*b):.4e}", flush=True)
