#!/bin/bash
# after the delta = 3/5 chain (pid 641960) ends: one-step linearization error at order 350 (core 12), then resume c007_p2048 on core 12
cd .
PY=python3
while kill -0 641960 2>/dev/null; do sleep 30; done
echo "$(date -u +%FT%TZ) 3/5 chain ended; running onestep_edge_error at 350" >> logs/after35_chain.out
taskset -c 12 nice -n 19 $PY -u code/onestep_edge_error.py ckpt/log_sin1_c3_N350.pkl 350 1,3,10,30,60,100,174 > notes/onestep_edge_error_350.txt 2>&1
echo "$(date -u +%FT%TZ) onestep done; resuming c007_p2048" >> logs/after35_chain.out
setsid nohup taskset -c 12 nice -n 19 $PY -u code/run_recursion.py --tag c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10 --resume >> logs/c007_p2048.out 2>&1 &
echo "$(date -u +%FT%TZ) c007_p2048 resumed pid $!" >> logs/after35_chain.out
