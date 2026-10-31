#!/bin/bash
# Third (l) chain: after chain2 (stopped after the S01 z_c named comparison), rerun the S05 c_l same-function check with the current sources
# (dd_pressure v2 per-build ranges, dd_chain v9, l_eval v4), copy its record, then the named J_cw comparison at S05_shift_c physical c_l.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=$1; SCOPE=$2; WAIT=$3
echo "$(date -u +%FT%TZ) chain3 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 10; done; rm -f validation/STOP_L_CHAIN
run() { name=$1; shift; echo "$(date -u +%FT%TZ) start $name: $*" >> $LOG; bash validation/run_frozen.sh "$name" "$@" >> $LOG 2>&1; echo "$(date -u +%FT%TZ) done $name exit $?" >> $LOG; [ -f validation/STOP_L_CHAIN ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN" >> $LOG; exit 0; }; }
mv validation/dd_chain_check_S05_shift_c_physical_c_l.json validation/dd_chain_check_S05_shift_c_physical_c_l_oldsources_1123.json 2>/dev/null
run ddcheck_S05_cl_$(date -u +%H%M) $GPU dd_chain.py S05_shift_c physical:c_l Jcw,Jf,Jc cuda:0
for d in runs_l/ddcheck_S05_cl_*; do f=$d/validation/dd_chain_check_S05_shift_c_physical_c_l.json; [ -f "$f" ] && [ ! -f validation/dd_chain_check_S05_shift_c_physical_c_l.json ] && [ "$d" != "runs_l/ddcheck_S05_cl_1123" ] && cp "$f" validation/ && echo "$(date -u +%FT%TZ) copied S05 c_l check from $d" >> $LOG; done
run leval_Jcw_S05_cl_$(date -u +%H%M) $GPU l_eval.py S05_shift_c Jcw physical:c_l $SCOPE cuda:0
T1=$(date -u +%FT%TZ); echo "$T1 (l) chain3 done" >> $LOG
echo "{\"ts\": \"$T1\", \"event\": \"hold_end\", \"pair\": \"P2 segment 2\", \"detail\": \"(l) chain3 ended at $T1: both named J_cw comparisons run; remaining items wait for the next free slot\"}" >> status/ledger.jsonl
# (superseded 2026-10-29T11:5xZ: every new launch must first check the lane's busy count, see validation/l_launch.sh)
