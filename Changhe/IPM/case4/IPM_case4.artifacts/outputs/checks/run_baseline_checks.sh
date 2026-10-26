#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Guarded baseline checks in the isolated copy (never the protected tree).
set -u
LANE=$IPM_ARTIFACT_ROOT
PY=$LANE/env/bin/python
REPO=$LANE/work
CHECKS=$LANE/outputs/checks
GUARD=$REPO/research/hardware/guard.py
SESSION=$CHECKS/session
cd $CHECKS
echo "[$(date -u +%FT%TZ)] guard init"
$PY -B $GUARD init --session-dir $SESSION --disk-path $CHECKS --policy $CHECKS/smoke_policy.json || exit 1
for spec in "value_smoke smoke smoke.json" "whole_axis_objective objective objective.json" "strict_replay_01 replay replay_01.json" "strict_replay_02 replay replay_02.json"; do
  set -- $spec
  echo "[$(date -u +%FT%TZ)] start $1"
  $PY -B $GUARD run --session-dir $SESSION --cwd $CHECKS --lock-file $CHECKS/verification.lock --label $1 \
     -- $PY -B $REPO/tools/portable.py $2 --output $CHECKS/$3
  echo "[$(date -u +%FT%TZ)] end $1 rc=$?"
done
echo "[$(date -u +%FT%TZ)] ALL DONE"
