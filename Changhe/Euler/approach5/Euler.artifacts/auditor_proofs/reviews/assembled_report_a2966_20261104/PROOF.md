# Audit of report564edbe5 and the LIT353 transfer

## 1. Exact assembly and scope

The checked report is SHA256 564edbe56b4930db4642afb07c3fb48054d87f5f38ae0e98096b85b8a1bb9060, with 7126 lines, at verdict cutoff A2966. Its predecessor is03952aa34e14ba3375b787101bfed460c4edb477d87ec6e69320e574b3dcfab7, approved at its stated scope in A2970. Both submitted reports, the coordinator's ordinary and cumulative differences, an independent unified difference and the complete changed LIT338 row are retained in verification.

The three current changes are the status line, the LIT338 row and the revision-history entry. The complete changed row has14571 characters and was read in full, with its end reread separately after a combined tool output was truncated. The cumulative difference also includes the previously checked provenance changes of report03952aa3. Every changed passage has been compared. Sections2A through2D are byte-identical between these two latest reports. The current report and Euler.report copies equaled the retained pin when checked.

The approval scope is the front matter, main Sections0-10 and AppendixA, under the qualifications already attached to their references. The revision entry is checked as a record of this change. Historical AppendicesB and C are not collectively recertified by a new whole-text reading.

## 2. Exact local-tail conclusion

For a bounded planar disc D let F be nonempty, compact and have empty interior, with F contained in D. Let U be an open neighborhood of F whose closure is contained in D, and let kappa>0. LIT353 constructs a nonnegative measurable b, finite everywhere, zero on F, smooth on D minus F and supported in U, with

    M^2 = sup_(t>0) t^2 |{b>t} in D| <= 16 pi kappa^2/3.

It belongs to Lp(D) for every0<p<2. For every open disc V contained in D and meeting F,

    T_V(b) = limsup_(t->infinity) t^2 |{b>t} in V| >= pi kappa^2,
    integral_V b^2 = infinity.

Here the subscript is restored to make the disc dependence explicit. The report defines the same quantity on discs and suppresses that subscript consistently. The underlying proof is the already confirmed seven-section reconstruction in nonadditive_weak_tail_20261104, with source claim A2963 and tail claim A2964.

The support construction is locally finite off F. Consequently each point x in D minus F has a disc V with closure in D minus F on which b is bounded; T_V(b)=0. If n is a positive integer and kappa=n/2, every point of F has T_V(b)>=pi n^2/4 on every such disc about it, whereas every point outside F has a zero-tail disc. Thus the set of points with no disc on which T_V(b)<pi n^2/4 is exactly F. This is a statement about an explicitly constructed coefficient, not about the zero set of any solution.

If F contains six distinct points, choose six pairwise disjoint small discs about them, all contained in D. Their tail quantities have sum at least6 pi kappa^2, strictly greater than16 pi kappa^2/3 and therefore greater than M^2. The report's nonadditivity assertion follows. A perfect F is permitted because the construction requires only compactness and empty interior.

## 3. Why the finite zero-index budget survives

For the separate smooth scalar inequality |partial_bar f|<=b|f|, a finite-order zero has a homogeneous leading term, a circle coefficient A(theta), and charge d=(1/2)integral|A(theta)|^2. Equation10 of weak_l2_zero_index_budget_20261104 proves, on each sufficiently small disc V about that zero,

    liminf_(t->infinity) t^2 |{b>t} in V| >= d.

For finitely many disjoint such discs the superlevel measures add at each fixed t. The finite-sum lower-limit inequality then gives sum d<=M^2. This is precisely the stronger asymptotic lower bound that permits summation. LIT353 instead supplies lower bounds for separate upper limits, possibly achieved at different threshold subsequences. No analogous upper-limit summation is valid, and its failure contradicts none of the lower-limit argument. The report correctly keeps the finite zero-index budget and the new coefficient obstruction separate.

No scalar solution, carrier, pressure or Euler profile is produced by LIT353. In particular, the arbitrary-norm finite-regularity scalar continuation question and the Euler coefficient estimate remain open. The report keeps A2965 in its OPEN list and A2963-A2964 in its CONFIRMED list.

## 4. Comparison and the corrected compact-annular sentence

The full Theory Agent A  Note A106 was read. Its comparison of the three changed passages and its six-disc arithmetic agree with Sections1-3. Its regeneration counts were not independently rerun here; the independent report-wide syntax check below is separate evidence. The earlier Theory Agent C  LIT353 comparison was already read with its complete script and logs in A2966. Its optional support-equality and finite-sample claims retain the explicit qualifications recorded there. Neither is used by the report.

The report now says that the compact-annular repairs are those of Proposition6.3 and Corollary6.4. This removes the possible implication that the displayed equation in Example4 had been repaired in that way. The earlier verdicts remain distinct: A2932 refutes that equation, A2933-A2934 refute the overly broad estimate scopes, A2935 confirms their compact-annular repairs, and A2937 checks persistence of the source defects. The main compact-support continuation theorem is not refuted.

The LIT353 status revision from submitted hash97e2e1d9a3b2df9ffb3a687ae393fa789cd72e0151a2325c9e525d5ccf1be41f to85193dc8066f52151cab510cd6e1774a8861146c7b5dbe8df7549b721d26379a was read as a complete difference. Only status and comparison scope change. The source correctly states support containment and says that its agent did not read or rerun the C diagnostics. No stronger theorem is inserted.

## 5. Additional energy-chain review

The separate literature-agent review at hash1ce84fa7f2dab8f8e37d0c6e232ef2b8b442cd95fec5dd09a87d0e8d1bb02af2 has five sections and28manual checks. All were read. It concerns the classical energy theorem for C1 exact whole-space profiles,0<c<1, bounded U and zero distributional dilation limit. It retains alpha=5-2/c, g(R)=R^(-alpha)integral_(B_R)|U|^2, the subcritical vanishing, critical finite energy with R^-5 tail, and the positive limiting normalized energy for nonzero supercritical profiles. The quantitative constants in this theorem are independent of omega; the pressure-normalization argument can use fixed test coefficients depending on omega without altering that assertion.

Its proof matches the already fully reconstructed energy_law_recheck_20261104: the canonical pressure gradient is defined on transformed derivative tests in L1, the harmonic remainder is removed using dilation and moving radial mean tests, and the annular pressure has one spatial constant. The inner pressure estimate4E(R/2)/(pi R^3) is used only on the annulus. The outer estimate192R I(R)/pi uses I(R)<=4integral_(4R)^infinity r^-5 E(r)dr; the discarded lower boundary term is nonpositive and the upper boundary tends to0 because E=O(R^3).

The exact flux identity has coefficient1-5c/2 and permits an independent constant on each annulus because divergence-free U has zero flux across every sphere. The dyadic iteration treats the logarithmic equality case and a final partial interval. At c=2/5, finite energy is proved before the exterior-energy improvement is used; the recurrence min(tau+1,(5+tau)/2), followed by Young's inequality at tau=4, yields the R^-5 tail without assuming it. The natural-tail and Lorentz consequences keep their stated additional premises.

For bounded-background normalization, the harmonic gradient difference is first a tempered harmonic polynomial and then a constant by dilation testing. With M=(1-c)I+omega J and background b=-M^(-1)g0, the bounded dilation limit solves the homogeneous transport equation after subtracting b. Its essential supremum is invariant under the invertible spatial linear map and multiplied by exp(-(1-c)t), hence is zero. The shift z0=-(cI-omega J)^(-1)b and pressure correction +(Mb).y have the signs needed to reduce to zero background.

The review accurately excludes a fresh proof of the weak-profile energy-defect theorem and excludes fresh primary-source verification of Hardy-Littlewood-Sobolev and O'Neil. It does not claim to have independently reread all of Section2C. Its finite-energy and normalization reasoning is not circular. The detailed proof is an explicit dependency here, rather than a newly claimed full derivation of every corollary.

## 6. Static verification and evidence limits

At the captured cutoff, all222 explicit confirmation lists contain only confirmed verdicts. All2485 distinct positive report references resolve. Nine Markdown tables,600 table lines and582 data rows pass the column check. Four mathematical norm blocks are correctly excluded from table parsing. No absolute local path or em dash occurs in the report. The scripts and their complete JSON outputs are retained; these are syntax checks, not proofs.

The Pan-Zhang slicing-source revision captured alongside this work has hash722318d490915b86d05e3fd228a343a4ab980829e90fc29c49b13717e4fd3bd3. Its complete new Section9 and pointer correction were read. They now describe the actual publisher copy, its persistent minor defects, and the peripheral hybrid-L2 sentence. This revision is not in report564edbe5 and receives no slicing-theorem verdict in this assembly audit. The separate independent nine-section reconstruction and the existing-model comparison process remain the appropriate evidence for that question.

## 7. Verdict scope

The added LIT353 passage and the corrected compact-annular attribution are sound. Report564edbe5 is cumulatively approved at cutoffA2966, under the prior exact theorem scopes. The separate energy review accurately checks the classical theorem and background corollary while identifying its imported results. The LIT353 status change is also accurate.

This gives no unrestricted Euler nonexistence result. Smooth coverage requires its stated regularity; finite-Cr coverage requires its explicit growth condition; the helicity theorem requires its sign condition. The configured model A/C comparison is through the existing files, with actual provider execution independently unattested. The static checks used only the permitted local Python interpreter and one worker.
