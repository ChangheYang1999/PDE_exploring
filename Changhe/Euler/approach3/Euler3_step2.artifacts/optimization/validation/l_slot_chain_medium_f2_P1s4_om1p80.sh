#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) medium chain started for f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free (J_c EVAL v5, start reference f2P1s4_start, end record)" >> $LOG
bash validation/l_launch_v6.sh frozen jceval_v5_f2_P1s4_om1p80_$(date -u +%H%M%S) 0 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free cuda:0 256
if [ ! -f validation/records_63a/f2P1s4_start.json ]; then bash scripts/r63a_run.sh 0 f2P1s4_start start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free.json; fi
REF2OPT=""; if [ -n "P1_start_v10" ] && [ -f validation/records_63a/P1_start_v10.json ]; then REF2OPT="--start-ref $(pwd)/validation/records_63a/P1_start_v10.json"; fi
bash scripts/r63a_run.sh 0 f2_P1s4_om1p80_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free --full --start-ref $(pwd)/validation/records_63a/f2P1s4_start.json $REF2OPT
DEC=$($PY scripts/r63a_decide.py --end f2_P1s4_om1p80_end --ref f2P1s4_start --ref P1_start_v10)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
echo "$(date -u +%FT%TZ) medium chain done for f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free (no enqueue by this chain; the lead decides the promotion)" >> $LOG
