"""stagnation_search.py -- whole-half-plane search for stagnation points of the transport field of a stored state (shift 6; prompt sec. 4
item 1/3: "any other stagnation points/separatrices", "stagnation-point locations/derivatives").

Transport field evaluated with the lane's modal whole-plane inverse at ARBITRARY points (fixedsrc.cross_inverse + velocity_from_modes):
  lambda-path states (source_mode fixed_velocity_block):  W = beta X + U_rel[Omega] + lambda U_rel[f]   (f in its seed geometry)
  eps-forcing states (eps < 1, cG_ext):                   W = beta X + U_rel[eps Omega + (1 - eps) Omega_ext]
  unforced evaluation (--unforced 1):                     W = beta X + U_rel[Omega]   (the B2-P field of the stored vorticity alone)
U_rel is the velocity of the modal inverse normalized to vanish at the centre (the B2-P field uses U - U(0); the gauge constant drops out).
Method: q = |W|/(beta r) on a log-polar grid (r in [r_lo, r_hi], phi in (0, pi), x = r sin phi > 0), the axis phi = 0, pi included;
EVERY local minimum of q below --qmax is refined by Newton on W = 0 (FD Jacobian, step 1e-6 r); converged zeros (|W| <= 1e-9 beta r) are
reported with DW (eigenvalues: saddle / node / focus) and classified axis / off-axis (n_newton_starts records how many minima qualified). Also: axis zeros by sign change of W_2(0, +-r),
the minimum of q per radial band, the minimum of W.X/(beta r^2) per band (inward flow), and the number of grid points with W.X < 0.
The search is a sampled grid search (resolution Nr x Nphi) with local refinement: a detection heuristic. It can miss zeros between grid points
where q is not small on the grid, zeros outside [r_lo, r_hi], tangential axis zeros and double crossings within one axis interval; sampled
positivity of W.X is not positivity everywhere and does not classify invariant curves (astra shift6a).
Usage: python3 code/stagnation_search.py runs/state.npz [--Nr 400] [--Nphi 181] [--r_lo 0.02] [--r_hi 1e5] [--qmax 0.5] [--unforced 0] [--out runs/stag_<tag>.json]"""
import sys, os, json, argparse, time, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from fixedsrc import cross_inverse, velocity_from_modes
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)
dev = 'cuda'


class WField:
    def __init__(self, path, unforced=False):
        cF, cG, meta = load_state(path, dev)
        self.meta = meta; self.beta = float(meta['beta']); L = float(meta['L']); bb = float(meta.get('beta_basis', self.beta)); rmap = str(meta.get('rmap', 'r'))
        self.lam = float(meta.get('lam', 0.0)); self.eps = float(meta.get('eps', 1.0))
        b = basis_from_meta(meta, dev); self.g = Geometry(b, bb, L, rmap=rmap)
        self.cG = cG.clone(); self.terms = [(self.g, self.cG, 1.0)]; self.desc = 'beta X + U_rel[Omega]'
        if not unforced:
            if str(meta.get('source_mode', '')) == 'fixed_velocity_block' and np.asarray(meta['cG_f']).size > 0:
                bs = Basis(int(meta['seed_Nt']), int(meta['seed_deg']), int(meta['seed_K']), int(meta['seed_Nphi']), ng_coll=int(meta['seed_ngc']), m_reg=int(meta['seed_mreg']), device=dev, grade=float(meta['seed_grade'])) \
                    if 'seed_K' in meta else b
                gs = Geometry(bs, float(meta['beta_seed']), float(meta.get('seed_L', L)), rmap=str(meta.get('seed_rmap', rmap)))
                self.terms.append((gs, torch.tensor(np.asarray(meta['cG_f']), dtype=DT, device=dev), self.lam)); self.desc = f'beta X + U_rel[Omega] + {self.lam:g} U_rel[f]'
            elif self.eps < 1.0 and np.asarray(meta.get('cG_ext', np.zeros(0))).size > 0:
                cext = torch.tensor(np.asarray(meta['cG_ext']), dtype=DT, device=dev)
                self.terms = [(self.g, self.eps * self.cG + (1 - self.eps) * cext, 1.0)]; self.desc = f'beta X + U_rel[{self.eps:g} Omega + {1 - self.eps:g} Omega_ext]'

    def U(self, x, y):
        """relative velocity (U1, U2) at points x >= 0 (torch 1D)."""
        r = torch.sqrt(x ** 2 + y ** 2)
        U1 = torch.zeros_like(x); U2 = torch.zeros_like(x)
        for g, c, w in self.terms:
            if w == 0.0:
                continue
            Psi, dPsi = cross_inverse(g, c, r)
            u1, u2 = velocity_from_modes(Psi, dPsi, x, y)
            U1 = U1 + w * u1; U2 = U2 + w * u2
        return U1, U2

    def W(self, x, y):
        U1, U2 = self.U(x, y)
        return self.beta * x + U1, self.beta * y + U2


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--Nr', type=int, default=400); ap.add_argument('--Nphi', type=int, default=181)
    ap.add_argument('--r_lo', type=float, default=0.02); ap.add_argument('--r_hi', type=float, default=1e5); ap.add_argument('--qmax', type=float, default=0.1)
    ap.add_argument('--unforced', type=int, default=0); ap.add_argument('--out', type=str, default=''); ap.add_argument('--chunk', type=int, default=40)
    a = ap.parse_args(); t0 = time.time()
    wf = WField(a.state, unforced=bool(a.unforced)); beta = wf.beta
    r = torch.logspace(np.log10(a.r_lo), np.log10(a.r_hi), a.Nr, dtype=DT, device=dev)
    phi = torch.linspace(0, np.pi, a.Nphi, dtype=DT, device=dev)
    W1 = torch.zeros(a.Nr, a.Nphi, dtype=DT, device=dev); W2 = torch.zeros_like(W1)
    X = r[:, None] * torch.sin(phi)[None, :]; Y = -r[:, None] * torch.cos(phi)[None, :]
    for s in range(0, a.Nr, a.chunk):       # chunks of radii (cross_inverse builds n x Nq weights)
        sl = slice(s, min(a.Nr, s + a.chunk))
        w1, w2 = wf.W(X[sl].reshape(-1), Y[sl].reshape(-1)); W1[sl] = w1.reshape(-1, a.Nphi); W2[sl] = w2.reshape(-1, a.Nphi)
    R = torch.sqrt(X ** 2 + Y ** 2)
    q = torch.sqrt(W1 ** 2 + W2 ** 2) / (beta * R)
    WX = (W1 * X + W2 * Y) / (beta * R ** 2)
    out = dict(file=a.state, beta=beta, lam=wf.lam, eps=wf.eps, field=wf.desc, grid=dict(Nr=a.Nr, Nphi=a.Nphi, r_lo=a.r_lo, r_hi=a.r_hi))
    qn = q.cpu().numpy(); rn = r.cpu().numpy(); pn = phi.cpu().numpy()
    # local minima of q (8-neighbourhood) below qmax; the axis columns (j = 0, Nphi-1) use one-sided neighbourhoods
    qp = np.pad(qn, 1, mode='edge'); qp[0, :] = np.inf; qp[-1, :] = np.inf
    nb = np.stack([qp[i:i + a.Nr, j:j + a.Nphi] for i in range(3) for j in range(3) if not (i == 1 and j == 1)], 0).min(0)
    locmin = np.argwhere((qn <= nb) & (qn < a.qmax))
    out['n_local_minima_below_qmax'] = int(len(locmin))
    # Newton refinement
    zeros = []; near = []
    def Wnp(xy):
        x = torch.tensor([max(xy[0], 0.0)], dtype=DT, device=dev); y = torch.tensor([xy[1]], dtype=DT, device=dev)
        w1, w2 = wf.W(x, y); return np.array([w1.item(), w2.item()])
    out['n_newton_starts'] = int(len(locmin))
    for (i, j) in locmin:
        xy = np.array([X[i, j].item(), Y[i, j].item()]); rr = float(np.hypot(*xy)); on_axis = (j == 0 or j == a.Nphi - 1)
        ok = False
        for it in range(25):
            w = Wnp(xy); h = 1e-6 * max(np.hypot(*xy), 1e-3)
            if on_axis:
                # the axis x = 0 is invariant: one-dimensional Newton in y on W_2(0, y)
                d2 = (Wnp([0.0, xy[1] + h])[1] - Wnp([0.0, xy[1] - h])[1]) / (2 * h)
                if abs(d2) < 1e-14: break
                xy = np.array([0.0, xy[1] - w[1] / d2])
            else:
                J = np.zeros((2, 2))
                J[:, 0] = (Wnp([xy[0] + h, xy[1]]) - Wnp([max(xy[0] - h, 0.0), xy[1]])) / (xy[0] + h - max(xy[0] - h, 0.0))
                J[:, 1] = (Wnp([xy[0], xy[1] + h]) - Wnp([xy[0], xy[1] - h])) / (2 * h)
                try:
                    step = np.linalg.solve(J, w)
                except np.linalg.LinAlgError:
                    break
                sn = np.linalg.norm(step); rr = max(np.hypot(*xy), 1e-6)
                if sn > 0.5 * rr: step *= 0.5 * rr / sn
                xy = xy - step
                if xy[0] < 0: xy[0] = 0.0; on_axis = True
            if np.hypot(*xy) > 10 * a.r_hi or np.hypot(*xy) < 0.5 * a.r_lo: break      # left the search region (toward the centre, the only zero at r -> 0)
            w = Wnp(xy)
            if np.linalg.norm(w) <= 1e-9 * beta * max(np.hypot(*xy), 1e-6):
                ok = True; break
        w = Wnp(xy); rr = float(np.hypot(*xy))
        rec = dict(start=dict(r=float(rn[i]), phi=float(pn[j]), q=float(qn[i, j])), x=float(xy[0]), y=float(xy[1]), r=rr, q=float(np.linalg.norm(w) / (beta * max(rr, 1e-12))), on_axis=bool(on_axis or xy[0] < 1e-9 * rr))
        if ok:
            h = 1e-5 * max(rr, 1e-3); J = np.zeros((2, 2))
            J[:, 0] = (Wnp([xy[0] + h, xy[1]]) - Wnp([max(xy[0] - h, 0.0), xy[1]])) / (xy[0] + h - max(xy[0] - h, 0.0))
            J[:, 1] = (Wnp([xy[0], xy[1] + h]) - Wnp([xy[0], xy[1] - h])) / (2 * h)
            ev = np.linalg.eigvals(J)
            rec['DW'] = J.tolist(); rec['eig'] = [complex(e).real for e in ev] if np.all(np.abs(ev.imag) < 1e-10) else [str(e) for e in ev]
            rec['type'] = ('saddle' if np.all(np.abs(ev.imag) < 1e-10) and ev.real.prod() < 0 else ('node' if np.all(np.abs(ev.imag) < 1e-10) else 'focus')) + (' (axis)' if rec['on_axis'] else ' (off-axis)')
            zeros.append(rec)
        else:
            near.append(rec)
    out['stagnation_points'] = zeros; out['unconverged_local_minima'] = near[:20]
    mq = torch.where(R >= a.r_lo, q, torch.full_like(q, 1e9)); jq = int(torch.argmin(mq))
    out['global_min_q'] = dict(q=float(q.reshape(-1)[jq]), x=float(X.reshape(-1)[jq]), y=float(Y.reshape(-1)[jq]), r=float(R.reshape(-1)[jq]),
                               note='(beta - c)/beta = %.4f is the horizontal-ray value of q near the centre for total strain c = 1 + beta/2' % ((beta - 1 - beta / 2) / beta))
    # axis zeros by sign change (fine 1D scan), both half-axes
    ra = torch.logspace(np.log10(a.r_lo), np.log10(a.r_hi), 4000, dtype=DT, device=dev); zx = torch.zeros_like(ra)
    ax = {}
    for name, yy in [('up', ra), ('down', -ra)]:
        w1, w2 = wf.W(zx, yy); pr = w2.cpu().numpy(); rv = ra.cpu().numpy(); z = []
        for i in range(len(pr) - 1):
            if pr[i] * pr[i + 1] < 0: z.append(float(rv[i] - pr[i] * (rv[i + 1] - rv[i]) / (pr[i + 1] - pr[i])))
        sgn = 1.0 if name == 'up' else -1.0; rel = sgn * pr / (beta * rv); k = int(np.argmin(rel))
        ax[name] = dict(zeros_r=z[:10], min_rel_outward=float(rel[k]), at_r=float(rv[k]))
    out['axis'] = ax
    bands = {}
    for lo, hi in [(a.r_lo, 0.3), (0.3, 1), (1, 3), (3, 10), (10, 100), (100, 1e3), (1e3, 1e4), (1e4, a.r_hi)]:
        mb = (R >= lo) & (R < hi)
        if mb.any():
            jq = int(torch.argmin(torch.where(mb, q, torch.full_like(q, 1e9)))); jw = int(torch.argmin(torch.where(mb, WX, torch.full_like(WX, 1e9))))
            bands[f'{lo:g}-{hi:g}'] = dict(min_q=float(q.reshape(-1)[jq]), at=(float(X.reshape(-1)[jq]), float(Y.reshape(-1)[jq])), min_WX=float(WX.reshape(-1)[jw]), at_WX=(float(X.reshape(-1)[jw]), float(Y.reshape(-1)[jw])), n_WX_neg=int((WX[mb] < 0).sum()))
    out['bands'] = bands; out['n_grid_WX_negative'] = int((WX < 0).sum()); out['time_s'] = time.time() - t0
    js = json.dumps(out, indent=1, default=str); print(js)
    if a.out:
        open(a.out, 'w').write(js)


if __name__ == '__main__':
    main()
