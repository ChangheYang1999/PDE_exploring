"""Merge a finer-outer-cover margin run (margin.py with MARGIN_OUTER_EXTRA) with the production arrays: on the radial range covered by the
new run's computed cells, the new per-box bounds replace the production ones (both are rigorous lower bounds of the same quantities; the new
cells are a refinement of the production cells there), elsewhere the production arrays stand. Reports inf m, inf m_a (and inf m_fam if the run
tracked a family) over the plane.   Usage: python3 outer_merge.py runs/<newtag> [a_ang Delta refined_family_json]"""
import sys, json, os
import numpy as np
new = np.load(os.path.join(sys.argv[1], "margin.npz"), allow_pickle=True); base = np.load("runs/MARGIN_REF2/margin.npz", allow_pickle=True)
def cell_range(z, sel):
    lo = min(float(z["cell_ta"][i]) for i in sel); hi = max(float(z["cell_ta"][i]) + (float(z["cell_h"][i]) if z["cell_kind"][i] not in ("minf", "pinf") else 1e9) for i in sel)
    return lo, hi
sel_new = [i for i in range(len(new["cell_ta"])) if np.isfinite(new["MA_ref"][i]).any()]
lo, hi = cell_range(new, sel_new); print("new run covers t in [%.6f, %.6f] with %d cells" % (lo, hi, len(sel_new)))
# production cells entirely inside [lo, hi] are replaced
bt = base["cell_ta"].astype(float); bh = np.array([float(x) if x is not None and np.isfinite(float(x)) else np.inf for x in base["cell_h"]])
replaced = [i for i in range(len(bt)) if bt[i] >= lo - 1e-12 and bt[i] + bh[i] <= hi + 1e-12 and base["cell_kind"][i] != "pinf"]
print("production cells replaced:", replaced, [round(bt[i], 4) for i in replaced])
assert abs(min(bt[i] for i in replaced) - lo) < 1e-9 and abs(max(bt[i] + bh[i] for i in replaced) - hi) < 1e-9, "the new cells must tile exactly the replaced production cells"
res = {}
for key in ("M_ref", "MA_ref"):
    B = base[key].copy(); keep = np.ones(len(bt), bool); keep[replaced] = False
    old_min_replaced = float(np.nanmin(base[key][replaced])); new_min = float(np.nanmin(new[key][sel_new])); rest_min = float(np.nanmin(B[keep]))
    i = np.unravel_index(np.nanargmin(np.where(keep[:, None], B, np.inf)), B.shape)
    res[key] = dict(old_min_on_replaced_cells=old_min_replaced, new_min_on_replaced_range=new_min, min_elsewhere=rest_min, elsewhere_cell=int(i[0]), elsewhere_ta=float(bt[i[0]]), elsewhere_box=int(i[1]),
                    combined=min(new_min, rest_min), old_global=float(np.nanmin(base[key])))
    print("%s: replaced cells old %.6f -> new %.6f; elsewhere %.6f (cell %d, t_a %.4f, box %d); combined inf >= %.6f (old %.6f)" % (key, old_min_replaced, new_min, rest_min, i[0], bt[i[0]], i[1], min(new_min, rest_min), float(np.nanmin(base[key]))))
if len(sys.argv) > 4 and np.isfinite(new["MF_ref"][sel_new]).any():
    a_ang, Delta = float(sys.argv[2]), float(sys.argv[3]); fam = json.load(open(sys.argv[4]))
    # the refined-family combination (family_combine.py) stored only summaries; recompute the whole-plane array as there, then substitute
    A_ANI = 17.0 / 4; MA = base["MA_ref"]; TANG_hi = base["TANG"][:, :, 1]; Q_hi = base["Q"][:, :, 1]; kind = base["cell_kind"]
    whole = np.array([k == "pinf" or (k != "minf" and t >= 0) for k, t in zip(kind, bt)]); part = np.array([(not w) and k != "minf" and (t + h) >= 0 for w, k, t, h in zip(whole, kind, bt, bh)])
    fam_q = np.where(whole[:, None], Q_hi, np.where(part[:, None], np.maximum(Q_hi, 0.0), 0.0)); MF = MA + (a_ang - A_ANI) * TANG_hi - Delta * fam_q - 1e-12
    for rd in fam.get("refdirs", []):
        z = np.load(os.path.join(rd, "margin.npz"), allow_pickle=True); R = z["MF_ref"]; ok = np.isfinite(R); MF[ok] = np.maximum(MF[ok], R[ok])
    keep = np.ones(len(bt), bool); keep[replaced] = False
    new_min = float(np.nanmin(new["MF_ref"][sel_new])); rest_min = float(np.nanmin(MF[keep])); i = np.unravel_index(np.nanargmin(np.where(keep[:, None], MF, np.inf)), MF.shape)
    res["MF_%g_%g" % (a_ang, Delta)] = dict(old_min_on_replaced_cells=float(np.nanmin(MF[replaced])), new_min_on_replaced_range=new_min, min_elsewhere=rest_min, elsewhere_cell=int(i[0]), elsewhere_ta=float(bt[i[0]]), elsewhere_box=int(i[1]), combined=min(new_min, rest_min))
    print("m_fam(%g, %g): replaced cells old %.6f -> new %.6f; elsewhere %.6f (cell %d, t_a %.4f, box %d); combined inf >= %.6f" % (a_ang, Delta, float(np.nanmin(MF[replaced])), new_min, rest_min, i[0], bt[i[0]], i[1], min(new_min, rest_min)))
json.dump(res, open(os.path.join(sys.argv[1], "outer_merge.json"), "w"), indent=1)
