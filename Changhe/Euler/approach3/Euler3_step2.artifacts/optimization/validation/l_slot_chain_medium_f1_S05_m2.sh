#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) medium chain started for f1_S05_m2_L6_cl0.4500_om0.3000_free (J_c EVAL v5, start reference f1_start, end record)" >> $LOG
bash validation/l_launch_v4.sh frozen jceval_v5_f1_S05_m2_$(date -u +%H%M%S) 6 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f1_S05_m2_L6_cl0.4500_om0.3000_free cuda:0 256
if [ ! -f validation/records_63a/f1_start.json ]; then bash scripts/r63a_run.sh 6 f1_start start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/f1_s1_S05_L6_cl0.4500_om0.3000_free.json; fi
REF2OPT=""; if [ -n "" ] && [ -f validation/records_63a/.json ]; then REF2OPT="--start-ref $(pwd)/validation/records_63a/.json"; fi
bash scripts/r63a_run.sh 6 f1_S05_m2_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f1_S05_m2_L6_cl0.4500_om0.3000_free --full --start-ref $(pwd)/validation/records_63a/f1_start.json $REF2OPT
DEC=$($PY scripts/r63a_decide.py --end f1_S05_m2_end --ref f1_start )
echo "$(date -u +%FT%TZ) 6.3 (a) decision for f1_S05_m2_L6_cl0.4500_om0.3000_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
echo "$(date -u +%FT%TZ) medium chain done for f1_S05_m2_L6_cl0.4500_om0.3000_free (no enqueue by this chain; the lead decides the promotion)" >> $LOG
