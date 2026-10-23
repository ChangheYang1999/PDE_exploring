# Independent audit of EQUATIONS.md v1

Date: 2026-10-23. Source SHA256: `60b287d6d61c5182ed8da5fdedfe6ee6cd0dd51bc3a2e18cf20c1ff9939b1692`. Archived copy: `snapshots/EQUATIONS-60b287d6d61c5182.md`. This audit applies to that exact version. Later corrections need a new snapshot and an addendum.

The canonical full 3D equations and primary residual identities are confirmed. Corrections are required in sections 7.1, 7.2 and 8.5. The quantitative non-axisymmetry claim and numerical residual-floor inference are not established. The conditional countable-stagnation theorem L1 has a complete independent informal proof, but it does not cover the whole prompt class.

CONFIRMED means the stated mathematics or precisely described check has been verified. REFUTED identifies a false clause or a failed tested claim. OPEN identifies a hypothesis, implementation step or stronger inference not established here. No finite-sample test certifies exact existence.

| Section / check | Verdict | Method, result and scope | Date (UTC) |
|---|---|---|---|
| Notation | CONFIRMED | J_ij=∂_j U_i and W a=Ω×a/2 have consistent curl signs. Independent index contraction tests pass. | 2026-10-23 |
| 1.1 canonical signs | CONFIRMED | Direct differentiation of tau and y gives the stated positive collapse and stretching signs; manufactured time-dependent test passes. | 2026-10-23 |
| 1.2 axial recentering | CONFIRMED | Y=y+(C/c_l)e_z removes C; translations of the field U_h(y)=U(y-h e_z) correspond to C_h=C-c_l h. Coordinate-translation wording should specify this convention. | 2026-10-23 |
| 1.3(a) divergence identity | CONFIRMED | Independent tensor calculation gives div Rm=δ+V·∇δ+tr(J²)+ΔP. The nonzero divergence correction is essential. | 2026-10-23 |
| 1.3(b) curl identity | CONFIRMED | Independent manufactured compressible test verifies curl Rm=Rω+δΩ. | 2026-10-23 |
| 1.3(c) Bernoulli identity | CONFIRMED | Expanding Ω×V=(J-Jᵀ)V and ∇|V|²/2 reproduces Rm, including the C-dependent center. | 2026-10-23 |
| 1.3(d) vorticity maximum | CONFIRMED | Dot the vorticity equation with Ω and use ∇|Ω|²=0. Requires a nonzero interior extremum; not a normalization. | 2026-10-23 |
| 1.4 scale symmetry | CONFIRMED | Independent symbolic and numerical rescaling tests verify U_a=aU(y/a), P_a=a²P(y/a), C_a=aC. Vorticity amplitude is invariant. | 2026-10-23 |
| 2 cylindrical formulation | CONFIRMED | Angular basis differentiation produces both geometric terms. Independent physical-coordinate and cylindrical finite differences agree on off-axis tests. | 2026-10-23 |
| 3.1 Q symmetry | CONFIRMED | Proper rotation Q preserves the equations and C e_z; simultaneous transverse parity is the required symmetry. | 2026-10-23 |
| 3.2 Fourier content | CONFIRMED | Cylindrical modes are even; horizontal Cartesian components shift by ±1. Quadratic terms generate higher even frequencies. | 2026-10-23 |
| 3.3 group average and energies | CONFIRMED | Pullback R_-α U(R_α y) is correct. Independent affine average and physical-volume Parseval tests pass. At n=0, sum over ±n must count the zero mode once. | 2026-10-23 |
| 3.4 orthogonal equivalences | CONFIRMED | For O e_z=±e_z, Q commutes with O; transform C with the corresponding sign. Velocity is polar and vorticity is axial under reflections. | 2026-10-23 |
| 3.5 seed extra symmetries | CONFIRMED | The explicit seed formula transforms correctly under orthogonal matrices commuting with M, including inversion and z-reflection. These are branch restrictions unless released. | 2026-10-23 |
| 4.1 axis Taylor structure | CONFIRMED | Parity gives odd horizontal and even vertical transverse degrees. Divergence supplies the transverse trace relation; n=2 velocity can be order r. | 2026-10-23 |
| 4.2 Fourier smoothness | CONFIRMED | For smooth Cartesian fields, a scalar angular mode has r^|k| times a smooth function of r². The ±1 component shift gives the stated coupled orders. | 2026-10-23 |
| 4.3 limiting regularity | CONFIRMED | Finite smooth representations do not prove derivative convergence of a limiting profile. The listed checks are required numerical evidence, not a theorem of convergence. | 2026-10-23 |
| 5.1 symmetry projector | CONFIRMED | S²=S by Q²=I. | 2026-10-23 |
| 5.2 curl and projector | CONFIRMED | Curl commutes with the action of a proper rotation, with determinant factor for an improper one. Hence U=curl(SA) has the required properties. | 2026-10-23 |
| 5.3 envelopes and maps | CONFIRMED | The product divergence term must be kept; potential envelopes avoid it. Chain rules are with respect to physical coordinates. | 2026-10-23 |
| 5.4 representation menu | OPEN | These are proposed search branches, not validated completeness claims. A smooth network on compactified directions has integer radial Taylor increments; explicit fractional envelope families add needed powers, while flat remainders can also occur. | 2026-10-23 |
| 6.1 freedoms | CONFIRMED | No free amplitude of Ω is provided. Canonical translation alone is not a profile symmetry; C allows a coordinate recentering. | 2026-10-23 |
| 6.2 amplitude/pressure/phase gauges | OPEN | A resolved global max gives the stated scale gauge. A fixed-grid or fixed-weight surrogate requires local sensitivity and interior-resolution checks. The proposed pressure-n=2 phase gauge degenerates when that coefficient vanishes, as it does for the initial seed. No P(0) loss was found in the current numerics loss, consistent with its P∞=0 architecture. | 2026-10-23 |
| 6.3 invariant derivatives | CONFIRMED | J(0) and the sup of Ω are invariant under spatial scaling. Higher derivatives of J scale as a^-k and should not be called invariant without that qualification. | 2026-10-23 |
| 7.1 exact affine family, scalar factor clause | REFUTED | The displayed M works at its stated scale, but not up to an arbitrary overall factor: skew(tM+t²M²)=(t-t²)skew M. The family is sufficient, not exhaustive of Q-equivariant affine solutions. | 2026-10-23 |
| 7.2 rejection list, force interpretation | REFUTED | The exclusions are appropriate for the target, but a constant velocity with the displayed linear pressure is an exact unforced Euler solution. Reject it for nondecay and zero vorticity, not for adding a body force. | 2026-10-23 |
| 7.3 diagnostic requirements | CONFIRMED | The required distinctions are mathematically appropriate. Check completion separately; no diagnostic list proves the properties automatically. | 2026-10-23 |
| 8.1 natural degrees | CONFIRMED | The homogeneous multiplier vanishes at d=1-1/c_l, giving all stated exponent ranges. This is an assumed matching class, not an exhaustive theorem. | 2026-10-23 |
| 8.2 leading divergence | CONFIRMED | Spherical divergence gives div_S A_T+(d+2)A_r=0; integrate over S² and use d+2≠0. | 2026-10-23 |
| 8.3 nonlinear correction multiplier | CONFIRMED | At degree 2d-1 the multiplier is -1. The formal cascade is a possible hierarchy; an arbitrary exact tail expansion is not proved to contain only those powers. | 2026-10-23 |
| 8.3 monopole/dipole cancellation | CONFIRMED | With the stated derivative decay and d<-1, f=∂i∂j(U_i U_j) has zero total mass and first moments by integration by parts. Both boundary terms for the first moment are O(R^(2d+2)). Decay of U alone without derivative control is insufficient for this argument. | 2026-10-23 |
| 8.4 finite-energy interpretation | CONFIRMED | The core exponent is 5c_l-2. For a nonzero angular leading tail the fixed-ball power of tau cancels, local L² requires d>-3/2, and the profile itself need not lie in L² at infinity. Strong matching is an additional hypothesis. | 2026-10-23 |
| 8.5 Chae attribution | REFUTED | Chae math/0601060v2, Theorem 1.1, assumes Ω∈L^p for every p in (0,p1), not one p below 3c_l. The paper’s abstract must not replace its theorem hypotheses. Natural nonzero Ω~R^(-1/c_l) is in L^p at infinity only for p>3c_l. One-p exclusion under extra assumptions needs a separate proof/source. | 2026-10-23 |
| 8.6 Newtonian pressure and Biot-Savart | CONFIRMED | With regularity and natural derivative decay, the integrals and signs are justified in research/whole-space-integrals/PROOF.md. Finite-radius quadrature with no analytic tail bound remains a numerical consistency check. | 2026-10-23 |
| 9.1 R3 Theorems 2.1, 3.4, 3.8, 3.9, 4.5 | CONFIRMED | Primary v3 checked. Keep finite-energy plus gradient-growth hypotheses for 2.1; p>max(3c_l,1) for 3.4; nonzero Ω and local outgoing at a zero for 3.8; decay, normalization and finite nodal set in Definition 3.7 for 3.9; axisymmetry and (3.5),(3.8) for 4.5. | 2026-10-23 |
| 9.1 quantitative O(1) n=2 consequence | OPEN | The axisymmetric theorem does not supply a quantitative lower bound on non-axisymmetric energy. Remove this purported consequence or prove a normalized compactness estimate. The prompt asks for a resolved nonzero n=2 signal. | 2026-10-23 |
| 9.2 axis and off-axis local checks | CONFIRMED | At a zero with Ω≠0, JΩ=SΩ=Ω; trace then gives the stated incoming direction and eigenvalue sum. It is conditional and must not be imposed when Ω=0. | 2026-10-23 |
| 9.3 L1, exact conditional theorem | CONFIRMED | Complete independent proof, including the local null-graph lemma, in research/stagnation-obstruction/PROOF.md. The C² decaying countable-stagnation class is excluded below one half. | 2026-10-23 |
| 9.3 numerical residual-floor interpretation | OPEN | A finite root search does not certify countability or exhaust all zeros. No universal quantitative residual floor follows without global compactness and stagnation-structure control. | 2026-10-23 |
| 9.4 peak identity | CONFIRMED | Same statement as 1.3(d). A numerically refined local extremum is not a global maximum certificate. | 2026-10-23 |
| 10 seed algebra and degrees | CONFIRMED | Independent curl derivation and symbolic/numerical tests agree. The displayed cylindrical n=2 formula is for the affine core M y; the localized seed has additional radial factors. Its generic tail is asymptotic, not exactly homogeneous at finite radius. | 2026-10-23 |
| 10 seed as Euler profile | REFUTED | Correctly labeled initializer in the lead file. Direct tests find momentum, vorticity and pressure defects. Its R^(d-2) correction generally fails nonlinear tail balance below one half. | 2026-10-23 |
| 11 residual metrics | CONFIRMED | The termwise L² denominator is well defined away from degeneracy. Use physical weights for physical norms. Quantiles/maxima stay sampled quantities. Proposed numeric thresholds are screening choices. | 2026-10-23 |
| 12 Navier-Stokes scaling | CONFIRMED | The viscosity coefficient is nu exp[-(1-2c_l)s]. Decay of that coefficient alone establishes no NS singularity. | 2026-10-23 |
| 13 validation tests | OPEN | The independent test suite and synthetic decoder checks pass. Cross-implementation tests are still partial and must be attached to actual checkpoint/source hashes. Numerics test results are its responsibility. | 2026-10-23 |


## Revision v1.1 audit

Observed UTC: 2026-10-23T06:42:08.371108+00:00. Snapshot SHA256 `4761bdd6b77349b797a86b4e8d7d507d85c00fbcdf34c45a9bcf8e7bac2dd770`. The file declares 06:45Z, later than its observed 06:33Z modification; this audit uses the system observation time and content hash, not the manually entered version clock.

The repaired matrix classification, constant-solution interpretation, Chae quantifier, and n=2 wording are confirmed at their stated scope. Pressure gauge options are now explicit; the numerical amplitude and phase degeneracies remain open. The full current ledger is evidence/equations_audit_current.json.

New correction: a smooth nonzero leading homogeneous tail of the natural degree cannot be irrotational. See research/irrotational-leading-tail/PROOF.md for the separate angular harmonic argument. This is not an application of Chae and does not rule out a vortical leading tail.

The countable-stagnation theorem extends from decaying U to uniformly sublinear U=o(R), yielding constant U. The independent proof addendum also confirms L1' for alpha-limit sets avoiding E. The report must retain countability or the alpha-limit hypothesis and cannot infer an unconditional residual floor from finite root finding.

## Full v1.3 re-audit and snapshot provenance correction

Observed UTC: 2026-10-23T06:59:45.079216+00:00. SHA256 `c291a875a063cb26b6235d55b94a424fbc76286e5a9172048f0f00d1a3544c10`. The complete byte snapshot was read again, including the additions in sections 3, 6, 8, 9, 10 and 14. The current full ledger is `evidence/equations_audit_current.json`.

The previous snapshot `4761bdd6b77349b7` has the correct hash, separate inode and link count one. It declares v1.2, not v1.1. Earlier prose mislabeled it and carried an obsolete irrotational-tail remark into that snapshot audit. No snapshot content changed. The historic JSON is preserved, and the current ledger corrects those attributions. Manually entered version times are not measurement evidence.

The principal equations, L1 theorem, revised multipole bounds, irrotational-tail exclusion and meridional swirl theorem are confirmed with the listed hypotheses. Remaining literal errors are the old spectral parentheticals in 7.2 and the missing nontrivial qualifier in the 9.3 consequence. The proposed compactness inference remains conditional until its topology, pressure and normalization controls are specified.
