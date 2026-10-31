#!/bin/bash
# Fourth (l) chain: after chain2's S01 z_c l_eval, run the S05 c_l named comparison INSIDE the frozen copy of its passing check (lead 11:35:30Z item 1).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=$1; SCOPE=$2; WAIT=$3
echo "$(date -u +%FT%TZ) chain4 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 10; done; rm -f validation/STOP_L_CHAIN
echo "$(date -u +%FT%TZ) start leval_Jcw_S05_cl in runs_l/ddcheck_S05_cl_1123" >> $LOG
bash validation/run_in_copy.sh runs_l/ddcheck_S05_cl_1123 $GPU l_eval.py S05_shift_c Jcw physical:c_l $SCOPE cuda:0 >> $LOG 2>&1; echo "$(date -u +%FT%TZ) done leval_Jcw_S05_cl exit $?" >> $LOG
T1=$(date -u +%FT%TZ); echo "$T1 (l) chain4 done" >> $LOG
echo "{\"ts\": \"$T1\", \"event\": \"hold_end\", \"pair\": \"P2 segment 2\", \"detail\": \"(l) chain4 ended at $T1: both named J_cw comparisons run; remaining items wait for the next free slot\"}" >> status/ledger.jsonl
# (superseded 2026-10-29T11:5xZ: every new launch must first check the lane's busy count, see validation/l_launch.sh)
