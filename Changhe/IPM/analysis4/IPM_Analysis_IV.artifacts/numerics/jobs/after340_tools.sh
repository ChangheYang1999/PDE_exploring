#!/bin/bash
cd .
PY=python3
while [ "$(stat -c %Y ckpt/log_sin1_c3_p512.pkl)" -lt "$(date -d '2026-10-31T10:30:00Z' +%s)" ]; do sleep 20; done
sleep 90
$PY code/tprofile.py ckpt/log_sin1_c3_p512.pkl 340 20,-20,40,-40 > notes/tprofile_340.txt 2>&1
$PY code/diagonal_bands.py ckpt/log_sin1_c3_p512.pkl 340 0,1,10,20,40,60 > notes/bands_340.txt 2>&1
$PY code/lead_stream_ratio_modes.py ckpt/log_sin1_c3_p512.pkl notes/stream_ratio_modes_331_340.json 331 332 333 334 335 336 337 338 339 340 > logs/stream_ratio_modes_331_340.out 2>&1
