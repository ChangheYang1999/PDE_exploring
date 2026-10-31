#!/bin/bash
# Chain 14 (shift 4, 15:37Z; lead 15:16:53Z item 5 / 15:27:53Z item 5): J_c EVAL of the four segment-2 end states (P1 FREE 228, P1 FIXED 360, P2 FREE 280, P2 FIXED 360), one frozen copy each, GPU 4 (free since chain 11 ended); the (n)(5) evaluation keeps the other free slot.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain14 started (J_c EVAL of the four segment-2 end states)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN14 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN14" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
for r in p1_s2_S01_L6_cl0.4500_om1.0000_free p1c_s2_S01_L6_cl0.4500_om1.0000_fixed p2_s2_S09_L6_cl0.4500_om0.3000_free p2c_s2_S09_L6_cl0.4500_om0.3000_fixed; do
  go frozen jceval_${r%%_L6*}_$(date -u +%H%M%S) $GPU jc_eval_state.py RUN_ROOT/numerics/degree6_free_parameters_48h/runs/$r cuda:0 256
done
echo "$(date -u +%FT%TZ) chain14 done" >> $LOG
