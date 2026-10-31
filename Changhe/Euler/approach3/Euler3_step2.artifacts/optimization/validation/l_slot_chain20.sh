#!/bin/bash
# Chain 20 (16:36Z; lead 14:52:14Z item 5 (c): fixed-aware segment_report rerun as an EVAL item): segment_report.py v4 (5acf7750f3195482) for the FIXED segment-1 members (v3 records invalid) and the four segment-2 ends; frozen copies; GPU 4 next to chain 18; about 12 s each.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain20 started (segment_report v4: FIXED s1 members and the four segment-2 ends)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN20 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN20" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
R=RUN_ROOT/numerics/degree6_free_parameters_48h/runs
for r in p1c_s1_S01_L6_cl0.4500_om1.0000_fixed p1_s2_S01_L6_cl0.4500_om1.0000_free p1c_s2_S01_L6_cl0.4500_om1.0000_fixed; do go frozen segrep4_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py $R/$r --reference-core 0.4304351316933 --source "verifier V235 plan: S01 baseline core radius; registered core ball = reference_core/32 = 0.013451097865415625 (V281)" cuda:0; done
for r in p2c_s1_S09_L6_cl0.4500_om0.3000_fixed p2_s2_S09_L6_cl0.4500_om0.3000_free p2c_s2_S09_L6_cl0.4500_om0.3000_fixed; do go frozen segrep4_${r%%_L6*}_$(date -u +%H%M%S) $GPU segment_report.py $R/$r --reference-core 0.14364049210478602 --source "verifier V304/V306: P2 registered core ball radius reference_core/32 = 0.004488765378274563 (confirmed 13:18:05Z)" cuda:0; done
echo "$(date -u +%FT%TZ) chain20 done" >> $LOG
