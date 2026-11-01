#!/bin/bash
# compact coefficient exports for the artifacts (prompt Part X item 4): best tuned runs, the certified Theorem A/D parameter run, Candidate 007 at 2048 bits, the 2/3 log state
cd .
PY=python3
mkdir -p artifacts/ckpt
for t in tuned_b1_p1024 tunedQ4_r6_p1024 tunedQ5_r6_p1024 tuned49_r5_p1024 tuned13_r6_p1024 tuned35_r4_p1024; do
  $PY code/export_coeffs.py ckpt/$t.pkl artifacts/ckpt/${t}_coeffs_n100.json --nmax 100 >> logs/exports.out 2>&1
done
$PY code/export_coeffs.py ckpt/sqrt5_sin1_p1024.pkl artifacts/ckpt/sqrt5_sin1_p1024_coeffs_n100.json --nmax 100 >> logs/exports.out 2>&1
$PY code/export_coeffs.py ckpt/c007_p2048.pkl artifacts/ckpt/c007_p2048_coeffs_n100.json --nmax 100 --nexact 0 >> logs/exports.out 2>&1
$PY code/export_coeffs.py ckpt/log_sin1_c3_N350.pkl artifacts/ckpt/log_sin1_c3_N350_coeffs_n60.json --nmax 60 --log >> logs/exports.out 2>&1
echo "$(date -u +%FT%TZ) exports done" >> logs/exports.out
du -sm artifacts/ckpt >> logs/exports.out
