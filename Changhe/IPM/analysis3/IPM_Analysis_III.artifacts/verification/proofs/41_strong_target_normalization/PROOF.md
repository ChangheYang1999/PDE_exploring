# Local normalization is required before taking the strong target

## Statement

Let a=17/4 and eta=5/4. In the parity class even in x and odd in y, define

 w(X)=|x|^(-2a) for r<1,
 w(X)=|cos(theta)|^(-2a) r^(-eta) for r>=1,
 R=L2(w dX),
 G=L2(exp(-t/2)dt on t<0; exp(27t/4)dt on t>=0),
 E gamma=x^2 y gamma(log r), and Y=E G direct-sum R.

Let rho be the exact normalized modal background of V005 and V042. Write p=x^2y, ell=1/k, V=ell X+U[rho]. Let chi0 be smooth, radial, one near0 and zero outside a compact set, and H0=chi0 X.grad rho/3. Thus H0=p+O(r^5) at0 and has the same parity and vertical-axis vanishing as rho. The O(r^5) assertions below may be replaced by O(r^5(1+|log r|)); the same integrability conclusions hold.

For the formal expressions

 Lfix h=(V.grad-1)h+U[h].grad rho,
 Lren h=Lfix h+c[h]H0,

the following assertions hold.

1. There is a smooth compactly supported h in R, vanishing near0, with J(h)=0 and c[h]>0, such that Lfix h is not in Y.
2. H0 is not in Y. Consequently c[.]H0 is not a bounded rank-one operator from R to Y, even though c is bounded on R.
3. For this same h, Lren h belongs to Y. The local cubic cancellation is part of the definition of the strong-target realization; it cannot be treated as an ordinary bounded perturbation of an R-to-Y realization of Lfix.

This does not refute the radial-space Fredholm theorem for Lfix, whose target is different. It also does not refute a theorem formulated with an explicitly enlarged target. It identifies a domain-and-range requirement for transferring that theorem to the axis-jet space.

## Construction and strain

Choose any nonnegative smooth nonzero radial function eta0 supported in 2<r<3, and put

 h(x,y)=x^4 y eta0(r).

This h is smooth and has the required parity. On its supporting annulus its square times the angular weight has order |cos(theta)|^(8-2a)=|cos(theta)|^(-1/2), which is integrable. Hence h belongs to R. All its origin jets vanish. The angular identity

 (1/pi) integral_0^(2pi) cos(theta)^4 sin(theta) sin(3theta)dtheta=3/16

gives

 c[h]=(3/16) integral_2^3 r^3 eta0(r)dr>0.

The strain functional is indeed bounded on R: its kernel is pi^(-1)r^(-3)sin(3theta). The squared dual integral is finite near0 since its radial factor is r^(2a-5)dr and a>2, and at infinity since its radial factor is r^(eta-5)dr and eta<4. The angular dual factor |cos(theta)|^(2a) is bounded and integrable. Cauchy-Schwarz therefore gives a finite operator norm.

## Why the image is excluded

The velocity of h is analytic near0 because h vanishes there. Parity and its canonical strain imply

 U[h](X)=c[h](-x,y)+O(r^3).

The exact background has rho=p+O(r^5), with the corresponding first-derivative expansion. Since h and its derivatives vanish near0,

 Lfix h=U[h].grad rho=-c[h]p+O(r^5).

The vertical-axis factor of this smooth expression is therefore

 gamma_fix(t)=lim_(x->0) (Lfix h)(x,e^t)/(x^2 e^t)
             =-c[h]+O(exp(2t)) as t->-infinity.

For a smooth function with a quadratic vertical-axis factor, membership in Y forces its E coordinate to equal this axis factor almost everywhere. To see this, if F-E gamma belongs to R, then for almost every r the angular integral is finite. A nonzero residual coefficient of x^2y at theta=pi/2 would make that integral contain |cos(theta)|^(4-2a)=|cos(theta)|^(-9/2), which diverges. The coefficient must vanish. This also proves uniqueness of the E G direct-sum R decomposition.

But gamma_fix is bounded away from0 for all sufficiently negative t, and

 integral_(-infinity)^0 exp(-t/2)dt=infinity.

Thus gamma_fix is not in G, proving Lfix h not in Y. The same argument, with axis factor1+O(exp(2t)), proves H0 not in Y.

## Why the corrected image is included for this test

Near0, Lren h has no cubic term, its axis factor is O(r^2), and subtracting its E coordinate leaves an x^4y remainder of order r^5. The same angular and radial calculation as V042 gives integrability: angular exponent8-2a=-1/2 and squared radial exponent12-2a=7/2 in dt.

On bounded annuli, all coefficients are smooth, with at least the C5 radial regularity of the exact modal representation, and the E subtraction leaves the x^4y angular factor. At infinity, compact support and oddness in y imply integral h=0. The canonical velocity kernel is homogeneous of degree-2, so its far-field expansion starts at degree-3: U[h]=O(r^(-3)), with the same decay after scaled differentiation. Since grad rho=O(r^(k-1)), Lfix h=O(r^(k-4)). Its axis factor is O(r^(k-7)), and its E-subtracted remainder has an x^4y angular factor by parity and smoothness. The far squared radial exponent of the density is2(k-4)+2-eta<0. Therefore both components are integrable and Lren h belongs to Y.

## A valid enlarged-target formulation

One may instead define Ytilde=Y direct-sum span{H0}, with its direct-sum norm. On an appropriate domain for which Lfix h belongs to Ytilde, its forbidden cubic coordinate is -c[h]. Then Lren is the Y component of Lfix under the bounded projection Ytilde->Y. This formulation can be used in a block Fredholm argument, but the mapping into Ytilde and the resulting block domain must be proved. It is not the assertion that c[.]H0 is a bounded perturbation with values in Y.

## Dependencies and scope

The proof uses the canonical kernel and strain from V002, the exact local normalization and modal expansions from V005 and V036, and the target decomposition and endpoint integrability from V042. It gives a smooth counterexample to an incorrect mapping claim. It proves neither a global coupling bound nor a global inverse.
