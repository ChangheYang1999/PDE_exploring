#!/bin/bash
# Stage III protected reproduction (lead note 41 item 5): re-run the operator test suite and the supervisor resume test once, from a clean
# process, and record UTC start/end, wall time and outcome. Run after the 11:59:44Z optimization stop and before 14:00Z.
# Usage: bash scripts/stage3_tests.sh [gpu-id or empty for CPU]   -> logs/tests/stage3_tests_<UTC>.log (and the two test logs it names)
set -u
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1
GPU="${1:-}"
PY="${PYTHON:-python3}"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
LOG=logs/tests/stage3_tests_${STAMP}.log
mkdir -p logs/tests
{
echo "stage3_tests start $(date -u +%Y-%m-%dT%H:%M:%SZ) host $(hostname) CUDA_VISIBLE_DEVICES=${GPU}"
echo "== tests/test_ops.py (operator identities, manufactured fields, dilation covariance, axis limits, dtype; CPU)"
T0=$(date +%s.%N); CUDA_VISIBLE_DEVICES= nice -n 19 $PY tests/test_ops.py > logs/tests/stage3_test_ops_${STAMP}.log 2>&1; RC=$?; T1=$(date +%s.%N)
echo "test_ops exit $RC wall $(python3 -c "print(round($T1-$T0,1))") s; summary: $(grep -ciE 'pass|ok' logs/tests/stage3_test_ops_${STAMP}.log) lines mention pass/ok, $(grep -ciE 'fail|error|traceback' logs/tests/stage3_test_ops_${STAMP}.log) mention fail/error; last line: $(tail -1 logs/tests/stage3_test_ops_${STAMP}.log | cut -c1-160)"
echo "== scripts/test_resume.sh (disposable job, SIGTERM after a checkpoint, relaunch, check resume)"
T0=$(date +%s.%N); CUDA_VISIBLE_DEVICES="${GPU}" nice -n 19 bash scripts/test_resume.sh > logs/tests/stage3_test_resume_${STAMP}.log 2>&1; RC=$?; T1=$(date +%s.%N)
echo "test_resume exit $RC wall $(python3 -c "print(round($T1-$T0,1))") s; last lines:"; tail -4 logs/tests/stage3_test_resume_${STAMP}.log | cut -c1-200
echo "resume markers in the disposable run log: $(R=$(cut -d" " -f3 logs/tests/resume_test.log.rundir); grep -cE "interrupted|resumed from checkpoint" $R/log.txt 2>/dev/null) ; $(R=$(cut -d" " -f3 logs/tests/resume_test.log.rundir); grep -E "resumed from checkpoint" $R/log.txt 2>/dev/null | tail -1 | cut -c1-160)"
echo "stage3_tests end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} | tee "$LOG"
