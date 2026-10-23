"""load_state.py -- standalone loader / evaluator for the saved states cited in the report (lead 07:40Z reconstruction package).

usage:  python3 load_state.py <state.pt> [--points 'x1,y1;x2,y2;...'] [--json out.json] [--device cpu|cuda]

For a saved state (Q/QL representation: keys beta, cl, N, M, L, Lf, p; or the first-shift ipm3 representation: keys b, cl, gamma, N, M, L, p, mu)
this script rebuilds the discretisation from the saved parameters (N, M, L, Lf, c_l, map power p, and the optimizer's angular oversampling M2 when saved in 'options'; the old ipm3 representation reconstructs gamma = 1/c_l), recomputes the canonical velocity with the modal Green-function inverse (the same
inverse the solver used), and prints
  * file, sha256, representation, N, M, L, c_l, gamma = 1/c_l (and mu for forced states),
  * a0 = rho_y(0), c = psi_xy(0), the centre defect c_l + c - 1, the y-axis far-field amplitude K (rho(0, y) ~ K y^gamma),
  * the cubic origin coefficients b = rho_xxy(0)/2 and e = rho_yyy(0)/6 (rho = a0 y + b x^2 y + e y^3 + ...; Q states only, from beta_0'(-1), beta_1(-1)),
  * the between-node sampled maxima of |R|, |R|/N_f, |R|/N_v by region (r < 0.1, 0.1-1, 1-100, > 100) on the NUM_REPORT section 7 sample set
    (midpoints of the radial nodes in t and of the quadrant angles plus four near-axis angles and the y-axis; radii beyond 1e120 discarded; finite sampled
    maxima, not suprema; for forced states the regional statistics use R_f = R - mu y phi(r), phi = (1 + r^2/Lf^2)^-2); the maximising (r, theta) is
    recorded for max |R| (or |R_f|) only,
  * rho, rho_x, rho_y, U_1, U_2, psi, R (the UNFORCED residual; for forced states an extra column R_f = R - mu y phi), N_f, N_v at the requested points (x, y) in any quadrant (evaluated at (|x|, |y|) with the parities applied;
    axis points at exact theta = 0 or pi/2; default points (0.5, 0.5), (3, 0), (0, 3), (6, 8), (30, 40)).
Definitions: R = (c_l X + U).grad rho - rho; N_f = |(c_l x + U_1) rho_x| + |(c_l y + U_2) rho_y| + |rho|; N_v = |rho| + |X.grad rho| + |U.grad rho|.
The evaluation is the producer's own (discrete inverse); the verifier's canonical evaluations differ near the x-axis for the unconverged fixed-c_l
states by factors up to 3 .. 11 at the maximisers (NUM_REPORT 4L(c14)).  Requires numpy and torch; imports the solver modules from ../src.
"""
import sys, os, math, hashlib, json, argparse, numpy as np, torch
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'src'))
import ipm3, ipm3s, ipm3q, ipm3ql
torch.set_default_dtype(torch.float64)

def load(path, device='cpu'):
    st = torch.load(path, weights_only=False, map_location='cpu'); cl = float(st['cl']); N, M, L = int(st['N']), int(st['M']), float(st['L']); gamma = 1.0 / cl
    out = dict(file=os.path.basename(path), sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(), N=N, M=M, L=L, cl=cl, gamma=gamma, mu=st.get('mu', None))
    if 'beta' in st and hasattr(st['beta'], 'shape'):
        Lf = float(st.get('Lf', L)); p_saved = float(st['p']) if 'p' in st else 1 / (1 - gamma); p_rebuilt = 1 / (1 - gamma)
        frozen = abs(p_saved - p_rebuilt) > 1e-8 * p_rebuilt
        gam_eff = 1 - 1 / p_saved if frozen else gamma
        M2 = st.get('options', {}).get('M2', None) if isinstance(st.get('options', None), dict) else None   # the optimizer's angular oversampling (3M for the fixed-c_l chains), else the default M + 2
        mdl = ipm3ql.IPM3QL(N=N, M=M, L=L, gamma=gam_eff, p=(p_saved if frozen else None), device=device, Lf=Lf, M2=M2)
        coef = st['beta'].to(device); flds = mdl.fields(coef); out.update(rep='Q (rho = y w b, b = sum sigma^k beta_k cos 2k theta)', Lf=Lf, frozen_map=frozen, p=p_saved, M2=mdl.M2, gamma_eff=gam_eff)
        a0 = coef[0, 0].item(); kappa = 2.0 ** (2 * mdl.p) / L ** 2
        d0 = 2 * (mdl.rad.DR @ coef)[0, 0].item(); d1 = coef[0, 1].item()
        out.update(b=kappa * (d0 - a0 + d1), e=kappa * (d0 - a0 - d1))
        bk1 = (mdl.rad.ext1_R @ coef).reshape(-1).cpu().numpy(); out['K'] = 0.5 * L ** (1 - gam_eff) * float((bk1 * np.cos(np.pi * np.arange(M))).sum())
        phi = lambda r: (1 + r ** 2 / Lf ** 2) ** (-2)
    else:
        mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=device); mdl.rad.rmap_np = mdl.rad.rmap
        coef = st['b'].to(device); flds = mdl.fields(coef); out.update(rep='ipm3 (rho = y w b, b on the Radau x angle grid)', Lf=float(st.get('Lf', L)))
        a0 = coef[0, 0].item(); bhat = mdl.ang.to_coef(coef, 'EE'); bk1 = (mdl.rad.ext1_R @ bhat).reshape(-1).cpu().numpy()
        out['K'] = L ** (1 - gamma) * float((bk1 * np.cos(np.pi * np.arange(len(bk1)))).sum()); out.update(b=None, e=None)
        phi = lambda r: (1 + r ** 2 / out['Lf'] ** 2) ** (-2)
    c = mdl.psi_xy0(flds).item(); out.update(a0=a0, c=c, centre_defect=cl + c - 1)
    return st, mdl, coef, flds, phi, out

def sample_set(mdl):
    tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    extra = np.array([th[0] / 4, th[0] / 2, (th[-1] + np.pi / 2) / 2, np.pi / 2 - (np.pi / 2 - th[-1]) / 4, np.pi / 2])
    tha = np.sort(np.concatenate([thm, extra])); rm = mdl.rad.rmap_np(torch.tensor(tm)).numpy() if hasattr(mdl.rad.rmap_np(torch.tensor(tm)), 'numpy') else mdl.rad.rmap_np(tm)
    rm = np.asarray(rm, dtype=np.float64); keep = rm < 1e120
    return np.meshgrid(rm[keep], tha, indexing='ij')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--points', default='0.5,0.5;3,0;0,3;6,8;30,40', help="semicolon-separated list of x,y pairs, e.g. '0.5,0.5;-0.5,0.5;3,0'"); ap.add_argument('--json', default=None); ap.add_argument('--device', default='cpu')
    a = ap.parse_args(); st, mdl, coef, flds, phi, out = load(a.state, a.device)
    print(f"file {out['file']}  sha256 {out['sha256']}")
    print(f"rep {out['rep']}; N {out['N']} M {out['M']} L {out['L']} Lf {out['Lf']} c_l {out['cl']:.12f} gamma {out['gamma']:.12f} mu {out['mu']}")
    print(f"a0 = rho_y(0) = {out['a0']:.12f}; c = psi_xy(0) = {out['c']:+.12f}; c_l + c - 1 = {out['centre_defect']:+.6e}; K = {out['K']:.10f}" + (f"; b = {out['b']:+.8f}; e = {out['e']:+.8f}" if out['b'] is not None else "")
          + (f"; forced origin defect a0 (c_l + c - 1) - mu = {out['a0'] * out['centre_defect'] - out['mu']:+.6e}" if out['mu'] is not None else "") + (f"; M2 = {out['M2']} (angular oversampling of the inverse); effective far-field exponent {out['gamma_eff']:.12f}" if 'M2' in out else ""))
    RR, TT = sample_set(mdl); ev = mdl.evaluate(coef, out['cl'], flds, RR, TT)
    mu = out['mu'] if out['mu'] is not None else 0.0
    Rf = ev['R'] - mu * ev['y'] * phi(RR) if mu else ev['R']
    out['sampled'] = {}
    print("between-node sampled maxima (region: max|R|, at (r, theta); max|R|/N_f; max|R|/N_v)" + ("  [forced: R -> R_f = R - mu y phi]" if mu else ""))
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e300)]:
        m = (RR >= lo) & (RR < hi)
        if not m.any(): continue
        aR = np.abs(Rf) * m; i = np.unravel_index(np.argmax(aR), aR.shape); q = (np.abs(Rf) / ev['Nf'])[m].max(); qv = (np.abs(Rf) / ev['Nv'])[m].max()
        out['sampled'][f'{lo}-{hi}'] = dict(maxR=float(aR[i]), r=float(RR[i]), theta=float(TT[i]), maxR_Nf=float(q), maxR_Nv=float(qv))
        print(f"  [{lo:g}, {hi:g}): {aR[i]:.4e} at ({RR[i]:.4e}, {TT[i]:.5f}); {q:.4e}; {qv:.4e}")
    # general (x, y): evaluate at (|x|, |y|) with EXACT axis angles (theta = 0 or pi/2; no clipping) and apply the parities (verifier result 181):
    # rho, R: even in x, odd in y;  rho_x: odd in x, odd in y;  rho_y: even, even;  U_1 = -psi_y: odd in x, even in y;  U_2 = psi_x: even in x, odd in y;
    # psi: odd in x, odd in y;  N_f, N_v: even, even.  The origin itself (r = 0) is excluded (polar representation).
    pts = [tuple(float(v) for v in p.split(',')) for p in a.points.split(';') if p.strip()]; xs = np.array([p[0] for p in pts]); ys = np.array([p[1] for p in pts])
    sx = np.where(xs < 0, -1.0, 1.0); sy = np.where(ys < 0, -1.0, 1.0); ax, ay = np.abs(xs), np.abs(ys)
    rr = np.hypot(ax, ay); th = np.arctan2(ay, ax); e2 = mdl.evaluate(coef, out['cl'], flds, rr, th)
    par = dict(rho=(1, -1), rho_x=(-1, -1), rho_y=(1, 1), U1=(-1, 1), U2=(1, -1), psi=(-1, -1), R=(1, -1), Nf=(1, 1), Nv=(1, 1))
    print("points (x, y) [parities applied; axis points evaluated at exact theta = 0 or pi/2]: rho, rho_x, rho_y, U_1, U_2, psi, R, N_f, N_v" + (", R_f = R - mu y phi" if mu else ""))
    out['points'] = []
    for i, (x, y) in enumerate(pts):
        if rr[i] == 0: print(f"  ({x:g}, {y:g}): origin not evaluated (rho = 0, rho_y = a0 analytically)"); continue
        row = [float(e2[k][i]) * (sx[i] if par[k][0] < 0 else 1.0) * (sy[i] if par[k][1] < 0 else 1.0) for k in ['rho', 'rho_x', 'rho_y', 'U1', 'U2', 'psi', 'R', 'Nf', 'Nv']]
        if mu: row.append(row[6] - mu * y * phi(rr[i]))                                         # forced residual at the point (R is the unforced one)
        out['points'].append(dict(x=x, y=y, values=row)); print(f"  ({x:g}, {y:g}): " + " ".join(f"{v:+.10e}" for v in row))
    if a.json:
        json.dump(out, open(a.json, 'w'), indent=1); print('json written to', a.json)

if __name__ == '__main__':
    main()
