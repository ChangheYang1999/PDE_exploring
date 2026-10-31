#!/bin/bash
# Chain 18 (16:27Z; lead 16:19:29Z item 4): G8 omitted-part sizes for the ten other 3.1 cases (information only, reporting requirement of the G8 text; not a release condition),
# validation/g8_controls_cases.py (derived from the frozen g8_controls.py 15882759c83d7aea; case table from the command line), one frozen copy per case, GPU 4 (one slot; the other slot stays free
# for the (n)(5) evaluation). Stop between cases: touch validation/STOP_L_CHAIN18.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=0
echo "$(date -u +%FT%TZ) chain18b started (G8 omitted-part sizes, the three remaining cases; GPU 0)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN18 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN18" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
for c in manu_near_edge manu_allm_c S20_own; do
  go frozen g8cases_${c}_$(date -u +%H%M%S) $GPU g8_controls_cases.py $c gpu_v1_$c
done
echo "$(date -u +%FT%TZ) chain18 done" >> $LOG
