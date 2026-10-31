#!/bin/bash
# 7.2/7.3 width record on the F2 m3 J_c EVAL (sensitivity.py version 6), then the branch test P1 s4 against F2 m3 with the parameter part at both sides.
# Waits for the 8.6 pair batch to end so that core 30 runs one computation at a time.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=
cd <analysis tree>
O=notes/sens_f2m3_v6
D=<optimization tree>
J=f2_S01_k0_keep_m3_L6_cl0.4597_om1.3389_free
f=$D/validation/jc_eval/$J/linearization_00481_eval_complete.npz
for i in $(seq 1 120); do grep -q ALLDONE logs/branch_86_pairs.log && break; sleep 30; done
echo "START sens $(date -u +%FT%TZ)" >> $O/status.txt
sha256sum tools/sensitivity.py tools/eta_bands.py tools/branch_field_lead.py tools/branch_param_v3.py > $O/tool.sha256
sha256sum $f > $O/inputs.sha256
taskset -c 30 nice -n 19 python3 tools/sensitivity.py $f > $O/$J.json 2> $O/$J.err
echo "sens exit $? $(date -u +%FT%TZ)" >> $O/status.txt
PY=<previous campaign>/e3-num/rotating_euler_96h/.venv/bin/python
R=$D/runs
A=$R/cont1_s4_S01_L6_cl0.4500_om1.0000_free/starts/start_000.pt
B=$R/$J/starts/start_000.pt
taskset -c 30 nice -n 19 $PY -u tools/branch_field_lead.py $A $B --tag lead_P1s4_vs_F2m3_n6_both --n-per-shell 6 \
  --sens-a notes/sens_s4p1_v6/cont1_s4_S01_L6_cl0.4500_om1.0000_free.json --jc-a $D/validation/jc_eval/cont1_s4_S01_L6_cl0.4500_om1.0000_free \
  --sens-b $O/$J.json --jc-b $D/validation/jc_eval/$J > $O/branch_both.log 2>&1
echo "branch exit $? $(date -u +%FT%TZ)" >> $O/status.txt
sha256sum $O/*.json artifacts/branch_field/lead_P1s4_vs_F2m3_n6_both.json > $O/outputs.sha256 2>/dev/null
echo DONE >> $O/status.txt
