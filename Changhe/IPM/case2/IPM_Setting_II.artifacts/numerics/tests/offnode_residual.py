"""Between-node (off-collocation) residual of a saved zeta state (verifier V24 suggestion): rebuild the state on a grid with
twice the radial nodes (same R, L, Ntheta) by polynomial interpolation of the modal functions q_m in xi, evaluate the full
nonlinear forced residual there (velocity recomputed on the fine grid), and report |R_z - lambda f0| relative to |lambda f0| (or
to the weight w) by radial region.  This is the truncation-error estimate of the collocation solution; the at-node residual
is not.  Usage: python3 tests/offnode_residual.py runs/<state>.pt"""
import sys, math; sys.path.insert(0, 'code')
import torch, numpy as np
from ipm2polar import Disc, bary_weights
from zetasolve import initial_zeta, weight_zeta
torch.set_default_dtype(torch.float64)
dev = 'cuda'
for fn in sys.argv[1:]:
    st = torch.load(fn, map_location=dev, weights_only=False)
    a = st['args']; Nr, Nth, R, L = a['Nr'], a['Nth'], a['R'], a['L']
    pre = a.get('prefactor', 'r'); smooth = a.get('smooth', False)
    d = Disc(Nr, Nth, R, L=L, K=2, tail='power2', device=dev, smooth=smooth, prefactor=pre)
    d2 = Disc(2 * Nr, Nth, R, L=L, K=2, tail='power2', device=dev, smooth=False, prefactor=pre)
    q = st['q'].to(dev); cl = float(st['cl']); lam = float(st.get('lam', 0.0))
    v = d.pack(q, cl); qz, _ = d.unpack(v)
    # interpolate q_m (polynomials in xi) to the fine nodes
    x_new = 2.0 * d2.xi_np / d.xi_max - 1.0
    wb = bary_weights(d.x)
    P = np.zeros((len(x_new), Nr))
    for i, xe in enumerate(x_new):
        dd = xe - d.x
        if np.any(np.abs(dd) < 1e-14): P[i, np.argmin(np.abs(dd))] = 1.0
        else:
            t = wb / dd; P[i] = t / t.sum()
    P = torch.tensor(P, device=dev, dtype=torch.complex128)
    qz2 = (P @ qz.T).T                                   # [M+1, 2Nr]
    out2 = d2.zeta_residual_modes(qz2, torch.tensor(cl, device=dev), return_all=True)
    Rz2 = out2['Rz']
    f0 = None
    if lam != 0.0:
        v0 = initial_zeta(d2, a['cl0'], eps=0.0, ay=a['ay']); qz0, cl0 = d2.unpack(v0)
        f0 = d2.to_phys(d2.zeta_residual_modes(qz0, cl0))
    E = Rz2 - (lam * f0 if f0 is not None else 0.0)
    if f0 is not None and abs(lam) > 0.05:
        ref = (lam * f0).abs().max(dim=0).values; refname = "|lambda f0|"
    else:
        ref = weight_zeta(d2, 1.0 / cl); refname = "w_zeta(r) (lambda small or zero: unforced residual)"
    rel = E.abs().max(dim=0).values / torch.clamp(ref, min=1e-300)
    r2 = d2.r
    # at the ORIGINAL nodes vs the NEW (midpoint-like) nodes: fine nodes nearest to the original nodes are not identical; report both sets by region
    print("state %s: c_l=%.4f lambda=%.4f prefactor=%s | off-node residual |E| relative to %s by region:" % (fn, cl, lam, pre, refname))
    for lo, hi in ((0, 1), (1, 3), (3, 10), (10, 30), (30, 100), (100, 300), (300, 1e9)):
        msk = (r2 >= lo) & (r2 < hi)
        if msk.any():
            print("   r in [%g,%g): max %.2e  median %.2e" % (lo, min(hi, R), float(rel[msk].max()), float(rel[msk].median())))
