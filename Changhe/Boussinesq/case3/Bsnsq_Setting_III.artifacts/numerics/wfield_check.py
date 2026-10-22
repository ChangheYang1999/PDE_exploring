"""wfield_check.py -- forced transport field W_lambda = beta X + U_rel[Omega] + lam U_rel[f] of a stored lambda-path state:
axis profile W_2(0, +-r) (the axis x = 0 is invariant, so axis zeros are stagnation points), sign of W.X (inward-flow regions),
and off-axis near-stagnation points on a fine polar grid, for the stored lambda and for a list of other lambda values (same
unknown; predictor view of how the flow changes along the path).  The unknown's velocity comes from the Geometry operators of
its own basis (any beta_basis); the source's from fixedsrc.cross_inverse of cG_f in the SEED geometry (beta_seed).
Usage: python3 code/wfield_check.py state.npz [--lams 0.97,0.96,0.95,0.9,0.5,0] [--ngc 9] [--nphi 48]"""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from fixedsrc import cross_inverse, velocity_from_modes
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)


def axis_U2(Psi, r):
    """U_2(0, y) on the axis from sine-mode data Psi_k(r) (K, n): phi = pi (y = +r): -(1/r) sum k Psi_k (-1)^k; phi = 0 (y = -r): (1/r) sum k Psi_k."""
    K = Psi.shape[0]; ks = torch.arange(1, K + 1, dtype=DT, device=Psi.device)[:, None]
    up = -(ks * Psi * (-1.0) ** ks).sum(0) / r
    down = (ks * Psi).sum(0) / r
    return up, down


def main(path, lams, ngc=9, nphi=48):
    dev = 'cuda'
    cF, cG, meta = load_state(path, dev)
    beta, L = float(meta['beta']), float(meta['L']); bb = float(meta.get('beta_basis', beta)); rmap = str(meta.get('rmap', 'r'))
    lam0 = float(meta.get('lam', 0.0))
    b = basis_from_meta(meta, dev, ngc=ngc, Nphi=nphi); g = Geometry(b, bb, L, rmap=rmap)
    Nc, Nphi = b.Nc, b.Nphi
    r = g.r; x = g.x.reshape(Nc, Nphi); y = g.y.reshape(Nc, Nphi)
    U1u = (g.M_U1 @ cG).reshape(Nc, Nphi); U2u = (g.M_U2 @ cG).reshape(Nc, Nphi)
    Psi_u = torch.einsum('kia,a->ki', g.Psi_op, cG)
    have_src = 'cG_f' in meta and np.asarray(meta['cG_f']).size > 0 and float(meta.get('beta_seed', 0)) > 0
    if have_src:
        bs = basis_from_meta(meta, dev); gs = Geometry(bs, float(meta['beta_seed']), L, rmap=rmap)
        cGf = torch.tensor(np.asarray(meta['cG_f']), dtype=DT, device=dev)
        Psi_f, dPsi_f = cross_inverse(gs, cGf, r)
        Pf = Psi_f[:, :, None].expand(-1, -1, Nphi).reshape(b.K, -1); dPf = dPsi_f[:, :, None].expand(-1, -1, Nphi).reshape(b.K, -1)
        U1f, U2f = velocity_from_modes(Pf, dPf, x.reshape(-1), y.reshape(-1)); U1f = U1f.reshape(Nc, Nphi); U2f = U2f.reshape(Nc, Nphi)
        ax_f = axis_U2(Psi_f, r)
    else:
        U1f = torch.zeros_like(U1u); U2f = torch.zeros_like(U2u); ax_f = (torch.zeros_like(r), torch.zeros_like(r))
    ax_u = axis_U2(Psi_u, r)
    out = dict(file=path, beta=beta, beta_basis=bb, lam_stored=lam0, source_mode=str(meta.get('source_mode', 'n/a')), results={})
    rn = r.cpu().numpy()
    for lam in lams:
        W1 = beta * x + U1u + lam * U1f; W2 = beta * y + U2u + lam * U2f
        rr = torch.sqrt(x ** 2 + y ** 2)
        WX = (W1 * x + W2 * y) / (beta * rr ** 2)                     # 1 for pure dilation
        Wn = torch.sqrt(W1 ** 2 + W2 ** 2) / (beta * rr)              # |W|/(beta r)
        res = {}
        # axis: W_2(0, +r) = beta r + U2_up, W_2(0, -r) = -beta r + U2_down ; zeros beyond the centre
        up = beta * r + ax_u[0] + lam * ax_f[0]; dn = -beta * r + ax_u[1] + lam * ax_f[1]
        for name, prof, sgn in [('axis_up', up, 1.0), ('axis_down', dn, -1.0)]:
            pn = prof.cpu().numpy(); z = []
            for i in range(len(pn) - 1):
                if pn[i] * pn[i + 1] < 0:
                    z.append(float(rn[i] - pn[i] * (rn[i + 1] - rn[i]) / (pn[i + 1] - pn[i])))
            res[name + '_zeros_r'] = z[:10]
            # minimum of the outward speed relative to beta r (1 = pure dilation) for r > 0.05
            m = rn > 0.05
            rel = (sgn * pn / (beta * rn))[m]
            j = int(np.argmin(rel)); res[name + '_min_rel_outward'] = dict(value=float(rel[j]), r=float(rn[m][j]))
        # inward flow / near-stagnation off the axis
        mask = rr > 0.05
        WXm = WX.clone(); WXm[~mask] = 10.0
        j = int(torch.argmin(WXm)); res['min_WX_over_beta_r2'] = dict(value=float(WX.reshape(-1)[j]), x=float(x.reshape(-1)[j]), y=float(y.reshape(-1)[j]))
        Wnm = Wn.clone(); Wnm[~mask] = 10.0
        j = int(torch.argmin(Wnm)); res['min_|W|_over_beta_r'] = dict(value=float(Wn.reshape(-1)[j]), x=float(x.reshape(-1)[j]), y=float(y.reshape(-1)[j]))
        cand = torch.nonzero((Wn < 0.1) & mask)
        res['near_stagnation_points_(|W|<0.1 beta r)'] = [dict(x=float(x[i, k]), y=float(y[i, k]), rel=float(Wn[i, k])) for i, k in cand.tolist()[:12]]
        res['n_points_WX_negative'] = int(((WX < 0) & mask).sum())
        # by radius band: min WX
        bands = {}
        for lo, hi in [(0.05, 0.3), (0.3, 1), (1, 3), (3, 10), (10, 100), (100, 1e4), (1e4, 1e99)]:
            mb = (rr >= lo) & (rr < hi)
            if mb.any():
                bands[f'{lo:g}-{hi:g}'] = float(WX[mb].min())
        res['min_WX_by_band'] = bands
        out['results'][f'{lam:g}'] = res
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--lams', type=str, default=''); ap.add_argument('--ngc', type=int, default=9); ap.add_argument('--nphi', type=int, default=48)
    a = ap.parse_args()
    d = np.load(a.state); lam0 = float(d['lam']) if 'lam' in d.files else 0.0
    lams = [float(v) for v in a.lams.split(',')] if a.lams else [lam0]
    if lam0 not in lams:
        lams = [lam0] + lams
    print(json.dumps(main(a.state, lams, a.ngc, a.nphi), indent=1))
