#!/bin/bash
# usage: nb_launch.sh NAME NS NTH ITERS MU0 INIT DESC   (DESC e.g. 0,1 or none); detached N-B run on r <= 64, sigma 0.3, beta_T 1e3
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
K16=../certificates/P14_algebraic_repair/algebraic_n12_m10_k16.json
SPEC="0:9:F@$K16,1:19:F@$K16,1:19:B8+26,2:29:F@$K16,3:39:F@$K16,4:49:F@$K16,5:59:F@$K16"
NAME=$1; NS=$2; NTH=$3; ITERS=$4; MU0=$5; INIT=$6; DESC=$7; EXTRA=$8; if [ -n "$EXTRA" ]; then SPEC="$SPEC,$EXTRA"; fi
echo "launch $NAME at $(date -u +%FT%TZ): ns $NS nth $NTH iters $ITERS mu0 $MU0 init $INIT desc $DESC" >> runs/nb_launch.log
N12_RMAX=64 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 setsid nohup nice -n 5 $P code/n12_run.py $CK $FT data/$NAME $NS $NTH 0.3 "$SPEC" $ITERS 1e3 $MU0 $INIT 1.0 0.0 $DESC > runs/$NAME.log 2>&1 < /dev/null &
echo "pid $!" >> runs/nb_launch.log
