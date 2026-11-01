#!/bin/bash
# lead's optional request 14:46Z: tuned series at delta = 3/5 (c = 5/2, h = 3, Q = 10), four real roots of P_10 (notes/tuned35_poly.json)
cd .
PY=python3
$PY -u code/tuned_general.py --tag tuned35_r4_p1024 --a 3 --b 5 --poly-coeffs @notes/tuned35_poly.json --root-guess 0.59420442548047 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned35_r4_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned35_r1_p1024 --a 3 --b 5 --poly-coeffs @notes/tuned35_poly.json --root-guess 0.06594721793948 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned35_r1_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned35_r3_p1024 --a 3 --b 5 --poly-coeffs @notes/tuned35_poly.json --root-guess 0.35056375993446 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned35_r3_p1024.out 2>&1
$PY -u code/tuned_general.py --tag tuned35_r2_p1024 --a 3 --b 5 --poly-coeffs @notes/tuned35_poly.json --root-guess 0.10934080096271 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned35_r2_p1024.out 2>&1
