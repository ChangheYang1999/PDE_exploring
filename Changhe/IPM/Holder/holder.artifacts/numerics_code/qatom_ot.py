"""Heuristic (float LP, NOT certified) transport cost of the 'Q + atom' term of the lead's D upper bounds (FINAL_REPORT Theorems 3.2/3.3):
   R_1^2 = P_R + H_R - (Q_R + (1/2 - kappa) I),  kappa = 1/pi,  R = h/2 = 1/2 for the poles x = (1/2, 0), y = (-1/2, 0).
The positive measure mu = (1/2 - 1/pi) delta_pole + Q has mass 1/2; Q has density sin(2t)/(2 pi) dt dr/r on the four negative half-lobes of
cos(2 theta - phi) (t = angle to the adjacent zero ray, 0 < t < pi/4), r in [R cos 2t, R].  The term costs
   |int f d(mu_x - mu_y)| <= W_alpha(mu_x, mu_y) [f]_alpha,  W = min over couplings of int |p - q|^alpha dpi  (Kantorovich-Rubinstein),
and the translation coupling gives W <= 1/2 h^alpha = 1/2 (the '+1/2' in the D bounds). This script discretises mu into atoms (midpoint cells
in t and log r; cells with r < rmin lumped into the pole atom) and solves the dual LP  max sum m_i u_i  s.t. |u_i - u_j| <= |x_i - x_j|^alpha
(otlp.solve_lp, constraint generation, HiGHS). The LP value is the exact W of the discretised measures; the discretisation error is not
controlled (heuristic). Usage: python3 qatom_ot.py alpha phi_list [nt ns rmin]"""
import sys, json, numpy as np
from scipy.integrate import quad
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from otlp import solve_lp
EXACT = True   # exact per-t-cell masses (quad of sin 2t log(1/cos 2t) over the cell, split evenly over the ns log-radius cells of the midpoint t);
               # the earlier midpoint rule (EXACT = False) misses mass at the endpoint log singularity t -> pi/4 (external-review referee, external-review/lpdiag)

def q_atoms(pole, phi, nt=20, ns=8, R=0.5, rmin=1e-3):
    """returns positions (n,2) and masses of the discretised mu (pole atom first)"""
    pos = [np.array(pole, float)]; mass = [0.5 - 1/np.pi]
    lumped = 0.0
    tt = (np.arange(nt) + 0.5)*(np.pi/4)/nt; dt = (np.pi/4)/nt
    rays = [(phi/2 + np.pi/4, +1), (phi/2 + 3*np.pi/4, -1), (phi/2 + 5*np.pi/4, +1), (phi/2 + 7*np.pi/4, -1)]
    for t in tt:
        L = np.log(1/np.cos(2*t)); ds = L/ns
        ss = np.log(R*np.cos(2*t)) + (np.arange(ns) + 0.5)*ds
        if EXACT:
            Mi = quad(lambda u: np.sin(2*u)*np.log(1/np.cos(2*u)), t - dt/2, t + dt/2, limit=200)[0]/(2*np.pi)
            m = Mi/ns
        else:
            m = np.sin(2*t)/(2*np.pi)*dt*ds
        for (th0, sg) in rays:
            th = th0 + sg*t
            for s in ss:
                r = np.exp(s)
                if r < rmin:
                    lumped += m; mass[0] += m
                else:
                    pos.append(np.array(pole) + r*np.array([np.cos(th), np.sin(th)])); mass.append(m)
    return np.array(pos), np.array(mass), lumped

if __name__ == '__main__':
    alpha = float(sys.argv[1]); phis = [eval(s) for s in sys.argv[2].split(',')]
    nt = int(sys.argv[3]) if len(sys.argv) > 3 else 20; ns = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    rmin = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-3
    out = []
    for phi in phis:
        px, mx, lx = q_atoms((0.5, 0.0), phi, nt, ns, rmin=rmin)
        py, my, ly = q_atoms((-0.5, 0.0), phi, nt, ns, rmin=rmin)
        nodes = np.vstack([px, py]); masses = np.concatenate([mx, -my])
        tot = mx.sum()
        u, val, hist, h, plan = solve_lp(nodes, masses, alpha, idx_fix=0, verbose=False, max_add=20000, max_iter=200)
        # translation coupling cost of the discretised measure = tot * 1^alpha = tot
        print(f"alpha={alpha} phi={phi:.4f}: atoms/measure {len(mx)} (Q mass discretised {tot - 0.5 + 1/np.pi:.6f} vs 1/pi {1/np.pi:.6f}, lumped {lx:.2e});"
              f"  W_LP = {val:.6f}  translation cost = {tot:.6f}  gain = {tot - val:.6f}  (scaled to mass 1/2: W = {val*0.5/tot:.6f}, gain {0.5 - val*0.5/tot:.6f});"
              f"  LP iters {len(hist)}, {hist[-1]['t']:.1f}s, final viol {hist[-1]['nviol']}", flush=True)
        out.append(dict(alpha=alpha, phi=phi, nt=nt, ns=ns, rmin=rmin, n_atoms=int(len(mx)), mass=float(tot), W=val, gain=float(tot - val), hist=hist))
    json.dump(out, open(f"qatom_a{alpha}_nt{nt}_ns{ns}{'_exact' if EXACT else ''}.json", 'w'))
