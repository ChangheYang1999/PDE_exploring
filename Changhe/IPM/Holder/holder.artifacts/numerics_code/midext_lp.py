"""Heuristic (float LP, NOT certified) value of the middle + exterior functional of the lead's upper-bound proofs (FINAL_REPORT Thm 3.3-3.7):
   V_me(alpha, phi) = sup{ int_{outside B(x,1/2) u B(y,1/2)} nu_phi f : [f]_alpha <= 1 },   nu_phi(w) = K_phi(w - x) - K_phi(w - y),
in this lane's coordinates (poles e1 and 0, midpoint m = e1/2; phase phi = 2 beta with K_beta(z) = cos(2 arg z - 2 beta)/(2 pi |z|^2)).
The certified bounds write C_alpha <= 2^(1-alpha) a_2(alpha)/alpha + [middle + exterior transport bound at the worst phase]; the second bracket is
>= V_me(alpha, phi_worst) (every transport plan bounds the functional). The LP value (otlp cells: Cartesian leftover cells of side h inside B(m,1),
log-polar far cells to rho_max, plus the dipole tail estimate 2 a_3 rho_max^(alpha-1)/(1-alpha)) approximates V_me without error control.
Comparison: plan slack = certified bracket - V_me; decoupling slack = (certified C upper) - (LP value of the full two-point functional).
Usage: python3 midext_lp.py alpha beta_list [ntheta_f h rho_max C_upper_certified region(both|far|mid|farpc|mphi)]"""
import sys, json, numpy as np
from scipy.integrate import quad
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from otlp import far_cells, leftover_cells, solve_lp, Kb, gl_nodes

def cross_cells(center, other_center, R, q, J, ntheta, beta, ngl=6):
    """polar cells about `center` (radius R, J shells of ratio q, ntheta angular cells) carrying ONLY the other pole's kernel
    (the cross term -K_beta(z) on B(e1, R) for center e1, +K_beta(z - e1) on B(0, R) for center 0), Gauss-Legendre in (log rho, theta)."""
    cx, cy = center
    radii = R*q**(-np.arange(J + 1)); thetas = 2*np.pi*np.arange(ntheta + 1)/ntheta
    gx, gw = gl_nodes(ngl); nodes, masses = [], []
    for j in range(J):
        r_hi, r_lo = radii[j], radii[j + 1]
        for l in range(ntheta):
            t_lo, t_hi = thetas[l], thetas[l + 1]
            lr = 0.5*(np.log(r_hi) + np.log(r_lo)) + 0.5*(np.log(r_hi) - np.log(r_lo))*gx
            tt = 0.5*(t_hi + t_lo) + 0.5*(t_hi - t_lo)*gx
            LR, TT = np.meshgrid(lr, tt, indexing='ij'); W = np.outer(gw, gw)*0.25*(np.log(r_hi) - np.log(r_lo))*(t_hi - t_lo)
            rr = np.exp(LR); zx = cx + rr*np.cos(TT); zy = cy + rr*np.sin(TT)
            other = -Kb(zx, zy, beta) if cx == 1.0 else Kb(zx - 1.0, zy, beta)
            nodes.append((cx + np.sqrt(r_hi*r_lo)*np.cos(0.5*(t_lo + t_hi)), cy + np.sqrt(r_hi*r_lo)*np.sin(0.5*(t_lo + t_hi))))
            masses.append(np.sum(W*other*rr*rr))
    # innermost disk lumped at the centre (smooth kernel there)
    r_in = radii[-1]; nodes.append((cx, cy)); masses.append((-Kb(cx, cy, beta) if cx == 1.0 else Kb(cx - 1.0, cy, beta))*np.pi*r_in**2)
    return np.array(nodes), np.array(masses)

def a_n(n, alpha):
    return n/np.pi*quad(lambda t: np.sin(n*t)*(2*np.sin(t))**alpha, 0, np.pi/(2*n))[0]

if __name__ == '__main__':
    alpha = float(sys.argv[1]); betas = [eval(s) for s in sys.argv[2].split(',')]
    ntheta_f = int(sys.argv[3]) if len(sys.argv) > 3 else 48; h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.04
    rho_max = float(sys.argv[5]) if len(sys.argv) > 5 else 1e6; Cup = float(sys.argv[6]) if len(sys.argv) > 6 else None
    region = sys.argv[7] if len(sys.argv) > 7 else 'both'      # 'both' = middle + exterior; 'far' = exterior |w - m| >= 1 only; 'mid' = middle region E only
    qf = 1.5; Jf = int(np.ceil(np.log(rho_max)/np.log(qf)))
    a2 = a_n(2, alpha); a3 = a_n(3, alpha); local = 2**(1 - alpha)*a2/alpha
    tail = 2*a3/(1 - alpha)*(qf**Jf)**(alpha - 1)
    print(f"alpha={alpha}: local term 2^(1-alpha) a_2/alpha = {local:.6f}; certified middle+exterior bracket = {Cup - local if Cup else float('nan'):.6f} (C upper {Cup}); far tail estimate beyond rho={qf**Jf:.1e}: {tail:.4f}", flush=True)
    out = []
    for beta in betas:
        nf, mf, cf = far_cells((0.5, 0.0), 1.0, qf, Jf, ntheta_f, beta)
        nl, ml = leftover_cells(0.5, 1.0, h, beta)
        if region in ('far', 'farpc'): nl, ml = nl[:0], ml[:0]
        if region == 'mid': nf, mf = nf[:0], mf[:0]
        nodes = np.vstack([nf, nl]); masses = np.concatenate([mf, ml])
        if region == 'mphi':
            # the whole remaining density m_phi of Theorem 3.3: cross kernels inside the two pole disks (radius 1/2) + middle + exterior
            n1, m1 = cross_cells((1.0, 0.0), (0.0, 0.0), 0.5, 1.5, 12, 32, beta)
            n0, m0 = cross_cells((0.0, 0.0), (1.0, 0.0), 0.5, 1.5, 12, 32, beta)
            nodes = np.vstack([nodes, n1, n0]); masses = np.concatenate([masses, m1, m0])
        if region == 'mid': tail = 0.0
        if region == 'farpc':
            # per-circle restriction: couplings only within the same radial shell (Jf shells of ntheta_f cells each, in far_cells order);
            # the per-shell LP values summed = the best bound obtainable by per-circle plans on this discretisation
            val = 0.0; hist = [dict(t=0.0, nviol=0)]
            for j in range(Jf):
                sl = slice(j*ntheta_f, (j + 1)*ntheta_f)
                mj = masses[sl] - masses[sl].mean()        # each shell has zero mass up to quadrature error; remove it (per-circle functional)
                uj, vj, hj, _, _ = solve_lp(nodes[sl], mj, alpha, idx_fix=0, verbose=False, max_add=5000, max_iter=100)
                val += vj; hist[0]['t'] += hj[-1]['t']
        else:
            u, val, hist, hs, plan = solve_lp(nodes, masses, alpha, idx_fix=0, verbose=False, max_add=30000, max_iter=300)
        print(f"  [{region}] beta={beta:.4f} (phi={2*beta:.4f}): nodes {len(nodes)} (far {len(mf)}, leftover {len(ml)}), total mass {masses.sum():+.3e}, |mass| {np.abs(masses).sum():.4f};"
              f"  V_me(LP) = {val:.6f}  + tail {tail:.4f} = {val + tail:.6f}"
              + (f";  plan slack vs certified bracket = {Cup - local - val - tail:+.4f}" if Cup else "")
              + f";  LP {len(hist)} iters, {hist[-1]['t']:.1f}s, viol {hist[-1]['nviol']}", flush=True)
        out.append(dict(alpha=alpha, beta=beta, phi=2*beta, region=region, nodes=int(len(nodes)), V_me=val, tail=tail, local=local, C_upper=Cup, hist=hist))
    json.dump(out, open(f"midext_a{alpha}_nt{ntheta_f}_h{h}_{region}.json", 'w'))
