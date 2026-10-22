"""Decomposition of the least-squares objective of a saved state by radial band (external referee's diagnostic 1): the weighted residual
rows of lm_solve (wa R_a, wG R_G on the 2N x 2M collocation nodes, plus origin rows and, if present, the first-tail rows) are
evaluated at the saved coefficients and their squared sums are grouped by the radius of the node. Printed per band: the number of
nodes, the fraction of the total squared loss in the band (a and G rows separately), the band RMS (sqrt of mean squared weighted row
in the band) and the max |wa R_a|, |wG R_G| in the band. Fitted-state data; where the objective 'comes from' at this N, no more."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import LMProblem, load_state, dev, DT
BANDS = [(0, 1), (1, 2), (2, 5), (5, 10), (10, 20), (20, 30), (30, 100), (100, 1e3), (1e3, 1e5), (1e5, np.inf)]
def build(d):
    tail = float(d['tail']) if ('tail' in d and float(d['tail']) > 0) else None
    p = LMProblem(int(d['N']), int(d['M']), float(d['L']), float(d['beta_map']), float(d['sigma_a']), float(d['sigma_G']),
                  float(d['a0_target']), float(d['w_origin']), float(d['beta']), ov=float(d['Ne']) / int(d['N']),
                  mapname=str(d['mapname']), Rw=float(d['Rw']), tail=tail, t1=(float(d['t1']) if tail else 1e-5))
    z = p.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), float(d['beta']))
    return p, z
def main(paths):
    for path in paths:
        d = load_state(path); p, z = build(d)
        with torch.no_grad():
            F = p.F(z).cpu().numpy()
        n = p.model.r.shape[0] * p.model.th.shape[0]; r = np.repeat(np.asarray(p.model.r), p.model.th.shape[0]) if False else np.asarray(torch.as_tensor(p.model.r).cpu()).repeat(p.model.th.shape[0])
        Fa, FG, rest = F[:n], F[n:2 * n], F[2 * n:]
        tot = float(np.sum(F**2)); rms = np.sqrt(tot / len(F))
        print(f"=== {path}: N={p.N} M={p.M} rows={len(F)} (a {n}, G {n}, other {len(rest)}); |F|/sqrt(rows) = {rms:.4e}; total squared loss {tot:.4e}; other rows' share {np.sum(rest**2)/tot:.3e}")
        print("   band          nodes   share_a   share_G   bandRMS_a  bandRMS_G  max|wa Ra|  max|wG RG|")
        for lo, hi in BANDS:
            m = (r >= lo) & (r < hi)
            if m.sum() == 0: continue
            print(f"   [{lo:>5g},{hi:>6g})  {int(m.sum()):6d}  {np.sum(Fa[m]**2)/tot:8.3e}  {np.sum(FG[m]**2)/tot:8.3e}  {np.sqrt(np.mean(Fa[m]**2)):9.3e}  {np.sqrt(np.mean(FG[m]**2)):9.3e}  {np.abs(Fa[m]).max():9.3e}  {np.abs(FG[m]).max():9.3e}")
if __name__ == '__main__': main(sys.argv[1:])
