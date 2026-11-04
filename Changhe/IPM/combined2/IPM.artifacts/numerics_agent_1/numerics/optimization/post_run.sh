#!/bin/bash
# post_run.sh <tag> [core] : FLOAT evaluation at MID 32 x ANG 180 (GPU) of runs/<tag>/<tag>_exact.json, then the exact ||F||_2 and ||rF||_2
# (c1-n3 Beta method, CPU, about 45 min). Outputs: runs/<tag>/<tag>_eval_mid32.json, numerics/cert/results/<tag>_g0.json. Log: logs/post_<tag>.out
TAG=$1; CORE=${2:-42}
LANE=$(cd "$(dirname "$0")/../.." && pwd); PY=python3
R=$LANE/numerics/optimization/runs/$TAG
cd $LANE
echo "post_run $TAG start $(date -u +%Y-%m-%dT%H:%M:%SZ)"
OMP_NUM_THREADS=1 IPM_DEVICE=cuda nice -n 10 taskset -c $CORE $PY -B numerics/optimization/eval_candidate.py $R/${TAG}_exact.json $R/${TAG}_eval_mid32.json 180 32
echo "eval done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
OMP_NUM_THREADS=1 nice -n 10 taskset -c $CORE $PY -B numerics/cert/exact_g0.py $R/${TAG}_exact.json $TAG numerics/cert/results 0
echo "post_run $TAG DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)"
