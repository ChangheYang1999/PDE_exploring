#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Retained, timestamped read of the G5 run for HANDOFF_860.md (section 11). Reader only: writes one text file and one values JSON under
# outputs/handoff_reads/ and one ETA record under outputs/g3/eta/; launches nothing (the launcher is run with --dry-run).
# Reader SHA-256 values are recorded before and after the read, in the text file and in the JSON. Usage: cd $LANE && bash bin/handoff_read.sh
LANE=$IPM_ARTIFACT_ROOT; cd $LANE || exit 1
R=outputs/campaign860/pilot_g4_v2; U=$(date -u +%Y%m%dT%H%M%SZ); F=outputs/handoff_reads/refresh_$U.txt; J=outputs/handoff_reads/refresh_$U.json; ETA=outputs/g3/eta/eta_observed_g4v2_$U.json
READERS="bin/handoff_read.sh bin/handoff_values.py bin/handoff_apply.py bin/handoff_refresh.py bin/handoff_walls.py bin/eta_observed860.py bin/launch_handoff_assess.sh work/research/hardware/guard.py"
mkdir -p outputs/handoff_reads
{ echo "retained refresh read; captured_at_utc $(date -u +%Y-%m-%dT%H:%M:%S.%NZ) epoch $(date -u +%s.%N)"
  echo "== reader sha256 BEFORE"; sha256sum $READERS
  echo "== process read"; S=$(cat $R/SUPERVISOR_PID); ps -o pid,ppid,pgid,sid,ni,etimes,args -p $S | cut -c1-160; G=$(pgrep -P $S); ps -o pid,ppid,pgid,sid,ni,etimes,args -p $G | cut -c1-160; W=$(pgrep -P $G); ps -o pid,ppid,pgid,sid,ni,etimes,args -p $W | cut -c1-160; echo "POOL_CHILDREN $(pgrep -P $W | tr '\n' ' ')"; taskset -cp $S; taskset -cp $W; cat $R/HEARTBEAT.json | tr -d '\n'; echo
  RES=$(env/bin/python -c "import json; print(max(900.0, 1.5*json.load(open('$R/state.json'))['iteration_wall_max_seconds']))")
  echo "== eta_observed860.py --reserve $RES --slice-seconds 5000 -> $ETA"; env/bin/python -B bin/eta_observed860.py $R $ETA --reserve $RES --slice-seconds 5000 | grep -v "^  [0-9]"; sha256sum $ETA
  echo "== handoff_values.py -> $J"; env/bin/python -B bin/handoff_values.py $R $ETA $J
  echo "== handoff_refresh.py"; env/bin/python -B bin/handoff_refresh.py
  echo "== handoff_walls.py"; env/bin/python -B bin/handoff_walls.py $R
  echo "== launcher dry run"; bash bin/launch_handoff_assess.sh --dry-run 2>&1 | grep -v "^command:"
  echo "== disk"; df -h $IPM_ARTIFACT_ROOT | tail -1; echo "run dir MiB $(du -sm $R | cut -f1)"; echo "lane $(du -sh . | cut -f1)"
  echo "== reader sha256 AFTER"; sha256sum $READERS
  echo "captured_end_utc $(date -u +%Y-%m-%dT%H:%M:%S.%NZ)"; } > $F 2>&1
echo "TXT $F $(sha256sum $F | cut -c1-64)"; echo "JSON $J $(sha256sum $J | cut -c1-64)"; echo "ETA $ETA $(sha256sum $ETA | cut -c1-64)"
echo "next: env/bin/python -B bin/handoff_apply.py $J $F"
