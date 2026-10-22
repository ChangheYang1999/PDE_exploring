"""Markdown tables of NUM_REPORT 7.3 (middle shells, regions and tails) and 7.3c (three resolutions) with DIRECTED decimal rounding:
every upper bound is rounded UP (ceiling at the printed number of significant digits), every lower endpoint of an interval DOWN; locations
('at r') are rounded to nearest and are not bounds.  Sources: runs/cert_resid_middle[_tag].json, runs/cert_resid_regions[_tag].json,
runs/cert_tail[_tag].json, runs/cert_inner_tail[_tag].json, runs/scalars_full.json / runs/scalars_<tag>.json, runs/variants_summary.json
(the aggregates there are the raw floats; this script re-derives them from the per-cell rows with the same outward arithmetic as
src/cert_summary.py and src/variants_summary.py: cell maxima of the stored per-cell upper bounds, weights (1+u)^gamma bounded at the right end
of each cell in Arb, L2 sums by outward fsum).  The far-weight exponent is 1/2 - k for the stored k (0.32063946870624582, written '0.3206' in
column heads).  Usage: python3 src/report_tables.py > runs/report_tables.md
"""
import os, sys, json, math, re, gzip
import numpy as np
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from flint import arb, ctx
ctx.prec = 100
lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K_TRIAL = 0.17936053129375418; L_TRIAL = 7.651424601381517; XSTAR = 8.600063803
GK = 0.5 - K_TRIAL


def jload(p):
    p = os.path.join(lane, p)
    if not os.path.exists(p) and os.path.exists(p + ".gz"): return json.load(gzip.open(p + ".gz", "rt"))
    if not os.path.exists(p): return None
    return json.load(open(p))


def up(x): return float(np.nextafter(x, np.inf))
def osum(vals): return up(up(math.fsum(vals)) + len(vals) * 2.0 ** -1074)
def wfac(rb, gk): return float(np.nextafter(float(((1 + arb(float(rb)) / arb(L_TRIAL)) ** arb(gk)).upper()), np.inf))


def _q(x, sig):
    d = Decimal.from_float(float(x))          # the EXACT binary64 value (not its shortest repr), so that the quantization is a true ceiling/floor
    return d, Decimal(1).scaleb(d.adjusted() - sig + 1)


def _efmt(d):
    """'1.2345e-4' style without zero-padded exponents; plain digits when the exponent is 0."""
    s = format(d, "e"); mant, ex = s.split("e"); ex = int(ex)
    return mant if ex == 0 else "%se%s%d" % (mant, "-" if ex < 0 else "+", abs(ex))


def ceil_sig(x, sig):
    """decimal with sig significant digits, rounded toward +infinity (upper bounds)."""
    if x == 0: return "0"
    d, q = _q(x, sig); return _efmt(d.quantize(q, rounding=ROUND_CEILING))


def floor_sig(x, sig):
    if x == 0: return "0"
    d, q = _q(x, sig); return _efmt(d.quantize(q, rounding=ROUND_FLOOR))


def ceil_fix(x, places): return format(Decimal.from_float(float(x)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_CEILING), "f")
def floor_fix(x, places): return format(Decimal.from_float(float(x)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_FLOOR), "f")
def near(x, sig): return ("%." + str(sig) + "g") % x


def ball_upper(s):
    m, r = re.match(r"\[\s*([-0-9.eE+]+)\s*\+/-\s*([-0-9.eE+]+)\s*\]", s).groups()
    b = arb(m) + arb(r); return float(np.nextafter(float(b.upper()), np.inf))


def files(tag):
    if tag == "":
        return dict(scalars="runs/scalars_full.json", middle="runs/cert_resid_middle.json", regions="runs/cert_resid_regions.json",
                    tail="runs/cert_tail.json", itail="runs/cert_inner_tail.json", label="X3 trial (h = 0.008, M = 260)")
    lab = {"v3_h0.004": "v3 (h = 0.004)", "v4_M230": "v4 (M = 230)", "v5_R0knot2": "v5 (knot scheme 2, R0 = 1468)", "n7": "N7 (centre-regular)"}.get(tag, tag)
    return dict(scalars="runs/scalars_%s.json" % tag, middle="runs/cert_resid_middle_%s.json" % tag, regions="runs/cert_resid_regions_%s.json" % tag,
                tail="runs/cert_tail_%s.json" % tag, itail="runs/cert_inner_tail_%s.json" % tag, label=lab)


def middle_arrays(d):
    rows = d["rows"]
    ra = np.exp(np.array([r["t_a"] for r in rows]))
    rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rows])
    Wm = np.array([r["W_over_m"] for r in rows]); W = np.array([r["W"] for r in rows]); L2 = np.array([r["L2piece"] for r in rows])
    W5 = np.array([up(Wm[i] * wfac(rb[i], 0.5)) for i in range(len(rows))]); Wg = np.array([up(Wm[i] * wfac(rb[i], GK)) for i in range(len(rows))])
    return rows, ra, rb, Wm, W, L2, W5, Wg


def shell_table(tag=""):
    f = files(tag); d = jload(f["middle"]); rows, ra, rb, Wm, W, L2, W5, Wg = middle_arrays(d)
    R0 = float(rb[-1])
    shells = [(ra[0], 0.0156), (0.0156, 0.0625), (0.0625, 0.25), (0.25, 1), (1, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, R0)]
    lines = ["| shell of r (cells meeting it) | max W/m (divisor) | at r | max W (1+u)^{1/2}/m | max W (1+u)^{1/2-k}/m | max W (absolute) | sum of L2 pieces |", "|---|---|---|---|---|---|---|"]
    for lo, hi in shells:
        m = (rb > lo) & (ra < hi)
        i = np.argmax(np.where(m, Wm, -1))
        lab = "[%s, %s)" % (near(lo, 4) if lo != ra[0] else "rmin = 0.0076514", near(hi, 4) if hi != R0 else "R0 = 3413.0")
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (lab, ceil_sig(Wm[m].max(), 5), near(ra[i], 4), ceil_sig(W5[m].max(), 5), ceil_sig(Wg[m].max(), 5), ceil_sig(W[m].max(), 4), ceil_sig(osum(L2[m]), 4)))
    i = int(np.argmax(Wm)); mP = (rb > XSTAR / 2) & (ra < 2 * XSTAR)
    summary = ("Whole middle region [rmin, R0] = [%s, %s] (%d sub-cells): sup W/m <= %s, attained on the cell r in [%s, %s] (the lobe next to P; the P-shell "
               "[x_*/2, 2 x_*] has the same maximum, %s); multiplier forms sup W (1+u)^{1/2}/m <= %s and sup W (1+u)^{1/2-k}/m <= %s (same cell); sup W <= %s; "
               "sum of the L2 pieces <= %s. Taylor remainders: eps <= %s, A <= %s, B <= %s." % (
                   near(ra[0], 6), near(R0, 6), len(rows), ceil_sig(Wm.max(), 5), near(ra[i], 5), near(rb[i], 5), ceil_sig(Wm[mP].max(), 5), ceil_sig(W5.max(), 5), ceil_sig(Wg.max(), 5),
                   ceil_sig(W.max(), 5), ceil_sig(osum(L2), 5), ceil_sig(max(r["rem_eps"] for r in rows), 3), ceil_sig(max(r["remA"] for r in rows), 2), ceil_sig(max(r["remB"] for r in rows), 2)))
    return "\n".join(lines), summary


def region_table(tag=""):
    f = files(tag); rows = jload(f["regions"])["rows"]; tail = jload(f["tail"]); itail = jload(f["itail"])
    out = {}
    for region in ("outer", "inner"):
        rr = [r for r in rows if r["region"] == region]
        ra = np.array([r["r_a"] for r in rr]); Wm = np.array([r["W_over_m"] for r in rr]); Wf = np.array([r["W_over_m_far"] for r in rr]); L2 = osum([r["L2piece"] for r in rr])
        rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rr])
        Wg = np.array([up(Wm[i] * wfac(rb[i], GK)) for i in range(len(rr))])
        out[region] = dict(n=len(rr), rmin=ra.min(), rmax=rb.max(), Wm=Wm.max(), r_Wm=ra[np.argmax(Wm)], Wf=Wf.max(), r_Wf=ra[np.argmax(Wf)], Wg=Wg.max(), r_Wg=ra[np.argmax(Wg)], L2=L2,
                           rem_eps=max(r["rem_eps"] for r in rr), remA=max(r["remA"] for r in rr), remB=max(r["remB"] for r in rr))
        if region == "inner": out[region]["W5"] = max(r["W_over_r5"] for r in rr); out[region]["r_W5"] = ra[np.argmax([r["W_over_r5"] for r in rr])]
    o, i_ = out["outer"], out["inner"]
    rT = tail["r_T"]; rTi = itail["r_T"]
    lines = ["| region (cells) | sup W/m (divisor) | at r | sup W (1+u)^{1/2}/m | at r | sup W (1+u)^{1/2-k}/m | at r | sum of L2 pieces |", "|---|---|---|---|---|---|---|---|"]
    lines.append("| outer: R0 <= r <= %s = r_T,out (%d) | %s | %s | %s | %s | %s | %s | %s |" % (near(o["rmax"], 5), o["n"], ceil_sig(o["Wm"], 5), near(o["r_Wm"], 4), ceil_sig(o["Wf"], 5), near(o["r_Wf"], 4), ceil_sig(o["Wg"], 5), near(o["r_Wg"], 4), ceil_sig(o["L2"], 4)))
    r2 = jload("runs/r2_tails%s.json" % (("_" + tag) if tag else ""))
    def r2ceil(key):
        if not r2: return "(run r2_tails.py)"
        v = r2[key]; v = float(re.match(r"\[?\s*([-0-9.eE+]+)", v).group(1)) * (1 + 1e-7) if isinstance(v, str) else float(v)
        return "<= " + ceil_sig(v, 3)
    tail05 = jload("runs/cert_tail%s_d05.json" % (("_" + tag) if tag else ""))
    lines.append("| outer tail r >= r_T,out = %s (termwise majorant) | %s | - | %s | - | %s | - | %s (r2_tails, norm^2) |" % (
        near(rT, 6), ceil_sig(ball_upper(tail["tail_bound_unweighted"]), 5), ceil_sig(ball_upper(tail05["tail_bound_weighted"]), 5) if tail05 else "-", ceil_sig(ball_upper(tail["tail_bound_weighted"]), 5), r2ceil("outer_tail_sq_upper")))
    lines.append("| inner: r_T,in <= r <= rmin (%d) | %s | %s | %s | %s | %s | %s | %s |" % (i_["n"], ceil_sig(i_["Wm"], 5), near(i_["r_Wm"], 4), ceil_sig(i_["Wf"], 5), near(i_["r_Wf"], 4), ceil_sig(i_["Wg"], 5), near(i_["r_Wg"], 4), ceil_sig(i_["L2"], 4)))
    lines.append("| inner tail r <= r_T,in = %s (termwise majorant) | %s (W/r^5 <= %s) | - | - | - | - | - | %s (r2_tails, norm^2) |" % (
        near(rTi, 6), ceil_sig(ball_upper(itail["bound_W_over_m"]), 4), ceil_sig(ball_upper(itail["bound_W_over_r5"]), 4), r2ceil("inner_tail_sq_upper")))
    notes = ("Outer-region Taylor remainders: eps <= %s, A <= %s, B <= %s; inner: eps <= %s, A <= %s, B <= %s. Inner R4: sup W/r^5 <= %s at r = %s (cells) and <= %s on the inner tail." % (
        ceil_sig(o["rem_eps"], 2), ceil_sig(o["remA"], 2), ceil_sig(o["remB"], 2), ceil_sig(i_["rem_eps"], 2), ceil_sig(i_["remA"], 2), ceil_sig(i_["remB"], 2), ceil_sig(i_["W5"], 5), near(i_["r_W5"], 4), ceil_sig(ball_upper(itail["bound_W_over_r5"]), 4)))
    return "\n".join(lines), notes, out, tail, itail


def variants_table(tags):
    cols = []
    for tag in tags:
        f = files(tag); s = jload(f["scalars"]); d = jload(f["middle"]); reg = jload(f["regions"]); tail = jload(f["tail"]); itail = jload(f["itail"])
        c = dict(label=f["label"])
        if s:
            c["x_*"] = "%s +/- %s" % (near(s["x_star_mid"], 16), ceil_sig(s["x_star_rad"], 2))
            c["mu~ - 1"] = "[%s, %s]" % (floor_sig(s["mu_minus_1"][0], 6), ceil_sig(s["mu_minus_1"][1], 6))
            c["g = rho~_y(P)"] = "[%s, %s]" % (floor_fix(s["g_star"][0], 12), ceil_fix(s["g_star"][1], 12))
            c["w'(P)"] = "[%s, %s]" % (floor_fix(s["w_prime_P"][0], 12), ceil_fix(s["w_prime_P"][1], 12))
        if d:
            rows, ra, rb, Wm, W, L2, W5, Wg = middle_arrays(d)
            c["middle cells (approximate r range)"] = "%d ([%s, %s])" % (len(rows), near(ra[0], 5), near(rb[-1], 5))
            c["middle sup W/m (lobe next to P)"] = ceil_sig(Wm.max(), 5); c["middle sup W (1+u)^{1/2}/m"] = ceil_sig(W5.max(), 5); c["middle sup W (1+u)^{1/2-k}/m"] = ceil_sig(Wg.max(), 5)
            c["middle sup W"] = ceil_sig(W.max(), 5); c["middle sum of L2 pieces"] = ceil_sig(osum(L2), 4)
        if reg:
            for region in ("outer", "inner"):
                rr = [r for r in reg["rows"] if r["region"] == region]
                if not rr: continue
                ra = np.array([r["r_a"] for r in rr]); Wm = np.array([r["W_over_m"] for r in rr]); Wf = np.array([r["W_over_m_far"] for r in rr])
                rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rr]); Wg = np.array([up(Wm[i] * wfac(rb[i], GK)) for i in range(len(rr))])
                c["%s cells (approximate r range)" % region] = "%d ([%s, %s])" % (len(rr), near(ra.min(), 5), near(rb.max(), 5))
                c["%s sup W/m" % region] = ceil_sig(Wm.max(), 5); c["%s sup W (1+u)^{1/2}/m" % region] = ceil_sig(Wf.max(), 5); c["%s sup W (1+u)^{1/2-k}/m" % region] = ceil_sig(Wg.max(), 5)
                c["%s sum of L2 pieces" % region] = ceil_sig(osum([r["L2piece"] for r in rr]), 4)
        if tail: c["outer tail sup W (1+u)^{1/2-k}/m"] = ceil_sig(ball_upper(tail["tail_bound_weighted"]), 4); c["outer tail sup W/m"] = ceil_sig(ball_upper(tail["tail_bound_unweighted"]), 4)
        if itail: c["inner tail sup W/m"] = ceil_sig(ball_upper(itail["bound_W_over_m"]), 4); c["inner tail sup W/r^5"] = ceil_sig(ball_upper(itail["bound_W_over_r5"]), 4)
        cols.append(c)
    keys = ["x_*", "mu~ - 1", "g = rho~_y(P)", "w'(P)", "middle cells (approximate r range)", "middle sup W/m (lobe next to P)", "middle sup W (1+u)^{1/2}/m", "middle sup W (1+u)^{1/2-k}/m", "middle sup W",
            "middle sum of L2 pieces", "outer cells (approximate r range)", "outer sup W/m", "outer sup W (1+u)^{1/2}/m", "outer sup W (1+u)^{1/2-k}/m", "outer sum of L2 pieces", "inner cells (approximate r range)", "inner sup W/m",
            "inner sup W (1+u)^{1/2}/m", "inner sup W (1+u)^{1/2-k}/m", "inner sum of L2 pieces", "outer tail sup W (1+u)^{1/2-k}/m", "outer tail sup W/m", "inner tail sup W/m", "inner tail sup W/r^5"]
    lines = ["| quantity (upper bounds rounded up, interval endpoints outward; the r-range endpoints are approximate locations, not bounds) | " + " | ".join(c["label"] for c in cols) + " |", "|---|" + "---:|" * len(cols)]
    for k in keys: lines.append("| %s | " % k + " | ".join(c.get(k, "-") for c in cols) + " |")
    return "\n".join(lines)


if __name__ == "__main__" and "--deriv" not in sys.argv and "--n8" not in sys.argv:
    tags = sys.argv[1:] if len(sys.argv) > 1 else ["", "v3_h0.004", "v4_M230", "v5_R0knot2"]
    st, ssum = shell_table("")
    print("## 7.3 middle shells (X3 trial)\n" + st + "\n\n" + ssum + "\n")
    rt, rnotes, out, tail, itail = region_table("")
    print("## 7.3 regions and tails (X3 trial)\n" + rt + "\n\n" + rnotes + "\n")
    print("## 7.3c three resolutions\n" + variants_table(tags))


# ---------------- 7.3b derivative certificate tables (directed ceilings) ----------------
DER_KEYS = ["W_0_0", "W_1_0", "W_0_1", "W_2_0", "W_1_1", "W_0_2", "W_eps_minus_dteps", "W_K", "W_dtK"]


def deriv_shell_table(path="runs/cert_deriv_middle.json", shells=None, sig=3):
    """per-shell ceilings of W_i_j / m_inf (cells meeting each shell); W_K, W_dtK with 4 significant digits."""
    d = jload(path); rows = d["rows"]
    ra = np.exp(np.array([r["t_a"] for r in rows])); rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rows])
    m = np.array([r["m_inf"] for r in rows])
    if shells is None:
        R0 = float(rb[-1]); shells = [(ra[0], 0.0156), (0.0156, 0.0625), (0.0625, 0.25), (0.25, 1), (1, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, R0)]
    hdr = "| shell of r (cell starts) | " + " | ".join(("%s/m" % key).replace("W_eps_minus_dteps", "W_F") for key in DER_KEYS) + " |"
    lines = [hdr, "|---|" + "---|" * len(DER_KEYS)]
    for lo, hi in shells:
        sel = (ra >= lo) & (ra < hi)          # left-end (cell start) convention, as in src/cert_deriv_summary.py and the 7.3b tables
        vals = []
        for key in DER_KEYS:
            v = np.array([up(r[key] / mm) for r, mm in zip(rows, m)])[sel]      # outward division
            vals.append(ceil_sig(v.max(), 4 if key in ("W_K", "W_dtK") else sig))
        lab = "[%s, %s)" % (near(lo, 4) if lo != ra[0] else "rmin", near(hi, 4) if hi != shells[-1][1] else "R0")
        lines.append("| %s | " % lab + " | ".join(vals) + " |")
    return "\n".join(lines)


def deriv_sups(path="runs/cert_deriv_middle.json"):
    """global ceilings used in the R1/R5 text: sup r|grad eps|/m <= (W_1_0 + W_0_1)/m, sup r^2|D^2 eps|/m <= (W_2_0 + 2 W_1_1 + W_0_2 + W_1_0 + 2 W_0_1)/m,
    per shell [4,16) and outside it; plus the P-disc absolute maxima (377 cells with nder = 5)."""
    d = jload(path); rows = d["rows"]
    ra = np.exp(np.array([r["t_a"] for r in rows])); rb = np.array([float(np.nextafter(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()), np.inf)) for r in rows])
    g1 = np.array([up(up(r["W_1_0"] + r["W_0_1"]) / r["m_inf"]) for r in rows])
    g2 = np.array([up(up(up(up(r["W_2_0"] + 2 * r["W_1_1"]) + r["W_0_2"]) + up(r["W_1_0"] + 2 * r["W_0_1"])) / r["m_inf"]) for r in rows])
    lobe = (rb > 4) & (ra < 16)
    out = dict(grad_all=ceil_sig(g1.max(), 4), grad_r=near(ra[np.argmax(g1)], 4), D2_all=ceil_sig(g2.max(), 4), D2_r=near(ra[np.argmax(g2)], 4),
               grad_off_lobe=ceil_sig(g1[~lobe].max(), 4), D2_off_lobe=ceil_sig(g2[~lobe].max(), 4),
               F_over_m=ceil_sig(max(up(r["W_eps_minus_dteps"] / r["m_inf"]) for r in rows), 5), K_over_m=ceil_sig(max(up(r["W_K"] / r["m_inf"]) for r in rows), 5),
               dtK_over_m=ceil_sig(max(up(r["W_dtK"] / r["m_inf"]) for r in rows), 5))
    pd = [r for r in rows if r.get("nder", 2) >= 5]
    keys = ["W_%d_%d" % (i, j) for s in range(6) for i in range(s, -1, -1) for j in [s - i]]
    out["pdisc_cells"] = len(pd); out["pdisc_r_range"] = (near(min(np.exp(r["t_a"]) for r in pd), 4), near(max(float((arb(r["t_a"]) + arb(r["h"])).exp().upper()) for r in pd), 4))
    out["pdisc"] = {key: ceil_sig(max(r[key] for r in pd), 3) for key in keys if key in pd[0]}
    out["pdisc_K"] = ceil_sig(max(r["W_K"] for r in pd), 3); out["pdisc_dtK"] = ceil_sig(max(r["W_dtK"] for r in pd), 3)
    out["pdisc_rem"] = {("rem_eps_%d" % i): ceil_sig(max(r["rem_eps_%d" % i] for r in pd), 2) for i in range(6)}
    return out


if __name__ == "__main__" and "--deriv" in sys.argv and "--n8" not in sys.argv:
    print("## 7.3b middle shells (derivative certificate; ceilings)\n" + deriv_shell_table() + "\n")
    print(json.dumps(deriv_sups(), indent=1))


# ---------------- 7.7a N8 table (directed ceilings) ----------------
def n8_table():
    rows = [("0.0165 (fine)", "runs/n8/cert_n8_fine0165.json", "0.0165"), ("0.05", "runs/n8/cert_n8_full.json", "0.05"), ("0.1", "runs/n8/cert_n8_full.json", "0.1"),
            ("0.2", "runs/n8/cert_n8_full.json", "0.2"), ("0.05 (mid)", "runs/n8/cert_n8_mid.json", "0.05"), ("0.06 (mid)", "runs/n8/cert_n8_mid.json", "0.06"), ("0.07 (mid)", "runs/n8/cert_n8_mid.json", "0.07")]
    lines = ["| delta | cells counted | M_V = sup\\|D^2 V\\|_F | sup\\|D^3 V\\|_F | sup\\|D^4 V\\|_F | M_rho = sup\\|D^2 rho~\\|_F | sup\\|D^3 rho~\\|_F | sup\\|D^4 rho~\\|_F | sup\\|D^5 rho~\\|_F | sup\\|DV\\|_F | C_V | kappa_loc/(2 delta) (rounded down) | |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    out = {}
    for lab, f, key in rows:
        d = jload(f)["deltas"][key]; sb = d["sup_bounds"]; thr = 3.374 / (2 * float(key))
        vals = [ceil_sig(sb["V2"], 5), ceil_sig(sb["V3"], 5), ceil_sig(sb["V4"], 5), ceil_sig(sb["rho2"], 5), ceil_sig(sb["rho3"], 5), ceil_sig(sb["rho4"], 5), ceil_sig(sb["rho5"], 5), ceil_sig(sb["V1"], 6), ceil_sig(d["C_V"], 4), floor_sig(thr, 5)]
        lines.append("| %s | %d | %s | %s |" % (lab, d["ncells"], " | ".join(vals), "OK" if d["C_V_ok"] else "FAIL"))
        out[lab] = dict(C_V=d["C_V"], C_V_ceil=ceil_sig(d["C_V"], 4), E_ceil=ceil_sig(d["C_V"] * float(key), 4), M_V=ceil_sig(sb["V2"], 5), M_rho=ceil_sig(sb["rho2"], 5))
    return "\n".join(lines), out


if __name__ == "__main__" and "--n8" in sys.argv:
    t, o = n8_table(); print("## 7.7a N8 table (ceilings)\n" + t + "\n"); print(json.dumps(o, indent=1))
