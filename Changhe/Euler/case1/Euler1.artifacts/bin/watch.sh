#!/bin/bash
# Compact trend view: last N validations of every run (default 3). Usage: bin/watch.sh [N] [pattern]
P=$(cd "$(dirname "$0")/.." && pwd); N=${1:-3}; PAT=${2:-}
python3 - "$P" "$N" "$PAT" <<'PY'
import json, glob, os, sys
P, N, PAT = sys.argv[1], int(sys.argv[2]), sys.argv[3]
for vl in sorted(glob.glob(os.path.join(P, "runs", "*", "val.jsonl"))):
    eid = os.path.basename(os.path.dirname(vl))
    if PAT and PAT not in eid: continue
    rows = [json.loads(l) for l in open(vl) if l.strip()]
    if not rows: continue
    st = {}
    sp = os.path.join(P, "runs", eid, "status.json")
    if os.path.exists(sp): st = json.load(open(sp))
    print("%-24s %-8s cl=%.3f stage %s" % (eid, st.get("state", "?"), rows[-1]["cl"], st.get("stage")))
    for r in rows[-N:]:
        print("   step %6d  nl-rms %.2e  eps_m D1/D2/D3 %.2e/%.2e/%.2e  eps_nl D4/D5 %.2e/%.2e  nonaxi %.2f n2 %.2f  zeros %s  |U|max %.2f R50 %.2f tail %.3f stretch %.2f" % (
            r["global_step"], r["val_score"], r.get("eps_m_D1_R<1", float("nan")), r.get("eps_m_D2_1-3", float("nan")), r.get("eps_m_D3_3-10", float("nan")),
            r.get("eps_nl_D4_10-100", float("nan")), r.get("eps_nl_D5_100-1e3", float("nan")), r["nonaxi_ratio_core"], r.get("ring_n2", float("nan")), r.get("stag_n_zeros", "-"),
            r["max_U_sampled"], r.get("core_R50_vort", float("nan")), r.get("tail_slope_U", float("nan")), r.get("stretch_at_max", float("nan"))))
PY
