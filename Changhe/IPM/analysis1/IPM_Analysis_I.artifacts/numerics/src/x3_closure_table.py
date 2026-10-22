"""Far-field closure test of the X3 residual table (lead 13:17Z (b)): relative change of every sampled maximum (per region and column) between the
base evaluation (16875 x 512, 1e-4 L <= r <= 1e6 L, four-power far continuation fitted on the last decade) and the variants: outer extent 1e5 L and
1e7 L; far continuation by the exact leading power r^{k-1} only ('lead'); fit window of two decades ('tail2dec'). Reads runs/closure/*.json.
The outer-extent variants come in two forms: ALIGNED grids (same spacing and inner end as the base, so the sample radii coincide and the change is
the closure effect alone) and SHIFTED grids (same Nr over the new range, so the sample radii move; the change then includes the sampling of the
knot-scale lobe near P). Usage: python3 src/x3_closure_table.py > runs/closure/closure_table.md"""
import json
base = json.load(open("runs/closure/resid_N16875_q512_base.json")); B = base["results"]["stored"]
variants = [("rmax1e5a", "outer extent 1e5 L (aligned grid, Nr 15188)"), ("rmax1e7a", "outer extent 1e7 L (aligned grid, Nr 18562)"), ("taillead", "far continuation r^{k-1} only"), ("tail2dec", "fit window 2 decades"),
            ("rmax1e5", "outer extent 1e5 L (shifted grid, Nr 16875)"), ("rmax1e7", "outer extent 1e7 L (shifted grid, Nr 16875)")]
files = {"rmax1e5a": "runs/closure/resid_N15188_q512_rmax1e5a.json", "rmax1e7a": "runs/closure/resid_N18562_q512_rmax1e7a.json"}
for key, l in variants: files.setdefault(key, "runs/closure/resid_N16875_q512_%s.json" % key)
cols = [("Nf_max_cut", "max |eps|/N_f (cut)"), ("Nv_max_cut", "max |eps|/N_v (cut)"), ("abs_max", "max |eps|")]
print("Base: Nr %d, Nt %d, r in [%.4g, %.4g], tail powers %s on the last %.1f decade(s); c = psi_xy(0) = %.12f, x_* = %.9f." % (base["Nr"], base["Nt"], base["rmin"], base["rmax"], base["tailmode"], base["tail_decades"], base["c"], B["x_star"]))
for key, label in variants:
    d = json.load(open(files[key])); V = d["results"]["stored"]
    print("%s: Nr %d, r in [%.4g, %.4g], tail %s / %.1f decades; c = %.12f (change %.2e), x_* = %.9f (change %.2e)" % (label, d["Nr"], d["rmin"], d["rmax"], d["tailmode"], d["tail_decades"], d["c"], d["c"] - base["c"], V["x_star"], V["x_star"] - B["x_star"]))
print("\n| region | column | base value @ (r, theta) | " + " | ".join("rel. change: " + l for k, l in variants) + " |")
print("|---|---|---|" + "---|" * len(variants))
Bd = {row["region"]: row for row in B["rows"]}
Vd = {key: {row["region"]: row for row in json.load(open(files[key]))["results"]["stored"]["rows"]} for key, l in variants}
for region in Bd:
    for ck, cl in cols:
        b = Bd[region][ck]; cells = []
        for key, l in variants:
            if region not in Vd[key]: cells.append("n/a"); continue
            v = Vd[key][region][ck]
            same = abs(v[1] - b[1]) / max(b[1], 1e-300) < 0.05 and abs(v[2] - b[2]) < 0.05
            cells.append("%+.2e%s" % ((v[0] - b[0]) / max(abs(b[0]), 1e-300), "" if same else " (moved to r=%.4g, th=%.3f)" % (v[1], v[2])))
        print("| %s | %s | %.3e @ (%.5g, %.4f) | %s |" % (region, cl, b[0], b[1], b[2], " | ".join(cells)))
