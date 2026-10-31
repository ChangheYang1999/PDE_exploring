#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) evals chain started for cont1_s5_S01_L6_cl0.4500_om1.0000_free (J_c EVAL v5 + segment_report v4.1, then 6.3 (a) records, then the decision)" >> $LOG
bash validation/l_launch_v3.sh frozen jceval_v5_cont1_s5_S01_$(date -u +%H%M%S) 1 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s5_S01_L6_cl0.4500_om1.0000_free cuda:0 256
bash validation/l_launch_v3.sh frozen segrep41_cont1_s5_S01_$(date -u +%H%M%S) 1 segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s5_S01_L6_cl0.4500_om1.0000_free --reference-core 0.4304351316933 --source "verifier V235 plan: S01 baseline core radius; registered core ball = reference_core/32 = 0.013451097865415625 (V281)" cuda:0
if [ ! -f validation/records_63a/P1_start_v10.json ]; then bash scripts/r63a_run.sh 1 P1_start_v10 start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/p1_s1_S01_L6_cl0.4500_om1.0000_free.json; fi
SEGSTART=""; if [ -n "cont1_s4_S01" ] && [ -f validation/records_63a/cont1_s4_S01_end.json ]; then SEGSTART="--segment-start $(pwd)/validation/records_63a/cont1_s4_S01_end.json"; fi
bash scripts/r63a_run.sh 1 cont1_s5_S01_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s5_S01_L6_cl0.4500_om1.0000_free --full --start-ref $(pwd)/validation/records_63a/P1_start_v10.json $SEGSTART
DEC=$($PY scripts/r63a_decide.py --end cont1_s5_S01_end --ref P1_start_v10)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for cont1_s5_S01_L6_cl0.4500_om1.0000_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
if [ "yes" = "yes" ] && [ "7200" -ge 600 ] && [ "${DEC%% |*}" = "yes" ]; then
  echo "$(date -u +%FT%TZ) 8.5 rule MET, 6.3 (a) records clear, 7200 s remain: enqueuing cont1_s6_S01 on GPU 1 (exclusive), time limit 7200 s" | tee -a $LOG
  bash scripts/enqueue_continuation_v122.sh "RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s5_S01_L6_cl0.4500_om1.0000_free" "cont1_s6_S01" "1" 1 "7200" | tee -a $LOG
else
  echo "$(date -u +%FT%TZ) NO next segment for cont1_s5_S01_L6_cl0.4500_om1.0000_free (rate met: yes; remaining s: 7200; 6.3 (a): $DEC): the slot goes to the next queue item" | tee -a $LOG
fi
echo "$(date -u +%FT%TZ) evals chain done for cont1_s5_S01_L6_cl0.4500_om1.0000_free" >> $LOG
