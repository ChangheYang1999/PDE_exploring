# Numerical audit reading guide, version 3

This guide summarizes the record through AN658. Its creation time and source hashes are in AUDIT_READING_GUIDE_v03.bindings.json. Later results belong to later dated entries in AUDIT_LEDGER.md and exchange/. The guide is a map of evidence, not an additional numerical certificate.

The fixed source C2-N1-013 has a rigorously enclosed small residual. A stationary existence theorem has not been certified. The difference lies in the remaining hypotheses: the background estimates still have an uncovered region, the complete near estimate is being assembled, and the full inverse and high-regularity invariant ball require their separate analytical arguments. None of these conditions follows from the optimizer's loss.

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

The most recent executed and independently reviewed union at this guide's cutoff contains 87 original radial indices. Under its stated source and containment hypotheses it proves, at every angle,

    M >= (3/5) I,  |grad h| <= 1/4,  ||Sym Du||_op <= 137/125
    on r^2 in [0,57/71] union [49/15,infinity).

Its single open gap is (57/71,49/15). This is a missing certificate, not evidence of a violated inequality. The stronger gradient target 71/500 has 83 indices and four open gaps:

    (57/71,99/29), (25/7,101/27),
    (51/13,103/25), (13/3,105/23).

Read the [progressive union proof](../research/background_progressive_union/PROOF.md), its [m=56 result](../research/background_progressive_union/verification/check_v02.json), and [AN637](../exchange/audit_v637.md). The adopted original indices are 0 through 56 and 98 through 127. The compactification t=r^2/(1+r^2) turns each finite root into [j/128,(j+1)/128]. A union check authenticates the selected local theorems and checks the exact endpoints. It does not rerun a field evaluator.

Individual roots [057](../research/source013_background_admission/roots/root_057_v02/PROOF.md), [058](../research/source013_background_admission/roots/root_058_v02/PROOF.md) and [059](../research/source013_background_admission/roots/root_059_v02/PROOF.md) were adopted after that union. Their local results remain valid, but they do not change the recorded m=56 union until a new assembly is executed and reviewed. Root 060 has completed its calculation and awaits its actual independent review at the cutoff. This separation prevents an expected result from entering a published global inventory.

The outermost region is complete. The [exterior theorem](../research/background_exterior_union/PROOF.md) proves on every finite point with r^2>=127 the matrix bound above, |grad h|<=899/10000, strain<350541070259/10^12, and d0^2 det(M-(3/5)I)>=949/20000, where d0=(1+3t)/4. The formal endpoint t=1 is not a spatial point. The intervening capped slabs have an independent complete-source calculation and two exact recounts, documented in [the X10 addendum](X10_AUDIT_ADDENDUM_v01.md).

For ordinary roots 97 down to 56, a new independent source calculation is prepared for core 49 in the second numerics agent. Its [method](../research/ordinary_slabs_host_method/PROOF.md) and [producer-prefix rule](../research/ordinary_slabs_host_plan/PRODUCER_PREFIX_PROOF_v02.md) have conditional admission. T1's complete, terminated producer record, its independent review, a concrete host request and both request admissions must precede that run. A timed-out producer may supply its complete required prefix only under the reviewed rule. The independent host still requires all 42 roots and a successful execution.

## 4. The near and far estimates have different evidence chains

The [far Schur assembly](../research/far_cs_b_updated_assembly/PROOF.md) and [independent window calculation](../research/far_window_updated_audit/PROOF.md) supply the far numerical inputs. The latter independently reconstructs all 5120 window cells using its own Bell recurrence and radial integration, while importing the explicitly cited containing derivative and kernel intervals. It is not a second full reconstruction of those imported intervals.

At strain 137/125 the recorded far margin is

    71675071190082633/5629499534213120000.

Non-strict absorption permits strain up to and including 4963249980622857/4503599627370496; positive slack requires a strict inequality. These conclusions still need the matching whole-plane strain premise and the other analytical hypotheses. A far margin does not supply the near estimate or the full inverse.

The near calculation uses 561 annular panels and two endpoint regions. Every complete owner has a disjoint subset of panel indices. The original owner's successful receipt is required before any of its panels can enter the independent chunk review. The [chunk theorem](../research/source013_near_admission/CHUNK_PROOF_v01.md) requires a complete-source majorant replay, coefficient and energy checks, an actual independent review and an adopted result. All chunks are then assembled into the owner's block.

The first N4 attempt failed when its archive check compared integer dictionary keys with their JSON string representations. Its numerical panel record was retained, but the failed request supplies no admitted chunk. The [version 2 repair](../research/source013_near_admission/ARCHIVE_REPAIR_PROOF_v02.md) checks exact decompressed JSON bytes and leaves the numerical majorant unchanged. Fourteen fresh requests were independently bound and adopted in [AN658](../exchange/audit_v658.md). Their sequential replay is active at this cutoff; a request admission is not an actual-result certificate.

The [whole-plane near proof](../research/source013_near_norms/PROOF.md) explains why all five blocks and both endpoint certificates are needed. It first sums Laplacian energies, then uses a whole-plane identity to obtain ordered Cartesian derivative norms D4, D5 and D6 and the corresponding Fourier-moment inputs. An individual annular Laplacian energy cannot be relabelled as a Cartesian tensor energy on that annulus. The [version 2 consumer migration](../research/source013_near_norms/CHUNK_MIGRATION_PROOF_v04.md) changes its explicit method bindings; at the cutoff its independent method review remains pending.

## 5. Reusing the record

The [research index](../research/README.md) leads to topic folders with standalone informal proofs, exact JSON and verification evidence. AUDIT_LEDGER.md is chronological, with each claim labelled CONFIRMED, REFUTED or OPEN. The immutable exchange reports show what was sent to the theory and numerical agents. status file names the current job and restart point.

A failed sufficient interval test is inconclusive unless a separate lower bound proves a violation. A floating mesh maximum controls only its sampled points. Agreement of two quadratures does not enclose the omitted exterior. A passing source calculation requires its exact input, complete range argument and successful receipt; the number of assertions executed is not a measure of proof coverage.

Some historical intermediate archives require regeneration. In particular, AN605 removed two source009 diagnostic archives before the required review. AT2138 refutes procedural compliance, and byte-identical recovery remains open. The [frozen X10 report](X10_AUDIT_INPUTS_v01.md) records this limitation and the prospective authorization separately. It does not turn that later authorization into a retrospective approval.

For the final existence statement, the remaining question is whether all numerical and analytical hypotheses hold together for this same exact source and fixed parameter. The numerical record at this cutoff does not answer that question affirmatively.
