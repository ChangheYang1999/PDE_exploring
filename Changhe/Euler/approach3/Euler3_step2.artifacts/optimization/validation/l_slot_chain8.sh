#!/bin/bash
# Chain 8 v7 (lead 13:35:25Z item 1: chain 8 split; this part keeps the g24 records on GPU 6 in the release order; cases with an existing record or copy are skipped).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=6
echo "$(date -u +%FT%TZ) chain8 v7 started (g24 remainder)" >> $LOG
go() { [ -f validation/STOP_L_CHAIN8 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN8" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
for c in S01_own S09_own S05_own manu_large_omega S01_shift_a S05_shift_c S20_own S11_own manu_a manu_allm_c manu_small_omega manu_near_edge; do
  [ -f validation/gates_gpu_v1_$c.json ] || continue
  if [ -f validation/g24_complete_$c.json ] || ls runs_l/ 2>/dev/null | grep -q "^g24_${c}_"; then continue; fi
  go frozen g24_${c}_$(date -u +%H%M%S) $GPU g24_complete.py $c RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_$c.json cuda:0
done
echo "$(date -u +%FT%TZ) chain8 v7 done" >> $LOG
