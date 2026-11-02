#!/bin/bash
# H13 / rule R13 (hrt-lead NOTES_FOR_TEAM, written before these games): the af2g gate, slot B, then the remaining
# best_v9e ablations of queue_ab4.sh (stopped while in ab10; the partial ab10 is in tmp/aborted/ab10-1904Z), then
# fk1 of queue_fork.sh (H12, header there) with af2g as a fifth candidate.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
G='bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null'
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "timing g13tm $G" "strike1 g13s1 $G" "targeted2 g13t2 $G" "punish g13pu $G" "handoff g13hd $G" \
           "screened g13sg $G" "guarded_maze g13gm $G" \
           "f5t ab10 $B?catch_up=false" "f5t ab11 $B?fortress_guns=false" "f5t ab12 $B?big_threat=null" \
           "growers ab16 $B?poke_insurance=false" "growers ab17 $B?mid_until=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
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
  --opponents "${OPP[@]}" --jobs 1 --keep-logs all > bot_research/runs/lead/fk1.out 2>&1
echo "end fk1 exit $? $(date -u +%FT%TZ)"
echo "== queue_g2 done $(date -u +%FT%TZ)"
