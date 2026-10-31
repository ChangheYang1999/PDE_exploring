#!/bin/bash
# P3 FREE-only continuation end actions (lead 02:11:51Z item 3; 6.3 (a) records): waits for the member's results.jsonl and its done file, then on one GPU through the busy
# guard: J_c EVAL v5 (copied into validation/jc_eval/<job>/, never overwriting), the --full end record against P3_start with the segment start p3_s2b_S20_end, the
# admitted decision wrapper (saved beside the record). No pair result (single member), no enqueue (no further P3 before the 08:30Z selection).
# Usage: bash scripts/p3_free_cont_end.sh <run dir> <gpu> <end tag> <segment-start record tag>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; export CUDA_VISIBLE_DEVICES=
RUN=$1; GPU=$2; TAG=$3; SEG=$4; LOG=validation/logs/l_slot_chain.log; JID=$(basename $RUN); JOB=$D/queue/done/$JID.json
n=0; while [ ! -f $RUN/results.jsonl ] || [ ! -f "$JOB" ]; do sleep 60; n=$((n+1)); [ $n -gt 240 ] && { echo "$(date -u +%FT%TZ) p3_free_cont_end: gave up waiting for $JID" | tee -a $LOG; exit 1; }; done
echo "$(date -u +%FT%TZ) p3_free_cont_end on GPU $GPU: $JID ended" | tee -a $LOG; grep -E "LM finished|JOB DONE" $RUN/worker.log | tail -2 | cut -c1-300
NAME=jceval_v5_${JID%%_L6*}_$(date -u +%H%M%S); ABS=$D/$RUN
bash validation/l_launch_v6.sh frozen $NAME $GPU jc_eval_state.py $ABS cuda:0 256
if [ -d runs_l/$NAME/validation/jc_eval/$JID ]; then mkdir -p validation/jc_eval/$JID; cp -n runs_l/$NAME/validation/jc_eval/$JID/* validation/jc_eval/$JID/; echo "$(date -u +%FT%TZ) J_c EVAL of $JID copied" | tee -a $LOG; else echo "$(date -u +%FT%TZ) NO EVAL output for $JID (see runs_l/$NAME)" | tee -a $LOG; fi
bash scripts/r63a_run.sh $GPU $TAG end $ABS --full --start-ref $D/validation/records_63a/P3_start.json --segment-start $D/validation/records_63a/$SEG.json
DEC=$($PY scripts/r63a_decide.py --end $TAG --ref P3_start)
echo "$(date -u +%FT%TZ) wrapper r63a_decide: --end $TAG --ref P3_start" > validation/records_63a/$TAG.decision.txt; echo "$DEC" >> validation/records_63a/$TAG.decision.txt
echo "$(date -u +%FT%TZ) 6.3 (a) decision for $TAG vs P3_start: $DEC" | tee -a $LOG
echo "$(date -u +%FT%TZ) p3_free_cont_end done (no enqueue)" | tee -a $LOG
