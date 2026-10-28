#!/bin/bash
# continuation of the branch-6 run once its exact projection is done (so the two do not compete for a slot)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
while ! grep -q "b6 exact done" runs/after_b6.log 2>/dev/null; do sleep 20; done
N12_EXTRA_ORDERS=$PWD/data/stationary_order7.json N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN="2:100" ./code/nb_launch.sh nb_b6b 48 32 40 0.0002 data/nb_b6_result.json 0,1 6:69:X16+8
echo "  (env N12_EXTRA_ORDERS=data/stationary_order7.json N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN=2:100; extra spec 6:69:X16+8; continuation of nb_b6)" >> runs/nb_launch.log
