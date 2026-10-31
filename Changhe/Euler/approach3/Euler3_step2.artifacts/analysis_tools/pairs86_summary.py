#!/usr/bin/env python3
"""Summarize the 8.6 pairwise field distances (lead copy of branch_distance v6; not an independent check).
Usage: python3 tools/pairs86_summary.py <tag-prefix> [extra tags...] -> prints a table and writes artifacts/branch_field/<prefix>summary.json"""
import json, glob, sys, os, hashlib
pre = sys.argv[1]
tags = sorted(os.path.basename(p)[:-5] for p in glob.glob("artifacts/branch_field/%s*_n6.json" % pre)) + sys.argv[2:]
rows = []
for t in tags:
    p = "artifacts/branch_field/%s.json" % t
    d = json.load(open(p)); f = d["field"]
    rows.append(dict(tag=t, sha256=hashlib.sha256(open(p, "rb").read()).hexdigest(), a=(d["a"]["c_l"], d["a"]["omega"]),
                     b=(d["b"]["c_l"], d["b"]["omega"]), d_ab=f["d_ab"], d_ba=f["d_ba"], d_max=f["d_max"],
                     worst_ab=f.get("worst_shell_ab"), worst_ba=f.get("worst_shell_ba"),
                     min_shell=min(min(s["ratio_ab"], s["ratio_ba"]) for s in f["shells"]),
                     agreement=f["agreement"], decision=d["decision"]))
    r = rows[-1]
    print("%-32s d_ab %.4f d_ba %.4f max %.4f worst %s/%s min shell ratio %.4f %s" % (t, r["d_ab"], r["d_ba"], r["d_max"], r["worst_ab"], r["worst_ba"], r["min_shell"], r["decision"]))
json.dump(rows, open("artifacts/branch_field/%ssummary.json" % pre, "w"), indent=1)
