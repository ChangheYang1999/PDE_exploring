#!/usr/bin/env python
"""Lead 2026-10-25T18:4xZ item (3): for the selected point with the largest grad P change under source re-sampling, give its radius in R0 units and the
local |grad P| relative to the local RMS of the five momentum terms on that shell (export samples: U, DU, grad P on the exchange grid). The five terms
(SPEC 7.2): T1 = (1 - c_l) U, T2 = c_l (y . grad) U, T3 = -omega ((J y) . grad) U, T4 = (U . grad) U, T5 = omega J U; grad P is the sixth; their sum is R_u.
DU_grid[.., m, i] = d_m U_i is checked by trace(DU) = div U = 0 and by the momentum residual. Usage: gradp_point_context.py <candidate id> <resolution json>"""
import sys, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
cid, rj = sys.argv[1], sys.argv[2]
smp = np.load(os.path.join(ROOT, "candidates", cid, "samples.npz")); meta = json.load(open(os.path.join(ROOT, "candidates", cid, "meta.json")))
R = json.load(open(rj)); c_l = float(meta["c_l"]); om = float(meta["omega"]); R0 = float(meta["R0"])
radii = smp["radii"]; y = smp["y_grid"]; U = smp["U_grid"]; DU = smp["DU_grid"]; gP = smp["gradP_grid"]; nth, nph = len(smp["theta"]), len(smp["phi"])
# convention check: divergence and momentum residual with DU[m, i] = d_m U_i
div = np.einsum('...mm->...', DU)
def terms(DUc):
    T1 = (1 - c_l) * U
    T2 = c_l * np.einsum('...mi,...m->...i', DUc, y)
    Jy = np.stack([-y[..., 1], y[..., 0], np.zeros_like(y[..., 2])], -1)
    T3 = -om * np.einsum('...mi,...m->...i', DUc, Jy)
    T4 = np.einsum('...mi,...m->...i', DUc, U)
    T5 = om * np.stack([-U[..., 1], U[..., 0], np.zeros_like(U[..., 2])], -1)
    return T1, T2, T3, T4, T5
best = None
for name, DUc in (("DU[m,i]=d_m U_i", DU), ("DU[i,m]=d_m U_i", np.swapaxes(DU, -1, -2))):
    T = terms(DUc); Ru = sum(T) + gP
    rel = np.sqrt((Ru ** 2).sum(-1).mean()) / np.sqrt(sum((t ** 2).sum(-1).mean() for t in T) + (gP ** 2).sum(-1).mean())
    print(f"convention {name}: RMS R_u / RMS of the six terms = {rel:.3e}; max |div U| / RMS|DU| = {np.abs(div).max() / np.sqrt((DU ** 2).sum((-1, -2)).mean()):.2e}")
    if best is None or rel < best[0]:
        best = (rel, name, T)
rel, name, T = best; print(f"using {name}")
sel = R.get("selection") or {}; ri = sel.get("radius_indices")
for k, rec in R["factors"].items():
    vb = rec.get("vs_3Nk")
    if not vb or "selected_points" not in vb:
        continue
    sp = vb["selected_points"]; per = np.array(sp["per_radius_max"]); j = int(np.argmax(per)); rj_ = ri[j]; r = radii[rj_]
    # five-term RMS on that shell (whole exchange sphere at that radius, angular mean) and |grad P| RMS there
    rms5 = np.sqrt(sum((t[rj_] ** 2).sum(-1).mean() for t in T)); rmsP = np.sqrt((gP[rj_] ** 2).sum(-1).mean())
    T1r = np.sqrt((T[0][rj_] ** 2).sum(-1).mean())
    print(f"{k} Nk vs 3 Nk: largest selected-point grad P change {per[j]:.2e} at radius index {rj_}, r = {r:.4g} = {r / R0:.4g} R0; on that sphere RMS|grad P| = {rmsP:.3e}, RMS of the five momentum terms (sqrt of the summed mean squares) = {rms5:.3e}, "
          f"|grad P| / five-term RMS = {rmsP / rms5:.3e}; |grad P| / RMS((1-c_l)U) = {rmsP / T1r:.3e}; per-radius list (r/R0: change): " + ", ".join(f"{radii[i] / R0:.3g}: {v:.1e}" for i, v in zip(ri, per)))
