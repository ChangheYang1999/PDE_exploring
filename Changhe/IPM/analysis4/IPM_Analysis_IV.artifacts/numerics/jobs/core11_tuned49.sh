#!/bin/bash
cd .
PY=python3
$PY -u code/tuned_general.py --tag tuned49_r5_p1024 --a 4 --b 9 --poly-coeffs @notes/tuned49_poly.json --root-guess 1.85667533842 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned49_r5_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned49_r1_p1024 --a 4 --b 9 --poly-coeffs @notes/tuned49_poly.json --root-guess 0.0634372744551 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned49_r1_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned49_r4_p1024 --a 4 --b 9 --poly-coeffs @notes/tuned49_poly.json --root-guess 0.422376482787 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned49_r4_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned49_r3_p1024 --a 4 --b 9 --poly-coeffs @notes/tuned49_poly.json --root-guess 0.269830839397 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned49_r3_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned49_r2_p1024 --a 4 --b 9 --poly-coeffs @notes/tuned49_poly.json --root-guess 0.152429987519 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned49_r2_p1024.out 2>&1
