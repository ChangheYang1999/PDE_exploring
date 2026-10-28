"""Discretised two-point problem for the sharp Hoelder constant of T_xx.

V(alpha, beta) = sup { int k u dz : [u]_alpha <= 1 },  k(z) = K_beta(z - e1) - K_beta(z),
K_beta(z) = cos(2 arg z - 2 beta) / (2 pi |z|^2).   C_alpha = sup_beta V(alpha, beta).
(beta = 0: increment along the kernel's x-axis; beta = pi/4: diagonal, i.e. T_xy along x-axis.)

Discretisation: cells with masses m_i = int_cell k, node p_i per cell; LP
    max sum m_i u_i  s.t.  u_i - u_j <= |p_i - p_j|^alpha  (all pairs), u_0 = 0,
solved by constraint generation with HiGHS.  Heuristic value only (discretisation error
is not controlled); the dual rows give a transport plan.
"""
import numpy as np, time, json, sys
import highspy

def gl_nodes(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def Kb(zx, zy, beta):
    r2 = zx*zx + zy*zy
    th = np.arctan2(zy, zx)
    return np.cos(2*th - 2*beta)/(2*np.pi*r2)

def k_total(zx, zy, beta):
    return Kb(zx - 1.0, zy, beta) - Kb(zx, zy, beta)

def polar_cells(center, R, q, J, ntheta, theta0, beta, own_sign, ngl=6):
    """Polar cells about `center` (a point near which k has the singular part own_sign*K_beta(z-center)).
    radii R q^-j, j=0..J (J shells), angular edges theta0 + 2 pi l / ntheta.
    Returns nodes (N,2), masses (N,), and cell descriptors (rho_lo, rho_hi, th_lo, th_hi)."""
    cx, cy = center
    radii = R*q**(-np.arange(J+1))
    thetas = theta0 + 2*np.pi*np.arange(ntheta+1)/ntheta
    gx, gw = gl_nodes(ngl)
    nodes, masses, cells = [], [], []
    for j in range(J):
        r_hi, r_lo = radii[j], radii[j+1]
        for l in range(ntheta):
            t_lo, t_hi = thetas[l], thetas[l+1]
            # own kernel, exact: own_sign * log(r_hi/r_lo)/(2 pi) * [sin(2t-2beta)]/2
            own = own_sign*np.log(r_hi/r_lo)/(2*np.pi)*(np.sin(2*t_hi - 2*beta) - np.sin(2*t_lo - 2*beta))/2
            # other kernel by Gauss-Legendre in (log rho, theta)
            lr = 0.5*(np.log(r_hi) + np.log(r_lo)) + 0.5*(np.log(r_hi) - np.log(r_lo))*gx
            tt = 0.5*(t_hi + t_lo) + 0.5*(t_hi - t_lo)*gx
            LR, TT = np.meshgrid(lr, tt, indexing='ij')
            W = np.outer(gw, gw)*0.25*(np.log(r_hi) - np.log(r_lo))*(t_hi - t_lo)
            rr = np.exp(LR)
            zx = cx + rr*np.cos(TT); zy = cy + rr*np.sin(TT)
            if own_sign > 0:   # center = e1: other kernel is -K_beta(z)
                other = -Kb(zx, zy, beta)
            else:              # center = 0: other kernel is +K_beta(z - e1)
                other = Kb(zx - 1.0, zy, beta)
            m_other = np.sum(W*other*rr*rr)   # dz = rho^2 dlogrho dtheta
            rc = np.sqrt(r_hi*r_lo); tc = 0.5*(t_lo + t_hi)
            nodes.append((cx + rc*np.cos(tc), cy + rc*np.sin(tc)))
            masses.append(own + m_other)
            cells.append((r_lo, r_hi, t_lo, t_hi))
    # innermost disk: own mass 0, other mass ~ value*area (negligible); node at center
    nodes.append((cx, cy))
    r_in = radii[-1]
    if own_sign > 0:
        masses.append(-Kb(cx, cy, beta)*np.pi*r_in**2)
    else:
        masses.append(Kb(cx - 1.0, cy, beta)*np.pi*r_in**2)
    cells.append((0.0, r_in, 0.0, 2*np.pi))
    return np.array(nodes), np.array(masses), cells

def far_cells(center, R0, qf, Jf, ntheta, beta, ngl=6):
    """Polar cells about `center` for rho in [R0, R0 qf^Jf], whole k by Gauss-Legendre."""
    cx, cy = center
    radii = R0*qf**np.arange(Jf+1)
    thetas = 2*np.pi*np.arange(ntheta+1)/ntheta
    gx, gw = gl_nodes(ngl)
    nodes, masses, cells = [], [], []
    for j in range(Jf):
        r_lo, r_hi = radii[j], radii[j+1]
        for l in range(ntheta):
            t_lo, t_hi = thetas[l], thetas[l+1]
            lr = 0.5*(np.log(r_hi) + np.log(r_lo)) + 0.5*(np.log(r_hi) - np.log(r_lo))*gx
            tt = 0.5*(t_hi + t_lo) + 0.5*(t_hi - t_lo)*gx
            LR, TT = np.meshgrid(lr, tt, indexing='ij')
            W = np.outer(gw, gw)*0.25*(np.log(r_hi) - np.log(r_lo))*(t_hi - t_lo)
            rr = np.exp(LR)
            zx = cx + rr*np.cos(TT); zy = cy + rr*np.sin(TT)
            m = np.sum(W*k_total(zx, zy, beta)*rr*rr)
            rc = np.sqrt(r_hi*r_lo); tc = 0.5*(t_lo + t_hi)
            nodes.append((cx + rc*np.cos(tc), cy + rc*np.sin(tc)))
            masses.append(m)
            cells.append((r_lo, r_hi, t_lo, t_hi))
    return np.array(nodes), np.array(masses), cells

def leftover_cells(Rn, Rf, h, beta, nsub=8):
    """Cartesian cells of side h covering B(m,Rf) minus (B(e1,Rn) u B(0,Rn)), m = e1/2; masses by subsampling."""
    mx, my = 0.5, 0.0
    xs = np.arange(mx - Rf, mx + Rf + h, h)
    ys = np.arange(my - Rf, my + Rf + h, h)
    sx = (np.arange(nsub) + 0.5)/nsub
    SX, SY = np.meshgrid(sx, sx, indexing='ij')
    nodes, masses = [], []
    for x0 in xs:
        for y0 in ys:
            px = x0 + h*SX; py = y0 + h*SY
            inside = ((px - mx)**2 + (py - my)**2 < Rf*Rf) & ((px - 1)**2 + py**2 >= Rn*Rn) & (px**2 + py**2 >= Rn*Rn)
            if not inside.any():
                continue
            vals = np.where(inside, k_total(px, py, beta), 0.0)
            m = vals.sum()*h*h/(nsub*nsub)
            # node: centroid of the inside part
            cxn = px[inside].mean(); cyn = py[inside].mean()
            nodes.append((cxn, cyn)); masses.append(m)
    return np.array(nodes), np.array(masses)

def build(alpha, beta, Rn=0.5, q=2.0, rho_min=1e-8, ntheta_n=16, Rf=1.0, qf=2.0, rho_max=1e5, ntheta_f=24, h=0.05):
    J = int(np.ceil(np.log(Rn/rho_min)/np.log(q)))
    Jf = int(np.ceil(np.log(rho_max/Rf)/np.log(qf)))
    n1, m1, c1 = polar_cells((1.0, 0.0), Rn, q, J, ntheta_n, beta + np.pi/4, beta, +1)
    n0, m0, c0 = polar_cells((0.0, 0.0), Rn, q, J, ntheta_n, beta + np.pi/4, beta, -1)
    nf, mf, cf = far_cells((0.5, 0.0), Rf, qf, Jf, ntheta_f, beta)
    nl, ml = leftover_cells(Rn, Rf, h, beta)
    nodes = np.vstack([n0, n1, nf, nl]); masses = np.concatenate([m0, m1, mf, ml])
    labels = np.concatenate([np.zeros(len(m0), int), np.ones(len(m1), int), 2*np.ones(len(mf), int), 3*np.ones(len(ml), int)])
    info = dict(J=J, Jf=Jf, n_near0=len(m0), n_near1=len(m1), n_far=len(mf), n_left=len(ml),
                mass_total=float(masses.sum()), abs_mass=float(np.abs(masses).sum()),
                idx_origin=int(len(m0) - 1), idx_e1=int(len(m0) + len(m1) - 1))
    return nodes, masses, labels, info

def solve_lp(nodes, masses, alpha, idx_fix=0, tol=1e-9, max_add=40000, max_iter=60, verbose=True, init_pairs=None, time_limit=3000):
    N = len(nodes)
    h = highspy.Highs()
    h.setOptionValue('output_flag', False)
    h.setOptionValue('time_limit', float(time_limit))
    inf = highspy.kHighsInf
    lb = -inf*np.ones(N); ub = inf*np.ones(N)
    lb[idx_fix] = 0.0; ub[idx_fix] = 0.0
    h.addVars(N, lb, ub)
    h.changeColsCost(N, np.arange(N, dtype=np.int32), -masses.astype(np.float64))  # minimise -sum m u
    # pair bookkeeping
    added = set()
    rowpairs = []
    def add_pairs(I, J):
        rowpairs.extend(zip(I.tolist(), J.tolist()))
        # constraint u_I - u_J <= d^alpha
        d = np.sqrt(((nodes[I] - nodes[J])**2).sum(axis=1))**alpha
        n = len(I)
        starts = np.arange(0, 2*n, 2, dtype=np.int32)
        idx = np.empty(2*n, dtype=np.int32); idx[0::2] = I; idx[1::2] = J
        vals = np.empty(2*n); vals[0::2] = 1.0; vals[1::2] = -1.0
        h.addRows(n, -inf*np.ones(n), d, 2*n, starts, idx, vals)
    # initial constraints: nearest neighbours in index order and a random sample
    rng = np.random.default_rng(0)
    if init_pairs is None:
        I = np.arange(N - 1); J = I + 1
        I2 = rng.integers(0, N, 5*N); J2 = rng.integers(0, N, 5*N)
        I = np.concatenate([I, I2]); J = np.concatenate([J, J2])
        keep = I != J
        I, J = I[keep], J[keep]
    else:
        I, J = init_pairs
    for a, b in zip(I.tolist(), J.tolist()):
        added.add((a, b)); added.add((b, a))
    add_pairs(np.concatenate([I, J]), np.concatenate([J, I]))
    t0 = time.time()
    hist = []
    for it in range(max_iter):
        h.run()
        st = h.getModelStatus()
        sol = h.getSolution()
        u = np.array(sol.col_value)
        val = float(masses @ u)
        # check all pairs in chunks: violation = u_i - u_j - d_ij^alpha > tol
        viol_I, viol_J, viol_V = [], [], []
        chunk = max(1, 20_000_000 // N)
        for s in range(0, N, chunk):
            e = min(N, s + chunk)
            D = np.sqrt(((nodes[s:e, None, :] - nodes[None, :, :])**2).sum(axis=2))
            np.fill_diagonal(D[:, s:e], np.inf)
            V = (u[s:e, None] - u[None, :]) - D**alpha
            mask = V > tol
            if mask.any():
                ii, jj = np.nonzero(mask)
                viol_I.append(ii + s); viol_J.append(jj); viol_V.append(V[mask])
        if viol_I:
            vi = np.concatenate(viol_I); vj = np.concatenate(viol_J); vv = np.concatenate(viol_V)
        else:
            vi = vj = vv = np.array([])
        nviol = len(vi); maxv = float(vv.max()) if nviol else 0.0
        hist.append(dict(it=it, val=val, nviol=int(nviol), maxviol=maxv, rows=h.getNumRow(), t=time.time() - t0))
        if verbose:
            print(f"  it {it:2d} val {val:.8f} rows {h.getNumRow():8d} viol {nviol:9d} max {maxv:.2e} status {st} t {time.time()-t0:.1f}s", flush=True)
        if nviol == 0:
            break
        order = np.argsort(-vv)[:max_add]
        I = vi[order]; J = vj[order]
        new = [(a, b) for a, b in zip(I.tolist(), J.tolist()) if (a, b) not in added]
        for a, b in new:
            added.add((a, b))
        if not new:
            break
        I = np.array([a for a, b in new]); J = np.array([b for a, b in new])
        add_pairs(I, J)
    # duals: row duals give the plan
    sol = h.getSolution()
    u = np.array(sol.col_value)
    duals = np.array(sol.row_dual)
    rp = np.array(rowpairs); nz = np.abs(duals) > 1e-10
    plan = np.column_stack([rp[nz], duals[nz]]) if nz.any() else np.zeros((0,3))
    return u, float(masses @ u), hist, h, plan

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--alpha', type=float, required=True)
    ap.add_argument('--beta', type=float, default=0.0)
    ap.add_argument('--ntheta', type=int, default=16)
    ap.add_argument('--q', type=float, default=2.0)
    ap.add_argument('--rho_min', type=float, default=1e-8)
    ap.add_argument('--rho_max', type=float, default=1e5)
    ap.add_argument('--ntheta_f', type=int, default=24)
    ap.add_argument('--qf', type=float, default=2.0)
    ap.add_argument('--h', type=float, default=0.05)
    ap.add_argument('--out', type=str, default=None)
    ap.add_argument('--ident', type=float, default=0.0, help='identity term c: functional (T - c I)f(e1) - (T - c I)f(0); c=1/2 gives D_alpha = ||T_xx - I/2|| (direction beta)')
    a = ap.parse_args()
    nodes, masses, labels, info = build(a.alpha, a.beta, q=a.q, rho_min=a.rho_min, ntheta_n=a.ntheta, qf=a.qf, rho_max=a.rho_max, ntheta_f=a.ntheta_f, h=a.h)
    if a.ident != 0.0:
        masses[info['idx_e1']] -= a.ident; masses[info['idx_origin']] += a.ident
    print("nodes", len(nodes), info, flush=True)
    u, val, hist, h, plan = solve_lp(nodes, masses, a.alpha, idx_fix=info['idx_origin'])
    # analytic tail corrections (heuristic): below rho_min at both points (reflection plan), beyond rho_max (dipole bound)
    a2 = 2**(1 + a.alpha/2)/(np.pi*(a.alpha + 2))
    corr_inner = 2*a2/a.alpha*a.rho_min**a.alpha
    print(f"V_h = {val:.6f}   inner-tail correction (add) ~ {corr_inner:.3e}   u(e1) = {u[info['idx_e1']]:.6f}")
    res = dict(alpha=a.alpha, beta=a.beta, params=vars(a), info=info, V_h=val, corr_inner=corr_inner, hist=hist,
               nodes=nodes.tolist(), masses=masses.tolist(), labels=labels.tolist(), u=u.tolist(), plan=plan.tolist())
    if a.out:
        json.dump(res, open(a.out, 'w'))
