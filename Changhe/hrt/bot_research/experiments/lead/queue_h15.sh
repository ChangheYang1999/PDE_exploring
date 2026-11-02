#!/bin/bash
# H14 follow-up (hrt-lead NOTES_FOR_TEAM, entry "attack-share screen", written before its games): AS1C fails H14's
# reading rule (worse on guard_roster ["tier1","tier1"], counter_astra33 and one guarded maze). Screen: best_v9e with
# attack_share 0.75 and 0.65 (catch-up 0.5) on TIMING2 and on those three opponents. Replaces the tail of
# queue_h14.sh after each gate: drops the f5t ablations ab4-ab6 and ab10-ab12 (best_v9f's af8-af10 already cover
# big_threat, big_partial and fortress_n on f5t); keeps ab14-ab17, fk1, frr1 and frr2. Usage: queue_h15.sh A|B.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
B="$BEST_V9E"
K='bot_research.bots.counters.'
pool() {  # POOL NAME SPEC
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > $L/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
}
if [ "$1" = A ]; then
  until grep -q "^== gate A done" $L/queue_h14A.log; do sleep 5; done
  kill -- -3321012
  sleep 5
  [ -d $L/ab4 ] && mv $L/ab4 bot_research/tmp/aborted/ab4-h15 && mv $L/ab4.out bot_research/tmp/aborted/ab4-h15.out
  echo "stopped queue_h14 A after gate A $(date -u +%FT%TZ)"
  for sh in 0.75 0.65; do
    n=s${sh#0.}
    pool timing2 ${n}tm2 "$B?attack_share=$sh&catch_up_share=0.5"
    echo "start ${n}x $(date -u +%FT%TZ)"
    taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name ${n}x \
      --candidates "$B?attack_share=$sh&catch_up_share=0.5" \
      --opponents "${K}guard_roster:@make?roster=[\"tier1\",\"tier1\"]" 'bot_research.bots.defense.counter_astra33:@make' \
      "${K}guarded_maze:@make?layout=\"cash_rank_1\"&growth_rounds=6&guard_round=4&bait=[]&bait_round=2&tier=\"tier5\"&factory_cap=2000&purchase_cap=1000" \
      --jobs 1 --keep-logs all > $L/${n}x.out 2>&1
    echo "end ${n}x exit $? $(date -u +%FT%TZ)"
  done
  echo "== screen done $(date -u +%FT%TZ)"
  pool growers ab14 "$B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null"
  pool growers ab15 "$B?big_threat=null"
  echo "start frr1 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr1 \
    --round-robin "$BEST_V9E" "$BEST_V9F" "$AF2G" "$P5TNUBM" "$V41" "$V29" "$G1" "$GUARD00" "$TDEF" "$AS1C" \
    --jobs 1 --keep-logs all > $L/frr1.out 2>&1
  echo "end frr1 exit $? $(date -u +%FT%TZ)"
elif [ "$1" = B ]; then
  until grep -q "^== gate B done" $L/queue_h14B.log; do sleep 5; done
  kill -- -3321013
  sleep 5
  [ -d $L/ab10 ] && mv $L/ab10 bot_research/tmp/aborted/ab10-h15 && mv $L/ab10.out bot_research/tmp/aborted/ab10-h15.out
  echo "stopped queue_h14 B after gate B $(date -u +%FT%TZ)"
  pool growers ab16 "$B?poke_insurance=false"; pool growers ab17 "$B?mid_until=null"
  F='bot_research.experiments.lead.prefix_fork:@make'
  OPP=("$F" "$F?bait=[\"tier1\"]")
  for spec in 'fork_round=4&tier="tier3"' 'fork_round=4&tier="tier3"&budget_fraction=0.5' 'fork_round=3&tier="tier1"' \
              'fork_round=3&tier="tier2"' 'fork_round=3&tier="tier3"' 'fork_round=4&tier="tier1"' 'fork_round=4&tier="tier2"' \
              'fork_round=5&tier="tier3"' 'fork_round=5&tier="tier4"'; do
    OPP+=("$F?continuation=\"strike\"&$spec")
  done
  OPP+=("$F?continuation=\"strike\"&fork_round=4&tier=\"tier3\"&bait=[\"tier1\"]")
  echo "start fk1 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name fk1 \
    --candidates "$B" "$BEST_V9F" "$P5TNUBM" "$BEST_V9F?passive_mid_from=null" "$AF2G" \
    --opponents "${OPP[@]}" --jobs 1 --keep-logs all > $L/fk1.out 2>&1
  echo "end fk1 exit $? $(date -u +%FT%TZ)"
  echo "start frr2 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr2 \
    --round-robin "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" "$AS1C" --scenarios mirror:1:2 asym:23:2 \
    --jobs 1 --keep-logs all > $L/frr2.out 2>&1
  echo "end frr2 exit $? $(date -u +%FT%TZ)"
fi
echo "== queue_h15 $1 done $(date -u +%FT%TZ)"
