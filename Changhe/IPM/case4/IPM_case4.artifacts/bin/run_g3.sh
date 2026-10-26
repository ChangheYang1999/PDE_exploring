#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G3 run: freeze manifest <tag>, then run tests/g3_t4.py under the guard. Usage: run_g3.sh <tag> [workers]
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=$LANE/work/research/hardware/guard.py
TAG=$1; W=${2:-8}; OUT=$LANE/outputs/g3/$TAG; mkdir -p $OUT; cd $LANE/work/research860
echo "[$(date -u +%FT%TZ)] freeze manifest $TAG" | tee -a $OUT/run.log
$LANE/bin/freeze_manifest.sh $TAG | tee -a $OUT/run.log || exit 1
M=$LANE/outputs/manifests/code_manifest_$TAG.json; SESS=$LANE/outputs/g3/session_$TAG
$PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $LANE/outputs/dev_policy.json >> $OUT/run.log 2>&1 || exit 1
echo "[$(date -u +%FT%TZ)] start t4" | tee -a $OUT/run.log
$PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label g3_t4 -- $PY -B tests/g3_t4.py $OUT/t4.json $M $W >> $OUT/run.log 2>&1
echo "[$(date -u +%FT%TZ)] end t4 rc=$?" | tee -a $OUT/run.log
