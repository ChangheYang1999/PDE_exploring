"""Three-resolutions table (SPEC item RES; PROMPT section 6 item 6): the same certificate quantities for every trial variant that has outputs.
Variants (tag -> files): '' = the X3 trial data/trial_v2_h0.008.npz (runs/scalars_full.json, cert_resid_middle.json, cert_resid_regions.json,
cert_tail.json, cert_tail_d05.json, cert_inner_tail.json); 'v3_h0.004' (half knot spacing), 'v4_M230' (230 modes), 'v5_R0knot2' (knot scheme 2),
'n7' (centre-regular variant): runs/<name>_<tag>.json.  Rigorous quantities, same formulas as src/cert_summary.py (outward rounding; the
multiplier weights (1+u)^gamma bounded at the right end of each cell in Arb).  Output: runs/variants_summary.txt and .json.
Usage: python3 src/variants_summary.py [tag ...]
"""
import sys, os, json, math
import numpy as np
from flint import arb, ctx


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 1 MB gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)


def _jexists(path):
    import os
    return os.path.exists(path) or os.path.exists(str(path) + ".gz")
ctx.prec = 100
lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K_TRIAL = 0.17936053129375418; L_TRIAL = 7.651424601381517; XSTAR = 8.600063803


def up(x): return float(np.nextafter(x, np.inf))
def osum(vals): return up(up(math.fsum(vals)) + len(vals) * 2.0 ** -1074)
def wfac(rb, gk):
    return float(np.nextafter(float(((1 + arb(float(rb)) / arb(L_TRIAL)) ** arb(gk)).upper()), np.inf))


def files(tag):
    if tag == "":
        return dict(scalars="runs/scalars_full.json", middle="runs/cert_resid_middle.json", regions="runs/cert_resid_regions.json",
                    tail="runs/cert_tail.json", tail05="runs/cert_tail_d05.json", itail="runs/cert_inner_tail.json", label="X3 trial (h = 0.008, M = 260)")
    lab = {"v3_h0.004": "v3: knot spacing h = 0.004", "v4_M230": "v4: 230 modes", "v5_R0knot2": "v5: knot scheme 2", "n7": "N7: centre-regular variant"}.get(tag, tag)
    return dict(scalars="runs/scalars_%s.json" % tag, middle="runs/cert_resid_middle_%s.json" % tag, regions="runs/cert_resid_regions_%s.json" % tag,
                tail="runs/cert_tail_%s.json" % tag, tail05="runs/cert_tail_%s_d05.json" % tag, itail="runs/cert_inner_tail_%s.json" % tag, label=lab)


def summarize(tag):
    f = files(tag); out = dict(tag=tag, label=f["label"])
    p = os.path.join(lane, f["scalars"])
    if _jexists(p):
        d = json.load(_jopen(p))
        out["scalars"] = dict(x_star=[d["x_star_mid"], d["x_star_rad"]], mu_minus_1=d["mu_minus_1"], g=d["g_star"], w_prime_P=d["w_prime_P"], c=d["c"], c_l=d["c_l"], contracted=d.get("newton_contracted"))
    p = os.path.join(lane, f["middle"])
    if _jexists(p):
        d = json.load(_jopen(p)); rows = d["rows"]
        ra = np.exp(np.array([r["t_a"] for r in rows]))
        rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rows])
        Wm = np.array([r["W_over_m"] for r in rows]); W = np.array([r["W"] for r in rows]); L2 = [r["L2piece"] for r in rows]
        W5 = np.array([up(Wm[i] * wfac(rb[i], 0.5)) for i in range(len(rows))])
        Wg = np.array([up(Wm[i] * wfac(rb[i], 0.5 - K_TRIAL)) for i in range(len(rows))])
        mP = (rb > XSTAR / 2) & (ra < 2 * XSTAR)
        out["middle"] = dict(ncells=len(rows), done=bool(d.get("done")), r_range=[float(ra[0]), float(rb[-1])], sup_W_over_m=float(Wm.max()), r_at=[float(ra[np.argmax(Wm)]), float(rb[np.argmax(Wm)])],
                             sup_W=float(W.max()), mult_half=float(W5.max()), mult_half_minus_k=float(Wg.max()), L2=osum(L2), P_shell_W_over_m=float(Wm[mP].max()) if mP.any() else None,
                             max_rem_eps=max(r["rem_eps"] for r in rows), max_remA=max(r["remA"] for r in rows))
    p = os.path.join(lane, f["regions"])
    if _jexists(p):
        rows = json.load(_jopen(p))["rows"]
        for region in ("outer", "inner"):
            rr = [r for r in rows if r["region"] == region]
            if not rr: continue
            ra = np.array([r["r_a"] for r in rr]); Wm = np.array([r["W_over_m"] for r in rr]); L2 = osum([r["L2piece"] for r in rr])
            Wg = np.array([up(Wm[i] * wfac(float(np.nextafter(float((arb(rr[i]["t_a"]) + arb(rr[i]["h"])).exp().upper()), np.inf)), 0.5 - K_TRIAL)) for i in range(len(rr))])
            out[region] = dict(ncells=len(rr), r_range=[float(ra.min()), float(ra.max())], sup_W_over_m=float(Wm.max()), r_at=float(ra[np.argmax(Wm)]), mult_half_minus_k=float(Wg.max()), L2=float(L2))
    for key in ("tail", "tail05", "itail"):
        p = os.path.join(lane, f[key])
        if _jexists(p): out[key] = json.load(_jopen(p))
    return out


def main(tags):
    res = [summarize(t) for t in tags]
    lines = ["Three-resolutions table (RES): rigorous certificate quantities per trial variant (outward rounded; raw values in runs/variants_summary.json)", ""]
    hdr = "%-34s %-22s %-28s %-24s %-24s %-12s %-12s %-12s %-12s %-10s" % ("variant", "x_* (mid, rad)", "mu~ - 1", "g = rho~_y(P)", "w'(P)", "mid W/m", "mid mult1/2", "mid sup W", "mid L2", "mid cells")
    lines.append(hdr)
    for r in res:
        s = r.get("scalars", {}); m = r.get("middle", {})
        lines.append("%-34s %-22s %-28s %-24s %-24s %-12s %-12s %-12s %-12s %-10s" % (
            r["label"], ("%.15g, %.2e" % tuple(s["x_star"])) if s else "-", ("[%.6e, %.6e]" % tuple(s["mu_minus_1"])) if s else "-",
            ("[%.12f, %.12f]" % tuple(s["g"])) if s else "-", ("[%.12f, %.12f]" % tuple(s["w_prime_P"])) if s else "-",
            ("%.4e" % m["sup_W_over_m"]) if m else "-", ("%.4e" % m["mult_half"]) if m else "-", ("%.4e" % m["sup_W"]) if m else "-", ("%.3e" % m["L2"]) if m else "-",
            ("%d%s" % (m["ncells"], "" if m["done"] else " (partial)")) if m else "-"))
    lines.append("")
    lines.append("%-34s %-14s %-14s %-14s %-14s %-14s %-14s %-16s %-16s" % ("variant", "outer W/m", "outer (1+u)^g", "outer L2", "inner W/m", "inner L2", "mid P-shell", "outer tail (wtd)", "inner tail W/m"))
    for r in res:
        o = r.get("outer", {}); i_ = r.get("inner", {}); m = r.get("middle", {}); t = r.get("tail", {}); it = r.get("itail", {})
        lines.append("%-34s %-14s %-14s %-14s %-14s %-14s %-14s %-16s %-16s" % (
            r["label"], ("%.4e" % o["sup_W_over_m"]) if o else "-", ("%.4e" % o["mult_half_minus_k"]) if o else "-", ("%.3e" % o["L2"]) if o else "-",
            ("%.4e" % i_["sup_W_over_m"]) if i_ else "-", ("%.3e" % i_["L2"]) if i_ else "-", ("%.4e" % m["P_shell_W_over_m"]) if m and m.get("P_shell_W_over_m") else "-",
            str(t["tail_bound_weighted"])[:14] if t else "-", str(it["bound_W_over_m"])[:14] if it else "-"))
    txt = "\n".join(lines); print(txt)
    open(os.path.join(lane, "runs/variants_summary.txt"), "w").write(txt + "\n")
    json.dump(res, open(os.path.join(lane, "runs/variants_summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1:] if len(sys.argv) > 1 else ["", "v3_h0.004", "v4_M230", "v5_R0knot2", "n7"])
