# Composed radial cutoff: conditional calculus and finite aggregation

Written2026-10-21before the checking programs. This note audits the newer
localized forcing construction. It is not a proof that its inherited
modal models enclose the physical residual.

## Statement and dependencies

Let delta=33/2000, r_in=7delta/4, r_out=9delta/4, P=(p,0), and
S(z)=1-126z^5+420z^6-540z^7+315z^8-70z^9.
Set tau=1 for |X-P|<=r_in, tau=0 for |X-P|>=r_out, and
tau=S((|X-P|-r_in)/(delta/2)) on the intervening annulus.
Let g be a C4 function on a neighborhood of the support, with g odd in y.
For f=tau g, define
 N_lambda,s(f)^2 = integral (lambda^2+|xi|^2)^s |f_hat(xi)|^2 dxi,
using the unitary Fourier transform and s=31/10.

Suppose a collection of restricted polar subcells covers the upper-half
support. On subcell c suppose saved nonnegative bounds A_c,B_c,C_c,D_c,E_c
bound respectively |f|, |grad f|, |Lap f|, |grad Lap f|, |Lap^2 f|.
Suppose a_c is an upper bound for its area together with its reflection.
Then, with sums over these subcells,
 J3(lambda)=sum_c a_c [lambda^2(lambda^2 A_c+C_c)^2
                              +(lambda^2 B_c+D_c)^2],
 J4(lambda)=sum_c a_c [lambda^4 A_c+2lambda^2 C_c+E_c]^2,
                 N_lambda,31/10(f) <= J3^(9/20) J4^(1/20).       (1)
The finite postprocessing below checks these sums for the saved v2.1 data,
without accepting their A,B,C,D,E as bounds on the physical function.

The conditional construction of tau's Taylor models on a block is valid
under the following hypotheses: its bivariate polynomial arithmetic and
remainders are sound on the restricted parent domain; q=|X-P|^2 has such
a model; a real c0>0 and x<1 satisfy |q-c0|<=c0 x; all coefficient and
scalar tail bounds used are outward. Every derivative of tau is built
from a separately justified pointwise composition formula below. No
uncontrolled derivative of a Taylor-model remainder is taken.

## Centering and the inverse-square-root series

For a polynomial H(s,t)=sum c_ij s^i t^j, the coefficient of s'^a t'^b in
H(s'+a_s,t'+a_t) is
 sum_{i>=a,j>=b} binom(i,a)binom(j,b)c_ij a_s^(i-a)a_t^(j-b).     (2)
This follows by expanding both binomials. Interval coefficients and shifts
enclosing their exact values therefore enclose the shifted coefficients
under sound interval operations. An old remainder stays valid at points
whose shifted coordinates lie in the original domain. A larger block
may be used to bound the resulting polynomial, but does not extend the
physical model hypothesis beyond this restricted intersection.

Write u=x-p, v=y, q=u^2+v^2, z=(q-c0)/c0. Since |z|<=x<1, q>0.
The real analytic function (1+z)^(-1/2) has the convergent binomial series
 sum_{k>=0} b_k z^k, b_k=(-1)^k binom(2k,k)/4^k.
The coefficient formula follows by differentiating at zero. The ratio
|b_(k+1)|/|b_k|=(2k+1)/(2k+2)<1, and b_0=1, so |b_k|<=1.
The absolute tail after degree K is at most x^(K+1)/(1-x).
Consequently the polynomial in q-c0 through degree K plus the scalar
remainder c0^(-1/2)x^(K+1)/(1-x) encloses W=q^(-1/2). Sound model
products then enclose sqrt(q)=qW. This proof does not assert that a
floating evaluation of the displayed remainder is outward; each actual
scalar evaluation must be checked or bounded independently.

## Derivatives without differentiating a remainder

Let zeta(q)=(sqrt(q)-r_in)/(delta/2)=2sqrt(q)/delta-7/2.
Its first four derivatives are
 zeta'=W/delta, zeta''=-W^3/(2delta),
 zeta'''=3W^5/(4delta), zeta''''=-15W^7/(8delta).
They follow by four ordinary differentiations of q^(1/2).
For F(q)=S(zeta(q)), put s_j=zeta^(j)(q). The chain and product rules give
 F'=S' s1,
 F''=S'' s1^2+S' s2,
 F'''=S''' s1^3+3S'' s1 s2+S' s3,
 F''''=S'''' s1^4+6S''' s1^2 s2+3S'' s2^2+4S'' s1 s3+S' s4.     (3)
For example, differentiating the third line yields coefficients1,6,3,4,1
in the fourth line. Each expression involves values of W and S derivatives,
so its enclosure follows by pointwise model algebra, without differentiating
an error term. A model of F^(k) need be correct only where the true distance
is in the transition annulus; polynomial continuation of S elsewhere does
not represent the cutoff there.

There is an independent closed formula for every Cartesian derivative:
 d_u^a d_v^b F(u^2+v^2)
 = a! b! sum_{j=0}^{floor(a/2)} sum_{l=0}^{floor(b/2)}
   (2u)^(a-2j)(2v)^(b-2l)
   F^(a+b-j-l)(q) / [(a-2j)!(b-2l)!j!l!].                    (4)
To prove it, substitute q(u+h,v+k)=q+2uh+h^2+2vk+k^2 into the Taylor
expansion of F and compare the coefficient of h^a k^b. Selecting j copies
of h^2 and l copies of k^2 leaves a-2j copies of 2uh and b-2l copies of 2vk;
the multinomial factor cancels the factorial of the F derivative. Multiply
by a!b!. Only orders<=a+b enter, so a Taylor expansion through a+b with its
small-o remainder suffices. This also proves the recursive polynomial rule
 d_u[F^(k)P]=F^(k+1)2uP+F^(k)P_u, and similarly for v.

## Products, regimes, and Sobolev regularity

For f=tau g, the multiindex Leibniz rule is
 D^alpha f=sum_{beta<=alpha} binom(alpha,beta)
                          D^beta tau D^(alpha-beta)g.     (5)
Applying (5) to the operators needed in(1) gives
 Lap f=tau Lap g+2grad tau.grad g+g Lap tau,
 grad Lap f=grad tau Lap g+tau grad Lap g+2D2tau grad g
                         +2D2g grad tau+grad g Lap tau+g grad Lap tau,
 Lap^2 f=tau Lap^2 g+g Lap^2 tau+2Lap tau Lap g
             +4grad tau.grad Lap g+4grad g.grad Lap tau+4D2tau:D2g. (6)
All mixed derivatives have their ordinary binomial multiplicity. Formula(5)
also supplies an independent finite symbolic check of every term in(6).

If a whole restricted subcell has distance<=r_in, tau=1 there and the g
bounds suffice. If its whole distance interval lies in[r_in,r_out], the
composed model and(3)-(6) are valid. If it crosses an endpoint, the piecewise
cutoff needs the separately justified pointwise product bounds, rather than
the polynomial continuation of S. Cells strictly outside have zero forcing.
A failed series test merely forces the separate product-bound method.

S'(z)=-630z^4(1-z)^4. Thus S has derivatives1..4 vanishing at both endpoints,
S(0)=1 and S(1)=0. The piecewise tau is C4, constant near P, and compactly
supported. Multiplying by g gives f in C4 with compact support, hence H4;
there are no distributional surface terms at the cutoff interfaces. Under
the actual local modal hypotheses, the stronger C5 regularity of g was
checked in topic115. The present assertion only needs C4.

Plancherel gives exactly
 N_lambda,3(f)^2=lambda^2||(lambda^2-Lap)f||2^2
                           +||grad(lambda^2-Lap)f||2^2,
 N_lambda,4(f)^2=||(lambda^2-Lap)^2f||2^2.
Use triangle bounds on each cell to obtain J3,J4. Reflection is legitimate:
tau is even in y, f is odd, and absolute values, Euclidean vector norms and
squares of each derivative combination are reflection invariant. Overlap
in upper area bounds can only enlarge the sums. Finally Holder with powers
10/9 and10 gives (1), including zero norms by continuity.

## Finite evidence and limits

The planned independent checks are: exact integer comparison of all15
Cartesian composition tables with(4); a second symbolic chain-rule check
of(3) and all product expressions against(5); exact and Arb512 sums of every
saved row, with iv160 fractional powers; full row and part coverage, geometry
and regime checks; and actual scalar-tail verification if its operands are
available. All code and data used are frozen with hashes. Current source
and historical v2.1 data are not automatically the same version.

The physical radial models, every composed model coefficient/remainder,
actual scalar series tails and historical source execution remain OPEN
until separately checked. Even a complete forcing certificate would be
only one ingredient of an existence argument. No global inverse, closing
inequality, or decisive PDE endpoint is supplied by this result.
