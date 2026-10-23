"""Near-origin structure of b for a saved state: b_0(r) - a0 and b_k(r) on small radii, log-log slope fits.
A smooth rho needs b_0 - a0 = O(r^2) with even powers only and b_k = O(r^{2k})."""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
for f in sys.argv[1:]:
    st = torch.load(f); dev='cuda'
    mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
    b = st['b'].to(dev); a0 = b[0,0].item()
    bhat = mdl.ang.to_coef(b, 'EE')             # (N+1, M) radial functions of cos(2k th) modes
    rr = np.logspace(-4, -0.5, 36)
    t = mdl.rad.t_of_r(rr)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, t, mdl.rad.wR_np), device=dev)
    bk = (P @ bhat).cpu().numpy()
    d0 = bk[:,0] - a0
    print(f"{f}: cl={st['cl']:.6f} a0={a0:.6f}  A=2cl-1={2*st['cl']-1:.4f}; lead's indicial estimate d-1 ~ a0/(A+3) = {a0/(2*st['cl']-1+3):.3f}")
    print("     r        b0-a0        b1          b2          local slope of |b0-a0|, b1, b2")
    for i in range(0, len(rr), 5):
        sl = lambda y, j: (np.log(abs(y[j+1])) - np.log(abs(y[j-1])))/(np.log(rr[j+1]) - np.log(rr[j-1])) if 0 < j < len(rr)-1 else float('nan')
        print(f" {rr[i]:9.2e}  {d0[i]:+.4e}  {bk[i,1]:+.4e}  {bk[i,2]:+.4e}    {sl(d0,i):6.3f} {sl(bk[:,1],i):6.3f} {sl(bk[:,2],i):6.3f}")
