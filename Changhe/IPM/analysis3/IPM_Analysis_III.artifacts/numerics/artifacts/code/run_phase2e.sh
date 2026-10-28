#!/bin/bash
# chain v5 (shift 2, 04:50Z; 4 cores): margin.py and hypA.py in two cell-range parts each (4 single-process jobs), merge, then the L_fix
# section (4 workers), certify_l2, S0 Phase 2 (run_norms, run_tailbound2, offbasis), identity rerun.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
PY=python3
L=numerics/logs
TAG=S0_M4_s60_o12; NW=4
cd numerics/artifacts/code
date -u; echo "== margin parts A (0:785) B (785:1569) and hypA parts A, B (logs $L/margin_A.log ...)"
$PY -u margin.py MARGIN_A 64 160 0:785 > $L/margin_A.log 2>&1 &
P1=$!
$PY -u margin.py MARGIN_B 64 160 785:1569 > $L/margin_B.log 2>&1 &
P2=$!
$PY -u hypA.py HYPA_A 64 160 0:785 > $L/hypA_A.log 2>&1 &
P3=$!
$PY -u hypA.py HYPA_B 64 160 785:1569 > $L/hypA_B.log 2>&1 &
P4=$!
wait $P3; echo "hypA_A exit $?"; date -u
wait $P4; echo "hypA_B exit $?"; date -u
$PY -u merge_hypA.py HYPA HYPA_A HYPA_B > $L/hypA_merge.log 2>&1; echo "hypA merge exit $?"
wait $P1; echo "margin_A exit $?"; date -u
wait $P2; echo "margin_B exit $?"; date -u
$PY -u merge_margin.py MARGIN MARGIN_A MARGIN_B > $L/margin_merge.log 2>&1; echo "margin merge exit $?"; date -u
echo "== L_fix section in the lead's L2(e^mu~) norm (section_l2): assembly, $NW workers"
$PY -u run_section_l2.py L2fix_M4_s60_o12 exact 4 60 12 30 $NW 256
date -u; echo "== certify_l2"
$PY -u certify_l2.py runs/L2fix_M4_s60_o12
date -u; echo "== run_norms $TAG"
$PY -u run_norms.py $TAG exact 4 60 12 30 $NW 256
date -u; echo "== run_tailbound2 $TAG"
$PY -u run_tailbound2.py $TAG exact 4 60 12 30 $NW 256
date -u; echo "== offbasis $TAG"
$PY -u offbasis.py runs/$TAG
date -u; echo DONE
date -u; echo "== identity rerun (fixture, 1 process)"
$PY -u test_identity.py > $L/test_identity4.log 2>&1
date -u; echo ALLDONE
