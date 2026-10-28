# Nonlinear obstructions in Holder and Holder graph norms

## Operator, hypotheses and exact scope

Let rho be the exactly normalized modal background. Write

    V=ell X+U[rho], G=X dot grad rho,
    Lg=V dot grad g-g+U[g] dot grad rho+(c[g]/3)G,
    N(h)=(U[h]+(c[h]/3)X) dot grad h.

The velocity multiplier is m(xi)=(xi_1 xi_2/|xi|^2,-xi_1^2/|xi|^2). It is real, even and perpendicular to xi. All densities are even in x and odd in y. On compact smooth densities supported away from0,

    c[h]=(1/pi) integral h(X) sin(3theta)/r^3 dX.

The background has bounded C^alpha gradient globally for every0<alpha<1, is C2 on each compact set away from0, and its velocity is C2 there. These facts follow from the finite exact modal construction and its inner/outer expansions, with k<1; no numerical bound is needed here. Its transport has V2(x,0)=0 and V1(x,0)=-Ax+o(x), A>0. Thus there are regular axis points x0>0 arbitrarily close to0, without any assumption about the sign of a sampled field along an entire axis interval. There are also regular points in the open first quadrant. For the constructions below choose both points strictly inside the innermost modal region and away from0. On a sufficiently small neighborhood of each point, rho and V are smooth: the modal sums, powers and logarithms are smooth away from0 inside this region. Choose every local box, its reflection and its short flow tubes inside this smooth region. Thus the smooth-flow assertion below uses local smoothness, not merely the global C2 statement. The operator conventions and these expansions are those of topics01,04 and15.

Fix alpha in(0,1). For a fixed compact set K, let X be a normed space on which L is distributionally defined near K, with

    ||g||_(C^alpha(K))+||U[g]||_(C^alpha(K))+|c[g]|
        <=C_X ||g||_X.                                  (H)

The arguments below concern every g in X solving a specified equation near K. They do not assume a global inverse exists. If an inverse does exist on these forcings, the lower bounds apply to that inverse. All constructed input densities are smooth, compactly supported away from0, and have J=0 and c=0 exactly.

We prove two results.

A. Near a regular axis point there are uniformly C^alpha-bounded inputs h_n such that

    ||N(h_n)||_infinity >=n^(1-2alpha)-C n^(-2alpha),
    ||N(h_n)||_(C^alpha)>=c n^(1-alpha),
    ||g||_X>=c_X n^(1-alpha)-C_X

whenever Lg=N(h_n) near K.

B. On a fixed union K of four boxes away from both axes there are inputs h_n such that

    sup_n (||h_n||_(C^alpha)+||Lh_n||_(C^alpha))<infinity,
    ||N(h_n)||_(C^alpha)>=c n,
    ||g||_X>=c_X n

for every g satisfying(H) and Lg=N(h_n) near K, for sufficiently large n. Consequently the nonlinearity is unbounded on a bounded set of the Holder graph domain, and the graph-norm version of the proposed perturbative closure fails. This result supplies a complete proof in place of the theory author's graph and off-axis sketches.

These are obstructions to a bounded fixed-point map in the specified norms. They do not rule out a stronger quasilinear iteration, a change of unknown, or a norm in which the input sequences are unbounded.

## A: exact crossing-wave construction

Choose a small box B+ around a regular point X0=(x0,0), with V1 nonzero throughout it, and its x-reflection B-. Let K=B+ union B-. Choose a smooth phi, even in x and y, supported in the interiors of these boxes, equal1 on smaller boxes around plus-or-minus X0. Set

    S_n=2 cos(nx)sin(ny)=sin(n(x+y))-sin(n(x-y)),
    h_n^0=n^(-alpha) phi S_n.

The standard difference estimate min(2,n|X-X'|) gives ||h_n^0||_C^alpha<=C. Its support avoids0, so all its center jets vanish. The strain kernel is smooth on K. Repeated integration by parts in y gives c[h_n^0]=O(n^(-M)) for every M, with constants depending on M and the fixed cutoffs.

Choose a smooth class-P function zeta with c[zeta]=1, supported inside K but outside the smaller boxes and their short flow tubes. Such a function exists: choose a nonnegative bump near (x0,y1), with small y1>0, where sin(3theta)>0, and reflect it evenly in x and oddly in y. Its strain is positive; divide by that exact real number. Define

    h_n=h_n^0-c[h_n^0]zeta.                              (1)

Then h_n is supported in K, J(h_n)=c[h_n]=0, and the C^alpha norms remain bounded. This repairs the support mismatch in the submitted proof: an exterior compensator would require enlarging the declared support.

For xi=n(1,1), eta=n(1,-1), put U_S=m(xi)sin(xi dot X)-m(eta)sin(eta dot X). Direct trigonometry gives

    U_S dot grad S_n=-n sin(2ny).                        (2)

Each self-interaction is zero since m(xi) dot xi=0. The two cross interactions produce(2).

Localization creates a controlled error. In Fourier variables,

    U[phi exp(i xi dot X)]-phi m(xi)exp(i xi dot X)

has amplitude bounded by the integral of |m(xi+zeta)-m(xi)||phihat(zeta)|. On |zeta|<=|xi|/2, smooth homogeneity bounds the multiplier difference by C|zeta|/|xi|. On the complement, boundedness of m and Schwartz decay give a bound smaller than any inverse power of n. Thus the error is O(n^(-1)) in L-infinity, and its first derivative is O(1). Formula(2), the cutoff derivative terms and(1) now give the global identity

    N(h_n)=-n^(1-2alpha)phi^2 sin(2ny)+e_n,
    ||e_n||_infinity<=C n^(-2alpha).                     (3)

The strain part of N is zero exactly. Every compensator term is smaller than any required inverse power after increasing the integration-by-parts order. At X0+(0,pi/(4n)), phi=1 for large n, proving the supremum lower bound. The nonlinearity has class-P parity, so it is exactly0 on y=0. Comparing these two points in(3) gives the C^alpha lower bound in A.

## Flow identity for distributional solutions

If g satisfies(H) and Lg=f near K, then

    V dot grad g=f+g-U[g] dot grad rho-(c[g]/3)G

is continuous. A C1 flow box for the nonzero field V changes this to a one-dimensional distributional derivative along flow time. The distributional fundamental theorem first holds for almost every transverse parameter; continuity then gives it for every parameter. Hence along each short trajectory remaining in K,

    exp(-tau)g(Phi_tau X)-g(X)
      =integral_0^tau exp(-s)[f-U[g] dot grad rho-(c[g]/3)G](Phi_s X)ds.   (4)

No differentiability of g transverse to V is assumed.

For the axis construction, write V2(x,y)=y beta(x,y), where |beta|<=B on the smaller boxes by the integral formula for partial_y V2. Choose a fixed tau>0 small enough that all trajectories from a fixed neighborhood of X0 remain where phi=1 and

    exp(B tau)<=sqrt(2).

A bound on the speed supplies a uniform such tau. No positive lower bound on beta is needed. For X_n=X0+(0,pi/(4n)), its y-coordinate along this trajectory lies between pi/(4sqrt(2)n) and sqrt(2)pi/(4n). Consequently

    sin(2n y(s))>=sin(pi/sqrt(2))>0.79.                 (5)

The value0.796 used in the submitted proof is larger than this sine and cannot be a rigorous lower bound. The actual sine is between0.79569 and0.79570.

The f-integral in(4) is zero for the trajectory through X0, by parity. For the trajectory through X_n, (3)-(5) give absolute value at least

    0.79(1-exp(-tau))n^(1-2alpha)-C n^(-2alpha).

The two trajectories remain at distance at most C/n. Subtract(4) at the two starting points. The g terms and U[g] dot grad rho terms are bounded by C||g||_X n^(-alpha), using(H) and the fixed C1 background coefficients. The strain-column difference is bounded by C|c[g]|/n and hence by the same expression. Multiplication by n^alpha proves A's solution lower bound.

## B: a compact perturbation with a transverse constant velocity

Choose a regular point X1 in the first quadrant and a small box disjoint from its three reflections. Take a unit transverse vector nu to V(X1). The map

    (s,z) -> Phi_s(X1+z nu)

has nonsingular derivative at(0,0), so it is a smooth local coordinate map after shrinking the box. In its inverse coordinates,

    V dot grad s=1, V dot grad z=0.                     (6)

Choose a constant vector w with w dot grad z(X1)>0. Shrink again so w dot grad z>=b*>0 on a fixed inner flow box.

There is a compact class-P density h1 whose velocity is exactly w and whose gradient is exactly0 on this inner box. To construct it, take a smooth cutoff P0 equal on a slightly larger box to

    (w2/2)(x-x1)^2-w1(x-x1)(y-y1),

and compactly supported in the original first-quadrant box. Reflect P0 evenly in x and oddly in y, giving P. Put h1=-Delta P. In Fourier variables, or by differentiating the compact stream function P_x,

    U[h1]=(-P_xy,P_xx).                                (7)

Thus U[h1]=w and h1=-w2 on the inner box. All supports avoid0, and the compact stream function implies c[h1]=0 exactly. Its center jets also vanish. This construction verifies the required transversality rather than assuming a controllability property of the nonlocal velocity.

## Thin characteristic strips and exact strain correction

Choose eta(s) smooth and compactly supported in the flow box, equal1 on a fixed interval containing[0,tau]. Choose Psi smooth and compactly supported, equal z^2 near both0 and1. In the first box define

    k_n^0=n^(-alpha)Psi(nz)eta(s),

and reflect it with class-P parity. For large n its support stays in the fixed boxes. The C^alpha norms are uniformly bounded. By(6),

    V dot grad k_n^0=n^(-alpha)Psi(nz)eta'(s),

whose C^alpha norm is also uniformly bounded. The support has area O(1/n), its amplitude is O(n^(-alpha)), and the strain kernel is smooth there; therefore c[k_n^0]=O(n^(-alpha-1)). Use a fixed smooth class-P compensator zeta, supported inside the four outer boxes but away from all inner flow tubes and from0, with c[zeta]=1, and set

    k_n=k_n^0-c[k_n^0]zeta, h_n=h1+k_n.                  (8)

All h_n have exactly zero strain and center jets. Their supports lie in a fixed compact set disjoint from both axes. The compact velocity estimate gives

    ||U[k_n]||_infinity<=C n^(-alpha)(1+log n),
    ||U[k_n]||_C^alpha<=C.                              (9)

Here is a direct check of the first estimate. In a ball of radius1/n about any observation point, subtract the density at that point and integrate its alpha-Holder difference against the degree-minus-two kernel, obtaining C n^(-alpha). Between radii1/n and a fixed radius use the amplitude n^(-alpha), giving C n^(-alpha)log n. Outside a common support neighborhood the decay kernel gives C n^(-alpha). The local multiplier term has the same amplitude. The second estimate follows from the same near/far difference split used in proof 25, with common compact support.

Since c[h_n]=0 exactly,

    Lh_n=V dot grad h_n-h_n+U[h_n] dot grad rho.

The transport part is uniformly C^alpha bounded by(6), the fixed smooth h1 and the small compensator. Formula(9) and the globally bounded C^alpha background gradient bound the last part. Thus

    sup_n(||h_n||_C^alpha+||Lh_n||_C^alpha)<infinity.     (10)

One must use the exact cancellation of the strain term before taking this global norm. The compensator alone may have an unbounded G tail and is not separately asserted to belong to this graph domain.

On the inner box, eta=1, the compensator is zero, grad h1=0 and U[h1]=w. Therefore

    N(h_n)=n^(1-alpha)Psi'(nz)(w+U[k_n]) dot grad z.      (11)

It is exactly0 on the trajectory z=0, because Psi'(0)=0. On the trajectory z=1/n it is at least b* n^(1-alpha) for all sufficiently large n, since Psi'(1)=2 and(9) tends to0. The two trajectories have distance O(1/n), uniformly on[0,tau]. Their initial values alone prove

    ||N(h_n)||_C^alpha>=c n.                            (12)

Integrating(11) in(4) and subtracting the two trajectories proves the stronger general solution statement ||g||_X>=c_X n under(H). All constants are independent of n. This completes B, including the off-axis version with exact normalization.

## The graph norm and the fixed-point conclusion

For a precise unweighted graph formulation, let D_alpha consist of bounded class-P C^alpha functions g for which the canonical parity-normalized U[g], the scalar c[g], and the distribution Lg are defined and Lg is bounded C^alpha. Give it the norm

    ||g||_gr=||g||_C^alpha+||Lg||_C^alpha.

No completeness claim is needed for this obstruction. The inputs in(8) belong to D_alpha and satisfy(10). Any g in D_alpha with Lg=N(h_n) has graph norm at least ||N(h_n)||_C^alpha>=cn immediately by(12).

This graph norm also implies(H) on any fixed compact K. The parity-normalized velocity obeys a local C^alpha bound by the global bounded C^alpha norm, using a compact cutoff and the subtracted far kernel as in proof 25. To bound c[g], choose a fixed smooth compact test chi with integral chi G nonzero; such a test exists since G is not identically0. Pairing the equation defining L gives

    (c[g]/3) integral chi G
      =integral chi Lg+integral g div(chi V)+integral chi g
         -integral chi U[g] dot grad rho.

Every term on the right is bounded by C(||g||_C^alpha+||Lg||_C^alpha). Thus the full strain column has been accounted for, not discarded from the solution estimate.

Finally suppose one of the constructed input sequences is bounded in a norm X satisfying(H). Write a_n=||h_n||_X>0 and let H_n=h_n/a_n. Then ||H_n||_X=1. Linearity of L and quadratic homogeneity of N show that every solution of Lg=N(H_n) has norm at least the preceding lower bound divided by a_n^2. Since a_n is bounded above, those norms diverge. Therefore no finite-valued function Phi can satisfy

    ||L^(-1)N(h)||_X<=Phi(||h||_X)

for all such inputs, whenever the inverse is defined. This normalization is necessary when excluding an arbitrary Phi; bounded inputs alone only exclude bounds uniform on bounded sets. Scaling all H_n by any fixed positive epsilon gives the same obstruction in an arbitrarily small ball. Adding a fixed residual forcing does not change the conclusion if its inverse is a fixed element of X.

The result does not prove that C^alpha(h_x) is a necessary condition for every possible nonlinear method. It proves a concrete failure of the stated low-regularity perturbative maps, including the full normalization and strain functional. The stronger transport or high/low requirements of a quasilinear scheme remain separate questions.
