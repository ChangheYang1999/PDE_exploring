# VT-5 reading: clean-process validation of nest10_L10_cl0.45_om+1.0_fixed_p0 start 0 against the saved values (helper compare_vt_nest10_v2.py; written 2026-10-27T18:45:15Z)

Saved sources: S1 runs/.../results.jsonl (worker row 2026-10-26T14:23:30Z); S2 status/ledger.jsonl start_result row; S3 candidates/nest10_L10_cl0.45_om1.0_p0/meta.json diagnostics. 'equal' is bitwise; 'agree to rounding' rel <= 1e-12; 'close' rel <= 1e-6; anything above 1e-6 is listed as DIFFERENT and is read by hand. These labels are reading aids, not thresholds. A match reproduces saved diagnostics from a clean process; it is not new evidence about the state.

Summary: 89 rows; n_match 81 (within 1e-6 relative or identical), n_diff 7, n_missing_vt 0 (saved keys missing in the VT output), n_new 0 (VT values without a saved counterpart; unreviewed), n_definitional 1, n_absent_both 0; identity n_match + n_diff + n_missing_vt + n_new + n_definitional + n_absent_both = 89 = row count (asserted).

| saved key | VT JSON path | VT value | saved value | saved sources | max rel diff | verdict |
|---|---|---|---|---|---|---|
| rho_u_max | spec_training/global_/rho_u_max | 0.04225184206 | 0.04225184206 | S1, S2 | 0.00e+00 | equal |
| rho_u_bal | spec_training/global_/rho_u_bal | 0.01849592493 | 0.01749539347 | S1, S2 | 5.41e-02 | DIFFERENT (rel > 1e-6) |
| rho_nl_max | spec_training/global_/rho_nl_max | 1.104630967 | 1.104630967 | S1, S2 | 0.00e+00 | equal |
| pi_u_max | spec_training/global_/pi_u_max | 0.2557549811 | 0.2557549811 | S1, S2 | 0.00e+00 | equal |
| rho_Om_max | spec_training/global_/rho_Om_max | 0.06485355309 | 0.06485355309 | S1, S2 | 0.00e+00 | equal |
| A_u | spec_training/global_/A_u | 0.002151507269 | 0.002151507269 | S1, S2 | 0.00e+00 | equal |
| A_Om | spec_training/global_/A_Om | 0.000228398543 | 0.000228398543 | S1, S2 | 0.00e+00 | equal |
| N_core | spec_training/nonaxi/N_core | 0.8276193499 | 0.8276193499 | S1, S2 | 0.00e+00 | equal |
| e_core | spec_training/nonaxi/e_core | 0.1266773346 | 0.1266773346 | S1, S2 | 0.00e+00 | equal |
| N_F | spec_training/nonaxi/N_F | 0.634855578 | 0.634855578 | S1, S2 | 0.00e+00 | equal |
| e_F | spec_training/nonaxi/e_F | 0.07366915497 | 0.07366915497 | S1, S2 | 0.00e+00 | equal |
| r_core | spec_training/guards/N4_r_core | 0.4674834908 | 0.4674834908 | S1, S2 | 0.00e+00 | equal |
| r_tail | spec_training/guards/N5_r_tail | 2.381266053 | 2.381266053 | S1, S2 | 0.00e+00 | equal |
| max_U | spec_training/guards/N4_max_U | 1.261343932 | 1.261343932 | S1, S2 | 0.00e+00 | equal |
| lambda_max_S | spec_training/guards/N2_lambda_max_S | 1.211983871 | 1.211983871 | S1, S2 | 0.00e+00 | equal |
| rho_u_max_holdout | spec_holdout/global_/rho_u_max | 0.04195389948 | 0.04195389948 | S1, S2 | 1.65e-16 | agree to rounding (rel <= 1e-12) |
| rho_u_bal_holdout | spec_holdout/global_/rho_u_bal | 0.01681603176 | 0.01606827472 | S1, S2 | 4.45e-02 | DIFFERENT (rel > 1e-6) |
| rho_nl_max_holdout | spec_holdout/global_/rho_nl_max | 1.12863293 | 1.12863293 | S1, S2 | 0.00e+00 | equal |
| pi_u_max_holdout | spec_holdout/global_/pi_u_max | 0.2858193685 | 0.2858193685 | S1, S2 | 9.71e-16 | agree to rounding (rel <= 1e-12) |
| rho_Om_max_holdout | spec_holdout/global_/rho_Om_max | 0.06501908529 | 0.06501908529 | S1, S2 | 0.00e+00 | equal |
| A_u_holdout | spec_holdout/global_/A_u | 0.0004046470998 | 0.0004046470998 | S1, S2 | 0.00e+00 | equal |
| N_core_holdout | spec_holdout/nonaxi/N_core | 0.8268799245 | 0.8268799245 | S1, S2 | 0.00e+00 | equal |
| e_core_holdout | spec_holdout/nonaxi/e_core | 0.1265462042 | 0.1265462042 | S1, S2 | 0.00e+00 | equal |
| r_core_holdout | spec_holdout/guards/N4_r_core | 0.4576511733 | 0.4576511733 | S1, S2 | 0.00e+00 | equal |
| r_tail_holdout | spec_holdout/guards/N5_r_tail | 2.338790614 | 2.338790614 | S1, S2 | 0.00e+00 | equal |
| pressure_ray_check | spec_holdout/pressure/ray_check/max_rel_diff | 1.911562395e-08 | 1.911562245e-08 | S1, S2 | 7.85e-08 | close (rel <= 1e-6) |
| tier_S_holdout | tier_S_holdout/0 | False | False | S1, S2 | n/a | definition differs (worker.py 679 recomputes tier_S with located_lambda_max; validate_candidate.py does not) |
| tier_S_holdout_half | tier_S_holdout_half/0 | False | False | S1, S2 | n/a | equal |
| rho_u_max_holdout_half | two_family/rho_u_max_half | 0.04145045598 | 0.04145045598 | S1, S2 | 0.00e+00 | equal |
| rho_u_max_holdout_both | two_family/rho_u_max_both | 0.04195389948 | 0.04195389948 | S1, S2 | 1.65e-16 | agree to rounding (rel <= 1e-12) |
| rho_nl_max_holdout_half | two_family/rho_nl_max_half | 1.126373255 | 1.126373255 | S1, S2 | 1.97e-16 | agree to rounding (rel <= 1e-12) |
| rho_nl_max_holdout_both | two_family/rho_nl_max_both | 1.12863293 | 1.12863293 | S1, S2 | 0.00e+00 | equal |
| sphere_rho_u_max | two_family/sphere_rho_u_max | 0.0500168078 | 0.0500168078 | S1, S2 | 0.00e+00 | equal |
| sphere_r_at_max | two_family/sphere_r_at_max | 0.5045378492 | 0.5045378492 | S1, S2 | 0.00e+00 | equal |
| sphere_rho_nl_max | two_family/sphere_rho_nl_max | 1.18908721 | 1.18908721 | S1, S2 | 0.00e+00 | equal |
| sphere_r_at_nl_max | two_family/sphere_r_at_nl_max | 5.708194152 | 5.708194152 | S1, S2 | 0.00e+00 | equal |
| rho_lin_max_holdout | two_family/rho_lin_max_std | 0.1537545496 | 0.1537545496 | S1, S2 | 1.81e-16 | agree to rounding (rel <= 1e-12) |
| rho_lin_max_holdout_half | two_family/rho_lin_max_half | 0.1374542785 | 0.1374542785 | S1, S2 | 2.02e-16 | agree to rounding (rel <= 1e-12) |
| rho_sp_max_holdout | two_family/rho_sp_max_std | 1.12863293 | 1.12863293 | S1, S2 | 0.00e+00 | equal |
| rho_sp_max_holdout_half | two_family/rho_sp_max_half | 1.126373255 | 1.126373255 | S1, S2 | 1.97e-16 | agree to rounding (rel <= 1e-12) |
| rho_lin_max_r1_holdout | two_family/rho_lin_max_r1_std | 0.1537545496 | 0.1537545496 | S1, S2 | 1.81e-16 | agree to rounding (rel <= 1e-12) |
| rho_sp_max_r1_holdout | two_family/rho_sp_max_r1_std | 0.1537545496 | 0.1537545496 | S1, S2 | 1.81e-16 | agree to rounding (rel <= 1e-12) |
| d30_Ru_over_T1_r1 | two_family/d30_Ru_over_T1_r1 | 0.2894783269 | 0.2894783269 | S1, S2 | 0.00e+00 | equal |
| d30_ROm_over_Om | two_family/d30_ROm_over_Om | 0.421366065 | 0.4213659808 | S1, S2 | 2.00e-07 | close (rel <= 1e-6) |
| gram_check_max | two_family/gram_check_max | 6.557725464e-13 | 6.557725464e-13 | S1, S2 | 0.00e+00 | equal |
| sigma_u_max | two_family/sigma_u_max_std | 0.4047748369 | 0.4047748369 | S1, S2 | 1.37e-16 | agree to rounding (rel <= 1e-12) |
| sigma_u_max_shell | two_family/sigma_u_max_shell_std | [0.25, 0.5] | [0.25, 0.5] | S1, S2 | 0.00e+00 | equal |
| sigma_u_max_half | two_family/sigma_u_max_half | 0.3698871487 | 0.3698871487 | S1, S2 | 1.50e-16 | agree to rounding (rel <= 1e-12) |
| sigma_u_max_r1 | two_family/sigma_u_max_r1_std | 0.4047748369 | 0.4047748369 | S1, S2 | 1.37e-16 | agree to rounding (rel <= 1e-12) |
| sigma_Om | two_family/sigma_Om | 0.421366065 | 0.4213659808 | S1, S2 | 2.00e-07 | close (rel <= 1e-6) |
| a_max | two_family/a_max_std | 0.4934334125 | 0.4934334125 | S1, S2 | 0.00e+00 | equal |
| a_max_half | two_family/a_max_half | 0.445981496 | 0.445981496 | S1, S2 | 0.00e+00 | equal |
| origin_U_rms | two_family/origin_U_rms | 1.08942169 | 1.08942169 | S1, S2 | 0.00e+00 | equal |
| origin_B | two_family/origin_B | 2.529721021 | 2.529721021 | S1, S2 | 0.00e+00 | equal |
| origin_L | two_family/origin_L | 0.6170896559 | 0.6170896559 | S1, S2 | 0.00e+00 | equal |
| peak_max_holdout | two_family/peak_max_std | 9.002013173 | 9.002013173 | S1, S2 | 9.87e-16 | agree to rounding (rel <= 1e-12) |
| gram_gamma_shells | two_family/gram_gamma_std | [-0.9998873127539967, -0.999557466909014 | [-0.9998873127539967, -0.999557466909014 | S1, S2 | n/a | DIFFERENT (non-numeric or shape) |
| gram_a_shells | two_family/gram_a_std | [0.5993126646222493, 0.5997288132695304, | [0.5993126646222493, 0.5997288132695304, | S1, S2 | n/a | DIFFERENT (non-numeric or shape) |
| gram_b_shells | two_family/gram_b_std | [0.5883466601491837, 0.5857886370412806, | [0.5883466601491837, 0.5857886370412807, | S1, S2 | n/a | DIFFERENT (non-numeric or shape) |
| G_norm | G_closure/G_norm | 0.401325421 | 0.401325421 | S1, S2 | 0.00e+00 | equal |
| G_closure_rel | G_closure/dist_rel | 1.744480508e-13 | 7.074199538e-14 | S1, S2 | 5.94e-01 | DIFFERENT (rel > 1e-6) |
| G_span_rank | G_closure/rank | 545 | 545 | S1, S2 | 0.00e+00 | equal |
| G_span_columns | G_closure/n_columns | 545 | 545 | S1, S2 | 0.00e+00 | equal |
| G_carried_mismatch_rel | G_closure/carried_mismatch_rel | 0.05634850551 | 0.05634850551 | S1, S2 | 1.35e-15 | agree to rounding (rel <= 1e-12) |
| G_carried_correlation | G_closure/carried_correlation | 0.9984112186 | 0.9984112186 | S1, S2 | 0.00e+00 | equal |
| G_carried_norm | G_closure/G_carried_norm | 0.4008241878 | 0.4008241878 | S1, S2 | 0.00e+00 | equal |
| K_ratio_direct | G_closure/K_ratio_direct | -4.249681669 | -4.249681669 | S1, S2 | 2.51e-15 | agree to rounding (rel <= 1e-12) |
| K_H_required | G_closure/K_H_required | -0.3881918108 | -0.3881918108 | S1, S2 | 4.29e-16 | agree to rounding (rel <= 1e-12) |
| K_H_carried | G_closure/K_H_carried | -0.4047096092 | -0.4047096092 | S1, S2 | 0.00e+00 | equal |
| K_H_ratio_direct | G_closure/K_H_ratio_direct | 1.04255061 | 1.04255061 | S1, S2 | 4.26e-16 | agree to rounding (rel <= 1e-12) |
| K_H_identity_rel_closure | G_closure/K_H_identity_rel_closure | 2.287988553e-14 | 2.245088768e-14 | S1, S2 | 1.88e-02 | DIFFERENT (rel > 1e-6) |
| G_defect_F_component | G_closure/G_defect_F_component | 0.01621401957 | 0.01621401957 | S1, S2 | 6.42e-16 | agree to rounding (rel <= 1e-12) |
| G_defect_cos_F | G_closure/G_defect_cos_F | 0.7169875604 | 0.7169875604 | S1, S2 | 6.19e-16 | agree to rounding (rel <= 1e-12) |
| G_defect_parallel_fraction | G_closure/G_defect_parallel_fraction | 0.5140711618 | 0.5140711618 | S1, S2 | 1.51e-15 | agree to rounding (rel <= 1e-12) |
| d84_bound_energy_ratio | G_closure/d84_bound_energy_ratio | 7.321858786 | 7.321858786 | S1, S2 | 1.21e-15 | agree to rounding (rel <= 1e-12) |
| R_trap | strength/R_trap | 0.7699534007 | 0.7699534007 | S1, S2 | 0.00e+00 | equal |
| lambda_max_S_inside_Rtrap | strength/lambda_max_S_inside_Rtrap | 5.385549393 | 5.385549393 | S1, S2 | 0.00e+00 | equal |
| B_u | strength/B_u | 19.46872788 | 19.46872788 | S1, S2 | 0.00e+00 | equal |
| KU_ratio | strength/KU_ratio | 0.3274290007 | 0.3274290007 | S1, S2 | 0.00e+00 | equal |
| KOmega_L2_ratio | strength/KOmega_L2_ratio | 0.9444616278 | 0.9444616278 | S1, S2 | 0.00e+00 | equal |
| located_max_abs_Omega | critical/local_maxima/0/abs_Omega | 13.4819948 | 13.4819948 | S1, S2 | 0.00e+00 | equal |
| located_max_r | critical/local_maxima/0/r | 0.2644568963 | 0.2644568963 | S1, S2 | 0.00e+00 | equal |
| located_strain_ratio | critical/local_maxima/0/strain_ratio | 0.911421342 | 0.911421342 | S1, S2 | 0.00e+00 | equal |
| located_transport_ratio | critical/local_maxima/0/transport_ratio | 2.938590433e-10 | 2.938590433e-10 | S1, S2 | 0.00e+00 | equal |
| n_W_zeros | DERIVED/n_W_zeros | 3 | 3 | S1, S2 | 0.00e+00 | equal |
| min_W_eigvec_defect | DERIVED/min_W_eigvec_defect | 0.3729240969 | 0.3729240969 | S1, S2 | 0.00e+00 | equal |
| Z | spec_training/global_integrals/Z | 22.39819774 | 22.39819774 | S1, S2 | 0.00e+00 | equal |
| Sigma_Z | spec_training/global_integrals/Sigma_Z | 0.3842113329 | 0.3842113329 | S1, S2 | 0.00e+00 | equal |
| F_norm2 | spec_training/global_integrals/F_norm2 | 1 | 1 | S1, S2 | 0.00e+00 | equal |

## Numeric S1 keys NOT compared (94; R5), plus two_family.structure (unmapped): E_F_max, E_F_weighted_deficit, E_F_weighted_excess, E_ren, E_ren_change_2oct, E_ren_two_forms_rel_diff, E_swirl_max, G_identity_rel, Gamma0_max, H_abs, H_tot, H_tot_change_2oct, H_tot_over_abs, L, L_ext, Nk, Q_sw, S_max, a_eff, a_max_ball_half_centre, a_max_ball_half_upper, a_max_ball_quarter_centre, a_max_ball_quarter_upper, a_max_core, a_max_core_upper, c_l, core_alignment, core_ball_over_a_eff, core_doubling_change_max, core_nonaxi, cost_final, delta_G_core, delta_G_max, delta_G_shells, f_sw_tail, far_radii, gauge_defect, gauge_defect_optimizer, gauge_version, gauge_weight, iterations, jtj_blocks, lambda_max, lambda_n_octaves_negative, lm_rms_per_entry, max_U_start, max_abs_Omega, max_mom, n_z, negative_pairing_fraction, omega, pivot_defect, pointwise_along_U_share, r_at_E_F_max, r_at_lambda_max, r_peak_Omega, r_star, radial_lambda_share, relU_change_holdout, rel_defect_max, rel_defect_mean, rms0, rms_final, rms_mom, rng_seed, rotation_content_rel, seconds, sigma_Om_ball_half, sigma_u_ball_half, sigma_u_ball_quarter, sigma_u_max_core, source_rho_nl, source_rho_u, source_rho_u_half, source_sphere_rho_u, start, strain_at_max, swirl_identity_closure, tail_nonaxi, tau0_floored, tau0_raw, tau1_floored, tau1_raw, tau2_floored, tau2_raw, tau_F_R12, tau_F_R8, tau_F_selfcheck, taylor_consistency, top_k_fraction, top_l_fraction, v10_iterations, v10_last_tenth_rel_decrease, y_star; two_family.structure.
## VT output sections without a saved counterpart (new, unreviewed; not compared): training_grid, refined_grid, holdout, X5_vorticity, orbit_averages, orbit_checks_7_14, critical.
- The worker's CRITICAL stdout line of 2026-10-26T13:58:28Z (worker.log line 148) reads: located |Omega| max 13.4820 at r=0.264, strain ratio 0.9114 (exact 1), transport 2.9e-10; the located_* rows above compare the saved full-precision values.
- VT critical.local_maxima[0]: {"abs_Omega": 13.481994803980982, "r": 0.26445689630862346, "strain_ratio": 0.9114213419634161, "transport_ratio": 2.938590432504349e-10, "lambda_max_S": 1.1949819408241238}
- VT holdout random points: {"n_points": 4003, "rms_scaled_R_Omega": 2.7789715345030404, "max_scaled_R_Omega": 40.72263534476823, "rms_scaled_Omega": 10.613187350352845}
- Not computed by the validation script and therefore not compared: V10 (an optimizer-history quantity), the LM cost, the SPECTRUM, RADIAL LAMBDA and ORIGIN battery lines, the core-set a_max variants, E_ren / H_tot balances (BALANCE line), FAR RATE, RAY by |m|.
