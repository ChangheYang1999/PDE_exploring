#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Run one command under the handoff resource guard (copy only). Usage: grun.sh <label> <cmd...>
# Uses a per-label lock so independent development runs can proceed concurrently inside the 12-core allotment.
LANE=$IPM_ARTIFACT_ROOT
PY=$LANE/env/bin/python
GUARD=$LANE/work/research/hardware/guard.py
SESS=$LANE/outputs/dev_sessions/$(date -u +%Y%m%d)_$1
LABEL=$1; shift
mkdir -p $LANE/outputs/dev_sessions
[ -d $SESS ] || $PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $LANE/outputs/dev_policy.json > /dev/null || exit 1
exec $PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label $LABEL -- "$@"
