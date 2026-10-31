#!/bin/bash
# Wait until the lane's busy count (python processes of the lane running scripts/*.py or validation/*.py, daemons excluded) is at most N (default 3), so that a job
# enqueued next (launched by the supervisor without a host-slot check) does not exceed four busy computations. Usage: bash scripts/wait_slot.sh [N] [max_wait_s]
N=${1:-3}; MAXW=${2:-7200}; t=0
busy() { n=0; for p in $(ps -eo pid,comm,args | awk '$2 ~ /^python/' | grep -E "venv/bin/python( -u)? [^ ]*(validation/[A-Za-z0-9_]+\.py|scripts/[A-Za-z0-9_]+\.py)" | grep -v grep | grep -v -E "scripts/(supervisor|slot_governor)\.py" | awk '{print $1}'); do case "$(readlink /proc/$p/cwd 2>/dev/null)" in RUN_ROOT/numerics*) n=$((n+1));; esac; done; echo $n; }
while [ "$(busy)" -gt "$N" ]; do sleep 20; t=$((t+20)); [ $t -ge $MAXW ] && { echo "wait_slot: gave up after $t s (busy $(busy))"; exit 1; }; done
echo "wait_slot: busy $(busy) <= $N after $t s"
