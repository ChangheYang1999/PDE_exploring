"""Lead 13:54Z (ver topic 138): X norms of the scaling tangent K = rho~ - X.grad rho~, of the residual eps~ and of eps~ - X.grad eps~ of the modal
trial, with the diagnostic weight w = m^{-2} (1+u^2)^{-3/2} of the C2 Gram (||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX), split into r < 2, the P-lobe
annulus 4 <= r <= 16, and the rest. FLOATING. For f = sum_N f_N(t) sin((2N+1) theta): ||f||_X^2 = pi int e^{2t} w(t) sum_N [f_N^2 + (d_t f_N)^2 +
(2N+1)^2 f_N^2] dt. Modes from the closed-form inverse (trial_green): R, Rt = rho_modes (rho~ and d_t rho~), eps = residual_modes; d_t eps by
central differences on the t grid (spacing dt). Integration on t in [log(rmin), log(rmax)] by the trapezoid rule; the omitted tails are estimated
from the end values (integrand ~ r^2 at 0 for K, ~ 1/r at infinity).
Usage: python3 src/xnorm_K.py trial.npz nt rmin rmax out.json"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen


def main(path, nt, rmin, rmax, out):
    T = Trial(np.load(path)); G = TrialGreen(T); t0 = time.time(); G.build(); k = T.k; L = T.L
    t = np.linspace(np.log(rmin), np.log(rmax), nt); dt = t[1] - t[0]; r = np.exp(t); u = r / L
    m = u ** 3 * (1 + u ** 2) ** ((k - 3) / 2); w = m ** -2 * (1 + u ** 2) ** -1.5
    R, Rt = G.rho_modes(t); K = R - Rt                                   # K_N(t)
    Kt = np.gradient(K, dt, axis=0)                                      # d_t K (central differences)
    eps = G.residual_modes(t); epst = np.gradient(eps, dt, axis=0)      # eps_N, d_t eps_N
    F2 = eps - epst                                                      # (eps~ - X.grad eps~)_N
    F2t = np.gradient(F2, dt, axis=0)
    print("modes at %d radii: %.0fs" % (nt, time.time() - t0), flush=True)
    def dens(f, ft):
        kN = 2 * np.arange(f.shape[1]) + 1.0
        return np.pi * np.exp(2 * t) * w * ((f ** 2).sum(1) + (ft ** 2).sum(1) + ((kN ** 2)[None, :] * f ** 2).sum(1))
    regions = {"r<2": r < 2, "4<=r<=16": (r >= 4) & (r <= 16), "rest (2<=r<4 or r>16)": ~((r < 2) | ((r >= 4) & (r <= 16))), "all": np.ones_like(r, bool)}
    res = dict(trial=path, nt=nt, dt=dt, rmin=rmin, rmax=rmax, weight="m^-2 (1+u^2)^-1.5, m = u^3 (1+u^2)^((k-3)/2)", norms={})
    for name, (f, ft) in {"K = rho~ - X.grad rho~": (K, Kt), "eps~": (eps, epst), "eps~ - X.grad eps~": (F2, F2t), "rho~": (R, Rt)}.items():
        d = dens(f, ft); row = {}
        row["norm2"] = {}
        for reg, mask in regions.items():
            dd = np.where(mask, d, 0.0); row["norm2"][reg] = float(np.trapezoid(dd, t)); row[reg] = float(np.sqrt(row["norm2"][reg]))
        # tail estimates: inner integrand ~ C r^2 (so int_{-inf}^{t0} ~ d(t0)/2), outer ~ C/r (int ~ d(t1))
        row["omitted tails (estimate, norm^2)"] = [float(d[0] / 2), float(d[-1])]
        row["integrand at ends"] = [float(d[0]), float(d[-1])]
        res["norms"][name] = row
        print("%-22s " % name + "  ".join("%s %.4e" % (reg, v) for reg, v in row.items() if isinstance(v, float)) + "  tails^2 ~ %.1e / %.1e" % (d[0] / 2, d[-1]), flush=True)
    rK = res["norms"]["K = rho~ - X.grad rho~"]["all"]; rF = res["norms"]["eps~ - X.grad eps~"]["all"]
    res["ratio_||K||_X_over_||eps~-X.grad eps~||_X"] = rK / rF; print("||K||_X / ||eps~ - X.grad eps~||_X = %.4e  (a lower bound for any C with ||h||_X <= C ||L h||_X on the graph domain, ver topic 138)" % (rK / rF))
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "(%.0fs)" % (time.time() - t0))


if __name__ == "__main__":
    a = sys.argv; main(a[1], int(a[2]), float(a[3]), float(a[4]), a[5])
