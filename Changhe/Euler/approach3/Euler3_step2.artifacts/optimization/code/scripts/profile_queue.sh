#!/bin/bash
# PROFILE queue (lead 02:59:34Z, 03:13:16Z items 2-3, 03:23:50Z item 2, 05:16:32Z item (4), 05:26:49Z item 5; V601, V611, V614, V642): the nine SPEC 7.3 (d) PROFILE runs of the
# top-ranked branch P1 s4, ONE AT A TIME, in the lead's order (reference, soft -1, soft +1, stiff -1, stiff +1, soft -2, soft +2, stiff -2, stiff +2), each through
# scripts/enqueue_profile_run.sh v6 under the launcher lock (its gate: no active FIXED-side job; (B + x) / (T_narrow + x) <= 0.15; F / (T_registered + x) >= 0.80; x = 0.80 h for
# the first run, then the largest PROFILE charge so far rounded up to 0.05 h). A refused gate is retried every 300 s. Each run must end (JOB DONE) before the next is tried.
# v3 (06:1xZ; V655): a time refusal at publication ends the sequence; latest_start_utc enforced at actual worker admission (cancel if not running by then). v2 (05:5xZ; lead 05:47:15Z item 4): last start at 16:30:31Z minus x (15:42:31Z for x = 0.80 h).
# Preconditions: status/ORDER_ITEMS_1to3_LAUNCHED (items (1) to (3) of the 05:16:32Z order placed) and status/PROFILE_GO (the verifier's check of gpu_hours v4.8: V642).
# Points: validation/lrs/profile_points_P1s4_lead_7ec7de8d.json (lead notes/profile_points_P1s4.json 7ec7de8db803812e). Usage: bash scripts/profile_queue.sh <gpu>
cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); LOG=validation/logs/l_slot_chain.log; P12=python3; GPU=$1
PTS=validation/lrs/profile_points_P1s4_lead_7ec7de8d.json; [ "$(sha256sum $PTS | cut -c1-16)" = "7ec7de8db803812e" ] || { echo "REFUSED: points file hash"; exit 3; }
while [ ! -f status/ORDER_ITEMS_1to3_LAUNCHED ] || [ ! -f status/PROFILE_GO ]; do sleep 60; done
echo "$(date -u +%FT%TZ) profile_queue: preconditions met; starting the nine PROFILE runs one at a time on GPU $GPU" | tee -a $LOG
XH=0.80; PREV=""
for NAME in reference soft_m1 soft_p1 stiff_m1 stiff_p1 soft_m2 soft_p2 stiff_m2 stiff_p2; do
  read CL OM < <($P12 - "$PTS" "$NAME" <<'PYEOF'
import json, sys
d = json.load(open(sys.argv[1])); nm = sys.argv[2]
if nm == "reference":
    print(repr(d["base"]["c_l"]), repr(d["base"]["omega"]))
else:
    dr, k = nm.split("_"); k = (-1 if k[0] == "m" else 1) * int(k[1:])
    p = [q for q in d["points"] if q["direction"] == dr and q["k"] == k][0]; print(repr(p["c_l"]), repr(p["omega"]))
PYEOF
)
  if [ -n "$PREV" ]; then
    # the previous PROFILE run must have ended; then x = the largest PROFILE charge so far, rounded up to 0.05 h (lead 03:23:50Z (a''))
    while [ ! -f queue/done/${PREV}.json ]; do sleep 60; done
    $P12 scripts/gpu_hours.py > /dev/null 2>&1
    XH=$($P12 -c "
import json, math; d=json.load(open('status/gpu_hours.json')); ch=[r['gpu_hours_charged'] for r in d['rows'] if r.get('label')=='PROFILE' and r.get('end')!='running']
x = math.ceil(max(ch) * 20) / 20 if ch else 0.80; print(f'{x:.2f}')")
  fi
  TAG=prof_P1s4_${NAME}
  while true; do
    # lead 05:47:15Z item 4: a PROFILE run starts only if its full charge allowance x ends by the Phase III end 16:30:31Z (x = 0.80 h -> last start 15:42:31Z); later points are reported as not run for time
    NOW=$(date -u +%s); DEADLINE=$(( $(date -u -d "2026-10-30T16:30:31Z" +%s) - $(python3 -c "print(int(float('$XH')*3600))") ))
    [ "$NOW" -gt "$DEADLINE" ] && { echo "$(date -u +%FT%TZ) profile_queue: $NAME not started: its allowance x = $XH h would end after 16:30:31Z (last start $(date -u -d @$DEADLINE +%FT%TZ)); this and the later points are not run for time (lead 05:47:15Z item 4)" | tee -a $LOG; exit 0; }
    OUT=$(bash scripts/enqueue_under_lock.sh $TAG bash scripts/enqueue_profile_run.sh $NAME $CL $OM $GPU 1 40 1800 $XH 2>&1); rc=$?
    echo "$OUT" | tail -4 | cut -c1-300
    if echo "$OUT" | grep -q "state visible\|admitted job"; then echo "$(date -u +%FT%TZ) profile_queue: $NAME admitted (x $XH h)" | tee -a $LOG; break; fi
    if echo "$OUT" | grep -q "not run for time"; then echo "$(date -u +%FT%TZ) profile_queue: $NAME refused for TIME at publication (v8 gate); this and the later points are not run for time" | tee -a $LOG; exit 0; fi
    if echo "$OUT" | grep -q "REFUSED"; then echo "$(date -u +%FT%TZ) profile_queue: $NAME refused by the gate (x $XH h); retry in 300 s" | tee -a $LOG; sleep 300; continue; fi
    echo "$(date -u +%FT%TZ) profile_queue: $NAME: unexpected enqueue result (rc $rc); retry in 300 s" | tee -a $LOG; sleep 300
  done
  PREV=$(ls queue/running/${TAG}_*.json queue/staged/${TAG}_*.json queue/pending/${TAG}_*.json queue/granted/${TAG}_*.json 2>/dev/null | head -1 | xargs -r basename | sed 's/\.json$//')
  [ -n "$PREV" ] || PREV=$(ls queue/done/${TAG}_*.json 2>/dev/null | head -1 | xargs -r basename | sed 's/\.json$//')
  # v3 (V655): enforce latest_start_utc at actual worker admission: a job still staged / pending / granted after it is cancelled (moved to queue/cancelled with a note) and the sequence stops
  while true; do
    [ -f queue/running/${PREV}.json ] || [ -f queue/done/${PREV}.json ] && break
    JF=$(ls queue/staged/${PREV}.json queue/pending/${PREV}.json queue/granted/${PREV}.json 2>/dev/null | head -1); [ -n "$JF" ] || break
    LS=$($P12 -c "import json,sys; print(json.load(open(sys.argv[1])).get('latest_start_utc',''))" "$JF"); NOW=$(date -u +%FT%TZ)
    if [ -n "$LS" ] && [[ "$NOW" > "$LS" ]]; then mkdir -p queue/cancelled; $P12 - "$JF" "$NOW" <<'PYEOF'
import json, sys, os, shutil
p, now = sys.argv[1], sys.argv[2]; j = json.load(open(p)); j["cancelled"] = dict(ts=now, reason=f"not started by latest_start_utc {j.get('latest_start_utc')} (queue delay); not run for time (lead 05:47:15Z item 4; V655)")
dst = os.path.join("queue", "cancelled", os.path.basename(p)); json.dump(j, open(dst, "w"), indent=1); os.remove(p); print("cancelled", dst)
PYEOF
      echo "$(date -u +%FT%TZ) profile_queue: $NAME cancelled: not started by its latest_start_utc $LS; this and the later points are not run for time" | tee -a $LOG; exit 0
    fi
    sleep 60
  done
done
while [ -n "$PREV" ] && [ ! -f queue/done/${PREV}.json ]; do sleep 60; done
echo "$(date -u +%FT%TZ) profile_queue: all nine PROFILE runs ended" | tee -a $LOG
