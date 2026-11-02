#!/bin/bash
# H14 (hrt-lead NOTES_FOR_TEAM 2026-10-31T20:19:29Z, written before any AS1C game): the R13 gate pools (report 5.14)
# for AS1C = frozen best_v9e with attack_share=1.0&catch_up_share=0.5. Descriptive: bots/best.py stays best_v9e.
# Replaces the tails of queue_g3b.sh (slot A, after its ab3) and queue_tm.sh (slot B, stopped in ab10) and the two
# queue_rr.sh waiters; their remaining jobs (ab4-ab6, ab14, ab15; ab10-ab12, ab16, ab17, fk1; frr1, frr2) follow the
# gate here, with AS1C added to both round robins. Usage: queue_h14.sh A|B.
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
  until grep -q "^end ab3 " $L/queue_g3b.log; do sleep 10; done
  kill -- -2094231
  sleep 5
  [ -d $L/ab4 ] && mv $L/ab4 bot_research/tmp/aborted/ab4-h14 && mv $L/ab4.out bot_research/tmp/aborted/ab4-h14.out
  echo "stopped queue_g3b after ab3 $(date -u +%FT%TZ)"
  pool targeted2 h14t2 "$AS1C"; pool timing2 h14tm2 "$AS1C"; pool f5t h14f "$AS1C"
  pool guarded_maze h14gm "$AS1C"; pool staged h14st "$AS1C"
  echo "== gate A done $(date -u +%FT%TZ)"
  pool f5t ab4 "$B?big_partial=false"; pool f5t ab5 "$B?fortress_n=null"; pool f5t ab6 "$B?attack_mode=\"current\""
  pool growers ab14 "$B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null"
  pool growers ab15 "$B?big_threat=null"
  echo "start frr1 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr1 \
    --round-robin "$BEST_V9E" "$BEST_V9F" "$AF2G" "$P5TNUBM" "$V41" "$V29" "$G1" "$GUARD00" "$TDEF" "$AS1C" \
    --jobs 1 --keep-logs all > $L/frr1.out 2>&1
  echo "end frr1 exit $? $(date -u +%FT%TZ)"
elif [ "$1" = B ]; then
  echo "start h14pc $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name h14pc \
    --candidates "$AS1C" \
    --opponents "${K}budget_timing:@make?tier=\"tier3\"&attack_round=4&budget_fraction=0.65" \
    "${K}budget_timing:@make?tier=\"tier4\"&attack_round=6&budget_fraction=0.65" \
    "${K}guard_geometry:@make?roster=[\"tier1\"]&x=9&y=2" "${K}guard_geometry:@make?roster=[\"tier2\"]&x=10&y=2" \
    --jobs 1 --keep-logs all > $L/h14pc.out 2>&1
  echo "end h14pc exit $? $(date -u +%FT%TZ)"
  pool timing h14tm "$AS1C"; pool strike1 h14s1 "$AS1C"; pool punish h14pu "$AS1C"; pool bluffcov h14b "$AS1C"
  pool targeted3_p5tf h14t3 "$AS1C"; pool handoff h14hd "$AS1C"; pool screened h14sg "$AS1C"
  pool growers h14g "$AS1C"
  pool targeted2 h14t2b "$B?attack_share=1.0"
  echo "== gate B done $(date -u +%FT%TZ)"
  pool f5t ab10 "$B?catch_up=false"; pool f5t ab11 "$B?fortress_guns=false"; pool f5t ab12 "$B?big_threat=null"
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
echo "== queue_h14 $1 done $(date -u +%FT%TZ)"
