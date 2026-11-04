#!/bin/bash
# NEAR_CHECK_v09 run (theory_agent_1): runs a scratch copy of near_check_v04.py (the direct NR-25 moment bound for a_n) on the
# unchanged near_params_v06.json of NEAR_CHECK_v08, then the HI' cuts at the resulting rate (hi_kq_v06.py).
# Usage (from the lane root): PYTHON=<python 3.12.13> bash research/closure_check/run_nc09.sh
set -euo pipefail
P=${PYTHON:?set PYTHON to the Python 3.12.13 interpreter with python-flint 0.9.0}
export OMP_NUM_THREADS=1
W=scratch/nc09; rm -rf $W; mkdir -p $W
cp research/closure_check/near_check_v04.py research/closure_check/near_params_v06.json $W/
cmp research/closure_check/near_check_v04.py $W/near_check_v04.py
T0=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
( cd $W && timeout 60 nice -n 19 taskset -c 41 $P -B near_check_v04.py near_params_v06.json > near_check_v09.out )
T1=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
cp $W/near_check_v09.out research/closure_check/near_check_v09.out
cp $W/near_check_v04.result.json research/closure_check/near_check_v09.result.json
T2=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
nice -n 19 taskset -c 41 $P -B research/h4rest/hi_kq_v06.py research/closure_check/near_check_v09.result.json > research/h4rest/hi_kq_v06.out
T3=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
echo "near check run $T0 to $T1; hi_kq_v06 run $T2 to $T3"
