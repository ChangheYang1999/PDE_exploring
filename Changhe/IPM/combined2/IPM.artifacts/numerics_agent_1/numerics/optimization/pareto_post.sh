#!/bin/bash
# pareto_post.sh <tag> <core> : light post-processing of a Pareto endpoint: MID 32 x 180 FLOAT evaluation, N_q at P-Q2/P-S1/P-S2/P-Q1 (numerics_agent_2 sobolev_proxy.py),
# S_F at P-H and alpha 1/10 (numerics_agent_2 strong_eval2.py). No exact G0 (use post_run.sh for snapshot candidates). Outputs in runs/<tag>/.
TAG=$1; CORE=${2:-44}; LANE=$(cd "$(dirname "$0")/../.." && pwd); PY=python3; R=$LANE/numerics/optimization/runs/$TAG
cd $LANE; export OMP_NUM_THREADS=1 IPM_DEVICE=cuda
echo "pareto_post $TAG start $(date -u +%Y-%m-%dT%H:%M:%SZ)"
nice -n 10 taskset -c $CORE $PY -B numerics/optimization/eval_candidate.py $R/${TAG}_exact.json $R/${TAG}_eval_mid32.json 180 32
nice -n 10 taskset -c $CORE $PY -B numerics/n2_code/sobolev_proxy.py $R/${TAG}_exact.json $R/${TAG}_NQ.json "2.4,1.0,0.25;2.1,1.0,0.5;2.1,1.4,1;2.6,1.4,0.25"
nice -n 10 taskset -c $CORE $PY -B numerics/n2_code/strong_eval2.py $R/${TAG}_exact.json $R/${TAG}_SF.json "0.5,0.4,1.75;0.1,0.4,1.75"
echo "pareto_post $TAG DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)"
