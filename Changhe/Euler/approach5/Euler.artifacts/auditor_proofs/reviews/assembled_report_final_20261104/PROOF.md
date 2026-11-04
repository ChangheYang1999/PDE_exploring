# Final cumulative report comparison

Status: CONFIRMED for the exact requested revision af81c04c, at the scope below. This is the proof for A3269. The unrestricted arbitrary-omega conjecture remains OPEN.

## 1. Exact object and scope

The base report is9836a8ea6513cbbf44a66b7f19a044653d794da349df013fbd11ff3c12ae85dd, approved by A3239 at verdict cutoff A3238. The candidate isaf81c04c4940440447970a8ee051402d79a6b914ce072709322a577fbfdf97d9, assembled at15:12 UTC on November4,2026, with cutoff A3268. Its live report, publication copy and coordinator pin were byte-identical when captured at2026-11-04T15:13:50.154594+00:00. The candidate has8,379 lines and1,348,780 bytes. The actual final request is coordinator Note 276, dated 15:25 UTC. At 2026-11-04T15:26:24.895003+00:00, the live report, publication copy, pin and report-v2 copy were all still byte-identical to this candidate. Its independently regenerated cumulative diff is identical to the already completely read 142-line diff. The final current-build record retains the exact request and checks.

The confirmed transfer covers only the front matter, Sections 0 through 10 and Appendix A. It inherits the exact hypotheses and limits of A3239 and the cited individual verdicts. It is not a fresh independent proof of every unchanged theorem. Historical Appendices B/C/D and the full coordinator README have no collective certification. Changed history entries are checked for accuracy without approving all surrounding historical claims.

The question is whether a cumulative change alters a theorem, removes a premise, misstates a verdict or broadens an approved conclusion. The pass criterion is that each substantive change is an independently confirmed correction or preserves the statement, with no unresolved conflict in the reviewed scope. A byte comparison transfers unchanged text; it is not an independent proof or a numerical experiment.

## 2. Exhaustive cumulative changes

The independently generated normal-format diff has142 lines and24 hunks, SHA2562afd805c8572042a0c568c8ac33c11bd2daf063b15bbf9576bb754361e6b53a7, identical to the coordinator's cumulative diff. All lines were read in bounded displays1-52,53-114 and115-142. Earlier complete incremental diffs are retained. This table exhausts the24 current hunks.

| Hunks | Change | Mathematical disposition |
| --- | --- | --- |
| 1 | Status and cutoff advance to A3268 | Accurate for the captured revision; final assembly approval remains separate. |
| 2-3 | Front matter records A3239 and its source-return repair assembly | The approved pin and exact scope are retained. |
| 4,9,12-16,18,21-22 | Eleven integer-regularity qualifiers | Three were accepted in A3262, seven in A3264, and the A454 row is checked in Section4 below. Hunk18 contains two rows. |
| 5-8,10-11,20,24 | Ten pairs of Markdown backticks | Existing expressions are unchanged; no mathematical extension. |
| 17 | Universal no-finite-energy remark replaced by theorem-specific hypotheses | A3261 refuted the original wording; A3262 accepts this exact repair. |
| 19 | Period and compact-set entropy qualifiers | A3248 and A3250, reconstructed in Section3 below. |
| 23 | Twenty-four chronological history lines replace the former latest line | The former line is retained as the earliest of the24; original refutations and later repairs remain distinct. |

The backticks wrap defect-measure expressions, one distributional scaling expression, generic proof paths and one Xue growth inequality. They correct CommonMark interpretation. The complete original patch and its application were already compared; removing the wrappers restores the old expressions. Neither an unread fragment nor a search match is treated as approval of unchanged mathematics.

## 3. The two mathematical qualifiers

For the changed periodic-orbit row, let 0<c<1/2 and omega be any fixed finite real number. Let U be C2 and P be C1 on R3, with div U=0 and

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    J(y1,y2,y3)=(-y2,y1,0).

Set B=(cI-omega J)y+U and W=curl U. A nonconstant periodic B orbit has zero U circulation. Indeed the Lie derivative of the circulation one-form is (2c-1) times that form plus the exact differential d(|U|^2/2-P). An oriented B orbit is preserved by its own flow, so its circulation equals exp((2c-1)s) times itself and is zero. For a T-periodic parametrization Y, substitution of U=Y'-cY+omega JY gives

    integral_0^T |Y'|^2 dt+omega integral_0^T JY.Y' dt=0.

The first term is positive. Subtracting the time average of Y, then applying Cauchy-Schwarz and the periodic Wirtinger inequality, bounds the absolute value of the second integral without omega by T/(2pi) times the first term. Hence omega is nonzero and T>=2pi/abs(omega). This step is local near the orbit and uses no escape assumption. At omega=0 it excludes the orbit; no division by zero is made.

For the W-flow conclusion, assume additionally that U is uniformly sublinear. The B flow Phi is complete and every backward image of a fixed compact set stays in a fixed ball D. From [B,W]=-(1+c)W, with kappa=1+c, the flow relation is

    Phi_s Gamma_t=Gamma_(exp(kappa s)t) Phi_s.

Let K be compact and invariant under the whole W flow Gamma. Its image Kn=Phi_(-n)K is another such compact set inside D. No global completeness of Gamma outside these sets is needed. If M=sup_D ||DW||, Gronwall and a three-dimensional grid give h_top(Gamma_1 on Kn)<=3M uniformly in n. The displayed conjugacy and compact-flow time scaling give

    h_top(Gamma_1 on Kn)=exp(kappa n) h_top(Gamma_1 on K).

It follows that h_top(Gamma_1 on K)=0. This proves exactly the compact-set qualifier. It supplies no entropy statement on a noncompact phase space. The complete 83-line A3250 reconstruction was reread during this comparison; it also proves the unchanged saddle and no-periodic-vortex-line statements. A3248 had already accepted the compact-set row repair.

## 4. The assumption remark and integer regularity

The original universal no-finite-energy clause was false because Theorem8(i) permits s=2 with U in L2 and P-p0 in L1. The corrected remark names Theorems1,2,4,5,6 themselves, preserves their other hypotheses, and explicitly keeps the integrability branches and additional symmetry or tail assumptions. It does not remove a premise of any theorem. The complete independent A3261 defect argument and A3262 repair proof were read, together with the complete C comparison. Theorem1's separate conditional corollaries still have their own hypotheses.

The eleven integer qualifiers restore the regularity used in the named sources. TheoremL and the componentwise A430 theorem use integer r>=2. A312 and A373 use integer r>=3. The A055 entropy source itself states integer r>=2; this is not a new reading of the original Yomdin article or a claim about fractional regularity. The source classes, strain thresholds and sign hypotheses remain unchanged. A3264 already accepts seven of these changes; A3262 accepts the three TheoremL summaries.

For the remaining A454 row, assume its full C^r/C1 profile class, integer r>=2,0<c<1/2, uniform sublinearity, and the stated strict bound lambda_min(sym DU)>-(c+r a) on each compact zero stratum Z_E, where a=1-2c. For nonempty Z_E, compactness and continuity give a positive margin delta_E. The symmetric derivative of the backward carrier is-cI-sym DU, since omega J is skew. Along each complete orbit in Z_E, differentiating a tangent vector's squared norm gives growth at most2(r a-delta_E) times that norm. Therefore every largest exponent there is at most r a-delta_E, so Gamma_E<r a. Empty Z_E uses Gamma_E=-infinity. This proves the precise sufficient implication for each E without a common margin.

A430 then supplies coverage. The Liouville consequence still additionally assumes uniform decay,2/5<=c<1/2 and one helicity sign per essential basin. Decay does not establish the pointwise strain condition. The complete13-line A454 successor diff and its C comparison were checked. Only the integer qualifier is new in that row, and it matches the original A454 statement.

## 5. New history and retained assumptions

A3242 remains REFUTED for its original natural-gradient wording; A3244 accepts its repair. A3245 remains REFUTED for the original equivalence in a C comparison; A3247 accepts the corrected sufficient condition. A3246 records the missing compact-set qualifier and A3248 accepts the repair. A3254 remains REFUTED for an auxiliary physical-path equality missing rotation; A3255 accepts the corrected comparison without changing the original physical-scaling theorem. The candidate preserves these distinctions.

The history of A3240 and A3243 retains the regularity and sign premises of A3235. A3241 approves obstruction presentation only. A3249-A3252 retain the derivative, Dini, blow-down, exponent and compact-set hypotheses of their separate results. A3253 retains the three elementary-vorticity conditions and the unresolved broader claim. A3256 retains both gradient-growth premises. A3257 distinguishes kernel triviality from a spectral gap. A3258 keeps gamma>=0 in its standalone logarithmic statement; under the report's additional uniform velocity decay, negative gamma falls under A3256. A3259 gives equality of joint normalized-gradient and strain singular sets at threshold one, with no emptiness conclusion. A3260 accepts only the strain-cutoff implications, not optimality or a numerical instance.

The two latest history lines record A3264-A3268 accurately. A3264-A3266 concern seven integer qualifiers, the exact componentwise/C2 recheck and presentation consistency only. A3267 refutes a literal source inference, not Chae's theorem; A3268 accepts the strict-weight repair and an already covered stationary class, retaining derivative decay and the strict exponent. The report does not rely on that source. Neither history line claims a final assembly verdict. Each of the two complete9-line successors from938e3c5f changes only history and status.

The retained exact statements are in the corresponding standalone proof folders. All four new focused comparisons, growth, weighted criteria, local strain sets and strain cutoffs, were checked against the complete existing A or C notes before their individual verdicts. Agreement alone is not evidence; their independent calculations and explicit dispositions support those verdicts.

## 6. Dependencies, unresolved steps and finalization

The transfer depends on A3239, A3248, A3250, the presentation application record, and the individual A3240-A3268 ledger entries at their exact scopes. The current capture manifest identifies the independently retained report and cumulative diff; the earlier preparation capture remains retained.

The complete initial C comparison is independently checked in the comparison disposition. Complete later C comparisons agree on the assumption repair and integer qualifiers, and the full51-line literature comparison was read at its explicit scope. A3261 remains REFUTED for the original universal remark; A3262 accepts its repair. A3263 reconfirms the classical pressure-energy chain. A3264 accepts the seven later integer qualifiers. A3265 reconfirms the componentwise/C2 interfaces; it changes no theorem in this candidate. A3266 independently confirms presentation consistency of Sections4-10 only. The ten-item task summary has also been completely read with the source hypotheses and the explicit open conclusions retained; this is presentation scope, not a fresh proof of every listed result. The complete final 44-line C comparison and 37-line literature comparison have now been independently checked, with no unresolved disagreement, in the final disposition. The remaining A454 qualifier is confirmed by Section 4. The actual requested revision matches the fully reviewed candidate, so the pass criterion in Section 1 is met. A3269 confirms the exact transfer; no current repair is pending. The deliverable review separately checks the eight required files and ten requested answer items, at presentation and existence scope only. Automatic helicity sign, automatic C2 coverage and a finite normalized gradient budget from velocity decay remain unproved. The unrestricted arbitrary-omega conjecture remains OPEN, with no verified full-profile counterexample.

Collaboration is through the existing configured model working files, with provider execution independently unattested. No new agent, model client, numerical experiment or formal build is used. Future deadlines are not elapsed work. All retained paths are relative.
