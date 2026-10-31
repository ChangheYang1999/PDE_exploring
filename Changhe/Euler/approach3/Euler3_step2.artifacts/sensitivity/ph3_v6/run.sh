#!/bin/bash
# 7.2/7.3 records (sensitivity.py version 6) on the J_c EVALs of the Phase III ends F1 m3, P3 cont4 and the
# perturbation repeat; the same tool and options as the earlier sens_*_v6 records.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=
cd <analysis tree>
O=notes/sens_ph3_v6
D=<optimization tree>
sha256sum tools/sensitivity.py tools/eta_bands.py > $O/tool.sha256
: > $O/inputs.sha256
for spec in jceval_v5_f1_S05_m3_044546:f1_S05_m3_L6_cl0.4500_om0.3000_free:00520 \
            jceval_v5_cont4free_S20_084339:cont4free_S20_L6_cl0.4500_om1.0000_free:00146 \
            jceval_v5_f3_P1s4_pert_s7_090548:f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free:00041; do
  IFS=: read R J K <<< "$spec"
  JC=$D/validation/jc_eval/$J
  [ -f $JC/linearization_${K}_eval_complete.npz ] || JC=$D/runs_l/$R/validation/jc_eval/$J
  f=$JC/linearization_${K}_eval_complete.npz
  echo "START $J $(date -u +%FT%TZ) $f" >> $O/status.txt
  sha256sum $f $JC/jc_eval.json >> $O/inputs.sha256
  taskset -c 30 nice -n 19 python3 tools/sensitivity.py $f > $O/$J.json 2> $O/$J.err
  echo "exit $? $(date -u +%FT%TZ)" >> $O/status.txt
done
sha256sum $O/*.json > $O/outputs.sha256
echo DONE >> $O/status.txt
