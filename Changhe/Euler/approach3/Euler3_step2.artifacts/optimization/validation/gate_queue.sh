#!/bin/bash
# D6FP 2026-10-29T05:02Z: queue runner for the remaining SPEC 3.1 gate cases on GPUs 4,5,6 within the lane limit of FOUR busy host processes
# v2 2026-10-29T08:05:17Z: busy() counts EVERY validation/*.py process of this lane (the v1 list omitted g1_step_addon.py, so a fifth computation was launched at 08:02:11Z)
# (gates.py, worker_d6.py, lm_cost_compare.py, g8_*.py, g3_addon.py processes of this lane). Picks the GPU with the fewest of our processes.
# Items: one per line in validation/gate_queue.txt ("<case>" for gates, or "CMD <shell command with GPU placeholder {GPU}>"); a line is removed
# when launched; stop file validation/STOP_GATE_QUEUE. Log validation/logs/gate_queue.log. Host processes run with taskset -c 31-34.
cd "$(dirname "$0")/.."; LOG=validation/logs/gate_queue.log; Q=validation/gate_queue.txt
PY=python3
busy() {   # our lane's heavy PYTHON processes only (comm python*, cwd under d6-num): not the bash -c wrappers whose args repeat the command, not the lead's copies
  n=0; for p in $(ps -eo pid,comm,args | awk '$2 ~ /^python/' | grep -E "venv/bin/python( -u)? (validation/[A-Za-z0-9_]+\.py|scripts/worker_d6)" | grep -v grep | awk '{print $1}'); do
    case "$(readlink /proc/$p/cwd 2>/dev/null)" in RUN_ROOT/numerics*) n=$((n+1));; esac; done; echo $n; }
gpu_load() { for g in 4 5 6; do n=$(ps -eo pid,comm,args | awk '$2 ~ /^python/' | grep -E "venv/bin/python" | grep -v grep | awk '{print $1}' | while read p; do tr '\0' '\n' < /proc/$p/environ 2>/dev/null | grep -c "^CUDA_VISIBLE_DEVICES=$g$"; done | awk '{s+=$1} END {print s+0}'); echo "$g $n"; done | sort -k2,2n -k1,1n | head -1 | cut -d' ' -f1; }
echo "$(date -u +%FT%TZ) gate queue started" >> $LOG
while [ -s $Q ]; do
  [ -f validation/STOP_GATE_QUEUE ] && { echo "$(date -u +%FT%TZ) STOP_GATE_QUEUE present; exiting" >> $LOG; exit 0; }
  if [ "$(busy)" -ge 4 ]; then sleep 30; continue; fi
  item=$(head -1 $Q)
  if [ "${item#CMD }" = "$item" ]; then          # a gates case needs a GPU without another gates process (G3 holds two full Jacobians; two cases on one A100 ran out of memory at 06:0xZ)
    g=""; for cand in 4 5 6; do n=$(ps -eo pid,comm,args | awk '$2 ~ /^python/' | grep -E "venv/bin/python -u validation/gates.py" | grep -v grep | awk '{print $1}' | while read pp; do tr '\0' '\n' < /proc/$pp/environ 2>/dev/null | grep -c "^CUDA_VISIBLE_DEVICES=$cand$"; done | awk '{s+=$1} END {print s+0}'); [ "$n" = "0" ] && { g=$cand; break; }; done
    [ -z "$g" ] && { sleep 30; continue; }
    sed -i '1d' $Q
  else
    sed -i '1d' $Q; g=$(gpu_load)
  fi
  if [ "${item#CMD }" != "$item" ]; then
    cmd=${item#CMD }; cmd=${cmd//\{GPU\}/$g}
    echo "$(date -u +%FT%TZ) launch on GPU $g: $cmd" >> $LOG
    CUDA_VISIBLE_DEVICES=$g OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 setsid nohup nice -n 10 taskset -c 31-34 bash -c "$cmd" > /dev/null 2>&1 < /dev/null &
  else
    echo "$(date -u +%FT%TZ) launch gates $item on GPU $g (tag gpu_v1_$item)" >> $LOG
    setsid nohup bash scripts/run_gpu_battery.sh $g 31-34 gpu_v1_$item $item > /dev/null 2>&1 < /dev/null &
  fi
  sleep 60
done
echo "$(date -u +%FT%TZ) gate queue empty" >> $LOG
