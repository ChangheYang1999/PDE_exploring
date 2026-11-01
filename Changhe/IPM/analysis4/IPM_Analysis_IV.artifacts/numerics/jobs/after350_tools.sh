#!/bin/bash
cd .
PY=python3
# wait for the 2/3 log to contain the 'done' line of the continuation (N 350), then the final checkpoint
until tail -1 logs/log_sin1_c3_p512.jsonl | grep -q '"done"'; do sleep 30; done
sleep 30
$PY code/tprofile.py ckpt/log_sin1_c3_p512.pkl 350 20,-20,40,-40 > notes/tprofile_350.txt 2>&1
$PY code/diagonal_bands.py ckpt/log_sin1_c3_p512.pkl 350 0,1,10,20,40,60 > notes/bands_350.txt 2>&1
$PY code/lead_stream_ratio_modes.py ckpt/log_sin1_c3_p512.pkl notes/stream_ratio_modes_341_350.json 341 342 343 344 345 346 347 348 349 350 > logs/stream_ratio_modes_341_350.out 2>&1
$PY code/regen_log.py --log ckpt/log_sin1_c3_p512.pkl > logs/regen_350.out 2>&1
