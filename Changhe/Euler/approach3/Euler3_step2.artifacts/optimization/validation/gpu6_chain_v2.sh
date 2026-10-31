#!/bin/bash
# D6FP 2026-10-29T04:58Z: GPU 6 follow-up: wait for the G7 driver v2 (pid 3883240; it resumes the smoke on GPU 6 and waits for its end), then gates S05_own (full) on GPU 6, core 32.
cd "$(dirname "$0")/.."; LOG=validation/logs/gpu6_chain.log
echo "$(date -u +%FT%TZ) gpu6_chain_v2: waiting for the G7 driver pid 3883240" >> $LOG
while kill -0 3883240 2>/dev/null; do sleep 15; done
[ -f validation/STOP_GPU6 ] && { echo "$(date -u +%FT%TZ) STOP_GPU6 present" >> $LOG; exit 0; }
echo "$(date -u +%FT%TZ) GPU 6: gates S05_own (full)" >> $LOG
bash scripts/run_gpu_battery.sh 6 32 gpu_v1_S05_own S05_own >> $LOG 2>&1
echo "$(date -u +%FT%TZ) gpu6_chain_v2 complete" >> $LOG
