#!/bin/bash
# Read-only hang check for a campaign root (no signals). Usage: bin/hang_check_v2.sh <root>
# Prints, for each campaign860 worker of the root: wchan, CPU ticks over 6 s, children with state/wchan/ticks. The old symptom
# (g4_v1): parent in do_wait for minutes, exactly one non-zombie pool child blocked in futex_wait_queue with zero CPU progress.
ROOT=${1:?root}; date -u +%FT%T.%3NZ
for W in $(pgrep -f "campaign860[.]py --root $ROOT"); do
  echo "worker $W wchan=$(cat /proc/$W/wchan 2>/dev/null) state=$(awk '{print $3}' /proc/$W/stat 2>/dev/null) threads=$(ls /proc/$W/task 2>/dev/null | wc -l)"
  t0=$(awk '{print $14+$15}' /proc/$W/stat 2>/dev/null); declare -A c0
  for C in $(pgrep -P $W); do c0[$C]=$(awk '{print $14+$15}' /proc/$C/stat 2>/dev/null); done
  sleep 6
  t1=$(awk '{print $14+$15}' /proc/$W/stat 2>/dev/null); echo "  parent ticks $t0 -> $t1 over 6 s"
  for C in $(pgrep -P $W); do echo "  child $C state=$(awk '{print $3}' /proc/$C/stat 2>/dev/null) wchan=$(cat /proc/$C/wchan 2>/dev/null) ticks ${c0[$C]:-?} -> $(awk '{print $14+$15}' /proc/$C/stat 2>/dev/null)"; done
done
[ -f "$ROOT/HEARTBEAT.json" ] && python3 -c 'import json,sys,time; d=json.load(open(sys.argv[1])); print("heartbeat age %.0f s phase %s slice %s trials %s accepted %s status %s" % (time.time()-d["epoch"], d.get("phase"), d.get("slice"), d.get("trials"), d.get("accepted"), d.get("status")))' "$ROOT/HEARTBEAT.json"
