"""stationarity_check.py -- at saved fixed-c_l Q endpoints: the truncated-SVD Gauss-Newton projection fraction ||P F||^2/||F||^2 (P = projector on the kept
left singular vectors), the predicted relative decrease, and the node residual; a small fraction means the GN direction can no longer reduce |F| much
(referee restart1ref item 5: the unscaled sufficient-decrease test 1e-4 lam can stop a genuine descent direction when this fraction < 1e-4).
usage: python3 src/stationarity_check.py state1.pt [state2.pt ...]"""
import sys, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3ql
torch.set_default_dtype(torch.float64); dev = 'cuda'
for f in sys.argv[1:]:
    st = torch.load(f, weights_only=False); N, M, cl, gK, Lf = st['N'], st['M'], st['cl'], st['gK'], st['Lf']
    q = ipm3ql.IPM3QL(N=N, M=M, L=st['L'], gamma=1 / cl, device=dev, Lf=Lf, centre='identity', M2=3 * M, fine=True)
    u = st['u'].to(dev); F, E, flds = q.system(u, cl, gK); J = q.jacobian(u, cl, gK, flds=flds)[:, :-1]
    U, S, Vh = torch.linalg.svd(J, full_matrices=False); keep = S >= 1e-13 * S[0]
    PF = U[:, keep] @ (U[:, keep].T @ F); frac = (PF.norm() / F.norm()).item() ** 2
    coef = (U[:, keep].T @ (-F)) / S[keep]; du = Vh[keep].T @ coef
    Fn, _, _ = q.system(u + du, cl, gK); Fh, _, _ = q.system(u + 0.5 * du, cl, gK)
    tail = (S[keep][-6:] / S[0]).tolist(); print(f"  smallest kept singular values / S_max: " + " ".join(f"{v:.2e}" for v in tail) + f"; number below 1e-9 S_max: {int((S < 1e-9 * S[0]).sum())}, below 1e-11: {int((S < 1e-11 * S[0]).sum())}")
    print(f"{f}: N={N} |F|2={F.norm().item():.4e} ||PF||^2/||F||^2={frac:.3e} (kept {int(keep.sum())} of {len(S)}; smin kept {S[keep][-1].item():.2e}) "
          f"|du|/|u|={du.norm().item()/u.norm().item():.2e}; |F| after full GN step {Fn.norm().item():.4e}, after half step {Fh.norm().item():.4e}; linear prediction (full) {((F - PF).norm().item()):.4e}")
