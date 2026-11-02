#!/bin/bash
# Slot B after the R13 gate: a descriptive TIMING2 screen (not a candidate for bots/best.py, which changes at most once,
# at the R13 selection note). hrt-w2 (notes/economy.md 18.6, 18.10) found that budget_timing's map locks at round 20
# (S = 1510) in all 40 TIMING2 games of best_v9e's twin, that best_v9e lands no hit in rounds 6-19 and spends a
# median 520 gold on minions in rounds 2-12, while V29, g1 and g0 win all 40 with hits in rounds 6-19.
# First gmchk (below). Question of tsc: which single rule of best_v9e blocks the early attacks? One option each on the 40 TIMING2 conditions:
# attack_mode="current" (no robust rule), big_threat=null (no all-gold insurance, rule 3b), fortress_n=null (no
# splash-only fortress trigger), attack_share=1.0. Then the rest of queue_g2.sh (ab10-ab12, ab16, ab17, fk1).
# Waits for "end g13gm" in queue_g2.log, then stops queue_g2 (PGID 128523) and keeps its partial ab10 in tmp/aborted.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
until grep -q "^end g13gm" $L/queue_g2.log; do sleep 20; done
sleep 2
kill -- -128523
sleep 5
echo "stopped queue_g2 $(date -u +%FT%TZ)"
ps -eo pid,pgid,args | grep -v grep | grep "name ab10" && echo "WARNING ab10 still running"
[ -d $L/ab10 ] && mv $L/ab10 bot_research/tmp/aborted/ab10-$(date -u +%H%MZ)
[ -f $L/ab10.out ] && mv $L/ab10.out bot_research/tmp/aborted/ab10-$(date -u +%H%MZ).out
B='bot_research.experiments.lead.frozen.best_v9e:@make'
G='bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null'
# gmchk: the GUARDED_MAZE condition (found at 78 of 144 rows) where g13gm (af2g) loses and the base gm2 (best_v9e's twin V18FT) wins,
# replayed with the frozen best_v9e file itself in the same run (R13 condition 1), together with best_v9e plus each
# one of af2g's four changed values (which of them loses this condition; descriptive).
GM='bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000'
echo "start gmchk $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name gmchk --candidates "$B" "$G" \
  "$B?poke_reactive=\"turret_only\"" "$B?fail_limit=2" "$B?robust_k=null" "$B?behind_mode=\"current\"" \
  --opponents "$GM" --jobs 1 --keep-logs all > $L/gmchk.out 2>&1
echo "end gmchk exit $? $(date -u +%FT%TZ)"
echo "start tsc (timing2) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh timing2 tsc "'$B?attack_mode=\"current\"' '$B?big_threat=null' '$B?fortress_n=null' '$B?attack_share=1.0'" --keep-logs all > $L/tsc.out 2>&1
echo "end tsc exit $? $(date -u +%FT%TZ)"
for job in "f5t ab10 $B?catch_up=false" "f5t ab11 $B?fortress_guns=false" "f5t ab12 $B?big_threat=null" \
           "growers ab16 $B?poke_insurance=false" "growers ab17 $B?mid_until=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > $L/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
F='bot_research.experiments.lead.prefix_fork:@make'
OPP=("$F" "$F?bait=[\"tier1\"]")
for spec in 'fork_round=4&tier="tier3"' 'fork_round=4&tier="tier3"&budget_fraction=0.5' 'fork_round=3&tier="tier1"' \
            'fork_round=3&tier="tier2"' 'fork_round=3&tier="tier3"' 'fork_round=4&tier="tier1"' 'fork_round=4&tier="tier2"' \
            'fork_round=5&tier="tier3"' 'fork_round=5&tier="tier4"'; do
  OPP+=("$F?continuation=\"strike\"&$spec")
done
OPP+=("$F?continuation=\"strike\"&fork_round=4&tier=\"tier3\"&bait=[\"tier1\"]")
P5='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5'
echo "start fk1 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name fk1 \
  --candidates "$B" bot_research.experiments.lead.frozen.best_v9f:@make "$P5" \
  'bot_research.experiments.lead.frozen.best_v9f:@make?passive_mid_from=null' "$G" \
  --opponents "${OPP[@]}" --jobs 1 --keep-logs all > $L/fk1.out 2>&1
echo "end fk1 exit $? $(date -u +%FT%TZ)"
echo "== queue_tm done $(date -u +%FT%TZ)"
