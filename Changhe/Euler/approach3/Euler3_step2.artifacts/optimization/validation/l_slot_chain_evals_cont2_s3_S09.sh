#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log
echo "$(date -u +%FT%TZ) evals chain started for cont2_s3_S09_L6_cl0.4500_om0.3000_free (J_c EVAL v5 + segment_report v4.1)" >> $LOG
bash validation/l_launch.sh frozen jceval_v5_cont2_s3_S09_$(date -u +%H%M%S) 4 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s3_S09_L6_cl0.4500_om0.3000_free cuda:0 256
bash validation/l_launch.sh frozen segrep41_cont2_s3_S09_$(date -u +%H%M%S) 4 segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont2_s3_S09_L6_cl0.4500_om0.3000_free --reference-core 0.14364049210478602 --source "verifier V304/V306: P2 registered core ball radius reference_core/32 = 0.004488765378274563 (confirmed 13:18:05Z)" cuda:0
echo "$(date -u +%FT%TZ) evals chain done for cont2_s3_S09_L6_cl0.4500_om0.3000_free" >> $LOG
