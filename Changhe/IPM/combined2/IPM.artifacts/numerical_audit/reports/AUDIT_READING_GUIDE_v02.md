# Numerical audit reading guide

Written 2026-11-03T23:55:17.541726Z, through AN449. Supersedes version 01 as a reading guide; earlier evidence is unchanged. This is a map of completed evidence and its limits, not the campaign's final closure report. Later dated entries in AUDIT_LEDGER.md and exchange/ record subsequent results. All paths below are relative to this agent.

The fixed source C2-N1-013 has a certified small residual, but a stationary existence theorem has not been certified. The distinction is concrete: residual integration is complete, while the global background cover and the near and far operator estimates still have missing actual results. The high-regularity invariant-ball argument also needs its stated analytical hypotheses. None of those obligations can be replaced by an optimizer loss or a sampled maximum.

## 1. Exact objects and constraints

The parameter is c = 4076476460239181/2251799813685248. Candidate 007 is unchanged, with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Its 2982 generator coordinates reduce to 1922 nonzero canonical coefficients. AN-001 verifies its exact origin normalization and eleven forbidden far-field cancellations. The 1060 redundant generator directions represent zero potentials; they are not elements of a newly found PDE kernel.

Read research/candidate007/PROOF.md and its verification/structure.json, then research/reference_b18s2_audit/RESULT_PROOF.md for source 013. The latter checks the exact correction normalization ell(h) = 0 and preservation of all eleven forbidden sectors. The origin slope lies in

    (10.297367365256267279177859, 10.297367365256267279177862).

The correction's raw SHA256 is a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, its canonical SHA256 is 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33, and its accepted complete-field SHA256 is 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb. Later floating research states do not replace this source.

## 2. Complete residual integration

Let psi = partial_y chi_007 + phi_013, rho = -Delta psi, u = (-psi_xy, psi_xx), and F = (cX+u).grad rho-rho. For W(X) = sqrt(1+4|X|^2), the accepted complete-plane bounds are

    0.0000007959400186993612 <= ||F||_2 <= 0.0000007961206656880281,

    0.0035510975483434412497 <= ||WF||_(H^(21/10))
                              <= 0.0055545729030073655758.

The Sobolev norm is inhomogeneous, with the unitary Fourier convention. Cartesian derivative tensors include every ordered entry, equivalently the binomial multiplicity of each distinct multi-index. These are neither the P-S2 norm nor the prompt's weighted Holder norm S_F.

The proof proceeds through the origin disk, 114 finite radial panels and the infinite exterior. Each regional contribution has an exact source binding, containing arithmetic and an analytic remainder. The whole-plane plain L2 computation divides the weighted zeroth integrand by its positive weight using two independent analytic quotient reductions. No unobserved exterior is discarded.

Read research/source013_norms/results/whole_plane/PROOF.md together with its verification/ACTUAL_REVIEW_v01.md. The original proof records the review as pending at its writing time; the adjacent actual review discharges that later obligation. Its original fractional upper was subsequently sharpened. Read research/source013_moment_refinement_audit/PROOF.md for the improved lower, and research/source013_hermite_majorant_audit/PROOF.md for the final displayed upper, independently checked in AN317. The cubic majorant has a negative linear coefficient, so its moment bound uses the lower endpoint of the first moment for that term. Treating all coefficients as positive would invalidate the argument.

## 3. What a background record proves

The compactified radial coordinate is t = |X|^2/(1+|X|^2). The global computation partitions it into 128 roots [j/128,(j+1)/128]. Each finite angular leaf is an exact interval in z = cos(2 theta). The accepted source has 45 branches and 621400 coefficients; actual root review reconstructs the complete source and every final containing range before accepting scalar predicates.

A typical target is the conjunction

    M >= (3/5) I,  |grad h| <= 71/500,
    ||Sym Du||_op <= 137/125,

where h = -Delta phi_013 and

    M = (c+1+(cX+u).X/(1/4+|X|^2)) I
        - (21/10) Sym D(cX+u)
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].

Read research/source013_background_admission/PROOF.md, then the individual root's PROOF.md under roots/. Those local proofs retain their exact intervals and actual review evidence. A root whose gradient interval is too wide can still prove the matrix and strain components. For example, AN432 confirms both components on original root 98, 49/15 <= |X|^2 <= 99/29, while its gradient upper is 18.943174083661 and all four joint flags remain false. That upper gives no lower bound on the physical gradient.

The balanced method in research/background_balanced_replay/PROOF.md changes the fresh radial order and angular partition while preserving the exact source and original archived ranges. AN437 adopts its root 098 version 01 after a separate complete actual-source review. On 49/15 <= r^2 <= 99/29, this result proves M >= (3/5)I, strain <= 137/125 and |grad h| < 0.174273660704 < 1/4. One angular leaf leaves the smaller 71/500 gradient target unresolved. The result uses order 32 and 32 uniform angular cells; its proof is research/background_balanced_replay/roots/root_098_v01/PROOF.md. The original and balanced results have different exact records and reviews.

AN446 similarly adopts balanced root 034 version 01 on 17/47 <= r^2 <= 35/93, with order 16 and eight uniform angular cells. It proves the matrix and strain targets and |grad h| < 0.141655687509 < 71/500. Read research/background_balanced_replay/roots/root_034_v01/PROOF.md. Original roots 000 through 029 have adopted all four joint tests, covering 0 <= r^2 <= 15/49. The separate annuli do not bridge the intervening unadopted regions. Original root 030 has an independent AT review awaiting AN adoption at this cutoff; later physical records likewise need their own actual reviews.

A global bound requires an adopted selected actual result on every radial root, both complete successful original owner records, and the reviewed complete-cover assembly. The mixed consumer, admitted in AN438, permits one selected original or balanced result per root. Per-component choices from different results require a different stated and reviewed contract. Method admission alone supplies no global value.

## 4. Conditional diagnostics and incomplete computations

The scalar audits in background_capped_scalar_audit, background_capped_matrix_lower and background_capped_outer_scalars verify the arithmetic of stored original ranges. They do not independently prove field containment. Their negative matrix lowers and large gradient uppers are insufficient estimates, not counterexamples. AN435 corrects the distinction between scattered completed slabs and a contiguous radial band.

Read research/background_range_floor/PROOF.md for AN448. If the raw correlated Taylor interval is [A-E,V+E], with A <= V and E >= 0, its magnitude is at least E. The deployed method intersects this interval with an independently computed interval, then may intersect again with an old containing record. These operations can remove the raw interval floor. A checked exact counterexample demonstrates this distinction. A source-specific failure forecast must inspect those intersections; the raw floor alone does not prove failure. On the original endpoint root 127, t in [127/128,1], the implementation uses the independent range directly, without the Taylor branch or angular splitting. Zero entries in its unused Taylor-error dictionary do not mean zero uncertainty.

Read research/near_remainder_growth/PROOF.md for the complete-source diagnostic behind AN418. The actual degree-128 allowances at several larger radii decrease sharply, refuting the proposed v^22 extrapolation there. Those tested points do not give an all-panel maximum. The five near owners must finish the full 561-panel cover and its exact remainder sum must be assembled. Agreement between a floating evaluator and completed panels helps assess conditioning on those panels; it cannot bound the error on uncomputed panels or prove the final D6 target.

The far-window scalar target A_E^+ <= 1.3263305 is sufficient only with the matching weight, window and other theorem inputs. Its floating estimate is not an adopted operator bound. AN444, in research/far_band_plan_audit/PROOF.md, checks the cited finite mesh and sample records: the literal mesh contains 202 cells, and the final floating sample leaves an origin interval and a terminal interval untested. A sampled peak does not bound either gap or the values between samples. The mu 68 fallback is also not an adopted certificate merely because its audit code is prepared.

## 5. Evidence and completion

AUDIT_LEDGER.md keeps dated claims, methods, results and CONFIRMED, REFUTED or OPEN verdicts, newest last. exchange/ contains immutable numbered reports to the other agents. status file is the restart checkpoint and includes the sole active computation, if any. Exact coefficient tables, interval endpoints and candidate parameters remain in JSON; no Lean or Lake build is claimed.

Computations and reviews distinguish finite fixtures, concrete execution admission, physical execution, independent actual-result review and mathematical assembly. These stages answer different questions. A successful fixture suite does not reconstruct a field, a successful process receipt does not verify its mathematical output, and several passing local results do not cover the plane. The final theorem requires all its same-source inequalities to hold simultaneously.
