#!/bin/bash
# misc validation runs on GPU 6, each started only when fewer than 4 of the lane's heavy computations are running (CPU limit)
cd "$(dirname "$0")/.."; PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1
waitslot() { while [ "$(pgrep -fc 'gates.py|g3_addon|profile_d6|worker_d6|far_noise_split|g8_tables|exterior_monopole_regression|o1_tables_regression|check_angular_dd')" -ge 4 ]; do sleep 20; done; }
for job in "check_angular_dd.py" "o1_tables_regression.py" "exterior_monopole_regression.py" "g8_tables.py --tag A --case S01_own"; do
  waitslot; name=$(echo $job | cut -d' ' -f1 | sed 's/.py//')
  echo "$(date -u +%FT%TZ) start $job"; nice -n 10 $PY -u validation/$job > validation/logs/misc_$name.log 2>&1; echo "$(date -u +%FT%TZ) done $job exit $?"
done
