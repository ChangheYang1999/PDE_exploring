# Finite angular expansions cannot solve the full sublinear IPM profile equation

Result 93. Written 2026-10-20T23:58:38Z; actual timestamps are in verification/.
Status: independent informal proof; 315 exact rational checks PASS. Lead review pending.

## Statement and scope

Let rho be a real C^1 function on R^2, even in x and odd in y. Assume that for some finite odd integer m >= 1,

    rho(r,theta) = sum_{1 <= j <= m, j odd} b_j(r) sin(j theta),

and that, for some 0 < gamma < 1,

    |rho(X)| + (1+|X|)|grad rho(X)| <= C(1+|X|)^gamma.

Let U be its canonical full-plane velocity: div U = 0, curl U = -rho_x, with the IPM parities and U(X) = o(|X|) at infinity. Suppose the classical transport identity

    (ell X + U) . grad rho = c_rho rho

holds, where ell and c_rho are any real constants. Then rho is identically zero.

In particular, no profile in the primary class, or its C^1 variant with the same growth and velocity law, has a finite angular expansion. The theorem makes no sign assumption and does not assume that the radial coefficients are analytic. It does not exclude infinite angular expansions. It does not give a positive quantitative lower bound for the residual of a sequence with increasing angular degree. It is not the principal NO endpoint.

## Canonical highest stream mode

Suppose rho is nonzero and choose m as its largest nonzero angular index. Put b = b_m. For r > 0, b is C^1, b(r) = O(r) at zero and b(r) = O(r^gamma) at infinity. The first bound follows from rho(0) = 0 and the C^1 bound on a disk. All sine coefficients here use the normalization b_j = pi^{-1} integral_0^{2pi} rho sin(j theta) dtheta.

The polar identity d_x = cos(theta) d_r - sin(theta) r^{-1} d_theta gives the highest mode of rho_x as

    (1/2)(b' - m b/r) sin((m+1) theta).

Define

    J(r) = integral_0^r s^{m+1} b(s) ds,
    P(r) = -J(r)/(2 r^{m+1}).                              (1)

Direct differentiation, using J' = r^{m+1}b, proves

    -(P'' + P'/r - (m+1)^2 P/r^2) = (b' - m b/r)/2.

Thus P is the coefficient of sin((m+1) theta) in the canonical stream function. Here is the boundary justification, including the harmonic freedom. The bound at zero gives J = O(r^{m+3}), P = O(r^2), P' = O(r); the bound at infinity gives J = O(r^{m+gamma+2}), P = O(r^{gamma+1}), P' = O(r^gamma). The other two solutions of the homogeneous modal equation are r^{m+1} and r^{-m-1}. The singular one is excluded at zero. The growing one has velocity of order r^m, which violates U = o(r), also when m = 1. Consequently (1) is the unique allowed highest coefficient.

For completeness, no stream mode above m+1 can occur. Such a mode has zero Poisson source. Its two homogeneous radial solutions are ruled out by the same regularity and growth argument. Oddness of the stream in both axes permits only the positive even sine modes; the zero mode and an additive constant do not affect U. These statements can also be read mode by mode from the distributional equation. There is no point source at zero for (1): P and its first radial derivative have the displayed vanishing bounds. The canonical velocity is locally continuous; the excluded homogeneous modes cannot be hidden by other modes because Fourier projection preserves the bounds. No exterior harmonic strain is added.

## The highest transport harmonic

In polar coordinates the top stream mode gives

    U_r = -(m+1)P cos((m+1)theta)/r,
    U_theta = P' sin((m+1)theta).

The linear transport terms ell r rho_r - c_rho rho have angular degree at most m. Products of a density mode j <= m and a stream mode k <= m+1 have degree at most j+k. The only product that can produce angular degree 2m+1 is the pair j=m, k=m+1. Product-to-sum therefore gives the sine coefficient of the full residual at degree 2m+1 as

    [m b P' - (m+1)P b']/(2r).                            (2)

Since the full residual vanishes, (2) is zero for every r > 0. Substitution of (1) and b=J'/r^{m+1} gives

    (m+1) J J'' - m (J')^2 - (m+1) J J'/r = 0.            (3)

In fact (2) is the left-hand side of (3), divided by 4 r^{2m+3}. Neither ell nor c_rho appears. Lower density and stream modes cannot cancel this harmonic.

## Zeros of J and the global contradiction

The function J is C^2 on (0,infinity), continuous at zero, and J(0)=0. Consider any connected component I=(a,d) of the open set {r>0:J(r) != 0}. On I its sign is constant. Set Z = |J|^{1/(m+1)}, a positive C^2 function there. Direct substitution in (3) gives

    (m+1)^2 Z^{2m+1} (Z'' - Z'/r) = 0.

Hence Z'' - Z'/r = 0, and integration gives

    Z(r) = A r^2 + B on I.                               (4)

At a finite endpoint of I, J tends to zero by continuity and maximality of the component. This also holds at a=0 by J(0)=0. Therefore Z tends to zero at its left endpoint in every case. A nonzero affine function of r^2 can have at most one root for r >= 0. It cannot vanish at both endpoints of a bounded nonempty component. Thus d=infinity.

On (a,infinity), positivity of (4) forces A >= 0. If A=0, then Z is a positive constant and cannot tend to zero at the finite left endpoint a. Thus A>0. It follows that

    |J(r)| / r^{2m+2} -> A^{m+1} > 0 as r -> infinity.    (5)

On the other hand b(r)=O(r^gamma) gives J(r)=O(r^{m+gamma+2}), so

    |J(r)| / r^{2m+2} = O(r^{gamma-m}) -> 0,

because gamma < 1 <= m. This contradicts (5). There is no nonempty component, so J=0 and b=0, contrary to the definition of the highest nonzero mode. Hence rho=0.

The component argument explicitly handles sign changes, arbitrary zero sets, and flat zeros of J. It does not divide by J across a zero or invoke uniqueness for a singular equation there.

## Dependencies and verification

The proof uses only Fourier projection, elementary polar differentiation, the classical or distributional Poisson equation with the canonical boundary behavior, and the elementary ODE on each nonzero component. It does not use the projected one-sided Mellin identities, result90, or the radial argument of result91.

The companion checker independently expands the angular products with exact rational arithmetic, checks (2)-(3) at arbitrary rational jets, verifies the Z substitution and explicit local solutions, and records source hashes. These checks support the algebra; the endpoint and component arguments are the written proof and require independent human/model review. No Lean build is requested or run.
