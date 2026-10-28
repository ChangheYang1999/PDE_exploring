# Residual membership in the global axis-jet target

## Exact spaces and statement

Let a=17/4 and eta=5/4. Put t=log r, C(theta)=cos(theta)^2 sin(theta), and

 w(X)=|x|^(-2a) for r<1,
 w(X)=|cos(theta)|^(-2a) r^(-eta) for r>=1.

All functions have the IPM parity: even in x and odd in y. Let R=L2(w dX). Let G be the scalar Hilbert space with norm

 ||gamma||_G^2=integral_{t<0}|gamma(t)|^2 exp((8-2a)t)dt
                   +integral_{t>=0}|gamma(t)|^2 exp((8-eta)t)dt.

Define E gamma=x^2 y gamma(log r) and Y=E G direct-sum R, with the sum of the two squared norms. The sum is algebraically direct: for nonzero gamma the angular integral of |E gamma|^2 w diverges near cos(theta)=0 because 4-2a<-1. The elements are locally integrable functions, so this also defines a concrete distributional target. The axis coefficient of E gamma is y gamma(log|y|).

Let rho0 be the exactly joined, exactly normalized modal trial verified in V005, with ell0=1/k. Its exact finite angular and radial formulas imply

 rho0=x^2 y(1+O(r^2)) at0,
 rho0=r^k Theta(theta)+O(r^(2k-1)) at infinity,

with differentiated modal estimates as specified below. Define F_ell(rho)=(ell X+U[rho]).grad rho-rho. Then

 F_ell0(rho0) belongs to Y.                                  (1)

More strongly, its remainder after the axis subtraction belongs to the space with up to five conormal derivatives x partial_x and y partial_y in R, and its scalar jet has up to five t derivatives in G. This is a qualitative membership theorem. It does not give a certified numerical residual norm, a global inverse, or a nonlinear correction theorem.

For a smooth radial cutoff chi supported in r>=1 and equal to1 eventually, put

 rho_ell=rho0+chi(r)(r^q-r^k)Theta(theta), q=1/ell,
 nu(ell,0)=3ell-1-c[rho_ell],
 H0=chi0(r) X.grad rho0/3,

where chi0 is smooth, compactly supported, and equal to1 near0. If ell varies in a compact interval in (1,infinity) with max(q,k)<eta/4=5/16, then

 F_ell(rho_ell)-nu(ell,0)H0 belongs to Y.                      (2)

This family is smooth in ell as a Y-valued family, also in the conormal target just described. Derivatives in ell introduce powers of log r and remain in the target because the exponent inequality is strict.

For an additional smooth correction h with cubic coefficient J(h), the exact cubic coefficient of F_ell(rho_ell+h) is

 (1+J(h))nu(ell,h),    nu(ell,h)=3ell-1-c[rho_ell]-c[h].       (3)

Consequently the augmented residual on a domain retaining a free J coordinate must use

 (F_ell(rho_ell+h)-(1+J(h))nu(ell,h)H0, nu(ell,h)).            (4)

Formula (4) removes the forbidden cubic coefficient. It does not by itself prove membership for arbitrary h in an unspecified high or low correction space. The simpler subtraction nu H0 from V038 is correct under that proof's explicit assumption J(h)=0. Both versions have the same derivative at (ell0,0).

## Factorization and exact axis subtraction

Write rho=x^2 y A(X), where A is even in both coordinates on every punctured annulus. The exact finite Fourier representation makes this a smooth factorization there. Parity and the canonical velocity give

 V1=x v1(X), V2=y v2(X),

with v1,v2 smooth and even on those annuli. Direct differentiation yields

 F_ell(rho)=x^2 y B(X),
 B=v1(2A+x A_x)+v2(A+y A_y)-A.                              (5)

For any such factor B let gamma(t)=B(e^t,pi/2) and put

 F_R=x^2 y[B(r,theta)-B(r,pi/2)].                            (6)

The function B is even in x, so its first angular derivative vanishes on the vertical axis. Taylor's theorem in theta, and a bound on the second angular derivative, imply

 |B(r,theta)-B(r,pi/2)|<=C(r) cos(theta)^2                  (7)

uniformly on the circle. Away from the vertical axis this follows by enlarging the constant; near the negative vertical axis it follows from even y parity of B. Thus the remainder has the stronger angular factor cos^4(theta)sin(theta).

Its weighted angular integral is finite:

 integral_0^{2pi}|cos(theta)|^(8-2a) sin(theta)^2 dtheta<infinity

because a<9/2. No pointwise trace is being extracted from an arbitrary member of R. We extract the trace from the explicit smooth modal residual before completing the target space.

## The exact modal estimates at the two ends

Near0 the density formula is a finite sum of x^2 y, terms r^(3+2j) times smooth finite angular functions for j>=1, and terms r^(3+bi) times logarithmic polynomials, with bi>50. The canonical modal Green formula gives

 U[rho0]=c[rho0](-x,y)+U3(X)+O(r^5(1+|log r|)),

where U3 is a homogeneous cubic polynomial vector field. Possible degree5 resonances introduce only the indicated higher-order logarithm. These claims follow by solving each radial Euler equation: a density power r^d produces a velocity power r^d, with a logarithm only at an angular resonance, and the smooth inner homogeneous solutions are harmonic polynomial velocities of odd degrees1,3,5,... . The density x^2 y has no degree3 resonance: its x derivative has angular frequency2, whereas a resonant stream function of degree4 would have frequency4. The parity forbids even-degree homogeneous velocities.

All fixed finite t and angular derivatives of the displayed remainders obey the corresponding bounds. In particular v1=-A0+O(r^2), v2=D0+O(r^2), where A0=2ell0-1 and D0=4ell0-1. The density factor A=1+O(r^2). Formula (5) has constant term

 -2A0+D0-1=0.

It follows that B=O(r^2), with each of its fixed t and angular derivatives O(r^2). The higher-order logarithmic terms are harmless: r^4 |log r| is bounded by a constant times r^2 near0. Formula (7) therefore gives

 |gamma(t)|<=C r^2,    |F_R|<=C r^5 |cos(theta)|^4|sin(theta)|. (8)

At infinity the exact trial has a leading density r^k Theta and a finite expansion of lower powers beginning at r^(2k-1), together with faster decaying logarithmic-polynomial terms. The leading drift cancels because ell0 k=1. The canonical velocity is O(r^k), so the first possible nonlinear residual is O(r^(2k-1)). Finite angular factorization in (5) then gives

 B=O(r^(2k-4)),
 |gamma(t)|<=C r^(2k-4),
 |F_R|<=C r^(2k-1)|cos(theta)|^4|sin(theta)|.                 (9)

The same bounds hold with fixed t and angular derivatives. The exact joins of rho0 are C6; its Green velocity is at least C6 across these radial circles. F therefore has the five radial derivatives used in the statement. There are only finitely many joins, all on compact annuli, and all angular derivatives remain finite Fourier sums. No C5 regularity of rho0 at the origin is asserted or needed.

## Integrability and conormal derivatives

Near0, the squared jet norm from (8) is bounded by a multiple of

 integral_{-infinity}^0 exp((12-2a)t)dt,

which is finite since a<6. The squared remainder norm has exactly the same radial exponent and the finite angular integral above.

At infinity, the squared jet and remainder radial integrals from (9) are bounded by

 integral_0^infinity exp((4k-eta)t)dt,

which is finite because k<eta/4. These arguments prove (1). All compact radial annuli contribute finite norms by (7).

The conormal fields are

 x partial_x=cos(theta)^2 partial_t-sin(theta)cos(theta)partial_theta,
 y partial_y=sin(theta)^2 partial_t+sin(theta)cos(theta)partial_theta.

They preserve the factor cos(theta)^4 sin(theta) up to smooth angular multiples. Thus repeated application does not destroy the weighted angular integrability. Their radial coefficients are bounded. Applying the differentiated modal estimates proves the conormal assertion up to order5. Ordinary angular differentiation alone would not preserve this weight; it is not claimed.

## Parameter family and the cubic correction

For rho_ell the density remains exactly rho0 near0. Only its canonical velocity and the explicit drift change there. Its linear velocity is c[rho_ell](-x,y), so formula (5) has constant term nu(ell,0). The factor H0/(x^2 y) is 1+O(r^2), with the same differentiated estimates. Subtracting nu(ell,0)H0 leaves the bounds (8).

At infinity rho_ell=r^q Theta+R, where R=O(r^(2k-1)). The leading drift cancels because ell q=1. The remaining residual is O(r^(2max(q,k)-1)); the exact nonzero highest angular interaction was checked in V038. Dividing by x^2 y and applying (7) gives the analogue of (9), with k replaced by max(q,k). On a compact parameter interval satisfying max(q,k)<eta/4 there is a uniform positive exponent gap. Parameter derivatives introduce only finitely many logarithmic factors at each derivative order, so dominated convergence proves (2) and its smooth parameter dependence. The finite angular Green formulas justify differentiation of the velocity with respect to ell; the leading exponent q remains separated from all resonance values on such a compact interval.

Finally, if rho_ell+h has cubic coefficient 1+J(h), its density derivatives at leading order are those of (1+J)x^2 y, and its linear velocity is c[rho_ell+h](-x,y). This gives exactly (3). Since H0 has cubic coefficient1, formula (4) removes it. If one instead subtracts only nu H0 while retaining J, the residual has coefficient J nu. Unless J nu=0, it is not in Y: the only possible scalar jet tends to that nonzero constant at -infinity, and exp((8-2a)t) is not integrable there. This is a concrete target-membership failure, regardless of how small J and nu are.

At the base point J=nu=0, the extra product J nu has zero derivative. Hence the verified linear bordering formulas of V034 and V038 remain unchanged. This repair affects the nonlinear augmented map only.

## Dependencies and outstanding quantities

Dependencies are the exact modal definition and joins of V005, the operator and velocity conventions of V002, the actual origin regularity analysis V036, and the tail cancellation of V038. The space G is equivalent to the coefficient-adapted scalar target of V041 if the axis-rate hypotheses there hold. Positivity of that rate is not needed for the membership proof here.

No residual norm is certified by this argument. Quantitative bounds for the radial coefficient integrals and the two angular factors are still required for an a posteriori theorem. The target is now fully specified, but boundedness of the full operator on a compatible correction domain and a global inverse remain OPEN.
