# Reading order for verifier results

Packets 310, 314, 318, 322, 327, 358, 359 and 360 audited the packaging of an earlier, superseded version of the working archives and of the report files as they then stood; they concern no mathematical or numerical result and are not included here. Only the written proof and summary of each packet are published; links to other files of a packet (its verification/ subfolder, inputs and outputs) point into the working archives, which are not published.

1. `01_transport/PROOF.md`: subcritical exclusion, bounded temperature at beta=2, and conditional growth for beta>2.
2. `02_beta2_curve/PROOF.md`: the compulsory local curve of equilibria, its curvature, and a local polynomial control example.
3. `03_inverse/PROOF.md`: signs, canonical relative velocity, absolute-velocity ambiguity, and scope of the decaying-vorticity class.

4. `04_source_basin/PROOF.md`: exact temperature sign and uniqueness on the source basin for beta>2.

Each directory separates the informal proof from `verification/` evidence and `formal/`. No formalization is claimed; Lean and Lake execution are prohibited for this run. Further packets will be indexed here before being used in the final report.

5. `05_scattering_tail/PROOF.md`: the audited scattering theorem, weighted vorticity exclusions, and the corrected absolute drift-component case.
6. `06_temperature_integrability/PROOF.md`: a single finite temperature L^p integral excludes every beta>0.

7. `07_reconstruction_scaling/PROOF.md`: exact physical reconstruction, signed scaling and the repaired time-dependent observer transformation.

8. `08_analytic_beta2/PROOF.md`: beta=2 analytic exclusions and necessary infinitely flat temperature/vorticity jets, confirmed by independent lead and verifier arguments.

9. [Vorticity mass and finite-integrability obstructions](09_vorticity_mass/PROOF.md). Half-plane mixed identity, a mass lower bound without DU decay, and a finite-enstrophy extension under only sublinear velocity.

10. [Material-center translation mode](10_translation_mode/PROOF.md). Exact fixed-beta and adaptive-beta linearized identities and the scope of the instability conclusion.

11. [Adversarial examples](11_adversarial_examples/PROOF.md). A perfect core with a remote annulus defect, distinct absolute-integrability conditions, and cutoff-shape dependence.

12. [Polar center smoothness](12_polar_smoothness/PROOF.md). Necessary angular Taylor powers, a documented intermediate-state defect and a compatible alternative radial map.

13. [Averaged velocity convention](13_mean_velocity_gauge/PROOF.md). An explicit possible observer gauge with nonzero center velocity and exact scaling covariance; not yet selected by the lead.

14. [Angular temperature far field](14_angular_far_field/PROOF.md). Derivative-free angular limit, logarithmic critical norm growth, and the critical-tail sign theorem.

15. [Sectorial mass and absolute center integral](15_sector_mass/PROOF.md). New distributional test gives mass away from the axis and removes DU decay from the actual center-component exclusion in the power-sublinear class.

16. [Fixed-basis tail exponent](16_basis_exponent/PROOF.md). A free PDE exponent in a fixed endpoint-power family is constrained by its far field; an intermediate-state residual limit is computed explicitly.

17. [Nonzero transported circulation](17_circulation_mass/PROOF.md). Stronger mass R^(2-1/beta), corrected positive-part sign, and all Lp through p=2 beta under only sublinear velocity.

18. [Circulation in a fixed sector](18_sector_circulation/PROOF.md). New extension under review: positive slow-tail mass away from the axis, including beta=2 via a regular-value escape lemma.

19. [Logarithmic inverse resonance](19_logarithmic_resonance/PROOF.md). Exact smooth dipole test, divergent ordinary center drift, and conditional limits of pure-power tail ansatzes.

20. [Smooth beta2 transport counterexample](20_beta2_transport_counterexample/PROOF.md). Canonical decaying velocity, compact equilibrium segment and flat endpoint jets coexist with nontrivial smooth first-integral temperature; the vorticity equation fails explicitly.

21. [Center regularity of the circulation resolvent](21_circulation_resolvent_regularities/PROOF.md). The auxiliary H has a sharp one-sided power exponent below1 and is not differentiable at the center.

22. [Independent Gaussian forcing check](22_gaussian_forcing_check/PROOF.md). Closed-form full-plane external inverse, nonzero material drift, independently derived source jets and adaptive characteristic verification.

23. [Integrable variational tail](23_integrable_variational_tail/PROOF.md). Precise H1prime hypothesis implies C1 scattering without a separate power velocity assumption; pointwise slow-tail classification remains conditional.

24. [Beta-two regular levels](24_beta2_regular_levels/PROOF.md). Independent Sard and proper-line proof of the range on the equilibrium set, with finite regular-level components and exact scope of the lead closure attempt.

25. [Constant relative-velocity tail](25_relative_constant_tail/PROOF.md). Canonical inverse can retain an outer constant; conditional transport corrections can require noninteger endpoint powers in an r2 compactification.

26. [Interpolated velocity at the center](26_interpolated_velocity/PROOF.md). Exact interpolation counterexample and independent manufactured divergence and smoothness checks for the current characteristic rule.

27. [Exact axis transport](27_axis_transport/PROOF.md). Independent scalar quadratures for desingularized F and G, branch positivity and a nonzero conditional axis tail.

28. [Axis zeros and smoothness resonances](28_axis_resonance/PROOF.md). Sign-free necessary arithmetic at nearest saddles, positivity refinements, degenerate flatness, analytic-axis scope and a third-order center test.

29. [Positive shifted-power forcing](29_shifted_power_forcing/PROOF.md). Independent proof of the lead transport-only construction, including canonical inverse, global contraction and an exact vorticity-equation defect.

30. [Global axis continuation parity](30_global_axis_parity/PROOF.md). Continuation beyond a first saddle excludes odd/odd reduced beta, with stronger restrictions under either temperature or vorticity positivity.

31. [Relative inverse under sublinear velocity](31_sublinear_relative_inverse/PROOF.md). Full vector identity as a smooth truncated limit, regularization-shape independence and the distinction from absolute convergence.

32. [Power-decaying vorticity without orbit-integral derivative control](32_decaying_vorticity_without_D/PROOF.md). CONFIRMED independent kinematic construction, with actual Opus18 audit checked. Smooth bounded canonical velocity and Omega=O(1/r), but(D) fails along the axis. Not a full B2 profile.

33. [Automatic derivative control in class A](33_automatic_D_in_class_A/PROOF.md). CONFIRMED. Two independently checked routes prove automatic(D), gradient-temperature decay and the nonzero angular vorticity tail in class A; no full endpoint.

34. [Center strain moment](34_center_strain_moment/PROOF.md). Exact strain identity with convergent integrals; polar temperature kernel is sin(3theta)/r^3 with plane measure. Corrects numerics note10.

35. [Fixed-polar second terms](35_fixed_polar_second_terms/PROOF.md). CONFIRMED: local physical continuation and circle characteristics give the second vorticity term in every finite angular Lq and the second temperature term uniformly.

36. [Local propagation of smoothness](36_local_smooth_continuation/PROOF.md). CONFIRMED by verifier: shrinking-cutoff energy induction upgrades the physical limits away from0 to smooth and the second polar corrections to uniform Cj. External requests24/25 supplied no text; actual Opus27 later audited the simplified starting step.

37. [Revised stream interpolation: interfaces and higher angular jets](37_revised_stream_interpolation/PROOF.md). CONFIRMED exact counterexamples with independent Legendre-series tests. Cellwise differentiated Gauss interpolants can jump across radial cells and leak r2 angular mode4 at0. Production-state error sizes measured in packet46.

38. [Velocity second terms and beta-two logarithm](38_velocity_second_terms/PROOF.md). CONFIRMED, with actual Opus26/27 audits checked: homogeneous second inverse for beta>2; resonant logarithm, fixed constant and stronger remainder at beta2.

39. [Bounded vorticity and beta-two class reductions](39_bounded_vorticity_reduction/PROOF.md). CONFIRMED: bounded Omega and U=o(r) imply power decay and the canonical relative inverse; beta2 needs no vorticity growth bound.

40. [Polynomial vorticity reduction](40_polynomial_tail_reduction/PROOF.md). CONFIRMED after actual Opus28 audit checked: local logM strain bound and finite exponent descent put the full polynomial-tail target in class A. No full endpoint.

41. [Absolute-Lp averaged vorticity reduction](41_averaged_vorticity_reduction/PROOF.md). CONFIRMED by verifier: bounded scale-normalized Lp averages for p>4 give a directional strain bound and an integrable coupled Gronwall estimate. Actual Opus29 audit checked; no signed-average or p=4 claim.

42. [Global smooth stream representation](42_global_stream_representation/PROOF.md). Independent new search space with exact canonical relative inverse and center constraints, fractional tails and analytic coefficient Jacobian. Manufactured FD, Jacobian and Cartesian inverse tests passed. All37 fits failed candidate checks. Opus30/31 supplied no audit text.

43. [homotopy scalar compatibility](43_homotopy_scalar_compatibility/PROOF.md). Complete independent proof and precise scope; see status at its start.

44. [critical vorticity flux](44_critical_vorticity_flux/PROOF.md). Complete independent proof and precise scope; see status at its start.

45. [Beta-two equilibrium arc and outgoing wedge](45_beta2_equilibrium_arc/PROOF.md). CONFIRMED after actual Opus32 audit checked. Compact symmetric arc, flat endpoints, and an open invariant zero-vorticity region in the outgoing case. Partial theorem, no endpoint.

46. [Production interpolation audit](46_production_interpolation_audit/PROOF.md). Independent modal integral derivation and Legendre trace evaluator; manufactures and order128/256 production-source measurements complete. Stable origin, interface and exterior polynomial-tail defects; details in its verification/SUMMARY.md.

47. [Strain-moment counterexamples with algebraic tails](47_strain_moment_counterexamples/PROOF.md). Exact canonical family with all listed center normalizations and a fixed nonzero algebraic tail; NL has both signs. One member satisfies the scalar strain identity exactly while the divided temperature PDE has a nonzero linear axis defect. CONFIRMED: own quadrature and inverse checks passed; actual Opus36 withdrew its earlier wrong-convention objection after an exact-prompt followup.

48. [Global source coordinates](48_global_source_coordinates/PROOF.md). Independent constructive proof of smooth area coordinates and a triangular normal form, with even resonances only; a global C1 linear conjugacy always exists. Refutes the lead note's C1 uniqueness argument and replaces it without a linearization theorem. CONFIRMED after actual Opus37 review, with chart and relative-velocity details made explicit.

49. [Axis reflection exclusions](49_axis_reflection_exclusions/PROOF.md). CONFIRMED with actual Opus38 and own symbolic algebra. G excludes every shifted radial vorticity quotient; a common horizontal source reflection requires a strict minimum of its axis quotient. Restricted shape results only.

50. [Axis quotients for the full target](50_axis_quotients_full_class/PROOF.md). CONFIRMED after actual Opus38 review. All derivative and tail bounds survive division by axis factors on the full class, extending the quadratic and critical horizontal identities beyond G. New critical quotient-power fluxes retain their nonzero outer terms. Independent temperature-only manufacture reproduces the critical flux7.5.

51. [Global-source integrals and vector-resolvent limitations](51_global_source_integrals/PROOF.md). Complete independent audit of the remaining gsrc1 estimates, positive axis tails, strip identity, absolute strain resolvent, finite-time integration by parts and the divergent-vector counterexample. CONFIRMED by the independent verifier; actual Opus39 returned no text, no endorsement. No endpoint.

52. [Two-term dipole obstruction](52_two_term_dipole_obstruction/PROOF.md). Own complete proof excludes a pure cosine in both first vorticity terms, hence every exactly shifted radial quotient, on the full target without G or sign assumptions. CONFIRMED with own symbolic sign check and actual Opus41 written audit; external40 remains unavailable. Restricted shape result only.

53. [Beta-two zero-arc dynamics and analytic boundary](53_beta2_zero_arc_audit/PROOF.md). Independent audit of beta2d D1-D4, including the return-loop area lemma and a separate complex reflection proof that avoids the analytic Poisson Cauchy construction. CONFIRMED by own complete proof after checking auditP local repair. Opus42/44 provided no audit text; actual Opus46 focused local-basin/reflection audit returned and was checked. It did not review the global return lemma or circle partition. Only restricted geometry/exclusion.

54. [Beta-two scattering and canonical moments](54_beta2_scattering_identities/PROOF.md). CONFIRMED independent D5-D8 audit: exact scattering Jacobian and source, weighted and levelwise critical production, absolute characteristic inverse, resonant moment constant, and positive axis tails under the single-axis-zero hypothesis. Exact algebra and independent full-plane manufactured quadrature passed. Opus43 provided no audit text.

55. [Extremal temperature and zero-vorticity escaping orbits](55_beta2_extremal_orbits/PROOF.md). CONFIRMED elementary transport proof excludes strictly signed vorticity throughout the open right half-plane at beta2, and excludes a nonzero pure-cosine leading tail already at first order. Weak sign with zeros remains open. Opus44 provided no text; actual Opus45 usable audit returned and was independently checked.

56. [Weak vorticity sign and degenerate angular extrema](56_weak_sign_extrema/PROOF.md). CONFIRMED own proof plus actual Opus47 checked. For beta>=2 weakly signed vorticity forbids every horizontal escaping orbit. At beta2 all interior critical points of h must have hsecond=0. Degenerate extrema and plateaus remain open; no full endpoint.

- [57 Additional equilibria for beta>2](57_additional_equilibria/PROOF.md): CONFIRMED complete own audit of zeros1 plus actual Opus48/50/51/52 with scope and reviewer corrections recorded. Source boundaries, axis resonances, hyperbolic tree and flatness propagation. Restricted structural results, no endpoint.

58. [Weak sign on interior equilibrium fibres](58_beta2_interior_fibre_sign/PROOF.md). Main theorem CONFIRMED with actual Opus53. Conditional monotonicity corollary CONFIRMED with actual Opus57 under its extra no-constant-subarc hypothesis. Continuous characteristic resolvent excludes every sign-reversing temperature derivative on an escaping fibre from the interior arc, including finite-order degenerate extrema. Endpoint/plateau cases remain open.

59. [Finite-order critical directions](59_beta2_critical_jets/PROOF.md). Complete independent beta2 jet proof and exact coupled local saddle-threshold tests. Actual Opus54/56 supplied no written audit; no endorsement claimed.

60. [Physical critical temperature orbits](60_physical_critical_orbits/PROOF.md). Complete independent proof of Hessian vanishing at every beta>=2 under weak sign, and finite even-order exclusion with a nonsaddle backward limit. External review58 supplied no text. No full endpoint.


2026-10-20 update: packets59 and60 are CONFIRMED by the independent verifier,
with exact product-rule tests for59 and explicit actual-Opus no-text
limitations. Packet59 now includes a transverse-section flatness proof
and the flatness of both first far-field vorticity coefficients. These
are restricted results and do not approve an early endpoint.

61. [Smooth escape conjugacy](61_smooth_scattering_map/PROOF.md): CONFIRMED 2026-10-20T19:05:38.044851+00:00, with actual Opus5.5 review60. Complete C-infinity proof on E using packet36; no extension through K and no endpoint.

62. `62_manufactured_nonlinear_validation/PROOF.md`: exact forced/self residual distinction, manufactured-test scope and serialization requirements; numerical audit linked separately.

63. `63_adaptive_fullplane_inverse/PROOF.md`: complete modal representation, gauge and uniqueness proof; independent adaptive physical-radius implementation, manufactured tests and Cartesian cross-check. Actual Opus62/63 review exchange checked and corrected.

64. [Global-source map equivalence and adjoint strain](64_global_source_map_adjoint/PROOF.md): centered nonresonant map formulation, local generating-function scope, and absolute Fubini justification of the global strain identity. No exclusion of G.

65. [Axis and angular tail matching](65_axis_angular_tail_matching/PROOF.md): CONFIRMED own proof of positive axis limits, angular vorticity slopes and quadratic temperature zeros under each no-additional-axis-zero hypothesis, including beta2. In G horizontal temperature monotonicity implies strictly positive vorticity and tail. No endpoint.

66. [Global-source temperature tail and angular area geometry](66_global_temperature_tail_geometry/PROOF.md): CONFIRMED positive temperature tail and global two-sided Theta/x^2 bound for all G. In the linearizable case the angular area identity forces two zeros of the eta coefficient. An explicit global weighted area map refutes geometry-only horizontal monotonicity. No PDE endpoint.

67. [Resonant angular logarithms and endpoint compatibility](67_resonant_angular_tail/PROOF.md): CONFIRMED finite-Taylor residue matching for the even normal-form resonance in G, with actual Opus5.5 review69 and smooth-remainder correction. Exact logarithmic radial law, corrected-coordinate zeros and logarithmic angular approach on large scattering circles. Necessary conditions only.

68. [Independent characteristic reconstruction](68_independent_characteristic_reconstruction/PROOF.md): CONFIRMED conditional transport formulas and leading-jet cutoff limit for a true beta>2 profile. Own C2 stream/C1 velocity implementation passes analytic and nonlinear cutoff manufactures. Opus71 returned provider refusal, no audit text. Finite-cutoff saved-state diagnostics are separate and not a profile.


69. [Homogeneous weights and their exact scope](69_homogeneous_weights/PROOF.md): CONFIRMED complete independent audit and15 exact checks. Grouped centered kernels, smooth-blob counterexamples to sign shortcuts, single-strain-identity feasibility with positive fields and exact jets, Mellin completeness/residue, and strain bound. Two draft4.23 scope repairs required. Actual Opus72 returned no audit text. No endpoint.

70. [Literature conventions and the center jet](70_literature_conventions/PROOF.md): CONFIRMED exact coordinate/sign translation and parity obstruction for the specified symmetric construction. Primary-text scope audit of2310.19780v1 and2604.01868v1, with regular-stage and fixed-center wording corrections. No general exclusion.

71. [Exact angular null directions](71_angular_sampling_nullspace/PROOF.md): CONFIRMED independent proof and tests. K16,Nphi_res12,Nb61 give at least218 null directions per value fit, preserving strain and optionally all center/tail data. New oversampled launches remove this particular nullspace; no nonlinear-map or PDE convergence claim.

72. [Analytic trajectories and limiting curves](72_analytic_trajectories_and_endpoint_scope/PROOF.md): complete elementary counterexample to promoting finite-time trajectory analyticity to analytic closure at an infinite-time equilibrium. No PDE profile or exclusion; beta2 flat endpoint remains open.

73. [Local affine-coordinate detachment](73_local_affine_detachment/PROOF.md): complete restricted ODE obstruction to a flat launch of horizontal velocity in a Cartesian affine-y ansatz. Does not apply after arbitrary coordinate straightening and does not settle beta2.

74. [Arbitrary strain-functional values](74_prescribed_strain_functional/PROOF.md): two positive temperature bumps give every real value with fixed canonical vorticity, exact center jets and tails, now including beta2. Smooth nonprofiles only; both PDEs fail explicitly.

75. [Center-strain shells](75_strain_shells_and_tail/PROOF.md): exact physical-radius and represented-spline shell formulas, cancellation ratio, slow-tail coefficient and scaling. Independent numerical audit follows; no PDE endpoint.

76. [Fixed forcing tail and changing basis](76_fixed_forcing_tail_scope/PROOF.md): exact weighted-tail obstruction and conditional seed/residual identities. Actual seed source leading coefficient checked by exact rational arithmetic; no zero-forcing endpoint exclusion.

77. [Adjoint derivative integrability](77_adjoint_derivative_integrability/PROOF.md): complete kinematic counterexample with exact local B2 equations and global temperature transport. Absolute integral of Theta M_x diverges although that of Theta_x M is finite. Not a global profile; actual Opus review unavailable (requests78/79; no endorsement).

78. [Fixed-source velocity tail](78_fixed_source_velocity_tail/PROOF.md): nonzero original source tail persists under canonical inversion and obstructs the stronger retied velocity norm. Explicit cutoff construction preserves center strain and local inverse convergence, delimiting the conclusion. No endpoint.

79. [Integrated residual balance](79_integrated_residual_balance/PROOF.md): complete full-plane identity D[V]=integral(g R_Theta/2-K R_Omega), with every singular and far boundary term controlled. It distinguishes self-induced and forced transport moments, and provides an independent numerical consistency check without claiming PDE accuracy from a moment.

80. [Retied forcing above the seed exponent](80_retied_source_above_seed/PROOF.md): exact transformed coefficient z^(beta/beta_S-1) D(1-z^(beta/beta_S)); its endpoint jumps at beta_S. Above the seed exponent a nonzero fitted endpoint yields an explicit weighted source and velocity error, whereas below it the error is infinite. This does not exclude a fixed-source formulation or a zero-forcing endpoint.

81. [Exact temperature transport and one strain moment](81_exact_transport_and_one_strain_moment/PROOF.md): for every beta>2, smooth canonical fields satisfy exact global temperature transport, both local PDEs, all center relations, global source geometry, a nonzero slow vorticity tail and the scalar strain identity, while the vorticity PDE fails on a full annular interval. An exact polar moment formula and continuity prove the construction; these are nonprofiles.

82. [Type I and boundary-literature scope](82_typeI_and_boundary_literature/PROOF.md): center pressure diagnostics and exact parameter/source translations; several literal source descriptions corrected. No full endpoint.

83. [Finite angular support obstruction](83_finite_angular_support/PROOF.md): complete restricted proof and53 exact symbolic checks. Smooth radial-zero matching and dissipative energy exclude simultaneous finite Fourier support of stream and temperature. Actual Opus86 checked the radial ODE; lead review pending. Full combined Opus88 request returned no written audit; no full endpoint.

84. [Finite angular vorticity](84_finite_vorticity_angular_support/PROOF.md): a Fourier division lemma under symbol derivative bounds turns finite angular support of vorticity into the excluded finite stream/temperature system. Actual Opus87 checked the Fourier lemma and conditional application. No residual lower bound and no full endpoint.

85. [Fixed-envelope exponent rigidity](85_fixed_envelope_rigidity/PROOF.md): the nonzero slow tail forces beta=beta_basis for a finite polynomial endpoint representation with beta_basis in(2,4). Interpreting identical source coefficients at a different basis exponent changes the physical source even when its strain remains zero. Exact proof and independent source comparison; no full endpoint.

86. [Positive Gaussian moment diagnostic](86_positive_gaussian_moment/PROOF.md): exact positive-source inverse and conditional temperature/strain-moment formulas. Global flow and a scalar zero remain open experimental questions; no profile claim.

87. [Positive vorticity with exact transport and one strain identity](87_positive_transport_strain_construction/PROOF.md): complete nonprofile construction, independently reviewed by the lead and an additional referee; justified precision repairs adopted. A positive mode1 source dominates modes2/4; its negative-square moment is quadratic in a small parameter while the mode2/4 contribution grows linearly times log R. Continuity fixes the scalar identity with positive amplitude and a nonzero slow tail. No numerical signs or profile claim.

88. [Nonstationary homogeneous limit](88_nonstationary_homogeneous_limit/PROOF.md). Independent derivation: the second scalar far-field coefficients cannot both vanish. Under one free half-axis the second temperature coefficient itself is nonzero. Complete proof, actual Opus94/95 reviews checked; no endpoint.

89. [Exact serialized tail residuals](89_exact_serialized_tail_residuals/PROOF.md): independently derived complete formulas for first and second residual coefficients, with six exact rational endpoint/Fourier evaluations and manufactured checks completed. This can prove that a represented absolute residual is unbounded; it is a finite-representation diagnostic, not a full-class exclusion.

90. [Third tails and the determined constant velocity](90_third_terms_and_constant_velocity/PROOF.md): third scalar coefficients for every beta>2; an absolutely convergent ordinary remainder inverse fixes C for2<beta<3 and yields rigorously the fractional translation terms. Forty exact Cartesian checks and nine manufactured ordinary moments. C need not be nonzero; no endpoint. Actual Opus98/99 supplied no written audit. Lead and referee90 reviews checked; exponent-support and general-a0 precisions adopted.

91. [Beta-three logarithmic resonance](91_beta_three_logarithmic_tail/PROOF.md): the first cosine coefficient of the third vorticity tail fixes the logarithmic velocity and both fourth scalar logarithms. Full finite-order proof and 30 exact checks. Opus101/102 checked the time integration after correcting a double-counted log; actual Opus103/104 checked the inverse under packet90 hypotheses after a sign correction. Own manufactured two-power/log inverse passes. Lead and additional referee91 reviews independently checked. No nonvanishing theorem for exact profiles and no endpoint.

92. [Beta-three resonance is not forced by leading signs](92_beta_three_resonance_not_forced_by_sign/PROOF.md): exact family with positive vorticity and temperature leading data has alpha negative, zero, or positive. Nine Cartesian identities and three exact examples pass; actual Opus105 written audit checked. Exterior coefficients only, not global profiles.

93. [Stable constant of a serialized inverse](93_stable_constant_of_serialized_inverse/PROOF.md): convergent two-subtraction moment reduced to a weighted spline-second-derivative integral for2<b<3. Twenty-one manufactures and a separate high-radius inverse check pass. Positive sources can have either sign or zero constant. Source diagnostics only, no PDE or interval certificate. Actual Opus105/106 reviews checked;107 acknowledges and corrects the106 center-ODE sign typo.

94. [Annular control of the inverse constant](94_annular_control_of_inverse_constant/PROOF.md): an annular first mode shifts the constant arbitrarily while preserving the entire core, center strain and leading tails. Perturbations converge in the stated weighted norms and their weighted absolute residual changes vanish. Uniform tail positivity can be retained. Exact proof, Cartesian inverse tests and actual Opus107 review; no PDE endpoint or normalized-residual impossibility claim.

95. [Serialized beta-three logarithmic constant](95_serialized_beta_three_log_constant/PROOF.md): exact stable log-moment formula fixes C with log r normalization.21 manufactures,114 exact endpoint tests, separate high-radius inverse and actual Opus108/109 reviews. Two stored beta3 K20 states have exact nonzero resonant coefficient, excluding those representations as exact profiles. No full endpoint.

96. [Annular control with normalized residuals](96_normalized_residual_topology/PROOF.md): under explicit positive exterior F/G envelopes, the constant remains discontinuous even after adding uniform convergence of the actual and divided normalized-residual functions. Exact proof with center-corrected nonprofile,18 own FD rows, actual Opus110/111 audits. No vanishing-residual or B2 endpoint claim.

97. [Nonresonant constant and the logarithmic limit](97_nonresonant_to_log_limit/PROOF.md): the b<3 constant pole cancels its third homogeneous velocity to produce the b=3 log-r term with the required scale and angular constants. Zero-C families force alpha3=0 but not C3=0. Own full proof,45 high-precision cases, direct inverse checks and8 exact families; additional written model/lead review OPEN after actual112-114 returned no audit. Not profiles.

98. [Noninteger source constant, including3<b<4](98_constant_above_three/PROOF.md). Exact finite-part identity withN=floor(b) fullhomogeneoussubtractions; ownchecksPASS, externalwrittenreviewOPEN. Source-only, no newB2 exclusion.

99. [Noninteger missing-power constant obstruction](99_constant_gap_noninteger_beta/PROOF.md): for beta>2 noninteger and explicitly differentiated integer-ladder expansions, the canonical inverse constant must vanish. Exact exponent and Cartesian checks passed; actual Opus119 audit checked, inverse uniqueness gap filled, false parity criticism rejected. Amendment follow-up OPEN. No broad-class endpoint.

100. [Mixed-chart formulation and resonance](100_mixed_chart_verification/PROOF.md): independent direct derivation with the omitted even-resonant term; chart coverage, coordinate kernel and explicit properness counterexample. Own exact algebra and Cartesian finite-difference checks passed; additional written model review OPEN after actual Opus121 returned no text. No B2 endpoint.

101. [Native source and distinct tail powers](101_native_source_mixed_powers/PROOF.md): own complete restricted expansion for a fixed exponent-three source with3<beta<4; missing mixed powers and a simple-axis-zero obstruction. Own exact source, exponent and32 Cartesian checks passed; actual Opus122-125 exchange completed with own rejection and model withdrawal of a false source-source objection. No B2 endpoint.

102. [Exact temperature monotonicity certificates](102_exact_temperature_monotonicity/PROOF.md): rational Bernstein certificate theorem for basis exponent3; lambda.97K16 archived temperature globally positive and monotone,101 exact leaves, direct archive validation and manufactured tests passed. No PDE endpoint.

103. [Proper canonical coordinates from a certified temperature](103_proper_temperature_chart/PROOF.md): complete conditional geometric proof from uniform compactified F and derivative bounds; coordinate and optional transport construction only. Tests and model audit pending.

Packet102 now has archive-linked exact global certificates for lambda.97 and.96 K16; packet103 proper-chart theorem and numerical implementation checks CONFIRMED on2026-10-21T01:46:56Z.

104. [Exact inverse constant](104_exact_inverse_constant/PROOF.md): four archive-linked exact rational certificates prove C2<0 for the represented bfree1os3 fields;55 controls and tamper checks pass. Restricted representation exclusion only.

105. [Independent generating-function evaluator](105_independent_generating_function_evaluator/PROOF.md): direct physical Laplacian,24 polynomial controls and independent85-digit value-only residuals refute all three lead S pilots as B2/G+ candidates. Canonical inverse and global chart not checked.

106. [Positive axis compatibility](106_positive_axis_compatibility/PROOF.md): independent construction and restricted positive transport-weight audit; implementation checks pending. Does not solve the off-axis PDE.

107. [Axis-slope functional and monotonicity](107_axis_slope_functional/PROOF.md): exact center-to-infinity relation, correct increasing dependence on axial velocity, explicit unbounded-Q axis family. No off-axis profile claim.

108. [Independent canonical stream-basis solver](108_independent_stream_basis_solver/PROOF.md): new direct-stream physical trial space with gap tail powers; implementation and pilot search pending.

109. [Noninteger tail-constant topology](109_noninteger_tail_constant_topology/PROOF.md). Independent proof extends annular discontinuity of C to all fixed noninteger beta>2, including normalized residual convergence under positive envelopes. Stronger remainder control is necessary for a C-based limiting inference. Thirty-six new finite checks pass; external written review pending. No endpoint.

110. [Compactified inverse endpoint audit](110_compactified_inverse_endpoint_audit/PROOF.md): literal radial polynomial endpoints, exact slow-tail controls, dynamic normalization; implementation checks pending.

111. [Higher inverse constant certificates](111_higher_inverse_constant_certificate/PROOF.md): N-fold finite-part reduction and rational certificates; near-resonant sign diagnostic.

112. [Axis cutoff normalization](112_axis_cutoff_normalization/PROOF.md): inexact center slope, inner-cutoff Q scaling and outer-tail bias; checks pending.

113. [Referee4 exterior example and report scope](113_report_referee4_scope_audit/PROOF.md): C=0 one-equation construction and the length rescaling needed in the axis summary.

- [114. Free-beta stream chart and divided residuals](114_free_beta_stream_solver/PROOF.md): independent numerical extension of108; no endpoint claimed.

115. [Affine kernels and fractional stream tails](115_affine_kernel_and_fractional_tail/PROOF.md): complete own proof of the additional gauged affine kernel and the first constant-induced shifted-tail compatibility. Implementation/model checks pending. No endpoint.

- 116. [Fractional-tail center chart](116_fractional_tail_center_chart/PROOF.md). Read after114/115. An exact smooth coefficient chart retaining the constant vertical tail and enforcing its first fractional terms; implementation and twelve fits complete, none accepted; exact local rejection in118. No full-class exclusion. Written2026-10-21T03:25:26.876437+00:00.

117. [First nonlinear tail correction](117_first_ladder_tail_chart/PROOF.md): complete polynomial calculation and smooth center-preserving trial construction for2<beta<3, written before code. Exact implementation controls passed; twelve-state search complete, all fields rejected by lower exact local coefficients; no profile or endpoint claim.

118. [Exact local stream residual](118_exact_local_stream_residual/PROOF.md): rational Taylor coefficients of x^2,x^2y in R_Theta and x,xy in R_Omega give exact rejection certificates for serialized smooth stream fields. Proof and exact controls CONFIRMED; all twelve116fits rejected by local rational certificates. No nearby-profile exclusion.

119. [Formal center recursion and smooth flat-residual realization](119_flat_center_realization/PROOF.md). Independent proof of draft4.28, including an explicit Borel cutoff construction, preserved positive vorticity/global source, and all-orders smooth temperature; no full vorticity equation.

120. [Angular transition diagnostics](120_angular_transition_diagnostics/PROOF.md): a width and slope do not locate a jump; include crossing angles. Own K24/K32/K40 common-grid comparison and seven-point angular derivative controls CONFIRMED; finite refinement at fixed forcing only.

121. [Local and finite-axis realizations](121_local_and_finite_axis_realization/PROOF.md): exact disk, all jets on any finite segment, and the compact-exterior axis obstruction. Read after119. CONFIRMED proof and executable controls; no full profile.

122. [Whole-axis first-order realization](122_global_axis_first_order_realization/PROOF.md): positive Q, moment-balanced strip correction, canonical inverse and center Borel corrections in x^5. Read after119/121. CONFIRMED proof, exact/ODE controls and written model follow-up; no full profile.

123. [Whole-axis flat realization with an exact small disk](123_whole_axis_flat_realization/PROOF.md). CONFIRMED proof and controls with actual Opus160/161 written audits; noncompact weighted Borel extension. These exact-exterior constructions are nonprofiles by124; the full B2 problem remains open.

124. [Analytic prescribed-velocity obstruction](124_analytic_prescribed_velocity_obstruction/PROOF.md). A temperature-elimination identity is nonzero for the explicit base, ruling out both PDEs on every open set of exact agreement. Proof, exact controls and actual Opus163/164 written audits CONFIRMED. No full-class exclusion.

- 2026-10-21T04:51:17.459905+00:00: packet124 CONFIRMED, explicit analytic base incompatible with BOTH PDEs on every nonempty open set; packet123 configurations therefore REFUTED as full profiles, with construction theorem intact. Verification: 124_analytic_prescribed_velocity_obstruction/verification/SUMMARY.md.

125. [Third-order center equations with first tails](125_third_order_center_tail_chart/PROOF.md): exact six-pivot chart preserves117 tails and enforces118 transverse center conditions. Proof and exact/Jacobian/inverse controls confirmed; eighteen-state fixed/free-beta search complete; all exact lower constraints hold, every literal field rejected by independent degree4/3 rational coefficients.

126. [Arbitrary-disk anisotropic realization](126_arbitrary_disk_anisotropic_realization/PROOF.md): CONFIRMED independent proof, exact/Cartesian/inverse controls, plus fixed-exterior nonprofile proof.

127. [Prescribed disk, whole-axis flatness and smooth angular tails](127_prescribed_disk_full_axis_symbols/PROOF.md). CONFIRMED complete combined proof, exact/conic/Cartesian controls and actual Opus170/171 written follow-up audits. Fixed finite-L fields remain nonprofiles.

128. [Horizontal primitive stream reduction](128_horizontal_primitive_stream_reduction/PROOF.md): exact elimination of temperature through horizontal integration of the vorticity equation, with divided residual and analytic coefficient Jacobian. Proof, actual Opus173 audit and manufactured implementation controls CONFIRMED. Eighteen-state search complete with no candidate; all literal fields rejected by independent exact thermal jets. Six final fields also audited using physical primitive differences and a separate whole-plane inverse.

129. [Smooth angular horizontal primitive](129_horizontal_primitive_angular_compatibility/PROOF.md): Proof, actualOpus174 and independent radial/angular manufactured controls CONFIRMED. No B2 endpoint.

130. [Two exact tail moments and center-preserving repair](130_exact_primitive_tail_cancellation/PROOF.md): Informal proof, exact/Cartesian and nonlinear chart controls complete. Actual claude-opus-5-5 written review182 CONFIRMED after unsuccessful175/176/177/180 calls. Sign and scope comments independently checked. No B2 endpoint.

131. [Exact primitive center certificate](131_exact_primitive_center_certificate/PROOF.md): Proof and independent symbolic controls CONFIRMED; all eighteen primitive fields rejected exactly by rational degree-four thermal coefficients. No B2 endpoint.

132. [Triangular local primitive repair](132_primitive_local_residual_projection/PROOF.md): explicit decaying corrections annul every thermal coefficient through degree four while retaining both leading tail moments. Exact symbolic and twelve rational controls plus actual claude-opus-5-5 written review183 CONFIRMED.

133. [Axis normalization and conditional tail application](133_primitive_application_hypotheses/PROOF.md): zero-free axis propagation, a flat scalar-ODE counterexample, and integrable angular transport giving the C1 limit needed for both primitive moments to vanish. Independent proof and actual claude-opus-5-5 written reviews179/181 CONFIRMED; full stated hypotheses are essential.

134. [Joint center and tail primitive chart](134_joint_primitive_center_tail_chart/PROOF.md): exact center, degree-four thermal jets and two leading moments; controls and written Opus182/183 CONFIRMED. Eighteen-state constrained search complete, all literal fields rejected by exact degree5 thermal coefficients; all six finest horizontal offsets are nonzero. No endpoint.

135. [Exterior exactness with a prescribed disk](135_exterior_gluing_verification/PROOF.md): independent complete proof and exact algebra controls CONFIRMED, conditional on126. One fixed gluing radius gives all smooth derivatives; residual is compactly supported and nonzero by124. No global profile. Fresh Opus calls184/185 returned no written audit.

136. [Horizontal offsets of the exact primitive](136_horizontal_offset_obstruction/PROOF.md). CONFIRMED necessary condition, exact full-function coefficient certificate, independent symbolic/physical controls and two written actual Opus5.5 reviews. Three fixed final134 fields rejected despite exact leading moments and degree4 conditions. Verification/SUMMARY.md and build_inputs.json record scope and hashes.

137. [A compact residual detected without boundary terms](137_compact_residual_detector/PROOF.md): exact E=L f+M t, positive compact square for135, and a fixed-reference lower bound uniform in the gluing radius. Independent symbolic controls and written actual Opus188/189 checked. The required exact thermal equation is explicit in135;190 returned no written audit. No full endpoint.

138. [Compatibility jets determine the analytic primitive equation](138_compatibility_jet_injectivity/PROOF.md): CONFIRMED nonzero thermal jet forces nonzero E; beta>2 extension uses nonflat J and a lowest-y-power argument.272 manufactured exact cases, three stream certificates and written actual Opus193 checked. For admissible analytic streams E=0 reformulates the transport system; no existence/nonexistence theorem.

139. [Smooth local sufficiency of compatibility](139_smooth_compatibility_uniqueness/PROOF.md): CONFIRMED E=0 implies normalized primitive solves both transports locally if Psi_xxx(0)!=0. Also covers uniform Psi_xx=x^m j with j(0)!=0 and fixed finite odd m. Removable quotient and two singular scalar ODEs exclude smooth flat residuals;190 exact controls,9 flat-function points, written actual Opus196/197. No global endpoint.

140. [A compact conjugacy changes the residual moment](140_compact_conjugacy_moment/PROOF.md): CONFIRMED conditional construction preserving thermal transport, center, exterior, inverse, parity, positivity and basin. Explicit nonzero adjoint coefficient,8 exact controls and9 factored quadrature checks. First expanded quadrature failure retained; three fresh Opus5.5 requests returned no written audit. No residual-removal theorem or endpoint.

141. [A transverse-J stream cannot realize the scalar kernel](141_beta2_transverse_J_obstruction/PROOF.md): CONFIRMED local beta2 obstruction for Psi=x(b(y)-2y)+d x³y/6 with dq nonzero.21 exact identities, four polynomial controls and written actual Opus203 confirm the coefficient contradiction. Compatibility necessity is now derived self-containedly;202/204 returned no written audit. No broad endpoint.

142. [Compact residual impulse identities](142_compact_residual_impulse/PROOF.md). Exact coupled nonlinear moment identity for compact stream/temperature differences; a necessary fixed-exterior repair condition and explicit algebraic annihilators. Read after140. No value for135 impulse and no full-class exclusion.

143. [Compact thermal-preserving changes](143_compact_thermal_deformations/PROOF.md): CONFIRMED equimeasurability and exact local compact linearized Hamiltonian parametrization; 28 exact and nine nonlinear controls, actual Opus206/207 reviews. Read after142.

144. [Infinitely many polynomial adjoint moments](144_polynomial_patch_adjoint_moments/PROOF.md): CONFIRMED all-k dimension lower bound and infinite algebraic codimension for the local polynomial-patch linearized problem; affine moments are insufficient. 33 algebraic,54 exact matrix and nine counterexample controls; complete actual Opus207 audit. Read after143. No global nonlinear endpoint.

145. [Exterior residual impulse](145_exterior_residual_impulse/PROOF.md): CONFIRMED boundary identity and fixed-reference I(R)=R^(3-2s)[C_rho m1+O(R^-s)], with exact compensator handling.29 independent exact/manufactured checks pass; actualOpus210 rate review checked. Actual m1 for126 remains uncomputed; fixed-exterior necessary condition only.

146. [Compact stream sign loss](146_compact_stream_sign_loss/PROOF.md): CONFIRMED compact odd streams retaining a positive core must have negative right-half-plane vorticity. Remote restoration retains it. Three exact controls and actualOpus210 review checked. This limits the positive-vorticity interpretation, not the broad B2 class.

147. [Realized angular temperature moments](147_angular_tail_realization/PROOF.md): CONFIRMED continuous signed-vorticity family with exact thermal equation, common core and exterior stream, canonical inverse and both signs of the leading angular moment.18 manufactured controls; actualOpus227 scalar review and229 withdrawal of the wrong-reflection objection. Geometric/scattering proof independently checked; complete external review unavailable. No full B2 profile.

148. [Zero affine impulse configurations](148_zero_impulse_glued_configurations/PROOF.md): CONFIRMED conditional signed extension of135 and weak fixed-point parameter continuity. For every large R a nonprofile has exact thermal transport and nonzero compact f with all affine moments zero. Outside149's exceptional set it also has actual dipole D=0 by150. Additional model review of continuity unavailable; complete independent proof supplied. No residual repair or endpoint.

149. [Conditional renormalized impulse](149_renormalized_impulse/PROOF.md): CONFIRMED boundary finite-part identity under an explicit deep finite expansion and weighted L1 residual. Outside rational exponents with reduced denominator<=3, integral x R_Omega=2pi(1-3beta)D.184 exact controls and written actualOpus216 review checked; the expansion premise for class A was open at publication and is now established in150. Positive vorticity alone permits both signs of D.

150. [Finite exterior expansions](150_finite_exterior_expansion/PROOF.md): CONFIRMED finite full-symbol power/log expansion from the exact exterior B2 equations. Independent physical-space odd Poisson lemma, finite Euler induction,82 controls, actualOpus220/222 written review and221 partial written review. Checked36 and135 dependencies give expansions for class A profiles and compact-residual configurations. Outside reduced-denominator<=3 exponents, D=0 is necessary for a profile. No full endpoint.

151. [Renormalized energy and positivity scope](151_renormalized_energy_audit/PROOF.md). Exact disk identity with cubic flux, sufficient expansion depth, class A E_fp=0 outside denominator<=4 collisions, and positive-vorticity D=0 sign tests with zero temperature and noncompact residual.181 independent exact controls; actual Opus231/232 written reviews. No endpoint.

- 152. [Compact thermal-preserving deformations change finite-part energy](152_compact_energy_variation/PROOF.md). CONFIRMED 2026-10-21T09:59:38.274344+00:00. Exact compact-flow formula, affine moments retained, nonprofile application with nonzero energy; no endpoint.

153. [An omitted axis-pressure term](153_axis_reduction_literature_audit/PROOF.md): CONFIRMED 2026-10-21T10:11:08.627759+00:00. Direct exact full-system counterexample to arXiv2603.26715v5 Theorem2.11,37 exact controls and actualOpus235/236 written reviews. Reduced ODE lifespan and axis-only buoyancy scope corrected. Not a B2 field; no endpoint.

154. [Unbounded finite-part energy under compact twists](154_unbounded_compact_energy/PROOF.md): CONFIRMED 2026-10-21T10:23:59.814382+00:00. Exact reflected compact flow, strictly positive quadratic energy coefficient, canonical inverse and affine moments retained.9 exact controls,9 manufactured cases, actualOpus237/239 written reviews. Produces arbitrarily large positive energies in nonprofiles; no zero crossing or endpoint.

155. [Prescribed finite-part energy with the residual retained](155_arbitrary_finite_part_energy/PROOF.md): CONFIRMED 2026-10-21T10:38:11.243226+00:00. Far-annulus deformations make energy arbitrarily negative;154 then gives every prescribed real energy in148 nonprofiles with zero affine moments, same center and exterior coefficients.9 exact and9 numerical configurations pass after documented quadrature refinement. ActualOpus240/241/242 gave no written review. No endpoint.

156. [Beta-two local PDE realization with a compact equilibrium arc](156_beta2_local_pde_realization/PROOF.md): CONFIRMED 2026-10-21T10:49:37.789836+00:00. Exact both PDEs on an arbitrary prescribed disk and near the interior of the full compact zero arc, with flat endpoint data; canonical ordinary inverse and exact global thermal transport retained.17 exact and22 flow-point controls PASS. Explicit exterior residual rejects it as a profile. ActualOpus243/244 gave no written audit. No endpoint.

157. [Decaying canonical-pressure counterexample](157_decaying_canonical_pressure_counterexample/PROOF.md): CONFIRMED 2026-10-21T11:05:08.233000+00:00. Exact Gaussian pressure Hessian and an actual smooth Euler subclass refute the same closed apex equation as153 using Schwartz initial velocity and a uniquely decaying pressure.23 exact and36 full-plane Cartesian controls PASS after documented finite-difference refinement. Actual245/246 supplied no written audit. Not a B2 profile.

158. [Outgoing beta-two endpoint and residual](158_beta2_outgoing_residual/PROOF.md): CONFIRMED 2026-10-21T11:05:08.233000+00:00. Construction156 has outgoing endpoints, an open invariant backward-attracted set with nonzero vorticity, and the full interior arc identities.12 exact controls PASS. The vorticity PDE must fail on that set. No full beta2 exclusion.

159. [Nonanalytic endpoint deformation](159_nonanalytic_endpoint_deformation/PROOF.md): CONFIRMED. Compact flat Hamiltonian bends both strong unstable germs while preserving156 local equations, arc and all endpoint jets. Explicit nonzero outgoing residual, not a profile.10exact,56flows,24FD-Jacobian controlsPASS; actualOpus247/248 written reviews and resolved dependency.

160. [Exact center-strain certificates](160_exact_center_strain/PROOF.md). Full-plane angular moment and frozen-binary B-spline integral give exact rational center residuals; seven L2 scan states fail both inverse interpretations, with no fold or exponent-interval claim.

161. [Harmonic local outgoing region](161_harmonic_local_outgoing_region/PROOF.md): CONFIRMED explicit flat holomorphic perturbation with nonanalytic strong unstable curves and Omega=0 on the LOCAL outgoing side. Global thermal equation, core, arc and canonical inverse retained; vorticity equation fails in every full endpoint neighborhood and in the exterior.209 independent controls PASS; actualOpus252 written local review; broader written review unavailable. No endpoint.

162. [No terminal temperature plateau at an outgoing beta2 endpoint](162_outgoing_endpoint_plateau_obstruction/PROOF.md): CONFIRMED local obstruction from backward containment, both transports and analyticity on a full neighborhood. No global zero-set hypothesis.12 exact and60 numerical controls PASS. General nonconstant-flat terminal temperature remains OPEN; actual5.5 written review unavailable.

163. [Exact center normalized residual lower bounds](163_exact_center_residual_lower_bounds/PROOF.md):45 manufactured controls and six separate integer certificate checks PASS. All six accepted forced continuation states, beta3.088 through3.105, have exact unforced thermal normalized supremum greater than0.6327. REFUTED as literal B2 profiles; no fold or global exclusion. ActualOpus259 confirms the clarified two-target limit.

164. `164_finite_transverse_polynomial_endpoint/PROOF.md`: an outgoing beta-two endpoint is incompatible with velocity polynomial of any fixed finite degree in the physical transverse Cartesian coordinate;197 exact manufactured controls and two written actual Opus5.5 reviews. Full smooth class OPEN.

165. `165_no_automatic_quantitative_flatness/PROOF.md`: a log-square flat function has no finite Gevrey order. Exact local comparison fields show why the displayed weaker packages of endpoint hypotheses do not imply quantitative flatness; the joint full PDE/outgoing endpoint question remains OPEN.24 exact controls and23 logarithmic diagnostics PASS; a false review was corrected in an actual Opus5.5 follow-up.

166. `166_transverse_analytic_cauchy_obstruction/PROOF.md`: analytic transverse curl on a common real interval plus analytic velocity VALUE traces excludes an outgoing endpoint. Odd reflection removes the earlier Neumann trace assumption.101 exact controls+2 negative controls PASS; actual Opus267 written audit confirmed with explicit interval/divergence/orientation precision.164 is a special case.

- [167. Finite continuation diagnostics](167_finite_continuation_diagnostics/PROOF.md). Nine accepted states and23 secants on common physical grids; exact unbounded temperature difference for all36 pairs; finite samples do not prove no roots, branch continuity or a fold. CONFIRMED scoped diagnostics, OPEN branch. 2026-10-21T12:48:51.594490+00:00.

168. `168_analytic_trace_hypothesis_is_needed/PROOF.md`: explicit flat outgoing local field with constant divergence and zero curl on a common right half-rectangle, but both value traces nonanalytic. The extra value-trace assumption of166 cannot be deleted from those partial premises. Same field as161; no full B2 counterexample.38 exact controls and one negative control PASS; actual Opus273 complete written review checked.

169. [Exact spline knot regularity](169_exact_spline_knot_regularity/PROOF.md): three frozen continuation field pairs fail C5 at all55 interior axis knot points, by exact binary-rational derivative certificates and an independent value-based checker.27 manufactured functions pass. Smooth nearby fields remain possible; actual Opus5.5 review errors were corrected in follow-ups.

170. [Center hypothesis in the compatibility converse](170_compatibility_center_hypothesis/PROOF.md): the smooth local converse holds for c>-2 and fails at c=-2 without the B2 strain. Complete two-ODE argument;40 exact algebra controls and one negative control. Actual Opus5.5 found and rechecked a corrected intermediate sign. No profile-class endpoint.

171. [Independent Cartesian elliptic audit](171_independent_elliptic_residual_audit/PROOF.md): five frozen self sources,210points,3steps,2tolerances;26exact+9floating controls,328format checks,27diagnostic counterexamples. Band-max statistic does not bound local physical-vorticity error. ActualOpus285 complete audit; no candidate. 2026-10-21T13:57:03.812537+00:00.

172. [Full-plane harmonic moments](172_center_moment_inverse/PROOF.md): exact global-moment/local inverse decomposition;56exact+2floating and24additional exact controls, five frozen sources. Small local elliptic residuals are paired with distinct moment quadratures and ALL failure flags. No profile or error certificate. 2026-10-21T14:14:50.755021+00:00.

173. [Smooth arc coordinates](173_smooth_arc_coordinate_audit/PROOF.md): smooth contraction chart along an actual zero arc, area identity and exact local coupled converse.104 exact and2negative controls; actual291complete written audit. Artificial chart extension is not endpoint gluing. 2026-10-21T14:16:25.763359+00:00.

174. [endpoint unstable curve and index](174_endpoint_unstable_curve_and_index/PROOF.md): conditional local theorem. 73 exact+1negative controls; written model reviews with limitations in verification/SUMMARY.md. 2026-10-21T14:27:27.701606+00:00.

175. [odd curvature endpoint crossing](175_odd_curvature_endpoint_crossing/PROOF.md): conditional local theorem. 74 exact+2negative controls; written model reviews with limitations in verification/SUMMARY.md. 2026-10-21T14:27:27.701606+00:00.

176. [Smooth fields within the finite spline representation](176_smooth_finite_spline_counterexample/PROOF.md). Read after169. A nonzero analytic finite field refutes automatic nonsmoothness;61 exact controls and a negative control. Not a B2 profile.

177. [Incoming endpoint isothermal side](177_incoming_endpoint_isothermal_side/PROOF.md): isolated exterior zeros give an open isothermal and irrotational side; two conditional analytic exclusions.113 exact+3negative and12supplemental checks; actual306/308/310 reviews, corrections resolved. General B2 remains OPEN. 2026-10-21T15:12:58.502401+00:00.

178. [Tree, incoming sectors and flat attachments](178_incoming_tree_sectors_and_attachments/PROOF.md): CONFIRMED conditional compact tree and range theorem, individual endpoint-sector basins, analytic exclusions and hyperbolic attachment flatness.56 exact+4negative controls; actual311/312 reviews with corrections. 2026-10-21T15:24:02.157619+00:00.

179. [Strong-orbit neighborhood obstructions](179_strong_unstable_neighborhood_obstruction/PROOF.md): CONFIRMED restricted beta-two nonconstancy, irrotational-neighborhood exclusion, flat jets and global exterior-basin components.48 exact+6 negative controls; actual314/316 reviews and follow-up availability limitations documented. 2026-10-21T15:39:29.014275+00:00.

180. [Incoming arc with saddle ancestors](180_incoming_arc_with_saddle_ancestors/PROOF.md): CONFIRMED explicit smooth geometric construction with four sources and two saddles; not a B2 profile.62 exact+3 negative controls, actual320/321 reviews, follow-up availability documented. 2026-10-21T15:49:45.588076+00:00.

181. [Holder control of the inverse constant](181_holder_control_of_inverse_constant/PROOF.md): CONFIRMED sharp native regularity threshold, critical smooth counterexample and sharp quintic cell power; no numerical error or PDE endpoint inferred. Relative center jets preserved, absolute drift changes. 2026-10-21T16:08:33.571059+00:00.

182. [Beta-two three-region geometry](182_beta2_global_three_region_decomposition/PROOF.md): CONFIRMED necessary decomposition for Z=gamma, proper strong lines, simply connected basins, flat boundaries and direction arcs. No exclusion or solution. 2026-10-21T16:17:21.164380+00:00.

183. [Exact native spline comparisons](183_certified_native_spline_differences/PROOF.md): global rational norms, independent de Boor/Bernstein certificates, finite-cell inverse bound and same-parameter Nt56/Nt84/K32/tolerance comparisons. CONFIRMED finite-state claims only. 2026-10-21T16:28:30.268480+00:00.

184. [Endpoint sign and critical vorticity flux](184_beta2_endpoint_sign_and_critical_flux/PROOF.md): harmonic sign changes at smooth zero-half-arc endpoints; full/right-plane weighted moments with the retained critical flux. CONFIRMED necessary/conditional statements only. 2026-10-21T16:39:51.224312+00:00.

185. [Quasianalytic B2 exclusions](185_quasianalytic_B2_exclusions/PROOF.md): compact-interval uniqueness, local/global beta-two regularity exclusions, strict logarithmic weight and fully justified Fourier example. CONFIRMED conditional exclusions, smooth B2 OPEN. 2026-10-21T16:57:03.223205+00:00.

186. [Directional quasianalytic obstructions](186_directional_quasianalytic_obstructions/PROOF.md): generic fixed-direction transverse line germs for Theta/Omega and weak-curl exclusion for U with nonuniform linewise bounds; conditional endpoint application. CONFIRMED, fullsmoothB2 OPEN. 2026-10-21T17:09:49.364764+00:00.

187. [Full modal L2 certificates](187_full_modal_L2_certificates/PROOF.md): complete-plane G and fixed-r angular-derivative distances for four K32/K40 pairs, exact rational intervals and independent de Boor checks. CONFIRMED for specified ideal archive reconstructions; no PDE or convergence claim. 2026-10-21T17:58:34.163828+00:00.

188. [Outgoing-endpoint local reduction](188_local_outgoing_endpoint_reduction/PROOF.md): area coordinates, scalar curl equation, potential gluing and formal jets, with an explicit oriented local outgoing hypothesis. CONFIRMED conditional equivalence, no local existence and no B2 endpoint. 2026-10-21T17:55:22.934306+00:00.

189. [Physical norms and inverse constant](189_physical_norms_and_inverse_constant/PROOF.md): remote annuli, sharp weighted-L2 threshold and annular support control. CONFIRMED inverse theorem; no B2 solution. 2026-10-21T18:17:18.349801+00:00.

190. [Finite differences and curvature](190_finite_difference_curvature_audit/PROOF.md): exact three-state mismatch, sharp node propagation and derivative nonidentifiability. CONFIRMED finite facts; actual fold OPEN, NUM nondegeneracy inference REFUTED. 2026-10-21T18:26:40.412727+00:00.

191. [Physical weighted center-strain control](191_weighted_center_strain_control/PROOF.md): sufficient quantitative bound, strict power threshold and remote-annulus counterexample to unweighted G control. CONFIRMED inverse theorem, no B2 solution. 2026-10-21T18:34:48.969044+00:00.

192. [WLGB boundary literature and wall trace](192_WLGB_boundary_literature_audit/PROOF.md): L1-L5 primary-source audit, normalized trace obstruction, image-tail convergence and reflected-class uniqueness. CONFIRMED within scope, not B2 evidence. 2026-10-21T18:40:52.436712+00:00.

193. [Fresh literature search](193_recent_literature_search/PROOF.md): bounded primary-source audit, explicit unannounced-window limitation; recheck after22October00:00Z. 2026-10-21T18:54:22.777855+00:00.

195. [Interior zero arcs](195_interior_zero_arc_examples/PROOF.md): exact local families, center-preserving graph of no finite Gevrey order; no B2 admissibility or endpoint. 2026-10-21T18:58:37.087072+00:00.

194. [Stagnation samples](194_stagnation_grid_audit/PROOF.md): independent six-state inverse checks and compact inverse counterexample to sample-only global exclusion. 2026-10-21T18:59:21.358296+00:00.

196. [196_forced_tail_coefficients](196_forced_tail_coefficients/PROOF.md). CONFIRMED six stored own-ladder coefficient measurements and the corrected beta_seed/beta factor. REFUTED the implication that missing mixed powers force the observed near100percent own-coefficient mismatch. Full B2 endpoint OPEN. 2026-10-21T19:05:47.503999+00:00.

197. [197_vertex_mapscale_audit](197_vertex_mapscale_audit/PROOF.md). CONFIRMED exact serialized map-scale mismatch difference5.14958506001e-7, greater than4e-7; the printed-solve difference3.48606429057e-7 is a different quantity. Vertex/map-scale independence beyond these samples OPEN. 2026-10-21T19:05:47.503999+00:00.

198. [Spatial scaling and projected Jacobian](198_scaling_and_projected_jacobian/PROOF.md). 2026-10-21T19:21:14.667330+00:00. Exact divided scaling, fixed-source defects, projection eigenvector and finite-difference counterexample; six native-field and Cartesian full-plane inverse controls. Literal NUM scaling formula REFUTED; actual matrix OPEN.

199. [Finite separated outgoing endpoint](199_finite_separation_outgoing_endpoint/PROOF.md). 2026-10-21T19:24:02.579709+00:00. Arbitrary-coefficient finite separation exclusion in fixed endpoint coordinates; area-chart symbol and integral scope. Lead v2 K1-K6 CONFIRMED; v1 domain repaired.58exact controls; actualOpus371/373/374, disagreement resolved. Full B2 OPEN.

201. [Retied exponent derivatives](201_retied_exponent_derivatives/PROOF.md). 2026-10-21T19:45:43.556880+00:00. Physical basis derivatives, projected parameter columns, corrected finite-dimensional IFT and weighted-C0 topology. CONFIRMED restricted statements; no unseen matrix or B2 endpoint.

203. [Outgoing endpoint Gevrey audit](203_outgoing_endpoint_gevrey_audit/PROOF.md). 2026-10-21T20:04:52.029620+00:00. Lead xix v2 G1-G8 CONFIRMED; critical tangent-disk uniqueness, directional vorticity growth and nonvertical support. V1 scope repaired.57 exact controls,8191 compositions, actual384/386 reviews. Full B2 OPEN.

- P200: [projected characteristic response ](200_projected_characteristic_response/PROOF.md). Published 2026-10-21T20:19:15.397588+00:00; finite-cutoff identities and controls CONFIRMED, continuum derivative/root/B2 endpoint OPEN. [Evidence](200_projected_characteristic_response/verification/SUMMARY.md).

- P202: [moment inverse and flow sensitivity ](202_moment_inverse_and_flow_sensitivity/PROOF.md). Published 2026-10-21T20:19:15.397588+00:00; finite-cutoff identities and controls CONFIRMED, continuum derivative/root/B2 endpoint OPEN. [Evidence](202_moment_inverse_and_flow_sensitivity/verification/SUMMARY.md).

204. [Incoming endpoint extension of the local Gevrey obstruction](204_incoming_endpoint_gevrey_extension/PROOF.md). Sign-independent local theorem; B2 reflection supplies both incoming endpoints; global finite basins give a full harmonic side; candidatev3 H1-H4 CONFIRMED with actual model disagreements resolved. No general smooth exclusion.

205. [Physical Gram matrix and sharp center-strain norm](205_physical_gram_and_strain_norm/PROOF.md). Exact weighted strain bound, native integral Gram and strain row, basis-invariant singular-value reporting; independent endpoint and physical-space controls. No continuum or candidate certification.

206. [Accumulating equilibria and the full harmonic side](206_accumulating_endpoint_phase/PROOF.md). Independent center/phase construction and nearby-fast-curve barrier proof; unconditional neighborhood nonconstancy, conditional full-side harmonicity and analyticity restrictions. Candidate v2 J1-J6 confirmed with physical-coordinate regularity clarification. General smooth profiles remain open.

207. [Global saturation of constant-temperature open sets](207_global_isothermal_hull/PROOF.md). Complete global-flow proof, level-set interior invariance, support inclusion and neighborhood nonconstancy at every endpoint. Exact nonadmissible counterexample records why global backward boundedness matters. Candidate v2 K1-K3 confirmed. The v1 novelty/scope verdict was corrected; the theorem also follows from prior scattering identities.

208. [Saved Jacobian and physical sensitivity](208_saved_jacobian_audit/PROOF.md). 2026-10-21T21:32:29.183983+00:00. Stored-array algebra CONFIRMED; original dilation and neutral-ratio inference REFUTED; current scaling repair acknowledged. Finite-matrix conditioning, exact Newton counterexample and independent sampled lambda response. True derivative and full B2 OPEN.

209. [Referee17 endpoint edits](209_referee17_adoption/PROOF.md). 2026-10-21T21:32:29.183983+00:00. Candidatev1 M1-M4 CONFIRMED,35 full-preview and timeline controls. Actual entry CONFIRMED21:39. Harmonic continuation, common analytic interval, preserved hypotheses and scope.

211. [Saved Jacobian report entry](211_jacobian_report_entry/PROOF.md). 2026-10-21T21:59:58.519412+00:00. v2 Q1-Q3 CONFIRMED,33 controls. Actual entry CONFIRMED22:07 with13 controls. Explicit physical norm and corrected audit start; no exact-map claim.

210. [Independent selected-map derivatives](210_independent_jacobian_actions/PROOF.md). 2026-10-21T22:03:18.446041+00:00. Finite-cutoff identities and sampled controls CONFIRMED; exact fitting decomposition in P213; different-map gaps are not derivative-error bounds. Full B2 OPEN.

212. [Independent selected-map derivatives](212_moment_jacobian_actions/PROOF.md). 2026-10-21T22:03:18.446041+00:00. Finite-cutoff identities and sampled controls CONFIRMED; exact fitting decomposition in P213; different-map gaps are not derivative-error bounds. Full B2 OPEN.

213. [Independent selected-map derivatives](213_transport_fit_derivative_controls/PROOF.md). 2026-10-21T22:03:18.446041+00:00. Finite-cutoff identities and sampled controls CONFIRMED; exact fitting decomposition in P213; different-map gaps are not derivative-error bounds. Full B2 OPEN.

214. [Constant zero subarcs and endpoint restrictions](214_constant_subarc_audit/PROOF.md). 2026-10-21T22:14:15.190594+00:00. V2 H1-H5 CONFIRMED,39 controls, scalar integrable-forcing and triangular lemmas independently checked with actual Opus5.5 corrections. Actual entry pending; general smooth B2 OPEN.

215. [Equal-count resolution audit](215_equal_count_resolution_audit/PROOF.md). 2026-10-21T22:20:18.092485+00:00. Same-seed20-evaluation comparison independently confirmed; finite common-grid diagnostics and exact center/tail certificates reject all three literal B2 fields. No approximation floor or beta determination. [Evidence](215_equal_count_resolution_audit/verification/SUMMARY.md).

P214 actual entry update 2026-10-21T22:23:23.890281+00:00:19/19 controlsCONFIRMED, actual report3444c476 equals reviewed preview outside timeline. [Evidence](214_constant_subarc_audit/verification/actual/checks.json).

216. [Augmented matrix audit](216_augmented_matrix_audit/PROOF.md). 2026-10-21T22:24:38.263237+00:00.65/65 independent controls confirm finite arrays. Exact-root and fold assumptions distinguished; no-root counterexample. One NUM conditional requires repair. [Evidence](216_augmented_matrix_audit/verification/SUMMARY.md).

218. [Restricted separable-temperature theorem](218_separable_temperature_foliation/PROOF.md). 2026-10-21T22:39:55.351655+00:00. CONFIRMED restricted scope; [verification](218_separable_temperature_foliation/verification/SUMMARY.md). General B2 OPEN.

219. [Equal-count report entry](219_equal_count_entry_audit/PROOF.md). 2026-10-21T22:39:55.351655+00:00. CONFIRMED restricted scope; [verification](219_equal_count_entry_audit/verification/SUMMARY.md). General B2 OPEN.

217. [Three map scales](217_three_map_scale_audit/PROOF.md). 2026-10-21T22:43:39.920174+00:00. Sixliteralfieldsrefutedbyexactcenter/tail; independentcommon-grid diagnostics and history audit. [Evidence](217_three_map_scale_audit/verification/SUMMARY.md).

221. [Referee18 adoption](221_referee18_adoption_audit/PROOF.md). 2026-10-21T23:00:17.230058+00:00. Candidate S1-S4 CONFIRMED74/74; [evidence](221_referee18_adoption_audit/verification/SUMMARY.md). Actualentrypending, fullB2OPEN.

220. [Compact temperature foliation diagnostic](220_compact_foliation_manufactured/PROOF.md). 2026-10-21T23:00:57.653070+00:00. Smooth exact transport and canonical inverse with both leading center jets, but exact nonzero vorticity residual. [Evidence](220_compact_foliation_manufactured/verification/SUMMARY.md).

- [223: polynomial transport constants](223_polynomial_foliation_constant/PROOF.md). Restricted beta2 nonexistence theorem, exact nonconstant polynomial C on one regular interval;33 symbolic controls and actual Opus5.5 review437 confirmed. General smooth/constant C and full B2 OPEN.

- [224: opposite derivatives on regular temperature curves](224_foliation_constant_sign/PROOF.md). H'C'<0 necessary for global beta2 foliation;26 controls and actualOpus439 confirmed. Excludes constantC; with223 excludes all exact finite polynomials. General smoothC remains open.

222. [Separated-foliation report entry](222_separable_foliation_entry_audit/PROOF.md). Restricted transport theorems, plateau example, interval repairs, revised content and independently completed timeline proposal; source preview omission retained; actual insertion CONFIRMED23:37:09 with11controls.

226. [Supercritical separated-temperature exclusion](226_supercritical_foliation_exclusion/PROOF.md). beta>2, quadratic center jet and temperature transport force incompatible vertical and horizontal growth;34controls and actualOpus443review. General temperatures remain open.

- P225 [225_global_foliation_exclusion/PROOF.md](225_global_foliation_exclusion/PROOF.md): beta2 exclusion of every nonconstant global separated temperature with the stated regularity. CONFIRMED 2026-10-21T23:39:48.085212+00:00; critical-boundary proof, 39 exact controls, actual Opus4445.5. Full B2 remains OPEN.

- P228 [228_finite_horizontal_polynomial/PROOF.md](228_finite_horizontal_polynomial/PROOF.md): exact finite polynomial dependence on x excluded under T,divergence and isotropic sublinear velocity, all beta>0. CONFIRMED 2026-10-21T23:47:48.391625+00:00;49controls,actual Opus4465.5. General polynomial growth not excluded.

- P227 [227_lead_separable_vorticity_audit/PROOF.md](227_lead_separable_vorticity_audit/PROOF.md): beta2 arbitrary entire-axis neighbourhood representation excluded, exact53controls and35entrychecks, actualOpus447/4485.5. CONFIRMED 2026-10-21T23:52:22.389390+00:00; general B2 OPEN.

- [229. Supercritical entire-axis separated temperature](229_supercritical_neighbourhood_symbols/PROOF.md): CONFIRMED 2026-10-22T00:04:57.241018+00:00; exact(S) proof and broad-target symbol corollary,53+23controls. ActualOpus5.5 no written audit on449-452; lead review pending. Representation exclusion only.

- [230. Finite axis-derivative obstruction](230_finite_axis_jet_obstruction/PROOF.md): CONFIRMED 2026-10-22T00:13:11.191127+00:00, 81 exact controls. At beta>2 a finite family of normalized derivatives cannot all be constant when Theta_xx never vanishes. Actual Opus5.5 returned no audit; lead review pending. General B2 OPEN.

- [231. Critical finite axis ratios](231_critical_finite_axis_ratios/PROOF.md): CONFIRMED 2026-10-22T00:18:08.987142+00:00,32exactcontrols. At beta2 with nowhere-zero Theta_xx, normalized fourth and sixth derivatives cannot both be constant. Actual Opus5.5 returned no review; lead audit pending.

- [232. Restricted-representation report entry](232_restricted_representation_entry/PROOF.md): CONFIRMED v2 preview 2026-10-22T00:23:22.970826+00:00,51+13 independent controls. Required scope and timing repairs adopted. Actual insertion CONFIRMED9/9 at00:26:51.

- [P233: beta > 2 entire-axis neighbourhood report entry](233_neighbourhood_report_entry/PROOF.md). Complete proof and 61 independent insertion/scope controls; proposed4.40 and actual insertion CONFIRMED; actual9/9 checks00:35:30.

- [P235: finite-axis-jet report entry](235_finite_axis_report_entry/PROOF.md). Full proofs,92 independent insertion/scope/threshold controls; proposed4.41 and actual insertion CONFIRMED; actual9/9 checks00:47:58.

- [P237: finite axis jets on the center component](237_axis_component_extensions/PROOF.md). CONFIRMED 2026-10-22T00:54:09.746050+00:00,52 own exact controls; finite endpoint proof removes whole-axis nonvanishing at beta2 and permits unbounded proper components at beta>2. General B2 OPEN.

- [P238: extra equilibria of a signed Gaussian source](238_signed_source_axis_equilibria/PROOF.md). CONFIRMED 2026-10-22T01:01:26.533191+00:00; exact rational13/13 certificate gives one additional axis source and one saddle for the literal h4/central-negative source. Explains a center-basin obstruction for that external experiment only. General B2 OPEN.

- [P236: independent signed Gaussian source feedback](236_signed_gaussian_feedback/PROOF.md). Completed 2026-10-22T01:02:42.878903+00:00, eleven quadratures/6288 paths; weak-source bracket CONFIRMED numerically, three literal-source negative witnesses not reproduced, exact-vs-fitted discrepancy OPEN. See verification/SUMMARY.md. No unforced B2 candidate.

- [P234: lineage1 Jacobian](234_lineage1_jacobian/PROOF.md). CONFIRMED 2026-10-22T01:07:22.005501+00:00,12geometry+41matrixchecks; finite-array/full-plane geometry only. Exact derivative/root/fold/B2endpoint OPEN.

- [239. Signed-scan angular nullspace](239_signed_scan_angular_nullspace/PROOF.md): exact rank519, nullity172 of the12-angle/16-mode fits; smooth invisible perturbations change Theta_x. CONFIRMED by own73controls; numerical attributionOPEN.

- [241: actual J2 report scope audit](241_j2_report_scope/PROOF.md). Matrix rounding CONFIRMED; derivative-causality/support/actual-stationary-point interpretations need repairs. Evidence verification/SUMMARY.md and34controls.

242. [Two axis ratios for beta>2](242_two_axis_ratios_beta_gt2/PROOF.md). CONFIRMED restricted theorem on the central component, by own physical-coordinate reduction and exact integer compatibility certificate. General B2 OPEN.

243. [Axis-component report entry](243_axis_component_report_entry/PROOF.md). 4.42 v2 CONFIRMED45/45 after two explicit contradiction assumptions were added. The underlying P237 theorem is confirmed. Actual4.42 insertion independently CONFIRMED9/9 in P243.

- [244 Revised J2 diagnostics and Schur bound](244_j2_revision_and_schur/PROOF.md): finite-array checks and revisedscopeCONFIRMED, globalheaderrepairpending; actual nonlinear systemOPEN.

245. [Exact value-invisible transport manufacture](245_alias_transport_manufacture/PROOF.md): degree14 temperature perturbation preserves all12-ray samples and center jet but changes forced vorticity sign.23 exact controls and actual Opus5.5 review with corrected arithmetic. Diagnostic only.

P240 completed2026-10-22T01:44:39Z: all30240paths finish; literalGaussian K16/N12 reproduces all3negativefitted witnesses whiledirectgradienttransportpositive.36-anglefitsnotresolved; no convergenceorprofileclaim. Seeverification/SUMMARY.md.

- [242: two constant axis ratios at beta>2](242_two_axis_ratios_beta_gt2/PROOF.md). CONFIRMED on the central component, with exact physical-coordinate elimination and integer resultant certificates. General B2 OPEN.

247. [Finite-sphere gradient compatibility](247_finite_sphere_gradient/PROOF.md). ExactlocalformulasCONFIRMED; correctedGaussiantransportremainspositiveatthree negativefitwitnesses.15cases,288scalarFDpaths,34controlsandactualOpus5.5followup. NoB2endpoint.

246. [Two-ratio report entry](246_two_ratio_report_entry/PROOF.md). Version2 CONFIRMED59/59,01:43 to02:00; actualinsertionpending. UnderlyingP242theoremCONFIRMED.

- P249: [Consolidated finite-table integrity](249_consolidated_table_integrity/PROOF.md). All4560rows and roundedtables confirmed; gridheaderrefuted; 95auditentries/93distinctarchives.

248. [K40 whole-plane center, residual and tail audit](248_k40_vertex_regional/PROOF.md). Exact literal-field rejection, separately sampled residuals and finite three-resolution continuation comparisons; general B2 OPEN.

250. [Report consistency edits](250_report_block_consistency/PROOF.md). Seventeen replacements CONFIRMED158/158; t=0 small algebra and global-parity scope checked. Actual insertion pending.

251. [Two further K40 whole-plane checks](251_k40_extension_regional/PROOF.md): beta3.11/3.076 exact center rejection, infinite thermal residuals, independent regional grids and precise finite-resolution scope.

252. [Interior elliptic residual blindness with matching center jets](252_interior_elliptic_blindness/PROOF.md): compact annular source, canonical sublinear inverse, zero harmonic moments and arbitrary interior velocity error;37exact and9numerical controls.

253. [K40 inverse, geometry and endpoint diagnostics](253_k40_inverse_geometry_diagnostics/PROOF.md): separate Cartesian inverse derivatives, shifted transport grid and exact endpoint algebra; finite diagnostics confirmed, inverse-error/global-zero bounds open.

254. [Two K48 whole-plane checks](254_k48_vertex_regional/PROOF.md): independent center/tail rejection, regional residuals and four-resolution finite comparison with inherited first stage disclosed.

255. [Sublinear canonical velocity with unbounded vorticity](255_nondecaying_vorticity_transport/PROOF.md): exact beta2 thermal transport and local B2 data do not force decay; explicit global vorticity failure.
256. [Numerics integration audit](256_numerics_integration_entry/PROOF.md): independent17-edit preview and finite-data checks; v1 OPEN only repeated spread bound.

257. [No nonzero finite fourth-order axis-ratio limit](257_nonzero_axis_ratio_limit/PROOF.md): beta>2, infinite end of central axis component, no higher derivative bounds; signed normalization corrected.

258. [Restrictions on fourth-order axis-ratio tails](258_axis_ratio_tail_restrictions/PROOF.md): beta>2, power threshold q<=-1+2/beta and eventual-monotonicity zero limit; no general-class exclusion.

260. [Axis-limit report entry](260_axis_limit_report_entry/PROOF.md). Complete frozen-preview reconstruction and independent signed-axis proof; 70/70 controls, actual insertion pending.

259. [Signed weighted axis mean](259_axis_ratio_weighted_mean/PROOF.md). beta>2, infinite-end necessary condition from an exact weighted energy identity; 34/34 controls, actualOpus473 no audit text. Extended threshold is checked separately in P261.

261. [Signed axis-ratio power threshold](261_axis_ratio_power_lower_bound/PROOF.md). beta>=2, s>-1+2/beta, infinite-end weighted and pointwise necessary bounds; own61/61controls confirm leadz445 and a weighted extension.

- 262. [First-lineage K48 whole-plane audit](262_lineage1_k48_regional/PROOF.md), then verification/SUMMARY.md.

- 263. [Both signs of supercritical axis ratios](263_axis_ratio_both_signs/PROOF.md), then verification/SUMMARY.md. CONFIRMED partial theorem.

264. [Critical axis-data tails](264_critical_axis_data/PROOF.md). CONFIRMED low-order construction only,48+22 exactcontrols, actualOpus476/477adjudicated; no full B2 profile.

265. [Two-sign power report-entry audit](265_axis_power_report_entry/PROOF.md). v3 and actual adoption CONFIRMED204/204 plus18/18; mathematical theoremP263CONFIRMED.

- 266_logarithmic_critical_axis_data: complete low-order logarithmic-tail construction and62exactcontrols; own verdict CONFIRMED, A157 public review independently adjudicated; not a B2 profile. Read PROOF.md then verification/SUMMARY.md.

- 267_lineage1_k48_beta3092: accepted first-lineage K48 beta3.092, independently refuted literal B2 field. Read PROOF.md, verification/SUMMARY.md, REGIONAL_RESIDUALS.md and exact certificates.

268. [Critical tails with either sign](268_critical_axis_both_signs/PROOF.md), then verification/SUMMARY.md. Complete low-order proof,57 exact controls and fixed-A extension; full B2 remains open.

269. [Critical axis-data report entry](269_critical_axis_report_entry/PROOF.md), then verification/SUMMARY.md. Full preview and proof CONFIRMED203/203; actual4.46 adoption CONFIRMED18/18.

270. [Concave logarithmic axis tails](270_concave_logarithmic_axis_tails/PROOF.md), then verification/SUMMARY.md. Either sign at fixed A for beta>2;65 exact controls, actual Opus480VALID; class-A rate and full B2 not asserted.

271. [No positive signed quartic-ratio divergence at beta2](271_beta2_positive_ratio_divergence/PROOF.md), then verification/SUMMARY.md. Necessary infinite-end theorem,46 exact controls; own proof CONFIRMED; A157 independent proof adjudicated with8 supplemental controls; full-P271 referee pending.

272. [Quantitative critical limits of normalized axis jets](272_quantitative_axis_ratio_limits/PROOF.md), then verification/SUMMARY.md. CONFIRMED79/79 and actualOpus482/483; class-A necessary limits at every infinite end, all finite even orders.

- [273: Bounded central component for low-order axis jets](273_bounded_axis_component/PROOF.md). CONFIRMED own proof and65controls; external review OPEN. Compact flat jets with strongest axis decay, not a full-plane profile.

- [274: Logarithmic-axis report entry4.47](274_logarithmic_axis_report_entry/PROOF.md). CONFIRMED236controls, complete frozen preview independently assembled; actual adoption pending.

- P275, 2026-10-22T04:41:15.897774+00:00: [Curvature spikes and critical axis limits](275_curvature_spikes_axis_limits/PROOF.md), with91 independent controls and actual Opus485/486 adjudication. Read after P272. CONFIRMED axis theorem only; full B2 OPEN.

276. [Critical limits report entry](276_critical_limits_report_entry/PROOF.md): finite critical/all-jet limits, exact spike-width variant and complete4.48 preview audit,273 controls; one approved p_n notation correction.

277. [Backward K48 beta3.076](277_backward_k48_beta3076/PROOF.md). Four completed secants, independent residual/inverse/tail and exact certificate consumers. Finite lambda comparison confirmed; the literal state is rejected as B2.

280. [Backward K48 beta3.062](280_backward_k48_beta3062/PROOF.md). Final backward stage,48/48 independent checks, exact center/tail/C2 and regional residuals. Finite three-point lambda minimum confirmed; the literal state is rejected as B2.

278. [All axis jets with compact canonical extension](278_all_axis_jets_compact_extension/PROOF.md), then verification/SUMMARY.md. CONFIRMED93+15controls and actualOpus487/488; compact fields meet everyaxisTaylorPDE and exactinverse, yet fullthermalPDEfails. NoB2endpoint.

- [P279 num_s8 entry audit](279_numerics_integration_s8/PROOF.md):307/309; finite numbers CONFIRMED, literal acceptance wording REFUTED; entry OPEN pending three precise replacements.

281. [Actual num_s8 adoption](281_actual_num_s8_adoption/PROOF.md), then verification/SUMMARY.md. CONFIRMED57/57 for full report68a71421 and SPEC77.

P279 update: concrete corrected proposal CONFIRMED307 original successful controls plus12/12delta; actual adoption confirmed byP281.

- P282: [bounded-component entry audit](282_bounded_component_report_entry/PROOF.md), [verdict](282_bounded_component_report_entry/SUMMARY.md). 223/223; complete preview CONFIRMED with two exact wording corrections.

- P283: [exact global thermal transport with boundedJ](283_exact_thermal_bounded_axis/PROOF.md), [verdict](283_exact_thermal_bounded_axis/SUMMARY.md). CONFIRMED55/55+15/15and actual Opus492-494adjudication. Non-solutions, global vorticity PDE fails.

- P285: [Actual bounded-component adoption](285_actual_bounded_component_adoption/PROOF.md). CONFIRMED34/34; e78109ab, SPEC78,155entries.

- P284: [Numerics integration s9](284_numerics_integration_s9/PROOF.md). CONFIRMED206/206, actualOpus495VALID. Twelveedits,89states,156entries; literalprofilesstillREFUTED.

- P286: [Finite-order axis endpoint law](286_finite_order_axis_endpoint/PROOF.md), then SUMMARY.md. CONFIRMED114/114 and actualOpus496 with corrected translation. Local four-axis-equation theorem only.

- P287: [Six quadrature re-solved fields](287_quadrature_resolved_fields/PROOF.md). Pipeline pending; inherited-lambda and raw-field checks, independent full-plane residuals.

- 288_actual_num_s9_adoption: actual num_s9 adoption,24/24; one date-elision adjudicated.

- 289_infinitely_flat_axis_endpoints: four-axis-equation smooth flat examples; quartic ratio can diverge with both signs. Read after286.51exact controls; actualOpus497VALIDadjudicated.

- 290_exact_thermal_report_entry: complete4.50entry audit165/165 and actualOpus498; read after283, including its support and A164supplements. Actual adoption pending.

- P287: [six quadrature reruns](287_quadrature_resolved_fields/PROOF.md), 284 exact/data controls, independent full-plane residuals and certified literal-field obstructions.

- P291: [runtime velocity norms](291_runtime_velocity_norms/PROOF.md), independent full-plane component norms, exact-moment refinement, and conditional comparison to published runtime maxima.

- P294: [tighter quadrature secant re-solves](294_tight_quadrature_roots/PROOF.md), proof before raw independent center, whole-plane, tail and inverse-constant checks.

- P295: [actual4.50 adoption](295_actual_exact_thermal_adoption/PROOF.md), complete report and SPEC equivalence to approved P290.

- P296: [simple axis endpoints](296_simple_axis_endpoints/PROOF.md), complete extended-limit classification, local signs, curvature law and analytic finite-ratio examples; not full B2.

- [P297: actual adoption of finite-order and infinitely flat endpoint results](297_actual_axis_endpoint_adoption/PROOF.md). Complete content-equivalence proof; independent checks follow.

- [P298: complete numerical integration num_s10](298_numerics_integration_s10/PROOF.md). All eleven edits, six new fields and conditional runtime-norm claims.

299. [All extended limits at a simple local axis endpoint](299_simple_endpoint_all_limits/PROOF.md). Analytic constructions for every beta>0 and either orientation; full B2 remains open.

300. [The next vorticity jet at a simple endpoint](300_simple_endpoint_next_vorticity_jet/PROOF.md). Every P299 ratio persists through one additional analytic jet equation; no full profile claim.

301. [Runtime24/48 agreement versus full-plane norms](301_runtime_24_48_comparison/PROOF.md). Conditional scalar comparisons on the K48beta3.092field, not error enclosures.

302. [Actual numerical integration s10](302_actual_numerics_s10/PROOF.md): complete adoption24/24,95states160timelineentries.

301. [Runtime24/48 comparisons](301_runtime_24_48_comparison/PROOF.md):103controls,conditionalnormdiscrepancy andno common-error upper bound.

303. [Curved simple-end residue](303_curved_simple_endpoint_residue/PROOF.md): analytic localfour-relationexampleswithbothinfinitesigns,131ownexactcontrols;modelcompletionpending.

- P304 [Simple-endpoint complete entry](304_simple_endpoint_report_entry/PROOF.md): CONFIRMED167 controls with seven scope/wording corrections; approved complete preview.

- P306 [Curved-endpoint next vorticity jet](306_curved_endpoint_next_jet/PROOF.md): CONFIRMED own general residue proof and594 exact controls; model audit unavailable; restricted family only.

- [P308 next two curved-endpoint resonances](308_next_two_curved_resonances/PROOF.md): follows P303/P306; arbitrary-parameter proof,256+23exactcontrols, finite local jets only.
- [P309 actual 4.53 and review19](309_actual_453_review19/PROOF.md):50adoptioncontrols.

- [P311 ninth-order curvature](311_ninth_order_curvature/PROOF.md): follows P303/P306, both signs through five equations, complete proof and739controls; no global endpoint.

- [P315 actual num_s11 adoption](315_actual_numerics_s11/PROOF.md):30 controls; fdfbbb0a, SPEC85,97 states and163 timeline entries confirmed.


312. [Complete fifth-axis-relation entry](312_fifth_axis_relation_report_entry/PROOF.md): 242 controls; corrected polynomial explanation, limit scope and scalar resonance discussion. [Summary](312_fifth_axis_relation_report_entry/SUMMARY.md).

313. [123-entry consolidated residual audit](313_consolidated_123_state_audit/PROOF.md): all5904 measurements, raw-array reductions, provenance, repeated archive hashes and Q/EQ/MS scope. [Summary and header repairs](313_consolidated_123_state_audit/SUMMARY.md).

- [P316: portable residual-table inputs](316_portable_residual_package/PROOF.md), then [evidence and scoped verdict](316_portable_residual_package/SUMMARY.md).
- [P317: actual fifth-axis-relation entry](317_actual_fifth_axis_entry/PROOF.md), then [31-control adoption readback](317_actual_fifth_axis_entry/SUMMARY.md).

- [P320: external next-resonance audit adjudication](320_external_next_resonance_audit/PROOF.md), then [correction and 34 controls](320_external_next_resonance_audit/SUMMARY.md).


321. [All-order formal transverse compatibility](321_all_order_formal_resonance/PROOF.md): a nonzero generic-n triangular residue matrix yields formal analytic coefficient germs in the tuned curved family. No convergence or global profile.

319. [Complete next-two-axis entry](319_two_further_axis_entry/PROOF.md):129 controls approve the finite4.55 statement with five exact wording clarifications; actual adoption requires readback.


323. [Actual Section4.55 adoption](323_actual_two_further_axis_entry/PROOF.md). Complete approved report image and SPEC87 CONFIRMED30/30.

326. [Common axis disk for all formal coefficients](326_common_axis_disk/PROOF.md). Explicit fixed complexdisk for P321,88controls; no transverse convergence.

324. `324_nonlinear_formal_jet_checks/PROOF.md`: Finite nonlinear rational recurrences through n=10, 236/236 in the longest run; 176 source/range/precision controls. No convergence.

328. `328_leading_weighted_temperature/PROOF.md`: Leading formal temperature (C/2)r(s-kr/11)^10, with156 exact controls. No actual zero-curve claim.

325. [Complete all-order report entry](325_all_order_report_entry/PROOF.md). P321/P326 mapping and full integration audit,611controls; exact wording corrections, no transverse convergence.

330. [Numerical wording rebase](330_numerics_wording_rebase/PROOF.md).96 controls; six coupled source/report/checksum repairs prepared, actual adoption OPEN.

329. [Actual all-order entry](329_actual_all_order_entry/PROOF.md).35 controls confirm entire report03409f36 and SPEC88.

332. [Complete leading-temperature entry](332_leading_temperature_report_entry/PROOF.md). Proposed4.57 CONFIRMED1983+6 with mandatory axis scope repair; actual adoption pending.

334. [Smooth endpoint temperature factorization](334_smooth_temperature_factorization/PROOF.md). Conditional actual smooth local theorem,53 controls, flat formal-data counterexample.

336. [Complete formal factorization entry](336_formal_factorization_report_entry/PROOF.md). CONFIRMED1107plus9, exact four repairs; actual adoption remains separateP340.
338. [Complete smooth endpoint entry](338_smooth_endpoint_report_entry/PROOF.md). Proof prepared; controls and actual-base preview audit pending.

339. [Actual vorticity factorization](339_smooth_vorticity_factorization/PROOF.md). Conditional proof drafted before tests; review pending.

340. [Actual formal factorization adoption](340_actual_formal_factorization_entry/PROOF.md). CONFIRMED37 actual4.58report/SPECv90.

- P339 (2026-10-22T10:25:32.598280+00:00): [actual conditional vorticity factorization](339_smooth_vorticity_factorization/PROOF.md), CONFIRMED183 finite controls; actual smooth theorem, no profile. [Verdict](339_smooth_vorticity_factorization/SUMMARY.md).

- P338 [Complete4.59 audit](338_smooth_endpoint_report_entry/INDEX.md): CONFIRMED271+9 at2026-10-22T10:33:26.264614+00:00; actual adoptionP341OPEN.

- P341 [Actual4.59 readback](341_actual_smooth_endpoint_entry/INDEX.md): CONFIRMED42 at2026-10-22T10:35:44.814791+00:00, includingexactclockrepair.

- [335. Actual Section 4.57 adoption](335_actual_leading_temperature_entry/PROOF.md): complete proof and verification records, with scope in the packet.

- [337. Smooth temperature factorization at every simple hyperbolic endpoint](337_general_smooth_endpoint/PROOF.md): complete proof and verification records, with scope in the packet.

- [342. Complete vorticity endpoint entry and product sign](342_vorticity_factorization_report_entry/INDEX.md): complete proof and verification records, with scope in the packet.

- [343. Actual4.60 entry audit](343_actual_vorticity_endpoint_entry/INDEX.md): complete proof and verification records, with scope in the packet.

- [344. Formal vorticity factorization at the beta=2 simple endpoint](344_formal_vorticity_factorization/INDEX.md): complete proof and verification records, with scope in the packet.

- [345. Conditional summary of formal and smooth endpoint factorizations](345_summary_endpoint_entry/INDEX.md): complete proof and verification records, with scope in the packet.

- [P346: actual endpoint-summary adoption](346_actual_summary_endpoint_entry/INDEX.md): CONFIRMED 212 controls; current report and SPEC only.

- [P347 Final evidence and time accounting](347_final_evidence_and_time/INDEX.md): CONFIRMED83 finite controls; actual finalization and active time OPEN; 2026-10-22T11:14:01.849899+00:00.

- [P348 Final verifier synthesis](348_final_verifier_synthesis/INDEX.md): CONFIRMED 29740/29740 finite controls and exact identities; general B2 OPEN; 2026-10-22T11:24:32.464377+00:00.

- [P349 Numerics final time-source audit](349_numerics_final_time_source/INDEX.md): 79/79 controls; unchanged numerical content CONFIRMED, boundary/last-activity claims REFUTED for frozen source, repair OPEN; 2026-10-22T11:29:39.744822+00:00.

350. [Reading-order and counter scope audit](350_final_reading_order_audit/PROOF.md), [results](350_final_reading_order_audit/SUMMARY.md): file-link coverage, explicit inverse continuation, masked/global counters and model rebuttals.

351. [Absolute versus signed drift](351_spec_absolute_and_signed_drift/PROOF.md), [results](351_spec_absolute_and_signed_drift/SUMMARY.md): first angular moment, sign-conditional asymptotic and SPEC A5 scope repair.

353. [Actual SPEC v94 adoption](353_actual_spec_drift_clarification/PROOF.md), [results](353_actual_spec_drift_clarification/SUMMARY.md): approved A5 repair,25 controls, unchanged report.

- P352: [revised numerical final clock](352_revised_numerics_time_source/INDEX.md),224 controls, source scope confirmed with equality/display counterexamples; actual finalization OPEN.

- P356: [actual numerical clock repair](356_actual_numerics_clock_repair/INDEX.md),37 source and formatter controls; final APPLY OPEN.

- P354: [extended formal coefficients](354_extended_formal_coefficients/INDEX.md),721 controls; exact scope in proof and summary.

- P355: [euler resonance operator bounds](355_euler_resonance_operator_bounds/INDEX.md),515 controls; exact scope in proof and summary.

- P361: [euler one radius loss](361_euler_one_radius_loss/INDEX.md),991 controls; exact scope in proof and summary.

- P357: [completed finite order12 and second-width comparison](357_lower_width_formal_extension/INDEX.md),816 controls; shared range ends at order11, no convergence.



