# Research reading order

1. `parameter_derivatives/PROOF.md`: conditional velocity and momentum parameter identities and complete weighted least-squares differentiation.
2. `tail_coordinates/PROOF.md`: the existing reduced-to-full tail solve and its extra parameter derivative term.
3. `pressure_consistency/PROOF.md`: decay assumptions that justify pressure differentiation and the interior/exterior Green integrals.
4. `gaussian_pressure/PROOF.md`: an exact smooth non-axisymmetric pressure example for checking the independent integrator.
5. `field_reconstruction/PROOF.md`: exact Cartesian reconstruction and Jacobian identities used by the extended-precision reference.
6. `reduced_sensitivity/PROOF.md`: projection formulas, rank conditions and physical-coordinate conversion for reduced parameter sensitivity.
7. `rotation_generator/PROOF.md`: the vector rotation generator, the sign of the explicit omega column, and its azimuthal norm identity.
8. `angular_polynomials/PROOF.md`: the exact Cartesian polynomial reference for training angular tables.
9. `stable_linear_operator/PROOF.md`: exact potential-level evaluation of the rotating linear momentum operator.
10. `gauge_truncation/PROOF.md`: exact Taylor coefficient of the cost difference at a normalized squared gauge.
11. `pressure_moments/PROOF.md`: conditional zeroth and first source moments and equivalent exterior Newton formulas.
12. `represented_tail_decay/PROOF.md`: smoothness, decay, and zeroth/first source moments for the exact finite channel representation.
13. `homogeneous_tail_quadrature/PROOF.md`: separated radial field identities and exact power/log integration of the rotating leading source.
14. `angular_source_projection/PROOF.md`: finite angular support of the pressure source and exact product-quadrature conditions.
15. `normalized_angular_recurrence/PROOF.md`: normalized complex recurrence and literal Cartesian product derivatives for a faster independent angular reference.
16. `split_complete_jvp/PROOF.md`: exact row-block decomposition of the complete residual directional derivative.
17. `holdout_quadrature/PROOF.md`: normalized volume quadrature and exact finite-sample residual comparison identities.
18. `green_edge_recurrence/PROOF.md`: scaled finite Green-sum recurrences at source-panel edges, with the raw source moments retained.
19. `closure_norm/PROOF.md`: fixed weighted target-norm derivative and its distinction from residual row scaling.
20. `schwartz_pressure/PROOF.md`: exact decaying Poisson reference for the extended Green quadrature.
21. `low_multipole_flux/PROOF.md`: exact finite-radius monopole and dipole source moments from boundary fluxes.
22. `discrete_coefficient_derivative/PROOF.md`: fixed-discretization coefficient derivative including the complete nonlinear shell weights.
23. `endpoint_radial_polynomials/PROOF.md`: exact shifted-Chebyshev evaluation near the radial endpoint.
24. `radial_power_log_pressure/PROOF.md`: exact radial power and logarithmic tail pressure tests.
25. `vorticity_identity/PROOF.md`: Cartesian curl, divergence and Hessian identities for independent vorticity checks.
26. `vorticity_potentials/PROOF.md`: reusable tensor and scattered evaluation of Omega and its first derivative.
27. `vorticity_holdout/PROOF.md`: normalized cap and ball rules and physical-volume combination of vorticity norms.
28. `energy_helicity/PROOF.md`: exact finite-ball residual identities and conditional energy/helicity exterior bounds.
29. `canonical_origin_vorticity/PROOF.md`: exact dyadic axial origin residual and rigorous normalization enclosures.
30. `displaced_ball_quadrature/PROOF.md`: radial cap integration of a displaced ball and exact polynomial controls.
31. `pressure_cartesian_difference/PROOF.md`: Cartesian fourth-order pressure stencils and conditional error bounds.
32. `azimuthal_projection/PROOF.md`: resolved discrete Fourier projection and derivative-weighted non-axisymmetry bounds.
33. `finite_tail_integrability/PROOF.md`: exterior remainder bounds that imply finite renormalized energy and absolute helicity convergence for the exact finite basis.
34. `newton_tail_decay/PROOF.md`: explicit Newton-pressure decay from zeroth and first source moments, and exact integral compatibility for the finite basis.
35. `angular_residual_norms/PROOF.md`: angular polynomial degree bounds and exact-arithmetic product quadrature for centered-sphere residual norms.
36. `parameter_coordinate_conversion/PROOF.md`: conversion of native optimizer Jacobian columns to physical parameter columns at the same reduced coefficients.
37. `origin_parameter_sensitivity/PROOF.md`: exact origin vorticity sensitivity and whole-interval exclusion at fixed reduced coefficients.
38. `../verification record`: chronological implementation verdicts and numerical evidence.

Each topic has a standalone informal proof and named `formal/` and `verification/` subfolders. No formal proof has been attempted; Lean/Lake builds are prohibited. Numerical tests do not certify the analytic hypotheses for a saved state.

- [Small-group derivative exclusion: exact bound and counterexample](group_exclusion_bound/PROOF.md). Read with the G1 validation protocol; this is a gate-rationale review, not a field result.
- [Physical derivatives and a fixed error floor](physical_parameter_floor/PROOF.md): exact normalization identity and counterexample; read with specification 3.0(b), (b')(1).
- [Exact bytewise reference storage](lossless_reference_storage/PROOF.md): recovery of newly computed arrays from arbitrary retained reference bytes, with no numerical-equality assumption.
- [Exact reconstruction during archive packing](streaming_archive_preservation/PROOF.md): conditional byte-preservation argument for reversible capacity maintenance. This concerns storage integrity, not Euler validation.
- [Scope of a table sensitivity screen](table_sensitivity_scope/PROOF.md): exact counterexamples for perturbing outputs instead of intermediate tables, finite-direction guarantees, and frozen residual weights. Read before interpreting any base-point screen for rule (l).

- [Exact float imports and double-double splitting](exact_float_dd_import/PROOF.md): exact counterexample to decimal-string import under a binary64-input convention, with verification evidence in the adjacent verification folder.

- [Fixed-geometry pressure-table factorization](pressure_kernel_factorization/PROOF.md): finite-sum factorization and analytic parameter derivatives, under explicit unclamped-kernel and input conventions. Read after pressure_consistency and before a high-precision pressure-table implementation.

- [Finite radial and twist jets](radial_jet_tables/PROOF.md): exact derivative-table recurrences with input and precision scope; read before checking the proposed double-double radial tables.

- [Retaining double-double pairs through finite-difference division](dd_difference_rounding/PROOF.md): exact scalar counterexample to rounding the numerator first; helper check and scope limits.

- [Reverse-over-reverse pressure differentiation](reverse_mode_pressure/PROOF.md): required cotangent graph, exact frozen-wrapper fixtures, and the limitation of the supplementary graph checker (V253).

- [Elementary pair arithmetic](dd_elementary/PROOF.md): exact range-reduction and Taylor identities, with sampled implementation checks distinguished from uniform error guarantees.

- [Propagation of pressure-table perturbations](pressure_perturbation_scope/PROOF.md): conditional finite matrix and finite-difference bounds, including source, reconstruction and row-weight amplification. Read with the revised elementary-function qualification. No numerical bound for a campaign state is asserted.

- [Conditional finite residual correspondence](dd_residual_correspondence/PROOF.md): potential and finite Green assembly, held/recomputed reference conventions, the named degree-one E restriction, and separation of algebra from arithmetic. Read with V280 and the frozen source map in its verification folder.

- [P1 segment-1 finite comparison evidence](holdout_quadrature/verification/P1_SEGMENT1_READING_GUIDE.md): complete retained metrics, exact domain radii and the V281 correction. Read after the positive-volume quadrature proof.

- [Finite paired-exponent cutoff classification](pressure_cutoff_classification/PROOF.md): exact predicate theorem, rational logarithm enclosure and separately bound finite scans.

- 2026-10-29T12:25:26.983234+00:00: [Exact origin intervals at four segment-one endpoints](canonical_origin_vorticity/verification/SEGMENT1_ENDPOINTS_v1.md), V286. Exact finite canonical fields only.

Segment-one common vorticity extensions: `vorticity_holdout/verification/SEGMENT1_COMMON_plan_v1.md` (preregistered, execution pending).

- [Prospective Phase IV validation plan](holdout_quadrature/verification/PHASE_IV_plan_v1.md): cohort freeze, fresh seeds, stronger pressure grids, capacity and final claim audit. No final result is asserted.

- [Phase IV plan version 2](holdout_quadrature/verification/PHASE_IV_plan_v2.md) supersedes version1: reuse the existing V222-qualified memory-only driver; no new cache implementation is needed.

Additional reading-order entries (2026-10-29):

- Angular tables: [all-order reference plan](angular_polynomials/verification/ALLM_REFERENCE_plan_v1.md), after the angular-polynomial proof. V313 is a synthetic preflight; actual S20 coverage remains open.
- Independent holdouts: [segment-two common plan](holdout_quadrature/verification/SEGMENT2_COMMON_plan_v1.md), after the segment-one momentum comparisons.
- Vorticity: [segment-one comparison guide](vorticity_holdout/verification/SEGMENT1_READING_GUIDE.md), after the vorticity proof and quadrature plan.

- [Completed S20 all-order capture checks](angular_polynomials/verification/S20_CAPTURE_READING_GUIDE_v1.md): V317/V320/V321; exact nodes, finite reference comparisons, and CPU JVP argument-use scope.

Recent verification reading guides: [P1 segment-two momentum/pressure comparison](holdout_quadrature/verification/P1_SEGMENT2_READING_GUIDE.md), [S20 captured angular tables and CUDA transfer](angular_polynomials/verification/S20_CAPTURE_READING_GUIDE_v1.md), and [S01 retained-record adapter](dd_residual_correspondence/verification/S01_OLD_RECORD_ADAPTER_plan_v1.md). Read each topic's PROOF.md before the finite numerical checks; these guides introduce no new theorem.

- [Generic displaced-ball endpoint plan](displaced_ball_quadrature/verification/SEGMENT2_GENERIC_plan_v1.md): read after the displaced-ball PROOF.md; V331 qualifies the adapter, actual doubled-node endpoint evaluation is queued.

- [Conditional finite-difference attribution](finite_difference_attribution/PROOF.md): explicit truncation and evaluation-error hypotheses, Taylor coefficients, and exact quadratic-cost difference identities. Read before interpreting the S11 G3 failure.

- [Fixed-parameter coefficient derivative of the modal gauge](gauge_coefficient_derivative/PROOF.md): exact norm, rationalized centered difference, and reduced-coordinate scope. Read after tail_coordinates and before interpreting the manu_a gauge investigation.

- [Finite augmented diagnostics](augmented_diagnostics/PROOF.md): read after the holdout and displaced-ball proofs. Defines finite maxima, center and upper-radius weights, screening, and the scope of alternate quadrature unions.

- [Fixed binary64 constants and actual stencil offsets](fixed_constant_gauge/PROOF.md): read after the modal coefficient-gauge proof. Exact rational expansion and quadratic norms; Decimal square roots are numerical checks, with production correspondence still separate.

- [Six-state finite augmented comparison](../artifacts/six_state_augmented_comparison_v1/COMPARISON.md): INITIAL and both segment-two endpoints for P1/P2, after the individual holdout guides; read the augmented-diagnostics proof for exact definitions.

- [Scaled QR identity](scaled_qr_identity/PROOF.md): exact scaling required when comparing endpoint Jacobians with saved QR records; V364 source audit.

- [Finite accepted-step progress criterion](progress_criteria/PROOF.md): exact stored-number stopping decisions, window conventions across restarts, and the distinction from physical residual progress.

- [Scheduler acknowledgment counterexamples](scheduler_admission/PROOF.md): finite source-order proof; fixture evidence in ../artifacts/governor_v9_audit_v1.

- [Segment-two interpretation and warning predicates](reduced_sensitivity/verification/SEGMENT2_CLASSIFICATION_v1.md): distinguish eta from the stored-space complement and apply the registered absorption warning without inferring nonlinear non-identifiability.

- [Segment-three comparison qualification](holdout_quadrature/verification/SEGMENT3_COMPARATOR_v1.md): common-grid compatibility and complete scalar arithmetic, before interpreting the new development holdouts.

- [Continuation guard review](scheduler_admission/verification/SEGMENT_GUARD_v1.md): source omissions, exact false-clean fixtures and actual record outcomes, after the scheduler proof.

- [Limits of two pressure quadratures](pressure_refinement_limits/PROOF.md): read after holdout_quadrature. Distinguishes stability between computed approximations from an absolute error bound; exact counterexamples accompany V400.

- [Exact modal pressure Laplacians](modal_pressure_laplacian/PROOF.md): Gaussian and rational manufactured pressures, the centered radial-difference bound, and modal shell RMS. Read before the pressure code-test audit; no campaign-state error bound follows from a manufactured test.

- [Finite branch comparison and parameter boxes](branch_identity/PROOF.md): pairwise norm criterion, optimizer scaling, curvature scope, nontransitivity and incomplete endpoint evidence; then read its verification results.

- [Applying a fixed-state Jacobian correction exactly once](solver_jacobian_hook/PROOF.md): finite matrix identity, damped model step and the distinction between optimizer arithmetic and recorder metadata.

- [Segment-four displaced-ball plan](displaced_ball_quadrature/verification/SEGMENT4_plan_v1.md): read after the displaced-ball proof; both endpoints, sampled centers, unchanged doubled-node rules.
- [Segment-four and medium-end sensitivity plan](reduced_sensitivity/verification/SEGMENT4_MEDIUM_plan_v1.md): V446/V447 endpoint bindings, complete-factor arithmetic, model widths and branch parameter tests; read after reduced_sensitivity/PROOF.md.

- [Scope of high-mode flags](high_mode_flags/PROOF.md): exact scale invariance of normalized coefficient ratios, the proposed high-mode damping formula, and the limited meaning of a half-improvement test. Read with specification 6.3(b).

- [Least-squares model identity](least_squares_model_identity/PROOF.md): exact Gram/gradient/residual-norm characterization and its limits; read after scaled_qr_identity before interpreting strategy-2 smoke comparisons.

- [Axial-rotation field comparison](branch_identity/axial_rotation/INDEX.md): cylindrical shift, Fourier formula, and a complete finite-search margin. Read after the branch comparison and rotation-norm proofs. Numerical implementation is pending and will retain its quadrature and rounding limits.

- [Logarithmic twist and shell alignment](branch_identity/logarithmic_twist/INDEX.md): exact characteristic sign, producer-to-active angle conversion, and the conditional scope of an observed shell-angle slope.

- [Amplitude and normalized shape](branch_identity/amplitude_shape/PROOF.md): separates the rotation-invariant norm mismatch from the normalized directional field mismatch. Read after the axial-rotation proof.

- [Exact origin identity for unrestricted azimuthal modes](canonical_origin_vorticity/general_modes/INDEX.md): retains the radial poloidal curl and explicit rotation contributions. Read after the even-mode origin proof; actual unrestricted-mode checks require separate qualification.

- [Fixed-parameter field refit](tail_coordinates/refit/PROOF.md): the reduced coefficient fit, singular-value truncation and raw/post-gauge comparison scope.

- [Spectral cutoff margins and their limits](reduced_sensitivity/spectral_gap/PROOF.md): why a largest-singular-value discrepancy alone cannot validate matrix perturbation or sensitivities.

- [Odd azimuthal content and even-field comparison](branch_identity/odd_modes/PROOF.md): read after the axial-rotation and amplitude/shape identities; half-turn projection and its numerical scope.

- [Profile initialization and finite-budget bounds](profile_initialization/PROOF.md): a lower initial objective does not guarantee a lower optimized value; exact damped least-squares counterexample.

- [Scope of homogeneous transport and selected shell angles](branch_identity/logarithmic_twist/linearization_scope/PROOF.md): read after the logarithmic-twist proof; explicit small-velocity, Cartesian-frame and nonunique-minimizer counterexamples.

- [Signed origin ratios](canonical_origin_vorticity/signed_ratio/INDEX.md): exact interval division and the even-mode cancellation, with a zero-vorticity exception and pointwise diagnostic scope.

- [Field-relative coefficient perturbations at fixed parameters](initialization/perturbation/PROOF.md). Read before assessing F3 initialization: zero parameter increments are not zero physical parameters; training norms and permitted coefficient subspaces must be specified.

- [First nonlinear far-field coefficients](first_nonlinear_coefficient/PROOF.md): read after field reconstruction, angular normalization and the stable linear operator; exact carried B,D coefficient, homogeneous pressure coefficient, a separate modal norm and energy/helicity cross coefficients. The full-pressure implication has an explicit remainder hypothesis.

- [A finite refit retains the target leading exponent](tail_coordinates/refit/fixed_asymptotics/PROOF.md): read after the finite-representation tail expansion and fixed-parameter refit. A finite fit does not import another exponent, and amplitude signs require fit-domain information.

- [Objective recovery and field distance](initialization/perturbation/objective_recovery/PROOF.md): exact counterexample and the scope of the F3 two-step claim (V513).

- [Sharp even-field separation](branch_identity/odd_modes/sharp_normalized_bound/PROOF.md): read after the odd-mode proof. The normalized distance has lower bound sqrt(2-2sqrt(1-delta^2)), sharper than the odd fraction delta. This corrects V538's overly broad refutation of the0.43distance statement.

- [F1 second-medium saved-factor check](reduced_sensitivity/verification/F1_M2_plan_v1.md): read after the reduced-sensitivity and progress proofs; V560 gives endpoint bindings, cutoffs and numerical scope.

- [F1 second-medium exact origin application](canonical_origin_vorticity/verification/F1_M2_plan_v1.md): unchanged rational origin theorem at the raw iteration-386 endpoint, with explicit single-field scope.

- [Amplitude normalization and the Euler residual](profile_normalization/PROOF.md): read after pressure_consistency and profile_initialization. Distinguishes uniform coefficient scaling from the spatial profile dilation and gives the exact linear/quadratic residual identity; V727 supplies the separate saved-vector application.
