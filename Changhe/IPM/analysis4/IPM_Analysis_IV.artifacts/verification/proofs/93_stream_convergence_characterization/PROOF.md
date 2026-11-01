# A stream-only criterion and recovery of coefficient bounds from an annulus

Status: PROVED after the theory part's independent review at2026-10-31T07:27Z and verifier closure V173. The all-order hypotheses for the computed rational sequence remain open.

## Setting and exact statements

Let delta=a/b be reduced in(0,1), c=(1-delta)^(-1), q_0=2b/gcd(a,2), and let f_1 be a nonzero finite real S1 sine polynomial with largest frequency L and angular l1 norm F. Use the canonical stationary log-polynomial recursion, with resonant stream constants zero. Put

    p_n=1-n delta, P_n=2-n delta,
    M_n=sum_(q,m)|[t^q sin(m theta)]F_n|,
    N_n=sum_(q,m)|[t^q sin(m theta)]G_n|,
    C_0=3-delta+2/q_0, D_0=2(L+1)C_0/(c-1).

The support and degree bounds are those proved in topics17 and88: density frequencies are at most(L+1)n-1, stream frequencies at most(L+1)n, and deg_t G_n<=n/q_0.

(A) If N_n<=H A_0^n for all n>=1, with H,A_0>0, put

    K=D_0 H,
    y_*=1+K/2-sqrt(K+K^2/4),
    B_0=A_0/y_*=A_0(1+K/2+sqrt(K+K^2/4)).

Then 0<y_*<1 and, for every n>=1,

    M_n<=F B_0^(n-1)/n,
    N_n<=H A_0 B_0^(n-1).                           (1)

For every R>e with

    B_0 R^(-delta)(log R)^(2/q_0)<1,                 (2)

the density, stream and potential series converge absolutely and uniformly on r>=R in their natural weights, with every fixed weighted Cartesian derivative. Their sums are real analytic and solve the stationary IPM equation in r>R. The strict inequality in(2) supplies the derivative margin. The theory part's original statement used every B>B_0; the proof below also permits the coefficient base B_0 itself.

(B) The following three existence assertions are equivalent for this fixed generated sequence:

1. The plain stream norms N_n have a geometric bound.
2. The series of individual stream log terms is absolutely summable at some radius R_0>e.
3. The stream series sum_n r^(P_n)G_n(log r,theta) converges uniformly on some nondegenerate closed annulus 0<r_0<=r<=r_1<infinity, r_0<r_1, and all real theta.

Each assertion therefore implies the full exterior conclusion in(A), possibly beyond a larger radius. Assertion3 is an ordinary uniform convergence statement for the grouped stream terms; it does not assume absolute summability of the individual log monomials.

## Stream-to-density majorant

The degree and frequency estimates in the proof of topic88 give, without assuming any relation between N_n and M_n,

    n M_n <= D_0 sum_(i+j=n) i N_i j M_j, n>=2.     (3)

For completeness, the stationary inverse costs at most2/((c-1)n) in the plain norm because deg_t F_n<=delta(n-2)/2. The forcing is bounded by

    (L+1)(3-delta+2/q_0) sum_(i+j=n) ij N_i M_j,

using the algebra property, the Fourier cutoffs, and the log degrees. Multiplying these estimates proves(3).

Set Y_n=nM_n. Under(A),

    Y_1=F,
    Y_n<=K sum_(i=1)^(n-1) i A_0^i Y_(n-i).         (4)

The smaller positive root y_* of Ky=(1-y)^2 lies in(0,1), and

    K sum_(i>=1) i y_*^i = K y_* /(1-y_*)^2 =1.

Inductively suppose Y_j<=F B_0^(j-1) for j<n. Then(4) yields

    Y_n<=F B_0^(n-1) K sum_(i=1)^(n-1) i(A_0/B_0)^i
         <=F B_0^(n-1).

This proves the first inequality in(1), including the boundary base B_0. Since A_0<B_0, the second follows directly from the stream hypothesis. This also independently confirms the weaker B>B_0 statement in the theory part's draft.

Topic41 supplies a common potential for any generated pair with these geometric plain bounds. Its polynomial degree and coefficient estimates, together with the support bounds, make every fixed derivative cost only a polynomial in n times(log r)^(2(n-1)/q_0). The function r^(-delta)(log r)^(2/q_0) is nonincreasing for r>=e, because delta q_0>=2. The strict inequality(2) therefore gives all stated weighted uniform convergences and permits multiplication and differentiation in the PDE. The same strict margin in a small complex neighborhood gives real analyticity. No global extension through the interior is asserted.

## Individual log summability

For1 implies2, let N_n<=H A_0^n. At t=log R>=1,

    sum_q t^q ||[t^q]G_n||_l1 <= t^(n/q_0) N_n.

Choose R large enough that A_0 R^(-delta)(log R)^(1/q_0)<1. The weighted double sum then converges geometrically. Assertion1 implies3 by(A).

For2 implies1, let S be the finite weighted double sum at R_0>e. Since(log R_0)^q>=1, the whole order-n subsum gives the direct bound

    R_0^(-delta(n-1)) N_n<=S,
    N_n<=S R_0^(delta(n-1)).                        (5)

There is no need for an additional factor equal to the number of columns. Taking A_0=R_0^delta and H=S/A_0 proves the hypothesis of(A). The theory part's bound with an extra factor n+1 is also valid.

## Polynomial coefficient recovery from a real interval

Let p(t) be a real polynomial of degree at most d, with |p(t)|<=M on[T_0,T_1], where h=T_1-T_0>0. Define

    W=2/h+|1+2T_0/h|, A=2W+1>1.

Then its plain monomial coefficient norm satisfies

    sum_q |[t^q]p| <= [2A/(A-1)] M A^d.             (6)

To prove this, map the interval to[-1,1] by x=2t/h-1-2T_0/h. The Chebyshev expansion of p(T_0+h(x+1)/2) has coefficients c_j with |c_0|<=M and |c_j|<=2M for j>=1. These bounds follow by substituting x=cos(phi), applying cosine orthogonality, and bounding the defining integrals by M. The functions T_j(x) are polynomials of degree j, so this is a finite expansion.

In the coefficient norm on polynomials in t, ||x(t)||=W. The recurrence T_(j+1)=2xT_j-T_(j-1) and the norm's algebra property imply

    ||T_j(x(t))||<=A^j.

Indeed it holds for j=0,1, and 2W A^j+A^(j-1)<=A^(j+1), since A^2-2WA-1=2W>=0. Summing the finite expansion gives

    ||p||<=2M sum_(j=0)^d A^j<=2M A^(d+1)/(A-1),

which proves(6). The estimate is elementary and exponential in degree.

## Uniform stream convergence on an annulus implies geometric coefficients

Assume3. A uniformly convergent series has uniformly bounded terms, so there exists C such that

    |r^(P_n)G_n(log r,theta)|<=C

for all n and the given annulus. Set T_i=log r_i. For t in[T_0,T_1],

    |G_n(t,theta)|<=C exp(2|T_0|+2|T_1|) exp(n delta T_1).

The harmless factor exp(2|T_0|+2|T_1|) bounds exp(-2t) throughout the interval. Every sine coefficient B_(n,m)(t) has absolute value at most twice this bound, by its Fourier integral formula. Its degree is at most n/q_0. Apply(6) to each such coefficient and sum over at most(L+1)n stream frequencies. With A from(6), this gives

    N_n <= C_1 n [exp(delta T_1) A^(1/q_0)]^n,       (7)

where C_1=4C exp(2|T_0|+2|T_1|)(L+1)A/(A-1) is independent of n. For any B>exp(delta T_1)A^(1/q_0), the factor n(base/B)^n is bounded, so(7) is geometric. This proves3 implies1 and completes the equivalence.

## Scope and dependencies

The annulus converse uses uniform convergence in both radius and the complete angular circle, finite angular support growing at most linearly, and log degree growing at most linearly. This annulus argument alone does not use pointwise convergence, and it does not infer a coefficient bound from values at a single t. Part(C) below separately proves a stronger pointwise-boundedness converse. The general inverse counterexamples in topics89 and92 are compatible with this result: they do not impose a geometric bound on the generated stream sequence. The factorial-norm counterexample in topic83 also causes no conflict, because this theorem concerns the plain monomial norm.

Dependencies: the recurrence and potential identity in topics01,10,17; the support and stationary inverse estimates in topic88; the potential reconstruction and derivative convergence theorem in topic41. The coefficient-recovery lemma is proved in full above. Sources retain the exact draft of the theory part's Proposition14.17 inspected during this audit.

## Stronger proposed converse: pointwise bounded stream terms

(C) In assertion3 above, uniform convergence can be weakened to pointwise boundedness of the individual stream terms on any nonempty open rectangle in(t,theta). In particular, pointwise convergence of the stream series at every point of one such rectangle implies a geometric bound on N_n and therefore the full exterior conclusion of(A), at a possibly larger radius.

If N_n is not geometrically bounded, the individual stream terms are unbounded on a dense residual subset of every open rectangle in(t,theta). This conditional statement does not assert that the actual rational sequence has such growth.

Here a residual set means the complement of a countable union of closed sets with empty interior. The argument below supplies all analytic estimates and the elementary category step.

### Step1: pointwise boundedness supplies a uniformly bounded rectangle

Let U be an open rectangle on which the continuous functions

    T_n(t,theta)=exp((2-n delta)t)G_n(t,theta)

are pointwise bounded as n varies. Choose a compact rectangle Q with nonempty interior inside U. Define the closed subsets

    E_j={ (t,theta) in Q : |T_n(t,theta)|<=j for every n }, j=1,2,... .

Pointwise boundedness says Q is the union of these sets. At least one E_j has nonempty relative interior. For a direct proof, if all had empty interior, construct nested closed rectangles Q_j with nonempty interior, Q_j contained in the interior of Q_(j-1), Q_j disjoint from E_j, and diameter at most2^(-j). This is possible because each E_j is closed and contains no open rectangle. Compactness gives a point in every Q_j, outside every E_j, a contradiction.

A nonempty relatively open subset of Q contains a smaller nondegenerate closed rectangle J_t times J_theta inside the interior of Q. On that rectangle all terms satisfy the uniform bound |T_n|<=j. By shrinking J_theta we may assume its length ell lies in(0,pi]. Write J_t=[T_0,T_1]. Removing the radial factor gives

    |G_n(t,theta)| <= C exp(n delta T_1)

on this smaller rectangle, where C is independent of n.

### Step2: recover a trigonometric polynomial from one angular arc

Let h(theta) be a trigonometric polynomial with frequencies between-M and M, M>=1, and suppose |h|<=V on an arc of length ell in(0,pi]. Then

    sum_(m=-M)^M |hhat(m)| <= V (2pi e/ell)^(2M).    (8)

To prove this, put N=2M and P(z)=z^M h(theta), z=exp(i theta). It is a polynomial in z of degree at most N. Interpolate it at the N+1 points z_j=exp(i(theta_0+j ell/N)), j=0,...,N. Each numerator product in a Lagrange basis polynomial has coefficient l1 norm at most2^N, since all |z_j|=1. Also

    |z_j-z_k|=2sin(|j-k|ell/(2N))
              >=2|j-k|ell/(pi N),

using sin x>=2x/pi on[0,pi/2]. Consequently,

    product_(k!=j)|z_j-z_k|
       >=[2ell/(pi N)]^N j!(N-j)!.

The interpolation formula and sum_j1/(j!(N-j)!)=2^N/N! therefore give

    ||P||_coeff <= V (2pi N/ell)^N/N!
                  <=V(2pi e/ell)^N.

The last inequality follows from N!>=(N/e)^N, for example by summing log k and comparing with the integral of log x on[1,N]. Multiplication by z^M preserves the Laurent coefficient norm, proving(8). The case M=0 is immediate.

### Step3: recover the log-polynomial coefficients

Apply(8) at each t in J_t to G_n, with M bounded by(L+1)n. Thus its full angular coefficient norm, and in particular every sine amplitude, is bounded on J_t by

    C exp(n delta T_1)(2pi e/ell)^(2(L+1)n).

For a sine polynomial the angular Fourier coefficient l1 norm equals the sum of absolute sine amplitudes, because each sine amplitude contributes two coefficients of modulus half its own. Apply the radial polynomial estimate(6), using degree at most n/q_0, to each sine amplitude. There are at most(L+1)n amplitudes. It follows that

    N_n <= C_2 n [ exp(delta T_1)
                     (2pi e/ell)^(2(L+1)) A^(1/q_0) ]^n.

Absorbing the factor n into any slightly larger geometric base proves(C).

### Residual unboundedness when there is no geometric bound

If N_n has no geometric bound, the preceding estimates show that no E_j can contain a nonempty open rectangle, in any chosen compact rectangle Q. Each E_j is closed with empty interior. Their union is precisely the set of points where the stream terms are bounded. Its complement is a dense countable intersection of open sets by the same nested-rectangle argument. At each point in that complement the individual terms are unbounded, so the series cannot converge there.

This converse is non-effective when only pointwise boundedness is assumed: the category argument does not provide the location of the smaller rectangle or the bound j. Quantitative coefficient or radius bounds still require quantitative input.
