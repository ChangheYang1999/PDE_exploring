# A rational interval enclosure of the entire far section

Written 2026-10-21 before implementation. Status OPEN pending independent review and manufactured tests. No numerical source application is asserted here.

Let s and alpha be positive rationals, a be rational, and P(t,w) be a polynomial with rational coefficients. The beta=3 generating family and its far coefficients are those of research/analytic_far_residual/PROOF.md (result68). Its finite core patches do not contribute to these coefficients. Write X=x^2, H=e^2,

    F=X+H^3/s^6, w0=(H/s^2) F^(-1/3),
    c1=(1-exp(-alpha))/alpha,
    Pj(w)=partial_t^j P(0,w), j=0,1,2.

All coefficient functions below are smooth for F>0. On the first-quadrant section set X=1-w^3, H=s^2 w, 0<=w<=1, so F=1 exactly. Assume the limiting chart A=G0_xe is positive along the section. A separate global positive-chart theorem is needed to interpret these coefficients as the far limit of a particular globally defined physical candidate.

The goal is to enclose the whole continuous function

    q(w)=|C_d(w)|/sum_{j=1}^4 |Z_{j,d}(w)|,

where C=sum_j Zj and the signed terms Zj are from result68. The subscript d here denotes division by the mixed parity factor xe. This differs from division by physical xY by the common factor Y/e; the quotient q is the same. At either endpoint, the divisions mean smooth extensions. The quotient is undefined when its extended denominator is zero; no floor is allowed.

Define normalized generating functions

    g0=xe F^(1/3) P0(w0),
    g1=xe F^(1/6) P1(w0),
    g2=xe [alpha P1(w0)+P2(w0)]/2.

Then the G0,G1,G2 of result68 equal g0,c1*g1,c1^2*g2, since c2=alpha*c1^2/2. Set A=g0_xe, b=g0_xx/A, Dx=partial_x-b partial_e and Dy=A^(-1)partial_e. Set s0=-g1, s1=-2g2+g1_x*g1_e/A, v1=-Dy s0, v2=Dx s0 and oj=-(Dx^2+Dy^2)sj. By linearity and the powers of c1,

    Z1=c1^2*(-o1), Z2=c1^2*v1*Dx o0,
    Z3=c1^2*v2*Dy o0, Z4=a*b.                 (1)

This identity retains the dependence on alpha exactly; it is not specialized to alpha=3.

A parity representation avoids square roots and singular divisions in evaluating (1). Represent a smooth parity function as x^epsilon e^delta V(X,H), where epsilon,delta are each0 or1. Products multiply V and include an additional factor X when both x parities are1, and H when both e parities are1. Parities add modulo2. Partial differentiation has the exact rules

    partial_x[x^epsilon e^delta V]
      =x^(1-epsilon)e^delta [epsilon V+2X^epsilon partial_X V],
    partial_e[x^epsilon e^delta V]
      =x^epsilon e^(1-delta) [delta V+2H^delta partial_H V]. (2)

These follow from the product and chain rules, including the cases epsilon=0 and delta=0. Reciprocal is used only for the even-even A and requires A to stay nonzero. Addition is applied to functions with equal parities. It follows inductively from (2) that A has parity(0,0), b has(1,1), s0 and s1 have(1,1), v1 has(1,0), v2 has(0,1), oj has(1,1), and every Zj has(1,1). Therefore each divided Zj is simply the coefficient function Vj(X,H), evaluated at the section. There is no division by x or e, even at the endpoints.

For x,e>0, result68 divides the same terms by xY. Since Y/e>0 wherever the relevant first-quadrant limiting chart is positive and increasing from its zero-axis value, division by xY multiplies every Vj by e/Y>0. The ratio is unchanged. At the horizontal endpoint e=0,x=1, Y/e=A(1,0)>0; at the vertical endpoint x=0,e=s, Y/e=P0(1), and A(0,s)=3P0(1), so positivity follows from the section hypothesis. Positivity of A on the entire section also gives positivity on every nonzero mixed point by homogeneity. Integrating in e proves Y/e>0 in the interior. Continuity then gives the same desingularized endpoint ratios. Purely algebraically q remains the mixed-section quotient wherever its own denominator is positive, even if the global physical interpretation is unproved.

Here is a finite rational procedure for enclosing the Vj over a closed rational interval I=[l,h] contained in[0,1]. Store Taylor coefficients in two formal increments dX,dH, through a specified total degree. Coefficients are rational intervals. These are coefficients of derivatives at a varying basepoint on the section, not a Taylor approximation over a finite spatial neighborhood. Assign constant X to [1-h^3,1-l^3] and constant H to [s^2*l,s^2*h], with their linear formal terms exact. Compute the jet F=X+H^3/s^6, replacing its constant coefficient by exactly1. This replacement uses the section identity and is valid simultaneously for every basepoint; its higher derivatives are unchanged. Fractional powers F^r for rational r are computed by the finite binomial series in F-1, whose formal constant is exactly zero. Every retained coefficient is exact finite algebra, since terms of higher total degree cannot contribute.

The jet of w0=(H/s^2)F^(-1/3) has constant w in I. Replace that constant by I, and form its zero-constant increment J by setting the constant coefficient to zero. For each polynomial Pj use

    Pj(w+J)=sum_{k=0}^n [Pj^(k)(w)/k!] J^k

through the retained degree n. This formula is an identity of jets at the varying section basepoint. In particular the interval subtraction I-I must not be used to construct a purported zero-constant increment. Derivative intervals for Pj on I may be obtained from any exact Bernstein representation on I: a polynomial lies between the least and greatest of its Bernstein coefficients, because the Bernstein basis is nonnegative and sums to1. Derivatives follow from exact finite differences of those coefficients. The root Bernstein coefficients and all subdivisions must be related to the original rational Chebyshev coefficients by checked exact polynomial identities. An imported array without that check is not a certificate.

Products, additions, differentiation and reciprocals of nonzero jets are computed in the truncated polynomial algebra. A reciprocal with constant v0 is the finite geometric series v0^(-1) sum_k[-(v-v0)/v0]^k, where v-v0 has exactly zero formal constant. Interval arithmetic encloses the true coefficient at every basepoint. Its enclosure may be wide because correlations are discarded, but cannot be too narrow if every arithmetic operation rounds outward or uses exact rationals. Differentiation reduces the retained order; an implementation must reject insufficient order. Starting coefficient jets for g0,g1,g2 through orders5,4,3 suffices for (1) and one further mixed derivative, as can be checked by counting the occurrences of (2). Only the zeroth coefficients of the final parity-divided terms are needed for q. No assertion is made about a finite-neighborhood Taylor remainder.

The exponential is the only nonrational parameter in (1). Choose an integer N with N+2>alpha and let

    L=sum_{k=0}^N alpha^k/k!,
    U=L+[alpha^(N+1)/(N+1)!]/[1-alpha/(N+2)].

Then L<=exp(alpha)<=U. Indeed the remaining positive series terms have successive ratios at most alpha/(N+2), so a geometric series bounds their sum. Since L>0, interval inversion bounds c1 and its square. The same enclosure is used consistently in all terms; discarding that correlation only enlarges the answer.

For each interval I let Bj enclose Vj from(1), let BC=sum_j Bj, and let BN=sum_j abs(Bj), with the exact interval extension of absolute value. If A has a positive lower bound on I and BN has a positive lower bound, then q(I) is enclosed by abs(BC)/BN, intersected with[0,1]. The intersection is justified by the triangle inequality for the exact four terms. If either positive lower bound fails, subdivide or leave the interval OPEN. No small denominator may be replaced by a floor. A finite binary subdivision tree whose leaves partition[0,1] proves the resulting enclosure over the entire section. Taking the largest leaf upper endpoint gives a global upper bound. An exactly enclosed evaluation at any single rational point with positive denominator gives a lower bound for the supremum. For a positive continuous denominator, q is continuous on the compact section and attains its supremum.

The preceding algorithm is sound by induction on the exact jet operations and on the finite subdivision tree. Replaying the root polynomial identities, leaf coverage, rational arithmetic and positivity tests suffices to check a produced certificate. A separate implementation of these checks improves error detection but does not turn numerical coefficient files into a proof without the stated identities. Finite sampled MP values are useful comparisons; they are not a substitute for the interval enclosure or for global chart admissibility.

Dependencies: result68 for the far coefficients and physical interpretation; elementary parity calculus, Taylor coefficient algebra and the Bernstein convex-hull property proved above. No PDE existence, whole-plane residual bound, far convergence rate at a fixed radius, or broad nonexistence conclusion is claimed.

Supplement written before the symbolic implementation. The same jet calculation may be performed with exact rational functions of the section parameter w instead of intervals. Initially every jet coefficient is a polynomial in w with rational coefficients: X=1-w^3, H=s^2w and the constant F=1 make every retained binomial coefficient rational, and composition with the polynomial Pj uses its exact derivatives at w. Let A0(w) be the resulting zeroth coefficient of g0_xe. All subsequent divisions are reciprocals of the jet A, whose constant is A0. The finite geometric-series formula shows inductively that every retained coefficient belongs to Q[w,A0^(-1)]. Thus every final parity-divided normalized term in (1), before multiplication by c1^2 or a, can be written Nj(w)/A0(w)^kj with an integer kj>=0. Exact cancellation of a common A0 factor is optional and does not change the represented function away from zeros of A0.

Choose K=max kj and multiply the numerators by A0^(K-kj). The common denominator cancels from the absolute-value quotient, so its numerator is the absolute value of c1^2(N1+N2+N3)+a*N4, and its denominator is c1^2(|N1|+|N2|+|N3|)+|a*N4|. Combining N1+N2+N3 as an exact polynomial before interval evaluation retains cancellations lost by the direct interval jets. The chart condition A0>0 is checked separately. Exact polynomial conversion to a Bernstein basis and a closed subdivision cover therefore provide a second sound certificate method, with the same source and denominator obligations as above. This algebra does not assert that a practically small cover exists. The common denominator power, exact numerator arrays, source binding and jet algorithm must all be recorded and checked; a table of unverified rational functions is not itself evidence for the defining derivative identities.

Implementation supplement, written before the Bernstein producer. For a power polynomial p(w)=sum_j p_j w^j of degree n, its Bernstein coefficients on [0,1] are b_k=sum_{j<=k} p_j binom(k,j)/binom(n,j). The inverse identity is p_k=binom(n,k)sum_{j<=k}(-1)^(k-j)binom(k,j)b_j. These follow by expanding w^j=sum_{k=j}^n binom(k,j)/binom(n,j) B_{k,n}(w), or by the binomial theorem. Both identities can be checked using exact rational arithmetic.

For a sequence b_0,...,b_n, the transform T_j=sum_{k<=j}binom(j,k)b_k is the coefficient of z^j in (sum_k b_k z^k/k!)(sum_l z^l/l!), multiplied by j!. Thus exact polynomial multiplication gives a fast way to compute this transform. The Bernstein sequences on [0,1/2] and [1/2,1] are respectively T_j/2^j and T^rev_(n-j)/2^(n-j), where T^rev is the same transform of the reversed sequence. These are the de Casteljau midpoint identities; they follow by repeated averaging. Rational or common-denominator integer implementations compute exactly the same subdivision. Degree-zero polynomials are included.

A rational interval [l,u] containing c1^2 may be enlarged by rounding its endpoints outward to a dyadic grid. Put k=(l+u)/2 and eps=(u-l)/2, and form the exact polynomial P_C=k*(N1+N2+N3)+a*N4. If a leaf bounds P_C in I_C and N123 in I_123, the true numerator before absolute value lies in I_C+[-eps,eps]*I_123. Its denominator is bounded below by l times the sum of the lower bounds for |Nj|, j=1,2,3, plus |a| times the lower bound for |N4|. These follow directly from the common-denominator formula. A positive denominator bound and positive Bernstein lower bound for A0 complete the leaf check. The true ratio is always at most one, but a bound smaller than one must come from these computed inequalities; no tiny positive floor or midpoint denominator is permitted.
