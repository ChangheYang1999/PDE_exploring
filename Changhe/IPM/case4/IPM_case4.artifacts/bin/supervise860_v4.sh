#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Detached supervisor for the 860 campaign (G4 pilot / G5 long run), version 3: lead pre-audit F3(c), F10, F11, F12; SPEC v9.13 (a) and (e):
# hold reasons matched by exact enumerated codes; cumulative session budget exhaustion is a planned end (marker SESSION_BUDGET_EXHAUSTED, never auto-acknowledged;
# continuing needs a fresh guard session dir via SESSION_SUFFIX and an explicit --budget-renewal-reason recorded by the driver); an assessment run that exits
# nonzero or reports a failed/stopped assessment writes STOPPED_FOR_DIAGNOSIS; at G5 start the frozen code directory is made read-only (chmod) and recorded.
# Usage: supervise860_v3.sh <campaign-root> <label> <seconds-per-slice> <workers> [initial-radius] [max-trials]
# Launch as: taskset -c 78-89 nice -n 19 setsid nohup bin/supervise860_v3.sh ... > /dev/null 2>&1 < /dev/null &
# A slice continues only if (F12): the guard call exited 0, exactly one new run dir appeared, its result.json has success true and returncode 0,
# and campaign860 wrote the slice-completion record slice_completion/slice_<n>_<run_id>.json bound to that run id. Scientific stops are read from
# that record (status), never from state.json. Guard holds with only box-wide/budget reasons -> backoff, acknowledge (recorded), continue; other
# holds -> FAULTED and halt; process faults -> restart with backoff (max 5 in a row). STOP file -> exit. Between slices the section 13 cadence runs.
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=$LANE/work/research/hardware/guard.py
ROOT=$1; LABEL=$2; SECS=${3:-3300}; W=${4:-8}; RAD=${5:-}; MAXT=${6:-1000000000}
SEED=$LANE/outputs/campaign860/seed/seed_860.json; SEEDNPZ=$LANE/outputs/campaign860/seed/seed_860_replay_v3.npz; MANIFEST=$(cat $LANE/outputs/campaign860/ACTIVE_MANIFEST)
POLICY=$LANE/outputs/campaign860/campaign_policy_v3.json; KAPPA=$LANE/outputs/campaign860/kappa_calibration_typed.json
KAPPAARG=""; [ -f $KAPPA ] && KAPPAARG="--kappa-file $KAPPA"
SESSION_SUFFIX=${SESSION_SUFFIX:-}; RENEWAL=${BUDGET_RENEWAL_REASON:-}; RENEWARG=""; [ -n "$RENEWAL" ] && RENEWARG="--budget-renewal-reason \"$RENEWAL\""
mkdir -p $ROOT; LOG=$ROOT/supervisor.log; SESS=$ROOT/guard_session${SESSION_SUFFIX}
[ -n "${G5_READONLY_CODE:-}" ] && { chmod -R a-w $LANE/work/research860 && echo "$(date -u +%FT%TZ) frozen code directory made read-only (G5 start, SPEC v9.13 (f))" >> $LOG; }
stamp() { date -u +%FT%TZ; }
echo "$(stamp) supervisor v3 start pid $$ label $LABEL slice ${SECS}s workers $W manifest $MANIFEST seednpz $SEEDNPZ kappa ${KAPPAARG:-manifest} affinity $(taskset -cp $$ 2>/dev/null | cut -d: -f2) nice $(nice)" >> $LOG
echo $$ > $ROOT/SUPERVISOR_PID; export SUPERVISOR_SHA256=$(sha256sum "$0" | cut -d' ' -f1); echo "$(stamp) supervisor sha256 $SUPERVISOR_SHA256 (recorded by the driver in slice_start)" >> $LOG
[ -d $SESS ] || $PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $POLICY >> $LOG 2>&1 || exit 1
faults=0; acks=0
# exact enumerated hold codes (work/research/hardware/policy.py) that are box-wide contention or the per-run budget; everything else is a fault; the cumulative budget is a planned end
BOXWIDE_EXACT='["Linux memory PSI full pressure ceiling", "CPU load per logical CPU ceiling", "system pageout rate ceiling", "per-run wall-time budget exhausted"]'
CUMULATIVE='cumulative session wall-time budget exhausted'
while true; do
  if [ -e $ROOT/STOP ]; then echo "$(stamp) STOP file present; running the end assessment (SPEC section 13) then exiting" >> $LOG; $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $ROOT/worker.lock --label ${LABEL}_assess_end -- $PY -B $LANE/work/research860/assess_cadence860.py $ROOT $MANIFEST $W >> $LOG 2>&1; erc=$?; echo "$(stamp) end assessment exit=$erc; supervisor exits" >> $LOG; break; fi
  [ -e $ROOT/STOPPED_FOR_DIAGNOSIS ] && { echo "$(stamp) STOPPED_FOR_DIAGNOSIS present; supervisor exits" >> $LOG; break; }
  [ -e $ROOT/FAULTED ] && { echo "$(stamp) FAULTED present; supervisor exits" >> $LOG; break; }
  [ -e $ROOT/DRIVER_REFUSED ] && { echo "$(stamp) DRIVER_REFUSED present; supervisor exits" >> $LOG; break; }
  [ -e $ROOT/SESSION_BUDGET_EXHAUSTED ] && [ -z "$RENEWAL" ] && { echo "$(stamp) SESSION_BUDGET_EXHAUSTED present and no BUDGET_RENEWAL_REASON given; supervisor exits" >> $LOG; break; }
  # section 13 cadence (seed, halvings, every 100 accepted, end); writes STOPPED_FOR_DIAGNOSIS on a monitor scientific stop
  ABEFORE=$(ls -d $SESS/runs/*_${LABEL}_assess 2>/dev/null | sort | tr '\n' ' ')
  $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $ROOT/worker.lock --label ${LABEL}_assess -- $PY -B $LANE/work/research860/assess_cadence860.py $ROOT $MANIFEST $W >> $LOG 2>&1
  arc=$?; AAFTER=$(ls -d $SESS/runs/*_${LABEL}_assess 2>/dev/null | sort | tr '\n' ' '); ANEW=$(comm -13 <(echo $ABEFORE | tr ' ' '\n' | sed '/^$/d' | sort) <(echo $AAFTER | tr ' ' '\n' | sed '/^$/d' | sort))
  AOK=$($PY -c "import json,sys,os
d=json.load(open('$ANEW/result.json')) if '$ANEW' and os.path.exists('$ANEW/result.json') else {}
print('yes' if (d.get('success') is True and d.get('returncode')==0 and $arc==0) else 'no')" 2>/dev/null || echo no)
  if [ "$AOK" != yes ]; then echo "$(stamp) assessment run failed (guard_exit=$arc run=$ANEW): STOPPED_FOR_DIAGNOSIS (SPEC v9.13 (a))" >> $LOG; echo "assessment_run_failed $(stamp) run $ANEW guard_exit $arc" > $ROOT/STOPPED_FOR_DIAGNOSIS; break; fi
  [ -e $ROOT/STOPPED_FOR_DIAGNOSIS ] && { echo "$(stamp) assessment requested a scientific stop; supervisor exits" >> $LOG; break; }
  RESUME=""; [ -e $ROOT/state.json ] && RESUME="--resume"
  RADARG=""; [ -n "$RAD" ] && [ -z "$RESUME" ] && RADARG="--initial-radius $RAD"
  NEXT=$($PY -c "import json,sys; print(json.load(open('$ROOT/state.json'))['slices']+1 if __import__('os').path.exists('$ROOT/state.json') else 1)")
  echo "$(stamp) slice $NEXT start $RESUME" >> $LOG; date -u +%FT%TZ > $ROOT/HEARTBEAT
  BEFORE=$(ls -d $SESS/runs/*_${LABEL}_slice 2>/dev/null | sort | tr '\n' ' ')
  $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $ROOT/worker.lock --label ${LABEL}_slice -- \
     $PY -B $LANE/work/research860/campaign860.py --root $ROOT --seed-json $SEED --seed-npz $SEEDNPZ --manifest $MANIFEST --label $LABEL --seconds $SECS --workers $W --max-trials $MAXT $KAPPAARG $RESUME $RADARG $RENEWARG >> $LOG 2>&1
  grc=$?
  RENEWARG=""
  AFTER=$(ls -d $SESS/runs/*_${LABEL}_slice 2>/dev/null | sort | tr '\n' ' ')
  NEW=$(comm -13 <(echo $BEFORE | tr ' ' '\n' | sed '/^$/d' | sort) <(echo $AFTER | tr ' ' '\n' | sed '/^$/d' | sort)); NNEW=$(echo "$NEW" | sed '/^$/d' | wc -l)
  RES='{"success": null, "returncode": null, "stop_reasons": ["no new run dir"], "run_id": null}'
  [ "$NNEW" = 1 ] && RES=$($PY -c "import json; d=json.load(open('$NEW/result.json')); print(json.dumps({'run_id': d.get('run_id'), 'success': d.get('success'), 'returncode': d.get('returncode'), 'stop_reasons': d.get('stop_reasons'), 'wall': round(d.get('wall_seconds',0))}))" 2>/dev/null || echo '{"success": null, "returncode": null, "stop_reasons": ["no result.json"], "run_id": null}')
  RUNID=$(echo "$RES" | $PY -c "import json,sys; print(json.load(sys.stdin).get('run_id') or '')")
  COMP=$ROOT/slice_completion/slice_$(printf %04d $NEXT)_$RUNID.json
  status=unknown; [ -n "$RUNID" ] && [ -f "$COMP" ] && status=$($PY -c "import json; d=json.load(open('$COMP')); assert d['guard_run_id']=='$RUNID' and d['slice']==$NEXT; print(d['status'])" 2>/dev/null || echo unknown)
  echo "$(stamp) slice $NEXT end guard_exit=$grc new_run_dirs=$NNEW result=$RES completion=$([ -f "$COMP" ] && echo yes || echo no) status=$status" >> $LOG; date -u +%FT%TZ > $ROOT/HEARTBEAT
  reasons=$(echo "$RES" | $PY -c "import json,sys; print('|'.join(json.load(sys.stdin).get('stop_reasons') or []))")
  if [ -n "$reasons" ] && [ "$reasons" != "no new run dir" ] && [ "$reasons" != "no result.json" ]; then
     if echo "$reasons" | $PY -c "import sys; rs=sys.stdin.read().strip().split('|'); sys.exit(0 if any(r=='$CUMULATIVE' for r in rs) else 1)"; then
        echo "$(stamp) cumulative session wall-time budget exhausted: planned end, never acknowledged automatically (SPEC v9.13 (e)); marker SESSION_BUDGET_EXHAUSTED; relaunch with SESSION_SUFFIX=<new> and BUDGET_RENEWAL_REASON set" >> $LOG; echo "cumulative budget exhausted $(stamp) run $RUNID" > $ROOT/SESSION_BUDGET_EXHAUSTED; break
     fi
     if echo "$reasons" | $PY -c "import json,sys; rs=sys.stdin.read().strip().split('|'); ok=set(json.loads('$BOXWIDE_EXACT')); sys.exit(0 if all(r in ok for r in rs) else 1)"; then
        acks=$((acks+1)); echo "$(stamp) guard hold with box-wide/budget reasons only ($reasons); backoff then acknowledge #$acks" >> $LOG; sleep $((120*acks > 1800 ? 1800 : 120*acks))
        $PY -B $GUARD acknowledge --session-dir $SESS --lock-file $ROOT/worker.lock --reason "supervisor auto-acknowledge: box-wide contention or wall budget ($reasons) at $(stamp)" >> $LOG 2>&1 || { echo "$(stamp) acknowledge refused (conditions still fail); retry next loop" >> $LOG; sleep 300; }
        echo "{\"utc\": \"$(stamp)\", \"reasons\": \"$reasons\", \"ack\": $acks, \"run_id\": \"$RUNID\"}" >> $ROOT/auto_acknowledgements.jsonl; continue
     else
        echo "$(stamp) guard hold with non-box-wide reasons ($reasons): FAULTED, supervisor halts" >> $LOG; echo "hold $reasons $(stamp)" > $ROOT/FAULTED; break
     fi
  fi
  # F12: a slice counts as completed only with guard exit 0, success true, returncode 0 and the bound completion record
  OK=$(echo "$RES" | $PY -c "import json,sys; d=json.load(sys.stdin); print('yes' if (d.get('success') is True and d.get('returncode')==0 and $grc==0 and '$status'!='unknown') else 'no')")
  DRC=$($PY -c "import json; d=json.load(open('$NEW/result.json')); print(d.get('returncode'))" 2>/dev/null || echo none)
  if [ "$DRC" = 4 ]; then echo "$(stamp) driver refusal (exit 4): a scientific stop state, STOPPED_FOR_DIAGNOSIS, a due assessment or a binding refusal; supervisor halts (marker DRIVER_REFUSED)" >> $LOG; echo "refusal $(stamp) run $RUNID" > $ROOT/DRIVER_REFUSED; break; fi
  if [ "$OK" != yes ]; then
     faults=$((faults+1)); echo "$(stamp) process fault #$faults (guard_exit=$grc result=$RES completion_status=$status); backoff" >> $LOG
     [ $faults -ge 5 ] && { echo "$(stamp) five consecutive faults; supervisor halts (FAULTED marker)" >> $LOG; echo "faults $(stamp)" > $ROOT/FAULTED; break; }
     sleep $((60*faults)); continue
  fi
  case "$status" in
    checkpointed_slice) faults=0; sleep 5;;
    stopped_by_request) if [ -e $ROOT/STOP ]; then echo "$(stamp) stopped by operator STOP file" >> $LOG; break; else echo "$(stamp) SIGTERM without STOP file: treated as a process fault" >> $LOG; faults=$((faults+1)); sleep $((60*faults)); fi;;
    full_matrix_trust_subproblem_inaccuracy_requires_diagnosis|model_reduction_at_precision_floor|needs_mesh_refinement|trust_obstruction_requires_diagnosis|needs_independent_stationarity_verification|exceptional_parameter_requires_rank_treatment)
      echo "$(stamp) SCIENTIFIC STOP: $status (SPEC section 11); no automatic restart" >> $LOG; echo "$status $(stamp) run $RUNID" > $ROOT/STOPPED_FOR_DIAGNOSIS; break;;
    *) faults=$((faults+1)); echo "$(stamp) unexpected completion status '$status': process fault #$faults" >> $LOG; [ $faults -ge 5 ] && { echo "faults $(stamp)" > $ROOT/FAULTED; break; }; sleep $((60*faults));;
  esac
done
echo "$(stamp) supervisor exit" >> $LOG; rm -f $ROOT/SUPERVISOR_PID
