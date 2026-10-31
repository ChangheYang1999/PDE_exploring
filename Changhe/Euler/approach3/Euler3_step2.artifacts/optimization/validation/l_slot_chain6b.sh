#!/bin/bash
# Chain 6b (shift 4, 14:50Z): the S05 c_l J_f and J_c items of chain 6 moved from GPU 5 to GPU 4 (next to chain 11: 25.6 + about 20 + 8 GB < 80) so that GPU 5 is clear for the
# P3 FIXED-CONTROL member when the S05 c_l qualification ends; chain 6 was stopped after its running item with STOP_L_CHAIN6 (the host slot count is unchanged: lead 14:31:05Z item 2 (c)).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; WAIT=$1; GPU=4
echo "$(date -u +%FT%TZ) chain6b armed: wait for chain 6 (pid $WAIT); GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 15; done
go() { [ -f validation/STOP_L_CHAIN6B ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN6B" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go incopy runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jf physical:c_l c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jc physical:c_l c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
echo "$(date -u +%FT%TZ) chain6b done" >> $LOG
