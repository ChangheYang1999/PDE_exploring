# Independent source scalars for the exactly normalized modal trial

Date: 2026-10-20. Status: CONFIRMED by independent density-moment computation, exact output audit and actual Claude Opus 5.5 review. The object is the exact modal trial of ../modal_repair/PROOF.md, not the original X3 function.

## Definitions and hypotheses

The trial has cosine factor modes a_l and density modes rho=r^3 sum_j R_j(t) sin((2j+1)theta), t=log r. Its exact stored S,D,A and knot data are in data_exact/modal_v2.json. The inner and outer six-jets are recomputed from these exact inputs. The scalar-dependent outer correction z is enclosed by the independent mpmath.iv computation in ../modal_repair/evidence/independent_gauss_iv.json. By the definition and independently verified normalization in ../modal_repair/PROOF.md, the unique dependent correction z solves sigma[rho]=3/k-1 exactly. Hence c_l=(1+sigma)/3=1/k. The interval for z encloses that exact coefficient, not an arbitrary family substituted for this definition. All source calculations use that exact definition; radius-free exported dependent decimals are not definitions or inputs.

For m=2n and the scaled density moments i_n,j_n in ../modal_green/PROOF.md, let R_L=R_(n-1), R_U=R_n. Missing modes are zero. There are 261 stream modes and no angular tail: the factor has 260 cosine modes and the projection is finite. The canonical Green quantities satisfy

A_n=e^(4t)[(R_L+R_U)/2-m i_n],
B_n=e^(4t)[m j_n-(R_L+R_U)/2].

These follow from exact integration by parts, including the center and far-field boundary conditions proved in the cited note.

## Axis scalar formulas

At (x,0), x=e^t, put w=V_1(x,0), mu=partial_y V_2(x,0), g=rho_y(x,0). Polar conversion gives U_1=-sum_m m psi_m/x and U_2/y=sum_m m(psi_m'/x-psi_m/x^2). Substituting psi_m=(A_m+B_m)/(2m) yields

w(x)=c_l x+(x^3/2) sum_n m(i_n-j_n),
mu(x)=c_l+(x^2/2) sum_n [m(m+1)i_n+m(m-1)j_n-m(R_L+R_U)],
g(x)=x^2 sum_j (2j+1)R_j(t),
g'(x)=x sum_j (2j+1)[2R_j(t)+R_j'(t)].

The canonical velocity U has zero divergence, while V=c_l X+U has divergence 2c_l. Thus w'(x)=2c_l-mu(x) everywhere on the positive axis. These identities hold for the trial even when its transport residual is nonzero. In particular mu=1 cannot be imposed at its root.

## Interval evaluation near the source

A floating logarithm is used only to choose an exact dyadic t_c within the middle spline span near x=8.600063805. Its dyadic value is then the exact integration point, with no assumed accuracy of that initial floating logarithm. Reconstruct every polynomial span by exact rational Cox arithmetic. Evaluate all inner moment initial data and all outer moment final data in Arb using the independently enclosed z. Integrate i forwards to t_c and j backwards to t_c with the finite density recurrences. Every scaled exponential moment uses the proved Taylor series and explicit geometric tail, with all hypotheses checked. No exported Green value enters these computations.

Store the exact polynomial coefficients R_j(t_c+v)=sum_l C_jl v^l for the single source span. For an interval delta=log(x)-t_c in that span, the exact ODE solutions are

i_n(t_c+delta)=e^(-(m+4)delta)i_n(t_c)
 + integral_0^delta e^(-(m+4)v)R_L(t_c+delta-v)dv,

j_n(t_c+delta)=e^((m-4)delta)j_n(t_c)
 - integral_0^delta e^((m-4)v)R_U(t_c+delta-v)dv.

These formulas hold for either sign of delta. Expand R(t_c+delta-v) by the finite binomial formula and evaluate each integral as delta^(l+1) phi_l(lambda delta), where phi_l(z)=integral_0^1 e^(zu)u^l du. The Taylor remainder is uniform on the interval z, so this also encloses every x in an input box. The interval code verifies that the box remains inside the same exact original spline span. The source-span polynomial is exact, so there is no interpolation remainder.

Direct outward values w(a)<0<w(b) prove existence of a zero in [a,b] by continuity. A strictly positive bound for w' on this interval proves uniqueness there. Rational bisection narrows the interval using only certified point signs. No interval Newton derivative is assumed. Evaluating mu,g,g' on the whole final interval encloses these values at its unique root. A=sum relation 2c_l-1 is separately distinguished from the trial's actual source eigenvalue 2c_l-mu.

## Scope and dependencies

The proof uses finite exact input arithmetic, canonical Green identities, the previously proved exponential-moment remainder, outward Arb arithmetic and the intermediate value theorem. It supplies neither a residual norm nor a statement of exact stationary profile existence. Root uniqueness is only on the certified interval unless an additional global axis argument is proved for this trial. The root enclosure is compared with the numerics claim as a separate exact-interval containment check.

## Completed verification

The 2026-10-20 run started at 15:21:36 UTC and ended at 15:30:21 UTC (524.75 seconds). It used all 261 stream modes and 1559 exact integration cells, with 667 forward cells and 892 backward cells. The exact evaluation center was t_c=2422677217427199/1125899906842624. The largest exact moment argument |lambda h| was 1480558377498019/140737488355328 <129. The initial root bracket [8.600063805156,8.600063805159] had certified opposite signs and strictly positive w' throughout. Twenty-eight exact rational sign bisections give the final bracket

2308562049166462314693/268435456000000000000 <= x_* <= 288570256145807789337/33554432000000000000.

Convenient outward rounded consequences are

- |x_*-8.60006380515717832258| < 7.8e-21;
- |(mu-1)+2.2528046115e-8| < 4.7e-19;
- |g-29.7494906633335090153| < 9.2e-20;
- |g'-0.273411443977248614| < 3.5e-19;
- |A_trial-10.150725243811138133| < 6.9e-19.

The exact stored endpoint balls, not these displayed rounded values, control the comparison in evidence/output_audit.json. All eight independently computed scalar intervals lie inside the corresponding published numerics intervals. Published JSON numbers are interpreted as binary64 round-trip values, as actually written by float conversion and json.dump in the frozen producer. The sigma, c_l and 2c_l-1 entries here check the previously verified defining normalization; they are not a new independent strain integral.

The computation source SHA256 is 8bb85cfaa0732810773c6770cbd10c2a079d1daad03aee1d0dfa7628a0c2206e; the result SHA256 is 51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691. The exact output audit completed at 15:33:09 UTC and enforced all input, Cox, moment and scalar-correction hashes. The separate executable import-binding audit completed at 15:35:46 UTC: loaded source paths and compiled function bytecode matched those pinned files, including any valid Python cache. Actual claude-opus-5-5 reviewed the derivation and accepted the clarified normalization, bisection invariant and output audit in notes/reviews/modal_source_followup_metadata.json (15:33:48 UTC). This independently validates these scalar bounds despite the separate defect in numerics' interval-Newton derivative. No conclusion about a full residual norm follows.
