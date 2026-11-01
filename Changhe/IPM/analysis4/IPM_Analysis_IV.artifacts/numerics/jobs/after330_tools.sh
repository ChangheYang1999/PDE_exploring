#!/bin/bash
cd .
PY=python3
while [ "$(stat -c %Y ckpt/log_sin1_c3_p512.pkl)" -lt "$(date -d '2026-10-31T09:33:00Z' +%s)" ]; do sleep 20; done
sleep 60
$PY code/tprofile.py ckpt/log_sin1_c3_p512.pkl 330 20,-20,40,-40 > notes/tprofile_330.txt 2>&1
$PY code/diagonal_bands.py ckpt/log_sin1_c3_p512.pkl 330 0,1,10,20,40,60 > notes/bands_330.txt 2>&1
$PY code/lead_stream_ratio_modes.py ckpt/log_sin1_c3_p512.pkl notes/stream_ratio_modes_321_330.json 321 322 323 324 325 326 327 328 329 330 > logs/stream_ratio_modes_321_330.out 2>&1
