#!/bin/bash
# P3 pair SEGMENT-2 end actions (lead 02:11:51Z item 1; RUN_STATUS shift-6 handover; SPEC 3.6 (h) pair result; 6.3 (a) records): waits until both segment-2
# members have written results.jsonl (the worker's end battery) and the FREE job is in queue/done, then on ONE GPU, one at a time through the busy guard
# (validation/l_launch_v6.sh): J_c EVAL v5 of the FREE member and of the FIXED-CONTROL member (copied into validation/jc_eval/<job>/ after each EVAL
# finished, never overwriting), the pair result over BOTH segments (scripts/pair_result.py P3s2, matched 164 it / 7200 s), the FREE end record (--full)
# against P3_start with the segment start p3_s1b_S20_end, then the admitted decision wrapper (saved beside the record). No enqueue: P3 segment 3 is
# not run before the 08:30Z selection (lead 02:11:51Z item 1: FREE rate 0.87 per cent per hour, below the rule). Derived from scripts/p3_end_actions.sh (segment 1).
# Usage: bash scripts/p3_end_actions_s2.sh <gpu>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; export CUDA_VISIBLE_DEVICES=
GPU=$1; LOG=validation/logs/l_slot_chain.log
FREE1=runs/p3_s1b_S20_L6_cl0.4500_om1.0000_free; FIXED1=runs/p3c_s1b_S20_L6_cl0.4500_om1.0000_fixed
FREE=runs/p3_s2b_S20_L6_cl0.4500_om1.0000_free; FIXED=runs/p3c_s2b_S20_L6_cl0.4500_om1.0000_fixed; JOB=$D/queue/done/p3_s2b_S20_L6_cl0.4500_om1.0000_free.json
n=0; while [ ! -f $FREE/results.jsonl ] || [ ! -f $FIXED/results.jsonl ] || [ ! -f "$JOB" ]; do sleep 60; n=$((n+1)); [ $n -gt 180 ] && { echo "$(date -u +%FT%TZ) p3_end_actions_s2: gave up waiting for the P3 segment-2 end batteries" | tee -a $LOG; exit 1; }; done
echo "$(date -u +%FT%TZ) p3_end_actions_s2 on GPU $GPU: both P3 segment-2 members ended" | tee -a $LOG
grep -E "LM finished|JOB DONE" $FREE/worker.log | tail -2 | cut -c1-300; grep -E "LM finished|JOB DONE" $FIXED/worker.log | tail -2 | cut -c1-300
for R in $FREE $FIXED; do
  JID=$(basename $R); ABS=$D/$R; NAME=jceval_v5_${JID%%_L6*}_$(date -u +%H%M%S)
  bash validation/l_launch_v6.sh frozen $NAME $GPU jc_eval_state.py $ABS cuda:0 256
  if [ -d runs_l/$NAME/validation/jc_eval/$JID ]; then mkdir -p validation/jc_eval/$JID; cp -n runs_l/$NAME/validation/jc_eval/$JID/* validation/jc_eval/$JID/; echo "$(date -u +%FT%TZ) J_c EVAL of $JID copied: $(ls -la validation/jc_eval/$JID | tail -n +2 | awk '{print $5, $9}' | tr '\n' ' ')" | tee -a $LOG; else echo "$(date -u +%FT%TZ) NO EVAL output for $JID (see runs_l/$NAME)" | tee -a $LOG; fi
done
$PY scripts/pair_result.py P3s2 $FREE1,$FREE $FIXED1,$FIXED --it 164 --wall 7200 --flag "P3 pair (S20_own all-m class), segments 1 and 2 (equal nominal allowances 3600 s each; both members alone on their GPUs: segment 1 FREE GPU 6 / FIXED-CONTROL GPU 5 launched together 20:09:51Z; segment 2 FREE GPU 5 / FIXED-CONTROL GPU 6 launched together 01:08:49Z under scripts/enqueue_pair_under_lock.sh; max_iter FREE 164 = 44 + 120, FIXED-CONTROL 228 = 108 + 120; the FIXED-CONTROL member reaches 164 accepted iterations inside segment 2)" | tee validation/logs/pair_result_P3s2.out
bash scripts/r63a_run.sh $GPU p3_s2b_S20_end end $D/$FREE --full --start-ref $D/validation/records_63a/P3_start.json --segment-start $D/validation/records_63a/p3_s1b_S20_end.json
DEC=$($PY scripts/r63a_decide.py --end p3_s2b_S20_end --ref P3_start)
echo "$(date -u +%FT%TZ) wrapper r63a_decide: --end p3_s2b_S20_end --ref P3_start" > validation/records_63a/p3_s2b_S20_end.decision.txt; echo "$DEC" >> validation/records_63a/p3_s2b_S20_end.decision.txt
echo "$(date -u +%FT%TZ) 6.3 (a) decision for p3_s2b_S20_end vs P3_start: $DEC" | tee -a $LOG
echo "$(date -u +%FT%TZ) p3_end_actions_s2 done (no enqueue; P3 segment 3 not before the 08:30Z selection)" | tee -a $LOG
