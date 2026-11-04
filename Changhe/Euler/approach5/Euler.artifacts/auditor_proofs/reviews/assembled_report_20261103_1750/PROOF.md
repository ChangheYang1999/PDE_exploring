# Audit of the coordinator's Note 100 assembly

## 1. Statement, coverage and notation

This is an audit of the assembly pinned in the team records at 2026-11-03T17:51:14.895121Z. The report has 6298 lines and SHA256 bacd6b42958f5cfaf23a1b2926c66474d3b1820be9fd995b6aa88b4dedc7e5c2. The independently generated difference from the preceding audited pin has 374 lines; the coordinator's 214-line difference is not the coverage record used here. Every actual changed passage, all 95 lines of README, and the complete differences of THEOREM_ATTEMPTS and PROOF_OBSTRUCTIONS were read. Long changed historical paragraphs were inspected by word differences; their unchanged context is not a fresh whole-report reread.

Write c in (2/5,1/2), p=(1-c)/c, a=1-2c, b=2(1-c), q=b/a, and X=Ax for the rotating dilation field. On the punctured space let V be the natural velocity tail, W=curl V, k=X.V, E=|V|^2, P2 its normalized pressure, and S=P2-E/2. On the sphere K=k. All claims below about actual profiles retain the full divergence-free Euler profile equation. The report's Theorem 7(g) is confirmed at its stated conditional scope. Two short statements omit premises, and two compressed rows require a qualification. No unrestricted nonexistence theorem is certified.

## 2. Theorem 7(g)

The exact base class is U in C2(R3), P in C1(R3), satisfying the full equation and div U=0, with the natural bounds |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1). The half-power gradient formulation is equivalent in the stated decaying class by the earlier audited regularity theorem; that equivalence does not require helicity freedom. The comparison constants must satisfy 0<r_-<=r_+<infinity uniformly on the whole sphere.

In case (i), impose k=0, W.grad S=0 and r_-|S|<=E<=r_+|S| globally on the tail. No original helicity assumption is needed. Natural tail regularity gives V in C^(1,alpha) for a permissible alpha>2/c-4 and the exact Poisson equation. The root estimates of A1847-A1851 make |S|^(-eta)V continuous and locally W^(1,t), eta=(p-1)/(2p), for some t>1. The normalized form is closed across its zero set, has a global primitive on punctured R3, and k=0 makes the primitive invariant along X. Its compact angular extrema and the audited weighted maximum argument force the primitive constant, hence V=S=0.

In case (ii), retain original helicity freedom, comparison, and full rank grad k cross grad S=0 on S!=0. The same normalized form has a primitive whose change along the dilation flow is a constant times time. If this constant were nonzero, a compact regular level enclosing the origin would have strictly one-signed velocity flux. Divergence freedom and the twisted scaling make the sphere flux zero because c!=1/3. Thus the drift vanishes, k=0, and case (i) applies. Vortical density suffices here because actual helicity-free tails already satisfy the rank relation on W!=0, and the relation extends continuously.

In case (iii), extend the original rank identity across the dense exterior vortical set before taking scaled limits. The comparison uses P-P_inf-E_U/2, so constant pressure shifts do not matter. This gives case (ii) without claiming that density survives a limit. Tail vanishing improves U to O(r^(-2p-1)), giving finite energy; the previously checked cutoff identity, including its pressure, cubic and dilation boundary terms, gives (1-5c/2) integral |U|^2=0. Hence U=0. In case (iii) that contradicts the original exterior density, so that entire class is empty.

Dependencies and the complete analytic argument are in the team records, reread in full for this audit, with in the team records and in the team records. No integrability, sign, or pressure premise has been silently added to Theorem 7(g).

## 3. The short summary and literal T41

Summary item 8 removes helicity freedom in the globally k=0 branch but does not state W.grad S=0 there. This transport premise is explicit in Theorem 7(g)(i) and is used to close the normalized form. Add it to the summary. Its omission is not a proof that the weaker assertion is false; the weaker assertion remains unproved here.

T41 literally assumes C2/C1 and natural bounds, but omits the full profile equation and div U=0. A title mentioning profiles does not supply an exact standalone statement, particularly in a file without a standing global equation convention. The literal text is false. Let chi(x)=exp(-1/(1-|x|^2)) for |x|<1 and zero otherwise. Set U=(partial_2 chi,-partial_1 chi,0) and P=0. Then U is nonzero, smooth, divergence free and compactly supported. Every natural upper bound holds with a finite constant, and its scaled velocity and pressure tails are zero. Thus k=0, W.grad S=0 and every positive two-sided comparison hold for those tails, but U is not zero. This countertest fails the omitted profile equation and does not contradict the intended theorem.

Repair T41 by specifying the full equation on R3, div U=0, p=(1-c)/c, a finite C, and uniform 0<r_-<=r_+<infinity. Its repaired statement is precisely Section 2.

## 4. Rank and nodal-row qualifications

The C43 repair correctly separates the kinematic regular-arc statement from the actual-profile exclusion of periodic vortex curves. Its displayed counterfield at omega=0 is V=(2-p)r^(-p)e3+p x3 r^(-p-2)x. On the equator V=(2-p)e3 is nonzero, while K=c x.V=2c x3 on the unit sphere. Therefore the phrase 'its only angular zero set' must identify the scalar contraction K, not V. The mathematical counterexample and the actual-profile qualification pass; this is a necessary naming repair in both occurrences.

The LIT268 row states a valid abstract theorem with full rank. Its following density shortcut needs the phrase 'for actual helicity-free tails', or an independent assumption of rank on W!=0. The listed abstract hypotheses of divergence freedom, homogeneity, transport, Poisson and comparison alone do not imply that rank. The exact poloidal example audited in the team records has p=10/9, c=9/19, smooth axisymmetric homogeneous V, canonical P2, global comparison, W.grad S=0 and vortical density away from the axis, but rank fails on the equator. It fails full momentum. Thus density alone cannot replace full rank in that broader abstract class. The actual-profile Theorem 7(g) remains correct.

## 5. Section 2C revisions

The relevant current proofs were read in context, including Lemmas 2-3, 11-15, 20-29 and Theorems C and Cr; the complete earlier independent reconstruction in the team records was reread. The changes preserve the audited deduction.

The escape-time estimate uses max(log(R/R1),0)/b0 and thus does not assert a negative time for a bounded set already in the trapping ball. Shrinking the curve parameter epsilon so that 2epsilon is less than its arclength preserves all previously obtained small-parameter estimates. Lemma 12's entropy proof works in finite-dimensional compact coordinate neighborhoods; it does not require the ambient neighborhood itself to be a compact manifold.

In Lemma 15, generic points on an incoming curve with backward contraction have the same component label: backward contraction makes time averages of each member of a countable separating family equal. Disintegrating over that measurable label gives the asserted component mixture. Lemma 26 now asserts the existence of a captured ergodic component, which follows by choosing a finite-length curve with a positive set of generic points and then applying the already established product capture. Its old stronger universal quantifier is not needed by Lemma 27.

For Lemma 28, countably many controlled Pesin blocks cover almost every point of the positive-measure set. Backward recurrence supplies the required times, and the established full limiting exponent justifies taking the returning subsequence. The projective cocycle in Theorem Cr integrates the logarithmic derivative of the norm exactly. The zero set of the one-form alpha has zero volume where d alpha=a i_Omega vol is nonzero: at each zero some coefficient has a nonzero derivative, so locally its zero set lies in a C1 hypersurface; a countable covering concludes. The transport identity Omega(Phi_t x)=exp(-(1+c)t)D Phi_t(x)Omega(x) has the correct sign. The C^r strain condition remains explicit; the smooth theorem's scope is unchanged.

## 6. Other repaired passages

The C55 positive-stress statement is now restricted to points of the fixed component sufficiently near x0. It no longer claims positivity throughout the component. The C44 and C45 rows and their changed historical discussion identify the configurations as empty for every omega by A960-A964. The C36 reference now points to Proposition 14. LIT263 refers to infinite pointwise value order, and C59 says that the required vorticity bound has not been derived from decay. These changes agree with the previous verdicts. The new CO66 and LIT265-LIT269 material agrees with its independent audits, subject to the density qualification in Section 4. Seven conditional criteria are counted consistently in the changed locations.

## 7. Bibliographic verification and limits

The retained publisher-supplied Crossref metadata confirms Fathi-Herman-Yoccoz, A proof of Pesin's stable manifold theorem, pages177-215 (1983), DOI10.1007/bfb0061417, and Pesin, Families of invariant manifolds corresponding to nonzero characteristic exponents, volume-year1976, pages1261-1305, DOI10.1070/im1976v010n06abeh001835. This is metadata verification only. The Oseledets metadata query returned HTTP429, so this audit does not newly certify its revised pages from that query. The actual dynamical theorem inputs were read in earlier dedicated audits; Crossref is not a substitute for their proofs.

The assembled report is still changing and has pending submissions. This finite delta check is not approval of every sentence in the report or of any stronger theorem. The bare-decay, arbitrary-helicity, all-omega conjecture remains OPEN.

## 8. A precision in the subsequent C57 suggested row

The Theory Agent C note at17:54Z suggests saying N_delta lies in R<q 'exactly when' delta<=1/2-1/q. The source theorem proves a sharp uniform guarantee for the whole reduced class, not an equivalence for each individual field. Indeed the analytic local example of A1928 has R tending to zero at its central supported common zero. Shrink its domain so that R<2 everywhere away from V=0. Since q>6, every N_delta in this domain lies in R<q, even for delta above the proposed threshold. Conversely, for each such larger delta, A1931 supplies another reduced solution having a point of N_delta with R>q.

The correct wording is: delta<=1/2-1/q guarantees ellipticity throughout N_delta, and this threshold is sharp uniformly over the reduced class. The C57 source and its previously confirmed theorem are unchanged.
