#!/bin/bash
# Chain 13 (shift 4, 15:23Z; lead 15:16:53Z item 5 slot order): SPEC v1.22 3.6 (n) (4) gauge-row diagnostic at manu_a (columns 189, 186); frozen copy; GPU 4 next to chain 11.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain13 started (gauge_row_diag manu_a)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN13 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN13" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen gaugediag_manu_a_$(date -u +%H%M) $GPU gauge_row_diag.py cuda:0 189,186
echo "$(date -u +%FT%TZ) chain13 done" >> $LOG
