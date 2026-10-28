# Reading guide to the verified S2 results

Updated at 2026-10-28T18:14:16.287302+00:00. Current through V312. Final receipt snapshot PASS at 18:13:40 UTC.

This guide organizes the chronological verification record by question. It is not an additional theorem. Each linked `PROOF.md` gives the exact spaces, hypotheses, dependencies and argument; any adjacent `AUDIT_CLARIFICATIONS.md`, `AUDIT_ADOPTION.md` or `AUDIT_SCOPE.md` or `AUDIT_CORRECTION.md` is binding. The latest applicable entry in [VERIFICATION_RECORD.md](VERIFICATION_RECORD.md) controls status. Older statements that a later calculation is pending are historical. In particular, the residual norm is now enclosed, although the earlier conditional-existence proof predates that enclosure.

The complete topic index is [proofs/INDEX.md](proofs/INDEX.md). No proof-assistant verification is claimed. `CONFIRMED` means the analytical or computational check described by the corresponding ledger entry, with its stated scope.

## 1. Which profile and which linear operator?

Read [canonical conventions](proofs/01_operator_conventions/PROOF.md), [exact modal normalization](proofs/04_modal_scalar/PROOF.md), and [raw X3 audit](proofs/10_raw_x3_strain/PROOF.md), records V002, V005 and V018. The published raw X3 density and the exactly joined, scalar-repaired modal trial are different functions. The latter is the background of the new global theory. The exact normalization correction is defined by a scalar formula, not by choosing an interval endpoint.

The canonical signs are `U=(-R1 R2,R1^2)` and `c=psi_xy(0)=-partial_x U1(0)=partial_y U2(0)`. Unit cubic normalization gives `3 ell-c[rho]=1`. Its full variation has `delta ell=c[h]/3`. The uncancelled nonlocal term and its normalization term must be combined before asking for strong zero-jet target membership. The far exponent also varies: its derivative produces an `r^k log r` direction.

For exact rather than first-order exponent variation, continue with the [moving-tail identity](proofs/59_moving_tail_iteration/PROOF.md) and [uniform moving-tail family](proofs/167_moving_tail_uniform/PROOF.md). They define the operator `A_h` used in the closure theorem. It must not be confused with a fixed-scalar operator, the uncut formal linearization, or a projected finite-section core.

## 2. Which earlier X3 obstructions apply?

| Result | Exact scope and reading |
|---|---|
| Indefinite origin energy | [Proof 2](proofs/02_potential_energy/PROOF.md), V003 and V018. The displayed potential-energy pairing has a negative direction. This does not exclude other inverse estimates. |
| Origin quasimodes | [Proof 5](proofs/05_center_quasimodes/PROOF.md), V006 and V018. Applicable to the specified stronger center weights and realizations containing the corrected compact sequence. Not a theorem about every function space. |
| Cubic normalization is not closed in weak graph norms | [Proof 9](proofs/09_center_trace/PROOF.md), [proof 204](proofs/204_holder_graph_normalization/PROOF.md), and [proof 225](proofs/225_jet_graph_completion/PROOF.md), including V246. Adding `abs(J)` and completing creates an additional scalar coordinate; it does not identify that coordinate with a classical jet automatically. |
| Source freezing must use the actual trial | [Proof 15](proofs/15_modal_source/PROOF.md), [proof 209](proofs/209_source_transport_conjugacy/PROOF.md). A numerical source need not have the exact stationary rate `mu=1`. The rank-one term vanishes at the source point, not throughout its neighborhood. |
| High smoothness of the archived residual fails | [Proof 67](proofs/67_modal_knot_regularity/PROOF.md), V069. A certified nonzero sixth derivative jump excludes local `H^(13/2)` at the indicated knot sectors. The weaker `H^(25/4)` target remains admissible. |
| The scaling tangent is not a high-domain test | [Proof 194](proofs/194_scaling_tangent_membership/PROOF.md), V198. Even a smooth annular cutoff does not remove its relevant cofactor derivative jump. |

The old obstructions do not prove nonexistence of an exact profile. Their hypotheses, domains and target spaces are part of each statement.

## 3. Avenue I: weighted and variable-order Sobolev theory

Start with [the actual low Fredholm hypotheses](proofs/76_actual_modal_fredholm/PROOF.md), then [the high estimate](proofs/149_global_high_estimate/PROOF.md), [high Fredholm index zero](proofs/150_actual_high_fredholm/PROOF.md), and [the uniform family](proofs/167_moving_tail_uniform/PROOF.md). These give actual qualitative Fredholm theory and uniform inverses conditional on base low injectivity. The high construction has a separate scalar axis component, a variable-order bulk remainder and a `25/4` cofactor order. It is not the previously refuted uniform high-order space.

The detailed parameter choices and norm definitions are in [proof 173](proofs/173_high_low_embeddings/PROOF.md). The decoupled weight alternative is in [topics 168](proofs/168_decoupled_family_mapping/PROOF.md), [171](proofs/171_decoupled_uniform_family/PROOF.md) and [172](proofs/172_decoupled_nonlinear/PROOF.md).

Status: the specified Fredholm and conditional uniform theory is CONFIRMED. Actual base injectivity, a numerical continuum inverse norm and a certified complement inverse are OPEN. A positive coefficient margin or finite matrix singular value supplies none of these by itself.

## 4. Avenue II: local Hölder inverses and global targets

The local theory is in [topics 200](proofs/200_normalized_frozen_holder/PROOF.md), [203](proofs/203_quadratic_holder_endpoint/PROOF.md), [208](proofs/208_source_holder_l2/PROOF.md) and [210](proofs/210_variable_source_holder/PROOF.md). Read [proof 212](proofs/212_normalized_origin_cancellation/PROOF.md) for the sharp quadratic normalization cancellation and [proof 215](proofs/215_quadratic_origin_multiplier/PROOF.md) for the actual-field origin error. These are specified local or cutoff extensions, not a global inverse.

Let `E2` have the norm of [proof 213](proofs/213_common_holder_patch_space/PROOF.md): bounded supremum, horizontal alpha-Hölder seminorm and vertical alpha-Hölder seminorm divided by `x^2`, with physical parity and zero vertical-axis trace. Let `Y_gamma=E2 intersect L2((1+r^2)^(-gamma/2)dX)`.

| Target and parameters | Final established scope |
|---|---|
| `E2` and `Y_gamma`, `0<alpha<1`, `gamma>4k` | [Proof 226](proofs/226_holder_weight_extension/PROOF.md), V247: residual membership, bounded full coupling, closed maximal realizations and infinite algebraic cokernel of `T`, `Lren`, `A0`. Actual `F0` range membership is still OPEN. |
| Isotropically scaled far target `Z_sc` | [Proof 222](proofs/222_scaled_far_holder_realization/PROOF.md), [223](proofs/223_scaled_exterior_inverse/PROOF.md), [227](proofs/227_scaled_axis_range_obstruction/PROOF.md), V249: mapping and an auxiliary exterior inverse, but infinite algebraic cokernel globally. |
| Scaled quadratic-axis target `Z2` | [Proof 228](proofs/228_scaled_quadratic_axis_space/PROOF.md), V254: mapping, closedness and auxiliary exterior inverse. [Proof 234](proofs/234_divided_velocity_full_holder/PROOF.md), V265: `A0` and `Lren` are not onto when `alpha>1/2`. Their status for `alpha<=1/2` is OPEN. |
| Joint-cofactor target `Z_cof` (`Z3` in the proofs) | [Proof 236](proofs/236_joint_cofactor_holder_space/PROOF.md), V268: mapping, closed maximal domains, residual membership and auxiliary exterior inverse. The old turning-height packets do not belong to this target. Global inverses for `A0` and `Lren` are OPEN. |
| Transport alone on `Z2` and `Z_cof` | [Proof 238](proofs/238_actual_source_transport_cokernel/PROOF.md), V272: infinite algebraic cokernel for `alpha>1/A_s`, including every `alpha>=1/10` for the actual source. This is not a statement about the full coupled operators. |

The exterior inverse identities hold in the exterior region. They do not assert vanishing of the interior discrepancy. The normalization remains nonclosable in these Hölder graph topologies. The [semilinear graph obstruction on `Z_cof`](proofs/237_joint_cofactor_nonlinearity/PROOF.md), V271, and its earlier analogues do not refute the separate quasilinear iteration.

The sharp-tail refinements [proof 243](proofs/243_sharp_common_target_tail/PROOF.md) and [proof 244](proofs/244_sharp_renormalized_tail/PROOF.md) are CONFIRMED after independent audit, V286 and V287. For `E2`, the full `C0` tail norm is comparable to `R^(2k-1) log R`; for `Y_gamma` it is comparable to `R^max(2k-1,2k-gamma/2) log R`. On these same `E2` and `Y_gamma` spaces the `Cren` tail, including its restriction to exact `ker c`, is comparable to `R^(k-1) log R`. Since `C0=Cren` on that kernel, its restricted norm has the faster rate too. Constants are qualitative. Read proof 244's binding sign clarification and adoption. These are bounded coupling estimates, with no inverse conclusion. These sharp rates have not been proved in the separate `Z_cof` norm.

## 5. Avenue III: strain and finite-rank reduction

Read [proof 3](proofs/03_strain_norms/PROOF.md) for direct strain norms, [proof 7](proofs/07_local_moment_gap/PROOF.md) for the weaker-remainder obstruction, [proof 14](proofs/14_strain_adjoint/PROOF.md) for the source-local adjoint and its boundary conditions, and [proof 32](proofs/32_scalar_duality/PROOF.md) for the exact dual criterion. [Proof 230](proofs/230_strain_dual_integrability/PROOF.md) resolves the relevant integrability thresholds.

Direct boundedness of `c` in an input norm is CONFIRMED in the specified spaces. A bound of `c[h]` by an operator image has its own range or adjoint conditions. It is not a consequence of direct boundedness or of a scalar Schur complement written without domain and invertibility hypotheses. Global finite-rank reduction remains conditional on the missing complementary inverse.

## 6. Avenue IV: what is actually certified?

Read [the basis framework](proofs/12_basis_framework/PROOF.md), [the independent complement certificate](proofs/37_adjoint_complement_certificate/PROOF.md), [matrix whitening](proofs/53_gram_whitening/PROOF.md), and [the finite matrix audit](proofs/62_finite_section_matrix_certificate/PROOF.md). Exported interval matrices yield conditional finite matrix certificates until their entries are proved to enclose the exact pairings.

Input results with original-data reconstruction are [the pure-spline Gram](proofs/198_pure_spline_input_gram/PROOF.md), [the shifted outer Gram](proofs/235_shifted_outer_input/PROOF.md), and [the full 38-column Gram](proofs/239_s1j1_full_input/PROOF.md). Their exact low conformity does not imply high conformity. The pure 78-column section meets the selected high input and high graph in 66 and 60 columns, by [proof 206](proofs/206_pure_spline_high_domain/PROOF.md), V220. The shifted 38-column section meets them in dimensions 32 and 29, by [proof 240](proofs/240_s1j1_high_intersections/PROOF.md), V275.

Completed floating assemblies are independently accounted for in [proof 231](proofs/231_s1m4p_completed_input_audit/PROOF.md), V252, and [proof 242](proofs/242_s1j1_completed_audit/PROOF.md), V277. Their relative input-form comparisons are rigorous. Their output Grams, generalized singular values and model error ranges remain numerical. The images are the projected `S1` core after the exact jet split, in low norms. Restricting to high-conforming inputs does not change those norms or turn them into full `A0` images.

[Proof 245](proofs/245_conditioning_does_not_prove_artifact/PROOF.md), V279, gives an exact two-dimensional counterexample: poor Gram conditioning and disappearance of a small value after deleting columns do not prove the value spurious. [Proof 246](proofs/246_exact_strain_hyperplane/PROOF.md), V282 and V291, is CONFIRMED after independent audit. It gives exact strain-zero dimensions 37, 31 and 28 in the whole section and its two high intersections, and projection distance below `6.244e-16` from the exact binary-row kernel in each inherited LOW metric. Read its binding clarification: a computed floating nullspace basis has further errors not bounded by this theorem. No output bound is transferred without an independently bounded operator norm and certified images.

## 7. Nonlinear closure and a concrete remaining test

[Proof 174](proofs/174_conditional_existence/PROOF.md), V178, is a conditional existence theorem for the exact moving-tail chart. It assumes base low injectivity `(I)` and the specified high-radius and contraction inequalities `(S)`. A final dilation gives unit cubic normalization under the additional condition `abs(J(h))<1`. Uniqueness is only in the stated chart and ball under its extra inequality.

[Proof 177](proofs/177_high_residual_majorant/PROOF.md), V182, and [proof 187](proofs/187_fractional_difference_constant/PROOF.md), V192, now enclose the fixed high norm. [Topics 180](proofs/180_necessary_closure_test/PROOF.md), [181](proofs/181_scalar_radius_necessary_test/PROOF.md), [190](proofs/190_residual_subtracted_scalar_test/PROOF.md) and [195](proofs/195_relative_scalar_threshold/PROOF.md) provide necessary tests for `(I)` and `(S)` together, with `c[d]!=0` for the residual-subtracted tests. Their violation would refute that conjunction, hence `(S)` under `(I)`, not profile existence.

The explicit Gaussian in [proof 241](proofs/241_gaussian_strain_test/PROOF.md), V283, has `c=1`, `J=0` and belongs to the actual high graph domain. It gives exact admissible test vectors with no numerical Poisson solve. Their high norm upper bounds have not been computed. Therefore neither `(I)` nor `(S)` has been proved or disproved for the actual trial.

The corrected [local axis identity](proofs/247_axis_test_identity/PROOF.md), V296, is available inside the chart's zero-cutoff disk. Read its binding correction and adoption; the Gaussian trace is `-g''`. The [global axis extension](proofs/248_global_axis_test_identity/PROOF.md), V298/V301, retains all cutoff terms and is CONFIRMED after independent audit with its binding adoption. These are pointwise algebra, with no certified high norm.


The exact knot-jump identity in [proof 249](proofs/249_exact_knot_jump_test/PROOF.md), V302/V307, is CONFIRMED after independent audit. Read its binding [adoption](proofs/249_exact_knot_jump_test/AUDIT_ADOPTION.md). It computes a derivative-jump ratio at a certified nonzero knot, with no high-norm ratio or bound. All late theorem audits have been resolved.
