"""local_exponent.py -- lead 23:43Z items (1), (3), (4) and 23:46Z: for Q-representation states (fixed-c_l chains), print
  (1) cubic jets b, e, e/b against (a0 - 2A)/6 [(T1)], core scale ell_c = sqrt(a0/|b|);
  (3) (T2): q1 - q2 against (a0 - 4A) b/(3 a0);
  (4) the local exponent s(r) = d log|1 - q| / d log r on the y-axis (q = rho/(a0 y) = w b(sigma, pi/2)/a0) and on the x-axis
      (q = rho_y(x, 0)/a0 = w b(sigma, 0)/a0) at log-spaced radii in [1e-4, 10] and in [1e-3 ell_c, 10 ell_c];
  (5) a fit 1 - q = alpha r^2 + beta r^(d-1) on the y-axis over a radius window (default [1e-4, 1]), relative least squares.
Everything is evaluated from the spectral representation (not at the nodes).  Smooth limit: s = 2 on a range of r that does not shrink
with N.  Finite-regularity limit: s = 2 only below a transition radius r_t(N) falling with N, with an N-independent plateau d - 1 < 2 above.
usage: python3 src/local_exponent.py state.pt [state2.pt ...] [rfit=1e-4,1]"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from scipy.optimize import least_squares

def jets(S):
    q = S.mdl; beta = S.coef; kappa = 2.0 ** (2 * q.p) / S.L ** 2
    dbeta = (q.rad.DR @ beta); d0 = 2 * dbeta[0, 0].item(); d1 = beta[0, 1].item(); a0 = beta[0, 0].item()
    b = kappa * (d0 - a0 + d1); e = kappa * (d0 - a0 - d1)
    PsiC = S.flds['PsiC']; dPsi = q.rad.DL @ PsiC
    Psi1, dPsi1, dPsi2 = PsiC[0, 0].item(), dPsi[0, 0].item(), dPsi[0, 1].item()
    c = 2 * Psi1; qsum = 4 * kappa * (2 * dPsi1 - Psi1); qdif = 16 * kappa * dPsi2
    return a0, b, e, c, (qsum + qdif) / 2, (qsum - qdif) / 2

def axis_q(S, rr, th):
    out = S.ev(rr, np.full_like(rr, th))
    return out['w'] * out['b'] / S.a0            # q = rho/(a0 y) = w b / a0 (exact in the Q representation; no division by y)

def exponent(rr, f):
    lf = np.log(np.abs(f)); lr = np.log(rr)
    s = np.gradient(lf, lr)
    return s

def main():
    kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a); files = [a for a in sys.argv[1:] if '=' not in a]
    rfit = [float(v) for v in kw.get('rfit', '1e-4,1').split(',')]
    r_report = np.exp(np.linspace(np.log(1e-4), np.log(10), 12))
    rr = np.exp(np.linspace(np.log(1e-6), np.log(1e3), 1801))                     # fine log grid for the derivative
    for fn in files:
        S = qdiag.State(fn); cl = S.cl; A = 2 * cl - 1; D = cl - 1
        a0, b, e, c, q1, q2 = jets(S)
        ell = math.sqrt(abs(a0 / b)) if b != 0 else float('nan')
        T1 = e / b - (a0 - 2 * A) / 6; T2 = (q1 - q2) - (a0 - 4 * A) * b / (3 * a0)
        print(f"LOCEXP {fn}: {S.N}x{S.M} c_l={cl:.6f} L={S.L} a0={a0:.6f} a0/A={a0/A:.4f} c_l+c-1={cl+c-1:+.2e}")
        print(f"  (1) b={b:+.5g} e={e:+.5g} e/b={e/b:+.6f} (a0-2A)/6={(a0-2*A)/6:+.6f} T1 defect e/b-(a0-2A)/6={T1:+.3e} (rel to e/b {T1/(e/b):+.2e}); ell_c=sqrt(a0/|b|)={ell:.5f}")
        print(f"  (3) q1={q1:+.5g} q2={q2:+.5g} q1-q2={q1-q2:+.5g} (a0-4A)b/(3a0)={(a0-4*A)*b/(3*a0):+.5g} T2 defect={T2:+.3e} (rel to q1-q2 {T2/(q1-q2):+.2e}); Poisson q1+q2+b/3={q1+q2+b/3:+.3e}")
        qy = axis_q(S, rr, math.pi / 2); qx = axis_q(S, rr, 0.0)
        fy = 1 - qy; fx = 1 - qx; sy = exponent(rr, fy); sx = exponent(rr, fx)
        # leading coefficients: 1 - q ~ -(e/a0) y^2 on the y-axis, ~ -(b/a0) x^2 on the x-axis
        print(f"  (4) local exponent s = dlog|1-q|/dlog r (y-axis | x-axis); leading smooth prediction 1-q ~ {-e/a0:+.4g} r^2 (y), {-b/a0:+.4g} r^2 (x)")
        print(f"      {'r':>9s} {'1-q_y':>11s} {'s_y':>7s} {'1-q_x':>11s} {'s_x':>7s}")
        for r0 in r_report:
            i = np.argmin(np.abs(np.log(rr) - np.log(r0)))
            print(f"      {rr[i]:9.3e} {fy[i]:+11.4e} {sy[i]:7.4f} {fx[i]:+11.4e} {sx[i]:7.4f}")
        print(f"      ell_c-relative radii (r/ell_c = 1e-3 .. 10):")
        for fac in [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1, 3, 10]:
            r0 = fac * ell; i = np.argmin(np.abs(np.log(rr) - np.log(r0)))
            print(f"      r/ell_c={fac:7.3g} r={rr[i]:9.3e} 1-q_y={fy[i]:+11.4e} s_y={sy[i]:7.4f} 1-q_x={fx[i]:+11.4e} s_x={sx[i]:7.4f}")
        # (5) fit on the y-axis over the window
        m = (rr >= rfit[0]) & (rr <= rfit[1]); r_, f_ = rr[m], fy[m]
        def res(p):
            al, be, d = p; return (al * r_ ** 2 + be * r_ ** (d - 1) - f_) / np.abs(f_)
        best = None
        for d0 in [1.5, 2.0, 2.5, 3.5, 4.5]:
            for be0 in [0.0, 1e-3 * np.sign(f_[-1]), 1e-1 * np.sign(f_[-1])]:
                try:
                    sol = least_squares(res, [-e / a0, be0, d0], bounds=([-np.inf, -np.inf, 1.01], [np.inf, np.inf, 12.0]), max_nfev=4000)
                    if best is None or sol.cost < best.cost: best = sol
                except Exception as ex:
                    pass
        al, be, d = best.x; rel = np.sqrt(2 * best.cost / len(r_))
        # pure r^2 fit for comparison
        al2 = np.sum(f_ * r_ ** 2 / f_ ** 2) / np.sum(r_ ** 4 / f_ ** 2); rel2 = np.sqrt(np.mean(((al2 * r_ ** 2 - f_) / f_) ** 2))
        print(f"  (5) y-axis fit on [{rfit[0]:g}, {rfit[1]:g}] ({m.sum()} pts): 1-q = alpha r^2 + beta r^(d-1): alpha={al:+.5g} (smooth: -e/a0={-e/a0:+.5g}), beta={be:+.4g}, d={d:.4f}, rms rel misfit {rel:.2e};"
              f"  pure r^2: alpha={al2:+.5g}, rms rel misfit {rel2:.2e}")
        sys.stdout.flush()

if __name__ == '__main__':
    main()
