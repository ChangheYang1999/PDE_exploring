#!/bin/bash
# 7.2/7.3 on the segment-4 and medium-end J_c EVAL records (sensitivity.py version 6, V398 minimizer-centred log widths added; see tool.sha256)
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
cd <analysis tree>
O=notes/sens_s4p1_v6
sha256sum tools/sensitivity.py tools/eta_bands.py > $O/tool.sha256
FILES=""
for spec in "$@"; do
  d=${spec%%:*}; it=${spec##*:}
  f=<optimization tree>/validation/jc_eval/$d/linearization_${it}_eval_complete.npz
  sha256sum $f >> $O/inputs.sha256
  taskset -c 30 nice -n 10 python3 tools/sensitivity.py $f > $O/$d.json 2> $O/$d.err
  echo "$d exit $? $(date -u +%H:%M:%SZ)" >> $O/status.txt
  FILES="$FILES $f"
done
taskset -c 30 nice -n 10 python3 tools/eta_bands.py $FILES > $O/eta_bands.json 2> $O/eta_bands.err
echo "eta_bands exit $? $(date -u +%H:%M:%SZ)" >> $O/status.txt
sha256sum $O/*.json >> $O/outputs.sha256
echo DONE >> $O/status.txt
