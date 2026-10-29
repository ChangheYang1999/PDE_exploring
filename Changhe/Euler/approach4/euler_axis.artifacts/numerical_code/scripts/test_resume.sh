#!/bin/bash
# Interruption/resume test on the disposable job zz_test_resume: launch worker detached, SIGTERM it after 45 s,
# confirm checkpoint, relaunch, confirm it resumes from the checkpoint iteration. Logs to logs/tests/resume_test.log.
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
export OMP_NUM_THREADS=1 CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
L=logs/tests/resume_test.log
RUN=runs/zz_test_resume_$(date -u +%Y%m%dT%H%M%SZ)   # unique directory: never overwrite an earlier test record (verifier 12:13Z)
mkdir -p $RUN logs/tests
cp configs/test_resume_job.json $RUN/job.json
echo "run dir $RUN" > $L.rundir
echo "$(date -u +%FT%TZ) first launch" > $L
setsid nohup $PY supervisor/worker.py $RUN/job.json --run-dir $RUN > logs/tests/resume_worker1.out 2>&1 &
P=$!
sleep 20
echo "$(date -u +%FT%TZ) sending SIGTERM to $P" >> $L
kill -TERM $P; wait $P; RC=$?; echo "$(date -u +%FT%TZ) exit code $RC (expect 3)" >> $L   # capture $? before the date subshell (verifier 12:13Z: the old line logged 0)
ls -la $RUN/ >> $L
grep -c "LM it" $RUN/log.txt >> $L
echo "$(date -u +%FT%TZ) relaunch" >> $L
setsid nohup $PY supervisor/worker.py $RUN/job.json --run-dir $RUN > logs/tests/resume_worker2.out 2>&1 &
P=$!; wait $P; RC=$?; echo "$(date -u +%FT%TZ) second run exit code $RC (expect 0)" >> $L
grep -E "resumed|interrupted|finished|initial cost" $RUN/log.txt >> $L
