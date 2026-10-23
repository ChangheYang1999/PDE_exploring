# An elementary complete axis inverse at P=2

Result240. This proof is written before the evaluator and its tests. It applies to the finite auxiliary hydrostatic densities used in the c=2 computations. It is not a formula for the full elliptic IPM inverse.

## Statement

Let C>0. Let k(w)=sum_(j=1)^d k_j w^j and H(w)=sum_(j=1)^e h_j w^j be real polynomials with zero constant coefficients. For y>=0 let t in [0,1) be the unique solution of

    y=C t/(1-t^2)^2,

and write w=1-t^2 and G(y)=y H(w). The complete vertical inverse on the axis has derivative V'(y)=k(w(y)) and gauge V(0)=0. Then

    V(y)=C[2k_1 t/(1-t^2)+(4k_2-k_1)atanh(t)+P(t)],                (1)

where missing coefficients are zero and the odd polynomial is

    P(t)=-3k_2 t
         +sum_(j=3)^d k_j sum_(m=0)^(j-3) (-1)^m binom(j-3,m)
              [t^(2m+1)/(2m+1)+3t^(2m+3)/(2m+3)].                (2)

This expression includes the entire line inverse, not a finite cutoff. It has no series truncation error. Floating evaluation still needs enough precision to control cancellation in P. The input coefficients and P can be stored as exact rational JSON when the input data are rational.

The scalar identity determines the axis velocity of the auxiliary inverse because symmetry gives V(0)=0 and the complete inversion gives V'=k. These are precisely the hypotheses of the previously checked axis primitive. Arbitrary k,H in this statement are manufactured fields; only coefficients derived from a frozen density represent that density's actual auxiliary inverse.

## Derivation

The coordinate map is strictly increasing from zero to infinity, since

    dy/dt=C(1+3t^2)/(1-t^2)^3>0.

Thus V=C sum_j k_j int_0^t (1+3u^2)(1-u^2)^(j-3)du. At j=1 and j=2 the primitives with value zero at zero are

    2t/(1-t^2)-atanh(t),
    4atanh(t)-3t,

respectively; direct differentiation verifies both identities. For j>=3, expand the integer power by the binomial theorem and integrate each monomial. This gives (1)-(2). Differentiation and V(0)=0 prove uniqueness. The construction does not introduce an additive vertical constant or a harmonic strain.

The P=2 logarithmic constant in research/hydrostatic_axis_log_constant/PROOF.md follows from this expression as well. Write B=C(k_2-k_1/4), Q=k_1 sqrt(C)/2. Then V=4Q sqrt(y)+B log(y)+M+O(y^-1/2). For j>=3 the constant contribution is

    C k_j int_0^1 (1+3u^2)(1-u^2)^(j-3)du
       =C j k_j Beta(j-2,3/2).

For example the equality follows by the beta substitution v=u^2 and its elementary recurrence; integration by parts yields the same identity. The j=1,2 finite parts give

    M=C[k_1(-1/2-log2)+k_2(4log2-3)
         +sum_(j>=3)j k_j Beta(j-2,3/2)]-B log C.

Consequently the elementary formula and the independently derived subtracted-tail formula must agree; their numerical comparison tests different cancellation patterns.

## Axis derivatives and extrema

For y>0 set d(w)=2-3w/2 and a(w)=w(1-w)/d(w). Differentiating y=C sqrt(1-w)w^-2 gives w'=-a(w)/y. Hence

    G'=H-aH',
    G''=[(1-a')H'-aH''] w',
    R=(2y+V)G'-G,
    R'=(1+k)G'+(2y+V)G''.

Primes on H,a denote w derivatives; primes on G,V,R denote y derivatives. Where G>0 and (2y+V)G'>0, the force denominator is N_f=2G+R. Therefore

    (R/N_f)'=2(R'G-RG')/N_f^2.                                  (3)

The sign assumptions must be checked at the evaluated points; if they fail, use the original absolute-value denominator. On a region where R has fixed nonzero sign, extrema of |R|/N_f satisfy R'G-RG'=0. Zeros of R are possible minima and must not be confused with maxima. The formulas permit a fine logarithmic scan and scalar bracket refinement without numerical differentiation of the producer's interpolant. A finite scan with refined sign changes is not a proof that every stationary point has been located. Report sampled and refined maxima as lower bounds for the supremum, with the search range and all brackets. No grid maximum is a uniform PDE error bound.

## Verification and scope

First compare both rational primitives by symbolic differentiation. For general finite rational k, construct P by exact arithmetic, compare V and V' with independent high-precision quadrature in t, and compare G',G'',R' with scalar differentiation. Test both signs, log-free examples and several scales. Compare (1) with the earlier complete subtracted-series inverse at two precisions before using saved states. Store the resulting rational P and source hashes. For candidate-derived data, use enough digits for all rational polynomial coefficient sizes, and refine representative peaks at higher precision.

All conclusions concern the auxiliary axis inverse of exact finite trial formulas. Nonzero residuals exclude only those trial formulas as exact auxiliary solutions. They imply neither a full-plane IPM candidate nor nonexistence of one. The Setting III endpoint remains UNRESOLVED.
