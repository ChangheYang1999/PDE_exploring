# A deflated center equation does not enforce a nonzero density slope

Date: 2026-10-20. Status: independently reconstructed explicit counterexample to a numerical safeguard, with separate canonical inverse checks completed. The3ell x3quadrature independent canonical inverse and residual checks passed at2026-10-20T18:07:06.596378Z, with center errors below2.3e-14. This is a smooth canonical non-profile. It is not an existence claim for either branch.

## 1. Statement and conventions

Fix ell>1, kappa=ell/(ell-1)>1, L>0 and G nonzero. Write D=ell-1 and A=2ell-1. Define sigma(r) in [0,1) by

    r = L sqrt(sigma) / [2(1-sigma)]^kappa,
    sigma(0)=0, w=1-sigma.

Equivalently t=2sigma-1 is the numerical compactification variable and r=L sqrt((1+t)/2)/(1-t)^kappa. Put

    v = -8D/(1+2kappa), u=v+G,
    rho(x,y)=y w(r) sigma(r) [u+v cos(2theta)].             (1)

At r=0 the formula is interpreted by smooth extension. Let U be the canonical full-plane IPM inverse, with div U=0, curl U=-rho_x and U=o(r), and let c=partial_x partial_y psi(0)=partial_y U_2(0).

This field is C-infinity at every finite point, is even in x and odd in y, obeys the strict sublinear growth and gradient bounds with exponent p=1-1/kappa=1/ell, and has a nonzero cubic density on the vertical axis. Nevertheless

    a0=rho_y(0)=0, c=1-ell, gK=G nonzero.                 (2)

Here gK is the endpoint gauge sum in the Q representation. Consequently the proposed replacement center row

    (ell-1+c)gK=0                                         (3)

and a prescribed nonzero gK both hold, while primary nondegeneracy fails. The row removes the automatic factor a0 in the differentiated transport equation. It does not enforce a0 nonzero.

The field fails transport already at cubic order. On the positive vertical axis, as y tends to zero,

    R=(ell X+U).grad rho-rho = 2 e3 y^3+O(y^5),
    e3=2^(2kappa)G/L^2 nonzero,
    |R|/Nf -> 1/2,
    |R|/Nv -> 2/(4+3D),                                  (4)

where Nf and Nv are the prompt's two pointwise denominators. Thus the defect remains detectable without dividing by an origin slope.

## 2. Smoothness, growth and finite-basis membership

Squaring the radial map gives

    r^2 = L^2 sigma [2(1-sigma)]^(-2kappa).

The right side has a positive derivative on 0<=sigma<1 and derivative L^2 2^(-2kappa) at sigma=0. Its inverse is smooth for all finite r^2, and analytic near zero by the analytic implicit function theorem. In particular

    sigma(r)=2^(2kappa)r^2/L^2+O(r^4).

The potentially ambiguous angular factor sigma cos2theta equals (sigma/r^2)(x^2-y^2); sigma/r^2 extends smoothly. This proves Cartesian smoothness of (1) and the stated parities. Its leading polynomial is

    rho = [2^(2kappa)/L^2] y[(u+v)x^2+(u-v)y^2]+O(r^5).   (5)

Thus a0=0 and the cubic vertical coefficient is e3 as stated. The vertical axis density is y w sigma G, nonzero whenever y is nonzero.

At infinity 1-t is asymptotic to (L/r)^(1/kappa), and sigma tends to one. Differentiation of the monotone map gives the same power bounds for its first derivatives. Hence rho=O(r^p), grad rho=O(r^(p-1)), with p=1/ell in (0,1). The canonical inverse exists and has the required gauge by the separately proved cancellation inverse theorem.

In the Q basis

    rho=y w sum_k sigma^k B_k(t) cos(2k theta),

take B_0(t)=u(1+t)/2, B_1(t)=v and all other B_k zero. These are allowed finite polynomials already at N>=1, M>=2. Their endpoint sum is B_0(1)-B_1(1)=u-v=G. The actual density amplitude on the positive vertical axis is K=L^(1/kappa)G/2. The counterexample is therefore inside the representation to which the safeguard was applied.

## 3. Independent canonical strain calculation

Using sin theta cos2theta=(sin3theta-sin theta)/2, the third sine mode is

    rho_3(r)=v r w(r) sigma(r)/2.

The canonical origin identity is c=-a0/4+integral_0^infinity rho_3(r)r^(-2)dr. In this example the integral is absolutely convergent even before an origin renormalization, since rho=O(r^3) near zero. Logarithmic differentiation of the map gives

    dr/r = [1/(2sigma)+kappa/(1-sigma)] d sigma.

Consequently

    integral_0^infinity w sigma dr/r
      = integral_0^1 [(1-sigma)/2+kappa sigma] d sigma
      = (1+2kappa)/4,
    c=v(1+2kappa)/8=-D.

No harmonic strain is added. This proves (2)-(3) from the independently computed canonical functional.

## 4. Cubic transport defect and denominators

Parity and smoothness give U_2(0,y)=c y+O(y^3)=-D y+O(y^3), U_1(0,y)=0 and rho_x(0,y)=0. Equation (5) gives rho(0,y)=e3 y^3+O(y^5) and rho_y(0,y)=3e3 y^2+O(y^4). Since ell+c=1, the transport term on this axis is 3e3 y^3+O(y^5); subtracting rho gives (4).

For y>0 small, the two terms in Nf have leading absolute values 3|e3|y^3 and |e3|y^3. The three terms in Nv have leading absolute values |e3|y^3, 3|e3|y^3 and 3D|e3|y^3. Dividing proves the limits. This direct calculation avoids using the primary cubic formulas outside their nonzero-slope hypotheses.

## 5. Scope, scaling and dependencies

The counterexample refutes only the assertion that (3) together with gK nonzero excludes a0=0. It does not show that a zero-slope solution satisfies all collocation rows, nor that any retained numerical state actually has zero slope. Each saved state's slope and PDE residual must still be evaluated.

Under genuine spatial dilation rho_lambda(X)=lambda rho(X/lambda), a0 remains zero and e3 changes to lambda^(-2)e3. The defect and denominator ratios in (4) are unchanged after the corresponding spatial change. Neither scaling nor the fixed canonical gauge repairs nondegeneracy.

Dependencies are the canonical inverse and origin identities proved in ../inverse/PROOF.md and ../origin/PROOF.md, elementary smooth inversion of a scalar map, and Taylor expansion. The construction was independently checked after reading the separate rep3 audit's explicit numerical-safeguard counterexample. It supplies no primary or secondary existence endpoint.
