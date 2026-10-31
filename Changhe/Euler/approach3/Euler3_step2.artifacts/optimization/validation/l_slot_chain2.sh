#!/bin/bash
# Second (l) chain (shortened so that the hold on P2's segment 2 stays within 45 min): waits for the first chain's pid, then from frozen copies on GPU 5:
# dd check S05_shift_c physical c_l (J_cw, J_f, J_c), copy of the check records into validation/, then l_eval J_cw for the two named comparisons.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=$1; SCOPE=$2; WAIT=$3
echo "$(date -u +%FT%TZ) chain2 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 10; done; rm -f validation/STOP_L_CHAIN
run() { name=$1; shift; echo "$(date -u +%FT%TZ) start $name: $*" >> $LOG; bash validation/run_frozen.sh "$name" "$@" >> $LOG 2>&1; echo "$(date -u +%FT%TZ) done $name exit $?" >> $LOG; [ -f validation/STOP_L_CHAIN ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN" >> $LOG; exit 0; }; }
copyrec() { for d in runs_l/ddcheck_*; do for f in $d/validation/dd_chain_check_*.json; do [ -f "$f" ] && [ ! -f "validation/$(basename $f)" ] && cp "$f" validation/ && echo "$(date -u +%FT%TZ) copied $(basename $f) from $d" >> $LOG; done; done; }
copyrec
run ddcheck_S05_cl_$(date -u +%H%M) $GPU dd_chain.py S05_shift_c physical:c_l Jcw,Jf,Jc cuda:0
copyrec
run leval_Jcw_S01_zc_$(date -u +%H%M) $GPU l_eval.py S01_shift_a Jcw optimizer:z_c $SCOPE cuda:0
run leval_Jcw_S05_cl_$(date -u +%H%M) $GPU l_eval.py S05_shift_c Jcw physical:c_l $SCOPE cuda:0
T1=$(date -u +%FT%TZ); echo "$T1 (l) chain2 done" >> $LOG
echo "{\"ts\": \"$T1\", \"event\": \"hold_end\", \"pair\": \"P2 segment 2\", \"detail\": \"(l) chain2 ended at $T1: the named J_cw comparisons were run; the remaining checks and comparisons wait for the next free slot\"}" >> status/ledger.jsonl
# (superseded 2026-10-29T11:5xZ: every new launch must first check the lane's busy count, see validation/l_launch.sh)
