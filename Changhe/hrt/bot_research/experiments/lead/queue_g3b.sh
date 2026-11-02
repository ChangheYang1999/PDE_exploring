#!/bin/bash
# Slot A after the R13 gate (replaces queue_g3.sh, whose gx1-gx4 specs were wrong: the frozen best_v9e has no
# robust_k or behind_mode parameter, and its poke_reactive="turret_only" acts like poke_reactive=true). Which of the
# four values that separate af2g from best_v9e carries af2g's GUARDED_MAZE loss and its GROWERS gain: af2g with one
# best_v9e value restored at a time (poke_reactive="turret", fail_limit=1, robust_k=2, behind_mode=null; all four
# together give best_v9e, tests/test_best.py OPTION_SPECS of best_v9f). Descriptive, no selection depends on it.
# gmchk2: the GUARDED_MAZE condition lost by af2g (see queue_tm.sh), both seats; gy1-gy4: GROWERS (142 games).
# Then the rest of queue_g1.sh (ab3-ab6, ab14, ab15). Waits for "end g13st" in queue_g1.log, then stops queue_g1
# (PGID 127418) and keeps its partial ab3 in tmp/aborted.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
until grep -q "^end g13st" $L/queue_g1.log; do sleep 20; done
sleep 2
kill -- -127418
sleep 5
echo "stopped queue_g1 $(date -u +%FT%TZ)"
ps -eo pid,pgid,args | grep -v grep | grep "name ab3" && echo "WARNING ab3 still running"
[ -d $L/ab3 ] && mv $L/ab3 bot_research/tmp/aborted/ab3-$(date -u +%H%MZ)
[ -f $L/ab3.out ] && mv $L/ab3.out bot_research/tmp/aborted/ab3-$(date -u +%H%MZ).out
G='bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null'
B='bot_research.experiments.lead.frozen.best_v9e:@make'
GM='bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000'
echo "start gmchk2 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name gmchk2 \
  --candidates "$G&poke_reactive=\"turret\"" "$G&fail_limit=1" "$G&robust_k=2" "$G&behind_mode=null" \
  --opponents "$GM" --jobs 1 --keep-logs all > $L/gmchk2.out 2>&1
echo "end gmchk2 exit $? $(date -u +%FT%TZ)"
for job in "growers gy1 $G&poke_reactive=\"turret\"" "growers gy2 $G&fail_limit=1" "growers gy3 $G&robust_k=2" \
           "growers gy4 $G&behind_mode=null" \
           "f5t ab3 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "f5t ab4 $B?big_partial=false" \
           "f5t ab5 $B?fortress_n=null" "f5t ab6 $B?attack_mode=\"current\"" \
           "growers ab14 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "growers ab15 $B?big_threat=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > $L/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_g3b done $(date -u +%FT%TZ)"
