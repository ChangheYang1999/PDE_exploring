#!/bin/bash
# wait for the from329 continuation (parent pid 2491233) to finish at N = 350, keep a copy of the 350 state, run the 350 checkpoint tools
# on the copy, then continue the same run (midpoint continuation, honest propagation radii) to N = 400 on cores 13-16.
cd .
PY=python3
while kill -0 2491233 2>/dev/null; do sleep 20; done
sleep 30
grep -q '"done"' logs/log_sin1_c3_from329.jsonl || echo "WARNING: no done line in the from329 log" >> logs/after350_continue.out
cp ckpt/log_sin1_c3_from329.pkl ckpt/log_sin1_c3_N350.pkl
echo "$(date -u +%FT%TZ) copied 350 state" >> logs/after350_continue.out
taskset -c 13 nice -n 19 $PY code/tprofile.py ckpt/log_sin1_c3_N350.pkl 350 20,-20,40,-40 > notes/tprofile_350.txt 2>&1
taskset -c 14 nice -n 19 $PY code/diagonal_bands.py ckpt/log_sin1_c3_N350.pkl 350 0,1,10,20,40,60 > notes/bands_350.txt 2>&1 &
taskset -c 15 nice -n 19 $PY code/lead_stream_ratio_modes.py ckpt/log_sin1_c3_N350.pkl notes/stream_ratio_modes_341_350.json 341 342 343 344 345 346 347 348 349 350 > logs/stream_ratio_modes_341_350.out 2>&1 &
wait
echo "$(date -u +%FT%TZ) tools done; relaunching to 400" >> logs/after350_continue.out
setsid nohup taskset -c 13,14,15,16 nice -n 19 $PY -u code/logff.py --tag log_sin1_c3_from329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 400 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9 >> logs/log_sin1_c3_from329.out 2>&1 &
echo "$(date -u +%FT%TZ) relaunched pid $!" >> logs/after350_continue.out
