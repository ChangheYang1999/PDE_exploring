#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; PY=python3; export CUDA_VISIBLE_DEVICES=
echo "$(date -u +%FT%TZ) evals chain started for cont2_s5_S09_L6_cl0.4500_om0.3000_free (J_c EVAL v5 + segment_report v4.1, then 6.3 (a) records, then the decision)" >> $LOG
bash validation/l_launch_v3.sh frozen jceval_v5_cont2_s5_S09_$(date -u +%H%M%S) 2 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s5_S09_L6_cl0.4500_om0.3000_free cuda:0 256
bash validation/l_launch_v3.sh frozen segrep41_cont2_s5_S09_$(date -u +%H%M%S) 2 segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s5_S09_L6_cl0.4500_om0.3000_free --reference-core 0.14364049210478602 --source "verifier V304/V306: P2 registered core ball radius reference_core/32 = 0.004488765378274563 (confirmed 13:18:05Z)" cuda:0
if [ ! -f validation/records_63a/P2_start_v10.json ]; then bash scripts/r63a_run.sh 2 P2_start_v10 start RUN_ROOT/numerics/degree6_free_parameters_48h/queue/done/p2_s1_S09_L6_cl0.4500_om0.3000_free.json; fi
SEGSTART=""; if [ -n "cont2_s4_S09" ] && [ -f validation/records_63a/cont2_s4_S09_end.json ]; then SEGSTART="--segment-start $(pwd)/validation/records_63a/cont2_s4_S09_end.json"; fi
bash scripts/r63a_run.sh 2 cont2_s5_S09_end end RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s5_S09_L6_cl0.4500_om0.3000_free --full --start-ref $(pwd)/validation/records_63a/P2_start_v10.json $SEGSTART
DEC=$($PY scripts/r63a_decide.py --end cont2_s5_S09_end --ref P2_start_v10)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for cont2_s5_S09_L6_cl0.4500_om0.3000_free: $DEC" >> $LOG; echo "6.3 (a) decision: $DEC"
if [ "yes" = "yes" ] && [ "7200" -ge 600 ] && [ "${DEC%% |*}" = "yes" ]; then
  echo "$(date -u +%FT%TZ) 8.5 rule MET, 6.3 (a) records clear, 7200 s remain: waiting for a host slot, then enqueuing cont2_s6_S09 on GPU 2 (exclusive), time limit 7200 s" | tee -a $LOG
  bash scripts/wait_slot.sh 3 7200 | tee -a $LOG
  bash scripts/enqueue_continuation_v122.sh "RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s5_S09_L6_cl0.4500_om0.3000_free" "cont2_s6_S09" "2" 1 "7200" | tee -a $LOG
else
  echo "$(date -u +%FT%TZ) NO next segment for cont2_s5_S09_L6_cl0.4500_om0.3000_free (rate met: yes; remaining s: 7200; 6.3 (a): $DEC): the slot goes to the next queue item" | tee -a $LOG
fi
echo "$(date -u +%FT%TZ) evals chain done for cont2_s5_S09_L6_cl0.4500_om0.3000_free" >> $LOG
