"""Evaluate the B2-P residuals of a state at arbitrary Cartesian points (x > 0 by symmetry) with the exact modal inverse
(no interpolation): builds a product grid (radii x angles) containing the points and picks them out.
Default point set: the verifier's seven independent points (verification verification/r2_projected_fullplane/SUMMARY.md)."""
import sys, os, json, argparse, numpy as np, torch, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)
DEFAULT_PTS = [(0.13, 0.27), (0.63, -0.42), (1.13, 0.73), (0.0, 0.81), (-0.63, -0.42), (0.47, 0.0), (2.03, -1.17)]

def point_geometry(b, beta_b, L, rmap, pts):
    """Return (geometry, index list) for a product grid whose radii/angles cover the given points."""
    pts = np.array(pts, float)
    x = np.abs(pts[:, 0]); y = pts[:, 1]
    x = np.maximum(x, 1e-9)                      # points on the axis: use the limit x -> 0+
    r = np.sqrt(x ** 2 + y ** 2); phi = np.arctan2(x, -y)
    gtmp = Geometry.__new__(Geometry); gtmp.beta_t = torch.tensor(float(beta_b), dtype=DT); gtmp.L_t = torch.tensor(float(L), dtype=DT); gtmp.rmap = rmap; gtmp.beta = float(beta_b); gtmp.L = float(L)
    t = gtmp.t_of_r(torch.tensor(r, dtype=DT)).numpy()
    bp = copy.copy(b)
    bp.t_coll = np.array(t); bp.w_coll = np.ones_like(t); bp.Nc = len(t)
    bp.phi = np.array(phi); bp.eta = np.cos(phi); bp.sphi = np.sin(phi); bp.Nphi = len(phi)
    kk = np.arange(b.K); ks = np.arange(1, b.K + 1)
    bp.C = np.cos(np.outer(phi, kk)); bp.S = np.sin(np.outer(phi, kk)); bp.Ssin = np.sin(np.outer(phi, ks)); bp.Csin = np.cos(np.outer(phi, ks))
    U = np.zeros((len(phi), b.K)); dU = np.zeros_like(U); U[:, 0] = 1
    if b.K > 1: U[:, 1] = 2 * bp.eta; dU[:, 1] = 2
    for k in range(2, b.K):
        U[:, k] = 2 * bp.eta * U[:, k - 1] - U[:, k - 2]; dU[:, k] = 2 * U[:, k - 1] + 2 * bp.eta * dU[:, k - 1] - dU[:, k - 2]
    bp.U, bp.dU = U, dU
    bp.B_coll, bp.dB_coll = b._design(bp.t_coll)
    bp.to_torch()
    g = Geometry(bp, beta_b, L, rmap=rmap)
    idx = [i * bp.Nphi + i for i in range(len(pts))]       # diagonal of the product grid
    return g, idx, pts

def main(path, pts=DEFAULT_PTS):
    dev = 'cuda'
    cF, cG, meta = load_state(path, dev)
    beta, L = meta['beta'], meta['L']; beta_b = meta.get('beta_basis', beta); rmap = str(meta.get('rmap', 'r'))
    b = basis_from_meta(meta, dev)
    g, idx, P = point_geometry(b, beta_b, L, rmap, pts)
    p = Problem(g, beta_dyn=beta); f = p.fields(cF, cG)
    RF, RG, NF, NG = p.residuals(cF, cG, f)
    rows = []
    for n, i in enumerate(idx):
        xx = g.x[i].item(); yy = g.y[i].item()
        rows.append(dict(x=float(P[n, 0]), y=float(P[n, 1]), RF_over_NF=(RF[i] / NF[i]).abs().item(), RG_over_NG=(RG[i] / NG[i]).abs().item(),
                         RTheta=(RF[i] * xx ** 2).item(), ROmega=(RG[i] * xx).item(), Theta=(f['F'][i] * xx ** 2).item(), Omega=(f['G'][i] * xx).item(),
                         W1=(f['A'][i] * xx).item() * np.sign(P[n, 0] if P[n, 0] != 0 else 1), W2=f['B'][i].item()))
    return dict(file=path, beta=beta, points=rows, max_RF_over_NF=max(r['RF_over_NF'] for r in rows), max_RG_over_NG=max(r['RG_over_NG'] for r in rows))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('state'); a = ap.parse_args()
    out = main(a.state)
    print(json.dumps({k: v for k, v in out.items() if k != 'points'}))
    for r in out['points']:
        print(f"({r['x']:+.2f},{r['y']:+.2f}): |RF/NF|={r['RF_over_NF']:.3e} |RG/NG|={r['RG_over_NG']:.3e} RTheta={r['RTheta']:+.3e} ROmega={r['ROmega']:+.3e} Theta={r['Theta']:.4f} Omega={r['Omega']:.4f} W=({r['W1']:+.3f},{r['W2']:+.3f})")
