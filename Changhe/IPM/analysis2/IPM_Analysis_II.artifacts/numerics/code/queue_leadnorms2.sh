#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
while [ $(pgrep -fc "python3 .*code/(n12_run|n12_norms|cert_sups)[.]py") -ge 2 ]; do sleep 30; done
for f in state131_T1_exact n12_m8_exact n12_m10_exact; do nice -n 5 $P code/n12_norms.py data/$f.json -6.9 9.21 240 24 L data/${f}_lead.json > runs/lead_$f.log 2>&1; done
echo "done $(date -u +%FT%TZ)" >> runs/queue_leadnorms2.done
