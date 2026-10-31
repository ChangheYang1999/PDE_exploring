#!/bin/bash
# (l) work chain in the slots freed by P2's segment-1 end (lead 09:39:59Z item 3: the (l) differences may hold the next production enqueue at most 45 min;
# ledger hold rows appended). Waits for the given pids, then runs, one process at a time, from frozen copies (validation/run_frozen.sh):
# dd_elementary self-test (CPU), dd checks (S01 z_c; S05 c_l; S05 z_c; S01 physical c_l; S01 physical omega), then l_eval J_cw for the two named
# comparisons. Items can be stopped with validation/STOP_L_CHAIN. GPU: the first clear GPU is taken from the argument.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3; LOG=validation/logs/l_slot_chain.log
GPU=$1; SCOPE=$2; shift 2; PIDS="$*"
echo "$(date -u +%FT%TZ) chain armed: wait for pids $PIDS; GPU $GPU; scope $SCOPE" >> $LOG
for p in $PIDS; do while kill -0 $p 2>/dev/null; do sleep 15; done; done
T0=$(date -u +%FT%TZ); echo "$T0 pids gone; (l) chain starts" >> $LOG
echo "{\"ts\": \"$T0\", \"event\": \"hold\", \"pair\": \"P2 segment 2 (to be enqueued)\", \"reason\": \"(l) work in the freed slots: dd same-function checks and the two named J_cw comparisons from frozen copies (lead 09:39:59Z item 3: at most 45 min)\", \"start\": \"$T0\"}" >> status/ledger.jsonl
run() { name=$1; shift; echo "$(date -u +%FT%TZ) start $name: $*" >> $LOG; bash validation/run_frozen.sh "$name" "$@" >> $LOG 2>&1; echo "$(date -u +%FT%TZ) done $name exit $?" >> $LOG; [ -f validation/STOP_L_CHAIN ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN" >> $LOG; exit 0; }; }
run ddelem_$(date -u +%H%M) cpu dd_elementary.py
run ddcheck_S01_zc_$(date -u +%H%M) $GPU dd_chain.py S01_shift_a optimizer:z_c Jcw,Jf,Jc cuda:0
run ddcheck_S05_cl_$(date -u +%H%M) $GPU dd_chain.py S05_shift_c physical:c_l Jcw,Jf,Jc cuda:0
run ddcheck_S05_zc_$(date -u +%H%M) $GPU dd_chain.py S05_shift_c optimizer:z_c Jcw,Jf,Jc cuda:0
run ddcheck_S01_cl_$(date -u +%H%M) $GPU dd_chain.py S01_shift_a physical:c_l Jf cuda:0
run ddcheck_S01_om_$(date -u +%H%M) $GPU dd_chain.py S01_shift_a physical:omega Jf cuda:0
# copy the same-function records into validation/ (no overwrite) so that l_eval's frozen copy finds them
for d in runs_l/ddcheck_*; do for f in $d/validation/dd_chain_check_*.json; do [ -f "$f" ] && [ ! -f "validation/$(basename $f)" ] && cp "$f" validation/; done; done
run leval_Jcw_S01_zc_$(date -u +%H%M) $GPU l_eval.py S01_shift_a Jcw optimizer:z_c $SCOPE cuda:0
run leval_Jcw_S05_cl_$(date -u +%H%M) $GPU l_eval.py S05_shift_c Jcw physical:c_l $SCOPE cuda:0
T1=$(date -u +%FT%TZ); echo "$T1 (l) chain done" >> $LOG
echo "{\"ts\": \"$T1\", \"event\": \"hold_end\", \"pair\": \"P2 segment 2\", \"detail\": \"(l) chain ended at $T1 (started $T0)\"}" >> status/ledger.jsonl
# (superseded 2026-10-29T11:5xZ: every new launch must first check the lane's busy count, see validation/l_launch.sh)
