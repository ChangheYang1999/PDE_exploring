# Closed-form upper bounds from the regular remainder

## Statement and scope

Let 0<alpha<1, and let dot C^alpha(R^2) be the space of real-valued functions with finite seminorm

    [f]_alpha = sup_{x!=y} |f(x)-f(y)|/|x-y|^alpha,

modulo additive constants. Define T_xx and T_xy by their circular principal-value kernels cos(2theta)/(2pi r^2) and sin(2theta)/(2pi r^2). On growing inputs define output differences through the convergent kernel-difference formula of ../../01_setup/PROOF.md. Put R_1^2=T_xx-I/2 and

    A(alpha)=Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)),
    kappa=209/500, c=72/125,
    F*(alpha)=4*2^(-alpha/2)/(pi alpha(alpha+2))
                 +kappa/(1-alpha)+c,
    G*(alpha)=2^(1-alpha)A(alpha)/alpha
                 +kappa/(1-alpha)+c+1/2.

Every such f satisfies

    [T_xx f]_alpha <= F*(alpha)[f]_alpha,
    [T_xy f]_alpha <= F*(alpha)[f]_alpha,
    [R_1^2 f]_alpha <= G*(alpha)[f]_alpha.

The same inequalities hold for complex f with the modulus seminorm, by scalar projection for each of these real kernels. The constants also bound the suprema starting from compact smooth functions. They are explicit upper bounds, not exact finite-exponent norms. Acceptance of the finite conditions is recorded at the end.

## Previously verified decomposition

Use the reflection-orbit compact costs M_j and fixed exterior transport costs E_{g,j} of ../../09_uniform_comparison/lead_certificate/PROOF.md. The group g fixes an exterior transport plan selected at the reference exponent listed there. Let

    q=sec(pi/64), phi_j=j*pi/32, 0<=j<=16,
    R_g(alpha)=q max_j (M_j(alpha)+E_{g,j}(alpha)),
    L_C(alpha)=2^(1-alpha)a2(alpha)/alpha,
    L_D(alpha)=2^(1-alpha)A(alpha)/alpha+1/2,
    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)).

The verified decomposition gives C_alpha<=L_C+R_g and D_alpha<=L_D+R_g at every exponent, with any of these fixed plans. The compact costs include the cross-pole kernels, and the local D cost includes its entire identity contribution. No singular term is included in R_g. All endpoint and infinity convergence has already been proved in the cited decomposition.

Each R_g is log-convex. For a compact reflection orbit with nonnegative mass magnitudes a,b, the plan chosen by a>=b or b>=a has cost a nonnegative combination of fixed distances raised to alpha. The choice is independent of alpha. Exterior plans have fixed nonnegative masses and distances. Their radial factors are positive moments integral u^(-alpha)du. The harmonic tail is a uniformly convergent positive sum of such moments. Positive sums and maxima preserve log-convexity. This statement applies to each fixed group, and makes no assertion about a minimum across different plans.

## Nodal bounds and the zero endpoint

The positive-exponent nodal bounds were fully audited under V081. The exact input files are recorded under source/data, with hashes checked against the accepted copies in ../../09_uniform_comparison/pass3/data. If U_C is a certified upper endpoint for L_C+R_g, then U_C minus any certified lower endpoint of L_C is an upper bound for R_g. The identical statement holds for D. Thus subtraction in the indicated direction is valid. At a node shared by groups, use the larger upper bound. The resulting values are rational decimals in source/data/remainders.json.

At alpha=0 only the regular remainder is extended. The operator itself is not being defined on dot C^0. The compact domains avoid both kernel poles. Their densities are bounded, and each distance is bounded above. For alpha in [0,1/2], every distance power is bounded by max(1,sqrt(d)), so dominated convergence applies. Zero distances occur only on null sets. Off those sets the orbit cost tends to the maximum of its two mass magnitudes in the symmetry-reduced integral.

For the exterior finite mesh, every permitted edge joins distinct angular cells or has a strictly positive enclosing chord length. At alpha=0 each edge cost is one. Total extracted flow is the extracted half-circle variation, and the residual cost is the unextracted half-circle variation. Their sum is precisely the certified half-circle variation bound, independent of the transport plan. The radial factor tends to the bin length. The tail is dominated uniformly for alpha in [0,1/2] by its geometric harmonic coefficients and the integrable radial power r^(-3/2). Consequently R_0 extends continuously to zero. Log-convexity then gives the chord inequality on the first interval [0,1/200].

The independent program ../../code/replay_closed_form_alpha0.py uses these simplified limiting costs to verify

    R_0(0)<=993975/1000000.

It uses interval geometry on 384 by 384 compact rectangles, 512 exterior angular cells, 128 radial bins, and an explicit positive harmonic-tail remainder. It does not select or solve for a transport plan.

## A finite analytic check of each chord

For consecutive rational nodes x<y in one group, let r_x,r_y be the certified positive remainder upper bounds and let

    E(t)=log(r_x)+(t-x)s,
    s=(log(r_y)-log(r_x))/(y-x),
    H(t)=kappa/(1-t)+c.

Log-convexity gives R_g(t)<=exp(E(t)). To prove exp(E)<=H, consider J=E-log H. Write u=1-t. Direct differentiation gives

    (log H)'=kappa/[u(kappa+c u)],
    (log H)''=kappa(kappa+2cu)/[u^2(kappa+cu)^2]>0.

Thus J is strictly concave. If s<=0, J is decreasing, so its maximum is at x. If s>0, a possible interior maximum has

    u=2kappa/[s(kappa+sqrt(kappa^2+4c kappa/s))],
    t=1-u.

It suffices to check x,y and this critical point if it lies in [x,y]. An interval enclosure overlapping an endpoint is also checked conservatively. The independent program ../../code/audit_closed_form_lead.py verifies negative upper endpoints for J on all 59 segments. It checks that the groups cover [0,199/200] without gaps and that each group has the required fixed nodal inputs. This is independent of the lead's 4000-subdivision procedure.

It follows that R_g(alpha)<=kappa/(1-alpha)+c on the entire central range. Adding the appropriate exact local term proves the two upper bounds there.

## The interval near one

For 199/200<=alpha<1, use the already proved elementary real upper bound U_b from ../../02_upper_bounds/PROOF.md with boundary cost b(alpha)=2^(alpha+1)/(3pi). Put delta=1-alpha. Then

    delta U_b=(2a2)^(1-alpha)
                  [2a3+delta b]^alpha/alpha,
    a3(alpha)=3/pi integral_0^(pi/6) sin(3t)(2sin t)^alpha dt.

The independent audit checks on 100 rational closed subintervals that

    delta U_b < delta L_C+kappa+c delta,
    delta U_b < delta (L_D-1/2)+kappa+c delta.

These formulas are continuous at alpha=1. The calculation uses entire exponent intervals, not sampled points. A separately derived positive series evaluates a3:

    a3=(3/pi) sum_{k>=0} c_k 4^(-k-1)
               2(alpha+5+2k)/[(alpha+2+2k)(alpha+4+2k)],
    c_k=binom(2k,k)/4^k.

After N terms its nonnegative tail is at most

    3*4^(-N)/[pi(alpha+2+2N)].

Indeed the bracketed expression is at most 3/(alpha+2+2k), c_k<=1, and the remaining geometric sum has ratio1/4. Dividing the interval inequalities by delta proves C<=F*. Since D<=C+1/2, it proves D<=G*. No numerical assertion at the excluded operator endpoint alpha=1 is needed.

## Verification status

Both verification/alpha0_replay.json and verification/independent_chord_audit.json pass. The independent alpha-zero upper endpoint is66699911/67108864, below0.993975. All66node subtractions,59chord intervals and100endpoint intervals pass. LedgerV115 accepts the complete theorem.
