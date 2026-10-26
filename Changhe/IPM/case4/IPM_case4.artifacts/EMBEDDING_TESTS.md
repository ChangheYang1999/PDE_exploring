# EMBEDDING_TESTS.md (numerics lane) — test plan, version 3 (04:10Z; aligned with SPEC v5 and the lead's 04:00Z release note)

Scope: the G2 embedding gate of SPEC v5 section 9 and the G3 chart/Jacobian gate of section 10, for the 860 family in
the T1 internal coordinates described in BASIS_860_IMPLEMENTATION.md. Tolerances are copied here before any run; a
result table is appended after each gate run, together with the frozen-code manifest hash that produced it. No numbers
below are results yet; the pre-G1 draft runs (03:22 to 03:37Z) are not admissible and are not reported as results.

Procedure for every gate run: (1) `bin/freeze_manifest.sh <tag>` records sha256 of every file under `work/research860`,
`bin/`, `outputs/dev_policy.json`, the frozen 181D closure (state.json source hashes recomputed) and
`outputs/manifests/environment.json` into `outputs/manifests/code_manifest_<tag>.json`; (2) the gate script is run under
the guard and writes its JSON next to the manifest with the manifest hash inside; (3) any code edit after (1) requires a
new tag and a rerun of the affected gate.

High-precision references: all identity and spot checks use the frozen binary64 N_n (the T1 manifest hex values, as exact
rationals) on BOTH sides, in my own Decimal evaluator (`research860/hp860.py`, to be written after release): Cartesian
point-centered Taylor jets of the potential built from H_m, R^{p}, t^h and the shifted-Legendre recurrence with the frozen
N_n. The handoff's `highprecision_origin.radial_series` and `basis_tests.potential_jet` use the ideal Decimal sqrt(2n+1) and
are therefore NOT used as references for the 1e-40 identities (SPEC v5 section 9); they may appear only as labeled
cross-checks with the expected 3e-15-level normalization difference. mpmath (available in the system interpreter only) may be
used for an additional independent run; it is not in the pinned environment.

## T0. Static identities (Decimal 85 and 110 digits)
| Test | Inputs | Pass criterion |
|---|---|---|
| T0.1 manifest | canonical triples, I(j,m,k) | 860 unique triples, I bijective onto 0..859, 215 per j, 26-m per (j,m) |
| T0.2 T1 matrix | T (860x860, frozen N_n as exact binary values) | block triangular, nonzero diagonal, T^{-1}T - I max entry <= 1e-40 at 60 digits and at 110 digits |
| T0.2b frozen N_n | the 26 constants used by the production evaluator (frozen `spectral_basis._radial` expression on this host) | bit for bit equal to the T1 manifest hex values (lead `source_Nn_pinned.json`); N_0 = 1 exactly; deviations from sqrt(2n+1) recorded (expected up to 25 ulps) |
| T0.3 generator identities | each T1 internal function vs its monomial expansion at 12 points (both axes, r = 0.005, 0.02, 0.3, 1, 7, e^16), c_l in {1.8089923602744993, 1.5, 2.5, 4.0} | |difference| <= 1e-40 max(|value|, 1e-30) at 85 and 110 digits (precision independence) |
| T0.4 old generators | each of the 186 old functions (exact source form, including the frozen N_n) vs its B-map combination | same criterion; the (3,2) three-term relation included |
| T0.5 strains and jets | low-block strains vs SPEC section 7 list; jets of the 60 low generators vs the frozen taylor_jet.series on the 23 identity-mapped old core functions | exact rational agreement for strains; jets <= 1e-12 absolute in float, <= 1e-60 in Decimal |

## T1. Seed construction (SPEC sections 8, 9)
| Test | Pass criterion |
|---|---|
| T1.1 a_000 identity | with the old c0 taken from the TOP-LEVEL 90-digit `coefficients_decimal` of the accepted278 JSON (not the 70-digit copy in core_HP_analytic_center): the eliminated a_000 (section 7 strains, >= 90 digits) equals b_00 + b_01 + b_02 to <= 1e-80 (lead reference: -8.3e-89, center defect 4.6e-88); equals -3.611632420753814241569187726598932770153 to >= 40 digits |
| T1.1b coefficient-by-coefficient | all 860 saved raw a (50-digit strings) vs the lead's independent mpmath map B `c4-lead/checks/embed_seed_coefficients.json` (sha256 6b118ca0...f081): agreement to >= 40 significant digits for every nonzero coefficient (absolute 1e-40 for zeros); the 800 T1 coordinates vs the old 162 Global values (bitwise) and zeros elsewhere except c_{3,0,0} = b_{3,2} |
| T1.2 low-block coefficients | max |a| over the 60 low coefficients = 20.1129691482296 at (0,0,3) (lead reference, >= 15 digits) |
| T1.3 T1 high coordinates | equal the old 162 Global coordinates one to one (bitwise) and c_{3,0,0} = b_{3,2} |
| T1.4 center and C5 from the raw a | center defect 0 by construction; five raw defects each <= 1e-12 (expected 4.888e-14 level), equal to the JSON constraints_decimal to <= 1e-60 |
| T1.5 Poisson jet identities | b + 3(u+v), 2d + 10w + 3z, e + 10k + 3z each <= 1e-60 in Decimal |
| T1.6 a_0, W_x, W_y | a_0 = 14.767729990606481 (rel <= 1e-13); W_x = 2.7795669555872, W_y = 2.20529251441704 (>= 12 digits) |
| T1.7 tail moments | C_{mj0} = sum_k a_{mkj} from the raw a in 50-digit arithmetic, recorded in the manifest; a_{8,25,0} = 1304.34597872917 and the k = 26 leakage coefficient -2 (p_0 - 25) a_{8,25,0} = 60583.2264578523 (lead reference, >= 12 digits) |

## T2. Fields and derivatives against the 181D evaluator (SPEC section 9, band-scaled)
Random old coefficient vectors (24 core, analytic c0, plus 162 Global) at c_l in {accepted278, 1.5, 2.5, 4.0}, mapped by B
to the 860 representation; sample points in the seven radial bands of SPEC v5 (r < 0.02 via the origin series, [0.02,0.1),
[0.1,1), [1,10), [10,1e3), [1e3,e^16], beyond e^16), both axes and random angles.
| Test | Pass criterion |
|---|---|
| T2.1 fields f, f_x, f_y, psi_x, psi_y, psi_x/y | max |difference| <= 1e-11 x band scale (band max of |quantity| from the 181D code; absolute 1e-30 if the band max < 1e-30) |
| T2.2 d/dc_l of each field at fixed raw old coefficients | same criterion |
| T2.3 composed physical derivative at fixed independent parameters (c0 chain) | same criterion, separately reported |
| T2.4 origin series overlap | at r = 0.02, angle 7 pi/32: order-20 and order-24 series vs 85-digit Cartesian value (frozen N_n), |error| <= 1e-18 + 1e-7 |R_f| |
| T2.5 infinity block, direct | on the training nodes with r > e^16 (the infinity block r = e^16/u): 860 vs 181D residual entries and all 186 chain-rule Jacobian columns, banded rule of T2.1 with the band max of the 181D code |
| T2.6 infinity block, high precision | 50-digit spot values of f, f_x, f_y, psi_x, psi_y, psi_x/y, R_f and representative Jacobian columns (c_l, one low, one high per j) at r = e^24, e^32, e^44 on angles 0, 1e-6, 0.3, pi/4, pi/2 - 1e-6, pi/2, compared with the float64 production values by the banded rule; the low-block raw monomials are expected to lose relative accuracy there while staying inside the absolute envelope (SPEC section 5), and this is measured and reported |

## T3. Embedded seed on the production meshes
| Test | Pass criterion |
|---|---|
| T3.1 residual vector, training mesh (90,624 nodes) | ||r_860 - r_181||_2 <= 1e-9 ||r_181||_2 and max |Delta R_f| / a_ref <= 1e-12 (r_181 = fresh Linux V3 production vector) |
| T3.2 residual vector, refined mesh (241,664 nodes) | same |
| T3.3 J_mesh | reported with the difference; implied by T3.1 |
| T3.4 same-host determinism | two fresh processes give bitwise equal r_860; 1, 4, 8 BLAS threads bitwise equal |
| T3.5 independent whole-axis J_abs | |J_860 - J_181| <= 1e-9 J_181 + (e_860 + e_181); conclusive only if e_860 + e_181 <= 1e-9 J_181 = 4.268e-18, which requires integral targets tighter than the production 2.5e-15 (planned target 1e-18 for both sides, as in the assessment's tight integral whose error diagnostic was 2.07e-21); the setting is recorded with the result |
| T3.6 refined sampled maxima E_f, E_rho | within 1e-10 relative of the 181D values on the same sample points (32 frozen regions and the refinement grids) |
| T3.7 exact dilation | J of the exactly dilated fields at L = 1 +- 1e-3 and L = 2 on the frozen mesh vs L = 1, reported with the quadrature error |
| T3.8 widths and drift baseline | W_x = sqrt(-a_0/b), W_y = sqrt(-a_0/c) from the Decimal jets (reference 2.7795669555872, 2.20529251441704), l = (1/2) log(W_x W_y) and eta = log(W_x/W_y) recorded as the baseline for the SPEC section 6 drift warning |

## T4. Jacobian chain rule and chart (SPEC sections 9, 10)
| Test | Pass criterion |
|---|---|
| T4.1 chain rule | J_860 @ E (E = embedding derivative, 860x186, with the c_l column and the (3,2) relation) vs J_181 column by column: <= 1e-9 x column 2-norm plus absolute floor 1e-13 x max column norm; floor-only passes listed |
| T4.2 constraint Jacobian | 6x861 (center + C5 with c_l) rank 6 and 5x59 block rank 5, singular values and gaps recorded |
| T4.3 tangent | tangent rank 55, complete rank 60, G T <= 1e-8, old 19 tangent directions inside the new 55 to <= 1e-9 |
| T4.4 lifts | random 55-vectors of norm 1e-3: C5 max defect <= 1e-10 after lift, c_l bit pattern preserved, lift tangent vs central FD <= 1e-6 |
| T4.5 analytic vs FD residual Jacobian | central differences at relative steps 1e-4, 1e-5, 1e-6 along: c_l through the chart, 5 low tangent directions, 8 high directions (small and large k, every j), the 3 weakest right singular vectors, the projected dilation D; report convergence ratios and best agreement; PASS/FAIL at the baseline thresholds: raw directions relative error <= 3e-5, feasible (chart-lifted) directions <= 1e-3 at the best step; 1e-6 is a target to report, not a criterion |
| T4.6 dilation tangency and leakage | G D at the seed vs w = (0, 0, -2E_x, -2E_y, -4D_1, -4D_2, -4D_3), PASS if |(G D)_i - w_i| <= 1e-10 rowscale_i ||D|| for every row (rowscale_i = norm of the coefficient part of row i of G); the k = 26 leakage term measured as a residual-vector and field change; D compared with the exact-dilation column -X.grad R_f and with the right singular vectors in the column-scaled metric; ||A_s D_s||/||D_s|| reported against the smallest and median singular values |
| T4.7 zero step | zero trial reproduces the incumbent residual bitwise or within 64 eps |
| T4.8 spectrum | all 855 singular values of the column-scaled Jacobian recorded; diagnostic rank; condition number; comparison with the 181 spectrum (no truncation) |

## T5. Seed persistence and replay
| Test | Pass criterion |
|---|---|
| T5.1 seed files | seed_860.json/npz written once, sha256 recorded, read-only |
| T5.2 strict replay | a fresh process reloads the seed and reproduces its residual under norm(r_fresh - r_saved) <= 64 eps max(norms) |

## Changes from version 1 (03:52Z) to version 2 (04:02Z)
Frozen-N_n-only high-precision references (own evaluator, handoff helpers excluded as references); T0.2b, T1.1 (top-level
90-digit c0, lead reference -8.3e-89), T1.1b coefficient-by-coefficient check of the saved embedding against an independent
map B; T1.7 leakage reference; bands corrected to [1e3, e^16] then beyond; T2.5/T2.6 infinity-block residual, Jacobian and
50-digit spots at e^24, e^32, e^44; T3.5 cap 4.268e-18 with tightened targets; T3.8 width baseline; T4.6 leakage metric.

## Changes from version 2 to version 3 (04:10Z, lead release note)
T1.1b compares against the lead's embed_seed_coefficients.json to >= 40 digits; T4.5 pass/fail at the baseline thresholds (raw 3e-5,
feasible 1e-3; 1e-6 a reported target); T4.6 tolerance |(G D)_i - w_i| <= 1e-10 rowscale_i ||D||.

## Results, run g2_v1 (frozen manifest outputs/manifests/code_manifest_g2_v1.json, sha256 edb5e7aa780692025733ccbde8a40251cf9bb0b050fe229bc72dc836530b3463)

Lead ruling (NOTES_FOR_TEAM 04:29Z): T0/T1 and T2 of g2_v1 are admissible with the deviations stated below; the T3 trust-matrix
preview (feasible matrix, column scales, singular values) is not evidence; a full rerun g2_v2 under a new manifest adds the
chart860 rank-statement fix, T2.7 (all 860 generators against hp860) and items (b) to (g); the seed is regenerated into a check
directory and compared with the sealed seed. Deviations of g2_v1 from the plan: T0.3 covered 32 high generators (all 60 low);
T0.5 Decimal strain tolerance was 1e-55 (measured 1e-59); R_f and T2.1b are diagnostics; T2.2 is indirect (c0-chain derivative).

### T0/T1 (g2_v1/t0t1.json, 111 s, began 2026-10-24T04:23:18Z)
| check | value | tolerance | result |
|---|---:|---:|---|
| T0.1_canonical_860_unique_bijective | True | boolean | PASS |
| T0.1_per_j_215_per_jm_26_minus_m | True | boolean | PASS |
| T0.2_Tinv_T_identity_low_digits60 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_high_rel_digits60 | 4.664e-60 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_low_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_high_rel_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_T_block_triangular_nonzero_diagonal | True | boolean | PASS |
| T0.2b_frozen_Nn_hex_equal_lead_manifest | True | boolean | PASS |
| T0.2b_N0_exactly_one | True | boolean | PASS |
| T0.2b_production_mode_chi_matches_frozen_Nn_value_rel | 2.597e-16 | 1.0e-14 | PASS |
| T0.3_low_identities_digits85 | 0.000e+00 | 1.0e-40 | PASS |
| T0.3_high_identities_digits85 | 3.310e-52 | 1.0e-40 | PASS |
| T0.4_old_core_identities_digits85 | 1.759e-54 | 1.0e-40 | PASS |
| T0.3_low_identities_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.3_high_identities_digits110 | 3.618e-77 | 1.0e-40 | PASS |
| T0.4_old_core_identities_digits110 | 1.529e-79 | 1.0e-40 | PASS |
| T0.5_strain_equals_jet_h_cl1.8090 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl1.8090 | 1.000e-59 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl1.8090 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl1.8090 | 6.403e-14 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl1.8090 | 5.353e-14 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl1.5000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl1.5000 | 2.000e-59 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl1.5000 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl1.5000 | 1.303e-13 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl1.5000 | 2.584e-13 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl2.5000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl2.5000 | 0.000e+00 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl2.5000 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl2.5000 | 5.910e-15 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl2.5000 | 3.751e-13 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl4.0000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl4.0000 | 0.000e+00 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl4.0000 | 0.000e+00 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl4.0000 | 4.078e-15 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl4.0000 | 3.385e-15 | 1.0e-12 | PASS |
| T1.0_accepted278_sha256 | True | boolean | PASS |
| T1.1b_raw_a_vs_lead_min_agreeing_digits | -4.933e+01 | -4.0e+01 | PASS |
| T1.1b_lead_assumes_I_order | True | boolean | PASS |
| T1.1_a000_elimination_minus_b00_b01_b02 | 8.269e-89 | 1.0e-80 | PASS |
| T1.1_a000_equals_map_B_value | 0.000e+00 | 1.0e-80 | PASS |
| T1.1_a000_lead_reference_40_digits | 4.009e-40 | 1.0e-39 | PASS |
| T1.2_low_max_abs_20.1129691482296_at_003 | 3.306e-14 | 1.0e-12 | PASS |
| T1.3_high_equals_old_globals_bitwise | True | boolean | PASS |
| T1.3_c300_equals_b32 | True | boolean | PASS |
| T1.3_nonzero_internal_count_186 | True | boolean | PASS |
| T1.4_center_defect_zero | 0.000e+00 | 1.0e-80 | PASS |
| T1.4_C5_raw_defects_max | 7.944e-14 | 1.0e-12 | PASS |
| T1.4_C5_float_chart_vs_json_constraints_decimal | 6.029e-14 | 1.0e-12 | PASS |
| T1.4_C5_from_exact_map_vs_json | 8.460e-67 | 1.0e-60 | PASS |
| T1.4_center_from_exact_map | 4.562e-88 | 1.0e-60 | PASS |
| T1.5_poisson_identities | 1.300e-97 | 1.0e-60 | PASS |
| T1.6_a0 | 3.746e-17 | 1.0e-13 | PASS |
| T1.6_Wx | 1.541e-15 | 1.0e-12 | PASS |
| T1.6_Wy | 3.078e-15 | 1.0e-12 | PASS |
| T1.7_a_8_25_0 | 2.325e-12 | 1.0e-10 | PASS |
| T1.7_k26_leakage_coefficient | 3.553e-11 | 1.0e-09 | PASS |

Identity worst cases: 85 digits: high-vs-monomial 3.31e-52, old core vs map B 1.76e-54; 110 digits: 3.62e-77 and 1.53e-79
(precision independence). The 50-digit canonical record round-trips the internal high coordinates to 4.6e-39 relative only
(T0.2 record loss; the internal hex coordinates are authoritative). Widths at the seed: W_x = 2.779566955587201540916207,
W_y = 2.205292514417036922360838, l = 0.90657765194864065, eta = 0.23143498449754931. Low max |a| = 20.11296914822956694 at (0,0,3).
Seed written: outputs/campaign860/seed/seed_860.json (sha256 d80ad6eb2336a61177dd89609f594ebaadfd50e4dcf63cdad26e777aff29b0e5), content verified by the lead (04:29Z).

### T2 (g2_v1/t2.json, 131 s)
| check | value | tolerance | result |
|---|---:|---:|---|
| T2.1_fields_cl1.8090_trial0 | 6.578e-13 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl1.8090_trial0 | 5.240e-15 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl1.8090_trial0 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl1.8090_trial1 | 9.900e-14 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl1.8090_trial1 | 2.011e-14 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl1.8090_trial1 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl1.5000_trial0 | 2.907e-14 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl1.5000_trial0 | 1.623e-14 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl1.5000_trial0 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl1.5000_trial1 | 2.580e-14 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl1.5000_trial1 | 1.562e-14 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl1.5000_trial1 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl2.5000_trial0 | 1.329e-14 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl2.5000_trial0 | 8.612e-15 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl2.5000_trial0 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl2.5000_trial1 | 2.168e-14 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl2.5000_trial1 | 7.155e-15 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl2.5000_trial1 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl4.0000_trial0 | 4.986e-15 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl4.0000_trial0 | 2.696e-15 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl4.0000_trial0 | 0.000e+00 | 1.0e-11 | PASS |
| T2.1_fields_cl4.0000_trial1 | 3.456e-15 | 1.0e-11 | PASS |
| T2.3_total_cl_derivative_with_c0_chain_cl4.0000_trial1 | 2.154e-15 | 1.0e-11 | PASS |
| T2.2_c0_chain_dc0dcl_rel_cl4.0000_trial1 | 0.000e+00 | 1.0e-11 | PASS |
| T2.4_origin_overlap_order20 | 8.272e-25 | 6.8e-16 | PASS |
| T2.4_origin_overlap_order24 | 8.272e-25 | 6.8e-16 | PASS |
| T2.6_infinity_spots_fields_band_scaled | 1.394e-14 | 1.0e-11 | PASS |

Per quantity (band-scaled worst over 7 bands x 12 points, both axes included), fields f, f_x, f_y, psi_x, psi_y, psi_x/y, q:
at most 6.6e-13 (q, seed cl) and otherwise 1e-14 level; total c_l derivatives at most 2.0e-14. R_f band-scaled diagnostic:
up to 1.1e-9 (seed cl) and 8.7e-11 (c_l = 4), consistent with eps times the term sum divided by the band maximum of the
cancelled residual. Origin overlap at r = 0.02: order 20 and 24 series vs own 85-digit value 8.27e-25 (tolerance 6.8e-16);
the old ideal-sqrt reference differs from the frozen-N_n reference by 2.3e-18 in R_f there (normalization semantics).
Infinity spots e^24, e^32, e^44: all seven fields within 1.4e-14 of the 50-digit values (band-scaled); R_f band ratios
1.6e-8, 1.2e-7, 2.6e-5 (float64 cancellation of the residual at extreme radii, measured and reported, not gated).
Sampled per-column chain rule (diagnostic): the old offset generators (s = 1, 2, column 17 = old (3,2)) lose relative
accuracy in the infinity band as SPEC v5 section 5 states; the gate is T4.1 on the training mesh (g2_v1 T3: all 186 columns
pass the column-norm rule, see T3 below).

### T3 (+T2.5, T4.1 chain rule, T5) of g2_v1 (g2_v1/t3.json, 04:27-05:14Z) -- PRE-REPAIR evaluator (order-20 origin series, direct linear transport, frozen float64 high block); results are diagnostics of that model per the lead's 05:17Z ruling; the T4.8 preview (chart, scales, spectrum) of this run is not evidence of any kind
| check | value | tolerance | result |
|---|---:|---:|---|
| T3.0_seed_json_matches_embedding | True | boolean | PASS |
| T3.4_repeat_same_process_bitwise | True | boolean | PASS |
| T3.1_training_residual_rel_norm | 5.483e-11 | 1.0e-09 | PASS |
| T3.1_training_max_dRf_over_aref | 1.145e-14 | 1.0e-12 | PASS |
| T2.5_infinity_block_residual_rel_norm | 4.858e-10 | 1.0e-09 | PASS |
| T4.1_jacobian_chain_rule_all_columns | True | boolean | PASS |
| T2.5_infinity_block_jacobian_columns | True | boolean | PASS |
| T3.2_refined_residual_rel_norm | 5.017e-11 | 1.0e-09 | PASS |
| T3.2_refined_max_dRf_over_aref | 1.087e-14 | 1.0e-12 | PASS |
| T3.5_J_abs_difference | 1.610e-21 | 4.3e-18 | PASS |
| T3.5_errors_conclusive | 5.561e-21 | 4.3e-18 | PASS |
| T3.5_new_accuracy_passed | True | boolean | PASS |
| T3.5_new_overlap_passed | True | boolean | PASS |
| T3.6_frozen32_E_f_max_rel | 4.491e-12 | 1.0e-10 | PASS |
| T3.6_frozen32_E_rho_max_rel | 4.916e-12 | 1.0e-10 | PASS |
| T3.6_all_regions_worst_rel | 1.281e-09 | 1.0e-10 | FAIL |
| T5.2_fresh_process_strict_replay_64eps | True | 1.3e-18 | PASS |

Notes: T3.6_all_regions_worst_rel is my own stricter per-region extension (the SPEC criterion is the frozen/refined maxima, which pass at 4.5e-12 and 4.9e-12); the 1.28e-9 comes from the near-origin region (E_f maximum 1.6e-6 there), where the 181D and 860 evaluators differ at the 1e-15 absolute level of a small maximum. T5.2 printed FAIL because of a keyword collision in my test helper (the child replay itself passed: the replay JSON shows passed=true, difference 0.0, bitwise); the helper is fixed for g2_v2. Independent J_abs of the seed: 860 evaluator 4.2683726070971950e-09 (error 3.49e-21), 181D evaluator 4.2683726070955853e-09 (error 2.07e-21), difference 1.61e-21 against the cap 4.27e-18 (conclusive). Block residual relative norms: origin 6.0e-10, middle 5.5e-11, infinity 4.9e-10 (max |dR_f|/a_ref 2.2e-19, 1.1e-14, 1.6e-17). Timings of the pre-repair model on the training mesh: cache build 90.9 s, Jacobian 19.9 s (origin series 18.2 s), SVD values 7.9 s, stateless refined mesh 190.7 s, independent integral at target 1e-18: 1178 s (860) vs 366 s (181D).

## Results, run g2_v3 (repaired evaluator, SPEC v7/v8/v8.1; frozen manifest code_manifest_g2_v3.json sha256 44582e5e7283adbb82be40d07f659178100b3d6332b603da5090f369d98eef65; chain started 05:37:56Z; section written 2026-10-24T05:41Z, extended as steps finish)

Manifest g2_v2 (7fa2de6f...) was frozen with a syntax error in tests/g2_t26.py, stopped during t0t1 and superseded; no evidence under it.

### T0/T1 (g2_v3/t0t1.json, 110 s)
| check | value | tolerance | result |
|---|---:|---:|---|
| T0.1_canonical_860_unique_bijective | True | boolean | PASS |
| T0.1_per_j_215_per_jm_26_minus_m | True | boolean | PASS |
| T0.2_Tinv_T_identity_low_digits60 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_high_rel_digits60 | 4.664e-60 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_low_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_Tinv_T_identity_high_rel_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.2_T_block_triangular_nonzero_diagonal | True | boolean | PASS |
| T0.2b_frozen_Nn_hex_equal_lead_manifest | True | boolean | PASS |
| T0.2b_N0_exactly_one | True | boolean | PASS |
| T0.2b_production_mode_chi_matches_frozen_Nn_value_rel | 2.597e-16 | 1.0e-14 | PASS |
| T0.3_low_identities_digits85 | 0.000e+00 | 1.0e-40 | PASS |
| T0.3_high_identities_digits85 | 3.310e-52 | 1.0e-40 | PASS |
| T0.4_old_core_identities_digits85 | 1.759e-54 | 1.0e-40 | PASS |
| T0.3_low_identities_digits110 | 0.000e+00 | 1.0e-40 | PASS |
| T0.3_high_identities_digits110 | 3.618e-77 | 1.0e-40 | PASS |
| T0.4_old_core_identities_digits110 | 1.529e-79 | 1.0e-40 | PASS |
| T0.5_strain_equals_jet_h_cl1.8090 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl1.8090 | 1.000e-59 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl1.8090 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl1.8090 | 6.403e-14 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl1.8090 | 5.353e-14 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl1.5000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl1.5000 | 2.000e-59 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl1.5000 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl1.5000 | 1.303e-13 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl1.5000 | 2.584e-13 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl2.5000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl2.5000 | 0.000e+00 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl2.5000 | 9.095e-13 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl2.5000 | 5.910e-15 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl2.5000 | 3.751e-13 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_cl4.0000 | 0.000e+00 | 1.0e-12 | PASS |
| T0.5_strain_equals_jet_h_decimal_cl4.0000 | 0.000e+00 | 1.0e-55 | PASS |
| T0.5_old_core_jets_via_B_map_cl4.0000 | 0.000e+00 | 1.0e-11 | PASS |
| T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl4.0000 | 4.078e-15 | 1.0e-12 | PASS |
| T0.5_low_evaluator_cl_derivative_envelope_rel_cl4.0000 | 3.385e-15 | 1.0e-12 | PASS |
| T1.0_accepted278_sha256 | True | boolean | PASS |
| T1.1b_raw_a_vs_lead_min_agreeing_digits | -4.933e+01 | -4.0e+01 | PASS |
| T1.1b_lead_assumes_I_order | True | boolean | PASS |
| T1.1_a000_elimination_minus_b00_b01_b02 | 8.269e-89 | 1.0e-80 | PASS |
| T1.1_a000_equals_map_B_value | 0.000e+00 | 1.0e-80 | PASS |
| T1.1_a000_lead_reference_40_digits | 4.009e-40 | 1.0e-39 | PASS |
| T1.2_low_max_abs_20.1129691482296_at_003 | 3.306e-14 | 1.0e-12 | PASS |
| T1.3_high_equals_old_globals_bitwise | True | boolean | PASS |
| T1.3_c300_equals_b32 | True | boolean | PASS |
| T1.3_nonzero_internal_count_186 | True | boolean | PASS |
| T1.4_center_defect_zero | 0.000e+00 | 1.0e-80 | PASS |
| T1.4_C5_raw_defects_max | 7.944e-14 | 1.0e-12 | PASS |
| T1.4_C5_float_chart_vs_json_constraints_decimal | 6.029e-14 | 1.0e-12 | PASS |
| T1.4_C5_from_exact_map_vs_json | 8.460e-67 | 1.0e-60 | PASS |
| T1.4_center_from_exact_map | 4.562e-88 | 1.0e-60 | PASS |
| T1.5_poisson_identities | 1.300e-97 | 1.0e-60 | PASS |
| T1.6_a0 | 3.746e-17 | 1.0e-13 | PASS |
| T1.6_Wx | 1.541e-15 | 1.0e-12 | PASS |
| T1.6_Wy | 3.078e-15 | 1.0e-12 | PASS |
| T1.7_a_8_25_0 | 2.325e-12 | 1.0e-10 | PASS |
| T1.7_k26_leakage_coefficient | 3.553e-11 | 1.0e-09 | PASS |
| T1.8_regenerated_seed_equals_sealed_seed_content_fields | False | boolean | FAIL |

T1.8 note: the regenerated seed (outputs/g2/g2_v3/seed_check/seed_860.json) differs from the sealed seed_860.json only in implementation
descriptors (basis_version and the manifest block: version, origin orders, switch radius, replay file, providers, longdouble statement,
derivative version; the three triple lists differ only as JSON lists vs tuples). Every coefficient field is identical. Import closure
recorded in the JSON (11 work-tree files for this test).

### g2_v3 chain interruption and rerun (2026-10-24T05:49Z)
The first chain run (bin/run_g2.sh g2_v3, guard session session_g2_v3, policy outputs/g2_policy.json with max_memory_psi_full_avg10 = 5.0)
completed t0t1 and then had t2 (guard run 20261024T053946Z_..._g2_t2) terminated by the guard after 148 s: stop reason "Linux memory PSI
full pressure ceiling" (box-wide PSI full avg10 = 16.67 against the ceiling 5.0, with the worker at 714 MiB RSS and 82% of memory
available, 1-minute load 41 on 96 CPUs from other users' jobs). The guard then held the session, so t3, t26 and the supplement refused
to start. That t2 run is INTERRUPTED (resource) and produced no evidence. The log lines "end <step> rc=0" of run_g2.sh are a harness
defect (the exit status printed is that of the date substitution); step verdicts are read from the guard result.json files.
Rerun: t2, t3, t26 and the supplement under the same manifest 44582e5e in session session_g2_v3_s2 (bin/run_g2_steps.sh, which verifies
every manifested file hash and the frozen 181D closure before each step; verified true at 05:47:04Z), with policy outputs/g2_policy_v2.json
whose only change is the PSI full avg10 ceiling (5 -> 60): PSI is a system-wide contention indicator not attributable to the worker;
the RSS (40 GiB), available-memory (16 GiB, 10%), load (1.5 per CPU) and disk (10 GiB) limits are unchanged. Four non-chain files edited
after the freeze were restored to their frozen bytes before the rerun (hashes verified); their edited versions are kept in
outputs/g2/pending_edits/ for the G3/G4 manifests.


## g2_v3 record closure and the v9 chain (2026-10-24T06:43:11Z)
- g2_v3 (manifest 44582e5e...) is a G2 FAILURE by the lead ruling of 05:58Z (SPEC v9): T2.6c R_f fails at its own frozen points by the verifier's MP170 references (one-point Model860 7.12e-9 of band_max in [0.02, 0.1) at (0.03, 0); batch 7.07e-9; stateless 1.05e-8; batch and stateless 1.15e-11 and 1.13e-11 in [10, 1e3)). All 860 columns passed there. Second failure (SPEC v9.1): the high route at c_l = 2 and 3 (44 values each, m = 0 generators with p_j = 1, far bands, worst 9.2e-5); the low block fails likewise at c_l = 2, 3 and near-integer values (verifier, v9.2).
- The g2_v3 chain was stopped by numerics at 06:10:12Z after t2 (rc 0, 05:47:04Z to 06:00:16Z; lead-authorized stop). Record: t0t1 PASS except T1.8 (harness scope FAIL, SPEC v8.2), t2 rehearsal PASS (outputs/g2/g2_v3/t2.json), t3/t26/supplement not run. T2.6c R_f: FAIL (verifier evidence).
- Reference defects disclosed (SPEC v9 References): the g2_v3 hp_point rounded the center-elimination factor -s_i/s_0 to binary64 before Decimal conversion (verifier bound: at most 6.4e-13 of the band-1 scale), and hp860.independent_fields returned the background fields in binary64 for the Jacobian reference (below 1e-11 in every gated band, up to 8.1e-11 at e^32 and 2.2e-8 at e^44). Both are Decimal in hp860.point_reference of the v9 library.
- Next chain g2_v4 (SPEC v9 to v9.3): steps t0t1 (with corrected T1.8), t2, t26 (three shapes, T2.6b at e24/e32/e44 and the largest mesh radii, T2.6c with the r = 1 straddle, T2.6d configurations and 64-eps agreement, T2.6x exceptional parameters, rho with u = 2^-64), t27h (eight c_l values, structural zeros), t3 (v9 excusal procedures, T3.9, replay reference seed_860_replay_v3.npz), supplement (T2.7, T2.6b spots, T3.4b (workers, threads) configurations, T3.7b, T3.8, T5), t27hx (T2.7H-X). Dev check before the freeze: NUM_REPORT.md 2026-10-24T06:43:11Z.

## G2 evidence under frozen manifests g2_v4 (base) and supplements (appended 2026-10-24T10:43:52Z by bin/embedding_tables_v2.py)

Verdict rule (SPEC v9.6 item 4): a step passes only if the runner verdict is ok, the step JSON passed field is true and no check record failed. The per-step table with sha256 values is outputs/g2/G2_SUMMARY.md. Numbers below are copied from the step JSONs.

### T0/T1 (g2_v5 t0t1v2, SPEC v9.6/v9.8): passed = True, 58 checks

| check | value | tolerance |
|---|---|---|
| T0.2_Tinv_T_identity_low_digits60 | 0.000e+00 | 1.000e-40 |
| T0.2_Tinv_T_identity_high_rel_digits60 | 4.664e-60 | 1.000e-40 |
| T0.2_Tinv_T_identity_low_digits110 | 0.000e+00 | 1.000e-40 |
| T0.2_Tinv_T_identity_high_rel_digits110 | 0.000e+00 | 1.000e-40 |
| T0.2_T_block_triangular_nonzero_diagonal | True | boolean |
| T0.2b_frozen_Nn_hex_equal_lead_manifest | True | boolean |
| T0.2b_N0_exactly_one | True | boolean |
| T0.2b_production_mode_chi_matches_frozen_Nn_value_rel | 2.597e-16 | 1.000e-14 |
| T0.3_low_identities_digits85 | 3.640e-70 | 1.000e-40 |
| T0.3_high_identities_digits85 | 3.310e-52 | 1.000e-40 |
| T0.4_old_core_identities_digits85 | 8.241e-54 | 1.000e-40 |
| T0.3_low_identities_digits110 | 2.299e-95 | 1.000e-40 |
| T0.3_high_identities_digits110 | 3.618e-77 | 1.000e-40 |
| T0.4_old_core_identities_digits110 | 1.529e-79 | 1.000e-40 |
| T0.5_low_evaluator_vs_90digit_reference_envelope_rel_cl1.8090 | 5.941e-15 | 1.000e-12 |
| T0.5_low_evaluator_cl_derivative_vs_90digit_reference_envelope_rel_cl1.8090 | 2.370e-15 | 1.000e-12 |
| T0.5_low_evaluator_vs_90digit_reference_envelope_rel_cl1.5000 | 2.552e-15 | 1.000e-12 |
| T0.5_low_evaluator_cl_derivative_vs_90digit_reference_envelope_rel_cl1.5000 | 2.157e-14 | 1.000e-12 |
| T0.5_low_evaluator_vs_90digit_reference_envelope_rel_cl2.5000 | 2.447e-15 | 1.000e-12 |
| T0.5_low_evaluator_cl_derivative_vs_90digit_reference_envelope_rel_cl2.5000 | 2.083e-15 | 1.000e-12 |
| T0.5_low_evaluator_vs_90digit_reference_envelope_rel_cl4.0000 | 4.370e-15 | 1.000e-12 |
| T0.5_low_evaluator_cl_derivative_vs_90digit_reference_envelope_rel_cl4.0000 | 1.934e-15 | 1.000e-12 |
| T1.1b_raw_a_vs_lead_min_agreeing_digits | -4.933e+01 | -4.000e+01 |
| T1.1b_lead_assumes_I_order | True | boolean |
| T1.1_a000_elimination_minus_b00_b01_b02 | 8.269e-89 | 1.000e-80 |
| T1.1_a000_equals_map_B_value | 0.000e+00 | 1.000e-80 |
| T1.1_a000_lead_reference_40_digits | 4.009e-40 | 1.000e-39 |
| T1.2_low_max_abs_20.1129691482296_at_003 | 3.306e-14 | 1.000e-12 |
| T1.3_high_equals_old_globals_bitwise | True | boolean |
| T1.3_c300_equals_b32 | True | boolean |
| T1.3_nonzero_internal_count_186 | True | boolean |
| T1.5_poisson_identities | 3.100e-97 | 1.000e-60 |
| T1.6_a0 | 3.746e-17 | 1.000e-13 |
| T1.6_Wx | 1.541e-15 | 1.000e-12 |
| T1.6_Wy | 3.078e-15 | 1.000e-12 |
| T1.7_a_8_25_0 | 2.325e-12 | 1.000e-10 |
| T1.7_k26_leakage_coefficient | 3.553e-11 | 1.000e-09 |
| T1.8_content_fields_equal_after_json_normalization_v96 | True | boolean |

### T2.1 to T2.4 fields and c_l derivatives at four c_l values (g2_v4 t2): passed = True, 27 checks; worst check value / tolerance = 7.528e-02

### T2.6b/c/d/x residual and complete columns, three shapes (g2_v4 t26): passed = True, 152 checks

| band | R_f ratio (single/batch/stateless) | columns ratio (single/batch/stateless) |
|---|---|---|
| origin | 0.000e+00 / 0.000e+00 / 0.000e+00 | 4.055e-14 / 4.055e-14 / 4.055e-14 |
| b1 | 7.079e-14 / 7.079e-14 / 7.079e-14 | 6.559e-13 / 6.559e-13 / 6.559e-13 |
| b2 | 5.547e-14 / 5.547e-14 / 5.547e-14 | 3.061e-15 / 3.061e-15 / 3.061e-15 |
| b3 | 2.516e-14 / 2.516e-14 / 2.516e-14 | 1.225e-15 / 1.225e-15 / 2.079e-15 |
| b4 | 2.716e-16 / 2.716e-16 / 2.716e-16 | 4.521e-15 / 4.521e-15 / 4.521e-15 |
| b5 | 7.429e-19 / 7.429e-19 / 0.000e+00 | 1.613e-15 / 1.613e-15 / 1.971e-15 |
| e24 | 0.000e+00 / 0.000e+00 / 0.000e+00 | 7.423e-16 / 1.114e-15 / 1.114e-15 |
| e32 | 5.986e-17 / 5.986e-17 / 5.986e-17 | 1.394e-15 / 1.549e-15 / 1.549e-15 |
| e44 | 4.187e-17 / 4.187e-17 / 4.187e-17 | 1.411e-15 / 8.683e-16 / 8.683e-16 |
| rmax_training | 0.000e+00 / 0.000e+00 / 0.000e+00 | 6.852e-16 / 1.417e-15 / 1.417e-15 |
| rmax_refined | 1.181e-16 / 1.181e-16 / 1.181e-16 | 8.019e-16 / 2.597e-15 / 2.597e-15 |

T2.6d: largest configuration difference of R_f 0.000e+00; training-sized call {"points_total": 90681, "direct_nodes": 86067, "block_size": 4096, "full_blocks": 21, "remainder_block_nodes": 51, "embedded_copies": ["start", "middle", "end (remainder chunk)"]}; T2.6x (c_l = 2, 3, 2(1+2^-20), 3(1-2^-20)) worst R_f 1.171e-16, worst columns 2.554e-13.

### T2.7H (g2_v4 t27h): passed = True, 20 checks

| c_l | worst field ratio | worst c_l-derivative ratio | floor cases |
|---|---|---|---|
| 1.02 | 3.306e-13 | 7.790e-14 | 0 |
| 2.0 | 3.527e-13 | 3.635e-13 | 416 |
| 3.0 | 3.141e-13 | 3.622e-13 | 562 |
| 10.0 | 3.560e-13 | 9.157e-14 | 1323 |
| 1.9999980926513672 | 3.821e-13 | 2.444e-13 | 86 |
| 2.000001907348633 | 3.120e-13 | 1.962e-13 | 86 |
| 2.999997138977051 | 3.387e-13 | 3.686e-13 | 245 |
| 3.000002861022949 | 3.401e-13 | 4.337e-13 | 245 |

### T2.7H-X (g2_v4 t27hx): passed = True, 24 checks

| c_l | worst field ratio | worst c_l-derivative ratio | floor cases |
|---|---|---|---|
| 1.9999999999999998 | 3.527e-13 | 2.943e-13 | 206 |
| 2.0000000000000004 | 3.527e-13 | 1.734e-13 | 204 |
| 1.9999999981373549 | 3.656e-13 | 1.074e-13 | 102 |
| 2.000000001862645 | 3.399e-13 | 4.670e-13 | 102 |
| 1.999999999998181 | 3.505e-13 | 4.263e-13 | 102 |
| 2.000000000001819 | 3.549e-13 | 1.209e-13 | 102 |
| 2.9999999999999996 | 3.141e-13 | 4.713e-13 | 359 |
| 3.0000000000000004 | 3.141e-13 | 1.554e-13 | 357 |
| 2.9999999972060323 | 3.239e-13 | 3.622e-13 | 248 |
| 3.0000000027939677 | 3.378e-13 | 4.617e-13 | 248 |
| 2.9999999999972715 | 3.609e-13 | 3.831e-13 | 248 |
| 3.0000000000027285 | 3.725e-13 | 4.947e-13 | 248 |

### T2.7H-X2 (g2_v6 t27hx2): passed = True, 24 checks

| c_l | worst field ratio | worst c_l-derivative ratio | floor cases |
|---|---|---|---|
| 1.9999999999999998 | 3.527e-13 | 2.943e-13 | 206 |
| 2.0000000000000004 | 3.527e-13 | 1.734e-13 | 204 |
| 1.9999999981373549 | 3.656e-13 | 1.074e-13 | 102 |
| 2.000000001862645 | 3.399e-13 | 4.670e-13 | 102 |
| 1.999999999998181 | 3.505e-13 | 4.263e-13 | 102 |
| 2.000000000001819 | 3.549e-13 | 1.209e-13 | 102 |
| 2.9999999999999996 | 3.141e-13 | 4.713e-13 | 359 |
| 3.0000000000000004 | 3.141e-13 | 1.554e-13 | 357 |
| 2.9999999972060323 | 3.239e-13 | 3.622e-13 | 248 |
| 3.0000000027939677 | 3.378e-13 | 4.617e-13 | 248 |
| 2.9999999999972715 | 3.609e-13 | 3.831e-13 | 248 |
| 3.0000000000027285 | 3.725e-13 | 4.947e-13 | 248 |

### T2.7H_floor (g2_v7 t27hfloor): passed = True, 10 checks

| c_l | worst field ratio | worst c_l-derivative ratio | floor cases |
|---|---|---|---|
| 2.0 | 3.527e-13 | 3.635e-13 | 416 |
| 3.0 | 3.141e-13 | 3.622e-13 | 562 |
| 10.0 | 3.560e-13 | 9.157e-14 | 1323 |

### T3/T4.1/T5 seed reproduction (g2_v4 t3): passed = True, 19 checks

| check | value | tolerance |
|---|---|---|
| T3.0_seed_json_matches_embedding | True | boolean |
| T3.4_repeat_same_process_bitwise | True | boolean |
| T3.1_training_residual_rel_norm | 3.329e-11 | 1.000e-09 |
| T3.1_training_max_dRf_over_aref | 7.477e-15 | 1.000e-12 |
| T2.5_infinity_block_residual_rel_norm | 2.704e-10 | 1.000e-09 |
| T4.1_jacobian_chain_rule_all_columns | True | boolean |
| T2.5_infinity_block_jacobian_columns | True | boolean |
| T3.9_training_residual_stateless_vs_production_64eps | 0.000e+00 | 1.313e-18 |
| T3.2_refined_residual_rel_norm | 3.215e-11 | 1.000e-09 |
| T3.2_refined_max_dRf_over_aref | 8.492e-15 | 1.000e-12 |
| T3.5_J_abs_difference | 5.294e-23 | 4.271e-18 |
| T3.5_errors_conclusive | 2.684e-21 | 4.268e-18 |
| T3.5_new_accuracy_passed | True | boolean |
| T3.5_new_overlap_passed | True | boolean |
| T3.6_frozen32_E_f_max_rel | 2.954e-12 | 1.000e-10 |
| T3.6_frozen32_E_rho_max_rel | 3.046e-12 | 1.000e-10 |
| T3.6_all_regions_worst_rel_diagnostic_with_excusal | True | boolean |
| T5.0_replay_file_coefficient_arrays_bitwise_equal_sealed_g2_v1 | True | boolean |
| T5.2_fresh_process_strict_replay_64eps | True | boolean |

Timings (s): {"old_v3_fun_cold_s": 39, "old_v3_jacobian_s": 8, "new_fun_cold_s": 193, "new_cache_build_s": 131, "new_origin_series_value_s": 57, "new_jacobian_s": 120, "new_origin_series_total_s": 167, "stateless_training_s": 96, "new_stateless_refined_s": 199, "independent_integral_new_s": 868, "independent_integral_old_s": 370, "replay_fresh_process_s": 172}
Replay reference: @OUTPUT_REALPATH@/campaign860/seed/seed_860_replay_v3.npz (sha256 ee2ba0afa60e1dff).

### SPEC v9.7 rounding calibration (g2_v10 kappa): passed = True, 3 checks

rho_max = 4.837e+01 at {"cl_label": "cl3minus2m20", "point": "b3", "path": "single", "rho": 48.37027853518094, "S_R": 29775.822573794085, "abs_error": 2.9507650201801695e-13}; kappa = 2048.0; coverage {"T2.6c_finite_v92": 19, "T2.6b_far": 9, "T2.6d": "same T2.6c points embedded in the training-sized call (covered)", "T3.6_diagnosed_points": 5, "T2.6x_parameter_values": [1.8089923602744993, 2.0, 3.0, 2.000001907348633, 2.999997138977051], "note": "the T2.6x parameter values (seed c_l, 2, 3, 2(1+2^-20), 3(1-2^-20)) are covered at every point set below", "T3.6_source": {"path": "@OUTPUT_REALPATH@/g2/g2_v4/t3.json", "sha256": "2d729aa1bceed5be9263babb7fd3240034b8ce12bd92bf03a1e9ad2d499c777d", "regions": 1, "points_per_region": {"near_origin": 5}}, "near_y_axis_.

### Supplement v2 (g2_v11 supplement2): passed = True, 12 checks

| check | value | tolerance |
|---|---|---|
| T2.7_all_generators_fields_band_scaled_cl1.8090 | 2.677e-14 | 1.000e-11 |
| T2.7_all_generators_dcl_band_scaled_cl1.8090 | 2.825e-14 | 1.000e-11 |
| T2.7_all_generators_fields_band_scaled_cl2.5000 | 2.529e-14 | 1.000e-11 |
| T2.7_all_generators_dcl_band_scaled_cl2.5000 | 3.165e-14 | 1.000e-11 |
| T2.6b_jacobian_spot_columns_e24_band_scaled | 7.423e-16 | 1.000e-11 |
| T2.6b_new_production_Rf_e32_e44_band_scaled | 5.986e-17 | 1.000e-11 |
| T3.4b_fresh_processes_and_threads_bitwise | True | boolean |
| T3.7b_independent_integral_L1_accuracy | True | boolean |
| T3.7b_frozen_rule_dilation_errors_small | 1.822e-14 | 1.000e-09 |
| T3.8_widths_baseline_recorded_and_bound | True | boolean |
| T5_seed_files_read_only_0444 | True | boolean |
| T5_replay_reference_coefficients_bitwise_equal_sealed_seed | True | boolean |


## G3 T4 (feasible chart gate) on the frozen g3_v1 bytes (appended 2026-10-24T17:2xZ)
Manifest g3_v1 sha256 fcedf0984e7ca9b53479d44c8291517f13fd0983123f82ea440742b1cd302165. Session s1 (12:50:01Z, policy v3, 3 h): lead-ordered budget stop at 13:31:47Z (result.json returncode -15, 'supervisor received signal 15'), no verdict. Session s3 (13:32:15Z to 17:09:45Z, outputs/g3_t4_policy.json, 8 h, identical bytes): run 20261024T133215Z_1792848735809499497_g3_t4; result.json success true, returncode 0, wall 13049.98 s; t4.json sha256 f48311553b85264aed5da663ebf89d30ab649be44a3ab896a09329d7d18dacab.

| check | value | verdict |
|---|---|---|
| T4.0 seed JSON P/high equal the replay arrays | True | PASS |
| T4.2 reduced C5 rank 5 of 5 x 60; coefficient block rank 5; unreduced center + C5 rank 6 of 6 x 61 (singular values 1.2e5 ... 53); C5 block rank 5 | True | PASS |
| T4.3 tangent rank 55; complete rank 60; G T | 1.157e-11 | PASS |
| T4.3 old 19 tangents inside the new 55 (low projection); inside the embedded 855 | 1.05e-15; 1.11e-15 | PASS |
| T4.4 three random lifts: C5 max; c_l bits preserved; FD tangent | 1.8e-13, 1.2e-13, 6.9e-14; True; 5.8e-11, 2.8e-10, 1.7e-10 | PASS |
| T4.6 dilation tangency rows | 3.81e-19 | PASS |
| T4.7 zero step vs seed residual; through the chart; through campaign860.feasible_trial with the cache cleared (recomputed) | bitwise | PASS |
| T4.8 all 855 singular values positive; count 855; A shape 90624 x 855 | sigma_max 9.6204, median 2.06e-15, s_min 4.14e-18 | PASS |
| T4.5 c_l along the chart (best relative error, all three steps within 1e-3, lifted C5 < 1e-10) | 1.92e-10 | PASS |
| T4.5 five low tangents (38, 35, 43, 34, 27) | 1.10e-10 to 1.83e-10 | PASS |
| T4.5 sixteen high directions (all four j, small and large n; threshold 3e-5) | 2.1e-16 to 6.8e-15 | PASS |
| T4.5 projected dilation D | 7.93e-13 | PASS |
| T4.5 weakest right singular vectors 0, 1, 2 (relative error vs threshold 1e-3) | 2635, 3338, 2174 (||A v|| 3.6e-15, 3.6e-15, 2.5e-15; absolute discrepancies 9.4e-12, 1.2e-11, 5.5e-12 at h = 1e-4) | FAIL (exception E-T4.5w) |
| T4.5 gates (best step; all steps and lifted C5) | False | FAIL |

Strict verdict: FAIL (27 of 29 checks). Lead ruling T4-R1 (17:12Z): the three weak rows are a resolution-scope defect of the frozen predicate (the baseline feasible threshold applied to directions whose analytic derivative sits at the numerical null floor); recorded exception E-T4.5w; no rerun, no predicate change; the remaining 23 directions, ranks, lifts, zero-step and spectrum results stand; FINAL reports FAIL plus the exception. Details: outputs/g3/g3_v1/t4_s3_fd_table.md, outputs/g3/g3_v1/t4_interpretation_sidecar.md. Verifier concurrence pending.
