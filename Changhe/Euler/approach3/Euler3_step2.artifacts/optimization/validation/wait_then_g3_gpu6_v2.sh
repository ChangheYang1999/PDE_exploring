#!/bin/bash
# G3 add-on (fixed active-set enforcement) and the far-noise split on GPU 6 once the smk_jc2 smoke worker has released its memory and fewer than 4 heavy jobs run
cd "$(dirname "$0")/.."; PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1
while pgrep -f 'worker_d6.py runs/smk_jc2' > /dev/null || [ "$(pgrep -fc 'gates.py|g3_addon|profile_d6|worker_d6|far_noise_split|g8_tables|exterior_monopole_regression|cache_regression')" -ge 4 ]; do sleep 20; done
echo "$(date -u +%FT%TZ) G3 add-on start"; nice -n 10 $PY -u validation/g3_addon.py --tag A --cases S01_own,S05_own,manu_small_omega,manu_large_omega > validation/logs/g3_addon_A.log 2>&1; echo "$(date -u +%FT%TZ) G3 add-on done exit $?"
while [ "$(pgrep -fc 'gates.py|g3_addon|profile_d6|worker_d6|far_noise_split|g8_tables|exterior_monopole_regression|cache_regression')" -ge 4 ]; do sleep 20; done
echo "$(date -u +%FT%TZ) far noise split start"; nice -n 10 $PY -u validation/far_noise_split.py --tag A --cases S01_own,manu_a > validation/logs/far_noise_split_A.log 2>&1; echo "$(date -u +%FT%TZ) far noise split done exit $?"
