"""Crossing-cell certificate for (H2') (verifier objection 21:34Z, notes/flow_crossing_gap_20261020.md): on every radial sub-cell that
intersects the root bracket of x_*, certify w'(x) = d_x V_1(x, 0) > 0 on the WHOLE cell (so V_1(x, 0) has exactly one zero there) and the
signs of V_1(x, 0) at the cell ends. Uses the axis Taylor models of cert_scalars2.axis_tms: F = x V_1, dF/dt = x V_1 + x dV_1/dt, x^2;
w' = (dF/dt - F)/x^2; two-sided Bernstein ranges over the cell (K sub-intervals). Root bracket imported with outward endpoints.
Usage: python3 cert_axis_cell.py data/cert_green.npz trial.npz runs/scalars_full.json out.json
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from midrad import MR, succ, U
from cert_resid import Certifier, TMArr
from cert_scalars2 import axis_tms, tm_eval
from cert_flow import bern_range, pred

def main(green, trial, scalars, out):
    C = Certifier(green, trial, Q=12); S = json.load(open(scalars))
    xs_lo = float(np.nextafter(S["x_star_mid"] - S["x_star_rad"], -np.inf)); xs_hi = float(np.nextafter(S["x_star_mid"] + S["x_star_rad"], np.inf))
    tb = C.tb; res = dict(x_star_bracket=[xs_lo, xs_hi], cells=[])
    for ci in range(C.nc):
        r_lo = float(pred(C.e_ta.m[ci] - C.e_ta.r[ci])); h_up = (tb[ci + 1] - tb[ci]).mag(); r_hi = float(succ((C.e_ta.m[ci] + C.e_ta.r[ci]) * succ(1 + h_up + h_up * h_up)))
        if r_hi < xs_lo or r_lo > xs_hi: continue
        tm = axis_tms(C, ci); Q = C.Q; hp = C.mr_powers(h_up, Q)
        num = tm["xdV1"] - tm["xV1"]                                   # x^2 w'  (as TM row)
        # two-sided ranges over [0, h] with K = 8 sub-intervals (re-centred Bernstein)
        from math import comb as _comb
        def rng(tmrow, K=8):
            coef = tmrow.c; rem = float(tmrow.r[0]); hk = succ(h_up / K); hkP = C.mr_powers(hk, Q)
            lo_ = np.inf; hi_ = -np.inf
            for kk in range(K):
                a = kk * hk; apow = [MR.exact(1.0)]
                for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
                cm = np.zeros_like(coef.m); cr = np.zeros_like(coef.r)
                for j in range(Q + 1):
                    acc = MR(np.zeros(1), np.zeros(1))
                    for i in range(j, Q + 1): acc = acc + coef[..., i] * MR.exact(float(_comb(i, j))) * apow[i - j]
                    cm[:, j] = acc.m; cr[:, j] = acc.r
                l_, h_ = bern_range(MR(cm, cr), hkP, C.Bern); lo_ = min(lo_, float(l_[0])); hi_ = max(hi_, float(h_[0]))
            return pred(lo_ - rem), succ(hi_ + rem)
        num_lo, num_hi = rng(num); x2_lo, x2_hi = rng(tm["x2"])
        wp_lo = pred(num_lo / x2_hi) if num_lo > 0 else pred(num_lo / x2_lo)       # lower bound of w' = num/x^2 (x^2 > 0)
        F_left = tm_eval(tm["xV1"], MR.exact(np.array([0.0]))); F_right = tm_eval(tm["xV1"], MR(np.array([h_up]), np.array([succ(U * h_up)])))
        cell = dict(ci=ci, r_lo=r_lo, r_hi=r_hi, x2wprime_range=[num_lo, num_hi], x2_range=[x2_lo, x2_hi], wprime_lower=wp_lo,
                    xV1_left=[float(F_left.lower()[0]), float(F_left.upper()[0])], xV1_right=[float(F_right.lower()[0]), float(F_right.upper()[0])],
                    unique_zero=bool(wp_lo > 0 and F_left.upper()[0] < 0 and F_right.lower()[0] > 0))
        res["cells"].append(cell)
        print("cell %d r in [%.9f, %.9f]: x^2 w' in [%.6f, %.6f], w' >= %.6f; x V_1 at the ends: left %s, right %s; unique zero certified: %s" % (
            ci, r_lo, r_hi, num_lo, num_hi, wp_lo, cell["xV1_left"], cell["xV1_right"], cell["unique_zero"]))
    res["all_certified"] = all(c["unique_zero"] for c in res["cells"]) and len(res["cells"]) > 0
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "all certified:", res["all_certified"])

if __name__ == "__main__":
    main(*sys.argv[1:5])
