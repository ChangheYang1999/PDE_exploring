"""Summarize the certificate outputs (SPEC item R0 by region, R2, R4) from runs/cert_resid_middle.json,
runs/cert_resid_regions.json, runs/cert_tail.json, runs/cert_inner_tail.json (those that exist)."""
import sys, os, json
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
_U = 2.0 ** -53


def up(x):                 # outward rounding of a nonnegative float
    return float(np.nextafter(x, np.inf))


def wfac(rb, gk):
    """upper bound of (1 + rb/L)^gk, rb an exact double (right end of a cell), via Arb."""
    LL = arb(7.651424601381517)
    return float(np.nextafter(float(((1 + arb(float(rb)) / LL) ** arb(gk)).upper()), np.inf))     # outward


def osum(vals):
    """outward-rounded sum of nonnegative floats: fsum (correctly rounded) then one successor step plus n*eta."""
    import math
    return up(up(math.fsum(vals)) + len(vals) * 2.0 ** -1074)

lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xstar = 8.600063803
out = {}
mid = os.path.join(lane, "runs/cert_resid_middle.json")
if _jexists(mid):
    d = json.load(_jopen(mid)); rows = d["rows"]
    ra = np.exp(np.array([r["t_a"] for r in rows]))
    rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rows])   # right end radius, outward (Arb)
    Wm = np.array([r["W_over_m"] for r in rows]); L2 = np.array([r["L2piece"] for r in rows]); W = np.array([r["W"] for r in rows])
    GK = 0.5 - 0.17936053129375418                   # gamma - k for gamma = 0.5 (SPEC v2 weight m (1+u)^(gamma-k)); the double of gamma - k
    # (1+u)^(gamma-k) is increasing: bound by its value at the right end of each cell, computed outward in Arb (exact double rb)
    Wg = np.array([up(Wm[i] * wfac(rb[i], GK)) for i in range(len(rows))])
    W5 = np.array([up(Wm[i] * wfac(rb[i], 0.5)) for i in range(len(rows))])      # lead's multiplier form (1+u)^{1/2}
    print("middle region: %d sub-cells, done=%s" % (len(rows), d.get("done")))
    print("  multiplier form (lead 16:5xZ): max W (1+u)^(1/2) / m [allowed growth k - 1/2] = %.4e at r = %.4g ; secondary (1+u)^(1/2-k): %.4e" % (W5.max(), ra[np.argmax(W5)], Wg.max()))
    print("  r range [%.5g, %.5g]; max W/m = %.4e at r in [%.4g, %.4g]; max W = %.4e; sum L2 pieces = %.4e" % (ra[0], rb[-1], Wm.max(), ra[np.argmax(Wm)], rb[np.argmax(Wm)], W.max(), osum(L2)))
    shells = [(ra[0], 0.0156), (0.0156, 0.0625), (0.0625, 0.25), (0.25, 1), (1, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, 3413.1)]
    table = []
    for lo, hi in shells:
        m = (rb > lo) & (ra < hi)
        if m.any():
            i = np.argmax(np.where(m, Wm, -1))
            table.append(dict(lo=lo, hi=hi, max_W_over_m=float(Wm[m].max()), r_at=float(ra[i]), max_W=float(W[m].max()), L2=osum(L2[m]), max_W_over_m_g05=float(Wg[m].max()), max_W_over_m_mult_half=float(W5[m].max())))
            print("  shell [%8.4g, %8.4g): divisor W/m = %.4e at r = %.4g ; multiplier W(1+u)^(1/2)/m = %.4e ; (1+u)^(1/2-k): %.4e ; max W = %.3e ; L2 piece sum %.3e" % (lo, hi, Wm[m].max(), ra[i], W5[m].max(), Wg[m].max(), W[m].max(), osum(L2[m])))
    m = (rb > xstar / 2) & (ra < 2 * xstar)
    i = np.argmax(np.where(m, Wm, -1))
    print("  P-shell [x*/2, 2x*] = [%.4g, %.4g]: max W/m = %.4e at r = %.4g ; max W = %.3e" % (xstar / 2, 2 * xstar, Wm[m].max(), ra[i], W[m].max()))
    rem = max(r["rem_eps"] for r in rows); print("  max Taylor remainder of eps over cells: %.2e ; max remA %.1e remB %.1e" % (rem, max(r["remA"] for r in rows), max(r["remB"] for r in rows)))
    out["middle"] = dict(max_W_over_m=float(Wm.max()), r_at=float(ra[np.argmax(Wm)]), L2=osum(L2), shells=table, P_shell=float(Wm[m].max()), max_W_over_m_g05=float(Wg.max()))
reg = os.path.join(lane, "runs/cert_resid_regions.json")
if _jexists(reg):
    rows = json.load(_jopen(reg))["rows"]
    for region in ("outer", "inner"):
        rr = [r for r in rows if r["region"] == region]
        if not rr: continue
        ra = np.array([r["r_a"] for r in rr]); Wm = np.array([r["W_over_m"] for r in rr]); Wf = np.array([r["W_over_m_far"] for r in rr]); L2 = osum([r["L2piece"] for r in rr])
        hh = np.array([r["h"] for r in rr])
        Wg = np.array([up(Wm[i] * wfac(float(np.nextafter(float((arb(rr[i]["t_a"]) + arb(rr[i]["h"])).exp().upper()), np.inf)), 0.5 - 0.17936053129375418)) for i in range(len(rr))])
        print("%s region: %d sub-cells, r in [%.4g, %.4g]: max W/m = %.4e at r = %.4g ; max W (1+u)^0.3206 / m = %.4e at r = %.4g ; (v1 weight (1+u)^0.5: %.4e) ; L2 sum %.3e" % (
            region, len(rr), ra.min(), ra.max(), Wm.max(), ra[np.argmax(Wm)], Wg.max(), ra[np.argmax(Wg)], Wf.max(), L2))
        if region == "inner":
            W5 = np.array([r["W_over_r5"] for r in rr]); print("  inner R4: max W / r^5 = %.4e at r = %.4g" % (W5.max(), ra[np.argmax(W5)]))
        out[region] = dict(max_W_over_m=float(Wm.max()), max_W_over_m_g05=float(Wg.max()), max_W_over_m_far_v1=float(Wf.max()), L2=float(L2))
for name in ("runs/cert_tail.json", "runs/cert_inner_tail.json"):
    p = os.path.join(lane, name)
    if _jexists(p):
        print(name, ":", json.load(_jopen(p)))
json.dump(out, open(os.path.join(lane, "runs/cert_summary.json"), "w"), indent=1)


# ---- derivative certificate (R1, R3, R5) and R4 from runs/cert_deriv_*.json (chain3/chain4) ----
def deriv_summary(lane):
    import glob
    for name in ("middle", "outer", "inner"):
        found = glob.glob(os.path.join(lane, "runs/cert_deriv*_%s.json" % name)) + glob.glob(os.path.join(lane, "runs/cert_deriv*_%s.json.gz" % name))
        for path in sorted(set(q[:-3] if q.endswith(".gz") else q for q in found)):   # _jopen falls back to path + .gz (shift 8: the gzipped shipped files were skipped before)
            d = json.load(_jopen(path)); rows = d["rows"]
            if not rows: continue
            r_a = np.exp(np.array([r["t_a"] for r in rows])); m = np.array([r["m_inf"] for r in rows])
            keys = sorted(k for k in rows[0] if k.startswith("W_") and "_" in k[2:] and k[2:].replace("_", "").isdigit())
            print("%s (%s): %d cells, done=%s" % (os.path.basename(path), name, len(rows), d.get("done")))
            for key in keys:
                v = np.array([r.get(key, np.nan) for r in rows]) / m
                print("   sup %s / m = %.4e at r = %.4g" % (key, np.nanmax(v), r_a[np.nanargmax(v)]))
            for key in ("W_eps_minus_dteps", "W_K", "W1_K", "W_dtK"):
                if key in rows[0]:
                    v = np.array([r.get(key, np.nan) for r in rows]) / m
                    print("   sup %s / m = %.4e at r = %.4g  (unweighted sup %s = %.4e)" % (key, np.nanmax(v), r_a[np.nanargmax(v)], key, np.nanmax([r.get(key, np.nan) for r in rows])))
            if name == "middle":
                sel = (r_a > 0.75 * xstar) & (r_a < 1.25 * xstar)
                print("   P-disc cells (r in [0.75 x*, 1.25 x*]): %d cells with nder = %s" % (sel.sum(), sorted(set(r["nder"] for r in rows if 0.75 * xstar < np.exp(r["t_a"]) < 1.25 * xstar))))
                for key in keys:
                    if key[2] in "345" or key[4] in "345":
                        v = np.array([r.get(key, np.nan) for r in rows])[sel]
                        if np.isfinite(v).any(): print("     P-disc sup %s = %.4e" % (key, np.nanmax(v)))
            if name == "inner" and "W_over_r5" in rows[0]:
                v = np.array([r["W_over_r5"] for r in rows]); print("   R4: sup W / r^5 = %.4e at r = %.4g" % (v.max(), r_a[np.argmax(v)]))


deriv_summary(lane)
