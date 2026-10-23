"""Conditioning in smoothness-weighted norms (lead's request 3, crude version).  For a saved forced state, build the
(b, c_l)-Jacobian of the unforced system WITHOUT the identity row and WITHOUT the gauge row (rows: continuity, interior
equations), project the scaling generator g = -(r b_r + omega b) out of the b-space, and compute the smallest singular
value of  D_Y^{sY/2} T_Y J T_X^{-1} D_X^{-sX/2}  where T maps grid values to (Chebyshev in t) x (cos 2k theta)
coefficients and D = diag(1 + n^2 + (2k)^2) (n radial, k angular degree); sX = s, sY = s - 1 (transport loses one
derivative).  Also the raw coefficient-norm smin for comparison.  Reported for several s at several resolutions."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
def analyze(mdl, b, cl, label, svals=(0.0, 2.0, 3.0, 4.0)):
    N, M = mdl.N, mdl.M; nb = (N+1)*M
    flds = mdl.fields(b)
    Jfull = mdl.jacobian(b, cl, flds)                 # rows: M-1 continuity, identity, N*M interior, gauge ; cols: nb + 1
    # square unforced linearization at fixed c_l with the (redundant) identity row replaced by the gauge row:
    rows = list(range(0, M-1)) + [nb] + list(range(M, nb))
    J = Jfull[rows][:, :nb]                            # (nb, nb), laid out as (N+1, M): centre block = continuity + gauge
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(N+1))); Vinv = torch.tensor(np.linalg.pinv(V), device=dev).contiguous()
    A = mdl.ang.A["EE"].contiguous()
    TX = torch.kron(Vinv, A)                           # grid values (flattened (N+1, M)) -> Chebyshev x cos coefficients
    TXinv = torch.linalg.inv(TX)
    n = torch.arange(N+1, device=dev, dtype=torch.float64); k = torch.arange(M, device=dev, dtype=torch.float64)
    D = (1 + n[:, None]**2 + (2*k[None, :])**2).reshape(-1)
    out = []
    for s in svals:
        Jw = (D**(max(s-1, 0)/2))[:, None] * (TX @ J @ TXinv) * (D**(-s/2))[None, :]
        sv = torch.linalg.svdvals(Jw)
        out.append((s, sv[-1].item(), sv[-2].item(), sv[0].item()))
    svraw = torch.linalg.svdvals(J)
    msg = f"{label} N={N} M={M} cl={cl:.6f}: raw smin {svraw[-1].item():.2e} (s2 {svraw[-2].item():.2e}, smax {svraw[0].item():.2e}); weighted (X^s -> Y^(s-1), D = 1+n^2+4k^2): " + "; ".join(f"s={s:g}: smin {a:.2e} s2 {b2:.2e} smax {c:.2e}" for s,a,b2,c in out)
    print(msg, flush=True); return msg
if __name__ == '__main__':
    files = sys.argv[1:]
    log = open('runs/weighted_smin.log', 'a')
    for f in files:
        st = torch.load(f)
        mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); mdl.gauge = 'inf'
        msg = analyze(mdl, st['b'].to(dev), st['cl'], f); log.write(msg + "\n"); log.flush()
