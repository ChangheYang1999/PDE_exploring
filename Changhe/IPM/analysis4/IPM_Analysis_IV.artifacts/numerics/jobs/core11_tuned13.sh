#!/bin/bash
cd .
PY=python3
$PY -u code/tuned_general.py --tag tuned13_r6_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.51215647362036 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r6_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned13_r1_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess -0.60872691379266 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r1_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned13_r2_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.08855689210118 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r2_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned13_r5_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.27849788943874 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r5_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned13_r3_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.14072417909483 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r3_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned13_r4_p1024 --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.19651536351146 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned13_r4_p1024.out 2>&1
