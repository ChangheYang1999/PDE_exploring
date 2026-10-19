"""Summary of a soft-tangent run (soft_tangent.py jsonl, dwr_eval.py jsonl, quick_scan json of the tangent shapes).
Usage: python3 tan_summary.py PREFIX   (e.g. tan_c6b; reads PREFIX_tangent.jsonl, PREFIX_g*_dwr.jsonl, PREFIX_tan*_scan.json)"""
import sys
import json
import glob


def lines(fn):
    out = []
    for ln in open(fn):
        try:
            out.append(json.loads(ln))
        except ValueError:
            pass
    return out


pre = sys.argv[1]
ev = lines(pre + "_tangent.jsonl")
for d in ev:
    if d["event"] == "start":
        print("start c0 %.9f nr %d nt %d norm %.4e hP-1 %+.2e" % (d["c0"], d["nr"], d["nt"], d["norm"], d["hP1"]))
    elif d["event"] == "k_column":
        print("k column: |Fk| %.4e FD rel diff %.2e" % (d["norm_Fk"], d["rel_diff"]))
    elif d["event"] == "check":
        print("it %5d |s| %.4e sigma/cl %.4e dcl* %+.3e m_lin_min/m0 %.6f wall %.0f" % (
            d["it"], d["norm_r"], d["sigma_per_cl"], d["dcl_star"], d["m_lin_min"] / d["m0"], d.get("wall", 0)))
        if "m_nonlinear" in d:
            for dc, inf in d["m_nonlinear"].items():
                print("     dc %+.0e  m_lin %.4e  m_nl %.4e  transport %.4e  hP-1 %+.2e  E %+.1e  D2 %+.1e" % (
                    float(dc), d["m_lin"][dc], inf["norm"], inf["transport"], inf["hP1"], inf["E"], inf["D2"]))
for fn in sorted(glob.glob(pre + "_g*_dwr.jsonl")):
    print(fn)
    for d in lines(fn):
        if d["event"] == "start":
            print("  start nr %d nt %d norm %.4e hP-1 %+.2e" % (d["nr"], d["nt"], d["norm_f"], d["hP1"]))
        elif d["event"] == "check":
            sp = " ".join("%s %+.2e" % (k, v) for k, v in d["split"].items())
            print("  it %4d |s| %.4e sigma/cl %.4e dcl %+.3e stat %.3f/%.4f m_min %.6e | %s" % (
                d["it"], d["norm_s"], d["sigma_per_cl"], d["dcl"], d["stationarity"], d["stationarity_rms"],
                d["m_min"], sp))
            if "s2_fraction" in d:
                print("       |s|^2 fractions: " + " ".join("%s %.3f" % (k, v) for k, v in d["s2_fraction"].items()))
for fn in sorted(glob.glob(pre + "_tan*_scan.json"), key=lambda f: float(f.split("_tan")[-1].split("_scan")[0])):
    d = json.load(open(fn)); b = d["bands"]
    g = lambda k, q: b.get(k, {}).get(q, float("nan"))
    print("%-28s cl %.8f hP-1 %+.2e | 2-10 flux %.2e N4 %.2e | 0.1-2 %.2e | 10-100 %.2e | 100-1e3 %.2e | rms %.2e" % (
        fn, d["cl"], d["hP"] - 1, g("2<=r<=10/all", "max"), g("2<=r<=10/all", "N4_max"), g("0.1<=r<=2/all", "max"),
        g("10<=r<=100/all", "max"), g("100<=r<=1000/all", "max"), g("all/all", "rms")))
