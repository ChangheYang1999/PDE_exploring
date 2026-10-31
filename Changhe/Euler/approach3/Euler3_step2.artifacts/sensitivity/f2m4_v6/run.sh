#!/bin/bash
# 7.2/7.3 width record on the F2 m4 J_c EVAL (sensitivity.py version 6), then the branch test P1 s4 against F2 m4 with the parameter part at both sides.
# Waits for the P1 s4 / F2 m4 twist (logs/branch_p1s4_f2m4.log ALLDONE) so that core 30 runs one computation at a time.
# Uses the copied-back J_c EVAL in validation/jc_eval if present, otherwise the frozen-copy run directory of the EVAL job.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=
cd <analysis tree>
O=notes/sens_f2m4_v6
D=<optimization tree>
J=f2_S01_k0_keep_m4_L6_cl0.4597_om1.3389_free
for i in $(seq 1 240); do grep -q ALLDONE logs/branch_p1s4_f2m4.log && break; sleep 30; done
JC=$D/validation/jc_eval/$J
[ -f $JC/linearization_00557_eval_complete.npz ] || JC=$D/runs_l/jceval_v5_f2_S01_k0_keep_m4_084913/validation/jc_eval/$J
f=$JC/linearization_00557_eval_complete.npz
echo "START sens $(date -u +%FT%TZ) jc=$JC" >> $O/status.txt
sha256sum tools/sensitivity.py tools/eta_bands.py tools/branch_field_lead.py tools/branch_param_v3.py > $O/tool.sha256
sha256sum $JC/* > $O/inputs.sha256
taskset -c 30 nice -n 19 python3 tools/sensitivity.py $f > $O/$J.json 2> $O/$J.err
echo "sens exit $? $(date -u +%FT%TZ)" >> $O/status.txt
PY=<previous campaign>/e3-num/rotating_euler_96h/.venv/bin/python
R=$D/runs
A=$R/cont1_s4_S01_L6_cl0.4500_om1.0000_free/starts/start_000.pt
B=$R/$J/starts/start_000.pt
sha256sum $A $B >> $O/inputs.sha256
taskset -c 30 nice -n 19 $PY -u tools/branch_field_lead.py $A $B --tag lead_P1s4_vs_F2m4_n6_both --n-per-shell 6 \
  --sens-a notes/sens_s4p1_v6/cont1_s4_S01_L6_cl0.4500_om1.0000_free.json --jc-a $D/validation/jc_eval/cont1_s4_S01_L6_cl0.4500_om1.0000_free \
  --sens-b $O/$J.json --jc-b $JC > $O/branch_both.log 2>&1
echo "branch exit $? $(date -u +%FT%TZ)" >> $O/status.txt
sha256sum $O/*.json artifacts/branch_field/lead_P1s4_vs_F2m4_n6_both.json > $O/outputs.sha256 2>/dev/null
echo DONE >> $O/status.txt
