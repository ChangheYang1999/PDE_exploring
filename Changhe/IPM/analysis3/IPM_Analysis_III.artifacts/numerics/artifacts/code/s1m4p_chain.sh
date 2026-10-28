#!/bin/bash
export OMP_NUM_THREADS=1; PY=python3; cd numerics/artifacts/code
echo "== assemble $(date -u +%H:%M:%SZ)"; $PY fsec_assemble.py runs/S1M4P
echo "== gram_compare $(date -u +%H:%M:%SZ)"; $PY gram_compare.py runs/S1M4P S1M4P
echo "== blocks $(date -u +%H:%M:%SZ)"; $PY s1_blocks.py runs/S1M4P
echo "== vectors $(date -u +%H:%M:%SZ)"; $PY s1_vectors.py runs/S1M4P runs/S1M4P/vectors.json
echo "== robust $(date -u +%H:%M:%SZ)"; $PY s1_robust.py runs/S1M4P
echo "== CHAIN DONE $(date -u +%H:%M:%SZ)"
