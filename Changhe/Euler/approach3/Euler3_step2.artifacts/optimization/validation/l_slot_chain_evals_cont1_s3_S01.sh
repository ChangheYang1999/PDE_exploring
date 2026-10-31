#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log
echo "$(date -u +%FT%TZ) evals chain started for cont1_s3_S01_L6_cl0.4500_om1.0000_free (J_c EVAL v5 + segment_report v4.1)" >> $LOG
bash validation/l_launch.sh frozen jceval_v5_cont1_s3_S01_$(date -u +%H%M%S) 4 jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s3_S01_L6_cl0.4500_om1.0000_free cuda:0 256
bash validation/l_launch.sh frozen segrep41_cont1_s3_S01_$(date -u +%H%M%S) 4 segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/cont1_s3_S01_L6_cl0.4500_om1.0000_free --reference-core 0.4304351316933 --source "verifier V235 plan: S01 baseline core radius; registered core ball = reference_core/32 = 0.013451097865415625 (V281)" cuda:0
echo "$(date -u +%FT%TZ) evals chain done for cont1_s3_S01_L6_cl0.4500_om1.0000_free" >> $LOG
