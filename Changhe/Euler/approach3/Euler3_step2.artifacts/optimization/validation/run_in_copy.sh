#!/bin/bash
# Run a script INSIDE an existing frozen copy (lead 11:35:30Z item 1: an l_eval may run from the frozen copy of its passing dd check; identical
# SOURCES_SHA256). Usage: validation/run_in_copy.sh <existing runs_l dir> <gpu index or cpu> <script relative to validation/> [args...]
set -u; PY=python3
RUN=$(cd "$1" && pwd); GPU=$2; SCRIPT=$3; shift 3   # absolute path: the redirect after cd failed with a relative path (chain4, 11:43:56Z)
[ -f "$RUN/SOURCES_SHA256.txt" ] || { echo "not a frozen copy: $RUN"; exit 1; }
( cd "$RUN" && sha256sum -c --quiet SOURCES_SHA256.txt ) && echo "$(date -u +%FT%TZ) sources of $RUN verified against SOURCES_SHA256.txt; launching $SCRIPT $*" | tee -a "$RUN/launch.log" || { echo "$(date -u +%FT%TZ) SOURCE MISMATCH in $RUN" | tee -a "$RUN/launch.log"; exit 2; }
if [ "$GPU" = "cpu" ]; then CVD=""; else CVD=$GPU; fi
cd "$RUN" && CUDA_VISIBLE_DEVICES=$CVD OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY -u validation/$SCRIPT "$@" > "$RUN/validation/logs/${SCRIPT%.py}_$(date -u +%H%M%S).log" 2>&1; rc=$?
echo "$(date -u +%FT%TZ) exit $rc" | tee -a "$RUN/launch.log"; exit $rc
