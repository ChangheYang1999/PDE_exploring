#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Per-commit routine for the G5 long run (numerics lane): apply one committed trial event to the documents
# (bin/trial_apply.py), and for an accepted trial run the guarded far-field monitor on the new accepted snapshot and
# insert its row (bin/farfield_apply.py). Prints the lines to report. Reader of the run; writes only lane documents.
# Usage: bin/commit_apply.sh <event-number>
set -u
LANE=$IPM_ARTIFACT_ROOT
PY=$LANE/env/bin/python
ROOT=$LANE/outputs/campaign860/pilot_g4_v2
EV=$1
EVF=$ROOT/commits/event_$(printf %08d $EV).json
[ -f "$EVF" ] || { echo "no event file $EVF"; exit 1; }
cd $LANE
$PY -B bin/trial_apply.py $ROOT $EV | tail -1
read ACC ACCB <<<"$($PY -B -c "import json;t=json.load(open('$EVF'))['trial'];print(int(bool(t['accepted'])), t['accepted_before'])")"
if [ "$ACC" = "1" ]; then
  N=$((ACCB+1)); SNAP=$ROOT/snapshots/accepted_$(printf %08d $N).json
  [ -f "$SNAP" ] || { echo "snapshot $SNAP missing"; exit 2; }
  echo "accepted: state $N; sha256 $(sha256sum $SNAP | cut -c1-64)"
  taskset -c 78-89 nice -n 19 $LANE/bin/grun.sh farfield $PY -B $LANE/outputs/dev_v9/farfield_states.py $LANE/outputs/dev_v9/farfield_states $SNAP | tail -1 | cut -c1-200
  $PY -B bin/farfield_apply.py $N
else
  echo "rejected: state unchanged at $ACCB"
fi
echo "df $IPM_ARTIFACT_ROOT avail: $(df -BG --output=avail $IPM_ARTIFACT_ROOT | tail -1 | tr -d ' ')"
ls $ROOT | grep -x -E "STOP|STOPPED_FOR_DIAGNOSIS|FAULTED|DRIVER_REFUSED|SESSION_BUDGET_EXHAUSTED" && echo "MARKER PRESENT (see above)"
exit 0
