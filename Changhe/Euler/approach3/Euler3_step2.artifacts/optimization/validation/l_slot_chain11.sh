#!/bin/bash
# Chain 11 (shift 4, 2026-10-29T14:3xZ): the S05 z_c qualification again with l_trig_qual v5 (ab075a60336e6898): the v4 run trigqual_S05_zc_1409 crashed in the ladder tie because the
# earlier copy's l_eval v5 record saves far-anchor-block rows only (KeyError D_hi_1e-03); v5 ties on those rows (plus the norm tie). GPU 4 (clear), through l_launch.sh.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain11 started (S05 z_c qualification, qualifier v5)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN11 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN11" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen trigqual_S05_zc_v5_$(date -u +%H%M) $GPU l_trig_qual.py S05_shift_c optimizer:z_c RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_S05_shift_c.json cuda:0 RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/ddcheck_S05_zc_1231
echo "$(date -u +%FT%TZ) chain11 done" >> $LOG
