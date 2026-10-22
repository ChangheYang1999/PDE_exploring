"""Residual of the explicit modal trial (float64): eps_N(t) modes via the closed-form Green inverse (trial_green),
Wiener norm W(t) = sum_N |eps_N(t)|, pointwise sup over theta by dense sampling, comparison with X3's residual
(x3.py + inverse.py) at the same radii, and the normalizations N_f, N_v of the prompt (sampled).
Usage: python3 trial_resid.py trial.npz Nt_eval out.json
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen


def main(path, nt_eval, out):
    T = Trial(np.load(path)); G = TrialGreen(T)
    t0 = time.time(); G.build(); print("build %.1fs, c = %.12f, c_l = 1/k = %.12f, 3c_l-1-c = %.3e" % (time.time() - t0, G.c, G.c_l, 3 * G.c_l - 1 - G.c), flush=True)
    L = T.L
    # evaluation radii: log-uniform, dense in the core
    t = np.concatenate([np.linspace(np.log(1e-4 * L), np.log(1e-3 * L), 40), np.linspace(np.log(1e-3 * L), np.log(500.0), nt_eval),
                        np.linspace(np.log(500.0), np.log(1e6 * L), 400)])
    t = np.unique(t); r = np.exp(t)
    t1 = time.time(); eps = G.residual_modes(t); print("residual modes at %d radii: %.1fs" % (len(t), time.time() - t1), flush=True)
    N = np.arange(eps.shape[1]); th = np.linspace(0, np.pi / 2, 2049)
    S = np.sin((2 * N[:, None] + 1) * th[None, :])
    E = eps @ S                                  # eps(r, theta) sampled
    W = np.abs(eps).sum(1); sup = np.abs(E).max(1)
    # X3 fields at the same radii for the normalizations and comparison of the trial density with X3
    from x3 import X3
    X = X3(); F = X.rho(r, th)
    rho_x3 = F["rho"]
    # trial density on the grid: rho~ = e^{3t} sum_j R_j sin((2j+1) th)
    R, Rt = G.rho_modes(t); Sj = np.sin((2 * np.arange(R.shape[1])[:, None] + 1) * th[None, :])
    rho_tr = R @ Sj
    drho = np.abs(rho_tr - rho_x3).max(1) / np.abs(rho_x3).max(1)
    # normalizations (sampled): N_v = |rho| + |X.grad rho| + |U.grad rho|; use X.grad rho = Rt @ S and U.grad rho = eps - c_l X.grad rho + rho
    Xg = Rt @ Sj; Ug = E - G.c_l * Xg + rho_tr
    Nv = np.abs(rho_tr) + np.abs(Xg) + np.abs(Ug)
    with np.errstate(invalid="ignore", divide="ignore"):
        qv = np.where(Nv > 0, np.abs(E) / Nv, 0.0)
    qv[:, th >= np.pi / 2 - 0.006] = 0.0; qv[:, 0] = 0.0          # axis columns excluded (0/0), as in the published 'cut'
    rows = []
    for lo, hi, name in [(0, 0.1, "r<=0.1"), (0.1, 2, "0.1<=r<=2"), (2, 10, "2<=r<=10"), (10, 100, "10<=r<=100"), (100, 1000, "100<=r<=1000"),
                         (1000, 1000 * L, "1000<=r<=1000L"), (1000 * L, 1e9, "r>1000L")]:
        m = (r >= lo) & (r <= hi)
        if not m.any(): continue
        i = np.argmax(sup[m]); j = np.argmax(np.where(m, qv.max(1), -1))
        rows.append(dict(region=name, sup_abs=float(sup[m].max()), wiener_max=float(W[m].max()), wiener_over_sup_max=float((W[m] / np.maximum(sup[m], 1e-300)).max()),
                         Nv_max=float(qv[m].max()), rho_dev_max=float(drho[m].max()), r_at_sup=float(r[m][i])))
        print("  %-16s sup|eps| %.3e  Wiener max %.3e  (W/sup max %.1f)  N_v max %.3e  |rho~-rho_X3|/|rho_X3| max %.1e  @r=%.4g" % (
            name, rows[-1]["sup_abs"], rows[-1]["wiener_max"], rows[-1]["wiener_over_sup_max"], rows[-1]["Nv_max"], rows[-1]["rho_dev_max"], rows[-1]["r_at_sup"]))
    json.dump(dict(path=path, c=G.c, c_l=G.c_l, n_radii=len(t), rows=rows), open(out, "w"), indent=1)
    np.savez_compressed(out.replace(".json", "_modes.npz"), t=t, eps=eps)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
