# A turning-height obstruction for the globally quadratic Holder target

## Exact statement and scope

Use the normalized joined trial, canonical velocity, exact strain, and full column of topics217 and228. Put k=1615536043799051/9007199254740992, ell=1/k and V=ell X+U[rho0]. Let Z2=Z2_(alpha,beta,gamma), D2, T, Lren and A0 be exactly those of proof 228, with

 0<alpha<1, 2k-1<beta<k, gamma>4k.

Thus the local norm is ||chi h||E2, the annular norm on R<=r<=4R is R^(-beta) times

 ||h||infinity + R^alpha[h]_(x,alpha)
                  + R^(2+alpha)[h]_(y,2,alpha),

and the remaining term is L2((1+r^2)^(-gamma/2)). The vertical seminorm divides differences by x^2|y-y'|^alpha. Functions are even in x, odd in y, continuous and zero on x=0. D2 is the exact distributional maximal transport domain. All three operators are closed on D2 by proof 228.

The argument uses a SIMPLE turning height, certified below for the actual trial:

 there is s_*>0 with a(0,s_*)=0 and partial_y a(0,s_*) !=0,
 a(x,y)=V1(x,y)/x, extended through x=0.                 (H)

The local stationary-phase argument uses a smooth field near the chosen height and a slightly lower initial height. The certificate places this entire neighborhood strictly inside one analytic radial cell. Global C2 punctured regularity suffices for the all-future variational estimates; it follows from the actual C6 density regularity. The actual global axis sign and far-field bounds of topics88,214,227 are also used.

For the actual trial, T:D2->Z2 is not onto whenever alpha>1/2. Neither Lren nor A0 is onto whenever alpha>2/3. The latter statements include the COMPLETE velocity and the full moving-tail column. They hold even without a cubic normalization. The proof supplies bounded sequences of smooth compactly supported, zero-strain, zero-jet forcings and rules out uniformly bounded choices of their preimages. It does not identify the actual residual F0 as being outside a range, prove nonexistence of a profile, prove an infinite-dimensional cokernel, or address alpha<=2/3 for the full operator.

Hypothesis(H) is certified below. The interval arithmetic and analytic proof have been independently derived in this team; the separate independent audit is pending. A degenerate turning height is not covered by this proof.

## Original-data interval certificate of a simple turn

Let t=log y and d(t)=V2(0,exp(t))/exp(t). The exact divergence identity div V=2ell gives

 a(0,exp(t))=2ell-d(t)-d'(t).                         (CT1)

In the modal convention of the certified Green reconstruction,

 d(t)=ell-sum_(n=1)^261 (-1)^n P_n(t),
 a(t)=ell+sum_(n=1)^261 (-1)^n(P_n(t)+P'_n(t)).         (CT2)

No angular truncation beyond the exact finite expansion is used. The canonical normalization is the same exact joined trial as proof 228, including its scalar repair.

The script code/certify_turn.py encloses the following rational t-interval:

 L=4533/2048, R=145057/65536,
 2490080864828181/1125899906842624 < L < R
                       <4984432832360809/2251799813685248.   (CT3)

The outer endpoints displayed in(CT3) are the neighboring exact knots of spline span705. Directed512-bit and640-bit computations give

 -0.000014 < a(L) < -0.000013,
  0.000096 < a(R) <  0.000097,
  7.1952 < a_t(t) < 7.1954 for EVERY t in[L,R],
  0.7866 < a_y(0,exp(t)) <0.7868 for EVERY t in[L,R],
  9.1465 < exp(t) <9.1468 for EVERY t in[L,R].          (CT4)

All printed decimals in(CT4) are deliberately widened rational bounds. Therefore exactly one zero t_* lies in(L,R), and s_*=exp(t_*) is a simple turning height with a_y>0. No uniqueness assertion outside this interval is made. The strict separation from both radial knots gives an analytic annulus about this axis segment. The modal density there is a finite polynomial in log r times r^3 and angular functions; its finite Green functions solve analytic ordinary differential equations there. Hence V is smooth on a small planar neighborhood of the turn. Choose y0<s_* and both height intervals inside this annulus.

Here is the enclosure method, including the derivative interval rather than just point samples. The exact binary source NPZ is reconstructed using the independently verified rational spline coefficients, exact joining convention, scalar-repair enclosure and Green endpoint cache. On span705, each P_n is represented as a finite exponential polynomial centered at (L+R)/2. Formula(CT2) and its exact derivative are formed before enclosure. Expand each exponential-polynomial term to degree16 on the interval of half-width h=(R-L)/2. For a term v x^j exp(e x), the absolute omitted part is bounded by

 |v| h^j exp(|e|h)(|e|h)^(17-j)/(17-j)!, j<=7.

The sum of nonconstant Taylor coefficient magnitudes plus this remainder encloses the entire interval around the constant coefficient. The same construction is applied to a_t. Endpoint signs use directed evaluation of the exponential-polynomial representation. An independent center calculation obtains d,d',d'' from the original Green ODE recurrence, using density and its first derivative, and checks overlap with both a and a_t. Finally a_y=a_t/exp(t), with a positive exponential interval. The sign and derivative tests pass at both precisions. Bisection chooses the rational interval but is not used in place of an interval derivative bound.

The exact source SHA is a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874, the independently verified Green cache SHA is817da858bacb71182584aef99311572a8212e4525105de775dedb8bb513c5da2, and the scalar-repair SHA is d9d13c3d31214057f90d9585decd585c464fbc120f2c2c756868532618dddbb6. The complete rational endpoints, source and code hashes, both-precision results and center checks are preserved in evidence/turn_certificate.json, SHA0c0efde05da80d130d6244ed3aad0e31ccd856359a4099f27807cd7e4cc4afd8. The calculation took39.164seconds single-thread. Its Python code is not a formal proof; the analytic enclosure argument and the previously checked source/cache construction justify the interval claims.

## Uniform actual orbits near the outgoing vertical axis

By the established zero geometry, V2(0,y)>0 for every y>0. Choose a height y0<s_* at which a(0,y0) !=0, and a small interval I about y0 lying strictly below a small interval J about s_*. Hypothesis(H) permits these choices, possibly after moving y0 close to s_*. For initial point (q,y), 0<q<q0 and y in I, write the full forward flow as Phi_t(q,y)=(x_t,y_t).

The same finite-time and far-field argument as proof 227, uniform for y in the compact interval I, gives

 c q exp(ell t)<=x_t<=C q exp(ell t),
 c exp(ell t)<=y_t<=C exp(ell t),
 c exp(ell t)<=r_t<=C exp(ell t),                       (1)

for every t>=0. The orbits stay in a fixed thin cone about the positive vertical axis. They cross J with positive vertical speed and never return to it after leaving a fixed slightly larger annulus. In the initial compact segment this follows from V2>0 in a sufficiently thin axis neighborhood. In the far segment, V2/y=ell+O(r^(k-1)) is positive and the error is integrable along each orbit.

We also need a comparison for different initial heights, which is stronger than the ordinary flow Lipschitz bound:

 |x_t(q,y)-x_t(q,y')|<=C q exp(ell t)|y-y'|,
 |y_t(q,y)-y_t(q,y')|<=C exp(ell t)|y-y'|.             (2)

On the compact initial segment, differentiating V1=x a gives the first estimate by a scalar linear equation, since the initial x derivative with respect to y is zero. On the far segment, DV=ell I+O(r^(k-1)) gives ||D Phi_t||<=C exp(ell t). Moreover Da=O(r^(k-2)), uniformly in the thin cone, so

 partial_y log(x_t/q)=integral_0^t Da(Phi_s).partial_y Phi_s ds

is uniformly bounded: its far integrand is O(exp(ell(k-1)s)), and its initial part is bounded. This proves the first line of(2) for all time. The second is the ordinary variational estimate. All derivatives used exist for the actual punctured C4 field.

At large radius the proof 228 divided velocity bounds are

 ||U[h]||infinity+r^alpha[U[h]]_(C^alpha)<=C N r^beta,
 ||U1[h]/x||infinity+r^alpha[U1[h]/x]_(y,alpha)
                                             <=C N r^(beta-1),  (3)

where N=||h||Z2. The same bounds, with a changed constant and radius bounded above and below, hold on the fixed compact annulus containing the initial trajectories. This follows from the same localized proof of proof 228. No global unscaled E2 membership is assumed.

## Whole-trajectory differences of the complete coupling

Let delta=|y-y'|<=delta0. Compare the two points in(2) at each fixed time, first horizontally and then vertically in a comparable-radius annulus. Their abscissas are comparable to q r and their ordinate difference is O(r delta).

For the horizontal step, ordinary C^alpha regularity of U1 and the supremum of its quotient give

 |Delta_x(U1/x)|
 <=C N r^(beta-1)(q^(alpha-1)delta^alpha+delta).

Indeed |Delta_x U1|/|x| is bounded by C N r^(beta-alpha)(q r delta)^alpha/(q r), and the denominator difference costs C N r^(beta-1)delta. For the vertical step, the divided vertical estimate in(3) gives C N r^(beta-1)delta^alpha. Also the full difference of U2 is at most C N r^beta delta^alpha. No horizontal Holder estimate for U1/x itself has been assumed.

Write

 (U[h].grad rho0)/x^2 = a1(U1[h]/x)+a2 U2[h],
 a1=rho0_x/x=O(r^(k-2)), a2=rho0_y/x^2=O(r^(k-3)).

Their first derivatives have one further inverse power of r, and they have bounded corresponding derivatives on the compact initial annulus. Equations(1)-(3), including the variation of x_t^2 and of the coefficients, therefore show

 |Delta(U[h].grad rho0)(Phi_t(q,.))|
 <=C N (q^(1+alpha)+q^2) delta^alpha
                                      exp(ell(beta+k-1)t).    (4)

For q<1 this is bounded by twice its first q-power. For M0, the divided coefficient has order r^(2k-3)(1+log r), with first derivatives of order r^(2k-4)(1+log r), and is smooth on the compact initial annulus. Its two-orbit difference is at most C q^2 delta (1+t)exp(ell(2k-1)t). The compact H0 obeys the corresponding finite-time bound. Since |c[h]|<=C N, integration of all these differences against exp(-t) yields

 |I_C(h;q,y)-I_C(h;q,y')|
 <=C N q^(1+alpha)delta^alpha,
 I_C(h;q,y)=integral_0^infinity exp(-t)C[h](Phi_t(q,y))dt,    (5)

for C=C0 or Cren. The velocity exponent after multiplication by exp(-t) is ell(beta-1)<0. The column exponent is 1-ell<0. Thus(5) includes the entire future trajectory, not merely the turning neighborhood. For C=0 the left side is zero.

Every h in Z2 has, on the fixed initial-height annulus,

 |h(q,y)-h(q,y')|<=C N q^2|y-y'|^alpha.               (6)

This follows either from the local E2 term or from a finite number of annular terms. It is valid at any fixed positive y0, without requiring y0<2.

## Uniform stationary-phase lemma used here

Suppose a real C6 phase phi on a fixed compact interval has one critical point s_c in its interior, |phi''(s_c)|>=b>0, no other critical point, and uniformly bounded C6 norm; suppose the C2 compactly supported amplitude A and its derivatives are uniformly bounded, with A(s_c)>=b. If all these bounds are uniform over a compact parameter set, then uniformly as lambda tends to infinity,

 integral A(s)cos(lambda phi(s))ds
 = sqrt(2pi/lambda) A(s_c)/sqrt(|phi''(s_c)|)
       cos(lambda phi(s_c)+sign(phi''(s_c))pi/4)
       +O(lambda^-1).                                  (7)

For completeness, split with a fixed smooth cutoff about the unique critical point. Off that neighborhood integrate exp(i lambda phi)/(i lambda phi') by parts, which gives O(lambda^-1). On it use the C4 Morse coordinate u with phi=phi(s_c)+sign(phi'')u^2/2. The transformed amplitude B is C2 with uniformly bounded derivatives through order two. Subtract B(0) times a fixed even cutoff equal one near0. The remaining amplitude is u times a bounded piecewise C1 function. Integration by parts using partial_u exp(i lambda sign(phi'')u^2/2)=i lambda sign(phi'')u exp(...) gives O(lambda^-1); its derivative is integrable with a uniform bound, by the original C2 amplitude and C6 phase bounds. The constant term is the Fresnel integral plus an O(lambda^-1) cutoff tail. Its value is sqrt(2pi/lambda)exp(i sign(phi'')pi/4), obtained by inserting exp(-epsilon u^2), evaluating the Gaussian integral, and taking epsilon down to zero after the tail integration by parts. This proves(7) with uniform constants. The same proof applies when the critical point and amplitude vary smoothly with small q and y in I.

## Bounded smooth forcing packets

Choose a nonnegative smooth g_+ supported in J with g_+(s_*)>0 and let g be its odd extension. For q>0 and epsilon>0 let

 F_(q,epsilon)(x,y)=x^2 phi(x/q) cos(x/epsilon) g(y),     (8)

where phi is a fixed smooth even compact cutoff equal one throughout the abscissa range of the trajectories while they meet J. More explicitly, the ratios x_t/q in that crossing lie in a fixed interval [b,B]; choose phi=1 for |z|<=2B. Its compact support is fixed. This choice works uniformly for small q and every y in I.

The functions are smooth, compactly supported away from the origin, have the physical parities and vanish on the vertical axis. Their vertical divided seminorm is uniformly bounded by C[g]_alpha. Their horizontal seminorm is at most

 C(q^2 epsilon^-alpha+q^(2-alpha)),

by the supremum and derivative interpolation estimates for the cosine and cutoff. Their weighted L2 norms tend to zero. Consequently

 ||F_(q,epsilon)||Z2<=C whenever q^2<=epsilon^alpha.     (9)

Each individual packet also belongs to D2, since it is smooth and compact, with the required axis divisibility preserved by V1=x a. Its graph norm is not claimed uniformly bounded.

Choose a fixed smooth compact q_c supported outside the thin cone traversed by all these trajectories, with c[q_c]=1 and J(q_c)=0. The parity-reflected bump construction of proof 227 provides one. Replace F by

 f_(q,epsilon)=F_(q,epsilon)-c[F_(q,epsilon)]q_c.         (10)

Boundedness of c on Z2 preserves(9); these forcings have exact c=J=0. The correction vanishes on every trajectory in question.

## Actual turning phase and a large vertical difference

Parametrize each crossing of J by its height s. Write its abscissa as X(s;q,y). The scalar equation is

 partial_s X=V1(X,s)/V2(X,s), X(y;q,y)=q.

Parity and smoothness in the certified analytic annulus give, uniformly with the needed derivatives on J times I,

 X(s;q,y)/q -> Lambda(s;y)
 =exp(integral_y^s a(0,v)/V2(0,v)dv) as q->0.           (11)

At s=s_*, Lambda_s=0 and Lambda_ss=Lambda a_y(0,s_*)/V2(0,s_*) !=0. Shrink J so that this is its unique critical point. For small q, the phase phi_(q,y)(s)=X(s;q,y)/q has exactly one nondegenerate critical point s_c(q,y) in J, with uniform bounds for(7). The phase value v_q(y)=phi_(q,y)(s_c(q,y)) has

 v'_q(y) -> -a(0,y)Lambda(s_*;y)/V2(0,y),              (12)

uniformly on I. Its derivative is bounded away from zero by the choice of y0. The exact travel time tau(s;q,y) and vertical speed yield the forcing integral

 I_F(q,y)=q^2 integral_J A_(q,y)(s)cos(lambda phi_(q,y)(s))ds,
 lambda=q/epsilon,
 A_(q,y)=exp(-tau) (X/q)^2 g(s)/V2(X,s).               (13)

Its amplitude is smooth with uniform derivative bounds and positive at the critical point. No leading approximation to the rapidly oscillating phase is substituted into(13). In particular an error of size q^3/epsilon is never discarded.

By(7), I_F=q^2 lambda^-1/2 B_q(y)cos(lambda v_q(y)+sigma pi/4)+O(q^2/lambda), where B_q is uniformly positive and has bounded first derivative. Equation(12) allows, for each sufficiently large lambda, two points y_lambda,y'_lambda in I converging to y0, separated by comparable positive multiples of lambda^-1, such that the two cosine values are 1 and -1. Hence

 |I_F(q,y_lambda)-I_F(q,y'_lambda)|
                         >=b q^2 lambda^-1/2.          (14)

This holds uniformly for sufficiently small q and sufficiently large lambda. The exact zero-strain correction has no effect on it.

## Closed-domain and open-mapping contradiction

If (T+C)h=f, the exact maximal-domain equation and the C1 flow-box argument give

 h(q,y)=-I_F(q,y)+I_C(h;q,y).                           (15)

The terminal value vanishes because |h(Phi_t)|<=C N exp(ell beta t), and beta<k. This argument does not assume smooth density in Z2. It applies to any preimage in D2. Combining(5),(6),(14),(15), with delta comparable to lambda^-1, gives

 b q^2 lambda^-1/2
 <= C N (q^2 lambda^-alpha+q^(1+alpha)lambda^-alpha).   (16)

For T alone the second term is absent.

A surjective closed operator from the Banach graph domain D2 onto Z2 would, by the open mapping theorem, admit choices of preimages with ||h||Z2<=K||f||Z2. Injectivity or a linear right inverse is not required. Apply this to the uniformly bounded forcings(10).

For T choose epsilon=n^-1, q=n^-kappa with alpha/2<kappa<1. Then(9) holds and lambda=n^(1-kappa) tends to infinity. Dividing(16), without its second term, by q^2 lambda^-1/2 contradicts alpha>1/2 and bounded N.

For C0 or Cren assume alpha>2/3 and choose

 alpha/2<kappa<2alpha-1<1.

The first ratio on the right after division tends to zero. The second is

 q^(alpha-1)lambda^(1/2-alpha)
       =n^((1+kappa)/2-alpha) ->0.                    (17)

This contradicts(16) for bounded N. Therefore these operators are not onto at the stated thresholds, under(H).

## Dependencies and exclusions

Proof 228 supplies the exact Z2 norm, canonical divided velocity estimates, bounded strain, closed maximal realizations and the full column bounds. Proof 227 supplies the actual all-future axis orbit geometry and the characteristic-domain justification, re-derived here with the height-variation estimate(2). Topics88 and217 supply the zero geometry and full moving-tail column. The stationary-phase estimate, forcing norms, full coupling difference and open-mapping contradiction are proved above.

The conclusion is non-surjectivity, not an infinite cokernel or nonclosed range statement. No property of the actual residual's range follows. The simple-turn hypothesis is certified by(CT1)-(CT4). The exterior inverse of proof 228 is unaffected, because a=V1/x is positive sufficiently far away, so the turning height lies in the bounded middle region. No claim for a degenerate turn is made.
