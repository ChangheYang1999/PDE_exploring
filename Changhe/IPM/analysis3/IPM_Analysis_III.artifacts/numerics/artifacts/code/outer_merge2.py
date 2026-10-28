"""Merge SEVERAL finer-outer-cover margin runs (margin.py with MARGIN_OUTER_EXTRA) with the production arrays runs/MARGIN_REF2/margin.npz:
each run's computed cells replace the production cells that they tile exactly (both rigorous lower bounds of the same quantities); the
production arrays stand elsewhere. Reports the plane infima of m (M_ref), m_a (MA_ref) and, if '-- a_ang Delta family_json' is given, of
m_fam(a_ang, Delta) = m_a + (a_ang - 17/4) tang - Delta q 1_{t >= 0} (recomputed from the base arrays with DIRECTED float rounding, then
sharpened by the refinement directories of the family json). Validation (astra referee 16:05Z): the computed new cells must be contiguous and
tile the replaced production cells exactly; every retained or replacing box must carry a finite bound (no NaN is ever skipped); Delta >= 0
and a_ang <= 17/4 are required by the endpoint choices; refinement arrays must have the base cell geometry; printed bounds are truncated
toward -infinity (6 decimals) and the exact floats are printed too.
Usage: python3 outer_merge2.py runs/<tag1> [runs/<tag2> ...] [-- a_ang Delta refined_family_json]"""
import sys, json, os, math
import numpy as np
def fail(msg): raise SystemExit("INVALID: " + msg)
def floor6(x): return math.floor(x * 1e6) / 1e6
def lo(x): return np.nextafter(x, -np.inf)
def up(x): return np.nextafter(x, np.inf)
args = sys.argv[1:]; fam_args = None
if "--" in args: k = args.index("--"); fam_args = args[k + 1:]; args = args[:k]
base = np.load("runs/MARGIN_REF2/margin.npz", allow_pickle=True)
bt = base["cell_ta"].astype(float); bh = np.array([float(x) if x is not None and np.isfinite(float(x)) else np.inf for x in base["cell_h"]]); kind = base["cell_kind"]
nb, ntheta = base["MA_ref"].shape
replaced_all = set(); news = []
for rd in args:
    new = np.load(os.path.join(rd, "margin.npz"), allow_pickle=True)
    if new["MA_ref"].shape[1] != ntheta: fail("%s: angular box count differs" % rd)
    sel = [i for i in range(len(new["cell_ta"])) if np.isfinite(new["MA_ref"][i]).any()]
    if not sel: fail("%s: no computed cells" % rd)
    for i in sel:
        if new["cell_kind"][i] in ("minf", "pinf"): fail("%s: half-infinite cell %d computed; this merge handles finite cells only" % (rd, i))
        for key in ("M_ref", "MA_ref") + (("MF_ref",) if fam_args else ()):
            if not np.isfinite(new[key][i]).all(): fail("%s: cell %d has a non-finite %s box" % (rd, i, key))
    # contiguity of the computed cells and exact tiling of production cells
    ta = [float(new["cell_ta"][i]) for i in sel]; h = [float(new["cell_h"][i]) for i in sel]
    for a in range(len(sel) - 1):
        if abs(ta[a] + h[a] - ta[a + 1]) > 1e-9: fail("%s: computed cells %d and %d are not contiguous" % (rd, sel[a], sel[a + 1]))
    lo_t, hi_t = ta[0], ta[-1] + h[-1]
    rep = [i for i in range(nb) if kind[i] not in ("minf", "pinf") and bt[i] >= lo_t - 1e-9 and bt[i] + bh[i] <= hi_t + 1e-9]
    if not rep: fail("%s: no production cell inside [%.6f, %.6f]" % (rd, lo_t, hi_t))
    rt = sorted((bt[i], bt[i] + bh[i]) for i in rep)
    if abs(rt[0][0] - lo_t) > 1e-9 or abs(rt[-1][1] - hi_t) > 1e-9: fail("%s: new cells do not end on production cell boundaries" % rd)
    for a in range(len(rt) - 1):
        if abs(rt[a][1] - rt[a + 1][0]) > 1e-9: fail("%s: replaced production cells are not contiguous" % rd)
    if replaced_all & set(rep): fail("overlapping runs")
    replaced_all |= set(rep)
    print("%s: covers t in [%.6f, %.6f] with %d contiguous cells (all %d boxes finite); replaces production cells %s (t_a %s)" % (rd, lo_t, hi_t, len(sel), ntheta, rep, [round(bt[i], 4) for i in rep]))
    news.append((rd, new, sel, rep))
keep = np.ones(nb, bool); keep[sorted(replaced_all)] = False
res = {}
def report(key, base_arr, getnew):
    if not np.isfinite(base_arr[keep]).all(): fail("retained production boxes with a non-finite %s bound: %s" % (key, np.argwhere(~np.isfinite(base_arr) & keep[:, None])[:5].tolist()))
    rest_min = float(np.min(base_arr[keep])); i = np.unravel_index(np.argmin(np.where(keep[:, None], base_arr, np.inf)), base_arr.shape)
    parts = [(rd, float(np.min(getnew(new)[sel]))) for rd, new, sel, rep in news]
    comb = min([rest_min] + [v for _, v in parts]); old = float(np.nanmin(base_arr))
    res[key] = dict(min_elsewhere=rest_min, elsewhere_cell=int(i[0]), elsewhere_ta=float(bt[i[0]]), elsewhere_box=int(i[1]), new_mins={rd: v for rd, v in parts},
                    old_min_on_replaced_cells=float(np.nanmin(base_arr[sorted(replaced_all)])), combined_float=comb, combined_floor6=floor6(comb), old_global=old)
    print("%s: new-run minima %s; production elsewhere %r (cell %d, t_a %.4f, box %d); replaced cells old min %r; COMBINED plane inf >= %.6f (float %r; old %r)"
          % (key, {rd: repr(v) for rd, v in parts}, rest_min, i[0], bt[i[0]], i[1], res[key]["old_min_on_replaced_cells"], floor6(comb), comb, old))
report("M_ref", base["M_ref"], lambda z: z["M_ref"]); report("MA_ref", base["MA_ref"], lambda z: z["MA_ref"])
if fam_args:
    a_ang, Delta = float(fam_args[0]), float(fam_args[1]); fam = json.load(open(fam_args[2]))
    if not (Delta >= 0 and a_ang <= 17.0 / 4): fail("endpoint choices need Delta >= 0 and a_ang <= 17/4")
    c = a_ang - 17.0 / 4                       # exact in binary64 for a_ang = 4 (c = -1/4); c <= 0
    Delta_up = up(Delta) if Delta != 0 else 0.0  # the decimal Delta may not be representable: use an upper float so that -Delta_up q <= -Delta q
    MA = base["MA_ref"]; TANG_hi = base["TANG"][:, :, 1]; Q_hi = base["Q"][:, :, 1]
    whole = np.array([k == "pinf" or (k != "minf" and t >= 0) for k, t in zip(kind, bt)]); part = np.array([(not w) and k != "minf" and (t + h) >= 0 for w, k, t, h in zip(whole, kind, bt, bh)])
    fam_q = np.where(whole[:, None], Q_hi, np.where(part[:, None], np.maximum(Q_hi, 0.0), 0.0))
    # directed lower bound of MA + c*TANG_hi - Delta*q: c*TANG_hi rounded down (c <= 0, TANG_hi an upper end), Delta_up*q rounded up, sums rounded down
    MF = lo(lo(MA + lo(c * TANG_hi)) - up(Delta_up * fam_q))
    for rd in fam.get("refdirs", []):
        z = np.load(os.path.join(rd, "margin.npz"), allow_pickle=True)
        if z["MF_ref"].shape != MF.shape or not np.array_equal(z["cell_ta"].astype(float), bt): fail("%s: refinement arrays do not have the base cell geometry" % rd)
        R = z["MF_ref"]; ok = np.isfinite(R); MF[ok] = np.maximum(MF[ok], R[ok])
    print("family (%g, %g): directed recomputation on the base cover (Delta_up = %r), sharpened by %d refinement runs" % (a_ang, Delta, Delta_up, len(fam.get("refdirs", []))))
    report("MF_%g_%g" % (a_ang, Delta), MF, lambda z: z["MF_ref"])
out = os.path.join(args[-1], "outer_merge2.json"); json.dump(dict(runs=args, results=res, printed_bounds_are_floor6=True), open(out, "w"), indent=1); print("saved", out)
