#!/bin/bash
# NEAR_CHECK_v08 run (theory_agent_1): builds near_params_v06.json with the reviewed whole-plane uppers and runs an unchanged
# scratch copy of near_check_v03.py on it, then the HI' cuts at the new rate (hi_kq_v05.py).
# Usage (from the lane root): PYTHON=<python 3.12.13> bash research/closure_check/run_nc08.sh "<source text>"
set -euo pipefail
SRC="$1"
D4=444.194167252431246601983285; D5=4186.352092180269533722245282; D6=63050.392730580225839237053713
P=${PYTHON:?set PYTHON to the Python 3.12.13 interpreter with python-flint 0.9.0}
export OMP_NUM_THREADS=1
nice -n 19 taskset -c 41 $P -B research/closure_check/mk_params_v06.py $D4 $D5 $D6 "$SRC" > research/closure_check/near_params_v06.json
W=scratch/nc08; rm -rf $W; mkdir -p $W
cp research/closure_check/near_check_v03.py $W/
cmp research/closure_check/near_check_v03.py $W/near_check_v03.py
cp research/closure_check/near_params_v06.json $W/
T0=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
( cd $W && timeout 60 nice -n 19 taskset -c 41 $P -B near_check_v03.py near_params_v06.json > near_check_v08.out )
T1=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
cp $W/near_check_v08.out research/closure_check/near_check_v08.out
cp $W/near_check_v03.result.json research/closure_check/near_check_v08.result.json
T2=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
nice -n 19 taskset -c 41 $P -B research/h4rest/hi_kq_v05.py research/closure_check/near_check_v08.result.json > research/h4rest/hi_kq_v05.out
T3=$(date -u +%Y-%m-%dT%H:%M:%S.%2NZ)
echo "near check run $T0 to $T1; hi_kq_v05 run $T2 to $T3"
