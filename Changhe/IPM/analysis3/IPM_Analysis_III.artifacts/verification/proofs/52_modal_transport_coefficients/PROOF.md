# Transport-coefficient hypotheses for the exact modal field

## Statement and scope

Let rho be the normalized exact-join modal density verified in topics04 and50, with its exact real scalar repair. Let ell=1/k, c=3ell-1, A=2ell-1 and D=4ell-1. Define its canonical stream function by the modewise whole-plane Green formula below, U=(-psi_y,psi_x) and V=ell X+U. Set t=log r,

 d(t)=V2(0,r)/r,
 q(r,theta)=V(X).X/r^2,
 p(r,theta)=2V1(X)/x+V2(X)/y-1,
 b(t)=D-d(t)-2d'(t).

Axis values of the quotients mean their continuous extensions. Then V is a globally Lipschitz C1 field, div V=2ell, and V1/x and V2/y are globally bounded. The function d is continuously differentiable and satisfies, for finite constants Cminus,Cplus,

 |d-D|+|d'|<=Cminus r^2, 0<r<=1,
 |d-ell|+|d'|<=Cplus r^(k-1), r>=1.                 (1)

There are finite constants M_Q,M_P with

 |q-d|<=M_Q cos(theta)^2,
 |p-b|<=M_P min(r^2,1) cos(theta)^2.                (2)

No positivity of d is asserted. These statements verify every regularity and endpoint part of (A) and (CB), leaving only the global positive lower bound for d to be certified.

For a=17/4, eta=5/4 and the piecewise weight of proof 44, the energy coefficient

 kappa_w=1+ell+(mu'/2)q+a tan(theta)V.grad(theta)

has the uniform angular limits

 kappa_w -> kappa0=(19/2)ell-13/4 as r->0,
 kappa_w -> kappainf=1+(3/8)ell as r->infinity.       (3)

The multiplier bplus=(|grad rho|-rho_y)/2 tends uniformly to0 at both ends. Hence kappa_w-bplus is strictly positive outside some compact radial annulus. This does not give explicit cutoffs or a certified global margin on that annulus.

## Canonical finite-mode Green formula

The angular expansion of f=partial_x rho is a finite sum

 f(r,theta)=sum_(n=1)^N f_n(r) sin(2n theta).

The density and exact joins imply that these radial coefficients are C5 away from0. The origin and infinity bounds from proof 50 give, with any fixed number of angular derivatives and the needed radial derivatives,

 f_n(r)=delta_(n1) r^2+O(r^4), r->0,
 f_n(r)=O(r^(k-1)), r->infinity.                     (4)

The exact leading term follows from partial_x(x^2y)=2xy=r^2sin(2theta). For n>=1 define

 psi_n(r)=[r^(-2n) int_0^r s^(2n+1)f_n(s) ds
           +r^(2n) int_r^infinity s^(1-2n)f_n(s) ds]/(4n). (5)

Both integrals converge: the first integrand is O(s^(2n+3)) at0, and the second is O(s^(k-2n)) at infinity, with k<1<=2n-1. Direct differentiation of (5) gives

 -psi_n''-psi_n'/r+(2n)^2 psi_n/r^2=f_n.

Thus psi=sum psi_n sin(2n theta) solves -Delta psi=partial_x rho. Formula (5) specifies the canonical choice without adding growing harmonic fields. It also defines a finite-mode field when the original density itself is not absolutely integrable against an unpaired Riesz kernel at infinity.

The integral identities can be differentiated on every compact radial interval. Consequently V has the required annular C1 regularity and in fact several more derivatives. The finite angular sum preserves all reflection parities.

## Origin expansion and resonance count

For n=1, write f_1=r^2+O(r^4) near0 in (5). The first integral contributes r^4/24+O(r^6), and the second contributes a homogeneous quadratic term minus r^4/8+O(r^6). Their sum is

 psi_1(r)=(c/2)r^2-r^4/12+O(r^6).

Here c=(1/2)int_0^infinity f_1(s)ds/s is exactly the central strain already normalized in proof 04.

For n=2, the O(r^4) source in (4) gives a homogeneous r^4 term plus O(r^6). For n=3 it gives O(r^6(1+|log r|)), because the outer integrand is O(s^-1). For n>=4 it gives O(r^6) plus a homogeneous r^(2n) term, which is also O(r^6) on a sufficiently small disk. Summing the finite modes,

 psi(X)=cxy-r^4 sin(2theta)/12+H4 r^4 sin(4theta)
                         +O(r^6(1+|log r|)),             (6)

for a finite real H4. The same estimates hold after any fixed number of angular derivatives. For radial derivatives used here they follow either by differentiating (5), or by differentiating the finite inner exponential-polynomial expressions. The n=3 term is the only possible logarithm at degree6; higher-degree logarithmic resonances are absorbed in the displayed remainder.

Taking one Cartesian derivative gives

 U(X)=c(-x,y)+U3(X)+O(r^5(1+|log r|)),                  (7)

where U3 is a homogeneous cubic polynomial. Taking one further derivative shows DU approaches diag(-c,c), continuously. The parity allows division of the first component by x and the second by y. For example an odd smooth angular factor divided by cos(theta) is smooth at theta=pi/2. Since the angular sum is finite, the divided errors and their first two angular derivatives have order O(r^4(1+|log r|)). Therefore

 V1/x=-A+O(r^2), V2/y=D+O(r^2),                          (8)

with the corresponding angular bounds. On the vertical axis (7) also gives the first line of (1).

There is no claim that the velocity is analytic at0. The allowed r^5 log r remainder is sufficient for every stated conclusion.

## Infinity bounds

For r>=1, split the first integral in (5) at a fixed large radius beyond which (4) holds. The bounded inner part contributes O(r^-2n). The remaining integral is at most C r^(2n+k+1), since 2n+k>-1. The second integral is at most C r^(k-2n+1), since k-2n<-1. Hence

 psi_n=O(r^(k+1))+O(r^-2n),
 partial_r^j psi_n=O(r^(k+1-j))+O(r^(-2n-j)), j=1,2,3. (9)

The derivative estimates follow directly from (5) and the derivative versions of (4), with cancellation of the moving-endpoint terms in the first derivative. A finite angular sum then yields

 U=O(r^k), DU=O(r^(k-1)),
 U1/x=O(r^(k-1)), U2/y=O(r^(k-1)),                       (10)

uniformly in angle, including the first two angular derivatives of the divided components. The parity justifies division at either axis as at0. Differentiation along the vertical axis proves the second line of (1).

Together with (7) and annular regularity, (10) proves the global boundedness of DV and hence global Lipschitz continuity. The continuous extensions of V1/x and V2/y are bounded by the same endpoint estimates and compactness on the intervening annulus.

## The exact axis identities and lift bounds

Since V2(0,y)=y d(log y),

 partial_y V2(0,y)=d+d',
 partial_x V1(0,y)=2ell-d-d'

by incompressibility. Therefore

 p(r,pi/2)=2(2ell-d-d')+d-1=D-d-2d'=b.

Also q(r,pi/2)=d. Both q and p are even with respect to reflection across the vertical axis. Their first angular derivatives vanish there. Taylor's formula and |sin u|>=2|u|/pi for |u|<=pi/2 give

 |F(theta)-F(pi/2)|<= (pi^2/8) sup|F''| cos(theta)^2    (11)

on a half-quadrant; parity covers the plane. At0 the leading linear field is V=(-Ax,Dy), so

 q=-A cos^2(theta)+D sin^2(theta)+O(r^2),
 p=-2A+D-1+O(r^2)=O(r^2).

The same O(r^2) estimate holds for the second angular derivative of p. Thus (11) gives the first bound of (2) with a bounded coefficient and the second with an O(r^2) coefficient. At infinity (10) gives q=ell+O(r^(k-1)) and p=3ell-1+O(r^(k-1)); their angular derivatives have the same decaying order. Compactness handles the middle annulus. This proves (2) with finite global constants.

In fact (q-d)/cos^2(theta) tends uniformly to-(A+D)=-2c at0. Its nonzero limit is why the lower off-diagonal transport block is bounded but need not be compact.

## Energy coefficient at the two ends

The parity identities also give

 tan(theta)V.grad(theta)=sin(theta)^2(V2/y-V1/x),        (12)

with continuous axis values. At0, substitute q=-A cos^2(theta)+D sin^2(theta) and the leading value (A+D)sin^2(theta) into kappa_w, where mu'=-2a. The angle-dependent terms cancel exactly:

 kappa0=1+ell+aA=(19/2)ell-13/4.

The error is O(r^2) uniformly in angle, by (8). At infinity mu'=-eta; (10) and (12) give q=ell+O(r^(k-1)) and tan(theta)V.grad(theta)=O(r^(k-1)), so

 kappainf=1+ell-eta ell/2=1+(3/8)ell,
 kappa_w-kappainf=O(r^(k-1)).

Finally grad rho=O(r^2) at0 and O(r^(k-1)) at infinity, so 0<=bplus<=|grad rho| tends to0 at both ends. Both constants in (3) are positive for the exact ell>1. Uniform convergence proves eventual positivity, without assigning a radius.

## Dependencies and evidence

Dependencies are the exact modal specification and strain repair (proof 04), the all-mode joins and endpoint bounds (proof 50), and the canonical IPM conventions (proof 01). The code verifies the rational end constants and symbolic angular cancellation, and encloses the constants in Arb from the original exact k.

Verdict: CONFIRMED for regularity, qualitative endpoint and lift bounds, and eventual positivity. Global d positivity, an explicit positive global margin, injectivity, an inverse norm and nonlinear existence remain OPEN.
