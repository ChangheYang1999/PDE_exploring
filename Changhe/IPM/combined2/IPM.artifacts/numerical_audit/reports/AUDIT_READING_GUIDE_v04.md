# Numerical audit reading guide, version 4

Frozen 2026-11-04T09:52:54.730946+00:00 for X11, through AN741. Later results belong to later dated entries in AUDIT_LEDGER.md and exchange/. The guide is a map of evidence, not an additional numerical certificate.

The fixed source C2-N1-013 has a rigorously enclosed small residual. A stationary existence theorem has not been certified. The difference lies in the remaining hypotheses: the background estimates still have an uncovered region, the complete near estimate is being assembled, the H4 remainder has unbounded terms, and the full inverse and high-regularity invariant ball require their separate analytical arguments. None of these conditions follows from the optimizer's loss.

All numerical conclusions retain the exact-source and containing-arithmetic hypotheses stated in their cited proofs. The interval calculations use exact rational data and Arb enclosures. They are not Lean-verified, and a matching file hash establishes identity rather than mathematical containment.

## 1. Which function was checked

The parameter is fixed at

    c = 4076476460239181/2251799813685248.

The authoritative Candidate 007 has SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. The [exact reference proof](../research/candidate007/PROOF.md) and its [structural record](../research/candidate007/verification/structure.json) check the origin normalization and all eleven forbidden far-field sectors. Its 2982 generator coordinates reduce to 1922 nonzero canonical coefficients. The 1060 redundant directions represent zero potentials, not a newly established kernel of the PDE.

Source 013 adds the exact correction phi_013 while preserving the correction constraint ell(-Delta phi_013)=0 and those eleven cancellations. Its identifiers are:

| Object | SHA256 |
| --- | --- |
| Raw correction | a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a |
| Canonical correction | 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33 |
| Complete field record | 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb |

The [source 013 result](../research/reference_b18s2_audit/RESULT_PROOF.md) gives the exact structural checks. Later floating experiments are distinct objects unless an explicit identity check relates their exports. One such check, [b28 versus b29](../research/b28_b29_exact_identity/RESULT_PROOF.md), proves equality of all 18385 nonzero exported atoms and conventions. The extra 512 basis slots in b29 do not change the exported function. That equality says nothing by itself about optimizer rank, rejected steps or loss accuracy.

## 2. What the residual certificates establish

Write

    psi = partial_y chi_007 + phi_013,
    rho = -Delta psi,  u = (-psi_xy, psi_xx),
    F = (cX+u).grad rho - rho,  W(X) = sqrt(1+4|X|^2).

The completed whole-plane bounds for source 013 are

    7.959400186993612e-7 <= ||F||_2 <= 7.961206656880281e-7,

    0.0035510975483434412497 <= ||WF||_(H^(21/10))
                              <= 0.0055545729030073655758.

The second norm is the inhomogeneous P-S1 Sobolev norm with the unitary Fourier convention. Ordered Cartesian derivative tensors include every entry, equivalently the binomial multiplicity of each distinct multi-index. The upper bound proves a 0.006 target. The interval does not decide a 0.0055 target. Neither statement evaluates the P-S2 norm or the prompt's weighted Holder norm S_F.

The [whole-plane proof](../research/source013_norms/results/whole_plane/PROOF.md) sums an origin region, 114 finite panels and the full infinite exterior. Its [actual review](../research/source013_norms/results/whole_plane/verification/ACTUAL_REVIEW_v01.md) discharges the execution and review obligations that were still pending when the proof was written. The [moment refinement](../research/source013_moment_refinement_audit/PROOF.md) improves the fractional lower bound. The [Hermite majorant](../research/source013_hermite_majorant_audit/PROOF.md) gives the displayed upper. Because that majorant has a negative linear coefficient, it must use a lower endpoint for the corresponding first moment. Substituting an upper endpoint there would reverse the required inequality.

For comparison, the original reference calculation enclosed

    0.3766893247058942619446457 < ||F_007||_2
                               < 0.3766893247058942619446458.

That reference calculation includes all 160 positive odd angular modes through 319 and uses analytic whole-plane radial integration. Its [2048-bit moment record](../research/candidate007/verification/moments_2048.json) remains available. The large derived reference expansion was retired under [the recorded reference-retention policy](../storage/COMPLETED_REFERENCE_RETENTION_V04.md); replaying that construction requires regeneration from the retained exact input and code. The small residual of source 013 is a statement about a different, explicitly corrected reference, not a modification of Candidate 007's authoritative file.

## 3. How local background bounds become a cover

Put h=-Delta phi_013 and

    M = (c+1+(cX+u).X/(1/4+|X|^2)) I
        - (21/10) Sym D(cX+u)
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].

The latest executed and independently reviewed union contains 91 original radial indices. Under its stated source and containment hypotheses it proves, at every angle,

    M >= (3/5) I,  |grad h| <= 1/4,  ||Sym Du||_op <= 137/125
    on r^2 in [0,61/67] union [49/15,infinity).

Its single open gap is (61/67,49/15), comprising indices 061 through 097. This is a missing certificate, not evidence of a violated inequality. The stronger gradient target 71/500 has 87 indices and four open gaps:

    (61/67,99/29), (25/7,101/27),
    (51/13,103/25), (13/3,105/23).

Read the [progressive union proof](../research/background_progressive_union/PROOF.md), its [m=60 result](../research/background_progressive_union/verification/check_v03.json), and the [actual adoption](../research/background_progressive_union/verification/actual_review_v03.json). The weak-target union selects indices 0 through 60 and 98 through 127. The compactification t=r^2/(1+r^2) turns each finite root into [j/128,(j+1)/128]. A union check authenticates the selected local theorems and checks their exact endpoints. It does not rerun a field evaluator.

Retained interval data also prove stronger regional matrix bounds:

| Squared-radius region | Certified matrix lower |
| --- | --- |
| [0,61/67] | M >= (704955805507/10^12) I |
| [49/15,infinity) | M >= (761272835221/10^12) I |

The [matrix argument](../research/background_matrix_margin_recount/PROOF_v02.md) replaces each diagonal by its lower endpoint, bounds the off-diagonal square from above, and rounds the resulting smaller eigenvalue downward using exact integer square comparisons. It checks the sign when dividing by d0: a negative numerator uses the lower denominator, while a nonnegative numerator uses the upper denominator. This is a bound on every point in each containing cell. It is not the smallest value observed on a mesh.

The inner result combines the [sixty ordinary-root adoption](../research/background_matrix_margin_recount/verification/actual_review_v01.json) with the [balanced-root adoption](../research/background_matrix_margin_recount/verification/actual_balanced_review_v02.json), which supplies the missing index 034. The outer result combines [39 recounted rectangular regions](../research/background_matrix_margin_recount/results/rectangular_v01/PROOF.md) with five balanced roots; its [actual adoption](../research/background_matrix_margin_recount/verification/actual_rectangular_review_v01.json) confirms the complete exterior. These stronger matrix bounds leave the gradient and strain bounds unchanged.

The [original exterior theorem](../research/background_exterior_union/PROOF.md) also gives |grad h|<=899/10000, strain<350541070259/10^12, and d0^2 det(M-(3/5)I)>=949/20000 for r^2>=127, where d0=(1+3t)/4. The formal endpoint t=1 is not a spatial point.

The independent source calculation for ordinary roots 97 down to 56 completed in the second numerics agent on core 49 at 09:31:39.907812Z on November 4, after 2372.995782851707 measured seconds. Its [exact request](../research/ordinary_host_request/verification/request_v01.json) and [request adoption](../research/ordinary_host_request/verification/request_adoption_v01.json) require all 42 roots and a successful resource guard. The complete [host receipt](../../numerics_agent_2/source_host_049/ordinary_v01/execution_v01.json) satisfies that execution condition, and AT2471 to AT2473 authenticate all 84 coefficient and cell archives. The separate [exact field recount](../research/ordinary_slabs_host_method/verification/recount_v01.json) completed at 09:47:18Z, with 12108987 checks of all 344064 cells and every stored coefficient interval and branch-tail record. All four exact predicates pass on every root. Its distinct actual review is still pending at this cutoff. The admitted [matrix adapter](../research/ordinary_host_matrix_margin/PROOF.md) completed at 09:51:32Z, after 82.71866334369406 measured seconds, and gives M >= (890672299617/10^12) I throughout the host region. Its [result](../research/ordinary_host_matrix_margin/verification/check_v01.json) still requires distinct actual review. If the two host results are adopted and the complete union is independently reviewed, the whole-plane matrix lower will be the inner value 704955805507/10^12. No host inequality has entered the regional bounds above. The [complete-union theorem](../research/background_complete_union/PROOF.md) explains precisely how these remaining premises would fill the gap and why the stronger gradient mask would still omit indices 98, 100, 102 and 104.

## 4. The near and far estimates have different evidence chains

The [far Schur assembly](../research/far_cs_b_updated_assembly/PROOF.md) and [independent window calculation](../research/far_window_updated_audit/PROOF.md) supply the far numerical inputs. The latter independently reconstructs all 5120 window cells using its own Bell recurrence and radial integration, while importing the explicitly cited containing derivative and kernel intervals. It is not a second full reconstruction of those imported intervals.

At strain 137/125 the recorded far margin is

    71675071190082633/5629499534213120000.

Non-strict absorption permits strain up to and including 4963249980622857/4503599627370496; positive slack requires a strict inequality. These conclusions still need the matching whole-plane strain premise and the other analytical hypotheses. A far margin does not supply the near estimate or the full inverse.

The near coefficient is

    a_n(X) = (4u(X).X-c)/(1+4|X|^2) * erfc(log(|X|/sqrt(8))/L)/2,
    L = log(8)/(2sqrt(pi)),  a_n(0) = -c.

Its calculation uses 561 annular panels between radii 1/4096 and 10000, together with an origin disk and the full infinite exterior. Every original owner has a disjoint residue class of panel indices. Its successful complete receipt is required before any of its panels can enter the independent chunk review. The [chunk theorem](../research/source013_near_admission/CHUNK_PROOF_v01.md) requires a complete-source majorant replay, coefficient and energy checks, an actual independent review and an adopted result. All chunks are then assembled into the owner's block.

N4 is complete and adopted. Its 112 panels, with indices 4,9,...,559, form fourteen disjoint chunks. Their regional Laplacian energy sums satisfy

    E4 in [39461,39462],
    E5 in [3505225,3505226],
    E6 in [803311347,803311348].

The [standalone N4 result](../research/source013_near_admission/results/block_n4_v02/PROOF.md) states the exact source and containment hypotheses. Its [actual adoption](../research/source013_near_admission/verification/block_n4_v02/actual_review_v01.json) binds the complete chain of owner, chunk and reduction evidence. These are sums of the squared norms of Delta^2 a_n, grad Delta^2 a_n and Delta^3 a_n on this residue-class annulus union. They are not Cartesian tensor energies on that region.

N3 completed its original 112-panel calculation at 09:16:54.452570Z on November 4. Its fourteen concrete chunk requests are independently bound by AT2452 to AT2455 and adopted. The first two physical chunks finished at 09:39:41Z and 09:41:13Z. AT2499 to AT2504 independently confirm their actual energy records; [chunk 00](../research/source013_near_admission/verification/chunk_n3_00_v02/actual_review_v01.json) and [chunk 01](../research/source013_near_admission/verification/chunk_n3_01_v02/actual_review_v01.json) are adopted, while the remaining twelve chunk calculations are still pending at this cutoff. N1, N2 and N0 completed at 09:25:56.948997Z, 09:27:28.081340Z and 09:29:34.841690Z, respectively. Their 43 concrete chunk requests are frozen and independently bound by AT2481 to AT2492; local request adoptions and actual calculations are pending. All 561 original panels now have complete owner receipts, but that fact alone supplies no admitted whole-plane derivative bound.

The first N4 attempt failed when its archive check compared integer dictionary keys with their JSON string representations. Its numerical panel record was retained, but that failed request supplied no admitted chunk. The [version 2 repair](../research/source013_near_admission/ARCHIVE_REPAIR_PROOF_v02.md) checks exact decompressed JSON bytes and leaves the numerical majorant unchanged. Every adopted chunk passed a fresh complete request under the repaired method.

The [whole-plane near proof](../research/source013_near_norms/PROOF.md) explains why all five blocks and both endpoint certificates are needed. After summing all regional Laplacian energies, a whole-plane identity gives the ordered Cartesian derivative norms D4, D5 and D6. It also gives containing Fourier-moment inputs by exact power comparisons. An individual annular energy cannot be relabelled as a Cartesian tensor energy on that annulus. The [version 2 consumer migration](../research/source013_near_norms/CHUNK_MIGRATION_PROOF_v04.md) has an admitted method, but its whole-plane execution still requires the remaining complete blocks.

## 5. The rate budget still needs all its terms

The H4 composition uses the near loss and remainder together:

    e_up + eps_rest <= beta_star - b0.

Here beta_star must be a matrix lower on the whole plane for this source, e_up must be the upper obtained from the actual near inputs, and eps_rest must bound the other H4 terms. A cap-level comparison e_up <= c+1-q-b0 is only a necessary preliminary test. It does not supply the matrix lower or remove the remainder.

The origin already forces Lambda_+(a_n)>=8(2c-1)=2950576553396557/140737488355328. The [exact Hessian proof](../../theory_audit/research/lambda_target_incompatibility_audit/PROOF.md) uses the normalized velocity jet and the flatness of the erflog cutoff at zero. This lower exceeds the old FLOAT target 20.862082. Taking a maximum of that FLOAT value and the origin lower does not certify a global upper; the required upper must be proved separately.

With the revised near diagnostic, the regional matrix lower would leave rate room 0.000938706156 at (b0,mu)=(11/20,72), or 0.008104144765 at (103/200,68), before eps_rest, if it held globally and if the remaining diagnostic inputs were certified. A larger Hessian upper consumes part of the same room. The one-variable thresholds in the theory near checks cannot be saturated jointly without recomputing the complete input tuple. A rounded sufficient target is also not a necessary limit: AT2493 to AT2498 refute that reading of the D6 target 63279.8 in version 4. The later [version 5 near check](../../theory_agent_1/research/closure_check/NEAR_CHECK_v05.md) uses the admitted R4 version 1 inputs and keeps the other uncertified premises explicit.

The [complete local R4 replay](../research/source013_r4_replay/PROOF.md) finished at 09:34:43.233991Z on November 4, after 916.999437529128 measured seconds. All 446 compact panels and both infinite tails were recomputed with copied, hash-checked T2 source, followed by a separately written exact reducer. This is a complete numerical replay and an independent reduction; it is not a separately redesigned field evaluator. AT2447 to AT2451 review the analytical method, and AT2477 to AT2480 confirm its [actual record](../../theory_audit/research/near_r4_actual_v01_audit/verification/actual_review_v01.json). The [local adoption](../research/source013_r4_replay/verification/actual_review_v01.json) authenticates that review and the complete replay. The bound is Lambda_+(a_n)<=5901153228680477/2^48, with weighted negative and positive suprema at most 8.678463435 and 8.547679596 and positive-part integral at most 4.161116960. Inserting these inputs gives conditional regional rate rooms 0.000902291613 and 0.008067730195 for the same two parameter choices; the global matrix and other near and remainder premises are still required. A finer v02 replacement has a reviewed conditional method and a frozen local replay preparation, but no completed local replay at this cutoff.

An independent [exact origin-jet calculation](../research/source013_rest_origin_jets/RESULT_PROOF_v01.md) gives the downward bounds

    sup ||Delta Sym Du||_op >= 1.899576001577,
    u_3 >= 1.024389316421,
    M_S >= 5.698728004731.

The two Fourier-moment statements require the finite moments and inverse-transform identities in its [proof](../research/source013_rest_origin_jets/PROOF.md). They are obtained from exact low-order Taylor coefficients of all 1922 chi atoms and 12273 phi atoms, without sampling or quadrature. AT2456 to AT2458 independently confirm these exact bounds and their limited consequence; the [actual adoption](../research/source013_rest_origin_jets/verification/actual_review_v01.json) checks that complete review and both execution receipts. The sufficient cost (q/2)M_S in the unsplit TIS-FG estimate already exceeds the entire conditional far free gain. That excludes paying this particular sufficient upper from that gain. It is not a lower bound on the bilinear form and does not exclude a sharper estimate or existence.

The [H4 remainder plan](../../theory_agent_1/research/h4rest/H4REST_PLAN_v01.md) identifies T_IS, C_tr and C_vs1 through C_vs3. Its budgets and proposed sufficient estimates do not certify their values for source 013. The remaining near derivative inputs, H4 remainder, full inverse and invariant-ball argument remain separate obligations. The admitted global Hessian upper does not supply any of them.

## 6. Reusing the record

The [research index](../research/README.md) leads to topic folders with standalone informal proofs, exact JSON and verification evidence. AUDIT_LEDGER.md is chronological, with each claim labelled CONFIRMED, REFUTED or OPEN. The immutable exchange reports show what was sent to the theory and numerical agents. status file names the current job and restart point.

A failed sufficient interval test is inconclusive unless a separate lower bound proves a violation. A floating mesh maximum controls only its sampled points. Agreement of two quadratures does not enclose the omitted exterior. A passing source calculation requires its exact input, complete range argument and successful receipt; the number of assertions executed is not a measure of proof coverage.

Some historical intermediate archives require regeneration. In particular, AN605 removed two source009 diagnostic archives before the required review. AT2138 refutes procedural compliance, and byte-identical recovery remains open. The [frozen X10 report](X10_AUDIT_INPUTS_v01.md) records this limitation and the prospective authorization separately. It does not turn that later authorization into a retrospective approval.

The two old N2 Cartesian FLOAT dumps have a separate [dependency review](../research/n2_cartesian_retirement_audit/RESULT_PROOF.md). They are outputs, not inputs to the inspected certificates or probes; the probes use retained polar archives. Their owner reports removal at 09:08:08Z on November 4 in its [retirement receipt](../../numerics_agent_2/results/RETIREMENT_T1REQ_cart_v01.json), after AN723 and AT2426 to AT2427. This owner-reported, reviewed case does not change the earlier source009 deviation.

For the final existence statement, all numerical and analytical hypotheses must hold together for this same exact source and fixed parameter. The numerical record at this cutoff does not establish that conjunction.
