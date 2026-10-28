#!/bin/bash
set -eu
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
py=python3
src=05_team_audit/stieltjes_v7/preliminary/cert_v7.py
out=05_team_audit/stieltjes_v7/a30/replay
mkdir -p "$out"
date -u '+START %Y-%m-%dT%H:%M:%SZ'
timeout 540 "$py" -B -u "$src" --alpha 3/10 --b 3/8 --shift=-1/20 --K 1007/1000 --sign 1 --left=-18 --right=12 --nx 16384 --ny 512 --vleft=-6 --vright=3 --start 8192 --stop 10240 --out "$out/a30v7_s1_p2_r8192_10240.json"
timeout 540 "$py" -B -u "$src" --alpha 3/10 --b 3/8 --shift=-1/20 --K 1007/1000 --sign 1 --left=-18 --right=12 --nx 16384 --ny 512 --vleft=-6 --vright=3 --start 10240 --stop 12288 --out "$out/a30v7_s1_p2_r10240_12288.json"
timeout 540 "$py" -B -u "$src" --alpha 3/10 --b 3/8 --shift=-1/20 --K 1007/1000 --sign -1 --left=-18 --nx 16384 --ny 512 --vleft=-6 --vright=3 --start 14336 --stop 16384 --out "$out/a30v7_s-1_p3_r14336_16384.json"
date -u '+COMPLETE %Y-%m-%dT%H:%M:%SZ'
