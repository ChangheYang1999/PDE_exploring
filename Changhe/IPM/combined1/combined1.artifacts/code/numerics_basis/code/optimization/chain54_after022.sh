#!/bin/bash
# core 54 after the 022 snapshot: (1) weak_tests3 sweep over odd modes 33..47 for 022 (IPM_NMAX=47; held-out probes, never rows; separate output file), (2) chain024 (MID 32 rule control of 016).
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
T=legqs25_m16to23_gpu_m16
IPM_NMAX=47 taskset -c 54 nice -n 19 $PY -B weak_tests3.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests3c_n47.json 32 > logs/weaktests3c_n47_$T.out 2>&1
echo N47_DONE >> logs/weaktests3c_n47_$T.out
./chain024_coreXX_gpu.sh 54
