#!/bin/bash
# Chain 12 (shift 4): S11_own random_scaled_2 single-direction G3 capture (verifier 14:33:22Z request; lead 14:31:05Z item 4 (a)); frozen copy; GPU 5 next to chain 6 (30 + about 26 + 8 GB < 80).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=5
echo "$(date -u +%FT%TZ) chain12 started (S11 random_scaled_2 capture)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN12 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN12" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen g3cap_S11_rs2_$(date -u +%H%M) $GPU g3_direction_capture.py S11_own random_scaled_2 cuda:0
echo "$(date -u +%FT%TZ) chain12 done" >> $LOG
