#!/bin/bash
# snap_run.sh <tag> <ID> <parent_id> <parent_sha256> "<description>" "<notes>" [sf_json|none]
# Snapshots runs/<tag>/<tag>_exact.json with its sectors JSON and MID 32 eval JSON (post_run.sh must have run) into exchange/candidate_snapshots/<ID>/.
TAG=$1; ID=$2; PID=$3; PSHA=$4; DESCR=$5; NOTES=$6; SF=${7:-none}
LANE=$(cd "$(dirname "$0")/../.." && pwd); PY=python3; R=$LANE/numerics/optimization/runs/$TAG
LOSS=$($PY -c "import json; print(json.load(open('$R/${TAG}_summary.json'))['meta']['final_objective'])")
W=$($PY -c "import json; print(json.dumps(json.load(open('$R/${TAG}_summary.json'))['meta']['weights']))")
cd $LANE && OMP_NUM_THREADS=1 nice -n 10 $PY -B numerics/optimization/snapshot_n1.py "$ID" "$PID" "$PSHA" $R/${TAG}_exact.json $R/${TAG}_sectors.json $R/${TAG}_eval_mid32.json "$LOSS" "run_n1.py objective on the MID 16 x 180 training mesh (0.02 <= r <= 1e4): weights $W; value at the saved coefficients" "$DESCR" "$NOTES" "$SF"
