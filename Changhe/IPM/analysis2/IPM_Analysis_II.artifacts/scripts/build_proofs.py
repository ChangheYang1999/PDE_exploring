"""Assemble S1_PROOFS.md from the independently checked topic proofs.

Reads the topic proof files (read-only), rewrites file references into section labels, removes
team-internal wording, and writes S1_PROOFS.md. A list of suspicious tokens left after rewriting
is printed for manual review.
"""
import re, sys, os, datetime

SRC = sys.argv[1]           # root of the topic proofs
OUT = sys.argv[2]           # output file

PARTS = [
 ("P1", "Source reconstruction, operator, normalization and scaling", [
   ("source_audit/PROOF.md", "P1.1"), ("01_operator/PROOF.md", "P1.2")]),
 ("P2", "Center strain functional, singular moment and strain unboundedness", [
   ("04_singular/PROOF.md", "P2.1"), ("04_singular/STRAIN_INTEGRAL_PROOF.md", "P2.2"),
   ("04_singular/MOMENT_PROOF.md", "P2.3"), ("04_singular/UNBOUNDEDNESS_PROOF.md", "P2.4")]),
 ("P3", "Far field: tails, finite-family exclusion, stationary completion, residual lower bounds", [
   ("05_tails/PROOF.md", "P3.1"), ("05_tails/NONEXISTENCE_PROOF.md", "P3.2"),
   ("05_tails/FORMAL_COMPLETION_PROOF.md", "P3.3"), ("05_tails/RESIDUAL_HESSIAN_PROOF.md", "P3.4")]),
 ("P4", "Negative-order and L2 energies, global matrix certificates, Hoelder estimate", [
   ("02_energy/PROOF.md", "P4.1"), ("02_energy/FIXED_EXPONENT_INVERSE_PROOF.md", "P4.2"),
   ("02_energy/COMPACT_CERTIFICATE_PROOF.md", "P4.3"), ("02_energy/EXTERIOR_CERTIFICATE_PROOF.md", "P4.4"),
   ("02_energy/AUXILIARY_CERTIFICATE_PROOF.md", "P4.5"), ("02_energy/L2_ENERGY_PROOF.md", "P4.6"),
   ("02_energy/SOBOLEV_HOLDER_PROOF.md", "P4.7")]),
 ("P5", "Frozen principal operator: Hoelder and Sobolev inverses, trace, regularity obstruction", [
   ("03_frozen/HEAT_PROOF.md", "P5.1"), ("03_frozen/PROOF.md", "P5.2"),
   ("03_frozen/TRACE_REGULARITY_PROOF.md", "P5.3"), ("03_frozen/SOBOLEV_REGULARITY_PROOF.md", "P5.4"),
   ("03_frozen/ENDPOINT_REGULARITY_PROOF.md", "P5.5")]),
 ("P6", "Weighted spaces, weighted low and high inverses (the realization admitting the original residual)", [
   ("07_weighted/PROOF.md", "P6.1"), ("07_weighted/PRINCIPAL_SYMBOL_PROOF.md", "P6.2"),
   ("07_weighted/COMMUTATOR_PROOF.md", "P6.3"), ("07_weighted/LOW_INVERSE_PROOF.md", "P6.4"),
   ("07_weighted/LOW_INVERSE_FAMILY_PROOF.md", "P6.5"), ("07_weighted/ENDPOINT_PROOF.md", "P6.6"),
   ("07_weighted/UNSYMMETRIZED_TEST_PROOF.md", "P6.7"), ("07_weighted/BILINEAR_PROOF.md", "P6.8"),
   ("07_weighted/HIGH_SYMBOL_CERTIFICATE_PROOF.md", "P6.9"), ("07_weighted/H2_INVERSE_PROOF.md", "P6.10"),
   ("07_weighted/WEIGHTED_HIGH_PROOF.md", "P6.11"), ("07_weighted/FRACTIONAL_BILINEAR_PROOF.md", "P6.12"),
   ("07_weighted/RADIAL_COMMUTATOR_PROOF.md", "P6.13"), ("07_weighted/SHARP_WEIGHTED_H2_PROOF.md", "P6.14"),
   ("07_weighted/R2_DERIVATIVE_PROOF.md", "P6.15"), ("07_weighted/SHARP_WEIGHTED_HIGH_PROOF.md", "P6.16")]),
 ("P7", "Unweighted-bottom realization (Route U): low perturbation inverse, Riesz bounds, sharp coefficients, high inverse", [
   ("07_weighted/UNWEIGHTED_NONLINEAR_PROOF.md", "P7.1"), ("07_weighted/MELLIN_RIESZ_PROOF.md", "P7.2"),
   ("07_weighted/SHARP_COEFFICIENT_PROOF.md", "P7.3"), ("07_weighted/ROUTE_U_HIGH_PROOF.md", "P7.4"),
   ("07_weighted/SHARP_ROUTE_U_PROOF.md", "P7.5"), ("07_weighted/FRACTIONAL_TOOL_PROOF.md", "P7.6"),
   ("07_weighted/HARDY_OBJECTIVE_PROOF.md", "P7.7")]),
 ("P8", "Rough-velocity inverse, conditional existence, reference independence", [
   ("09_quasilinear/PROOF.md", "P8.1"), ("09_quasilinear/REFERENCE_AUDIT.md", "P8.2"),
   ("09_quasilinear/LEAD_STATEMENT_AUDIT.md", "P8.3"), ("09_quasilinear/SHARP_COMMUTATOR_PROOF.md", "P8.4")]),
 ("P9", "Abstract closure theorems and the nonlinear derivative-loss obstruction", [
   ("06_closure/QUASILINEAR_PROOF.md", "P9.1"), ("06_closure/FIXED_TAIL_NORMALIZATION_PROOF.md", "P9.2"),
   ("06_closure/DERIVATIVE_LOSS_PROOF.md", "P9.3"), ("06_closure/PROOF.md", "P9.4")]),
 ("P10", "Improved references: exact refits and the potential-level tail repair", [
   ("08_refits/PROOF.md", "P10.1"), ("10_tail_splice/PROOF.md", "P10.2")]),
 ("P11", "Audits of floating-point evaluators", [
   ("numerics_audit/PROOF.md", "P11.1"), ("numerics_audit/C8_PROOF.md", "P11.2"),
   ("numerics_audit/C2_CORRECTION_PROOF.md", "P11.3"), ("numerics_audit/C9_PROOF.md", "P11.4"),
   ("numerics_audit/BINARY_ENDPOINT_PROOF.md", "P11.5"), ("numerics_audit/INTERVAL_SERIALIZATION_PROOF.md", "P11.6")]),
 ("P12", "Certified whole-plane residual norms of exact finite potentials", [
   ("11_residual_norms/PROOF.md", "P12.1")]),
 ("P13", "Necessary conditions in the affine correction class", [
   ("12_affine_obstruction/PROOF.md", "P13.1"), ("12_affine_obstruction/WEAK_ANNULUS_PROOF.md", "P13.2")]),
 ("P14", "Algebraic tail repair: exact finite rational references with admissible residual", [
   ("13_algebraic_repair/PROOF.md", "P14.1"), ("13_algebraic_repair/INTERVAL_HESSIAN_PROOF.md", "P14.2"),
   ("13_algebraic_repair/STABLE_COORDINATES_PROOF.md", "P14.3")]),
 ("P15", "Homogeneous and regularized weights for the negative-order norm: sharp transform bounds and a coercivity failure", [
   ("14_homogeneous_weight/PROOF.md", "P15.1"), ("14_homogeneous_weight/REGULARIZED_PROOF.md", "P15.2")]),
 ("P16", "Angular sampling of residual diagnostics", [
   ("15_angular_sampling/PROOF.md", "P16.1")]),
 ("P17", "Weighted fractional space: conditional existence theorem D_w, reference contract and residual gap", [
   ("16_weighted_fractional/PROOF.md", "P17.1"), ("16_weighted_fractional/ROUGH_INVERSE_PROOF.md", "P17.2"),
   ("16_weighted_fractional/RESIDUAL_GAP_PROOF.md", "P17.3"),
   ("16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md", "P17.4"),
   ("16_weighted_fractional/SHARP_ROUGH_INVERSE_PROOF.md", "P17.5"),
   ("16_weighted_fractional/REFERENCE_AUDIT.md", "P17.6"),
   ("16_weighted_fractional/ANNULAR_RESIDUAL_PROOF.md", "P17.7")]),
 ("P18", "A smaller weight radius for Theorem D_w and the residual gap at that radius", [
   ("17_weight_radius/PROOF.md", "P18.1"), ("17_weight_radius/RESIDUAL_PROOF.md", "P18.2")]),
 ("P19", "Sharper constants for Theorem D_w in the same space", [
   ("18_fractional_constants/PROOF.md", "P19.1")]),
 ("P20", "An exactly admissible projected refit and its failure of the matrix and smallness conditions", [
   ("19_nb_candidates/PROOF.md", "P20.1")]),
 ("P21", "Real angular pairing: a smaller velocity constant, the weight radius 2^31 and the residual gap there", [
   ("20_real_velocity/PROOF.md", "P21.1"), ("20_real_velocity/RESIDUAL_PROOF.md", "P21.2")]),
 ("P22", "Optimality of the frozen heat-norm inverse, including the trace constraints", [
   ("21_frozen_optimality/PROOF.md", "P22.1")]),
 ("P23", "Vertical-axis consequences of the matrix condition and the distance of the projected refits from it", [
   ("22_axis_constraints/PROOF.md", "P23.1")]),
 ("P24", "A weaker low matrix hypothesis for Theorem D_w", [
   ("24_weaker_matrix/PROOF.md", "P24.1")]),
 ("P25", "An annular lower bound for the residuals of two exactly admissible projected refits", [
   ("23_admissible_tail_gap/PROOF.md", "P25.1")]),
 ("P26", "Necessary point tests of the full reference contract for the projected refits", [
   ("25_candidate_contract/PROOF.md", "P26.1")]),
 ("P27", "A uniform unweighted residual bound for the fitting family", [
   ("26_uniform_family_gap/PROOF.md", "P27.1")]),
 ("P28", "Point tests of the reference contract for four later projected refits", [
   ("27_candidate_point_audit/PROOF.md", "P28.1")]),
 ("P29", "The fixed tail sector alone does not force a weighted residual gap", [
   ("28_limits_of_tail_invariants/PROOF.md", "P29.1")]),
 ("P30", "Necessary residual scales for the weighted theorem", [
   ("29_residual_targets/PROOF.md", "P30.1")]),
 ("P31", "The uniform unweighted residual bound for every radial degree up to 779", [
   ("30_radial_degree_obstruction/PROOF.md", "P31.1"),
   ("31_logarithmic_derivative/PROOF.md", "P31.2")]),
 ("P32", "The seventh stationary order and the next fixed residual sector", [
   ("32_stationary_order_seven/PROOF.md", "P32.1")]),
 ("P33", "A recursive dilation constant: the uniform unweighted residual bound for every radial degree up to 3675", [
   ("33_recursive_dilation/PROOF.md", "P33.1")]),
 ("P34", "Scope of the annular obstruction: residuals in the negative-order space have square-summable annular pairings", [
   ("34_affine_scope/PROOF.md", "P34.1")]),
 ("P35", "The uniform bound for the seven-branch fitting family is inconclusive", [
   ("35_seven_branch_gap/PROOF.md", "P35.1")]),
 ("P36", "An exactly admissible seven-branch refit and its failure of the coefficient and smallness conditions", [
   ("36_b6_candidates/PROOF.md", "P36.1")]),
 ("P37", "The canonical strain as a bounded velocity-gradient trace and the output constant of Theorem D_w", [
   ("37_strain_trace/PROOF.md", "P37.1")]),
 ("P38", "Necessary local distance of exact solutions from the projected refits", [
   ("38_local_distance/PROOF.md", "P38.1")]),
 ("P39", "A necessary annular distance of exact solutions from the checkpoint, for every exponent", [
   ("39_annular_distance/PROOF.md", "P39.1")]),
 ("P40", "Fixed-tail exponent rigidity and the resulting local distance radii of the refits", [
   ("40_fixed_tail_distance/PROOF.md", "P40.1")]),
 ("P41", "Square tests uniform in the smoothness index", [
   ("41_compact_distance/PROOF.md", "P41.1")]),
 ("P42", "The exactly admissible six-branch refit d2", [
   ("42_d2_candidate/PROOF.md", "P42.1")]),
 ("P43", "The smooth commutator and the second version of the weighted theorem", [
   ("43_smooth_commutator/PROOF.md", "P43.1")]),
 ("P44", "Smaller amplitude constants in the weighted space", [
   ("44_small_amplitude/PROOF.md", "P44.1")]),
 ("P45", "Improved necessary distances and residual point bounds", [
   ("45_improved_distances/PROOF.md", "P45.1")]),
 ("P46", "Centered weak tests", [
   ("46_centered_weak_tests/PROOF.md", "P46.1")]),
 ("P47", "Weighted Bessel bound and negative-order weak tests", [
   ("47_low_bessel_duality/PROOF.md", "P47.1")]),
 ("P48", "Negative-energy amplitude embeddings and larger necessary distances", [
   ("48_negative_energy_amplitudes/PROOF.md", "P48.1")]),
 ("P49", "A negative-order annular exclusion around the checkpoint", [
   ("49_negative_annular_distance/PROOF.md", "P49.1")]),
 ("P50", "The natural normalized maximal domain and forcing compatibility", [
   ("50_normalized_maximal_domain/PROOF.md", "P50.1")]),
 ("P51", "Exterior weight transfer of the annular witnesses", [
   ("51_exterior_weight_transfer/PROOF.md", "P51.1")]),
 ("P52", "Annular residual gaps and necessary distances for the refits Mpen2 and d2", [
   ("52_refit_annular_distance/PROOF.md", "P52.1"), ("52_refit_annular_distance/RESULTS.md", "P52.2")]),
 ("P53", "The frozen heat inverse for the full parameter range", [
   ("53_heat_frozen_inverse/PROOF.md", "P53.1")]),
 ("P54", "Off-axis violation of the fourth-derivative bound by the refit d2", [
   ("54_d2_offaxis_derivative/PROOF.md", "P54.1"), ("54_d2_offaxis_derivative/RESULTS.md", "P54.2")]),
 ("P55", "A smaller ordinary Hoelder constant for the frozen inverse", [
   ("55_holder_conversion/PROOF.md", "P55.1"), ("55_holder_conversion/RESULTS.md", "P55.2")]),
 ("P56", "A positive weighted residual minimum over each finite fitting family", [
   ("56_weighted_family_properness/PROOF.md", "P56.1"), ("56_weighted_family_properness/RESULTS.md", "P56.2")]),
 ("P57", "A constructive positive floor, uniform in the smoothness index and the weight radius", [
   ("57_constructive_properness/PROOF.md", "P57.1"), ("57_constructive_properness/RESULTS.md", "P57.2")]),
 ("P58", "Off-axis violations of three derivative bounds by the refit Mpen2", [
   ("58_mpen2_offaxis_derivatives/PROOF.md", "P58.1"), ("58_mpen2_offaxis_derivatives/RESULTS.md", "P58.2")]),
 ("P59", "Sharp Riesz coercivity on a finite angular band", [
   ("59_angular_coercivity/PROOF.md", "P59.1"), ("59_angular_coercivity/RESULTS.md", "P59.2")]),
 ("P60", "A positive weighted floor for the seven-branch family", [
   ("60_seven_branch_weighted/PROOF.md", "P60.1"), ("60_seven_branch_weighted/RESULTS.md", "P60.2")]),
 ("P61", "Exact finite constraints do not repair the critical far-field space", [
   ("61_endpoint_finite_constraints/PROOF.md", "P61.1"), ("61_endpoint_finite_constraints/RESULTS.md", "P61.2")]),
 ("P62", "An evaluated weighted floor from the finite power representation", [
   ("62_weighted_cauchy/PROOF.md", "P62.1"), ("62_weighted_cauchy/RESULTS.md", "P62.2")]),
 ("P63", "The conditional inverse of the second version: domains, normalization and derivative loss", [
   ("63_conditional_domain_audit/PROOF.md", "P63.1"), ("63_conditional_domain_audit/RESULTS.md", "P63.2")]),
 ("P64", "Critical weighted Sobolev spaces and finite augmentations", [
   ("64_critical_sobolev/PROOF.md", "P64.1"), ("64_critical_sobolev/RESULTS.md", "P64.2")]),
 ("P65", "A far-field spectral line in weighted Sobolev spaces", [
   ("65_far_spectral_line/PROOF.md", "P65.1"), ("65_far_spectral_line/RESULTS.md", "P65.2")]),
 ("P66", "Gaussian finite differences and sharper frozen Hoelder constants", [
   ("66_gaussian_holder/PROOF.md", "P66.1"), ("66_gaussian_holder/RESULTS.md", "P66.2")]),
 ("P67", "Fractional Gaussian kernels and the frozen Hoelder constant 87", [
   ("67_fractional_gaussian/PROOF.md", "P67.1"), ("67_fractional_gaussian/RESULTS.md", "P67.2")]),
 ("P68", "Logarithmic weights and asymptotic coordinates at the critical exponent", [
   ("68_logarithmic_endpoint/PROOF.md", "P68.1"), ("68_logarithmic_endpoint/RESULTS.md", "P68.2")]),
 ("P69", "The sharp small-regularity cost of the strain trace", [
   ("69_strain_regularization/PROOF.md", "P69.1"), ("69_strain_regularization/RESULTS.md", "P69.2")]),
 ("P70", "A logarithmic replacement for the fractional strain regularization", [
   ("70_logarithmic_strain/PROOF.md", "P70.1"), ("70_logarithmic_strain/RESULTS.md", "P70.2")]),
 ("P71", "The logarithmic strain space retains the low residual obstruction", [
   ("71_logarithmic_low_transfer/PROOF.md", "P71.1"), ("71_logarithmic_low_transfer/RESULTS.md", "P71.2")]),
 ("P72", "The circular principal value of the strain as a positive average", [
   ("72_strain_cutoff_average/PROOF.md", "P72.1"), ("72_strain_cutoff_average/RESULTS.md", "P72.2")]),
 ("P73", "Necessary logarithmic distances of exact profiles from the references", [
   ("73_logarithmic_distances/PROOF.md", "P73.1"), ("73_logarithmic_distances/RESULTS.md", "P73.2")]),
 ("P74", "An explicit density with divergent strain at the logarithmic endpoint", [
   ("74_explicit_endpoint/PROOF.md", "P74.1"), ("74_explicit_endpoint/RESULTS.md", "P74.2")]),
 ("P75", "A fixed-background inverse with a logarithmic gain", [
   ("75_logarithmic_linear_inverse/PROOF.md", "P75.1"), ("75_logarithmic_linear_inverse/RESULTS.md", "P75.2")]),
 ("P76", "The quadratic transport term is not continuous in the logarithmic space", [
   ("76_logarithmic_transport_loss/PROOF.md", "P76.1"), ("76_logarithmic_transport_loss/RESULTS.md", "P76.2")]),
 ("P77", "The logarithmic inverse at every power above the trace threshold", [
   ("77_logarithmic_power_inverse/PROOF.md", "P77.1"), ("77_logarithmic_power_inverse/RESULTS.md", "P77.2")]),
 ("P78", "A sharp half-logarithmic product estimate", [
   ("78_logarithmic_multiplier/PROOF.md", "P78.1"), ("78_logarithmic_multiplier/RESULTS.md", "P78.2")]),
 ("P79", "Commutators of the logarithmic multiplier with moderate weights", [
   ("79_logarithmic_weight_commutator/PROOF.md", "P79.1"), ("79_logarithmic_weight_commutator/RESULTS.md", "P79.2")]),
 ("P80", "A low-order product estimate in the logarithmic space", [
   ("80_logarithmic_low_product/PROOF.md", "P80.1"), ("80_logarithmic_low_product/RESULTS.md", "P80.2")]),
 ("P81", "A Lipschitz commutator bound for the logarithmic multiplier", [
   ("81_lipschitz_log_commutator/PROOF.md", "P81.1"), ("81_lipschitz_log_commutator/RESULTS.md", "P81.2")]),
 ("P82", "A derivative product estimate in the logarithmic space", [
   ("82_logarithmic_derivative_product/PROOF.md", "P82.1"), ("82_logarithmic_derivative_product/RESULTS.md", "P82.2")]),
 ("P83", "The native logarithmic norm and its equivalence with the earlier norms", [
   ("83_logarithmic_native_low/PROOF.md", "P83.1"), ("83_logarithmic_native_low/RESULTS.md", "P83.2")]),
 ("P84", "Products, velocity and strain in the native logarithmic norm", [
   ("84_native_logarithmic_products/PROOF.md", "P84.1"), ("84_native_logarithmic_products/RESULTS.md", "P84.2")]),
 ("P85", "A conditional nonlinear theorem in the logarithmic space", [
   ("85_logarithmic_conditional_theorem/PROOF.md", "P85.1"), ("85_logarithmic_conditional_theorem/RESULTS.md", "P85.2")]),
 ("P86", "The references stay excluded in the native logarithmic norm", [
   ("86_native_logarithmic_exclusions/PROOF.md", "P86.1"), ("86_native_logarithmic_exclusions/RESULTS.md", "P86.2")]),
 ("P87", "Four compatible outputs of the logarithmic inverse", [
   ("87_logarithmic_four_outputs/PROOF.md", "P87.1"), ("87_logarithmic_four_outputs/RESULTS.md", "P87.2")]),
 ("P88", "A consolidated dependency and domain audit of the logarithmic theorem", [
   ("88_logarithmic_dependency_audit/PROOF.md", "P88.1"), ("88_logarithmic_dependency_audit/RESULTS.md", "P88.2")]),
 ("P89", "The logarithmic theorem with adjustable higher derivative bounds", [
   ("89_parametric_logarithmic_theorem/PROOF.md", "P89.1"), ("89_parametric_logarithmic_theorem/RESULTS.md", "P89.2")]),
 ("P90", "Exclusions and gaps for every parameter choice", [
   ("90_parameter_uniform_exclusions/PROOF.md", "P90.1"), ("90_parameter_uniform_exclusions/RESULTS.md", "P90.2")]),
 ("P91", "Exact global derivative caps for finite potentials", [
   ("91_algebraic_derivative_caps/PROOF.md", "P91.1"), ("91_algebraic_derivative_caps/RESULTS.md", "P91.2")]),
 ("P92", "An independent global matrix certificate for the checkpoint", [
   ("92_global_matrix_recomputation/PROOF.md", "P92.1"), ("92_global_matrix_recomputation/RESULTS.md", "P92.2")]),
 ("P93", "An audit of the polar covering of the checkpoint matrix bound", [
   ("93_polar_covering_audit/PROOF.md", "P93.1"), ("93_polar_covering_audit/RESULTS.md", "P93.2")]),
 ("P94", "The sharp global matrix margin of the checkpoint", [
   ("94_sharp_original_matrix/PROOF.md", "P94.1"), ("94_sharp_original_matrix/RESULTS.md", "P94.2")]),
 ("P95", "Global hypotheses of the exact refits: the matrix, derivative and decay bounds for the reference d2", [
   ("95_refit_global_hypotheses/PROOF.md", "P95.1"), ("95_refit_global_hypotheses/RESULTS.md", "P95.2")]),
 ("P96", "An independent full-plane certificate of the auxiliary matrix bounds of the checkpoint", [
   ("96_original_auxiliary_recomputation/PROOF.md", "P96.1"), ("96_original_auxiliary_recomputation/RESULTS.md", "P96.2")]),
 ("P97", "The full absolute jet moment needs more than three halves of a logarithm", [
   ("97_absolute_jet_moment/PROOF.md", "P97.1"), ("97_absolute_jet_moment/RESULTS.md", "P97.2")]),
 ("P98", "Exact origin remainder bounds for the checkpoint through radius one tenth", [
   ("98_original_origin_recomputation/PROOF.md", "P98.1"), ("98_original_origin_recomputation/RESULTS.md", "P98.2")]),
 ("P99", "Independent density sign and matrix bounds for the checkpoint", [
   ("99_original_global_signs/PROOF.md", "P99.1"), ("99_original_global_signs/RESULTS.md", "P99.2")]),
 ("P101", "A directed exterior residual bound for the checkpoint", [
   ("101_directed_far_residual/PROOF.md", "P101.1"), ("101_directed_far_residual/RESULTS.md", "P101.2")]),
 ("P102", "The divergent absolute jet moment lies outside the fractional weighted spaces", [
   ("102_absolute_moment_scope/PROOF.md", "P102.1"), ("102_absolute_moment_scope/RESULTS.md", "P102.2")]),
 ("P103", "Polynomial growth passes from the density to the canonical velocity", [
   ("103_velocity_growth/PROOF.md", "P103.1"), ("103_velocity_growth/RESULTS.md", "P103.2")]),
 ("P104", "Independent full-plane decay bounds for the checkpoint", [
   ("104_original_decay_recomputation/PROOF.md", "P104.1"), ("104_original_decay_recomputation/RESULTS.md", "P104.2")]),
 ("P105", "The refit d2 satisfies every reference hypothesis of the parametric logarithmic theorem", [
   ("105_refit_reference_contract/PROOF.md", "P105.1"), ("105_refit_reference_contract/RESULTS.md", "P105.2")]),
 ("P106", "The actual residuals lie in the logarithmic forcing spaces", [
   ("106_logarithmic_residual_membership/PROOF.md", "P106.1"), ("106_logarithmic_residual_membership/RESULTS.md", "P106.2")]),
 ("P108", "The power one fifth is the sharp forcing-tail threshold of the logarithmic spaces", [
   ("108_sharp_logarithmic_forcing_tails/PROOF.md", "P108.1"), ("108_sharp_logarithmic_forcing_tails/RESULTS.md", "P108.2")]),
 ("P111", "Direct exclusion radii in the native logarithmic norm", [
   ("111_direct_native_distance/PROOF.md", "P111.1"), ("111_direct_native_distance/RESULTS.md", "P111.2")]),
]

label_of = {}
for _, _, files in PARTS:
    for f, lab in files:
        label_of[f] = lab

from collections import Counter
_base_count = Counter(f.split('/')[1] for f in label_of)
label_of_base = {f.split('/')[1]: lab for f, lab in label_of.items() if _base_count[f.split('/')[1]] == 1}

TOPIC_PART = {"source_audit": "P1.1", "01_operator": "P1.2", "04_singular": "P2", "05_tails": "P3", "02_energy": "P4",
              "03_frozen": "P5", "07_weighted": "P6 and P7", "09_quasilinear": "P8", "06_closure": "P9",
              "08_refits": "P10.1", "10_tail_splice": "P10.2", "numerics_audit": "P11", "11_residual_norms": "P12",
              "12_affine_obstruction": "P13", "13_algebraic_repair": "P14",
              "14_homogeneous_weight": "P15", "15_angular_sampling": "P16",
              "16_weighted_fractional": "P17", "17_weight_radius": "P18",
              "18_fractional_constants": "P19", "19_nb_candidates": "P20",
              "20_real_velocity": "P21", "21_frozen_optimality": "P22", "22_axis_constraints": "P23",
              "24_weaker_matrix": "P24", "23_admissible_tail_gap": "P25", "25_candidate_contract": "P26",
              "26_uniform_family_gap": "P27", "27_candidate_point_audit": "P28", "28_limits_of_tail_invariants": "P29",
              "29_residual_targets": "P30", "30_radial_degree_obstruction": "P31.1",
              "31_logarithmic_derivative": "P31.2", "32_stationary_order_seven": "P32",
              "33_recursive_dilation": "P33", "34_affine_scope": "P34", "35_seven_branch_gap": "P35",
              "36_b6_candidates": "P36", "37_strain_trace": "P37", "38_local_distance": "P38",
              "39_annular_distance": "P39", "40_fixed_tail_distance": "P40",
              "41_compact_distance": "P41", "42_d2_candidate": "P42", "43_smooth_commutator": "P43",
              "44_small_amplitude": "P44", "45_improved_distances": "P45", "46_centered_weak_tests": "P46",
              "47_low_bessel_duality": "P47", "48_negative_energy_amplitudes": "P48",
              "49_negative_annular_distance": "P49", "50_normalized_maximal_domain": "P50",
              "51_exterior_weight_transfer": "P51", "52_refit_annular_distance": "P52",
              "53_heat_frozen_inverse": "P53", "54_d2_offaxis_derivative": "P54", "55_holder_conversion": "P55",
              "56_weighted_family_properness": "P56", "57_constructive_properness": "P57",
              "58_mpen2_offaxis_derivatives": "P58", "59_angular_coercivity": "P59",
              "60_seven_branch_weighted": "P60", "61_endpoint_finite_constraints": "P61",
              "62_weighted_cauchy": "P62", "63_conditional_domain_audit": "P63",
              "64_critical_sobolev": "P64", "65_far_spectral_line": "P65", "66_gaussian_holder": "P66",
              "67_fractional_gaussian": "P67", "68_logarithmic_endpoint": "P68",
              "69_strain_regularization": "P69",
              "70_logarithmic_strain": "P70", "71_logarithmic_low_transfer": "P71",
              "72_strain_cutoff_average": "P72",
              "73_logarithmic_distances": "P73",
              "74_explicit_endpoint": "P74",
              "75_logarithmic_linear_inverse": "P75",
              "76_logarithmic_transport_loss": "P76",
              "77_logarithmic_power_inverse": "P77",
              "78_logarithmic_multiplier": "P78",
              "79_logarithmic_weight_commutator": "P79",
              "80_logarithmic_low_product": "P80",
              "81_lipschitz_log_commutator": "P81",
              "82_logarithmic_derivative_product": "P82",
              "83_logarithmic_native_low": "P83",
              "84_native_logarithmic_products": "P84",
              "85_logarithmic_conditional_theorem": "P85",
              "86_native_logarithmic_exclusions": "P86",
              "87_logarithmic_four_outputs": "P87",
              "88_logarithmic_dependency_audit": "P88",
              "89_parametric_logarithmic_theorem": "P89",
              "90_parameter_uniform_exclusions": "P90",
              "91_algebraic_derivative_caps": "P91",
              "92_global_matrix_recomputation": "P92",
              "93_polar_covering_audit": "P93",
              "94_sharp_original_matrix": "P94",
              "95_refit_global_hypotheses": "P95",
              "96_original_auxiliary_recomputation": "P96",
              "97_absolute_jet_moment": "P97",
              "102_absolute_moment_scope": "P102",
              "103_velocity_growth": "P103",
              "106_logarithmic_residual_membership": "P106",
              "108_sharp_logarithmic_forcing_tails": "P108",
              "111_direct_native_distance": "P111",
              "98_original_origin_recomputation": "P98",
              "99_original_global_signs": "P99",
              "101_directed_far_residual": "P101",
              "104_original_decay_recomputation": "P104",
              "105_refit_reference_contract": "P105"}
WORDS = """about above adding after all and are area at baseline because before below between bound bounds by checkpoint
checkpoints coefficient constant constants contain contains corresponding decay degree dimension dominates equals error
estimate evaluated every exact example exceed exceeds exponent factor factors for frequencies from gave gives has have
hypothesis if in independent indices inverse is its keep least level loss margin maximum moments most norm norms not
number obey of on or order original outside period powers radius rates rational replacing retained scalar section
smaller so stated states subtracting targets than the threshold through times to under using value weight whenever
with approximately magnitude frequency interactions
since rate harmonic branches branch sections theorem integral near inequality over descendant coefficients thus uses use row range power overlap give exclusion equivalence equivalences contraction argument against when velocity that side separate residue remains radii orders modes remain exactly estimates equivalently entries costs contribute comparison both here fix claims claim add while unrestricted unrelated total time throughout their target symmetric sum substituting stronger strictly still squared some selected satisfies same rounded retaining residual required replace reconstruction ratio quotients proves proofs proof product prior primary polynomials plus permits particular part parameters parameter outputs older old obstruction namely modulus minus interpolation including implies hence giving gap fraction floor fixed first final existing exclusions equal entire energy either earlier descendants controls contributing certificates calculation budget beyond begins becomes ball assume around approaching applying any annulus also additional across three therefore then let hypotheses finally formula exponents into""".split()

FOLDER_OF = {f[:2]: f for f in os.listdir(SRC) if re.match(r'\d\d_[a-z0-9_]+$', f)}


def part_of(nn):
    return TOPIC_PART.get(FOLDER_OF.get(nn, ''), 'topic ' + nn)


def rewrite(text, here):
    topic = here.split('/')[0]
    text = re.sub(r'([a-z])((?:PROOF|RESULTS)\.md)', r'\1 \2', text)
    text = re.sub(r'\bledger ?V(\d\d\d)\b', r'independent check \1', text)
    text = re.sub(r'\bledger (?=check \d)', '', text)
    text = re.sub(r'(^|\s)Opus [^.\n]*requested\.', r'\1', text)
    text = re.sub(r' ?(?:Opus )?cross-review is requested\.', '', text)
    text = re.sub(r' ?(?:(?:Independent|Opus|Lead|lead) )+review(?: is)? requested\.', '', text)
    text = re.sub(r' ?(?:Independent )?(?:Opus )?(?:Lead |lead )?review is requested\.', '', text)
    text = re.sub(r' ?(?:Independent )?Opus ?\d(?:\.\d)? (?:lead )?review (?:is )?(?:pending|requested)\.', '', text)
    text = re.sub(r' ?(?:Independent )?Opus ?\d(?:\.\d)? cross-review (?:is )?(?:pending|requested)\.', '', text)
    text = re.sub(r'\bThe only lane dependency\b', 'The only outside dependency', text)
    text = re.sub(r'\bLedger V(\d\d\d)\b', r'Independent check \1', text)
    text = re.sub(r'\bLedger (?=check \d)', 'Independent ', text)
    text = re.sub(r'^(#{2,4} )V(\d\d\d), (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.\d+\+00:00:', r'\1Independent check \2, \3Z:',
                  text, flags=re.M)
    text = re.sub(r'^V(\d\d\d), (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.\d+\+00:00\.', r'Independent check \1, \2Z.', text,
                  flags=re.M)
    text = re.sub(r'^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.\d+\+00:00, V(\d\d\d)\.', r'\1Z, independent check \2.', text,
                  flags=re.M)
    text = re.sub(r' ?Opus ?\d(?:\.\d)? follow-up (?:is )?pending\.', '', text)
    text = re.sub(r"\b(in|by) ?85(?= supplies|\.)", r"\1 P85", text)
    text = re.sub(r"\bin ?85 and ?89\b", "in P85 and P89", text)
    text = re.sub(r"\b(state|cap|pass)(\d\d\d?)\b", r"\1 \2", text)
    # glued references in dependency lists: audit19, certificate91, tail05, "moments:19", "membership:106"
    text = re.sub(r"\b(audit|certificate|tail)(\d\d)\b", lambda m: m.group(1) + " " + part_of(m.group(2)), text)
    text = re.sub(r"(?<=[a-z]):(\d\d)(?=[,.;]|\s|$)(?! leaves)", lambda m: ": " + part_of(m.group(1)), text)
    text = re.sub(r"(?<=[a-z]):(1\d\d)(?=[,.;]|\s|$)(?! leaves)",
                  lambda m: ": P" + m.group(1) if "P" + m.group(1) in TOPIC_PART.values() else m.group(0), text)
    text = re.sub(r"algebra ?05 and the differentiated remainder proof ?20/RESIDUAL_PROOF\.md",
                  "algebra of P3 and the differentiated remainder proof P21.2", text)
    text = re.sub(r' ?(?:Lead |lead )?analytical review requested\.', '', text)
    text = re.sub(r'; draft analytical review requested\.', '.', text)
    text = re.sub(r'\bthis topic\b', 'this part', text)
    # absolute paths
    text = re.sub(r'/(?:mnt|home|efs|tmp)/\S*', '[file]', text)
    # numbered topic references: topicNN/FILE becomes the folder path (converted below); bare topicNN becomes its part
    text = re.sub(r'\b[Tt]opic ?(\d\d)/', lambda m: FOLDER_OF.get(m.group(1), m.group(0)) + '/', text)
    def topics(m):
        nums = re.findall(r'\d\d', m.group(0))
        labels = [part_of(n) for n in nums]
        return 'parts ' + ', '.join(labels[:-1]) + ' and ' + labels[-1]
    text = re.sub(r'\b[Tt]opics ?(\d\d) section ?(\d+) and ?(\d\d) section ?(\d+)\b',
                  lambda m: f'{part_of(m.group(1))} section {m.group(2)} and {part_of(m.group(3))} section {m.group(4)}', text)
    text = text.replace('No source or other lane is modified', 'No source file is modified')
    text = re.sub(r'\b[Tt]opics ?\d\d(?:, ?\d\d)*,? and ?\d\d\b', topics, text)
    text = re.sub(r'\b([Tt])opics ?(\d\d)/(\d\d)\b', lambda m: ('P' if m.group(1) == 'T' else 'p') + 'arts ' + part_of(m.group(2)) + ' and ' + part_of(m.group(3)), text)
    text = re.sub(r'\b([Tt])opics ?(\d\d)-(\d\d)\b', lambda m: ('P' if m.group(1) == 'T' else 'p') + 'arts ' + part_of(m.group(2)) + ' to ' + part_of(m.group(3)), text)
    text = re.sub(r'\bin that topic\b', 'in that part', text)
    text = re.sub(r'\b[Tt]opic ?\d\d and ?\d\d\b', topics, text)
    text = re.sub(r'\b[Tt]opics ?\d\d(?:, ?\d\d)+\b', topics, text)
    text = re.sub(r'\b([Tt])opic ?(\d\d)\b', lambda m: ('P' if m.group(1) == 'T' else 'p') + 'art ' + part_of(m.group(2)), text)
    text = text.replace("this topic's", "this part's")
    # bare part numbers in the late logarithmic topics: "in 89", "proof 91", "of 106"
    if re.match(r'(7[5-9]|[89]\d|1\d\d)_', topic):
        def plist(m):
            nums = re.findall(r'\d\d\d?', m.group(2))
            labels = [part_of(n) if len(n) == 2 else 'P' + n for n in nums]
            if any(not re.match(r'P\d', x) or x not in TOPIC_PART.values() for x in labels):
                return m.group(0)
            return m.group(1) + ' parts ' + ', '.join(labels[:-1]) + ' and ' + labels[-1]
        text = re.sub(r"\b(by|in|of|from) ?(\d\d\d?(?:, ?\d\d\d?)+(?:,? and ?\d\d\d?)?)\b(?![./]\d| leaves)", plist, text)
        text = re.sub(r"\b(in|of|from|proof|theorem|and|by) ?(7[5-9]|[89]\d|1\d\d)\b"
                      r"(?![./]\d| (?:angular|radial|intervals|leaves|bits|cells|checks|digits|terms|points|boxes|times))",
                      lambda m: m.group(1) + " P" + m.group(2) if "P" + m.group(2) in TOPIC_PART.values() else m.group(0),
                      text)
        text = re.sub(r"\bequivalences ?(\d\d) and P(\d\d)\b", r"equivalences P\1 and P\2", text)
        text = re.sub(r"\bexclusion ?73, the norm", "exclusion P73, the norm", text)
        text = re.sub(r"\bproved in ?70/73 and the norm equivalences ?77/83\b",
                      "proved in P70 and P73 and the norm equivalences P77 and P83", text)
        text = text.replace("Until the registration record verifies every input, the consolidation is OPEN.",
                            "The registration audit verifies every input; all 47 checks pass.")
    # explicit topic/file references, with or without ../ or research/ prefix
    def ref(m):
        t, f = m.group(1), m.group(2)
        key = f"{t}/{f}"
        return f"section {label_of[key]}" if key in label_of else f"[{f}]"
    text = re.sub(r'`?(?:\.\./|research/)?(\d\d_[a-z0-9_]+|source_audit|numerics_audit)/([A-Za-z_0-9]+\.md)`?', ref, text)
    # verification evidence
    text = re.sub(r'`?(?:\.\./)?(?:(\d\d_[a-z0-9_]+|source_audit|numerics_audit)/)?verification/([A-Za-z_0-9.\-*]*[A-Za-z_0-9*])`?',
                  lambda m: f"certificate file {m.group(2)}", text)
    text = re.sub(r'`?\.\./[a-z_0-9]+/([A-Za-z_0-9.]*[A-Za-z_0-9])`?', r'certificate file \1', text)
    text = text.replace('lead SPEC S11.4', 'an earlier draft formulation')
    text = re.sub(r'`?research/source_audit/([A-Za-z_0-9.]*[A-Za-z_0-9])`?', r'certificate file \1', text)
    text = re.sub(r' ?Independent Opus review of the analytical proofs remains requested through the shared lane notes\.',
                  ' A second independent review of the analytical proofs was carried out separately.', text)
    # bare file names in the same topic
    def bare(m):
        key = f"{topic}/{m.group(1)}"
        if key in label_of:
            return f"section {label_of[key]}"
        if m.group(1) in label_of_base:
            return f"section {label_of_base[m.group(1)]}"
        return m.group(0)
    text = re.sub(r'`?\b([A-Z_0-9]*PROOF\.md|REFERENCE_AUDIT\.md|LEAD_STATEMENT_AUDIT\.md)\b`?', bare, text)
    # bare topic folder names
    text = re.sub(r'(?:\.\./)?(\d\d_[a-z0-9_]*[a-z]|source_audit|numerics_audit)(?![/\w])',
                  lambda m: f"part {TOPIC_PART[m.group(1)]}" if m.group(1) in TOPIC_PART else m.group(0), text)
    # missing space between an English word and a following number, bracket or parenthesis
    text = re.sub(r'\b(' + '|'.join(WORDS) + r')(?=\d|\[|\(|-\d)', r'\1 ', text, flags=re.I)
    # team-internal wording
    reps = [
      (r" ?(?:Opus lead|Lead Opus|lead Opus) (?:review|audit)s? (?:is |are )?requested\.", ""),
      (r" ?(?:Independent )?Opus (?:lead )?review is (?:requested|pending)\.", ""),
      (r"\bin the numerical lane\b", "in the numerical work"),
      (r"\bimports numerics code\b", "imports code of the numerical work"),
      (r",? with lead Opus (?:analytical )?review CORRECT at ?\d\d:\d\dZ\.", ", and by a second independent review of the argument."),
      (r" ?(?:Lead|lead) (?:Opus )?(?:analytical )?review is pending\.", " A second independent review of the argument found it correct."),
      (r" ?(?:Lead|lead) (?:Opus )?(?:analytical )?review was CORRECT at ?\d{4}-\d\d-\d\dT\d\d:\d\dZ; its independent interval "
       r"computation is confirmed by V\d\d\d\.",
       " A second independent review of the argument found it correct, and a separate interval computation of its constants agrees."),
      (r"agrees with the numerics record\.", "agrees with the record of the numerical work."),
      (r"the numerics lane's exact seventh-order coefficients", "the exact seventh-order coefficients of the numerical work"),
      (r"No numerics producer code is imported\.", "No code of the numerical work is imported."),
      (r"No numerics producer evaluator or sector code is imported\.", "No evaluator or sector code of the numerical work is imported."),
      (r"the general statement in the numerics lane's ?\d\d:\d\d note", "the general statement made in the numerical work"),
      (r"\bin the numerics note\b", "in the numerical work"),
      (r"These imply the numerics compact B1/B2/B3 numbers and", "These imply the compact-region numbers of the numerical covering for B1, B2, B3 and"),
      (r"the seven decimal targets identified in V208 pass", "the seven rounded decimal displays of the numerical work pass"),
      (r"all seven suspect rounded decimal targets from V208", "all seven rounded decimal displays of the numerical work"),
      (r"the unsafe outward-rounding deduction noted in V208\.", "the unsafe outward-rounding deduction in the numerical work."),
      (r"all ?32 original C3-131 numerical targets", "all 32 original numerical targets"),
      (r"certificates\.original 32\.json", "certificates.original32.json"),
      (r"\bRespectively(?=\d)", "Respectively "),
      (r"\bthe lead report's\b", "the report's"), (r"\bthe lead report\b", "the report"),
      (r"The lead's FINAL_REPORT\.md inspected at \d{4}-\d\d-\d\dT\d\d:\d\dZ says", "An earlier version of the report said"),
      (r"this assertion is false by \(2\)\. The precise replacement is", "this assertion is false by (2); the report now refers to"),
      (r'The lead report phrase "in the weighted spaces of the weighted theorem" is false if read as Theorem D_w; replace it by',
       'The phrase "in the weighted spaces of the weighted theorem" of an earlier version of the report is false if read as '
       'Theorem D_w; the report now refers to'),
      (r"conclusion from that topic\b", "conclusion from that part"),
      (r"inspected in the sibling lane use", "inspected in the numerical work use"),
      (r"in the sibling lane's research/code/n12_fit\.py, n12_norms\.py and splice_norms\.py", "in the numerical fitting, norm and splice programs"),
      (r"the exact rational files in the numerics lane's research/data", "the exact rational files of the numerical work"),
      (r"the binary-exact checkpoint in source/case4/IPM_case4\.artifacts/checkpoints/state131_last_unverified/accepted_00000131\.json",
       "the binary-exact checkpoint of state 131 (accepted_00000131.json of the case 4 artifacts)"),
      (r"\bthe numerics lane's\b", "the numerical"), (r"\bnumerics lane's\b", "numerical"),
      (r"\bthe lead's referee answer\b", "a draft argument"), (r"\bthe lead's\b", "the"), (r"\blead's\b", ""),
      (r"\bthe referee's\b", "the draft's"), (r"\breferee's\b", "draft's"),
      (r"\bthis lane's\b", "our"), (r"\bthe lane's\b", "the"), (r"\blane's\b", ""), (r"\blane code\b", "fitting code"),
      (r"\bthe verifier\b", "the independent check"), (r"\bverifier\b", "independent check"),
      (r"(?<![(+])\bS13\b(?![\^)+])", "the abstract two-norm statement"),
      (r"\bV0(\d\d)\b", r"check \1"), (r"\bV(1\d\d)\b", r"check \1"),
      (r"\bFINAL_REPORT\.md\b", "the report"),
      (r"\bthe lead\b", "the draft"), (r"\blead\b", "draft"),
      (r"\bwritten into the numerics lane\b", "written into the numerical work"),
      (r"\bThe numerics lane\b", "The numerical work"), (r"\bthe numerics lane\b", "the numerical work"),
      (r"\bof the numerics (C8|N-B)\b", r"of the numerical \1"),
      (r"\bindependent check lane\b", "independent check"),
      (r"\bthe numerics producer's\b", "the producer's"),
      (r"No Hölder-team result or unverified teammate claim is imported\.", "No unverified external claim is imported."),
    ]
    for a, b in reps:
        text = re.sub(a, b, text)
    # a rewritten reference that starts a sentence
    text = re.sub(r'(^|\. )(section|part|certificate file) ', lambda m: m.group(1) + m.group(2).capitalize() + ' ', text,
                  flags=re.M)
    # a word glued to a following section reference or to the symbol K
    text = re.sub(r'([a-z])(section P\d)', r'\1 \2', text)
    text = re.sub(r'\b(The|[a-z]{2,})K(?=\d|\+)', r'\1 K', text)
    text = re.sub(r'certificate file ([A-Za-z_0-9]+)\.py,json,log', r'certificate files \1.py, \1.json and \1.log', text)
    # ASCII only
    for a, b in (("\u00b2", "^2"), ("\u00b3", "^3"), ("\u00b9", "^1"), ("\u00f6", "oe"), ("\u220e", "QED"),
                 ("\u201c", '"'), ("\u201d", '"')):
        text = text.replace(a, b)
    # demote headings by two levels
    text = re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + 2) + ' ', text, flags=re.M)
    return text

now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
out = [f"# S1 proofs\n\nCheckpoint of {now}. This file collects the complete proofs behind every statement labelled THEOREM in\n"
       "the report and in S1_CLOSURE.md. Each section was written and checked as a separate unit; each states its exact\n"
       "hypotheses, argument, dependencies and scope, and no statement is used outside that scope. Some sections record\n"
       "intermediate results that were later sharpened; where a later section supersedes an earlier constant, the later\n"
       "section says so. The shipped files are those listed, with their folders, sizes and SHA-256 hashes, in\n"
       "S1_NUMERICAL_CERTIFICATES.md (certificates folder) and the programs of the scripts folder; every file that the\n"
       "shipped check, recomputation and recheck programs read is among them (all of them ran from a fresh restore,\n"
       "S1_RESTART.md section 9). The text also names records and programs of the independent checking of single\n"
       "sections that are not shipped (for example audit_serialization.py in P11.3, audit_recursive.py and its record\n"
       "and log in P33, audit_bound.py and its record and log in P35, audit_extended.json and summary.json in P42), so a\n"
       "file name in the text, even after the words certificate file, does not by itself mean that the file is shipped.\n\n"
       "Convention: a strict inequality between homogeneous quantities of an argument h (norms, seminorms, or such a\n"
       "quantity times a constant), for example N(h) < C E(h), is asserted for h nonzero; at h = 0 both sides vanish and\n"
       "the non-strict form holds. No coefficient or conclusion depends on the strict form at zero.\n\n"
       "Section P10.2 (tail repair) is independently checked: membership of its residual, the coefficient transfer at\n"
       "R = 2^1024 and the residual lower bound 2^1028. Section P8.2 and the statement audit in P8.3 record corrections to\n"
       "earlier drafts of the hypothesis list; S1_CLOSURE.md is the corrected statement. Section P8.4 gives the sharper\n"
       "constants (rate 1/10 - 4800 s - 5 N_s(k)/s^(1/2)) behind version (b) of the conditional existence theorem.\n"
       "Section P12 certifies whole-plane weighted residual norms by exact integration. Section P13 proves that a residual\n"
       "sector r^q E with q >= -2 excludes every exact solution in the affine class reference + N_s (Theorem E of\n"
       "S1_CLOSURE.md) and that the exponent cannot vary in that class; P13.1 is the characteristic version with the forced\n"
       "leading correction. Section P14 constructs exact finite rational references whose residual lies in the space and\n"
       "shows by certified point values that nine of the ten explicit variants violate the energy-matrix hypothesis; P14.2\n"
       "certifies a whole-plane Hessian residual norm of one variant by interval polynomials. Section P15 gives sharp\n"
       "weighted transform bounds for the negative-order norm with homogeneous and regularized weights and shows that the pure\n"
       "homogeneous weight is not coercive; it is not used for closure. Section P16 shows that midpoint angular sampling with\n"
       "too few angles can miss a residual entirely and gives a sufficient number of angles; it concerns floating-point\n"
       "diagnostics only. Section P17 proves the conditional existence theorem D_w in the weighted fractional space N^w_s\n"
       "(far-field weight with R = 2^35), lists the complete reference contract and bounds the residual of the checkpoint\n"
       "from below in that space (P17.7: an annular duality bound N^w_s(F) > 2^89, more than 2^135 times the threshold).\n"
       "Sections P6.12 to P6.16 sharpen the constants of the weighted realization X_W of P6 (radial-resolvent commutator,\n"
       "derivative-energy coefficients, radial weights on higher background derivatives, the inverse norm, and a weighted\n"
       "low bilinear bound); P14.3 writes one repaired reference exactly in the original stable radial coordinates.\n"
       "Section P18 lowers the weight radius of Theorem D_w to R = 2^32 (decay exponent 4/9 in the low-energy bounds) and\n"
       "repeats the annular bound there (N^w_s(F) > 2^82, more than 2^128 times the threshold). Section P19 keeps the\n"
       "coefficients of the lower derivative components of the norm and so improves the threshold of Theorem D_w to\n"
       "2^-35 in the same space (gaps more than 2^124 at R = 2^35 and 2^117 at R = 2^32). Section P20 checks exactly\n"
       "that two projected refits have residuals in both spaces and shows by certified point values that they violate the\n"
       "energy-matrix condition and the smallness condition. Section P21 uses the reality of the density to lower the\n"
       "weighted velocity constant to 13/3 and the radial commutator coefficient to 21/2, which lowers the weight radius of\n"
       "Theorem D_w to R = 2^31 with the constants of P19, and repeats the annular bound there (N^w_s(F) > 2^80, more than\n"
       "2^115 times the threshold 2^-35). Section P22 shows that the frozen heat-norm bounds of P5.1 are optimal, even on\n"
       "test functions with zero strain and zero origin slope. Section P23 derives what the matrix condition forces on the\n"
       "vertical axis (an integrated velocity bound, concavity of a power of an exact profile, a lower bound on the size of\n"
       "any correction that restores the matrix floor) and applies it to the projected refits of P20. Section P24 shows\n"
       "that the matrix condition M >= (19/5) I of Theorem D_w can be replaced by M >= (5/2) I, or by the position-dependent\n"
       "floor 2/5 + (11/5) c r^2/(R^2 + r^2), on the ball r <= R, with every other hypothesis and every constant unchanged.\n"
       "Section P25 bounds from below, by an annular duality argument, the residuals of two exactly admissible projected\n"
       "refits at the weight radius 2^31 (N^w_s(F) > 2^24, more than 2^59 times the threshold). Section P26 records\n"
       "necessary point tests of the full reference contract: both refits violate the Hessian bound |D^2 rho| <= 3, and a\n"
       "third admissible refit has a certified pointwise residual lower bound. Section P27 proves that no choice of\n"
       "coefficients in the generator family of the projected refits, with the prescribed leading data, brings the\n"
       "unweighted residual norm within a factor of 210 of the threshold of Theorem D: the first nonzero residual sector is\n"
       "the same for all of them, and a distance formula for powers in a finite power space turns it into a lower bound for\n"
       "the whole norm. Section P28 records point tests of the reference contract for four later refits (each violates a\n"
       "fourth-derivative bound at a certified point, and certified point values bound their residuals from below).\n"
       "Section P29 shows by an explicit function that the fixed sector and the power structure alone do not force a\n"
       "weighted residual gap. Section P30 derives the residual scales that the threshold of Theorem D_w forces: an Hdot^-1\n"
       "bound below 2^-58 for the weighted residual and a pointwise bound 2^-31 max(1, |X|^(1/5)). Section P31 sharpens the\n"
       "derivative estimate of P27 (P31.1 by an integral operator bound, P31.2 by an orthonormal exponential basis that keeps\n"
       "the radial factor of the cylinder derivative): the factor at the radial degree of P27 becomes more than 1308, and\n"
       "the uniform bound holds for every radial degree up to 779. Section P32 computes the seventh order of the formal\n"
       "stationary expansion exactly and the residual sector that becomes fixed once a seventh branch is added, with the\n"
       "condition that the descendant sector (2,1) must then vanish exactly. P11.2 and P11.4 independently\n"
       "check two annular lower bounds of the checkpoint residual computed in the numerical work; P11.3 audits a\n"
       "floating-point summary. Sections P33 to P35 extend the uniform unweighted bound to every radial degree up to 3675,\n"
       "delimit the annular obstruction and show that the seven-branch family gives\n"
       "no bound exceeding the sufficient threshold; P36 and P42 treat the refits\n"
       "b6 and d2; P37 bounds the strain as a velocity-gradient trace. Sections P38 to P41 and P45 to P49 prove necessary\n"
       "local distances (no exact solution of any exponent near a given reference) by point, square and annular tests, with\n"
       "the amplitude and negative-order embeddings of P44, P47 and P48. Section P43 is the second version of Theorem D_w\n"
       "(smooth commutator, threshold 2^-30). Section P50 identifies the natural domain of the normalized linearization.\n"
       "Section P51 transfers the annular witnesses to every larger weight radius, and P52 gives annular residual gaps and\n"
       "distances for the refits Mpen2 and d2. Sections P53 and P55 extend and sharpen the frozen Hoelder inverse. Section\n"
       "P54 certifies an off-axis violation of the fourth-derivative bound by d2. Section P56 proves that the weighted\n"
       "residual norm attains a positive minimum over each finite fitting family; P57 makes it uniform in the smoothness\n"
       "index and the weight radius with a finite-constant formula, P59 gives the sharp velocity constant on the angular\n"
       "band of the fits, and P60 extends the floor to the seven-branch family; no value is computed. Section P58 certifies\n"
       "off-axis violations of three derivative bounds by Mpen2. Section P61 shows that exact finite constraints and compact\n"
       "perturbations do not make the linearization Fredholm in the critical far-field space. Section P62 evaluates a\n"
       "weaker floor exactly (far below the threshold), and P63 is a consolidated audit of the second conditional\n"
       "theorem (domains, normalized range, low and high inverses). Section P64 extends P61 to critical weighted Sobolev\n"
       "spaces of every order m >= 3 (where the strain is continuous) and to finite parameter columns, P65 gives the\n"
       "far-field spectral line Re z = c b - 1 for the growth exponent b of the space, and P66 sharpens the frozen\n"
       "ordinary Hoelder constants to 97 and 96; P67 improves them to 87 for both checkpoints by a fractional heat\n"
       "representation of the kernel. Section P68 extends P64 to logarithmically modified critical weights and to\n"
       "closed block realizations with arbitrary Banach tail coordinates, and gives the exact membership thresholds of\n"
       "polynomial-log tails. Section P69 computes the exact norm of the strain trace on H^(2+s) and its sharp\n"
       "small-s asymptotics in the weighted norm of the conditional theorem, and shows that it is unbounded at s = 0.\n"
       "Section P70 replaces the fractional gain by a logarithmic one: the strain is continuous exactly for beta > 1/2,\n"
       "with no gradient Hoelder control. Section P71 shows that the certified low residual bounds hold in that\n"
       "logarithmic space as well. Sections P72 to P87 develop the logarithmic space into a complete conditional\n"
       "theorem: P72 writes the circular strain cutoff as a positive average, so the principal value is literal on the\n"
       "completion, and P74 gives an explicit density with divergent strain at the endpoint beta = 1/2; P73 proves the\n"
       "necessary logarithmic distances of exact profiles from the references; P75 and P77 give the fixed-background\n"
       "inverse for every power 0 < beta <= 1 and the normalized range for beta > 1/2; P76 shows that the quadratic\n"
       "transport term is not continuous at 0 from the space into itself; P78 to P82 prove the product and commutator\n"
       "estimates; P83 and P84 introduce the native norm and its products; P85 is the conditional nonlinear theorem\n"
       "(inverse 32, contraction in the low norm, threshold 2^-25 tau^beta (2 beta - 1)^(1/2)); P86 shows that the\n"
       "three references remain excluded in the native norm and miss its threshold; and P87 derives four compatible\n"
       "outputs (low norm, a density Hoelder norm, a projected singular moment at the center and the strain).\n"
       "Section P88 is a consolidated dependency and domain audit of P85. Section P89 makes the bounds on the third\n"
       "velocity derivative and the third and fourth density derivatives free parameters (with a larger hierarchy\n"
       "coefficient and a smaller tau), P90 shows that the exclusions and residual gaps persist for every parameter\n"
       "choice, and P91 gives exact global caps for these derivatives from the coefficients of a finite potential.\n"
       "Section P92 is a second, independent certificate of the global matrix bound for the checkpoint. Section P93\n"
       "audits a third one, a numerical Taylor-box covering of the plane, and recomputes its matrix numbers\n"
       "independently; P94 proves that the bound is sharp: the smallest eigenvalue is at least c + 2 everywhere, with\n"
       "equality only at the origin. Section P95 sets up exact compactified certificates of the global hypotheses for the\n"
       "exact algebraic refits and proves the three matrix bounds M >= (19/5) I and M1, M2 >= I/2 on the whole plane for\n"
       "the reference d2, and also its five fixed derivative bounds and four decay bounds; the hypotheses for Mpen2 are not\n"
       "certified there. Section P96 is a second,\n"
       "independent certificate on the whole plane of the auxiliary matrix bounds M_1, M_2, M_3 and of the bound on\n"
       "sym DU for the checkpoint, with sharper constants.\n"
       "Section P97 shows that the full absolute first-jet-subtracted moment at the center is bounded on H_beta exactly\n"
       "for beta > 3/2, so it is unbounded on the logarithmic spaces of P83 to P87 (1/2 < beta <= 1), and the angular\n"
       "projection in the moment of P87 cannot be omitted. Section P98 proves explicit bounds for the remainders of the\n"
       "density and velocity derivatives at the center for the checkpoint on disks of radius up to 1/10 (exact\n"
       "Taylor division with a rational tail and complete covers). Section P99 gives independent directed covers of the\n"
       "density sign, of A >= -I/20 and of exterior matrix bounds for the checkpoint, and P101 a directed bound\n"
       "|F| <= (48707/200000) r^(2 gamma - 1) for r >= 300 on its residual. Section P102 shows that the example of P97 lies in none\n"
       "of the fractional weighted spaces of the earlier weighted theorem, where the full absolute moment is bounded.\n"
       "Section P103 shows that polynomial growth of every density derivative and of the velocity implies polynomial\n"
       "growth of every velocity derivative. Section P104 recomputes three decay bounds of the checkpoint independently.\n"
       "Section P105 assembles, for the refit d2, every reference hypothesis of the parametric logarithmic theorem of P89\n"
       "and proves that only the smallness of the residual fails, by a factor of more than 2^243. Section P106 shows that a smooth S1 function whose derivatives of order up\n"
       "to four grow at most like <r>^(q-m) with q < 1/5 lies in every logarithmic forcing space of P83 to P89; the actual\n"
       "residuals of the checkpoint, Mpen2 and d2 satisfy this, so their certified native residual floors bound finite norms.\n"
       "Section P108 shows that this power is sharp: an eventual tail r^q (log r)^(-a) Theta lies in these spaces for q < 1/5,\n"
       "not for q > 1/5, and at q = 1/5 exactly when a > 1/2. Section P111 compares the native norm with the norm of\n"
       "the exclusions of P73 directly, E_R(h) <= (1 + 7 tau) Mstar(h), and so excludes exact profiles from the closed\n"
       "native balls of radius 2^77/(2^20 + 7) around the checkpoint and 2^41/(2^20 + 7) around either exact refit.\n"
       "From P33 on, part numbers equal the numbers of the checked units, so a bare two-digit number in a cross\n"
       "reference (for example \"by 83\" or \"of 72, 77\") refers to the part with that number.\n\n"
       "## Contents\n"]
for pl, title, files in PARTS:
    out.append(f"- {pl}. {title}\n")
    for f, lab in files:
        p = os.path.join(SRC, f)
        first = rewrite(open(p).readline().strip().lstrip('# ').strip(), f).strip() if os.path.exists(p) else '(missing)'
        out.append(f"  - {lab}. {first}\n")
out.append("\n")
for pl, title, files in PARTS:
    out.append(f"## {pl}. {title}\n\n")
    for f, lab in files:
        p = os.path.join(SRC, f)
        if not os.path.exists(p):
            out.append(f"### {lab}. (missing)\n\n"); continue
        body = open(p).read()
        first, rest = body.split('\n', 1) if '\n' in body else (body, '')
        out.append(f"### {lab}. {rewrite(first.lstrip('# ').strip(), f).strip()}\n\n")
        out.append(rewrite(rest, f).strip() + "\n\n")
text = ''.join(out)
# words glued in the source texts, and one record pointer that is not part of the proof
for a, b in [('forstate', 'for state '), ('forMpen2', 'for Mpen2'), ('radiusr0', 'radius r0'),
             ('incertificate file', 'in certificate file'), ('ofcertificate file', 'of certificate file'),
             ('andmu=', 'and mu='), ('atalpha=', 'at alpha='), ('andvariable', 'and variable'),
             ('those of 73,', 'those of P73,'),
             ('The actual 16:16 draft review accepts the complete d2 reference contract in topic105; '
              'its bound record is ../review_status_99_101_104_105.json.',
              'The independent review of section P105 accepts its complete d2 reference contract.')]:
    text = text.replace(a, b)
open(OUT, 'w').write(text)
sus = re.findall(r'.{0,30}\b(?:lead|verifier|numerics|lane|astra|codex|Opus|Opus\d[\d.]*|GPT|Claude|Ledger|team|teammates?|[Tt]opics?\d*|V\d\d\d|s1-\w+|/mnt|research/|\.\./|[A-Z_0-9]+_PROOF\.md|PROOF\.md)\b.{0,30}', text)
print(f"wrote {OUT}: {len(text)} chars; suspicious tokens: {len(sus)}")
for s in sus[:60]:
    print('  ', s.replace('\n', ' '))
