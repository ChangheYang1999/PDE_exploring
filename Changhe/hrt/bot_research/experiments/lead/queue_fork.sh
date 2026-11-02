#!/bin/bash
# H12 (written 2026-10-31T18:57Z, before any game against these opponents): prefix-fork opponents (experiments/lead/prefix_fork.py)
# play the no-bait lead_opening grower (growth 6) before fork_round, then either keep growing or strike with
# budget_timing. Prediction: best_v9e wins or draws every strike and loses the grow continuation; best_v9f,
# P5TNUBM and V33M win the grow continuation and each loses at least one strike. Check of the determinism argument:
# each candidate's actions in rounds 1..fork_round are the same against all continuations with the same prefix
# (experiments/lead/fork_check.py on the logs). Development only. Runs after the PID in $1 exits (one slot).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 "$1" 2>/dev/null; do sleep 20; done
F='bot_research.experiments.lead.prefix_fork:@make'
OPP=("$F" "$F?bait=[\"tier1\"]")
for spec in 'fork_round=4&tier="tier3"' 'fork_round=4&tier="tier3"&budget_fraction=0.5' 'fork_round=3&tier="tier1"' \
            'fork_round=3&tier="tier2"' 'fork_round=3&tier="tier3"' 'fork_round=4&tier="tier1"' 'fork_round=4&tier="tier2"' \
            'fork_round=5&tier="tier3"' 'fork_round=5&tier="tier4"'; do
  OPP+=("$F?continuation=\"strike\"&$spec")
done
OPP+=("$F?continuation=\"strike\"&fork_round=4&tier=\"tier3\"&bait=[\"tier1\"]")
P5='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5'
date -u +"%FT%TZ fk1 start"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name fk1 \
  --candidates bot_research.experiments.lead.frozen.best_v9e:@make bot_research.experiments.lead.frozen.best_v9f:@make \
  "$P5" 'bot_research.experiments.lead.frozen.best_v9f:@make?passive_mid_from=null' \
  --opponents "${OPP[@]}" --jobs 1 --keep-logs all
date -u +"%FT%TZ fk1 done"
