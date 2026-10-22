"""Floating-point (evidence only) Sobolev norms of the trial residual eps~ on regions near the source point P = (x_*, 0):
H^k seminorms |eps|_k^2 = sum_{|alpha| = k} ||D^alpha eps||^2_{L^2(region)}, k = 0..K, and sup|D^alpha eps|, from the analytic
derivative jets (src/trial_jets.py) on a polar (t = log r, theta) grid, trapezoid quadrature, both half-planes by symmetry.
Regions (each a mask on the grid): discs |X - P| < rad, dyadic annuli 2^{-j-1} <= |X - P| <= 2^{-j}, thin annulus |r - x_*| < w
with theta in [th_lo, th_hi], a 'lobe' disc centred elsewhere, and the full annulus of the grid.
Usage: python3 pdisc_norms.py trial.npz grid_name out.json      (grid_name in A, B, C, D; see GRIDS)
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets

XS = 8.600063805157177; K = 4
GRIDS = {
    # name: (t_lo, t_hi, dt, th_lo, th_hi, dth, regions)
    "A": (np.log(XS - 0.52), np.log(XS + 0.52), 1e-5, 0.0, 0.0625, 1e-4,
          [("disc0.5", "disc", 0.5), ("disc0.25", "disc", 0.25), ("disc0.1", "disc", 0.1)] + [("ann%d" % j, "ann", j) for j in range(2, 7)]),
    "B": (np.log(XS - 0.0085), np.log(XS + 0.0085), 2e-7, 0.0, 0.00098, 2e-6,
          [("ann%d" % j, "ann", j) for j in range(7, 11)] + [("disc0.004", "disc", 0.004)]),
    "C": (np.log(XS - 2.17), np.log(XS + 2.17), 2e-5, 0.0, 0.2600, 2.5e-4,
          [("discQ", "disc", XS / 4), ("disc1", "disc", 1.0), ("disc0.5", "disc", 0.5)]),
    "D": (np.log(XS - 0.62), np.log(XS + 0.62), 4e-5, 0.0, np.pi / 2, 5e-4,
          [("thin0.01_th>0.2", "thin", (0.01, 0.2, np.pi / 2)), ("thin0.01_all", "thin", (0.01, 0.0, np.pi / 2)),
           ("lobe0.4", "lobe", (8.79145 * np.cos(0.2878), 8.79145 * np.sin(0.2878), 0.4)), ("annulus_right_half", "all", None),
           ("annulus_th<0.1", "thin", (0.62, 0.0, 0.1)), ("annulus_th>0.1", "thin", (0.62, 0.1, np.pi / 2))]),
}


def masks_for(regions, t, th):
    r = np.exp(t)[:, None]; TH = th[None, :]
    x = r * np.cos(TH); y = r * np.sin(TH); d = np.hypot(x - XS, y)
    out = {}
    for name, kind, par in regions:
        if kind == "disc": out[name] = d < par
        elif kind == "ann": out[name] = (d >= 2.0 ** (-par - 1)) & (d <= 2.0 ** (-par))
        elif kind == "thin":
            w, lo, hi = par; out[name] = (np.abs(r - XS) < w) & (TH >= lo) & (TH <= hi)
        elif kind == "lobe":
            cx, cy, rad = par; out[name] = np.hypot(x - cx, y - cy) < rad
        elif kind == "all": out[name] = np.ones_like(d, bool)
    return out


def main(path, gname, out):
    tlo, thi, dt, thlo, thhi, dth, regions = GRIDS[gname]
    T = Trial(np.load(path)); G = TrialGreen(T); G.build(); J = TrialJets(G, K=K)
    t = np.arange(tlo, thi + 0.5 * dt, dt); th = np.arange(thlo, thhi + 0.5 * dth, dth)
    print("grid %s: %d radii x %d angles" % (gname, len(t), len(th)), flush=True)
    alphas = [(a, b) for k in range(K + 1) for a in range(k + 1) for b in [k - a]]
    acc = {name: {"int": {str(al): 0.0 for al in alphas}, "sup": {str(al): 0.0 for al in alphas}, "area": 0.0} for name, _, _ in regions}
    # radial profiles (theta-max of |D^alpha eps| per radius) for the full grid, for inspection
    prof = {str(al): np.zeros(len(t)) for al in alphas}
    # trapezoid weights
    wth = np.full(len(th), dth); wth[0] *= 0.5; wth[-1] *= 0.5
    wt = np.full(len(t), dt); wt[0] *= 0.5; wt[-1] *= 0.5
    chunk = 400; t0 = time.time()
    for i0 in range(0, len(t), chunk):
        sl = slice(i0, min(i0 + chunk, len(t))); tc = t[sl]
        E, RHO, PSI = J.eps_jets(tc, th)
        D = TrialJets.polar_to_cart(E, tc, th, K)
        area_w = (np.exp(2 * tc) * wt[sl])[:, None] * wth[None, :] * 2.0          # r dr dtheta = e^{2t} dt dtheta ; both half planes
        M = masks_for(regions, tc, th)
        for name in M:
            m = M[name]
            if not m.any(): continue
            acc[name]["area"] += float((area_w * m).sum())
            for al in alphas:
                v = D[al]
                acc[name]["int"][str(al)] += float((v * v * area_w * m).sum())
                acc[name]["sup"][str(al)] = max(acc[name]["sup"][str(al)], float(np.abs(v[m]).max()))
        for al in alphas:
            prof[str(al)][sl] = np.abs(D[al]).max(1)
        if (i0 // chunk) % 5 == 0:
            print("  chunk %d/%d (%.0fs)" % (i0 // chunk, (len(t) + chunk - 1) // chunk, time.time() - t0), flush=True)
    # summaries: seminorms and full norms
    res = {"grid": gname, "t_range": [float(tlo), float(thi)], "dt": dt, "theta_range": [float(thlo), float(thhi)], "dth": dth, "K": K, "regions": {}}
    for name, _, _ in regions:
        a = acc[name]; semi = {}
        for k in range(K + 1):
            semi[k] = np.sqrt(sum(a["int"][str(al)] for al in alphas if sum(al) == k))
        full = {k: float(np.sqrt(sum(semi[j] ** 2 for j in range(k + 1)))) for k in range(K + 1)}
        from math import comb as _comb
        semi_w = {k: float(np.sqrt(sum(_comb(k, al[0]) * a["int"][str(al)] for al in alphas if sum(al) == k))) for k in range(K + 1)}   # Fourier-side |.|_{dot H^k}: weights binom(k, a)
        full_w = {k: float(np.sqrt(sum(_comb(k, j) * semi_w[j] ** 2 for j in range(k + 1)))) for k in range(K + 1)}                      # ||f||_{H^k}^2 = sum_j binom(k,j) |f|_{dot H^j}^2
        supk = {k: max(a["sup"][str(al)] for al in alphas if sum(al) == k) for k in range(K + 1)}
        res["regions"][name] = dict(area=a["area"], seminorm={str(k): float(semi[k]) for k in semi}, Hk_norm={str(k): full[k] for k in full},
                                    seminorm_multinomial={str(k): semi_w[k] for k in semi_w}, Hk_norm_fourier_convention={str(k): full_w[k] for k in full_w},
                                    note="regions use the theta in [0, pi/2] grid doubled by y-symmetry: discs centred on the positive x-axis are complete; 'thin'/'all' regions are the RIGHT half-plane parts only",
                                    sup_order={str(k): float(supk[k]) for k in supk}, per_alpha_L2={al: float(np.sqrt(a["int"][al])) for al in a["int"]},
                                    per_alpha_sup=a["sup"])
        print("%-18s area %.4g | seminorms |eps|_k: %s | sup_k: %s" % (name, a["area"], " ".join("%.3e" % semi[k] for k in range(K + 1)),
                                                                        " ".join("%.3e" % supk[k] for k in range(K + 1))), flush=True)
    json.dump(res, open(out, "w"), indent=1)
    np.savez_compressed(out.replace(".json", "_profile.npz"), t=t, **{"D" + al.replace(" ", "").replace(",", "_").strip("()"): prof[al] for al in prof})
    print("done %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
