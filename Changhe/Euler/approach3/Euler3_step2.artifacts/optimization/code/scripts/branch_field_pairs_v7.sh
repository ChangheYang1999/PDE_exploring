#!/bin/bash
# Field part of the branch identity on the F-projected endpoints (lead 20:05:46Z item 4 (a), 20:11:10Z item 2) with the producer tool v7 (CPU, one process,
# sequential; each pair about 3 to 4 minutes). States: the worker's end-of-segment checkpoints (the files the lead's branch_param v4 and the verifier's freezes
# name by sha256). Width records: the lead's v6 records; EVAL records: the npz each width record was made from (F1: the frozen copy jceval_v5_f1_S05_m1_200306).
# Usage: bash scripts/branch_field_pairs_v7.sh   (run only when at most three other busy computations of the lane are running)
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3; export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
LEAD=RUN_ROOT/lead/notes; JC=RUN_ROOT/numerics/degree6_free_parameters_48h/validation/jc_eval; LOG=validation/logs/branch_field_pairs_v7.out
run() { echo "$(date -u +%FT%TZ) branch_distance v7 $(sha256sum scripts/branch_distance.py | cut -c1-16): $1"; nice -n 10 taskset -c 31-34 $PY scripts/branch_distance.py "${@:2}"; echo "$(date -u +%FT%TZ) exit $?"; }
# 1. low pair, registered test: P2 segment-4 end (a) vs F1 medium end (b)
run p2s4_vs_f1m1 runs/cont2_s4_S09_L6_cl0.4500_om0.3000_free/starts/start_000.pt runs/f1_S05_m1_L6_cl0.4500_om0.3000_free/starts/start_000.pt --tag p2s4_vs_f1m1_v74 \
  --sens-a $LEAD/sens_s4records_v6/cont2_s4_S09_L6_cl0.4500_om0.3000_free.json --jc-a $JC/cont2_s4_S09_L6_cl0.4500_om0.3000_free/linearization_00648_eval_complete.npz \
  --sens-b $LEAD/sens_f1m1_v6/f1_S05_m1_L6_cl0.4500_om0.3000_free.json --jc-b RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/jceval_v5_f1_S05_m1_200306/validation/jc_eval/f1_S05_m1_L6_cl0.4500_om0.3000_free/linearization_00225_eval_complete.npz
# 2. high pair: P1 segment-4 end (a) vs F2 medium end (b)
run p1s4_vs_f2m1 runs/cont1_s4_S01_L6_cl0.4500_om1.0000_free/starts/start_000.pt runs/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free/starts/start_000.pt --tag p1s4_vs_f2m1_v74 \
  --sens-a $LEAD/sens_s4p1_v6/cont1_s4_S01_L6_cl0.4500_om1.0000_free.json --jc-a $JC/cont1_s4_S01_L6_cl0.4500_om1.0000_free/linearization_00587_eval_complete.npz \
  --sens-b $LEAD/sens_s4records_v6/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free.json --jc-b $JC/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free/linearization_00214_eval_complete.npz
# 3. information: P2 segment-3 end (a) vs F1 medium end (b)
run p2s3_vs_f1m1 runs/cont2_s3_S09_L6_cl0.4500_om0.3000_free/starts/start_000.pt runs/f1_S05_m1_L6_cl0.4500_om0.3000_free/starts/start_000.pt --tag p2s3_vs_f1m1_v74 \
  --sens-a $LEAD/sens_s3records_v6/cont2_s3_S09_L6_cl0.4500_om0.3000_free.json --jc-a $JC/cont2_s3_S09_L6_cl0.4500_om0.3000_free/linearization_00466_eval_complete.npz \
  --sens-b $LEAD/sens_f1m1_v6/f1_S05_m1_L6_cl0.4500_om0.3000_free.json --jc-b RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/jceval_v5_f1_S05_m1_200306/validation/jc_eval/f1_S05_m1_L6_cl0.4500_om0.3000_free/linearization_00225_eval_complete.npz
echo "$(date -u +%FT%TZ) all three pairs done"
