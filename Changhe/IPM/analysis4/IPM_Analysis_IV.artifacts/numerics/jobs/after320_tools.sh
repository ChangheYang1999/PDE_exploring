#!/bin/bash
# wait until the 2/3 checkpoint contains order 320 (mtime newer than 08:00Z), then run the t-profile and band tools at 320
cd .
PY=python3
while [ "$(stat -c %Y ckpt/log_sin1_c3_p512.pkl)" -lt "$(date -d '2026-10-31T08:00:00Z' +%s)" ]; do sleep 20; done
sleep 60
$PY code/tprofile.py ckpt/log_sin1_c3_p512.pkl 320 20,-20,40,-40 > notes/tprofile_320.txt 2>&1
$PY code/diagonal_bands.py ckpt/log_sin1_c3_p512.pkl 320 0,1,10,20,40,60 > notes/bands_320.txt 2>&1
