# Sharp Hölder control of the compactified inverse constant

Status: CONFIRMED by independent complete proof, exact and high-precision controls, and actual Opus5.5 review324 of the critical argument. Calls323/325 gave no written audit; see the adjudication.

The stored parameter and the constant term of its inverse measure different features of a field. Here we identify a norm that controls that constant and prove that its Hölder threshold is sharp. We also give an explicit error bound for quintic splines, with its dependence on the final cell width.

## Statement and notation

Fix a noninteger number b>2 and a scale L>0. Set N=floor(b), m=N-1 and gamma=b-N, so m>=1 and 0<gamma<1. For a function P on [0,1], let p_j=P^(j)(0)/j!. For smooth P define

    J_b(P) = sum_(j=0)^m p_j/(j+1-b)
             + integral_0^1 z^(-b)[P(z)-sum_(j=0)^m p_j z^j] dz.       (1)

This integral converges for smooth P. It is the finite part of integral z^(-b)P(z) dz obtained by subtracting those m+1 Taylor divergences. For the radial compactification

    z=(L²/(L²+r²))^(1/(2b)),
    q(r)=r z^(b+1)P(z),
    Omega(r,theta)=q(r) cos(theta),                                  (2)

the constant term of the canonical relative whole-plane velocity, after its N homogeneous tail velocities, is

    C=(0,C2),     C2=-(b L²/2) J_b(P).                               (3)

Here x=r cos(theta), Omega=-Delta Psi and U=(-Psi_y,Psi_x). Formula (3) uses the prescribed full-plane relative inverse U-U(0). It does not add a uniform velocity or another harmonic field. The basis exponent b need not be the PDE exponent beta of a stored forced state.

For 0<alpha<=1 use the norm

    ||P||_(m,alpha) = sum_(j=0)^m ||P^(j)||_infinity + [P^(m)]_alpha,
    [f]_alpha = sup_(z!=w) |f(z)-f(w)|/|z-w|^alpha.

At alpha=0 use ||P||_(m)=sum_(j=0)^m ||P^(j)||_infinity instead.

The following assertions hold.

1. If gamma<alpha<=1, (1) is defined for every P in C^(m,alpha)[0,1], and

       |J_b(P)| <= sum_(j=0)^m ||P^(j)||_infinity/[j! |j+1-b|]
                    + [P^(m)]_alpha /
                      [(alpha-gamma) product_(j=1)^m(alpha+j)].       (4)

   In particular (3) is bounded in this norm. No uniform estimate as alpha decreases to gamma or b approaches an integer is asserted.

2. For every 0<=alpha<=gamma there are smooth functions P_n compactly supported in (0,1), with all endpoint jets zero and support tending to z=0, such that their C^(m,alpha) norms tend to zero and J_b(P_n)=1. For alpha=0 this means the C^m norm. Consequently no bounded linear extension of J_b from smooth functions to those weaker spaces exists.

3. In the construction in item 2, the vorticities and their canonical relative velocities vanish on disks whose radii tend to infinity. They change C2 by exactly -bL²/2, without changing any relative center jet, center strain, thermal normalization or asymptotic vorticity coefficient. The ordinary absolutely convergent center velocity of the added compact source changes by (0,bL²/2); it is not being preserved. Multiplication by a fixed scalar gives any prescribed change in C2. Keeping a background temperature unchanged preserves its thermal center normalization and both B2 equations on those disks, but need not preserve either equation outside them.

4. For 3<b<4, write gamma=b-3. Suppose P is globally C² on [0,1] and is a polynomial of degree at most five on [0,delta], where 0<delta<=1. Let M=||P''||_infinity. Then J_b(P) is defined and

       |J_b(P)| <= sum_(j=0)^2 ||P^(j)||_infinity/[j! |j+1-b|]
            + M {17 delta^(-gamma)/[3(1-gamma)]
                         + [delta^(-gamma)-1]/gamma}.                (5)

   Thus the norm of this functional on quintic splines with last compactified cell width delta is at most a constant times delta^(-gamma), when the source norm is C². On uniform meshes this power is sharp. This is a bound for represented functions, not a uniform bound on numerical errors that have not been measured.

## The inverse formula and the sufficient norm

The exact change of variables in (2) gives

    q(r) |dr/dz| = b L² z^(-b) P(z).                                 (6)

The first N source powers are A_j r^[-(j+1)/b], where A_j=L^[1+(j+1)/b]p_j, for 0<=j<=m. They have exponent strictly below 1. Subtracting them globally leaves a source whose center-velocity integral is absolutely convergent: at zero each subtracted term is integrable in dr, and at infinity the smooth remainder is O(r^[-(N+1)/b]), up to still faster compactification corrections. The center value of the first cosine inverse is one half its radial integral. Hence the velocity constant is

    C2 = -1/2 integral_0^infinity
                 [q(r)-sum_(j=0)^m A_j r^[-(j+1)/b]] dr.             (7)

With r=L sqrt(epsilon^(-2b)-1), the integral of the jth subtracted power from zero to r is

    b L² p_j epsilon^(j+1-b)/(b-j-1)
                 (1-epsilon^(2b))^[(b-j-1)/(2b)].

Replacing the last factor by 1 changes this expression by O(epsilon^(j+1+b)), which tends to zero. The limit in (7) is therefore -bL²/2 times (1). This rederives the sign and finite-part convention of packet 111. At the integer values of b a logarithm replaces one of these subtractions, and the present formula is not asserted there.

For P in C^(m,alpha), repeated integration of P^(m)(t)-P^(m)(0) gives the exact Taylor remainder

    P(z)-sum_(j=0)^m p_j z^j
      = 1/(m-1)! integral_0^z (z-t)^(m-1)
                                [P^(m)(t)-P^(m)(0)] dt.              (8)

Its absolute value is at most

    [P^(m)]_alpha z^(m+alpha) / product_(j=1)^m(alpha+j).              (9)

To obtain the coefficient, substitute t=zu in (8) and integrate the beta integral by parts m-1 times. The remaining integral is 1/(alpha+1), giving the stated product without any regularity assumption on derivatives above m. Since m+alpha-b=alpha-gamma-1, the weighted integral of (9) converges exactly when alpha>gamma and yields (4). The same bound gives an integrable radial remainder in (7): its exponent is (N+alpha)/b>1. Formula (1) thus defines the claimed bounded map on the whole Hölder space directly; no density or uniqueness assertion about extensions from smooth functions is needed.

## Failure below the threshold

Choose a nonzero nonnegative smooth function phi supported in (1,2), and let

    I = integral_1^2 w^(-b) phi(w) dw > 0,
    P_h(z) = h^(b-1) phi(z/h)/I,        0<h<1/3.                      (10)

All endpoint jets of P_h vanish. Substituting z=hw gives J_b(P_h)=1 exactly. The jth derivative has supremum at most C_j h^(b-1-j), and

    [P_h^(m)]_alpha <= C h^(b-1-m-alpha)
                       = C h^(gamma-alpha).                        (11)

Here phi and all its derivatives are extended by zero, so the Hölder estimate is global, including points on opposite sides of its support. These norms tend to zero for alpha<gamma; the derivative suprema also give the alpha=0 case. The support is contained in [h,2h] and tends to zero.

## Failure at the critical Hölder exponent

A single annulus in (10) has a fixed critical seminorm. A growing logarithmic interval supplies the critical counterexample while its entire support still moves to z=0.

Choose smooth cutoffs chi and eta on [0,infinity), with values in [0,1], such that chi(w)=0 for w<=1, chi(w)=1 for w>=2, eta(w)=1 for w<=1/2 and eta(w)=0 for w>=3/4. They may be made from the normalized positive bump of packet 180. Let p=m+gamma=b-1, delta_h=sqrt(h), and for 0<h<1/16 put

    F_h(z)=z^p chi(z/h) eta(z/delta_h).                              (12)

This is smooth on [0,1], zero near both endpoints, and supported where h<=z<=3delta_h/4. To bound its critical norm, define on the nonnegative half-line

    f(w)=w^p eta(w),      g(w)=w^p[1-chi(w)].

Both f and g are compactly supported C^(m,gamma) functions. Indeed the only nonsmooth model at zero after m derivatives is a constant times w^gamma, and

    |a^gamma-b^gamma| <= |a-b|^gamma   for a,b>=0.

This inequality follows from (b+d)^gamma<=b^gamma+d^gamma, whose derivative in b is nonpositive after subtracting b^gamma. Multiplication by the smooth compact cutoffs preserves the Hölder bound by the product difference identity. Away from zero the functions are smooth.

Since 2h<delta_h/2, eta(z/delta_h)=1 on the support of 1-chi(z/h). Therefore

    F_h(z)=delta_h^p f(z/delta_h)-h^p g(z/h).                         (13)

For a fixed C^(m,gamma) function a, the mth Hölder seminorm of rho^p a(z/rho) is independent of rho, because p=m+gamma. Its jth derivative supremum is O(rho^(p-j)) for j<=m. Formula (13) thus gives a uniform C^(m,gamma) bound for F_h. The auxiliary f and g need not be smooth at zero; their exact difference (12) is zero near zero and is smooth there.

All Taylor subtractions of F_h vanish. Splitting its weighted integral at 2h and delta_h/2 gives

    J_b(F_h)=integral_0^1 chi(z/h) eta(z/delta_h) dz/z
            = log(delta_h/h)+c_cut
            = (1/2)log(1/h)+c_cut,                                  (14)

where the fixed finite number

    c_cut = -log 4 + integral_1^2 chi(w) dw/w
                      + integral_(1/2)^(3/4) eta(w) dw/w

does not depend on h. The transition supports do not overlap under h<1/16, so (14) is an exact identity. The integral is strictly positive, since both cutoffs equal 1 between 2h and delta_h/2. Set

    P_h=F_h/J_b(F_h).                                                (15)

Then J_b(P_h)=1 while ||P_h||_(m,gamma) tends to zero. Its support still tends to z=0. This proves the critical case, including failure of boundedness on smooth test functions with every endpoint jet fixed to zero.

## Local invisibility under the relative inverse

For each function constructed above, the source (2) is smooth and supported in a finite physical annulus. Its inner radius tends to infinity because the largest z in its support tends to zero. The ordinary first cosine stream function is

    Psi_abs(r,theta)=1/2 [r^(-1) integral_0^r s²q(s) ds
                             +r integral_r^infinity q(s) ds]
                                    cos(theta).                     (16)

Direct differentiation gives -Delta Psi_abs=q(r)cos(theta). Inside the source's inner radius, (16) equals x times (1/2) integral q(s)ds, so its velocity is constant and equals its center velocity. Subtracting that actual center value makes the relative velocity identically zero on the whole inner disk. Outside the outer source radius, the ordinary velocity decays like r^(-2), and the relative velocity tends to -(0,(1/2)integral q). By (6) this limit is (0,-bL²/2), exactly (3) for J_b(P_h)=1. All homogeneous vorticity coefficients are zero for each such compact source.

The ordinary center velocity of the compact added source is (0,bL²/2). Thus a background whose absolute center-velocity integral converges acquires exactly this change in v0. If that absolute integral is not defined, only the canonical relative statements are made. No claim of an unchanged physical moving-center drift is intended.

Adding these sources to a smooth background changes no vorticity or relative velocity on the inner disk. Keeping its temperature unchanged consequently changes no center coefficients, normalization or equation on that disk. The support eventually lies beyond each fixed disk. No equation outside the disk is asserted, and no B2 solution is constructed. This is the relative inverse dictated by the source; the outer constant is a consequence of subtraction at the center.

## The quintic bound and its sharp cell dependence

Assume 3<b<4 and the hypotheses of item 4. Write Q=P'' on [0,delta], a polynomial of degree at most three. Interpolate Q(delta t) at t=0,1/3,2/3,1. If ell_i are the four Lagrange basis polynomials, their derivatives in the quadratic Bernstein basis ((1-t)^2,2t(1-t),t²) have columns

    (-11/2, 9, -9/2, 1),
    (  7/2,-27/2,27/2,-7/2),
    (   -1, 9/2, -9,11/2).

The sums of absolute coefficients in these columns are 20,34,20. Positivity and sum one of the Bernstein basis imply

    ||P'''||_infinity,[0,delta] <= 34 M/delta.                        (17)

This is an explicit interpolation bound; no unproved spline inverse inequality is needed. By (8), with m=2, the remainder is bounded by (17/3) M z³/delta for 0<=z<=delta. On all of [0,1], the bound |P''(t)-P''(0)|<=2M instead gives remainder at most M z². Splitting the integral of z^(-b) times this remainder at delta yields

    (17 M/(3delta)) integral_0^delta z^(3-b) dz
             + M integral_delta^1 z^(2-b) dz
      = M {17 delta^(-gamma)/[3(1-gamma)]
                            + [delta^(-gamma)-1]/gamma}.

Adding the Taylor terms proves (5). This also proves convergence of (1) for this C² class; the polynomial first cell supplies the extra local regularity it needs.

For sharpness take delta=1/n with n>7, and let B be the nonnegative cardinal quintic B-spline supported in [0,6], normalized as the sixfold convolution of the indicator of [0,1]. It is piecewise polynomial of degree five, globally C4, positive in (0,6), and has knots at the integers. These properties follow by successive integration of piecewise polynomials; explicitly

    B(w)=1/120 sum_(k=0)^6 (-1)^k binom(6,k) (w-k)_+^5.

The cancellation for w>=6 is the sixth finite difference of a degree-five polynomial. Put P_delta(z)=delta² B(z/delta-1). It is a quintic spline on the uniform mesh, identically zero on its first cell [0,delta] and near 1. Its C² norm is uniformly bounded, while

    J_b(P_delta)=delta^(3-b) integral_1^7 w^(-b) B(w-1) dw
                  = c_b delta^(-gamma),       c_b>0.                 (18)

Thus no uniform bound with a smaller power of delta can hold for this spline class. The lower-bound functions are C4 splines, which is the class in item 4; they are not being asserted to be globally smooth B2 vorticities. The smooth counterexamples of items 2 and 3 were constructed separately.

## Scope and dependencies

For 3<b<4 the sharp sufficient source topology is C^(2,alpha) with alpha>b-3. Endpoint jets, a small C² difference, or agreement in a finitely sampled scalar parameter do not by themselves supply this control. Formula (5) supplies a finite-mesh error estimate if an actual global C² error and the final cell width are known. Neither a small error nor a convergent sequence has been inferred for the team's fields.

The inverse convention is independently rederived from packet 111. The local-invisibility conclusion strengthens the topology discussion of packet 109 by identifying the exact compactified Hölder threshold; it does not invalidate any exact stored-field certificate. Packet 180 supplies only one possible explicit smooth cutoff. No external regularity theorem or numerical result is used in the proof. Formal sources and reproducible controls are recorded alongside this file; no proof-assistant verification is claimed.

Written UTC 2026-10-21T15:56:58.323700+00:00, before new controls.

Independent audit completed UTC 2026-10-21T16:08:33.571059+00:00.
