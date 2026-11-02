#!/bin/bash
# Self-forecast known-policy screens for the econ14 settings and v13 late_round=4, one at a time (1 core).
cd "$(dirname "${BASH_SOURCE[0]}")/../.."  # bot_research/
E=bot_research/experiments/economy
C14=bot_research.bots.economy.frozen.v14.econ14:@make
C13=bot_research.bots.economy.frozen.v13.econ13:@make
export JOBS=1
experiments/economy/run_tourn.sh k14a $E/opp_k14a.txt "" "$C14?early_threat=20" > runs/economy/k14a.log 2>&1
experiments/economy/run_tourn.sh k14b $E/opp_k14b.txt "" "$C14?early_threat=20&early_partial=\"best\"" > runs/economy/k14b.log 2>&1
experiments/economy/run_tourn.sh k14c $E/opp_k14c.txt "" "$C14?early_threat=50&early_partial=\"best\"" > runs/economy/k14c.log 2>&1
experiments/economy/run_tourn.sh k14d $E/opp_k14d.txt "" "$C14?early_threat=20&early_partial=\"best\"&early_share=0.5" > runs/economy/k14d.log 2>&1
experiments/economy/run_tourn.sh k13lr4 $E/opp_known13_lr4.txt "" "$C13?late_round=4" > runs/economy/k13lr4.log 2>&1
