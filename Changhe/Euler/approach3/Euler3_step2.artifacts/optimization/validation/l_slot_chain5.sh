#!/bin/bash
# Fifth (l) chain: after the S05 c_l named comparison, the elementary-function qualification of the S01 z_c stencil set (lead 11:29:05Z (b), 11:41:09Z,
# 11:35:30Z item 2; V277) from a frozen copy on GPU 5, tied to the earlier copy runs_l/leval_Jcw_S01_zc_1133; then the hold on P2 segment 2 ends.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=$1; WAIT=$2
echo "$(date -u +%FT%TZ) chain5 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 10; done
T0=$(date -u +%FT%TZ); echo "{\"ts\": \"$T0\", \"event\": \"hold\", \"pair\": \"P2 segment 2 (staged 11:45Z)\", \"reason\": \"elementary-function qualification of the S01 z_c stencil set (l_trig_qual, about 25 min) on GPU 5; the hold window of 45 min from 11:44Z ends about 12:29Z, the chain stops itself at 12:27Z if still running\", \"start\": \"$T0\"}" >> status/ledger.jsonl
( sleep $(( $(date -u -d "2026-10-29T12:27:00Z" +%s) - $(date -u +%s) )) 2>/dev/null; touch validation/STOP_TRIGQUAL ) &
echo "$(date -u +%FT%TZ) start trigqual_S01_zc" >> $LOG
bash validation/run_frozen.sh trigqual_S01_zc_$(date -u +%H%M) $GPU l_trig_qual.py S01_shift_a optimizer:z_c validation/gates_gpu_v1_S01_shift_a.json cuda:0 RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/leval_Jcw_S01_zc_1133 >> $LOG 2>&1 &
QP=$!
while kill -0 $QP 2>/dev/null; do if [ -f validation/STOP_TRIGQUAL ]; then pkill -P $QP 2>/dev/null; echo "$(date -u +%FT%TZ) trig qualification stopped at the hold limit (12:27Z); to be rerun in the next free slot" >> $LOG; break; fi; sleep 10; done
wait $QP 2>/dev/null; rm -f validation/STOP_TRIGQUAL
T1=$(date -u +%FT%TZ); echo "$T1 chain5 done" >> $LOG
echo "{\"ts\": \"$T1\", \"event\": \"hold_end\", \"pair\": \"P2 segment 2\", \"detail\": \"chain5 (trig qualification S01 z_c) ended at $T1; GPU 5 clear\"}" >> status/ledger.jsonl
# (superseded 2026-10-29T11:5xZ: every new launch must first check the lane's busy count, see validation/l_launch.sh)
