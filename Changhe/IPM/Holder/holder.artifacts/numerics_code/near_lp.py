"""Heuristic LP value of the LOCAL functional alone (own-pole kernels inside the two pole disks of radius 1/2) on the otlp near-cell discretisation,
to calibrate the full two-point LP. The reference value 2^(1-alpha) a_2(alpha)/alpha is the SUM of the two independent disk suprema (Theorem 3.1(a),
per circle); the joint local supremum equals it only at phase pi/2 (the verification work V246/V250), so reference - LP(near) is the near-discretisation deficit
plus (at other phases) a small genuine gap. Usage: python3 near_lp.py alpha beta_list [ntheta q rho_min]"""
import sys, numpy as np
from scipy.integrate import quad
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from otlp import polar_cells, solve_lp, Kb
alpha = float(sys.argv[1]); betas = [eval(s) for s in sys.argv[2].split(',')]
ntheta = int(sys.argv[3]) if len(sys.argv) > 3 else 16; q = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0; rho_min = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-8
a2 = 2/np.pi*quad(lambda t: np.sin(2*t)*(2*np.sin(t))**alpha, 0, np.pi/4)[0]; exact = 2**(1 - alpha)*a2/alpha
J = int(np.ceil(np.log(0.5/rho_min)/np.log(q)))
for beta in betas:
    # own kernel only: polar_cells gives own + other; subtract the other part by calling with the other kernel masses computed separately is
    # not available, so rebuild: own mass of a cell is exact (closed form) = own_sign*log(r_hi/r_lo)/(2pi)*(sin(2t_hi-2beta)-sin(2t_lo-2beta))/2
    tot = 0.0
    for (center, own_sign) in [((1.0, 0.0), +1), ((0.0, 0.0), -1)]:
        radii = 0.5*q**(-np.arange(J + 1)); thetas = beta + np.pi/4 + 2*np.pi*np.arange(ntheta + 1)/ntheta
        nodes, masses = [], []
        for j in range(J):
            r_hi, r_lo = radii[j], radii[j + 1]
            for l in range(ntheta):
                t_lo, t_hi = thetas[l], thetas[l + 1]
                m = own_sign*np.log(r_hi/r_lo)/(2*np.pi)*(np.sin(2*t_hi - 2*beta) - np.sin(2*t_lo - 2*beta))/2
                rc = np.sqrt(r_hi*r_lo); tc = 0.5*(t_lo + t_hi)
                nodes.append((center[0] + rc*np.cos(tc), center[1] + rc*np.sin(tc))); masses.append(m)
        nodes.append(center); masses.append(0.0)
        nodes = np.array(nodes); masses = np.array(masses)
        u, val, hist, h, plan = solve_lp(nodes, masses, alpha, idx_fix=len(nodes) - 1, verbose=False, max_add=20000, max_iter=200)
        tot += val
    r_cut = 0.5*q**(-J); inner = exact*(2*r_cut)**alpha   # omitted own-kernel part of both disks below the actual cutoff radius r_cut = 0.5 q^-J (the verification work V248)
    print(f"alpha={alpha} beta={beta:.4f}: LP(near, ntheta {ntheta}, q {q}) = {tot:.6f} (+ inner tail {inner:.2e});  exact sup = {exact:.6f};  deficit = {exact - tot - inner:.6f}", flush=True)
