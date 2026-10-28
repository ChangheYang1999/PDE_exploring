"""Heuristic LP value of the LOCAL D functional: own-pole kernels inside the two pole disks (radius 1/2) plus the identity atoms -1/2 at e1 and
+1/2 at 0 (the increment of R_1^2 = T - I/2 restricted to the local terms), over [f]_alpha <= 1; compared with the certified local D term
2^(1-alpha) A_alpha/alpha + 1/2 (projection pairing of P_R exact per circle + translation coupling of Q + atom), and the local C functional
(own kernels only) against 2^(1-alpha) a_2/alpha. Discretisation: otlp near cells with NTHETA angular cells, ratio Q, down to RHO_MIN (own masses exact
per cell). Usage: python3 locD_lp.py alpha beta_list [ntheta q rho_min]"""
import sys, numpy as np
from scipy.special import gamma
from scipy.integrate import quad
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from otlp import solve_lp
alpha = float(sys.argv[1]); betas = [eval(s) for s in sys.argv[2].split(',')]
ntheta = int(sys.argv[3]) if len(sys.argv) > 3 else 64; q = float(sys.argv[4]) if len(sys.argv) > 4 else 1.5; rho_min = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-8
a2 = 2/np.pi*quad(lambda t: np.sin(2*t)*(2*np.sin(t))**alpha, 0, np.pi/4)[0]; locC = 2**(1 - alpha)*a2/alpha
A = gamma(1 + alpha/2)/(2*np.sqrt(np.pi)*gamma(1.5 + alpha/2)); locD = 2**(1 - alpha)*A/alpha + 0.5
J = int(np.ceil(np.log(0.5/rho_min)/np.log(q)))
def near_nodes(beta):
    nodes, masses, centers = [], [], []
    for (center, own_sign) in [((1.0, 0.0), +1), ((0.0, 0.0), -1)]:
        radii = 0.5*q**(-np.arange(J + 1)); thetas = beta + np.pi/4 + 2*np.pi*np.arange(ntheta + 1)/ntheta
        for j in range(J):
            r_hi, r_lo = radii[j], radii[j + 1]
            for l in range(ntheta):
                t_lo, t_hi = thetas[l], thetas[l + 1]
                m = own_sign*np.log(r_hi/r_lo)/(2*np.pi)*(np.sin(2*t_hi - 2*beta) - np.sin(2*t_lo - 2*beta))/2
                rc = np.sqrt(r_hi*r_lo); tc = 0.5*(t_lo + t_hi)
                nodes.append((center[0] + rc*np.cos(tc), center[1] + rc*np.sin(tc))); masses.append(m)
        nodes.append(center); masses.append(0.0); centers.append(len(nodes) - 1)
    return np.array(nodes), np.array(masses), centers
print(f"alpha={alpha}: certified local C term {locC:.6f}; certified local D term {locD:.6f}; J={J} shells x {ntheta} cells per disk")
for beta in betas:
    nodes, masses, (ie1, i0) = near_nodes(beta)
    u, vC, hist, h, plan = solve_lp(nodes, masses, alpha, idx_fix=i0, verbose=False, max_add=30000, max_iter=300)
    mD = masses.copy(); mD[ie1] -= 0.5; mD[i0] += 0.5
    u, vD, histD, h, plan = solve_lp(nodes, mD, alpha, idx_fix=i0, verbose=False, max_add=30000, max_iter=300)
    r_cut = 0.5*q**(-J)                      # actual innermost radius of the grid (the verification work V248); omitted own-kernel part of BOTH disks: U (2 r_cut)^alpha
    inner = locC*(2*r_cut)**alpha
    print(f"  beta={beta:.4f} (phi={2*beta:.4f}): nodes {len(nodes)};  local C LP {vC:.6f} (+ inner {inner:.1e}; certified {locC:.6f}, difference {locC - vC - inner:+.5f});"
          f"  local D LP {vD:.6f} (certified {locD:.6f}, difference {locD - vD - inner:+.5f});  LP {len(hist)}/{len(histD)} iters {hist[-1]['t']:.0f}+{histD[-1]['t']:.0f}s", flush=True)
