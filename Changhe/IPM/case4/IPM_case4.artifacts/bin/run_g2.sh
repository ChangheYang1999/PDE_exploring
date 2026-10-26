#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G2 evidence chain: freeze the code manifest, then run T0/T1, T2, T3(+T5) under the guard with the manifest hash in every output.
# Usage: run_g2.sh <tag> [workers]
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=$LANE/work/research/hardware/guard.py
TAG=$1; W=${2:-8}; OUT=$LANE/outputs/g2/$TAG; mkdir -p $OUT; cd $LANE/work/research860
echo "[$(date -u +%FT%TZ)] freeze manifest $TAG" | tee -a $OUT/run.log
$LANE/bin/freeze_manifest.sh $TAG | tee -a $OUT/run.log || exit 1
M=$LANE/outputs/manifests/code_manifest_$TAG.json
SESS=$LANE/outputs/g2/session_$TAG; $PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $LANE/outputs/g2_policy.json >> $OUT/run.log 2>&1 || exit 1
SEEDCHECK=$OUT/seed_check; [ -e $LANE/outputs/campaign860/seed/seed_860.npz ] && SEEDARG="--seed-dir=$SEEDCHECK" || SEEDARG=""
for step in "t0t1 g2_t0_t1.py" "t2 g2_t2.py" "t3 g2_t3.py" "t26 g2_t26.py" "supplement g2_supplement.py"; do
  set -- $step
  echo "[$(date -u +%FT%TZ)] start $1" | tee -a $OUT/run.log
  EXTRA=""; [ $1 = t3 ] && EXTRA="$W $SEEDARG"; [ $1 = supplement ] && EXTRA="$W"; [ $1 = t26 ] && EXTRA="$W"; [ $1 = t0t1 ] && EXTRA="$SEEDARG"
  $PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label g2_$1 -- $PY -B tests/$2 $OUT/$1.json $M $EXTRA >> $OUT/run.log 2>&1
  echo "[$(date -u +%FT%TZ)] end $1 rc=$?" | tee -a $OUT/run.log
done
echo "[$(date -u +%FT%TZ)] G2 CHAIN DONE" | tee -a $OUT/run.log
