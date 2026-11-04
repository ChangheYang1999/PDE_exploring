#!/bin/bash
# phi_eval_chain.sh <run_tag> <bg_tag> <core>   e.g. phi_eval_chain.sh phi_c5_b5 C5_mid32_ang256 45
# Evaluates the frozen correction phi_runs/<run_tag>/<run_tag>_phi_exact.json with full derivatives on phi_bg/<bg_tag>.pt (norms, N2 at P-S1/P-S2, BG margins,
# F_* polar field) and runs numerics_agent_2's FFT N_q routine on the field at the P-S1 and P-S2 weights.  Outputs in phi_runs/<run_tag>/eval_<bg_tag>.json, _Fstar_<bg_tag>.npy, nqfft_<bg_tag>.json
TAG=$1; BG=$2; CORE=$3
LANE=$(cd "$(dirname "$0")/../.." && pwd); PY=python3; R=$LANE/numerics/optimization/phi_runs/$TAG
cd $LANE
OMP_NUM_THREADS=1 CUDA_VISIBLE_DEVICES=0 taskset -c $CORE nice -n 10 $PY -B numerics/optimization/phi_fit.py eval $R/${TAG}_phi_exact.json numerics/optimization/phi_bg/$BG.pt $R/eval_$BG.json $R/Fstar_$BG.npy 2>&1 | grep -v Warning
OMP_NUM_THREADS=1 taskset -c $CORE nice -n 10 $PY -B numerics/n2_code/nq_fft.py $R/Fstar_$BG.npy $R/Fstar_${BG}_s.npy $R/nqfft_$BG.json "1,0.5;1.4,1;1.2,1" 64 0.03125 10,20,40,80 2>&1 | grep -v Warning
echo CHAIN-DONE $TAG $BG
