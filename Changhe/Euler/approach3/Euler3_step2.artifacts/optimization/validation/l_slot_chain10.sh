#!/bin/bash
# Chain 10 (lead 13:35:25Z item 1: chain 7's freed slot takes the tail of chain 8): S01 z_c J_f and J_c (in the check's copy) -> 3.1 add-ons (frozen copies) -> four segment reports (segment_report v3, pair-dependent reference_core). GPU 6 by the memory rule (g24 items short; add-ons 40 GB).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=6
echo "$(date -u +%FT%TZ) chain10 started (tail of chain 8)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN10 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN10" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go incopy runs_l/ddcheck_S01_zc_1113 $GPU l_eval.py S01_shift_a Jf optimizer:z_c c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/ddcheck_S01_zc_1113 $GPU l_eval.py S01_shift_a Jc optimizer:z_c c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go frozen g3addon_31_$(date -u +%H%M) $GPU g3_addon.py --tag gpu_v1_31 --cases manu_a,S11_own
go frozen g1step_manu_a_$(date -u +%H%M) $GPU g1_step_addon.py manu_a RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_manu_a.json
go frozen g1step_manu_allm_c_$(date -u +%H%M) $GPU g1_step_addon.py manu_allm_c RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_manu_allm_c.json
for r in p1_s1_S01_L6_cl0.4500_om1.0000_free p1c_s1_S01_L6_cl0.4500_om1.0000_fixed; do go frozen segrep_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/$r --reference-core 0.4304351316933 --source "verifier V235 plan: S01 baseline core radius; registered core ball = reference_core/32 = 0.013451097865415625 (V281)" cuda:0; done
for r in p2_s1_S09_L6_cl0.4500_om0.3000_free p2c_s1_S09_L6_cl0.4500_om0.3000_fixed; do go frozen segrep_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/$r --reference-core 0.14364049210478602 --source "verifier V304/V306: P2 registered core ball radius reference_core/32 = 0.004488765378274563, reference_core = 0.14364049210478602 (registered value confirmed by the verifier 13:18:05Z)" cuda:0; done
echo "$(date -u +%FT%TZ) chain10 done" >> $LOG
