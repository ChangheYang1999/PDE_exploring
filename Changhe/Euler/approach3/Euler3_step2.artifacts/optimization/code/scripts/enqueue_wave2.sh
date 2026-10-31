#!/bin/bash
# Wave 2 (full release): F1 lineage starts at their own parameters (medium budgets) and the three FIXED-CONTROL partners (SPEC 8.4).
cd "$(dirname "$0")/.."; PY=python3
for S in S05_nest6_cl0.45_om0.3_p0 S03_s11_cl0.45_om1.0_closure1 S07_s11_cl0.45_om0.3_closure1 S11_nest6_cl0.42_om0.3_p0 S10_d6t_cl0.45_om0.3 S02_nest6_cl0.45_om1.0_p1 S06_nest6_cl0.45_om0.3_p1 S12_s12_cl0.42_om0.3_rl3; do
  $PY scripts/enqueue_d6.py --start starts/$S.pt --label FREE --tag w2_${S%%_*} --max_iter 300 --time_limit 10800 --priority 15 --note "wave 2 F1 own parameters"
done
for S in S20_s4allm_cl0.45_om1.0 S13_s4om_cl0.45_om0.5 S14_s4om_cl0.45_om0.2 S15_s4om_cl0.45_om0.1 S16_d6scan_cl0.47_om0.3 S17_d6scan_cl0.46_om0.3 S18_s5r0_cl0.45_om1.0_R0p15 S19_s7c_cl0.45_om1.0_m1; do
  $PY scripts/enqueue_d6.py --start starts/$S.pt --label FREE --tag w2_${S%%_*} --max_iter 300 --time_limit 10800 --priority 13 --note "wave 2 F1/F5 own parameters"
done
# FIXED-CONTROL partners mirror their FREE partner's first segment (SPEC 8.4): c_S01, c_S09 mirror the wave-1 pilots (120 iterations, 3600 s); c_S20 mirrors w2_S20 (300, 10800 s)
for S in S01_nest6_cl0.45_om1.0_p0 S09_d6w_cl0.45_om0.3_R1; do
  $PY scripts/enqueue_d6.py --start starts/$S.pt --label FIXED-CONTROL --fixed --tag c_${S%%_*} --max_iter 120 --time_limit 3600 --priority 11 --note "FIXED-CONTROL partner of the wave-1 pilot (SPEC 8.4, segment 1: 120 iterations, 3600 s)"
done
$PY scripts/enqueue_d6.py --start starts/S20_s4allm_cl0.45_om1.0.pt --label FIXED-CONTROL --fixed --tag c_S20 --max_iter 300 --time_limit 10800 --priority 11 --note "FIXED-CONTROL partner of w2_S20 (SPEC 8.4: 300 iterations, 10800 s)"
