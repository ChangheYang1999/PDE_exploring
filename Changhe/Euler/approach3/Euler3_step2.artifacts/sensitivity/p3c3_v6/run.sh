#!/bin/bash
# 7.2/7.3 width record on the P3 segment-3 (cont3free) J_c EVAL at 110 iterations (sensitivity.py version 6).
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 CUDA_VISIBLE_DEVICES=
cd <analysis tree>
O=notes/sens_p3c3_v6
J=cont3free_S20_L6_cl0.4500_om1.0000_free
f=<optimization tree>/validation/jc_eval/$J/linearization_00110_eval_complete.npz
sha256sum tools/sensitivity.py > $O/tool.sha256; sha256sum $f > $O/inputs.sha256
echo "START $(date -u +%FT%TZ)" >> $O/status.txt
taskset -c 30 nice -n 19 python3 tools/sensitivity.py $f > $O/$J.json 2> $O/$J.err
echo "$J exit $? $(date -u +%FT%TZ)" >> $O/status.txt
sha256sum $O/*.json > $O/outputs.sha256; echo DONE >> $O/status.txt
