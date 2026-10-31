#!/bin/bash
# Chain 6 v4 (lead 11:58:44Z, 12:01:35Z item 3; GPU 5 from the P2 FIXED segment-2 end): S05 c_l producer comparison first (in its check's copy, about 12 min), then the S01 z_c qualification (qualifier v4), the S05 c_l qualification, S05 c_l J_f and J_c.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; WAIT=$1; GPU=5
echo "$(date -u +%FT%TZ) chain6 v4 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 15; done
go() { [ -f validation/STOP_L_CHAIN6 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN6" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go incopy runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jcw physical:c_l c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go frozen trigqual_S01_zc_$(date -u +%H%M) $GPU l_trig_qual.py S01_shift_a optimizer:z_c RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_S01_shift_a.json cuda:0 RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/leval_Jcw_S01_zc_1133
go frozen trigqual_S05_cl_$(date -u +%H%M) $GPU l_trig_qual.py S05_shift_c physical:c_l RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_S05_shift_c.json cuda:0 RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/ddcheck_S05_cl_1123
go incopy runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jf physical:c_l c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jc physical:c_l c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
echo "$(date -u +%FT%TZ) chain6 v4 done" >> $LOG
