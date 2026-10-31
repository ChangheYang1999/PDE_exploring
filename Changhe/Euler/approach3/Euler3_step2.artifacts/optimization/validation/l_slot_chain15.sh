#!/bin/bash
# Chain 15 (shift 4, 15:44Z): the PRE-INPUT capture of the (n)(5) copy v4 (gauge_row_dd.py prepare manu_a; no evaluation; V358 item 2) in a frozen copy, GPU 4 next to chain 14.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain15 started (gauge_row_dd prepare manu_a)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN15 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN15" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen gaugedd_prepare_v45_manu_a_$(date -u +%H%M) $GPU gauge_row_dd.py prepare manu_a cuda:0
echo "$(date -u +%FT%TZ) chain15 done" >> $LOG
