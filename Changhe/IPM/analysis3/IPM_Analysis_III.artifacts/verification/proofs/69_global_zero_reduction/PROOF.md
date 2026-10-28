# Reduction of the global zero count to local and box checks

## Statement

Let V be a C1 vector field on the closed first quadrant, with V(0)=0,
V_1 odd in x and even in y and V_2 even in x and odd in y under
reflection. Let 0<A<D, and let P=(p,0), p>0, satisfy V(P)=0 and
DV(P)=diag(a_P,mu_P), with a_P>=mu_P>0.

Suppose the following cover is given.

1. On the closed origin disk of radius r0,
   ||DV-diag(-A,D)||_op<=delta0<A.
2. On a convex source neighborhood Q containing P,
   ||D^2V||_F<=M. Let R bound |X-P| on Q, and suppose
   mu_P-MR/2>0.
3. Finitely many closed polar boxes cover the rest of the closed
   quadrant, and on each box |V(X)|>=m_i|X| with m_i>0.
   A box extending to zero or infinity requires a genuine half-line
   bound, not a finite sample or an asymptotic limit alone.

Then the only zeros in the quadrant are 0 and P. On the origin disk,
|V(X)|>=(A-delta0)|X|. On Q,

 |V(X)|>=(mu_P-M|X-P|/2)|X-P|.

The Frobenius norm here is that of the full derivative tensor. A
componentwise maximum without its multiplicity factor cannot replace
it. A bound on the full tensor bounds its contraction operator norm.

For the V017/V024 values M<0.308 and R=99/2000, the last constant is
strictly greater than0.992. For the larger rectangle of V070 its
stronger symmetric-Jacobian conclusion already proves uniqueness.

## Proof

The axis parity gives partial_y V_1(x,0)=0 and V_2(x,0)=0; differentiating
the latter in x gives partial_x V_2(x,0)=0. Thus DV(P) is diagonal.
For the origin, write V(X)=int_0^1 DV(sX)X ds. The average matrix is
within delta0 of diag(-A,D), whose smallest singular value is A.
The reverse triangle inequality gives the origin bound.

Put Z=X-P. Convexity keeps P+sZ in Q. The derivative tensor bound gives
||DV(P+sZ)-DV(P)||_op<=Ms|Z|. Integrating once more yields

 |V(X)-DV(P)Z|<=int_0^1 Ms|Z|^2 ds=M|Z|^2/2.

The smallest singular value of DV(P) is mu_P, giving the claimed
bound and source uniqueness. Every remaining point has nonzero radius
and belongs to a box with a strictly positive lower bound. This proves
the global conclusion. Both eigenvalues at P are positive, so it is a
hyperbolic source. No dynamical classification beyond this follows
without additional arguments such as V063.

## Exact polar containment checks

For a fixed P=(p,0), a polar box with finite radial interval [r-,r+]
and angular interval [theta-,theta+] in [0,pi/2] is contained in the
closed disk of radius R centered at P if and only if both points
(r-,theta+) and (r+,theta+) have distance at most R from P. Indeed,
the squared distance r^2-2rp cos(theta)+p^2 is increasing in theta
and convex in r. For a certified bracket p in [p-,p+], test these
points against both endpoint values of p: the squared distance is
also convex in p. This is a sufficient uniform certificate.

For the source rectangle [x-,x+] times[-h,h], a first-quadrant polar
box is contained if

 r- cos(theta+)>=x-, r+ cos(theta-)<=x+,
 r+ sin(theta+)<=h.

These follow from monotonicity on the quadrant and are exact necessary
and sufficient conditions for this rectangular containment.

## Star-shaped matrix-box alternative and a missing sign condition

Convexity of Q can be weakened to being star-shaped with respect to P
if the following uniform derivative bounds hold throughout Q:

 partial_x V_1>=alpha1>0, partial_y V_2>=alpha2>0,
 |partial_y V_1|<=beta1, |partial_x V_2|<=beta2,
 alpha1 alpha2>beta1 beta2.

Every averaged Jacobian int_0^1 DV(P+sZ)ds lies in the same convex
matrix box. Its determinant is at least alpha1 alpha2-beta1 beta2>0,
so it is invertible and V(P+Z) cannot vanish for Z nonzero.

The positivity of both alpha values is essential to this proof and
was missing from the source draft. The displayed product inequality
alone is insufficient. On Q=[-1/2,3/2] times[-1,1], take
V(s,y)=(s(1-s),y), P=(0,0). Its Jacobian is diag(1-2s,1), so it satisfies
alpha1=-2, alpha2=-1, beta1=beta2=0 and alpha1 alpha2>beta1 beta2.
The point P is a hyperbolic source but (1,0) is a second zero in Q.
Translation places this example in a positive-x source neighborhood;
the local parity in y is already correct. Only the corrected positive
lower-bound version is a valid sufficient test.

## Scope

This confirms the main conditional Lemma Z in the theory author's section6.3,
including its factor1/2 source estimate and polar-disk test, and repairs
the star-shaped variant. Actual global(Z) still requires the complete
nonzero-field cover. V070 supplies a larger independently verified
source patch; it does not by itself validate arbitrary omitted boxes.
