#!/bin/bash
cd .
while kill -0 3889500 2>/dev/null; do sleep 30; done
# continue midpoint-only (radius rule disabled) to 350 if the run stopped before 350
python3 -u code/logff.py --tag log_sin1_c3_p512 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9
