# Current theorem and evidence map

(Snapshot of the verifier's theorem map. Its links are relative to the root of the accompanying artifacts, not to this folder.)

This is the current reading guide for the independent verifier. The dated entries in the verifier's dated record (not included) retain the history, including rejected calculations and superseded candidates. Historical words such as “pending” in old notes do not override a later acceptance. The latest completely audited report is version 43 (not included), accepted in V256. It includes the improved half-exponent lower bound V239, the uniform moment estimate V247, and the local-program corrections V246/V248/V250. The live lead report may have later edits awaiting audit.

All C and D constants below refer to the real Euclidean homogeneous Holder seminorm on R^2, modulo constants, with circular principal values and the kernels in [the normalization proof](01_setup/PROOF.md). The same norm suprema are obtained on real smooth compactly supported inputs. Complex Beurling inputs are treated separately in Theorem 1.4. No theorem concerns the PDE motivating the prompt.

## Definitions and structural results

| Report location | Statement and scope | Standalone proof | Accepted checks |
|---|---|---|---|
| Section 1 | Kernels, multipliers, local identity, rotation, quotient extension and approximation | [Normalization](01_setup/PROOF.md), [approximation](02_upper_bounds/PROOF.md) | V002, V003, V011, V012, V129, V155 |
| Theorem 1.1 | Each fixed coordinate parity class has the unrestricted whole-plane norm | [Parity](14_reflection_symmetry/PROOF.md) | V091 |
| Theorem 1.2 | The full whole-plane norm is unbounded, even after output normalization by a constant | [Full norm](15_full_norm_scope/PROOF.md) | V096, V155 |
| Theorem 1.3 | Finite zero-mass transport approximation with explicit pole and exterior errors | [Finite transport](13_transport_duality/PROOF.md) | V077, V156 |
| Theorem 1.4(i) | Exact complex angular-mode seminorm and Fourier functional | [Angular modes](16_beurling_complex_norm/exact_angular_modes/PROOF.md), [radial powers](16_beurling_complex_norm/radial_power/PROOF.md) | V104, V107 |
| Theorem 1.4(ii) | Explicit complex Beurling lower and upper bounds, with B norm equal to twice the S norm | [Glued witness](16_beurling_complex_norm/glued_witness/PROOF.md), [upper bound](16_beurling_complex_norm/optimized_upper/PROOF.md) | V109, V112, V117 |
| Theorem 1.4(iii) | Strict complex-versus-real Beurling separation for every exponent | [Strict separation](16_beurling_complex_norm/strict_separation/PROOF.md) | V113 |
| Theorem 1.4(iv) | Sharp endpoint coefficients for complex inputs; only a bracket for the small-exponent second term | [Small endpoint](16_beurling_complex_norm/PROOF.md), [large endpoint](16_beurling_complex_norm/large_alpha/PROOF.md), [upper second term](16_beurling_complex_norm/upper_second_term/PROOF.md) | V098, V102, V112, V116 |
| Theorem 1.4(v) | Scalar real-kernel norms agree for real and complex inputs | [Normalization](01_setup/PROOF.md), report proof | V155 and the report change audits |
| Theorem 1.5 | Continuity in the exponent; strict gaps persist on explicitly described neighborhoods | [Continuity](13_transport_duality/exponent_continuity/PROOF.md), [explicit intervals](13_transport_duality/exponent_continuity/certified_neighborhoods/PROOF.md) | V204, V255 |
| Theorem 1.6 | A real homogeneous extremizer exists and may be odd about the increment midpoint | [Extremizers](13_transport_duality/extremizer_existence/PROOF.md) | V207 |

The untruncated infinite-variation transport shortcut in V015 was not accepted. Theorem 1.3 uses finite measures and explicit limiting errors instead. Theorem 1.6 does not assert smoothness, compact support, uniqueness or a maximizing direction.

## Upper bounds

| Report theorem | Statement and scope | Standalone proof | Accepted checks |
|---|---|---|---|
| 3.1 | Exact one-circle real functional, optimized splitting bound F and sharp endpoint coefficients | [Basic upper bounds](02_upper_bounds/PROOF.md) | V004, V005, V009 |
| 3.2; Section 10(7) | Projection pairing gives G for D, strictly below F+1/2; its cost admits a further strictly positive reduction | [Projection](08_improved_upper_bounds/local_projection/PROOF.md), [internal cycles](08_improved_upper_bounds/local_projection/internal_cycle/PROOF.md) | V033, V256 |
| 3.3 | Midpoint decomposition and harmonic exterior series | [Midpoint split](08_improved_upper_bounds/midpoint_split/PROOF.md) | V034 |
| 3.4 | Exact four-point reflection cost | [Reflection orbits](08_improved_upper_bounds/reflection_orbits/PROOF.md) | V035 theorem; V037, V040 corrected numbers |
| 3.5 | Exact-mass exterior-circle plans and explicit omitted tail | [Exterior circles](08_improved_upper_bounds/far_circle_transport/PROOF.md) | V041, V045 |
| 3.6 | Middle-circle plans, cross-disk term and balanced residual | [Middle circles](08_improved_upper_bounds/middle_circle_transport/PROOF.md), [balanced residual](08_improved_upper_bounds/middle_circle_transport/balanced_residual/PROOF.md) | V052, V054, V163, V168, V171, V179 |
| 3.7 | Paired local-circle C bound, balanced and radial residuals | [Local circles](08_improved_upper_bounds/paired_local_circles/PROOF.md), [balanced residual](08_improved_upper_bounds/local_disk_transport/balanced_residual/PROOF.md), [radial residual](08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement/PROOF.md), [finite-flow lifting](13_transport_duality/finite_flow_lifting/PROOF.md) | V243, V058, V063, V065, V070, V131, V150, V152, V159, V161 |
| 3.8 | Exact interpolation of adjacent phase bounds | [Phase interpolation](08_improved_upper_bounds/phase_interpolation/PROOF.md) | V177; cross-disk refinements V190, V219 |
| 3.9 | Radial-density quadratic and quartic savings in the positive identity remainder | [Exact radial density](08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/PROOF.md), [symmetric concavity](08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/PROOF.md), [fourth moment](08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/PROOF.md) | V195, V198, V206, V210, V220 |
| 3.10(a,b) | Optimal outer-tangent axis disks, all positive even moments and retained cutoff density | [Even moments](08_improved_upper_bounds/local_projection/strict_increment/all_even_moments/PROOF.md), [optimal disk](08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/PROOF.md) | V223, V224, V226 |
| 3.10(c) | Uniform-in-orientation density gives larger reflection savings | [Uniform density](08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/PROOF.md) | V230, V231 |
| 3.10(d) | Savings on pairwise disjoint additional disks add | [Supplemental disks](08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks/PROOF.md) | V234, V235 |

The V035 numerical implementation was retracted in V036; the analytic finite-orbit theorem was retained. No current number uses the retracted evaluation. Theorem 3.7's identity-allocation experiment remains uncertified and is not used for D. Theorems 3.9 and 3.10 give alternative savings on the same measure; they are not added to each other. Only the disjoint disk contributions within 3.10(d) are added.

The own-pole two-disk functional attains its summed angular bound exactly when cos(phi)=0. See [local phases](08_improved_upper_bounds/local_functional_audit/all_phases/PROOF.md), accepted in V253. Its quantitative phase-zero refinement remains separate and OPEN.

## Lower bounds

| Report theorem | Statement and scope | Standalone proof | Accepted checks |
|---|---|---|---|
| Lemma 4.0 | Signed distance to a closed sign-separating set gives a seminorm-one witness | [Basic lower bounds](03_lower_bounds/PROOF.md), [polygon](05_team_audit/structured_witness/PROOF.md) | V006, V018 |
| 4.1 | Explicit compact two-cusp bound | [Two cusps](03_lower_bounds/PROOF.md) | V006 |
| 4.2 | Full cusp self-integral and cross-moment correction | [Refined cusps](03_lower_bounds/two_cusp_refinement/PROOF.md) | V016 |
| 4.3 | Gated cusps | [Gated witness](03_lower_bounds/gated_witness/PROOF.md) | V017 |
| 4.4 | Cubic homogeneous witness and its exact transform modulo constants | [Degree three](03_lower_bounds/homogeneous_degree_three/PROOF.md) | V013 |
| 4.5 | Polygonal signed-distance family and rigorously enclosed full integrals | [Polygon](05_team_audit/structured_witness/PROOF.md), [layer cake](05_team_audit/structured_layercake/PROOF.md), [endpoint treatment](05_team_audit/structured_endpoints/PROOF.md) | V018, V025, V027, V032, V038, V067 |
| 4.6 | Finite projection witness, global profile factors and six small-exponent D lower bounds | [Finite witness](07_diagonal_identity_term/finite_projection_witness/PROOF.md), [geometric factor](07_diagonal_identity_term/geometric_profile_constant/PROOF.md), [full profile range](07_diagonal_identity_term/full_range_profile/PROOF.md) | V047-V049, V053, V055-V057, V064, V066, V082, V093 |
| 4.7(i) | Half-plane lattice construction with prescribed pole jump | [Half plane](11_lattice_pole_constraints/half_plane/PROOF.md), [axis reduction](11_lattice_pole_constraints/axis_reduction/PROOF.md) | V072, V076 |
| 4.7(ii,iii) | Positive axis layer-cake and sector-cusp lower bounds | [Axis layer cake](11_lattice_pole_constraints/axis_clamped_layercake/PROOF.md), [sector cusp](11_lattice_pole_constraints/axis_sector_cusp/PROOF.md) | V080, V084, V092 |
| 4.7(iv-viii) | Projection-cusp and polygon-clamp witnesses with explicit integration errors | [Positive Stieltjes rule](11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md), [polar integration audit](05_team_audit/note14_certificate/PROOF.md), [quadratic pole theorem](05_team_audit/note14_certificate/pole_profile/quadratic_lower/PROOF.md) | V089, V094, V103, V111, V121, V130, V148, V149, V164, V167, V182, V233, V237, V239 |

The strongest half- and three-quarter-exponent certificates have different replay scopes from their coarser predecessors. The next table is authoritative about those scopes.

| Exponent | Downward-rounded D lower bound | Independent verification scope | Record |
|---|---:|---|---|
| 1/2 | 2.4531232777 | Complete independent coarser-mesh replay, 1847 tasks and 13777550 cells | [V164](05_team_audit/note14_certificate/replay_fine_a50/full_quadratic/accepted.json) |
| 1/2 | 2.4542144708 | All 4019 finer producer records audited; 52 complete tasks and 1129918 cells independently replayed | [V239](05_team_audit/note14_certificate/producer_fine_a50/quadratic_recombination/accepted.json) |
| 3/4 | 2.8938332593 | Complete independent coarser-mesh replay, 1220 tasks and 27946926 cells | [V233](05_team_audit/note14_certificate/replay_fine_a75/full_quadratic/accepted.json) |
| 3/4 | 2.8948343532 | All 3961 finer producer records audited; 70 complete tasks and 2396908 cells independently replayed | [V237](05_team_audit/note14_certificate/producer_fine_a75/quadratic_recombination/accepted.json) |

## Asymptotics and uniform comparisons

| Report theorem | Statement and scope | Standalone proof | Accepted checks |
|---|---|---|---|
| 5.1 | Both real norms have small-exponent leading coefficient 2/pi | [Two cusps](03_lower_bounds/PROOF.md), [upper bound](02_upper_bounds/PROOF.md) | V005, V006 |
| 5.2 | Exact diagonal-direction finite part | [Fixed diagonal](06_small_alpha_second_term/diagonal/PROOF.md) | V020 |
| 5.3 | Uniform direction-dependent second term | [General direction](06_small_alpha_second_term/general_direction/PROOF.md) | V021 |
| 5.4 | Direction maximum and exact second term of C | [Direction maximum](06_small_alpha_second_term/direction_maximum/PROOF.md), [axis finite part](06_small_alpha_second_term/axis/PROOF.md) | V023, V029, V031, V247 |
| 5.5 | Asymmetric-cusp bracket for D's second term | [Asymmetric cusps](07_diagonal_identity_term/asymmetric_cusps/PROOF.md) | V024 |
| 5.6 | Exact second term of D | [Local profile](07_diagonal_identity_term/local_projection_profile/PROOF.md), [assembly](07_diagonal_identity_term/projection_assembly/PROOF.md), [full second term](07_diagonal_identity_term/exact_second_term/PROOF.md) | V042 conditional step closed by V043; V044 |
| 5.7 | Explicit sharp-second-term bounds and uniform linear remainder constants | [Explicit bounds](08_improved_upper_bounds/explicit_second_term/PROOF.md), [sharp deficiency](08_improved_upper_bounds/explicit_second_term/sharp_deficiency/PROOF.md), [exact tail series](08_improved_upper_bounds/explicit_second_term/tail_series/PROOF.md), [linear lower bound](06_small_alpha_second_term/linear_lower/PROOF.md), [D linear remainder](07_diagonal_identity_term/linear_remainder/PROOF.md) | V118, V123, V205, V209, V222, V225, V235 |
| 6.1 | Both real norms have large-exponent leading coefficient 3sqrt(3)/(4pi) | [Cubic witness](03_lower_bounds/homogeneous_degree_three/PROOF.md), [upper bound](02_upper_bounds/PROOF.md) | V005, V013 |
| 9.1 | Uniform endpoint comparison intervals | [Endpoint certificate](09_uniform_comparison/endpoints/PROOF.md) | V039 |
| 9.2 | Uniform comparison on the entire open exponent interval | [Finite certificate principle](09_uniform_comparison/PROOF.md), [complete nodal replay](09_uniform_comparison/lead_certificate/PROOF.md), [third pass](09_uniform_comparison/pass3/PROOF.md) | V075, V081 |
| 9.3 | Closed-form global comparison bounds | Report proof and [uniform-comparison evidence](09_uniform_comparison/PROOF.md) | V115, V124 |

## Literature and unresolved claims

The accepted primary-source statements, their exact hypotheses and their limitations are in [the source ledger](04_literature/README.md). The [closing statement audit](04_literature/final_statement_audit/PROOF.md), V244, checks report38 against twelve archived primary sources. The [local-source gate](04_literature/READ_BEFORE_LITERATURE.md) records retractions of unsupported access claims. Nolder 1987, Arsenovic-Mateljevic 2021, Rode-Simonenko and its correction, and the relevant Astala-Iwaniec-Martin book theorem remain unverified. Their titles, abstracts or contents pages do not support a theorem in this report.

The real-line and both periodic Hilbert norms also have direct proofs: [real line](04_literature/hilbert_exact/PROOF.md), [angular and chordal circle metrics](04_literature/hilbert_periodic_direct/PROOF.md), checked in V014, V157 and V196. They are one-dimensional comparison results, not two-dimensional operator formulas.

Still open: the exact finite-exponent C and D norms; whether C<D for every exponent; a uniform 5-percent comparison; the exact small-exponent second term for the complex Beurling norm; certified improvements from the joint identity-allocation experiments. Strict C<D is proved at the ten tabulated exponents and on some neighborhoods, and for all sufficiently small positive exponents. LP outputs and calibrated error forecasts are numerical observations or conditional statements, never certificates.

