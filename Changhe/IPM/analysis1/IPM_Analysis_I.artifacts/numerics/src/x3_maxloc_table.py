"""Locations (r, theta) of the sampled residual maxima of X3 for every row and column of the independent-evaluator table (lead 13:17Z, format
requirement of FINAL_REPORT section 6). Reads the saved runs/resid_N*_q*.json of src/x3_resid.py (each maximum is stored as [value, r, theta]).
Usage: python3 src/x3_maxloc_table.py runs/resid_N16875_q512.json runs/resid_N22500_q768.json [more...] > runs/x3_maxloc.md"""
import sys, json
files = sys.argv[1:]
cols = [("Nf_max", "max |eps|/N_f"), ("Nf_max_cut", "same, axis columns cut"), ("Nv_max", "max |eps|/N_v"), ("Nv_max_cut", "same, cut"), ("abs_max", "max |eps|")]
for f in files:
    d = json.load(open(f)); R = d["results"]["stored"]
    print("\n### %s: Nr = %d, Nt = %d, r in [%.4g, %.4g], c_l stored %.12f (x_* = %.9f); each cell: value @ (r, theta in rad; theta = pi/2 is the y axis)" % (
        f, d["Nr"], d["Nt"], d["rmin"], d["rmax"], R["c_l"], R["x_star"]))
    print("| region | " + " | ".join(c[1] for c in cols) + " |"); print("|---|" + "---|" * len(cols))
    for row in R["rows"]:
        cells = []
        for key, lab in cols:
            v, r, th = row[key]; cells.append("%.3e @ (%.5g, %.4f)" % (v, r, th))
        print("| %s | %s |" % (row["region"], " | ".join(cells)))
