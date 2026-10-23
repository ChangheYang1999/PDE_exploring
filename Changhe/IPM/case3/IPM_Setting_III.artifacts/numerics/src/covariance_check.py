"""covariance_check.py -- (1) exact scale covariance of the mapped discrete problem: evaluate the coefficients u of a saved state (map L) in the model
with map L' and the same gK; if the mapped problem is exactly covariant the node residual vector, a0 and c are unchanged (NUM_REPORT 4L(c14)).
(2) residual along the coefficient-space segment between two stall points of the same mapped problem (the L = 1 endpoint and the rescaled restarts).
usage: python3 src/covariance_check.py ref.pt other1.pt [other2.pt]"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3ql
torch.set_default_dtype(torch.float64); dev = 'cuda'
files = sys.argv[1:]; st = [torch.load(f, weights_only=False) for f in files]
s0 = st[0]; N, M, cl, gK, Lf = s0['N'], s0['M'], s0['cl'], s0['gK'], s0['Lf']
def model(L): return ipm3ql.IPM3QL(N=N, M=M, L=L, gamma=1 / cl, device=dev, Lf=Lf, centre='identity', M2=3 * M, fine=True)
q1 = model(s0['L']); u0 = s0['u'].to(dev)
F0, E0, fl0 = q1.system(u0, cl, gK); a00 = q1.beta_full(u0)[0, 0].item(); c0 = q1.psi_xy0(fl0).item()
print(f"ref {files[0]}: L={s0['L']} gK={gK} |F|2={F0.norm().item():.6e} max={F0.abs().max().item():.3e} a0={a00:.10f} c={c0:.10f}")
for Lp in [0.5, 2.0]:
    qp = model(Lp); Fp, Ep, flp = qp.system(u0, cl, gK)
    print(f"  same u in the model with L={Lp}: |F|2={Fp.norm().item():.6e} max|F - F_ref|={(Fp - F0).abs().max().item():.3e} a0={qp.beta_full(u0)[0,0].item():.10f} c={qp.psi_xy0(flp).item():.10f}  (covariance: identical up to rounding)")
# (2) segment between stall points, all evaluated in the reference model (L = s0['L'])
for f, s in zip(files[1:], st[1:]):
    u1 = s['u'].to(dev); F1, _, _ = q1.system(u1, cl, gK)
    print(f"segment ref -> {f} (its own L={s['L']}, gK={s['gK']}): |F|2 at the other endpoint evaluated in the ref model = {F1.norm().item():.4e} (its own log: see runs); |u1-u0|/|u0| = {(u1-u0).norm().item()/u0.norm().item():.3e}")
    line = "   t: |F|2 ="
    for t in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
        ut = u0 + t * (u1 - u0); Ft, _, flt = q1.system(ut, cl, gK)
        line += f" {t:.2f}:{Ft.norm().item():.3e}(a0 {q1.beta_full(ut)[0,0].item():.3f})"
    print(line)
