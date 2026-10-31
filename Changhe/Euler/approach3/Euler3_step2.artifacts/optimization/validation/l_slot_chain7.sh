#!/bin/bash
# Chain 7 v4 (lead 11:58:44Z; GPU 6 from the P1 segment-2 end): dd checks S05 z_c (three references), S01 physical c_l and omega (J_f); copy of the records; power check; S05 z_c comparisons J_cw, J_f, J_c in the check's copy.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; WAIT=$1; GPU=6
echo "$(date -u +%FT%TZ) chain7 v4 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 15; done
go() { [ -f validation/STOP_L_CHAIN7 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN7" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
N=ddcheck_S05_zc_$(date -u +%H%M); echo "$N" > validation/.chain7_S05_zc_check_name; go frozen $N $GPU dd_chain.py S05_shift_c optimizer:z_c Jcw,Jf,Jc cuda:0
NC=ddcheck_S01_cl_$(date -u +%H%M); go frozen $NC $GPU dd_chain.py S01_shift_a physical:c_l Jf cuda:0
NO=ddcheck_S01_om_$(date -u +%H%M); go frozen $NO $GPU dd_chain.py S01_shift_a physical:omega Jf cuda:0
for d in $N $NC $NO; do for f in runs_l/$d/validation/dd_chain_check_*.json; do [ -f "$f" ] && [ ! -f "validation/$(basename $f)" ] && cp "$f" validation/ && echo "$(date -u +%FT%TZ) copied $(basename $f) from $d" >> $LOG; done; done
go frozen lpower_S01_$(date -u +%H%M) $GPU l_power.py S01_shift_a c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/$N $GPU l_eval.py S05_shift_c Jcw optimizer:z_c c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/$N $GPU l_eval.py S05_shift_c Jf optimizer:z_c c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
go incopy runs_l/$N $GPU l_eval.py S05_shift_c Jc optimizer:z_c c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 cuda:0
echo "$(date -u +%FT%TZ) chain7 v4 done" >> $LOG
