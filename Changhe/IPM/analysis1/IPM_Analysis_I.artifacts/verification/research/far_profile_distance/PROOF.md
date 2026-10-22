# Leading-tail separation of X3 from a finite angular modal trial

Status: independent informal proof before the new numerical certificate.
The result concerns the distance between two explicit trial functions. It
is neither a stationary-profile exclusion nor an inverse obstruction in
every possible weighted space.

## 1. Exact objects and claims

Let X3 denote the exact coefficient interpretation of data_exact/x3.json,
whose original archive is identified there. Its parameters are L>0,
0<k<1/2 and p=6+2k/(2-k), hence 6<p<7. The endpoint spline coefficients
are beta_m=b_m(1), 0<=m<=200, and D=T(1) is the sum of its six exact
Chebyshev coefficients. All input floating numbers mean exact dyadics.
The stored k and L agree exactly with data_exact/modal_v2.json.

Let rho0 be the exact normalized modal trial defined in topic modal_repair,
with its exact real normalization parameter z, not a rounded replacement.
It has 260 cosine modes a_m(t), t=log r. Write tplus for the last exact
logarithmic knot, and A_m for the leading outer coefficient, with z added
to A_0 only. Put

 B(theta)=sum_(m=0)^200 beta_m cos(2m theta),
 C(theta)=sum_(m=0)^259 A_m cos(2m theta),
 ThetaX(theta)=L^(3-k) cos(theta)^2 sin(theta)
   exp(B(theta)+D |cos(theta)|^(p-2) sin(theta)^2),
 ThetaM(theta)=exp((3-k)tplus) cos(theta)^2 sin(theta) C(theta).       (1)

Then the explicit formulas give uniformly for theta in the entire circle

 r^(-k) X3(r,theta) -> ThetaX(theta),
 r^(-k) rho0(r,theta) -> ThetaM(theta).                             (2)

The finite exact check D=78259092636642149/9007199254740992>0 and
6<p<7 implies ThetaX is not C7 at theta=pi/2. ThetaM is real analytic
as a trigonometric polynomial. Hence ThetaX and ThetaM differ on some
open angular interval. It follows that

 X3-rho0 notin L2(R2,<r>^(-2gamma)dX) for every gamma<=1+k.          (3)

In particular X3-rho0 is not in whole-plane Hs for any s>=0. No finite
Hs ball centered at rho0 contains X3. The same analytic argument works
for any finite angular leading polynomial at this exponent, whatever its
finite coefficients, and for any positive replacement of L in X3.
A separate two-engine check of (1) at an interior rational multiple of
pi will give a quantitative witness for the actual modal trial. The
analytic conclusion (3) does not depend on finding that numerical witness.

## 2. Derivation and uniformity of the leading tails

For X3, let u=r/L, q=1-(1+u^2)^(-(1-k)/2),
s=u^2/(1+u^2), chi=u^2/(u^2+r0^2). These tend to 1 as r tends to infinity,
and 1-q=O(r^(k-1)), 1-s=O(r^-2), 1-chi=O(r^-2). Each spline is a
polynomial on its last span and is continuous with endpoint value beta_m.
There are only 201 splines. The Chebyshev polynomial tends to D, every
angular factor is bounded, and all finite powers of chi are uniformly
bounded. Thus the part of H after subtracting (k-3)log r converges
uniformly to (3-k)log L+B+D|cos theta|^(p-2)sin(theta)^2. It stays in
a bounded real interval after that subtraction, so exponentiation
preserves uniform convergence. Multiplication by cos(theta)^2 sin(theta)
gives the first part of (2), including the axes.

For rho0, the outer terms are exp(alpha_q(t-tplus)), where
alpha_q=(k-3)-j_q(1-k)-2 l_q. The first pair is (0,0), and every other
pair has j_q,l_q nonnegative and not both zero. Therefore alpha_q<k-3
for q>0. The join correction is exp(-bo(t-tplus)) times a polynomial
of degree at most six. The exact data obey bo>3-k, so the correction
also vanishes after division by r^(k-3). There are finitely many terms
and angular modes. The remaining leading factor is
exp(-(k-3)tplus) sum A_m cos(2m theta), proving (1) and the second
uniform limit. The exact z affects only finite coefficients, not these
exponent comparisons or angular regularity.

## 3. Why the leading angular functions cannot agree

Use x=cos(theta) near theta=pi/2, where sin(theta)=sqrt(1-x^2)>0.
Every cos(2m theta)=T_(2m)(x) is an even polynomial in x, as follows
inductively from T_(n+1)=2x T_n-T_(n-1), T_0=1,T_1=x. Consequently

 F(x)=L^(3-k) sqrt(1-x^2) exp(sum beta_m T_(2m)(x))

is positive and real analytic near zero, with F(0)>0, and

 ThetaX(arccos x)=x^2 F(x) exp(D |x|^(p-2)(1-x^2)).                 (4)

Expansion of the scalar exponential at zero gives

 ThetaX(arccos x)-x^2 F(x)
   =D F(0)|x|^p+o(|x|^p).                                       (5)

Indeed, the linear exponential term is D F(x)(1-x^2)|x|^p;
the quadratic error after multiplication by x^2 is O(|x|^(2p-2)),
which is o(|x|^p) since p>2. The leading coefficient in (5) is nonzero.

If the left side of (5) were C7 at zero, its degree-seven Taylor formula
with Peano remainder would apply. Since it is o(|x|^6), all coefficients
through degree six would vanish. Its quotient by |x|^p would then tend
to zero because 7>p. This contradicts (5). Thus ThetaX is not C7 in
this coordinate, and the smooth local coordinate change implies the
same on the circle. ThetaM is analytic, so the functions cannot agree.
The argument also shows they cannot agree throughout the open quadrant:
if they did, their identical one-sided values near the endpoint would
contradict the same one-sided Taylor expansion of the analytic ThetaM.

## 4. Weighted nonintegrability

The continuous difference Delta=ThetaX-ThetaM is not identically zero.
Choose a closed interval J of positive length in the open quadrant and
c>0 with |Delta|>=2c there. Uniform convergence in (2) gives R>=1
such that |X3-rho0|(r,theta)>=c r^k for r>=R, theta in J.
For any real gamma there is c_gamma>0 with
(1+r^2)^(-gamma)>=c_gamma r^(-2gamma) when r>=1. The weighted square
integral is therefore bounded below by a positive constant times

 integral_R^infinity r^(2k+1-2gamma) dr.

This diverges for gamma<=k+1, including logarithmic divergence at equality.
Taking gamma=0 proves failure of L2. The unitary Fourier definition of
Hs with s>=0 includes L2, so the Hs conclusion follows.

This concerns a difference of two functions growing like r^k and does
not claim either has an unweighted Hs norm. It does not prevent weighted
factor convergence, high accuracy on finite domains, or an exact solution
in a finite Hs ball about rho0 with its prescribed tail. In particular it
does not decide any numerical uncertainty ball in another topology.

## 5. Quantitative witness protocol

The arithmetic inputs will be copied as exact JSON with source archive
hashes and a complete extraction audit. At theta=pi/4 use the exact cycles
cos(m pi/2)=(1,0,-1,0) and cos^2(theta)sin(theta)=2^(-3/2). Then

 ThetaX= L^(3-k) 2^(-3/2)
          exp(sum beta_m cos(m pi/2)+D 2^(-p/2)),
 ThetaM= exp((3-k)tplus) 2^(-3/2)
          [sum Aout_(m,0) cos(m pi/2)+z].                         (6)

One engine will use Arb and exact rational cyclic sums. The other will
use mpmath.iv, a complex-root recurrence for the angular values and an
independent evaluation grouping. Both enclose the same exact z from its
audited definition; separate published z enclosures may be used. Each
method must separately prove every printed bound. An independent output
checker will verify all exact saved endpoints and source hashes. A failed
interior witness is an open numerical item, not a failure of the analytic
nonmembership proof or permission to invent a nonzero bound. Actual Opus5.5
will review the proof and executable bundle, and advice will be checked.
