#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Detached supervisor for the 860 campaign (G4 pilot / G5 long run), lead pre-audit F3(c), F10, F11.
# Usage: supervise860.sh <campaign-root> <label> <seconds-per-slice> <workers> [initial-radius] [max-trials]
# Launch as: taskset -c 78-89 nice -n 19 setsid nohup bin/supervise860.sh ... > /dev/null 2>&1 < /dev/null &
# Slice outcomes are read from the guard run result.json: normal slice end -> continue; STOP file -> exit; SPEC section 11 scientific
# stop -> STOPPED_FOR_DIAGNOSIS and halt; guard hold with only box-wide/budget reasons -> backoff, acknowledge (recorded), continue;
# other holds (family RSS, available memory, disk, swap, cgroup OOM, temperature, supervisor exception) -> FAULTED and halt;
# process faults -> restart with backoff (max 5 in a row). Between slices the section 13 assessment cadence runs (assess_cadence860.py).
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=$LANE/work/research/hardware/guard.py
ROOT=$1; LABEL=$2; SECS=${3:-3300}; W=${4:-8}; RAD=${5:-}; MAXT=${6:-1000000000}
SEED=$LANE/outputs/campaign860/seed/seed_860.json; SEEDNPZ=$LANE/outputs/campaign860/seed/seed_860_replay_v2.npz; MANIFEST=$(cat $LANE/outputs/campaign860/ACTIVE_MANIFEST)
POLICY=$LANE/outputs/campaign860/campaign_policy_v2.json
mkdir -p $ROOT; LOG=$ROOT/supervisor.log; SESS=$ROOT/guard_session
echo "$(date -u +%FT%TZ) supervisor start pid $$ label $LABEL slice ${SECS}s workers $W manifest $MANIFEST affinity $(taskset -cp $$ 2>/dev/null | cut -d: -f2) nice $(nice)" >> $LOG
echo $$ > $ROOT/SUPERVISOR_PID
[ -d $SESS ] || $PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $POLICY >> $LOG 2>&1 || exit 1
faults=0; acks=0
BOXWIDE='Linux memory PSI full pressure ceiling|CPU load per logical CPU ceiling|system pageout rate ceiling|per-run wall-time budget exhausted|cumulative session wall-time budget exhausted|Linux block paging'
while true; do
  [ -e $ROOT/STOP ] && { echo "$(date -u +%FT%TZ) STOP file present; supervisor exits" >> $LOG; break; }
  [ -e $ROOT/STOPPED_FOR_DIAGNOSIS ] && { echo "$(date -u +%FT%TZ) STOPPED_FOR_DIAGNOSIS present; supervisor exits" >> $LOG; break; }
  [ -e $ROOT/FAULTED ] && { echo "$(date -u +%FT%TZ) FAULTED present; supervisor exits" >> $LOG; break; }
  # section 13 cadence (seed, halvings, every 100 accepted, end); writes STOPPED_FOR_DIAGNOSIS on a monitor scientific stop
  $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $ROOT/worker.lock --label ${LABEL}_assess -- $PY -B $LANE/work/research860/assess_cadence860.py $ROOT $MANIFEST $W >> $LOG 2>&1
  [ -e $ROOT/STOPPED_FOR_DIAGNOSIS ] && { echo "$(date -u +%FT%TZ) assessment monitor requested a scientific stop; supervisor exits" >> $LOG; break; }
  RESUME=""; [ -e $ROOT/state.json ] && RESUME="--resume"
  RADARG=""; [ -n "$RAD" ] && [ -z "$RESUME" ] && RADARG="--initial-radius $RAD"
  echo "$(date -u +%FT%TZ) slice start $RESUME" >> $LOG; date -u +%FT%TZ > $ROOT/HEARTBEAT
  $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $ROOT/worker.lock --label ${LABEL}_slice -- \
     $PY -B $LANE/work/research860/campaign860.py --root $ROOT --seed-json $SEED --seed-npz $SEEDNPZ --manifest $MANIFEST --label $LABEL --seconds $SECS --workers $W --max-trials $MAXT $RESUME $RADARG >> $LOG 2>&1
  grc=$?
  R=$(ls -td $SESS/runs/*_${LABEL}_slice 2>/dev/null | head -1)
  RES=$($PY -c "import json; d=json.load(open('$R/result.json')); print(json.dumps({'run_id': d.get('run_id'), 'success': d.get('success'), 'returncode': d.get('returncode'), 'stop_reasons': d.get('stop_reasons'), 'wall': round(d.get('wall_seconds',0))}))" 2>/dev/null || echo '{"success": null, "stop_reasons": ["no result.json"]}')
  status=$($PY -c "import json; print(json.load(open('$ROOT/state.json')).get('status','?'))" 2>/dev/null || echo unknown)
  echo "$(date -u +%FT%TZ) slice end guard_exit=$grc result=$RES status=$status" >> $LOG; date -u +%FT%TZ > $ROOT/HEARTBEAT
  reasons=$(echo "$RES" | $PY -c "import json,sys; print('|'.join(json.load(sys.stdin).get('stop_reasons') or []))")
  if [ -n "$reasons" ]; then
     if echo "$reasons" | $PY -c "import re,sys; rs=sys.stdin.read().strip().split('|'); sys.exit(0 if all(re.search(r'$BOXWIDE', r) for r in rs) else 1)"; then
        acks=$((acks+1)); echo "$(date -u +%FT%TZ) guard hold with box-wide/budget reasons only ($reasons); backoff then acknowledge #$acks" >> $LOG; sleep $((120*acks > 1800 ? 1800 : 120*acks))
        $PY -B $GUARD acknowledge --session-dir $SESS --lock-file $ROOT/worker.lock --reason "supervisor auto-acknowledge: box-wide contention or wall budget ($reasons) at $(date -u +%FT%TZ)" >> $LOG 2>&1 || { echo "$(date -u +%FT%TZ) acknowledge refused (conditions still fail); retry next loop" >> $LOG; sleep 300; }
        echo "{\"utc\": \"$(date -u +%FT%TZ)\", \"reasons\": \"$reasons\", \"ack\": $acks}" >> $ROOT/auto_acknowledgements.jsonl; continue
     else
        echo "$(date -u +%FT%TZ) guard hold with non-box-wide reasons ($reasons): FAULTED, supervisor halts" >> $LOG; echo "hold $reasons $(date -u +%FT%TZ)" > $ROOT/FAULTED; break
     fi
  fi
  case "$status" in
    checkpointed_slice) faults=0; sleep 5;;
    stopped_by_request) if [ -e $ROOT/STOP ]; then echo "$(date -u +%FT%TZ) stopped by operator STOP file" >> $LOG; break; else echo "$(date -u +%FT%TZ) SIGTERM without STOP file treated as a process fault" >> $LOG; faults=$((faults+1)); sleep $((60*faults)); fi;;
    full_matrix_trust_subproblem_inaccuracy_requires_diagnosis|model_reduction_at_precision_floor|needs_mesh_refinement|trust_obstruction_requires_diagnosis|needs_independent_stationarity_verification)
      echo "$(date -u +%FT%TZ) SCIENTIFIC STOP: $status (SPEC section 11); no automatic restart" >> $LOG; echo "$status $(date -u +%FT%TZ)" > $ROOT/STOPPED_FOR_DIAGNOSIS; break;;
    *) faults=$((faults+1)); echo "$(date -u +%FT%TZ) process fault #$faults (guard_exit=$grc status=$status); backoff" >> $LOG
       [ $faults -ge 5 ] && { echo "$(date -u +%FT%TZ) five consecutive faults; supervisor halts (FAULTED marker)" >> $LOG; echo "faults $(date -u +%FT%TZ)" > $ROOT/FAULTED; break; }
       sleep $((60*faults));;
  esac
done
echo "$(date -u +%FT%TZ) supervisor exit" >> $LOG; rm -f $ROOT/SUPERVISOR_PID
