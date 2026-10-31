#!/bin/bash
# Manual recovery of a deadlocked governor barrier (lead 17:18:08Z item 2 option (b); V385 item 3): the acknowledgment is set only when the supervisor has READ the closed
# configuration causally after the current closure: the supervisor heartbeat epoch (written at every poll, after re-reading the configuration) is later than the closure
# epoch AND the configuration file still lists no GPU. Each action is logged with the evidence. Runs for at most <seconds> (default 240), polling every 5 s; stops when the
# governor has published (the configuration lists GPUs again). Usage: bash scripts/governor_manual_ack.sh [seconds]
cd "$(dirname "$0")/.."; PY=python3; T=${1:-240}; LOG=logs/governor_manual_ack.log; t0=$(date +%s)
while [ $(( $(date +%s) - t0 )) -lt "$T" ]; do
  R=$($PY - <<'PYEOF'
import json, time
st = json.load(open("status/slot_governor_state.json")); hb = json.load(open("status/supervisor_heartbeat.json")); cfg = json.load(open("configs/supervisor_gpu456.json"))
if cfg.get("gpus"):
    print("PUBLISHED gpus " + str(cfg["gpus"])); raise SystemExit
if st.get("closed") and not st.get("acked") and st.get("closure_epoch") and float(hb["epoch"]) > float(st["closure_epoch"]):
    st["acked"] = True; st["manual_ack"] = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), evidence=f"supervisor heartbeat {hb['ts']} (epoch {hb['epoch']}) later than the closure epoch {st['closure_epoch']} with the configuration listing no GPU: the supervisor read the closed configuration after the closure", rule="lead 17:18:08Z item 2 option (b); V385 item 3")
    json.dump(st, open("status/slot_governor_state.json", "w"), indent=1); print("ACKED " + st["manual_ack"]["evidence"])
else:
    print("WAIT closed=%s acked=%s hb=%s closure=%s" % (st.get("closed"), st.get("acked"), hb.get("ts"), st.get("closure_epoch")))
PYEOF
)
  echo "$(date -u +%FT%TZ) $R" >> $LOG
  case "$R" in PUBLISHED*) exit 0;; esac
  sleep 5
done
echo "$(date -u +%FT%TZ) timeout after $T s" >> $LOG
