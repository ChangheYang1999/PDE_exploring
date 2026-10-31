#!/bin/bash
# wait for the S09_own gates process (pid 122999, GPU 5) to exit, run the coefficient-column diagnostic on GPU 5 (core 33), then restart the gate queue
cd "$(dirname "$0")/.."; LOG=validation/logs/after_s09_diag.log; PY=python3
echo "$(date -u +%FT%TZ) waiting for pid 122999 (gates S09_own)" >> $LOG
while kill -0 122999 2>/dev/null; do sleep 10; done
echo "$(date -u +%FT%TZ) S09 gates finished; diagnostic on GPU 5" >> $LOG
CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 33 $PY -u validation/diag_coef_column.py S09_own 793,873,186,189,41 > validation/logs/diag_coef_S09.log 2>&1
echo "$(date -u +%FT%TZ) diagnostic exit $?; restarting the gate queue" >> $LOG
rm -f validation/STOP_GATE_QUEUE
pgrep -f "[g]ate_queue.sh" >/dev/null || setsid nohup bash validation/gate_queue.sh > /dev/null 2>&1 < /dev/null &
echo "$(date -u +%FT%TZ) done" >> $LOG
