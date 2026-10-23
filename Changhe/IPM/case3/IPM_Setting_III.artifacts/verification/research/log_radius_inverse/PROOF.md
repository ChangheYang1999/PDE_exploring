# A logarithmic-radius formula for the infinite exterior inverse

Date: 2026-10-20. Status: exact algebraic identity; implementation checks are recorded separately in verification/. This result concerns evaluation of the canonical inverse, not existence of an IPM profile.

## 1. Hypotheses and statement

Let rho be a smooth centrally odd density on the plane. Assume |rho(X)| <= C(1+|X|)^p, 0<p<1, and the usual local differentiability needed for the principal-value integral. Put eta=1-p. The canonical Darcy velocity is

    U(X) = PV integral K(X-Y) rho(Y) dY - (0,rho(X)/2),
    K(Z) = (-Z1 Z2/pi, (Z1^2-Z2^2)/(2 pi))/|Z|^4.

The integral at infinity uses concentric disks. Fix a nonzero query X=m n, where m=|X| and |n|=1, and an exterior radius R0>m. Write e(theta)=(cos theta,sin theta) and

    h(s,theta)=exp(-p s) rho(exp(s)e(theta)).

For any alpha>0, set beta=alpha eta-1>-1. The contribution from |Y|>R0 equals

    alpha m R0^(-eta) integral_0^1 t^beta integral_0^(2 pi)
       h(log R0-alpha log t,theta)
       H((m/R0)t^alpha,n,e(theta)) dtheta dt,                 (1)

where H extends continuously to its first argument equal to zero and is given below. Thus no exterior radius exp(s) or unscaled exterior density need be formed. Formula (1) is exact, with no finite-radius truncation.

## 2. Factoring the cancelled kernel

Write tau=m/R, d=n.e and

    v=tau-2d, q=1+tau v, j=v(2+tau v).

Because R>m, q=|tau n-e|^2>0. Direct substitution in K gives

    H1 = -[tau n1 n2-n1 e2-n2 e1-e1 e2 j]/(pi q^2),
    H2 = [tau(n1^2-n2^2)-2n1 e1+2n2 e2
                         -(e1^2-e2^2)j]/(2 pi q^2).         (2)

Indeed, the common denominator of K(tau n-e)-K(-e) is q^2. The difference q^2-1 is tau j. After subtracting the two numerators, each remaining term has a factor tau, and its quotient is exactly (2). Consequently

    K(tau n-e)-K(-e)=tau H(tau,n,e).                          (3)

Equation (2) remains finite at tau=0. It therefore evaluates the quotient without subtracting close numbers or dividing by a possibly underflowed tau.

## 3. Derivation and convergence of the exterior formula

For every R, the angular integral of K(-e)rho(Re) is zero: K is even in e, while rho is centrally odd. In polar coordinates the exterior is therefore

    integral_R0^infinity integral [K(X/R-e)-K(-e)]rho(Re) dtheta dR/R.

Use (3), rho(Re)=R^p h(log R,theta), and R=R0 t^(-alpha). The factors become

    (alpha/t) (m/R) R^p = alpha m R0^(-eta) t^(alpha eta-1),

which proves (1). The function H is bounded for 0<=tau<=m/R0<1. The growth assumption bounds h for R>=R0. Since beta>-1, the transformed integral is absolutely convergent. These bounds justify both the subtraction and the change of variables. At X=0 the exterior is exactly zero by central oddness. The principal-value near-field and the contact term are unchanged by this derivation.

## 4. Scaled evaluation for the finite Q representation

For kappa>1 and L>0, the Q radial coordinates are sigma in [0,1], z=2(1-sigma), t_Q=1-z, and

    r=L sqrt(sigma)/z^kappa,
    rho(r,theta)=r z/2 sin(theta) F(sigma,theta),
    F=sum_(k=0)^(M-1) sigma^k B_k(t_Q) cos(2k theta).

Each B_k is a finite polynomial. Here eta=1/kappa and p=1-eta. The map gives r^eta z=L^eta sigma^(eta/2), hence

    h(log r,theta)=L^eta/2 sigma^(eta/2) sin(theta) F.         (4)

To determine sigma from s=log r, solve either

    log sigma-2 kappa log(1-sigma)
                      =2(s-log L)+2 kappa log 2,

on sigma<=1/2, or

    kappa log z-(1/2)log(1-z/2)=-(s-log L),

on z<=1. Both left sides are strictly increasing on the indicated positive intervals, so the coordinate is unique and a bracketed scalar solve suffices. Formula (4) avoids both a large r and the product of a small z with a large r. For a finite Q representation the scaled h is bounded, so the preceding convergence proof applies.

## 5. Finite-query geometric scaling

Two elementary rewrites also avoid unnecessary overflow in the existing near/interior quadrature. Write S=max(length,|X|), C=outer_factor and d=(X/S).e. The distance along a ray from X to the outer circle of radius CS is

    s_max=S[-d+sqrt(d^2+C^2-(|X|/S)^2)].

This follows by solving |X+s e|^2=C^2 S^2 and factoring S^2 before the square root. All squared quantities inside the root are bounded. In an origin-centered core panel a<=r<=b, the kernel factor |X|^-2 can be multiplied into its area weight first:

    (b-a) w r / |X|^2 = [(b-a)/|X|] w [r/|X|].

The implemented core lies in r<=|X|/2, so these geometric ratios stay bounded. This changes only multiplication order and prevents the intermediate product r^2 rho from overflowing when the final integrand is representable. Finite query coordinates, density values, final velocities, and the prefactors must still fit in floating point.

## 6. Scope of numerical verification

The implementation uses the same independently written real-space near-field quadrature as the earlier direct inverse, and changes only the exact infinite exterior representation. Tests must compare the two formulas where ordinary radii are representable, check (2) against high precision algebra at very small tau, and compare velocities for smooth manufactured sublinear densities at kappa values for which direct exterior radii overflow.

An algebraic identity does not certify finite quadrature error. Convergence still requires radial and angular refinement. The geometric rewrites remove squares of large query radii, but do not remove overflow in center Taylor coefficients, Cartesian density derivatives, or genuinely unrepresentable final values. Very large finite query radii must still be selected within the arithmetic range of those operations. The code never replaces a divergent floating-point radius by a finite cutoff.
