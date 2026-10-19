"""Referee protocol (Q3, item 1): at a fixed moderate lambda, converge the corrector under several exterior closures and
compare the residual floor, c_l and the compatibility defect.  Starts from the saved lambda = 0.6 stage of the fixed
homotopy (48, 32, 300); the forcing f0 is recomputed with each closure from the same physical seed."""
import sys, math; sys.path.insert(0, 'code')
import torch, numpy as np
from ipm2polar import Disc
from zetasolve import weight_zeta, initial_zeta, lm_solve
torch.set_default_dtype(torch.float64)
dev = 'cuda'
lam = 0.6
st = torch.load('runs/homot_fix_48_32_300_lam0.600.pt', map_location=dev, weights_only=False)
for tail, exps in (('power2', None), ('power', None), ('zero', None), ('power2', (0.5, -0.5))):
    d = Disc(48, 32, 300.0, K=2, tail=tail, tail_exps=exps, device=dev, smooth=True)
    v0 = initial_zeta(d, 2.0, eps=0.0, ay=1.5); wz = weight_zeta(d, 0.5)
    f0 = d.residual_vec_zeta(v0, res_weight=1 / wz).detach(); f0[-3:] = 0
    v = d.pack(st['q'].to(dev), st['cl'])
    print("=== closure tail=%s exps=%s: start |F - lam f0| = %.3e" % (tail, exps, float((d.residual_vec_zeta(v, res_weight=1 / wz) - lam * f0).norm())), flush=True)
    v, r, hist = lm_solve(d, v, 0.5, maxit=60, lam0=1e-3, logf=None, f0=f0, hlam=lam, svd_cut=1e-11)
    h = hist[-1]
    print("    final: |res| = %.3e  c_l = %.5f  id = %.2e  psi_yy0 = %.1e  Rz_n = %.2e  its = %d" % (h['res_norm'], h['cl'], h['cl_identity'], h['psi_yy0'], h['Rz_max_norm'], len(hist)), flush=True)
