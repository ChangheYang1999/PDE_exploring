#!/bin/bash
# Guarded (l) launch v5 (00:5xZ; V527): release bound to a python descendant of the launched item (process ancestry), not to the aggregate busy count. v4 kept as l_launch_v4.sh.
# Guarded (l) launch v4 (00:1xZ; V523): the lock is held until the launched python process is visible (or the item exited), not for a fixed 25 s. v3.1 kept as l_launch_v3.sh for the instances still waiting on it.
# Guarded (l) launch v3.1 (22:1xZ): the idle daemons scripts/supervisor.py and scripts/slot_governor.py are excluded from the count.
# Guarded (l) launch v3 (22:1xZ): the busy count includes EVERY python process of the lane running a scripts/*.py or validation/*.py file (worker_d6, refit_start, branch_distance, record_63a, jc_eval_state, ...); v2 counted validation/*.py and worker_d6 only, so scripts/refit_start.py was invisible and five busy processes ran from 22:08:46Z to 22:12:29Z. v2 kept as l_launch.sh for the chains that already run it.
# Guarded (l) launch v2: under an exclusive lock, waits until the lane's busy count (python validation/*.py and worker_d6.py processes of this lane) is at
# most 3, launches ONE frozen-copy (run_frozen.sh), in-copy (run_in_copy.sh) or plain command item in the background, waits 25 s so that its python
# process is visible to the next launcher, releases the lock and waits for the item. Usage:
#   validation/l_launch.sh frozen <name> <gpu> <script> [args...] | incopy <run dir> <gpu> <script> [args...] | cmd <shell command string>
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; LOCK=validation/.l_launch.lock
busy() { n=0; for p in $(ps -eo pid,comm,args | awk '$2 ~ /^python/' | grep -E "venv/bin/python( -u)? [^ ]*(validation/[A-Za-z0-9_]+\.py|scripts/[A-Za-z0-9_]+\.py)" | grep -v grep | grep -v -E "scripts/(supervisor|slot_governor)\.py" | awk '{print $1}'); do case "$(readlink /proc/$p/cwd 2>/dev/null)" in RUN_ROOT/numerics*) n=$((n+1));; esac; done; echo $n; }
MODE=$1; shift
exec 9>"$LOCK"; flock -x 9
while [ "$(busy)" -ge 4 ]; do sleep 20; done
echo "$(date -u +%FT%TZ) l_launch: busy $(busy) -> start $MODE $*" >> $LOG
case $MODE in
  frozen) bash validation/run_frozen.sh "$@" >> $LOG 2>&1 & ;;
  incopy) bash validation/run_in_copy.sh "$@" >> $LOG 2>&1 & ;;
  cmd) bash -c "$*" >> $LOG 2>&1 & ;;
esac
PID=$!
# v5 (00:5xZ; V527): the lock is released only when a python DESCENDANT of the launched item (bound by process ancestry, not by the aggregate count) is visible,
# or when the launched item has exited (it used no slot); never after a fixed delay. Polls every 2 s; warning every 60 s after 600 s.
desc_python() { local q=("$1"); local found=0; while [ ${#q[@]} -gt 0 ]; do local cur=${q[0]}; q=("${q[@]:1}"); for c in $(ps -o pid= --ppid $cur 2>/dev/null); do if ps -o comm= -p $c 2>/dev/null | grep -q '^python'; then found=1; fi; q+=($c); done; done; echo $found; }
t=0
while kill -0 $PID 2>/dev/null; do [ "$(desc_python $PID)" = "1" ] && break; sleep 2; t=$((t+2)); [ $t -ge 600 ] && [ $((t % 60)) -eq 0 ] && echo "$(date -u +%FT%TZ) l_launch_v5: WARNING no python descendant of the launched item after $t s; lock held" >> $LOG; done
echo "$(date -u +%FT%TZ) l_launch_v5: lock released after $t s (busy $(busy); launched item $( kill -0 $PID 2>/dev/null && echo running || echo exited ))" >> $LOG
flock -u 9; exec 9>&-
wait $PID; rc=$?; echo "$(date -u +%FT%TZ) l_launch: done $MODE $1 exit $rc" >> $LOG; exit $rc
