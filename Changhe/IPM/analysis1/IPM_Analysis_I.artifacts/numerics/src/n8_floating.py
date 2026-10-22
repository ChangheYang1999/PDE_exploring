"""N8 (lead 00:06Z), FLOATING (evidence only): derivative bounds of the trial velocity V = c_l X + grad^perp psi~ and of rho~ on the balls
B_{3 delta}(P), P = (x_*, 0), delta in {0.0165, 0.05, 0.1, 0.2}:
  M_V   = sup ||D^2 V||_F,     ||D^j V||_F^2   = sum_i sum_{a+b=j} C(j,a) (d_x^a d_y^b V_i)^2   (Frobenius over all index tuples),
  M_rho = sup ||D^2 rho~||_F,  ||D^j rho~||_F^2 = sum_{a+b=j} C(j,a) (d_x^a d_y^b rho~)^2,
  sup ||D^j V||_F (j = 3, 4), sup ||D^j rho~||_F (j = 3, 4, 5), and C_V = 41.7 M_V + 3 M_rho against kappa/(2 delta) = 1.687/delta.
Also the max-entry norms (largest |d^alpha f|) for reference.
All derivatives analytic from the modal representation (src/trial_jets.py: psi (t, theta)-jets to order 5 via the Green ODEs; rho jets to
order 5), converted to Cartesian derivatives by TrialJets.polar_to_cart; sampled on a polar grid (dt, dth) covering the ball;
sup over the grid points inside the ball (sampled supremum, no remainder: floating evidence).
V_1 = c_l x - psi_y, V_2 = c_l y + psi_x  =>  d^alpha V_1 = -d^alpha psi_y, d^alpha V_2 = d^alpha psi_x for |alpha| >= 2.
Usage: python3 src/n8_floating.py trial.npz out.json [dt] [dth]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets

XS = 8.600063805157177
DELTAS = [0.0165, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2]
import os
if os.environ.get('N8_DELTAS'): DELTAS = [float(x) for x in os.environ['N8_DELTAS'].split(',')]


def main(path, out, dt=1e-4, dth=1e-4):
    T = Trial(np.load(path)); G = TrialGreen(T); G.build(); J = TrialJets(G, K=4)
    rmax = 3 * max(DELTAS)
    tlo, thi = np.log(XS - rmax), np.log(XS + rmax); thhi = np.arcsin(rmax / XS) * 1.001
    t = np.arange(tlo, thi + 0.5 * dt, dt); th = np.arange(0.0, thhi + 0.5 * dth, dth)
    print("grid: %d radii x %d angles, dt %.1e dth %.1e; c_l = %.15g" % (len(t), len(th), dt, dth, G.c_l), flush=True)
    # accumulators per delta: sup of Frobenius norms and max-entry norms
    keys = ["V2", "V3", "V4", "rho2", "rho3", "rho4", "rho5", "V1", "rho1", "rho0", "V0"]
    sup = {d: {k: 0.0 for k in keys} for d in DELTAS}
    supmax = {d: {k: 0.0 for k in keys} for d in DELTAS}
    argmax = {d: {} for d in DELTAS}
    npts = {d: 0 for d in DELTAS}
    chunk = 300; t0 = time.time()
    for i0 in range(0, len(t), chunk):
        sl = slice(i0, min(i0 + chunk, len(t))); tc = t[sl]
        E, RHO, PSI = J.eps_jets(tc, th)                     # RHO, PSI: (t,theta)-jets to order 5
        Dr = TrialJets.polar_to_cart(RHO, tc, th, 5)         # d_x^a d_y^b rho, a + b <= 5
        Dp = TrialJets.polar_to_cart(PSI, tc, th, 5)         # d_x^a d_y^b psi, a + b <= 5
        r = np.exp(tc)[:, None]; x = r * np.cos(th)[None, :]; y = r * np.sin(th)[None, :]
        dist = np.hypot(x - XS, y)
        fro = {}; mx = {}
        for j in range(0, 6):
            acc = np.zeros_like(dist); m = np.zeros_like(dist)
            for a in range(j + 1):
                b = j - a; v = Dr[(a, b)]
                acc += comb(j, a) * v * v; m = np.maximum(m, np.abs(v))
            fro["rho%d" % j] = np.sqrt(acc); mx["rho%d" % j] = m
        for j in range(0, 5):
            acc = np.zeros_like(dist); m = np.zeros_like(dist)
            for a in range(j + 1):
                b = j - a
                v1 = -Dp[(a, b + 1)]; v2 = Dp[(a + 1, b)]
                if j == 0: v1 = v1 + G.c_l * x; v2 = v2 + G.c_l * y
                if j == 1:
                    if a == 1: v1 = v1 + G.c_l
                    if b == 1: v2 = v2 + G.c_l
                acc += comb(j, a) * (v1 * v1 + v2 * v2); m = np.maximum(m, np.maximum(np.abs(v1), np.abs(v2)))
            fro["V%d" % j] = np.sqrt(acc); mx["V%d" % j] = m
        for d in DELTAS:
            mask = dist <= 3 * d
            if not mask.any(): continue
            npts[d] += int(mask.sum())
            for k in keys:
                v = fro[k][mask]; i = int(np.argmax(v))
                if v[i] > sup[d][k]:
                    sup[d][k] = float(v[i])
                    argmax[d][k] = [float(x[mask][i]), float(y[mask][i])]
                supmax[d][k] = max(supmax[d][k], float(mx[k][mask].max()))
        if (i0 // chunk) % 4 == 0:
            print("  chunk %d/%d (%.0fs)" % (i0 // chunk, (len(t) + chunk - 1) // chunk, time.time() - t0), flush=True)
    res = {"trial": path, "dt": dt, "dth": dth, "x_star": XS, "c_l": float(G.c_l), "note": "FLOATING sampled suprema on the polar grid points inside B_{3 delta}(P); Frobenius norms over all index tuples (multinomial weights); 'max_entry' = largest |d^alpha f| over the multi-indices of that order", "deltas": {}}
    print("\n%-8s %6s %12s %12s %12s %12s | %12s %12s %12s %12s | %10s %10s" % ("delta", "npts", "M_V=|D2V|", "|D3V|", "|D4V|", "M_rho=|D2rho|", "|D3rho|", "|D4rho|", "|D5rho|", "|D1V|", "C_V", "1.687/d"))
    for d in DELTAS:
        CV = 41.7 * sup[d]["V2"] + 3 * sup[d]["rho2"]
        res["deltas"][str(d)] = {"radius_3delta": 3 * d, "npts": npts[d], "frobenius_sup": sup[d], "max_entry_sup": supmax[d], "argmax_xy": argmax[d],
                                 "C_V": CV, "kappa_over_2delta": 1.687 / d, "C_V_ok": bool(CV <= 1.687 / d)}
        print("%-8g %6d %12.5g %12.5g %12.5g %12.5g | %12.5g %12.5g %12.5g %12.5g | %10.4g %10.4g %s" % (d, npts[d], sup[d]["V2"], sup[d]["V3"], sup[d]["V4"], sup[d]["rho2"], sup[d]["rho3"], sup[d]["rho4"], sup[d]["rho5"], sup[d]["V1"], CV, 1.687 / d, "OK" if CV <= 1.687 / d else "FAIL"))
    json.dump(res, open(out, "w"), indent=1)
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4, float(sys.argv[4]) if len(sys.argv) > 4 else 1e-4)
