# Numerical audit reading guide, version 5

Frozen 2026-11-04T11:22:12.383355+00:00 through AN812. This guide maps evidence; it is not an additional numerical certificate.

The fixed source C2-N1-013 has a rigorously enclosed small residual and a completed whole-plane background cover. A stationary existence theorem has not been certified. The complete near estimate is still being assembled, some H4 remainder terms still lack proved bounds, and the full inverse and high-regularity invariant ball require their separate analytical arguments. None of these conditions follows from the optimizer's loss.

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

## 3. How the background cover closes

Put h=-Delta phi_013 and

    M = (c+1+(cX+u).X/(1/4+|X|^2)) I
        - (21/10) Sym D(cX+u)
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].

The completed and independently adopted cover proves, throughout the plane,

    M >= (704955805507/10^12) I,
    |grad h| <= 1/4,
    ||Sym Du||_op <= 137/125.

These three inequalities use the same exact source. The [whole-plane union proof](../research/background_complete_union/PROOF.md) was written conditionally before the last region finished; its [actual adoption](../research/background_complete_union/verification/actual_review_v01.json) discharges the recorded execution and regional-review conditions. The union uses these matrix bounds:

| Squared-radius region | Certified matrix lower |
| --- | --- |
| [0,61/67] | 704955805507/10^12 |
| [7/9,49/15] | 890672299617/10^12 |
| [49/15,infinity) | 761272835221/10^12 |

The middle interval overlaps the inner interval and meets the exterior. Thus every point belongs to at least one certified region, and the smallest of the three constants is a global lower. No averaging across the regions is involved. In the compact coordinate t=r^2/(1+r^2), the regions cover [0,61/128], [56/128,98/128] and [98/128,1). The formal endpoint t=1 records the infinite exterior; it is not a further spatial point.

The [matrix recount](../research/background_matrix_margin_recount/PROOF_v02.md) bounds the smaller eigenvalue of each containing symmetric interval matrix. It uses downward diagonal bounds, an upward bound on the off-diagonal square and exact integer square comparisons. Where division by the positive weight occurs, the sign of the numerator determines which denominator endpoint is valid. The result holds at every point in the containing cell, rather than only at a mesh minimum.

The last region came from the complete 42-root ordinary reconstruction. Its [host receipt](../../numerics_agent_2/source_host_049/ordinary_v01/execution_v01.json) records completion at 09:31:39.907812Z on November 4 after 2372.995782851707 measured seconds. The subsequent [exact recount](../research/ordinary_slabs_host_method/verification/recount_v01.json) checked all 344064 cells and every stored coefficient interval and branch-tail record. The [host matrix argument](../research/ordinary_host_matrix_margin/PROOF.md) provides the stronger middle-region lower. Their separate actual reviews are bound by the complete union's adoption.

The stronger gradient target 71/500 has a different cover. It is proved on 124 of the 128 radial indices, with indices 98, 100, 102 and 104 missing. Its remaining open squared-radius gaps are

    (49/15,99/29), (25/7,101/27),
    (51/13,103/25), (13/3,105/23).

Those gaps are absent from the weaker 1/4 cover. An unproved stronger inequality cannot be substituted for the certified weaker one.

The background bounds can now supply their numerical premises in NR31. That conditional k=0 theorem still assumes the stated source, generator, common-domain, weighted-decay and semigroup properties. It permits every 0<beta_1<704955805507/10^12 and leaves the lower-order constant C_1 finite but uncomputed. It gives no uniform small-k conclusion by itself. The [theory dependency account](../../theory_audit/reports/SOURCE013_CHAIN_CONDITIONS_v04.md) retains these distinctions.

## 4. What is complete in the near and far calculations

The [far Schur assembly](../research/far_cs_b_updated_assembly/PROOF.md) and [independent window calculation](../research/far_window_updated_audit/PROOF.md) supply the far numerical inputs. The latter reconstructs all 5120 window cells using its own Bell recurrence and radial integration, while importing the explicitly cited containing derivative and kernel intervals. It is not a second full reconstruction of those imported intervals.

At the now globally certified strain 137/125, the recorded free far gain is

    71675071190082633/5629499534213120000.

Non-strict absorption permits strain up to and including 4963249980622857/4503599627370496; positive slack requires a strict inequality. The other analytical hypotheses in the far argument remain necessary. This scalar margin supplies neither the near estimate nor a full inverse.

The near coefficient is

    a_n(X) = (4u(X).X-c)/(1+4|X|^2) * erfc(log(|X|/sqrt(8))/L)/2,
    L = log(8)/(2sqrt(pi)),  a_n(0) = -c.

Its calculation uses 561 annular panels between radii 1/4096 and 10000, an origin disk and the full infinite exterior. Each original owner has a disjoint residue class of panel indices. All five original owner calculations completed, but a completed producer record is only one premise in the audit. The [chunk theorem](../research/source013_near_admission/CHUNK_PROOF_v01.md) also requires a complete-source majorant replay, exact coefficient and energy checks, a distinct actual review and an adopted result. Those checks include all 52 source branches, 5136 mode polynomials and 211664 exact polynomial coefficients.

N4's fourteen chunks and complete 112-panel block are adopted. With E4, E5 and E6 denoting the integrals of |Delta^2 a_n|^2, |grad Delta^2 a_n|^2 and |Delta^3 a_n|^2 on its annulus union,

    E4 in [39461,39462],
    E5 in [3505225,3505226],
    E6 in [803311347,803311348].

The [standalone N4 proof](../research/source013_near_admission/results/block_n4_v02/PROOF.md) states the exact source and containment hypotheses; its [actual adoption](../research/source013_near_admission/verification/block_n4_v02/actual_review_v01.json) binds the successful calculation and independent review. The displayed integer intervals are coarse outward summaries of the exact rational endpoints in JSON.

All fourteen N3 chunks and the complete 112-panel reduction are also actually reviewed and adopted. Its original 480-second guard finished at 11:08:42.846612Z on November 4, after24.440169002860785 measured seconds. The [N3 proof](../research/source013_near_admission/results/block_n3_v02/PROOF.md) covers exactly indices3,8,...,558; its [actual adoption](../research/source013_near_admission/verification/block_n3_v02/actual_review_v01.json) authenticates the separate independent review and all exact sums. The coarse outward intervals are E4 in[39461,39462], E5 in[3505317,3505318] and E6 in[815397470,815397471].

N0's first three chunks are adopted, giving248 adopted panel records across N4, N3 and N0. Every N0 physical chunk has completed, but the remaining12 actual reviews are pending. N1 has begun its14-chunk replay, and N2 remains queued. The remaining313 panel admissions, three complete owner reductions and final assembly are required before a whole-plane energy bound is available. These counts record provenance progress; they are not partial substitutes for the global estimate.

The first N4 admission attempt failed when an archive check compared integer dictionary keys with their JSON string representations. Its numerical panel record was retained, but the failed request supplied no admitted chunk. The [version 2 repair](../research/source013_near_admission/ARCHIVE_REPAIR_PROOF_v02.md) checks the exact decompressed JSON bytes and leaves the numerical majorant unchanged. Every adopted chunk passed a fresh complete request under that repaired method.

These are regional Laplacian energies. They cannot be relabelled as regional ordered Cartesian tensor energies. The [whole-plane near proof](../research/source013_near_norms/PROOF.md) first sums all five blocks and both endpoint certificates, then uses the global identity to obtain the ordered Cartesian D4, D5 and D6 norms. Its [version 2 migration](../research/source013_near_norms/CHUNK_MIGRATION_PROOF_v04.md) has an admitted method; actual execution still needs the remaining complete blocks. The endpoints and the infinite exterior are essential to the global identity.

## 5. The rate budget and the refined coefficient bounds

The H4 rate condition is

    e_up + eps_rest <= beta_star - b0.

Here beta_star is a matrix lower for the whole plane, e_up is the near loss at its complete input tuple, and eps_rest bounds the other H4 terms. The completed background supplies beta_star=704955805507/10^12. It does not certify a FLOAT near derivative input or allow eps_rest to be set to zero. The associated price condition C0>=P+C_rest and self-map condition C0 R^2<=M[(b0-L_B)M-n] must also hold with their own constants. The eight outstanding closure hypotheses are H-RC, H1, H2, H-BALL, H4-REST, H-N1, H-NEARU and H-REG. In the stronger-source route, the imported R6.4 restrictions remain alpha/(2c-2)<delta<1 and1<nu<2, with the full source assumptions; R9.4 also retains all its premises. The near-cut parameter nu=1/40 is a different use of the symbol and does not satisfy or replace that source-decay requirement.

The origin forces

    Lambda_+(a_n) >= 8(2c-1) = 2950576553396557/140737488355328.

The [exact Hessian argument](../../theory_audit/research/lambda_target_incompatibility_audit/PROOF.md) uses the normalized velocity jet and the flatness of the erflog cutoff at zero. This disproved the old FLOAT target 20.862082 as a global upper. Taking the maximum of a sampled value and a pointwise lower would not repair that upper; a complete range estimate was needed.

The [complete local R4 replay](../research/source013_r4_replay/PROOF.md), now at version 2, provides that range estimate. It recomputed 446 compact panels and both infinite tails with copied, hash-checked T2 source and a separately written exact reducer. Its [actual adoption](../research/source013_r4_replay/verification/actual_review_v02.json) binds the successful replay and distinct review. The refined calculation used 368 coarse and 78 fine panels, with 1015808 cells, and took 507.4918713979423 measured seconds. This is a complete numerical replay and independent reduction, not a separately redesigned field evaluator.

The admitted version 2 bounds are

    Lambda_+(a_n) <= 5901153228680477/281474976710656,
    sup (a_n)_- W^2 <= 4877321332131611/562949953421312,
    sup (a_n)_+ W^2 <= 4806001960566741/562949953421312,
    integral (a_n)_+ <=
      21218005723912562034147590433407517/5192296858534827628530496329220096.

Comparing the two supremum uppers gives sup |a_n|W^2 at most their maximum. It does not prove equality between the actual absolute supremum and actual negative-part supremum.

At these R4 inputs, the [independently reviewed closure calculation](../../theory_audit/research/closure_v06_audit/PROOF.md) gives the following conditional arithmetic:

| Case | (b0,mu) | Near loss upper used | Remaining rate before eps_rest |
| --- | --- | --- | --- |
| Plan | (11/20,72) | 154030238822/10^12 | 185113337/200000000000 |
| Fallback | (103/200,68) | 181864800240/10^12 | 8091005267/10^12 |

The near loss still depends on FLOAT D4, D5 and D6 inputs. The closure record uses zero stand-ins for eps_rest and C_rest; it does not prove those terms vanish. Its fallback kernel constants are also unaudited. The displayed rooms therefore describe what the remaining proof must fit, rather than a closed rate estimate. A separate near-table allowance has different inputs and must not be mixed with these rows.

One-variable thresholds must be used at their own complete tuple. They cannot be saturated jointly without recomputing the loss. Rounded sufficient D6 targets are not necessary limits on D6. These distinctions matter because the plan's remaining rate is less than one thousandth.

## 6. Exact origin information and the remaining moment bounds

For the H4 notation, put Phi=partial_y chi_007+phi_013, Psi=partial_x Phi and S=Sym Du, so u=(-Psi_y,Psi_x). Use the nonunitary Fourier convention and

    m_k(f) = (2pi)^(-2) integral |xi|^k |fhat(xi)| dxi,

with the matrix operator norm inside the integral for S. This convention differs from the unitary P-S1 convention above. All moment statements assume the ordinary Fourier representatives and valid inverse derivative formulas specified in their proofs, excluding an unaccounted distribution supported at zero.

The planar stream-function symbol gives

    u_3 = m_4(Psi) = 2m_2(S),  m_4(S)=m_6(Psi)/2.

The exact [origin-jet result](../research/source013_rest_origin_jets/RESULT_PROOF_v01.md), together with that symbol identity, implies

    u_3 >= 3799152003154/10^12.

A later [seventh-order calculation](../research/source013_rest_seventh_jets/PROOF.md) visits all 1922 chi atoms and 12273 phi atoms and retains their exact Taylor coefficients. If

    Phi_7 = A x^6 y+B x^4 y^3+C x^2 y^5+D y^7,
    J=720A+288B+240C,

then direct differentiation gives Delta^2 S(0)=diag(-J,J). The [actual adoption](../research/source013_rest_seventh_jets/verification/actual_review_v01.json) binds both the producer and an independent direct coefficient extraction. They prove

    5261.943457574294 <= ||Delta^2 S(0)||_op <= 5261.943457574295,
    M_S=3m_2(S)+2m_4(S) >= 263239641078833/25000000000.

The pointwise matrix result requires only the exact smooth source. The second inequality additionally uses the Fourier-moment hypotheses. Its right side is 10529.58564315332. Consequently the specified unsplit nonnegative sufficient charge (q/2)M_S cannot fit the recorded free far allowance. This excludes that charge with that allowance. It is not a lower bound on the actual T_IS form, does not force a frequency split, and does not rule out cancellation, another estimate or existence.

The [independent high-frequency cutoff replay](../research/hi_cutoffs_independent/PROOF.md) checks 24 fixed tuples and 480 decisions at 768-bit precision. For the refined R4 inputs and the whole-plane rate, the K_half sufficient estimate requires a window parameter mu_r at least a number in [207.422143510389,207.422143510390] at the plan, or [70.154855285062,70.154855285063] at the fallback. Thus 200 fails this necessary test at the plan, while 208 is merely not excluded by it. Passing the test does not establish H4. The [actual replay record](../research/hi_cutoffs_independent/verification/actual_review_v01.json) keeps each rate, lower moment and coefficient together. An earlier quoted value 140.055 was a cutoff using an older lower and room, not the multiplier sqrt(GK/R); the [specific correction](../research/hi_cutoffs_independent/N1_NOTE_1052_CORRECTION_v01.md) prevents that substitution. The numerical team acknowledged and repaired these constants in [numerics version17](../../exchange/numerical_results/numerics_v17.md); the older notes remain historical.

For upper bounds, the [scale-optimized moment theorem](../research/scale_optimized_moment/PROOF.md) supplies a useful conditional estimate. For a scalar f and E_j=|| |D|^(k+j)f ||_2^2, finite E0 and E2 imply

    m_k(f)^2 <= [lambda^2 E0+2E1+lambda^(-2)E2]/(4pi)
              for every lambda>0,
    m_k(f)^2 <= [sqrt(E0 E2)+E1]/(2pi).

The second bound follows by minimizing the first at lambda=(E2/E0)^(1/4) when both energies are positive. A zero endpoint energy makes the ordinary weighted Fourier representative zero almost everywhere. The [actual adoption](../research/scale_optimized_moment/verification/actual_review_v01.json) confirms this theorem and its monotone use with certified upper energy bounds. It supplies no Source013 energy values.

The numerical team's optimized moment values remain FLOAT. An [independent scalar audit](../research/h4rest_final_scalar_audit/PROOF.md) at 768 bits confirms that the two final saved reports evaluate their optimizing scale, optimizing length, optimized upper expression and a=1 expression to relative error below 10^(-13) from their own saved decimal A, B and C. It also confirms the two derived linear formulas and cross-grid agreement below 10^(-8). Its [101 checks](../research/h4rest_final_scalar_audit/verification/check_v01.json) concern report arithmetic only; the input energy values are still floating quadratures. For example, the 4000-radius optimized expressions are approximately21.3616036121 for u3,24130.8810503 for m4(S), and948.856823513 for r3. None is an enclosed true moment. Agreement between longdouble runs on 2000 and 4000 radii is useful evidence about grid stability, but it does not bound an arithmetic bias shared by both runs. The [conditioning audit](../research/h4rest_screen_conditioning/PROOF.md) finds that changing to binary64 on the same 2000-point mesh changes three earlier reported moment upper expressions by factors exceeding 4000, 1.9 and 44. The [precision-inference correction](../research/h4rest_screen_conditioning/PRECISION_INFERENCE_v01.md) explains why mesh agreement cannot certify the longdouble values.

There is a separate boundary issue. On a finite annulus, the difference between integrated Hessian and Laplacian squares equals a boundary flux. The [exact boundary identity](../research/h4rest_screen_symbol_audit/QUADRATURE_notes_v01.md) gives that flux and the leading omitted-disk term. Their difference is therefore not a pure quadrature-error estimate. A full-plane upper moment needs all regions, controlled arithmetic and the correct global identities.

## 7. Reusing the evidence

The [frozen research index](research_index_at_guide_v05.md) accompanying this guide leads to topic folders with standalone informal proofs, exact JSON and verification evidence. AUDIT_LEDGER.md is chronological, with each claim labelled CONFIRMED, REFUTED or OPEN. Immutable exchange reports record the information sent to the theory and numerical agents. status file is a mutable restart checkpoint and is not a certificate.

A failed sufficient interval test is inconclusive unless a separate lower bound proves the stated obstruction. A floating mesh maximum controls only its sampled points. Two agreeing quadratures do not enclose an omitted exterior. A successful source calculation needs its exact input, complete range argument and successful receipt; assertion counts do not measure mathematical coverage.

The large derived Candidate007 expansion was retired under its recorded retention policy, with exact input and reconstruction code retained. The separate historical Source009 deletion did not follow the required order: AN605 removed two diagnostic archives totaling437055889 bytes before review. Procedural compliance is REFUTED, and byte-identical recovery remains OPEN. The [frozen X10 account](X10_AUDIT_INPUTS_v01.md) records this deviation and the prospective authorization separately. A later authorization does not retrospectively approve that deletion. Source013's retained inputs and certificates were unchanged.

The two old N2 Cartesian FLOAT dumps have their own [dependency review](../research/n2_cartesian_retirement_audit/RESULT_PROOF.md). They were outputs rather than inputs to the inspected certificates or probes. Their owner reports removal at09:08:08Z on November 4 in the [retirement receipt](../../numerics_agent_2/results/RETIREMENT_T1REQ_cart_v01.json), after AN723 and AT2426 to AT2427.

A further conditioning-copy replacement followed the frozen owner undertaking, prospective permission, independently reviewed executor and semantic preapproval. The [completed receipt](../storage/verification/conditioning_copy_link_execution_v01.json) records unchanged owner bytes and metadata and35913728 bytes of local allocation saved. Its [actual postcondition adoption](../storage/verification/conditioning_postcondition_adoption_v01.json) checks the exact relative link, resolved target, complete byte streams and metadata. The current postcondition is confirmed. Future retention and packaging are separate obligations: the first numerics agent owner file must remain through18:05:30Z and be included wherever the relative link is published.

A second prospective operation would replace AT's historical origin-PS2 duplicate by a link to AN's existing independent regular file. Its [read-only executor and byte review](../research/at_origin_ps2_retention_audit/PROOF.md) and [owner retention undertaking](../research/at_origin_ps2_retention_audit/OWNER_RETENTION_UNDERTAKING_v01.md) are complete. At this guide cutoff, coordinator authorization, exact frozen approval review and the actual replacement postcondition are pending. The owner file must remain unchanged through18:05:30Z and thereafter as published evidence, with no reverse link to AT.

The work used local CPU calculations under the agent allocation, with no JavaScript/TypeScript, servers, cluster/RLScience, remote computation or Lean/Lake builds. The the main model-configured theory agents contributed through shared files throughout; the actual provider model identity could not be independently verified. The remaining mathematical task is to establish the near, remainder, inverse and invariant-ball hypotheses together for this same exact source and fixed parameter.
