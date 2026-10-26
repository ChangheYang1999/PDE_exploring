#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# C7 fixture (SPEC v9.13 (e)): the supervisor's hold classification uses exact enumerated codes, never substrings; the cumulative budget is a planned end.
# Extracts the BOXWIDE_EXACT and CUMULATIVE definitions from the (pending or frozen) supervisor and applies the same python tests the supervisor runs.
# Usage: test_supervisor_v3_holds.sh <supervise860_v3.sh path>
set -u
SUP=$1; PY=$IPM_ARTIFACT_ROOT/env/bin/python
eval "$(grep -E '^BOXWIDE_EXACT=|^CUMULATIVE=' $SUP)"
classify() {  # mirrors the supervisor: cumulative -> planned_end; all reasons exact box-wide codes -> acknowledge; else -> fault
  local reasons="$1"
  if echo "$reasons" | $PY -c "import sys; rs=sys.stdin.read().strip().split('|'); sys.exit(0 if any(r=='$CUMULATIVE' for r in rs) else 1)"; then echo planned_end; return; fi
  if echo "$reasons" | $PY -c "import json,sys; rs=sys.stdin.read().strip().split('|'); ok=set(json.loads('$BOXWIDE_EXACT')); sys.exit(0 if all(r in ok for r in rs) else 1)"; then echo acknowledge; else echo fault; fi
}
pass=0; fail=0
expect() { got=$(classify "$1"); if [ "$got" = "$2" ]; then echo "PASS [$1] -> $got"; pass=$((pass+1)); else echo "FAIL [$1] -> $got (expected $2)"; fail=$((fail+1)); fi; }
expect "Linux memory PSI full pressure ceiling" acknowledge
expect "CPU load per logical CPU ceiling|system pageout rate ceiling" acknowledge
expect "per-run wall-time budget exhausted" acknowledge
expect "cumulative session wall-time budget exhausted" planned_end
expect "cumulative session wall-time budget exhausted|Linux memory PSI full pressure ceiling" planned_end
expect "process-family RSS ceiling" fault
expect "minimum free disk ceiling" fault
expect "Linux memory PSI full pressure ceiling (disk failure)" fault
expect "disk" fault
expect "Linux memory PSI full pressure ceiling|process-family RSS ceiling" fault
expect "cgroup memory event: oom_kill" fault
echo "RESULT pass=$pass fail=$fail"; [ $fail = 0 ]
