#!/bin/bash
# Chain 21 (16:4xZ): segment_report.py v4.1 (d540d8c9ea28a67e) for the four segment-2 ends; frozen copies; GPU 4 next to chain 18; about 12 s each.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain21 started (segment_report v4.1: the four segment-2 ends)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN21 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN21" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
R=RUN_ROOT/numerics/degree6_free_parameters_48h/runs
for r in p1_s2_S01_L6_cl0.4500_om1.0000_free p1c_s2_S01_L6_cl0.4500_om1.0000_fixed; do go frozen segrep41_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py $R/$r --reference-core 0.4304351316933 --source "verifier V235 plan: S01 baseline core radius; registered core ball = reference_core/32 = 0.013451097865415625 (V281)" cuda:0; done
for r in p2_s2_S09_L6_cl0.4500_om0.3000_free p2c_s2_S09_L6_cl0.4500_om0.3000_fixed; do go frozen segrep41_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py $R/$r --reference-core 0.14364049210478602 --source "verifier V304/V306: P2 registered core ball radius reference_core/32 = 0.004488765378274563 (confirmed 13:18:05Z)" cuda:0; done
echo "$(date -u +%FT%TZ) chain21 done" >> $LOG
