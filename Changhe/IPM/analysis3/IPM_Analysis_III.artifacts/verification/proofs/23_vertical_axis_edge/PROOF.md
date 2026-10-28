# A local vertical-axis estimate beyond the usual weight range

## Statement, spaces and scope

Let 5/2<a<9/2 and R>0. Let H_(a,R) consist of measurable functions h(x,y),
even in x, zero for |x|>=R, with norm

 ||h||_(a,R)^2 = integral_R integral_0^R |h(x,y)|^2 x^(-2a) dx dy.

Oddness in y may be imposed, but is not needed for the estimates. The
half-strip norm is used consistently; the full-strip norm is sqrt(2)
times this norm. The canonical IPM velocity has Fourier multiplier
( xi eta/(xi^2+eta^2), -xi^2/(xi^2+eta^2) ). It is well-defined in unweighted
L2 because ||h||_2 <= sqrt(2)R^a ||h||_(a,R).

Initially take smooth h supported away from x=0 and from |x|=R, compact
in y. Write T h=U2[h](0,.) and T1 h=partial_x U1[h](0,.) on this core.
They extend to the stated weighted space by the formulas below. In the
whole theorem these symbols mean those extensions; a pointwise trace is
not assumed for an arbitrary measurable h.

There are explicit finite constants C_a,D_a,B_a, defined below, such that

 ||x(U1[h]-x T1 h)||_(a,R) <= C_a R ||h||_(a,R),                 (1)
 ||x^2(U2[h]-T h)||_(a,R) <= C_a R^2 ||h||_(a,R),               (2)
 ||x^3 U1[h]||_(a,R) <= D_a R^3 ||h||_(a,R),                   (3)
 ||x^4 U2[h]||_(a,R) <= D_a R^4 ||h||_(a,R),                   (4)
 ||partial_y^j T h||_L2(dy) <= B_a R^(a-j-1/2)||h||_(a,R),
                   j=0,1,2, and T1=-partial_y T.             (5)

The output norms in (1)-(4) are restricted to 0<x<R. One possible, far
from sharp, choice is

 B_a=max{(2a+1)^(-1/2), [Gamma(2a+1)/2^(2a+1)]^(1/2)},
 C_a=1+10*2^(a+1/2)+64[1+1/(9/2-a)]
          +2[1/(a+1/2)+1/(a-1/2)+1/(a-3/2)+1/(a-5/2)],
 D_a=C_a+B_a/sqrt(9-2a).

Suppose a background, on this strip, has the exact derivative expansions

 rho_x=2x rho_2(y)+x^3 r1(x,y),
 rho_y=x^2 rho_2'(y)+x^4 r2(x,y),

with the four displayed coefficients bounded. Subtract its entire x^2
velocity-coupling jet, and define

 E_R h=U[h].grad rho-x^2[2rho_2 T1 h+rho_2' T h].

Then

 ||E_R h||_(a,R) <= [2C_a R ||rho_2||_infinity
   +C_a R^2 ||rho_2'||_infinity
   +D_a R^3 ||r1||_infinity+D_a R^4 ||r2||_infinity]||h||_(a,R). (6)

In particular the strip-to-strip remainder coupling has norm tending to
zero as R tends to zero, if the coefficient bounds remain uniform. For
rho_2 in C_c^2(R), its jet coupling 2rho_2 T1+rho_2' T is compact from
H_(a,R) into L2(dy). The same statement holds after a smooth compact
cutoff in y.

These are local-strip estimates for a remainder input. They do not prove
the global edge Garding hypothesis of the theory author's draft. In particular
there is no product weight in y, no assertion about the origin corner,
no estimate for an independent x^2-axis-jet input, and no control here of
input outside the strip. On a fixed compact y interval away from0,
bounded positive weights are harmless norm changes. A proof still has
to control the interactions between such intervals and the origin.

## Fourier kernel and exact cancellation

Take the unitary Fourier transform in y, with frequency eta, and put
lambda=|eta|. For x,s>0 the even-input Green formula is

 U2hat(x,eta)=-hhat(x,eta)
       +lambda integral_0^R exp(-lambda max(x,s))
                         cosh(lambda min(x,s)) hhat(s,eta) ds,            (7)
 U1hat(x,eta)=i eta integral_0^R k_lambda(x,s) hhat(s,eta)ds,
 k_lambda(x,s)=-exp(-lambda s)sinh(lambda x),          x<s,
               exp(-lambda x)cosh(lambda s),         x>s.                (8)

To derive these identities, solve
(-partial_x^2+lambda^2)psihat=partial_x hhat on the line with the decaying
Green kernel exp(-lambda|x-s|)/(2lambda), integrate by parts in s, and
combine the positive and negative s integrals. Then U1hat=-i eta psihat
and U2hat=partial_x psihat. Differentiation of the sign kernel contributes
the -hhat term in (7). The formulas at lambda=0 are interpreted as their
limits; that single Fourier frequency does not affect an L2 estimate.

On the smooth core hhat vanishes near x=0. Consequently

 That(eta)=lambda integral_0^R exp(-lambda s) hhat(s,eta)ds,
 T1hat(eta)=-i eta That(eta).                                             (9)

Thus the kernel for A=x(U1-xT1), with the factor i eta retained, is

 x[-exp(-lambda s)(sinh(lambda x)-lambda x)],              x<s,
 x[ exp(-lambda x)cosh(lambda s)+lambda x exp(-lambda s)], x>s.           (10)

The kernel for B=x^2(U2-T) is -x^2 times the identity plus

 lambda x^2[exp(-lambda max(x,s))cosh(lambda min(x,s))
                                      -exp(-lambda s)].                 (11)

The first cancellation in (10) is cubic in lambda x, and the one in
(11) is quadratic in lambda x. In both cases the remaining weighted
output vanishes to fourth order in x. This is the reason the upper
threshold is a<9/2.

## Uniform weighted kernel bounds

Here are full Schur bounds, to avoid an appeal to a weighted singular
integral theorem outside its applicable range. Fix eta. For a positive
kernel bound K(x,s), conjugation by the weight gives x^(-a)K(x,s)s^a.
Use the Schur helper p(x)=x^(-1/2). The two required integrals are

 x^(1/2-a) integral_0^R K(x,s)s^(a-1/2)ds,
 s^(a+1/2) integral_0^R K(x,s)x^(-a-1/2)dx.                              (12)

Bounds M for both imply operator norm at most M on L2(x^(-2a)dx).
Split the square into s>2x, x>2s, and x/2<=s<=2x.

For s>2x, the elementary inequalities
sinh z-z<=z^3 exp(z)/6, cosh z-1<=z^2 exp(z)/2, and
u^n exp(-u)<=n! give

 |K_A(x,s)| <=64 x^4/s^4,
 |K_B(x,s)| <=24 x^4/s^3.                                               (13)

Here K_A includes |eta|=lambda, and K_B refers only to (11).
For A the row integral in (12) is at most
64 x integral_2^(R/x) v^(a-9/2)dv <=64R,
since a-9/2<0. The column integral is
64 s*2^(a-9/2)/(9/2-a) <=64R/(9/2-a).
For B the row integral is at most
24 x^2 integral_2^(R/x) v^(a-7/2)dv <=12R^2,
since a-7/2<1. Its column integral is
24 s^2*2^(a-9/2)/(9/2-a) <=24R^2/(9/2-a).
An empty interval contributes zero. Thus this region is controlled by
the 64[1+1/(9/2-a)] term of C_a, at the appropriate power of R.

For x>2s, split the original Green part and the subtracted trace part.
Their respective absolute kernel bounds are

 A: 2,                 2x^2/s^2,
 B: 2x,                  x^2/s.                                        (14)

For example lambda x exp(-lambda x/2)<=2 and
(lambda s)^2 exp(-lambda s)<=2. Direct integration in (12), using
x,s<R and a>5/2, gives the following sufficient bounds for the row and
column integrals, respectively:

 A first: R*2/(a+1/2),       R*2/(a-1/2),
 A trace: R*2/(a-3/2),       R*2/(a-5/2),
 B first: R^2*2/(a+1/2),     R^2*2/(a-3/2),
 B trace: R^2/(a-1/2),       R^2/(a-5/2).                                (15)

The omitted factors are powers of2 at most1. For instance the second
column integral for A is
2s^(a-3/2) integral_(2s)^R x^(3/2-a)dx
 <=2s*2^(5/2-a)/(a-5/2).
The sum of the four reciprocals in C_a dominates both required sums.

In the comparable region the original Green parts are bounded by
lambda R exp(-lambda|x-s|) for A and
lambda R^2 exp(-lambda|x-s|) for B. Their integrals in either variable
are at most2R and2R^2. The trace parts are bounded by8 for A and2R for B,
so their integrals are at most8R and2R^2. Both conjugated/helper weight
ratios are at most2^(a+1/2). This gives10*2^(a+1/2)R for A and
4*2^(a+1/2)R^2 for B. Finally the local multiplier -x^2 in B has norm R^2.
Combining all regions proves (1)-(2) uniformly in eta. Plancherel then
proves the corresponding strip estimates. All kernels can first be
truncated on the smooth core; the bounds justify their extension and
the limiting operations.

## Trace regularity, compactness and the coefficient remainder

By Cauchy-Schwarz in (9), for j=0,1,2,

 |eta|^j |That(eta)| <=lambda^(j+1)
       [integral_0^R s^(2a)exp(-2lambda s)ds]^(1/2)
       ||hhat(.,eta)||_L2(s^(-2a)ds).

For lambda<=1/R, use integral<=R^(2a+1)/(2a+1). For lambda>=1/R, use
integral<=Gamma(2a+1)/(2lambda)^(2a+1). Because j+1/2-a<0 for all three
values of j, these two estimates prove (5) with B_a. The relation between
T1 and T is (9). These are derivative bounds at fixed R, not homogeneous
bounds uniform over all R for an inhomogeneous H2 norm.

Now x^3 U1=x^2 A+x^4 T1 and x^4 U2=x^2 B+x^4 T.
The norm of x^4 as a function on (0,R) is
R^(9/2-a)/sqrt(9-2a). Combining this with (5) proves (3)-(4).
Multiplication by the four bounded coefficients in the statement gives
exactly

 E_R h=2rho_2 A+rho_2' B+r1 x^3U1+r2 x^4U2,

and proves (6). The two traces map boundedly into H2 and H1 in y,
respectively. Multiplication by compact C2 coefficients places the jet
coupling in a bounded subset of H1 on a fixed bounded interval, whose
inclusion into L2 is compact. For completeness, that compactness follows
by approximating H1 functions by their averages on intervals of length
ell: the L2 approximation error is at most ell times the derivative
norm, and the average-valued approximation has finite-dimensional range.
This proves compactness without any unlisted regularity hypothesis.

Smooth functions supported away from the vertical axis and the outer
strip boundary, then truncated and smoothed in y, are dense in H_(a,R).
Equations (1)-(5) give unique bounded extensions to the completion. The
unweighted velocity converges in L2 as well, so these extensions agree
with the canonical velocity and the distributionally defined subtractions.
This completes the theorem. Its constants and its local scope should not
be replaced by a global inverse statement.
