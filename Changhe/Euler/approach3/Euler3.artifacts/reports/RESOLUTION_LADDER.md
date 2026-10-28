# Resolution ladder of the continuation experiment (generated 2026-10-28T17:12Z)

Warm starts: the two best Sigma_Z states of s1k (c_l 0.47 omega 1, holdout rho_u 0.359; c_l 0.45 omega 1, 0.405), embedded exactly into the
larger bases; Sigma_Z = 1 (ramped), far anchoring, exact tail-moment constraints (v5), Nr = 3 Nk, channels at L >= 8.
v5 arms started from v4 states are PROJECTED warm starts (reduce/expand changes the parent; see relU_change_holdout in the ledger).
Rows marked 'no movement' ended at their start value (stalled at the first iteration) and carry no L dependence.
Weighting 'nl' = 1/(RMS T4 + RMS T5)^2 per shell (gamed by core inflation, FAILURE_ANALYSIS item 12: the training cost of these
arms is not evidence); 'all5' = five scaled terms (rho_u-like). 'WORSE than start' marks arms whose holdout rho_u rose.
Families: c2x2/c2x2b/c2x2c continue the two best s1k Sigma_Z states (c_l 0.47 and 0.45, omega 1); d6t/d6tZ/d6u/d6v continue the primary-basis fit
of the verifier's released degree-6 state (c_l 0.45, omega 0.3, omega/c_l 2/3; fitted holdout rho_u 0.0740, source 0.0729). d6tZ carries the Sigma_Z = 1 ramp;
d6t/d6u/d6v carry none. 'all5far' = all5 plus the far-imbalance term lambda/den_nl on shells r >= 1 (lead 22:40Z (b)).
SPEC 7.3a: 'half' is the half-offset shell family, 'sphere' the largest single-sphere rho_u on the exchange radii; rho_nl^max is over ALL shells of the standard family.
An ordering claim between two states needs the same order on both families. max|U| start -> end is the core-inflation flag (FAILURE_ANALYSIS item 12).
One row per (family, solver, weighting, source state, arm, L): the best start of that group.

| family | solver | weighting | source c_l | arm | L | Nk | channels | start holdout rho_u | best holdout rho_u^max (std) | half | sphere | rho_nl^max (all shells) | max U start -> end | Sigma_Z (fine) | e_F | strain ratio (located max) | min W-zero eigvec defect | c_l, omega at end | status | job/start |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c2x2 | v4-2026-10-24T20:35Z | nl | 0.47 | fixed (no movement: not a ladder point) | 6 | 16 | B0/D0/E0 | n/a | 3.586e-01 | n/a | n/a | 1.318e+07 | n/a -> 1.227e+00 | 0.695 | 0.91 | 1.447 | 0.006 | 0.4700, 1.0000 | stalled | c2x2_L6_cl0.47_om+1.0_fixed/0 |
| c2x2 | v5-2026-10-24T21:05Z | nl | 0.45 | fixed (no movement: not a ladder point) | 6 | 16 | B0/D0/E0 | n/a | 4.067e-01 | n/a | n/a | 1.353e+02 | n/a -> 1.100e+00 | 0.298 | 0.66 | 0.195 | 0.018 | 0.4500, 1.0000 | stalled | c2x2_L6_cl0.45_om+1.0_fixed/0 |
| c2x2 | v5-2026-10-24T21:05Z | nl | 0.45 | fixed (WORSE than start) | 8 | 20 | B6/D6/E6 | 4.053e-01 | 4.804e-01 | 5.223e-01 | 5.837e-01 | 6.291e+01 | n/a -> 1.725e+00 | 1.000 | 0.89 | 2.265 | 0.023 | 0.4500, 1.0000 | max_iter | c2x2_L8_cl0.45_om+1.0_fixed/0 |
| c2x2 | v5-2026-10-24T21:05Z | nl | 0.45 | fixed | 10 | 24 | B6/D6/E6 | n/a | 4.093e-01 | n/a | n/a | 3.190e+03 | n/a -> 1.145e+00 | 0.293 | 0.66 | 0.174 | 0.007 | 0.4500, 1.0000 | stalled | c2x2_L10_cl0.45_om+1.0_fixed/0 |
| c2x2 | v5-2026-10-24T21:05Z | nl | 0.47 | fixed | 8 | 20 | B6/D6/E6 | 3.587e-01 | 3.571e-01 | 3.755e-01 | 4.180e-01 | 3.708e+06 | n/a -> 1.362e+00 | 1.000 | 0.90 | 2.112 | 0.044 | 0.4700, 1.0000 | max_iter | c2x2_L8_cl0.47_om+1.0_fixed/0 |
| c2x2b | v5-2026-10-24T21:05Z | nl | 0.45 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 4.053e-01 | 4.715e-01 | n/a | n/a | 1.962e+03 | n/a -> 1.558e+00 | 1.000 | 0.73 | 2.496 | 0.017 | 0.4500, 1.0000 | max_iter | c2x2b_L6_cl0.45_om+1.0_fixed/0 |
| c2x2b | v5-2026-10-24T21:05Z | nl | 0.47 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 3.587e-01 | 3.892e-01 | n/a | n/a | 2.166e+01 | n/a -> 1.303e+00 | 1.000 | 0.93 | 2.058 | 0.019 | 0.4700, 1.0000 | max_iter | c2x2b_L6_cl0.47_om+1.0_fixed/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed | 6 | 16 | B0/D0/E0 | 4.053e-01 | 3.858e-01 | 3.883e-01 | 3.903e-01 | 9.147e+02 | n/a -> 1.072e+00 | 1.000 | 0.64 | 1.597 | 0.134 | 0.4500, 1.0000 | max_iter | c2x2c_L6_cl0.45_om+1.0_fixed/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed | 8 | 20 | B0/D0/E0 | 4.053e-01 | 3.577e-01 | n/a | n/a | 1.774e+03 | n/a -> 1.024e+00 | 1.000 | 0.68 | 1.413 | 0.106 | 0.4500, 1.0000 | max_iter | c2x2c_L8_cl0.45_om+1.0_fixed/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.45 | free (WORSE than start) | 6 | 16 | B0/D0/E0 | 4.053e-01 | 4.237e-01 | 4.081e-01 | 4.282e-01 | 1.140e+03 | n/a -> 1.349e+00 | 1.000 | 0.63 | 1.379 | 0.078 | 0.4498, 0.9015 | time_limit | c2x2c_L6_cl0.45_om+1.0_free/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.47 | fixed | 6 | 16 | B0/D0/E0 | 3.587e-01 | 2.496e-01 | 2.590e-01 | 2.626e-01 | 3.409e+02 | n/a -> 1.229e+00 | 1.000 | 0.85 | 1.527 | 0.071 | 0.4700, 1.0000 | max_iter | c2x2c_L6_cl0.47_om+1.0_fixed/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.47 | fixed | 8 | 20 | B0/D0/E0 | 3.587e-01 | 3.537e-01 | 3.547e-01 | 3.550e-01 | 6.370e+02 | 1.243e+00 -> 1.262e+00 | 1.000 | 0.89 | 1.717 | 0.059 | 0.4700, 1.0000 | max_iter | c2x2c_L8_cl0.47_om+1.0_fixed/0 |
| c2x2c | v5-2026-10-24T21:05Z | all5 | 0.47 | free | 6 | 16 | B0/D0/E0 | 3.587e-01 | 2.466e-01 | 2.458e-01 | 2.791e-01 | 4.773e+02 | 1.243e+00 -> 1.279e+00 | 1.000 | 0.91 | 1.686 | 0.058 | 0.4707, 0.9965 | time_limit | c2x2c_L6_cl0.47_om+1.0_free/0 |
| c2x2split | v5-2026-10-24T21:05Z | split | 0.47 | fixed | 6 | 16 | B0/D0/E0 | 3.587e-01 | 3.436e-01 | 3.564e-01 | 4.095e-01 | 8.613e+02 | 1.243e+00 -> 1.167e+00 | 0.556 | 0.92 | 1.295 | 0.035 | 0.4700, 1.0000 | max_iter | c2x2split_L6_cl0.47_om+1.0_fixed/0 |
| d6odd | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.521e-02 | 6.019e-02 | 8.672e-02 | 1.246e-01 | 2.950e+00 | 2.729e+00 -> 2.676e+00 | 0.199 | 0.10 | 1.051 | 14.579 | 0.4500, 0.3000 | max_iter | d6odd_L6_cl0.45_om+0.3_fixed_m1e-2/0 |
| d6scan | v5-2026-10-24T21:05Z | all5 | 0.46 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.521e-02 | 6.131e-02 | 8.810e-02 | 1.237e-01 | 2.155e+00 | 2.729e+00 -> 2.693e+00 | 0.143 | 0.02 | 0.983 | 14.918 | 0.4600, 0.3000 | max_iter | d6scan_L6_cl0.46_om+0.3_fixed/0 |
| d6scan | v5-2026-10-24T21:05Z | all5 | 0.47 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.521e-02 | 5.552e-02 | 7.937e-02 | 1.109e-01 | 1.861e+00 | 2.729e+00 -> 2.729e+00 | 0.225 | 0.03 | 0.880 | 1.388 | 0.4700, 0.3000 | max_iter | d6scan_L6_cl0.47_om+0.3_fixed/0 |
| d6scan | v5-2026-10-24T21:05Z | all5 | 0.48 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.552e-02 | 6.324e-02 | 8.972e-02 | 1.187e-01 | 1.439e+00 | 2.732e+00 -> 2.653e+00 | 0.232 | 0.02 | 1.080 | 2.787 | 0.4800, 0.3000 | ftol | d6scan_L6_cl0.48_om+0.3_fixed_from47/0 |
| d6scan | v5-2026-10-24T21:05Z | all5 | 0.49 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.521e-02 | 6.055e-01 | 6.617e-01 | 7.542e-01 | 1.982e+02 | 2.729e+00 -> 3.200e+00 | -0.942 | 0.00 | 0.020 | 2.554 | 0.4900, 0.3000 | max_iter | d6scan_L6_cl0.49_om+0.3_fixed/0 |
| d6split | v5-2026-10-24T21:05Z | split | 0.45 | fixed (WORSE than start) | 6 | 16 | B4/D4/E4 | 5.521e-02 | 1.837e-01 | 1.675e-01 | 2.099e-01 | 1.613e+00 | 2.729e+00 -> 2.725e+00 | 0.098 | 0.05 | 0.698 | 1.119 | 0.4500, 0.3000 | max_iter | d6split_L6_cl0.45_om+0.3_fixed/0 |
| d6t | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed | 6 | 16 | B0/D0/E0 | 7.403e-02 | 5.521e-02 | 7.482e-02 | 1.019e-01 | 3.117e+00 | n/a -> 2.726e+00 | 0.140 | 0.05 | 1.111 | 1.162 | 0.4500, 0.3000 | max_iter | d6t_L6_cl0.45_om+0.3_fixed/0 |
| d6t | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed | 8 | 20 | B4/D4/E4 | 7.403e-02 | 4.556e-02 | 5.540e-02 | 8.824e-02 | 2.896e+00 | n/a -> 2.918e+00 | 0.227 | 0.04 | 1.115 | 1.748 | 0.4500, 0.3000 | max_iter | d6t_L8_cl0.45_om+0.3_fixed/0 |
| d6tZ | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed (WORSE than start) | 6 | 16 | B0/D0/E0 | 7.403e-02 | 1.103e-01 | 1.158e-01 | 1.507e-01 | 4.728e+00 | n/a -> 2.022e+00 | 1.000 | 0.01 | 1.168 | 1.858 | 0.4500, 0.3000 | max_iter | d6tZ_L6_cl0.45_om+0.3_fixed/0 |
| d6u | v5-2026-10-24T21:05Z | all5 | 0.45 | fixed | 8 | 20 | B4/D4/E4 | 5.521e-02 | 5.094e-02 | 7.204e-02 | 1.139e-01 | 3.733e+00 | n/a -> 2.719e+00 | 0.278 | 0.04 | 0.968 | 1.302 | 0.4500, 0.3000 | ftol | d6u_L8_cl0.45_om+0.3_fixed/0 |
| d6u | v5-2026-10-24T21:05Z | all5 | 0.45 | free (WORSE than start) | 6 | 16 | B0/D0/E0 | 5.521e-02 | 6.113e-02 | n/a | n/a | 8.593e-01 | n/a -> 2.720e+00 | 0.350 | 0.02 | 0.642 | 3.397 | 0.4990, 0.2702 | ftol | d6u_L6_cl0.45_om+0.3_free/0 |
| d6u | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed (WORSE than start) | 10 | 24 | B4/D4/E4 | 5.521e-02 | 5.532e-02 | 7.328e-02 | 1.167e-01 | 1.524e+00 | 2.729e+00 -> 2.729e+00 | 0.161 | 0.05 | 1.143 | 1.073 | 0.4500, 0.3000 | max_iter | d6u_L10_cl0.45_om+0.3_fixed/0 |
| d6v | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed | 6 | 16 | B4/D4/E4 | 5.521e-02 | 5.489e-02 | 7.512e-02 | 1.017e-01 | 8.159e-01 | 2.729e+00 -> 2.727e+00 | 0.120 | 0.05 | 1.046 | 1.238 | 0.4500, 0.3000 | max_iter | d6v_L6_cl0.45_om+0.3_fixed/0 |
| d6v | v5-2026-10-24T21:05Z | all5far | 0.45 | free | 6 | 16 | B4/D4/E4 | 5.521e-02 | 5.383e-02 | 7.349e-02 | 9.925e-02 | 7.990e-01 | 2.729e+00 -> 2.727e+00 | 0.125 | 0.05 | 1.059 | 1.301 | 0.4518, 0.3680 | max_iter | d6v_L6_cl0.45_om+0.3_free/0 |
| d6w | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed | 6 | 16 | B4/D4/E4 lB15/lD14 | 5.521e-02 | 5.227e-02 | 7.173e-02 | 9.986e-02 | 8.347e-01 | 2.729e+00 -> 2.723e+00 | 0.184 | 0.05 | 0.978 | 0.530 | 0.4500, 0.3000 | max_iter | d6w_L6_cl0.45_om+0.3_fixed_R1/0 |
| d6w | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed | 8 | 20 | B4/D4/E4 lB19/lD18 | 4.556e-02 | 4.423e-02 | 5.432e-02 | 8.661e-02 | 1.455e+00 | 2.918e+00 -> 2.918e+00 | 0.236 | 0.04 | 1.175 | 13.555 | 0.4500, 0.3000 | time_limit | d6w_L8_cl0.45_om+0.3_fixed/0 |
| d6w | v5-2026-10-24T21:05Z | all5far | 0.45 | free | 6 | 16 | B4/D4/E4 lB15/lD14 | 5.521e-02 | 5.354e-02 | 7.225e-02 | 9.841e-02 | 1.260e+00 | 2.729e+00 -> 2.727e+00 | 0.139 | 0.05 | 1.124 | 14.373 | 0.4500, 0.3014 | time_limit | d6w_L6_cl0.45_om+0.3_free/0 |
| d6w2 | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed (WORSE than start) | 6 | 16 | B4/D4/E4 lB15/lD14 | 5.284e-02 | 5.378e-02 | 6.969e-02 | 9.233e-02 | 9.279e-01 | 2.724e+00 -> 2.687e+00 | 0.230 | 0.03 | 0.944 | 15.370 | 0.4500, 0.3000 | max_iter | d6w2_L6_cl0.45_om+0.3_fixed/0 |
| d6w3 | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed | 6 | 16 | B4/D4/E4 lB15/lD14 | 5.284e-02 | 5.228e-02 | 7.037e-02 | 9.625e-02 | 2.818e-01 | 2.724e+00 -> 2.716e+00 | 0.191 | 0.06 | 1.057 | 14.400 | 0.4500, 0.3000 | max_iter | d6w3_L6_cl0.45_om+0.3_fixed_cl1e-2/0 |
| d6w3 | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed (WORSE than start) | 8 | 20 | B4/D4/E4 lB19/lD18 | 4.423e-02 | 5.682e-02 | 5.867e-02 | 9.220e-02 | 1.002e+00 | 2.918e+00 -> 2.924e+00 | 0.289 | 0.04 | 1.059 | 12.513 | 0.4500, 0.3000 | max_iter | d6w3_L8_cl0.45_om+0.3_fixed/0 |
| d6w4 | v5-2026-10-24T21:05Z | all5far | 0.45 | fixed (WORSE than start) | 6 | 16 | B4/D4/E4 lB15/lD14 | 5.269e-02 | 5.326e-02 | 6.973e-02 | 9.375e-02 | 1.753e-01 | 2.707e+00 -> 2.686e+00 | 0.238 | 0.03 | 0.961 | 15.056 | 0.4500, 0.3000 | time_limit | d6w4_L6_cl0.45_om+0.3_fixed/0 |

Interpretation rule (lead 19:27Z): a floor that does not move with L means the representation is not the limit; one that falls means refinement.

## Nest ladder (route's own random starts promoted L2 -> L4 -> L6 -> L8; best holdout rho_u^max per level, standard / half-offset family; q = ratio of the standard values of successive levels; SPEC-degree channels and closure rows from L6 on)

| c_l | omega | omega/c_l | L | Nk | channels | best holdout rho_u^max std / half | q vs previous level (std) | sigma_u^max | sigma_Om | a_max | rho_nl^max | sampled Q_sw | E_ren | H_tot/int abs(h) | K_E ratio | carried mismatch | V10 | iterations | seconds | job/start |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.42 | 0.3 | 0.7143 | 2 | 8 | none | 0.1050 / 0.1087 | n/a | 1.684 | 1.470 | 2.790 | 2.37 | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 77 | nest2_L2_cl0.42_om+0.3/12 |
| 0.42 | 0.3 | 0.7143 | 4 | 12 | none | 0.0740 / 0.0748 | 0.705 | 0.635 | 0.551 | 2.735 | 6.11 | 2.630 | -4.529 | -0.878 | n/a | n/a | -3.6e-01 | 300 | 194 | nest4_L4_cl0.42_om+0.3_fixed_p0_om+0.3s12/0 |
| 0.42 | 0.3 | 0.7143 | 6 | 16 | B15/D14/E6 x Nk4 | 0.0641 / 0.0715 | 0.867 | 0.660 | 0.466 | 0.924 | 1.18 | 0.723 | -3.895 | -0.789 | 5.38 | 0.349 | 6.6e-02 | 600 | 6952 | nest6_L6_cl0.42_om+0.3_fixed_p0_om+0.3s12s0/0 |
| 0.42 | 0.3 | 0.7143 | 8 | 20 | B19/D18/E8 x Nk4 | 0.0615 / 0.0672 | 0.960 | 0.689 | 0.472 | 1.093 | 1.21 | 0.493 | -3.932 | -0.793 | 3.86 | 0.200 | 4.3e-03 | 150 | 6807 | nest8_L8_cl0.42_om+0.3_fixed_p0_cont150/0 |
| 0.45 | 0.3 | 0.6667 | 2 | 8 | none | 0.1075 / 0.1071 | n/a | 0.788 | 0.630 | 0.797 | 2.03 | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 66 | nest2_L2_cl0.45_om+0.3/34 |
| 0.45 | 0.3 | 0.6667 | 4 | 12 | none | 0.0857 / 0.0804 | 0.797 | 0.575 | 0.516 | 1.122 | 2.91 | n/a | n/a | n/a | n/a | n/a | 7.6e-03 | 300 | 191 | nest4_L4_cl0.45_om+0.3_fixed_p0_om+0.3s34/0 |
| 0.45 | 0.3 | 0.6667 | 6 | 16 | B15/D14/E6 x Nk4 | 0.0644 / 0.0657 | 0.752 | 0.645 | 0.417 | 1.218 | 2.85 | 0.385 | -2.068 | 0.891 | n/a | 0.980 | 4.0e-02 | 600 | 7029 | nest6_L6_cl0.45_om+0.3_fixed_p1_om+0.3s16s0/0 |
| 0.45 | 0.3 | 0.6667 | 8 | 20 | B19/D18/E8 x Nk4 | 0.0374 / 0.0394 | 0.580 | 0.601 | 0.454 | 1.435 | 0.28 | 0.244 | -1.036 | -0.888 | 1.00 | 0.000 | 7.0e-02 | 123 | 5122 | nest8_L8_cl0.45_om+0.3_fixed_cl1/0 |
| 0.45 | 0.3 | 0.6667 | 10 | 24 | B23/D22/E10 x Nk4 | 0.0565 / 0.0565 | 1.511 | 0.598 | 0.422 | 1.120 | 2.67 | 0.320 | -1.719 | -0.876 | -0.01 | 0.041 | 8.4e-03 | 300 | 70125 | nest10_L10_cl0.45_om+0.3_fixed_p0/0 |
| 0.45 | 1.0 | 2.2222 | 2 | 8 | none | 0.1111 / 0.1188 | n/a | 0.841 | 0.591 | 0.778 | 1.41 | 1.348 | -1.243 | -0.286 | n/a | n/a | n/a | 200 | 82 | nest2_L2_cl0.45_om+1.0/43 |
| 0.45 | 1.0 | 2.2222 | 4 | 12 | none | 0.0578 / 0.0584 | 0.520 | 0.639 | 0.500 | 1.333 | 3.72 | 2.016 | n/a | n/a | n/a | n/a | 9.7e-03 | 288 | 195 | nest4_L4_cl0.45_om+1.0_fixed_p1_om+1.0s43/0 |
| 0.45 | 1.0 | 2.2222 | 6 | 16 | B15/D14/E6 x Nk4 | 0.0460 / 0.0463 | 0.796 | 0.446 | 0.406 | 0.558 | 1.04 | 0.673 | -1.543 | -0.711 | n/a | 0.346 | 6.1e-02 | 600 | 6915 | nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/0 |
| 0.45 | 1.0 | 2.2222 | 8 | 20 | B19/D18/E8 x Nk4 | 0.0298 / 0.0313 | 0.648 | 0.505 | 0.397 | 1.206 | 0.33 | 0.407 | -1.071 | -0.599 | 1.00 | 0.000 | n/a | 1 | 54 | nest8_L8_cl0.45_om+1.0_fixed_cl1_sgcont150b/0 |
| 0.45 | 1.0 | 2.2222 | 10 | 24 | B23/D22/E10 x Nk4 | 0.0420 / 0.0415 | 1.407 | 0.424 | 0.421 | 0.596 | 1.13 | 0.682 | -1.570 | -0.699 | -4.25 | 0.056 | 5.2e-03 | 300 | 70654 | nest10_L10_cl0.45_om+1.0_fixed_p0/0 |

R1 (lead): a branch goes to the next level only if core-resolved and holdout rho_u^max <= 0.1; R2: two successive steps with q > 0.85 floor the branch; a q at the iteration limit (V10 > 1e-3) mixes truncation and budget and is read with its V10 (lead 12:32Z).

## R2 status by branch (lead readings of record; dated)
- nest (0.42, 0.3), omega/c_l 5/7: FLOORED at L8 under R2 (lead d128 AW 2026-10-26T00:23:50Z): L4 -> L6 q about 0.87 / 0.96, L6 -> L8 q 0.970 / 0.942 (std / half), two successive steps above 0.85; the 150-iteration continuation changed the L8 holdout by 1.0 / 0.4 per cent (0.06154 / 0.06718, independently read). Resources unchanged; the queued s12 (0.42, 0.3) arm is read against its own start.
- nest (0.45, 1), omega/c_l 20/9: one weak step (L6 -> L8 q 0.955 / 0.940 as recorded; recomputed 0.887 on the standard family after the channel-Nk 8 test, which is NOT ordered ahead of cont150; lead 23:09:17Z); the L10 rung decides (q_10 against cont150 0.04367 / 0.04331; a floor reads 'floored at correction-channel Nk 4').
- nest (0.45, 0.3), omega/c_l 2/3: one weak step (L6 -> L8 q 0.916, cont150 -2.6 per cent); the L10 rung decides (q_10 against cont150 0.0597 / 0.0594).
- D6 lineage (0.45, 0.3): floored at L8 (d6w3_L8 worse than d6w_L8; FAILURE_ANALYSIS 25) and within 4 per cent under Nk 16 -> 32 at L6 (FAILURE_ANALYSIS 33).
