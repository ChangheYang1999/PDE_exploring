#!/bin/bash
# when m14 ends: exact projection + norms (sigma set, lead set) of m14; then the splice evaluation (lead route H2) for m10 at R = 16, 32, 64, 128, 256
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/n12_m14.log || ! grep -q "^FINAL" runs/n12_m14.log; do sleep 30; done
nice -n 5 $P code/n12_exact.py data/n12_m14_result.json $CK $FT data/n12_m14_exact.json > runs/n12_m14_exact.log 2>&1
nice -n 5 $P code/n12_norms.py data/n12_m14_exact.json -6.9 9.21 240 24 0.15,0.3,0.4 data/n12_m14_norms.json > runs/n12_m14_norms.log 2>&1
nice -n 5 $P code/n12_norms.py data/n12_m14_exact.json -6.9 9.21 240 24 L data/n12_m14_exact_lead.json > runs/lead_n12_m14_exact.log 2>&1
echo "m14 finalized at $(date -u +%FT%TZ)" >> runs/queue_after_m14.log
nice -n 5 $P code/splice_norms.py data/state131_T1_exact.json $FT 32 60 8 > runs/splice_test.log 2>&1
for R in 16 32 64 128 256; do nice -n 5 $P code/splice_norms.py data/n12_m10_exact.json $FT $R 200 24 > runs/splice_m10_R$R.log 2>&1; done
echo "splice runs finished at $(date -u +%FT%TZ)" >> runs/queue_after_m14.log
