#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) medium chain started for f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free (J_c EVAL v5, start reference f2_start, end record)" >> $LOG
bash validation/l_launch.sh frozen jceval_v5_f2_S01_k0_keep_m1_$(date -u +%H%M%S) 1 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free cuda:0 256
if [ ! -f validation/records_63a/f2_start.json ]; then bash scripts/r63a_run.sh 1 f2_start start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/f2_S01_k0_keep_L6_cl0.4597_om1.3389_free.json; fi
REF2OPT=""; if [ -n "P1_start" ] && [ -f validation/records_63a/P1_start.json ]; then REF2OPT="--start-ref $(pwd)/validation/records_63a/P1_start.json"; fi
bash scripts/r63a_run.sh 1 f2_S01_k0_keep_m1_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free --full --start-ref $(pwd)/validation/records_63a/f2_start.json $REF2OPT
DEC=$($PY scripts/r63a_decide.py --end f2_S01_k0_keep_m1_end --ref f2_start --ref P1_start)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
echo "$(date -u +%FT%TZ) medium chain done for f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free (no enqueue by this chain; the lead decides the promotion)" >> $LOG
