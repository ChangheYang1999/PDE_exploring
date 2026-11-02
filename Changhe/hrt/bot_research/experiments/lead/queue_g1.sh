#!/bin/bash
# H13 / rule R13 (hrt-lead NOTES_FOR_TEAM, written before these games): the af2g gate, slot A, then the remaining
# best_v9e ablations of queue_ab3.sh (stopped while in ab3; the partial ab3 is in tmp/aborted/ab3-1904Z).
# af2g = frozen best_v9f with passive_until=null = best_v9e plus poke_reactive="turret_only", fail_limit=2,
# robust_k=null, behind_mode="current". PCS: the four pool C spec opponents C-08 to C-11, standard start, with the
# frozen best_v9e in the same run.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
G='bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null'
E='bot_research.experiments.lead.frozen.best_v9e:@make'
K='bot_research.bots.counters.'
echo "start g13pc $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name g13pc \
  --candidates "$G" "$E" \
  --opponents "${K}budget_timing:@make?tier=\"tier3\"&attack_round=4&budget_fraction=0.65" \
  "${K}budget_timing:@make?tier=\"tier4\"&attack_round=6&budget_fraction=0.65" \
  "${K}guard_geometry:@make?roster=[\"tier1\"]&x=9&y=2" "${K}guard_geometry:@make?roster=[\"tier2\"]&x=10&y=2" \
  --jobs 1 --keep-logs all > bot_research/runs/lead/g13pc.out 2>&1
echo "end g13pc exit $? $(date -u +%FT%TZ)"
B="$E"
for job in "timing2 g13tm2 $G" "f5t g13f $G" "targeted3_p5tf g13t3 $G" "bluffcov g13b $G" "staged g13st $G" \
           "f5t ab3 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "f5t ab4 $B?big_partial=false" \
           "f5t ab5 $B?fortress_n=null" "f5t ab6 $B?attack_mode=\"current\"" \
           "growers ab14 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "growers ab15 $B?big_threat=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_g1 done $(date -u +%FT%TZ)"
