#!/bin/bash
# SPEC v1.10 8.7 / rule R4 (lead 01:11Z, 03:16:18Z CPU PLAN; GRAD_EVERY env, default 4 per R5): after the PROVISIONAL RELEASE, P1 S01 and P2 S09 start together as pairs (FREE + FIXED-CONTROL each, identical
# max_iter and time limit), CPU only. Usage: scripts/enqueue_cpu_pairs.sh <max_iter> <time_limit_s> <threads> [lagJ 0|1] [precision_mode]
# The segment length (time limit) is the wall time that gives each FREE job about 6 h at the measured CPU rate (validation/cpu_profile_S01.json).
cd "$(dirname "$0")/.."; PY=python3
MI=$1; TL=$2; TH=${3:-1}; LAG=${4:-0}; PM=${5:-}
[ -z "$MI" ] || [ -z "$TL" ] && { echo "usage: enqueue_cpu_pairs.sh <max_iter> <time_limit_s> <threads> [lagJ 0|1] [precision_mode]"; exit 1; }
EXTRA="{\"threads\": $TH, \"lag_jacobian\": $([ "$LAG" = "1" ] && echo true || echo false)$([ -n "$PM" ] && echo ", \"precision_mode\": \"$PM\""), \"complete_gradient_every\": ${GRAD_EVERY:-4}, \"spec_version\": \"v1.10\", \"spec_sha256\": \"a955f949e70c5831231da947dc96c3c8fa635e95da8f17f36a4f25e1d7d40194\", \"release_battery\": \"CPU-reduced (v1.10)\"}"   # SPEC v1.10 labels and the R5 gradient spacing via --extra (no change to enqueue_d6.py, which is in the snapshot table)
NOTE="SPEC v1.10 8.7 pair (R4), CPU-reduced release battery (v1.10), provisional release"
export CUDA_VISIBLE_DEVICES=
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE          --tag p1_S01 --max_iter $MI --time_limit $TL --priority 30 --extra "$EXTRA" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FIXED-CONTROL --fixed --tag p1c_S01 --max_iter $MI --time_limit $TL --priority 29 --extra "$EXTRA" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S09_d6w_cl0.45_om0.3_R1.pt  --label FREE          --tag p2_S09 --max_iter $MI --time_limit $TL --priority 28 --extra "$EXTRA" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S09_d6w_cl0.45_om0.3_R1.pt  --label FIXED-CONTROL --fixed --tag p2c_S09 --max_iter $MI --time_limit $TL --priority 27 --extra "$EXTRA" --note "$NOTE"
echo "enqueued P1 S01 and P2 S09 pairs: max_iter $MI, time limit $TL s, threads $TH, lagJ $LAG, precision_mode ${PM:-module default}; start the supervisor with configs/supervisor_cpu.json (slots = concurrent jobs)"
