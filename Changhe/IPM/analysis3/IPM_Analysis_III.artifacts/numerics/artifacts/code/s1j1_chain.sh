#!/bin/bash
# post-processing of the junction test S1J1 (lead note 32): assemble (v3, coverage check), 50-digit values and robustness, weakest directions
export OMP_NUM_THREADS=1; PY=python3; cd numerics/artifacts/code
echo "== assemble $(date -u +%H:%M:%SZ)"; $PY fsec_assemble.py runs/S1J1
echo "== robust $(date -u +%H:%M:%SZ)"; $PY s1_robust.py runs/S1J1
echo "== blocks $(date -u +%H:%M:%SZ)"; $PY s1_blocks.py runs/S1J1
echo "== CHAIN DONE $(date -u +%H:%M:%SZ)"
