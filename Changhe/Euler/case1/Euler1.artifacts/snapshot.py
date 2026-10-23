#!/usr/bin/env python3
"""Aggregate the latest and best holdout metrics of every run into a table (markdown) for progress snapshots.
Usage: python3 snapshot.py [--out reports/snapshot_XXh.md] [--title ...]"""
import argparse, glob, json, os, time
P = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("--out", default=None); ap.add_argument("--title", default="Progress snapshot")
a = ap.parse_args()
import sys; sys.path.insert(0, P)
from ledger import summarize
L = summarize()
rows = []
for vl in sorted(glob.glob(os.path.join(P, "runs", "*", "val.jsonl"))):
    eid = os.path.basename(os.path.dirname(vl))
    lines = [json.loads(l) for l in open(vl) if l.strip()]
    if not lines:
        continue
    last = lines[-1]; best = min(lines, key=lambda r: r.get("val_score", float("inf")))
    st = {}
    sp = os.path.join(P, "runs", eid, "status.json")
    if os.path.exists(sp):
        st = json.load(open(sp))
    rows.append((eid, st.get("state", "?"), last.get("cl"), last.get("global_step"), round((st.get("active_seconds") or 0) / 3600, 2),
                 last.get("eps_m_D1_R<1"), last.get("eps_m_D2_1-3"), last.get("eps_m_D3_3-10"), last.get("eps_nl_D4_10-100"), last.get("eps_nl_D5_100-1e3"),
                 last.get("nonaxi_ratio_core"), last.get("ring_n2"), last.get("ring_n4"), last.get("stag_n_zeros"), last.get("stag_min_abs_eig_gradV"),
                 last.get("affine_resid_frac_core"), last.get("vort_frac_core"), last.get("max_U_sampled"), last.get("core_R50_vort"), last.get("tail_slope_U"),
                 last.get("stretch_at_max"), last.get("inversion_defect_core"), best.get("val_score"), best.get("global_step")))
hdr = ["exp_id", "state", "c_l(fixed)", "step", "act_h", "eps_m D1", "eps_m D2", "eps_m D3", "eps_nl D4", "eps_nl D5", "nonaxi", "ring n2", "ring n4", "zeros", "min|eig gradV|",
       "affine resid", "vort frac", "max|U|", "R50", "tail slope", "stretch", "inv defect", "best nl-rms", "best step"]
def fmt(v):
    if v is None: return "-"
    if isinstance(v, float):
        return ("%.2e" % v) if (abs(v) < 1e-2 or abs(v) >= 1e3) else ("%.3f" % v)
    return str(v)
out = ["# %s\n" % a.title, "Generated %s. Ledger non-overlapping active hours: %.2f (worker-sum %.2f, %d records)." % (
    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), L["active_hours_union"], L["worker_hours_sum"], L["records"]),
    "", "All c_l values are fixed inputs unless the run id contains 'clfree'. Residual columns are holdout (untouched) metrics at the LAST validation;",
    "eps_m(D) = term-normalized relative momentum residual (physical L2) on D1: R<1, D2: 1<R<3, D3: 3<R<10; eps_nl(D) = ||R_m||/(||U.grad U||+||grad P||)",
    "on D4: 10<R<100, D5: 100<R<1e3 (nonlinear-scale tail check). 'zeros' = stagnation points of V found by Newton in the core. None of these numbers is a candidate claim.", "",
    "| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
for r in rows:
    out.append("| " + " | ".join(fmt(v) for v in r) + " |")
txt = "\n".join(out) + "\n"
if a.out:
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True); open(a.out, "w").write(txt); print("wrote", a.out)
else:
    print(txt)
