#!/bin/bash
# Wave 1 (SPEC 3.4 (b) provisional release: at most two concurrent FREE jobs, records carry "pre-verifier"): pilots from the two priority lineages.
cd "$(dirname "$0")/.."; PY=python3
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE --tag w1_S01 --max_iter 120 --time_limit 3600 --priority 20 --note "wave 1 pilot, pre-verifier"
$PY scripts/enqueue_d6.py --start starts/S09_d6w_cl0.45_om0.3_R1.pt --label FREE --tag w1_S09 --max_iter 120 --time_limit 3600 --priority 20 --note "wave 1 pilot, pre-verifier"
