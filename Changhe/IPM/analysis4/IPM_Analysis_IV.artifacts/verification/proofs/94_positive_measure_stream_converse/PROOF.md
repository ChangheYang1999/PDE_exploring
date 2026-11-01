# Bounded stream terms on a positive-measure set force geometric coefficients

Status: PROVED after the theory part's independent review at2026-10-31T07:27Z and verifier closure V173. The all-order hypotheses for the computed rational sequence remain open.

## Statement and scope

Let delta=a/b be reduced in(0,1), let q_0=2b/gcd(a,2), and let f_1 be a nonzero finite real S1 profile with largest frequency L. Use the canonical stationary polynomial-log recursion. Its stream coefficients G_n(t,theta) have log degree at most n/q_0 and angular frequencies at most(L+1)n. Define

    N_n=sum_(q,m)|[t^q sin(m theta)]G_n|,
    T_n(t,theta)=exp((2-n delta)t)G_n(t,theta).

If the individual terms T_n are pointwise bounded on a Lebesgue-measurable subset E of the(t,theta) plane of positive two-dimensional measure, then N_n has a geometric bound. Consequently, by topic93, the density, stream and common-potential series define an exact real-analytic exterior stationary solution at all sufficiently large radii, with every fixed weighted derivative converging absolutely and uniformly.

It is enough that the stream series converges pointwise on a set of positive measure, since convergence implies bounded individual terms. The set E need not contain an open set, a rectangle or a product of two sets.

Equivalently, if N_n has no geometric bound, then the set where the individual stream terms are bounded has two-dimensional Lebesgue measure zero. Topic93 also proves that this set is meagre on every open rectangle. Thus in this case the individual terms are unbounded almost everywhere and on a dense residual set, and the stream series cannot converge at those points. This is a conditional alternative, not a claim that the latter case occurs for a tested profile.

The recovery argument below uses only the two linear degree bounds and the radial factor. The stationary recursion is used only for the implication from geometric stream coefficients to a solution.

## A separated-node lemma for measurable subsets of an interval

Let S be a measurable subset of a finite real interval, of length mu>0. For every integer d>=1 there exist d+1 points x_0<...<x_d in S with

    x_k-x_j >= (k-j)mu/(4d), 0<=j<k<=d.             (1)

To prove this, put F(x)=measure(S intersect(-infinity,x]). This function is continuous, nondecreasing and1-Lipschitz, with values from0 to mu. For each j choose x_j in S for which F(x_j) differs by less than mu/[4(d+1)] from (j+1/2)mu/(d+1). Such points exist: the inverse image between two interior levels of F contains a subset of S with measure equal to the level difference. The chosen level intervals are disjoint and ordered. For k>j,

    F(x_k)-F(x_j) > (k-j-1/2)mu/(d+1)
                         >=(k-j)mu/[2(d+1)]
                         >=(k-j)mu/(4d).

The Lipschitz property then gives(1). Changes to S on a null set do not affect this construction.

## Recovering a polynomial from a measurable set

Let p(t) have degree at most d and |p(t)|<=V on a measurable set S contained in[T_0,T_1] of length mu>0. Put B=max(|T_0|,|T_1|). For d>=1,

    sum_q |[t^q]p| <= V [8e(1+B)/mu]^d.             (2)

Use the nodes in(1). The coefficient l1 norm of the numerator of each Lagrange polynomial is at most(1+B)^d. Its denominator has modulus at least

    [mu/(4d)]^d j!(d-j)!.

Summing the interpolation formula and using sum_j1/[j!(d-j)!]=2^d/d! gives

    ||p||_coeff <= V [8d(1+B)/mu]^d/d!
                   <=V[8e(1+B)/mu]^d.

The inequality d!>=(d/e)^d follows by comparison of sum_k log k with the integral of log x. For d=0 the bound is |p|<=V. The bracket in(2) exceeds1, because mu<=T_1-T_0<=2B.

## Recovering a trigonometric polynomial from a measurable angular set

Let h(theta) have frequencies between-M and M, and suppose |h|<=V on a measurable subset S of one full angular period with length eta>0. Then

    sum_(m=-M)^M |hhat(m)| <= V (16pi e/eta)^(2M).  (3)

For M=0 this is immediate. Split the period into two intervals of length pi; one contains a subset S_0 of S of length mu>=eta/2. Put d=2M and apply(1) to S_0. Write z_j=exp(i x_j). Since every angular difference is at most pi,

    |z_k-z_j|=2sin((x_k-x_j)/2)
                 >=2(x_k-x_j)/pi
                 >=(k-j)mu/(2pi d).

The polynomial P(z)=z^M h(theta), z=exp(i theta), has degree at most d. Its Lagrange numerators have coefficient norm at most2^d because |z_j|=1. Its denominators have modulus at least[mu/(2pi d)]^d j!(d-j)!. Consequently

    ||P||_coeff <= V (8pi d/mu)^d/d!
                   <=V(8pi e/mu)^d
                   <=V(16pi e/eta)^d.

Multiplication by z^M preserves the Laurent coefficient norm, proving(3). No interior interval is required in S.

## Applying the measurable-set bounds to stream coefficients

It suffices to work in a bounded rectangle Q=[T_0,T_1] times one angular period on which E has positive measure. Such a rectangle exists by a countable cover of the plane; the terms are periodic in theta. Write h=T_1-T_0>0. The measurable sets

    E_j={ (t,theta) in E intersect Q : |T_n(t,theta)|<=j for every n }

increase to E intersect Q. Some E_j has measure A>0. For its angular slices let ell(t) be the slice measure and put

    eta=A/(2h), S_t={t in[T_0,T_1] : ell(t)>=eta}.

Fubini's theorem gives integral ell(t)dt=A. The complement of S_t contributes at most eta h=A/2, while ell(t)<=2pi. Hence

    measure(S_t)>=A/(4pi)=:mu>0.                   (4)

For every t in S_t where the slice is defined, the stream polynomial is bounded on an angular set of measure at least eta by

    |G_n(t,theta)| <= C exp(n delta T_1),
    C=j exp(2 max(|T_0|,|T_1|)).

Apply(3), using M<=(L+1)n. Each sine amplitude B_(n,m)(t) is therefore bounded on the measurable set S_t by

    C exp(n delta T_1)(16pi e/eta)^(2(L+1)n).

Here the angular Fourier coefficient norm of a sine polynomial equals the sum of absolute sine amplitudes. The log degree of every B_(n,m) is at most n/q_0. Apply(2), with the measure lower bound mu from(4), to each amplitude. There are at most(L+1)n such amplitudes. Therefore

    N_n <= C(L+1)n B_*^n,
    B_*=exp(delta T_1)(16pi e/eta)^(2(L+1))
                         [8e(1+max(|T_0|,|T_1|))/mu]^(1/q_0). (5)

For any B>B_*, the sequence n(B_*/B)^n is bounded. Thus(5) is geometric. Topic93 now proves the stated exterior conclusion.

If pointwise boundedness holds only outside a null subset of E, discard that subset; the argument is unchanged. If the boundedness set had positive measure while N_n were not geometric, the preceding proof would be a contradiction. Since the boundedness set is the countable union over j of countable intersections of closed sublevel sets, it is measurable. This proves the almost-everywhere alternative. The meagreness assertion is the independently stated category argument in topic93.

## Dependencies and effectiveness

The degree and frequency bounds come from topics17 and88; the stream-to-density estimate and common-potential reconstruction are in topic93 and its dependencies. The two interpolation bounds and the separated-node lemma are proved in full here. Standard one-dimensional measure continuity and Fubini are the only measure-theoretic tools.

If the rectangle, the uniform bound j and the area A are supplied quantitatively, formula(5) gives an explicit base, and topic93 supplies an explicit sufficient exterior radius. Mere pointwise boundedness on an unspecified positive-measure set supplies existence only. The proof neither estimates A for the actual sequence nor establishes its all-order boundedness.

## Corollaries for the potential and radial velocity

The same implication holds if bounded stream terms on E are replaced by either of the following assumptions:

1. The individual radial-velocity terms are pointwise bounded on E.
2. The individual terms of a common polynomial-log potential, with the linear degree and frequency bounds of topic41, are pointwise bounded on E.

In particular, pointwise convergence of either series on a positive-measure set implies the full exterior conclusion. If N_n has no geometric bound, both of these series have unbounded individual terms almost everywhere. These statements concern the canonical stream and a common potential with the stated support bounds.

To prove the first assertion, the order-n radial velocity is

    u_(r,n)=-r^(1-n delta) partial_theta G_n(t,theta).

The interpolation argument just proved applies without change when the constant radial exponent2 is replaced by1, and applies to cosine as well as sine coefficients. It therefore bounds geometrically the plain coefficient norm of partial_theta G_n. Every nonzero stream frequency is an even integer m>=2, so this norm is sum_(q,m) m|[t^q sin(m theta)]G_n|>=2N_n. Thus N_n is geometric and topic93 applies.

For the second assertion, write the potential term as r^(4-n delta)C_n(t,theta). At all sufficiently large orders its two degrees are bounded linearly in n by topic41. Finitely many early exceptions do not affect a geometric coefficient bound. The same measurable-set proof, with constant radial exponent4, therefore bounds the plain coefficient norm of C_n geometrically. Applying the two Cartesian derivatives in psi=partial_x partial_y chi costs at most a fixed polynomial in n: the radial exponent is O(n), the log derivative has norm bounded by the log degree O(n), angular differentiation costs the O(n) frequency cutoff, and multiplication by sin theta or cos theta has angular Wiener norm one. It follows that N_n<=C n^2||C_n||_* for all sufficiently large n. A polynomial factor can be absorbed into a slightly larger geometric base, proving the second assertion. Taking contrapositives gives the almost-everywhere statements. The category argument of topic93 also yields a dense residual set of unbounded terms for each of these two fields when N_n is not geometric.
