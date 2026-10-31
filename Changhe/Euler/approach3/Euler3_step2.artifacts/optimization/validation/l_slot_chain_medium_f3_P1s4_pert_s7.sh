#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) medium chain started for f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free (J_c EVAL v5, start reference f3P1s4pert_start, end record)" >> $LOG
bash validation/l_launch_v6.sh frozen jceval_v5_f3_P1s4_pert_s7_$(date -u +%H%M%S) 3 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free cuda:0 256
if [ ! -f validation/records_63a/f3P1s4pert_start.json ]; then bash scripts/r63a_run.sh 3 f3P1s4pert_start start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free.json; fi
REF2OPT=""; if [ -n "P1_start_v10" ] && [ -f validation/records_63a/P1_start_v10.json ]; then REF2OPT="--start-ref $(pwd)/validation/records_63a/P1_start_v10.json"; fi
bash scripts/r63a_run.sh 3 f3_P1s4_pert_s7_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free --full --start-ref $(pwd)/validation/records_63a/f3P1s4pert_start.json $REF2OPT
DEC=$($PY scripts/r63a_decide.py --end f3_P1s4_pert_s7_end --ref f3P1s4pert_start --ref P1_start_v10)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
echo "$(date -u +%FT%TZ) medium chain done for f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free (no enqueue by this chain; the lead decides the promotion)" >> $LOG
