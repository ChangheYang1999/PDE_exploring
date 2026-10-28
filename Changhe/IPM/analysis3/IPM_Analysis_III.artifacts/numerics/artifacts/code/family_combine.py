"""Decoupled weight family (lead notes 26-28): boxwise lower bound of m_fam = m_a + (a_ang - 17/4) tan(theta) V.grad(theta) - Delta q 1_{t>=0}
over the whole plane from the certified per-box data of runs/MARGIN_REF2 (MA_ref lower, TANG upper, Q upper; float arithmetic on directed
box data), with the near-axis refined values of the margin.py MARGIN_FAMILY runs substituted on their cells (MF_ref).
Usage: python3 family_combine.py a_ang Delta out.json runs/FAM_x_A runs/FAM_x_B ...   (refined run directories; may be empty)"""
import sys, json, os
import numpy as np
A_ANI = 17.0 / 4
a_ang, Delta, outp = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; refdirs = sys.argv[4:]
base = np.load("runs/MARGIN_REF2/margin.npz", allow_pickle=True)
MA = base["MA_ref"]; TANG_hi = base["TANG"][:, :, 1]; Q_hi = base["Q"][:, :, 1]
ta = base["cell_ta"]; h = base["cell_h"]; kind = base["cell_kind"]
nc, nb = MA.shape
whole = np.array([k == "pinf" or (k != "minf" and t >= 0) for k, t in zip(kind, ta)])
part = np.array([(not w) and k != "minf" and (t + hh) >= 0 for w, k, t, hh in zip(whole, kind, ta, h)])
fam_q = np.where(whole[:, None], Q_hi, np.where(part[:, None], np.maximum(Q_hi, 0.0), 0.0))
MF = MA + (a_ang - A_ANI) * TANG_hi - Delta * fam_q - 1e-12     # 1e-12: covers the double rounding of this float combination of directed box data (lower bound)
before = MF.copy()
cells_ref = set(); nsub = 0
for rd in refdirs:
    z = np.load(os.path.join(rd, "margin.npz"), allow_pickle=True); R = z["MF_ref"]
    ok = np.isfinite(R)
    MF[ok] = np.maximum(MF[ok], R[ok]); nsub += int(ok.sum()); cells_ref |= set(np.where(ok.any(axis=1))[0].tolist())
def amin(M):
    i = np.unravel_index(np.nanargmin(M), M.shape); return dict(value=float(M[i]), cell=int(i[0]), t_a=float(ta[i[0]]), theta_box=int(i[1]), theta_deg=float(np.degrees(base["theta_edges"][i[1]])))
cells_ref = sorted(cells_ref)
res = dict(a_ang=a_ang, Delta=Delta, whole_plane_before=amin(before), whole_plane_after=amin(MF), negative_boxes_before=int((before < 0).sum()), negative_boxes_after=int((MF < 0).sum()),
           refined_cells=len(cells_ref), substituted_boxes=nsub, refdirs=refdirs)
if cells_ref:
    sub = np.ix_(cells_ref, range(56, 64))
    res["near_axis_boxes_56_63_on_refined_cells"] = dict(before=float(np.nanmin(before[sub])), after=float(np.nanmin(MF[sub])))
    res["all_boxes_on_refined_cells"] = dict(before=float(np.nanmin(before[cells_ref])), after=float(np.nanmin(MF[cells_ref])))
    rest = np.ones(nc, bool); rest[cells_ref] = False
    res["other_cells_min"] = amin(before[rest]) if rest.any() else None
    if rest.any(): res["other_cells_min"]["cell"] = int(np.where(rest)[0][res["other_cells_min"]["cell"]]); res["other_cells_min"]["t_a"] = float(ta[res["other_cells_min"]["cell"]])
json.dump(res, open(outp, "w"), indent=1); print(json.dumps(res, indent=1))
