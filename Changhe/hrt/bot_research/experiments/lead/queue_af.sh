#!/bin/bash
# Slot B after queue_bse (written 2026-10-31T17:35Z): second half of the ablation ladder of the frozen best_v9f (V33C): GROWERS
# without the passive rule, without its round-5 mid step and without any insurance (af2g, af3g, af14g), then f5t
# without big_threat, big_partial, the fortress trigger, the adaptive attack, catch_up and fortress_guns (af8-af13).
# The step added in V33C (passive_cheap_from) is ablated by P5TNUBM's existing runs (same code with the step off).
# Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9f:@make'
for job in "growers af2g $B?passive_until=null" "growers af3g $B?passive_mid_from=null" \
           "growers af14g $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" \
           "f5t af8 $B?big_threat=null" "f5t af9 $B?big_partial=false" "f5t af10 $B?fortress_n=null" \
           "f5t af11 $B?attack_mode=\"current\"" "f5t af12 $B?catch_up=false" "f5t af13 $B?fortress_guns=false"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_af done $(date -u +%FT%TZ)"
