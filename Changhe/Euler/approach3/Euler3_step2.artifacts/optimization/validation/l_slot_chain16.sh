#!/bin/bash
# Chain 16 (shift 4, 15:58Z; lead 15:27:53Z item 6): S11 random_scaled_2 resolved closure action (diagnostic), frozen copy, GPU 4; one slot stays free for the (n)(5) evaluation.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain16 started (s11_closure_diag)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN16 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN16" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen s11closure_$(date -u +%H%M) $GPU s11_closure_diag.py RUN_ROOT/numerics/degree6_free_parameters_48h/validation/g3_capture_S11_own_random_scaled_2.json cuda:0
echo "$(date -u +%FT%TZ) chain16 done" >> $LOG
