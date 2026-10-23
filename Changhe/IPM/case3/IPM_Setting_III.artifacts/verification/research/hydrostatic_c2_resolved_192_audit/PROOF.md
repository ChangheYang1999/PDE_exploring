# Resolved c=2 N192 auxiliary state: independent audit

Result265, written before computation. The exact saved input is hsG_c2.0_N192_log, independently frozen in verification/INPUTS.json. The producer reports line-search failure at step69 after68 accepted steps; this termination claim is to be checked against the frozen log. The N96 and cappedN128 states were assessed in result235, continuedN128 in238, and N160 in242. This is a new coefficient file at a new resolution, so all exact and numerical diagnostics must be recomputed. The present statement is an audit protocol, not a passing verdict. Subsequent numerical findings belong in verification/ and VERDICT.md.

The setting is the auxiliary hydrostatic equation (2X+V).grad g=g, with V1(x,y)=-integral_y^infinity g_x(x,t)dt and V2(x,y)=integral_0^y t g_xx(x,t)dt+y integral_y^infinity g_xx(x,t)dt for x,y>=0 and parity continuation. Its stream solves -Phi_yy=g_x. These integrals fix the homogeneous terms. The finite smooth density has p=1/2, so the tails converge. This is not the isotropic Poisson inverse of full IPM and is not a full IPM candidate.

The exact origin relations for an auxiliary solution with a=g_y(0)!=0 are cH=V2_y(0)=-1 and DW(0)=diag(3,1). For an arbitrary saved state set delta=2+cH-1. If g=ay+bx^2y+ey^3+O(r^5), then the linear residual is a delta y and the axis cubic residual coefficient is e(2+3delta)-ab/3. The two exact independent center expressions and their complete quadrature cross-check in result235 apply to every polynomial in this representation; the same source reader reconstructs this new file without importing producer code. Independent Cartesian derivatives are compared with scalar differentiation of the radial-angular reconstruction at70 and100digits.

For each of774 physical probes, R=(2x+V1)g_x+(2y+V2)g_y-g, Nf=|(2x+V1)g_x|+|(2y+V2)g_y|+|g| and Nv=|g|+|xg_x+yg_y|+|V1g_x+V2g_y|. Zero denominators remain undefined. Use three complete inverse rules32/96/16,48/160/64 and64/192/128, followed by88/256/512 at each regional maximizing point. Extents10,100,10000 and all quadrants/axes are retained. Quadrature agreement is empirical and does not enclose unsampled points.

For the exact map P=2, let y=C sqrt(1-w)w^-2, C=L/4, H(w)=g(0,y)/y and k(w)=integral_y^infinity g_xx(0,t)dt. Both are polynomials with zero constant coefficients. Write H=sum h_j w^j, k=sum k_j w^j. The established axis formula gives
 K=h1 sqrt(C), Q=k1 sqrt(C)/2,
 c2=C(h2-h1/4), c3=C^(3/2)(h3-h2/2-h1/32),
 B=C(k2-k1/4), r2=-c2+2KQ,
 M=C[k1(-1/2-log2)+k2(4log2-3)+sum_(j>=3) j k_j Beta(j-2,3/2)]-B log C.
Thus G=g(0,y)=K sqrt(y)+c2+c3/sqrt(y)+O(y^-1), V2=4Q sqrt(y)+B log y+M+O(y^-1/2). Direct substitution into R=(2y+V2)G'-G and Nf=2G+R for large positive y, when K>0, gives
 yR/Nf=r2 sqrt(y)/(2K)+(B/4)log y+M/4-c3/K-r2(2c2+r2)/(4K^2)+o(1).
For finite radii all absolute values in Nf are evaluated directly. The proof of the expansion and the exact finite-radius primitive are result234; the summary reconstructs M through a separate positive-beta recurrence. No1<P<2 finite-part formula is evaluated at its P=2 pole. The angular complete cusp coefficient is evaluated by the independent rational kernel and monomial beta formula of229, including the factor sqrt(C); these two formulas and their manufacture gate are unchanged.

A comparison with the frozen earlier resolutions is meaningful only on identical physical probes and identical complete-inverse rules. Compare exact center and far coefficients separately from the optimizer's node loss. A decrease of the latter without convergence of residuals, jets and tails is not convergence of profiles. No conclusion about another solution or the full elliptic IPM problem follows from a failed individual auxiliary state.

Dependencies: result235 research/hydrostatic_c2_resolved_audit/PROOF.md and SUMMARY_PROOF.md; result234 research/hydrostatic_axis_log_constant/PROOF.md; the independent inverse, exact primitive and cusp proofs referenced there. All source and manufacture hashes must match. Current endpoint UNRESOLVED; no early finish.
