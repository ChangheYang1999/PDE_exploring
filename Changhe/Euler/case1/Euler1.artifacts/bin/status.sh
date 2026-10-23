#!/bin/bash
# One-screen status: runner, queue, running experiments, ledger active hours.
P=$(cd "$(dirname "$0")/.." && pwd)
cd "$P"
echo "== $(date -u +%FT%TZ)  runner: $( [ -f runner.pid ] && kill -0 "$(cat runner.pid)" 2>/dev/null && echo "alive pid $(cat runner.pid)" || echo "NOT running" )  STOP file: $( [ -e STOP ] && echo yes || echo no )"
python3 - <<'PY'
import json, os, glob
P = os.getcwd()
try:
    s = json.load(open("runner_status.json"))
    print("runner_status:", s.get("runner"), "at", s.get("time"), "| pending:", len(s.get("pending", [])), "done:", s.get("done"), "failed:", s.get("failed"))
    for r in s.get("running", []):
        lv = r.get("last_val") or {}
        print("  RUN %-34s gpu %s pid %s stage %s step %s active %.2fh best %s nonaxi %s maxU %s R50 %s tail %s" % (
            r["exp_id"], r["gpu"], r["pid"], r.get("stage"), r.get("step"), r.get("active_h") or 0,
            "%.2e" % r["best_val"] if r.get("best_val") not in (None, float("inf")) else "-",
            "%.2e" % lv["nonaxi_ratio_core"] if lv.get("nonaxi_ratio_core") is not None else "-",
            "%.3f" % lv["max_U_sampled"] if lv.get("max_U_sampled") is not None else "-",
            "%.3f" % lv["core_R50_vort"] if lv.get("core_R50_vort") is not None else "-",
            "%.3f" % lv["tail_slope_U"] if lv.get("tail_slope_U") is not None else "-"))
    print("  pending:", ", ".join(s.get("pending", [])[:12]))
except Exception as e:
    print("no runner status:", e)
PY
python3 "$P/ledger.py" | head -40
echo "disk: $(du -sh "$P" 2>/dev/null | cut -f1) project; $(df -h "$P" | tail -1 | awk '{print $4" free"}')"
