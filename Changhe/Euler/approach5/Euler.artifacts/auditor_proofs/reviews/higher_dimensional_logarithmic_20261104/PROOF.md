# Distributional logarithmic continuation in several complex variables

This is an independent reconstruction of LIT354, submitted source SHA256 b2ced346c386e5deb0febc284fd10af2257a074241c48d1f8d44769f11784834. All eight source sections and 46 manual checks have been read. The existing configured model comparison is pending at initial writing. No Euler conclusion is asserted.

## 1. Exact statement and dependencies

Let n,N be positive finite integers, d=2n, Rstar>0, and B={z in C^n:|z|<Rstar/e}. All measures are ordinary Lebesgue measures. The norm on C^N and the norm on the n-by-N derivative array are Euclidean. Write dbar_j=(partial_xj+i partial_yj)/2 and partial_zj=(partial_xj-i partial_yj)/2.

Suppose u is in L1_loc(B;C^N), g is in L1_loc(B minus {0};C^(nN)), and dbar u=g in distributions off 0. Suppose also

    |g(z)| <= [1/4+1/(8 log^2(Rstar/|z|))] |u(z)|/|z|

almost everywhere off 0, and integral_(|z|<r)|u|=o(r^L) as r decreases to 0 for every positive integer L. Then u=0 almost everywhere on B.

A separate regularity conclusion holds if the displayed majorant is replaced by C0|u|/|z| for any finite C0>=0: the equation extends across 0, and u belongs to W1,q_loc for every finite q>1. This regularity statement does not assert continuation for arbitrary C0.

The non-elementary continuation input is the planar LIT351 theorem, CONFIRMED A2942: on D_S={|w|<S/e}, a finite complex vector v in L2_loc, H1_loc off 0 and of infinite L2 integral order at 0 vanishes if |dbar_w v|<=[1/4+1/(8 log^2(S/|w|))]|v|/|w| almost everywhere. The analytic dependencies used below are distributional Weyl's lemma for the Laplacian, harmonic Liouville, local Lq constant-coefficient elliptic estimates for dbar for 1<q<infinity, and Sobolev and Morrey embeddings on balls. They are named inputs, not newly proved external theorems. The fundamental kernel, interpolation, finite iteration and slicing reductions are derived below.

## 2. Weighted flatness removes the singular point

For any fixed M>0 and integer m>=1, infinite L1 integral order gives, for sufficiently small t and every 0<s<=t,

    integral_(|z|<s)|u| <= epsilon s^(m+M).

An integer flatness order strictly greater than m+M gives this bound, so M need not be integral. On the annulus t/2^j<|z|<=t/2^(j-1), multiply the mass bound at its outer radius by (2^j/t)^M. Summing for j>=1 gives

    integral_(|z|<t) |u|/|z|^M
      <= epsilon 2^M t^m sum_(j>=1) 2^(-m(j-1))
      <= epsilon 2^(M+1)t^m.

Thus every weighted function |u|/|z|^M is locally integrable and itself has infinite L1 integral order at 0. In particular the inverse-radius bound makes g integrable across 0.

Let eta_epsilon be zero on B_epsilon, one outside B_(2epsilon), and have gradient bounded by C/epsilon. Test the punctured distributional equation after multiplication by eta_epsilon. The extra term has L1 norm at most C epsilon^(-1) integral_(B_(2epsilon))|u|, which tends to zero. Dominated convergence handles eta_epsilon u and eta_epsilon g. Hence dbar u=g on the full ball, with no residual distribution at 0. The given equation off 0 is essential to this step.

## 3. A weak estimate supplies the first integrability gain

Let sigma be the area of the unit sphere in R^d. A fundamental solution of Delta Gamma=delta_0 is Gamma=(log|x|)/(2pi) for d=2 and Gamma=-|x|^(2-d)/((d-2)sigma) for d>2. Direct differentiation in either dimension gives

    4 partial_zj Gamma(x)=2 conjugate(z_j)/(sigma |x|^d).

Choose chi smooth and compactly supported in the given ball, equal to one on an arbitrary smaller ball. Put v=chi u and h_j=chi g_j+(dbar_j chi)u, extended by zero to R^d. Both are compactly supported L1 functions, and h=dbar v in distributions. Define Rh=4 sum_j (partial_zj Gamma)*h_j. Its kernel, acting on the full derivative array, has operator norm at most C_d|x|^(1-d), where C_d=2/sigma. Cauchy-Schwarz over j proves this bound without a target-dimension factor.

The kernel is locally integrable. Tonelli gives local integrability of Rh. Since Delta=4 sum_j partial_zj dbar_j, compatibility h=dbar v implies Delta(v-Rh)=0. Weyl's lemma makes the difference a smooth entire harmonic vector. Outside a ball containing the supports, v=0 and |Rh(x)|<=C(|x|-R)^(1-d) ||h||1, which tends to zero. The harmonic difference is bounded on the remaining compact ball and therefore globally bounded. Harmonic Liouville gives v-Rh=0. This is not an inverse formula for an arbitrary incompatible array h.

For clarity, set M=||h||1. If M=0 the conclusion is immediate. Split the kernel at a radius a>0. Its near part has L1 norm at most C_d sigma a=2a. Its far part has supremum norm at most C_d a^(1-d). Choose a=(2 C_d M/lambda)^(1/(d-1)); the far convolution is at most lambda/2. Chebyshev and Tonelli then give

    volume{|Rh|>lambda} <= 4aM/lambda
      =4(2C_d)^(1/(d-1)) (M/lambda)^(d/(d-1)).

Thus Rh has the global weak exponent d/(d-1). On every finite-measure set it belongs to Lp for 1<p<d/(d-1), by integration of distribution functions. We may start with p0=2d/(2d-1), whose reciprocal is 1-1/(2d). The same argument works in a ball avoiding 0 whenever u and g are locally L1 there.

## 4. The bootstrap terminates after finitely many steps

Assume u is locally Lp for some p>1 near 0. For 1<q<p put eta=(p-q)/(p-1). Then eta is in (0,1) and q=eta+p(1-eta). Holder gives

    integral (|u|/|z|)^q
      <= (integral |u|/|z|^(q/eta))^eta
         (integral |u|^p)^(1-eta) < infinity.

The first factor is finite by Section 2. Therefore g and u are locally Lq. The stated elliptic estimate gives W1,q regularity on a smaller ball.

While 1/p>=1/d, choose 1/q=1/p+1/(4d). At the first step 1/q=1-1/(4d)<1, and subsequent values only decrease, so q>1 throughout. Also q<p and q<d. Sobolev embedding then gives a new exponent with

    1/p_new=1/q-1/d=1/p-3/(4d).

The reciprocal decreases by a fixed positive amount. Its first value below 1/d is at least 1/(4d), because the previous value was at least 1/d. Thus it stays positive and reaches p>d in finitely many steps. For example the number of these steps from p0 is floor((4d-6)/3)+1. Only finitely many nested-ball shrinkages are needed; an arbitrary fixed compact target ball can be retained by choosing the intermediate radii in advance.

Now choose d<q<p and apply the same weighted interpolation and elliptic estimate. Morrey gives local boundedness. For every finite q>1,

    integral (|u|/|z|)^q
       <= ||u||_infinity^(q-1) integral |u|/|z|^q < infinity.

A further elliptic estimate gives W1,q. Away from 0 all these weights are bounded on a sufficiently small ball, and g has a bounded coefficient times u. The initial gain and finite elliptic iteration work there as well. This proves W1,q_loc throughout the original ball. Continuous representatives from the different exponents agree, since they agree almost everywhere.

## 5. Flatness is uniform in direction

Fix q>d on a compact interior ball and let alpha=1-d/q. Morrey supplies K>=0 such that |u(x)-u(y)|<=K|x-y|^alpha on a smaller ball. Continuity and integral flatness imply u(0)=0. If K=0, u is zero on this ball. Otherwise take z with |z|=r small, let m=|u(z)|, and suppose m>0. Since m<=Kr^alpha, the radius a=(m/(2K))^(1/alpha) is at most r. On B_a(z), |u|>=m/2, and that ball is contained in B_(2r)(0). With v_d the unit-ball volume,

    integral_(B_(2r))|u|
       >= (v_d/2)(2K)^(-d/alpha) m^(1+d/alpha).

Choose an integer L>k(1+d/alpha) in the flatness hypothesis. The inequality implies |u(z)|<=C_k r^k near 0, uniformly in direction. This argument uses the vector norm directly. Every radial complex slice therefore has infinite L2 integral order at 0: its mass on |w|<r is at most C_k^2 pi r^(2k+2)/(k+1), and k is arbitrary.

## 6. Complex slices and their exact derivative norm

Fix 0<R<Rstar/e with a slightly larger closed ball still in B. For every nonnegative measurable H the complex polar formula is

    integral_(|z|<R) H(z) dz
      =(1/(2pi)) integral_(S^(d-1)) integral_(|w|<R)
            |w|^(d-2) H(w zeta) dA(w) dS(zeta).

Write w=r exp(i theta), use invariance of sphere measure under multiplication by exp(i theta), and compare with ordinary real polar coordinates to obtain this identity. Tonelli justifies it without an initial integrability assumption.

Choose p>d. Formula above makes the restrictions of u and Du weighted Lp for almost every unit zeta. Holder makes them unweighted L2 because

    integral_(|w|<R) |w|^(-2(d-2)/(p-2)) dA(w)<infinity.

For d>2 this is equivalent to p>d; for d=2 the weight is one and is integrable for every p>2 as already chosen. Approximate u in W1,p(B_R) by smooth u_j. Morrey gives uniform convergence. Choose a subsequence whose p-th powers of gradient errors have a summable sum. The polar formula and Tonelli give weighted Lp convergence of the restricted gradients for almost every zeta. Holder with the integrable weight |w|^(-(d-2)/(p-1)) gives unweighted L1 convergence. Passing the smooth real chain rule to distributions yields, for v_zeta(w)=u(w zeta),

    v_zeta in H1({|w|<R};C^N),
    dbar_w v_zeta=sum_j conjugate(zeta_j) g_j(w zeta).

The conjugates are necessary: differentiating conjugate(w zeta_j) with respect to conjugate(w) gives conjugate(zeta_j). Finite intersections handle the finitely many components. The polar formula applied to the indicator of an ambient exceptional null set shows that it is null on almost every selected slice away from w=0. The weight is strictly positive there.

Finally, Cauchy-Schwarz over j with sum_j|zeta_j|^2=1 gives |dbar_w v_zeta|<=|g(w zeta)|. This uses the full n-by-N Euclidean array norm. Neither n nor N changes the coefficient. Section 5 gives flatness on all these continuous slices.

## 7. The scale comparison and conclusion

The logarithm in Section 1 exceeds one on B. Its coefficient is therefore at most (3/8)/|z|, so Sections 2-6 apply with C0=3/8. On |w|<R the slice satisfies the original majorant with Rstar. Set S=eR<Rstar. Then

    1<log(S/|w|)<=log(Rstar/|w|),

so replacing Rstar by S enlarges the allowed logarithmic correction. The planar LIT351 hypotheses now hold on its exact disc D_S={|w|<R}: local L2, punctured H1, infinite L2 integral order and the correct coefficient bound. Thus v_zeta=0 there for almost every zeta. The polar formula implies u=0 almost everywhere on B_R.

Take a countable increasing sequence R tending to Rstar/e. The conclusion follows on B. No common exceptional set for uncountably many radii is needed, and no propagation theorem outside B is imported.

## 8. Positive corollaries and their limits

The coefficient C/|z| with 0<=C<=1/4 is bounded by the coefficient of Section 1, so the same distributional L1-flat hypotheses imply zero. For a local coefficient [1/4+A/(log(1/r))^p]/r with A,p>0, there is also continuation when p>2 or when p=2 and A<=1/8. For p>2 take T>=1 with A t^(-p)<=1/(8t^2) for t>=T; use Rstar=exp(1-T) and r<exp(-T). The shifted logarithm is t-T+1, in (1,t], and its correction dominates 1/(8t^2). For p=2 and A<=1/8 the same comparison works. These are local conclusions near 0, with no unmentioned conditions beyond that neighborhood.

The sharpness examples of LIT352 have one complex source variable and two complex target components. Extending them to depend only on z_1 in C^n would give a coefficient involving |z_1|, not the smaller inverse-radius coefficient involving |z|. Hence no higher-dimensional sharpness is established here. There is no theorem for arbitrary weak Ld coefficients, no resolution of the general finite-regularity scalar weak-L2 question, and no Euler-derived majorant.

## 9. Verification scope

The source's eight sections and all 46 manual checks were read. This proof explicitly separates its standard analytic inputs and the previously confirmed LIT351 continuation theorem. It does not depend on accepting the separate Pan-Zhang source audit. The exact constants in the continuation statement survive because the elliptic bootstrap constants affect regularity only, while the final slicing inequality has norm one. No computation or formalization was needed. The existing configured model comparison remains pending at initial writing; actual provider execution is independently unattested.


## 10. Existing model comparison and diagnostic limits

The complete Theory Agent C  comparison dated 2026-11-04T05:33:05Z, its 120-line Python script and its 27-line retained log have now been read. The comparison independently follows all eight source sections and the nine sections above. It agrees on puncture removal, compatibility of the fundamental-solution representation, the finite bootstrap, uniform flatness, distributional slicing and the smaller planar scale. This is the existing configured model agent; actual provider execution is independently unattested. No new client or agent was used.

The optional dimension-two qualification is correct: the weight in the L2 slice estimate is one, so the strict condition p>d is sufficient rather than necessary there. Section 6 above already makes that distinction. For d>2, the displayed integrability threshold is precisely p>d. This does not alter the chosen exponents or any conclusion.

The retained log contains 26 PASS entries: 18 SYM, four EXACT, one QUAD, two EX and one GRID. The script was not rerun. The four EXACT entries are finite rational tests of the geometric sum, reciprocal-exponent iteration and slice weights; they do not themselves prove the corresponding assertions for all dimensions or exponents. The geometric-series formula and fixed reciprocal decrease in Sections 2 and 4 supply those general arguments. Some symbolic checks likewise select particular dimensions or a polynomial slice; the general kernel and chain-rule arguments are given above.

The quadrature checks the complex polar formula in dimension four using a Gaussian polynomial integrand with a non-invariant term. Its two EX controls alter the normalization or radial weight and are numerical, as is the final GRID check. Their logged values are diagnostic evidence only. No numerical result is used as a premise of the theorem. The direct polar-coordinate derivation proves the normalization and weight for every even dimension.

The regularity theorem and continuation theorem therefore have separate scopes. Any finite inverse-radius constant suffices for regularization of a distributional L1-flat solution. Continuation uses the stated logarithmic majorant and the independently confirmed planar LIT351 theorem. Neither the regularization argument nor a one-variable embedding proves arbitrary higher-dimensional sharpness, general weak-Ld continuation, the unresolved scalar endpoint, or an Euler majorant.
