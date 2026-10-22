# A degree-five center term produced by a compact zero-strain perturbation

Date 2026-10-22T02:39:11.650300+00:00. This finite-regularity version is written before its new symbolic checks. It supersedes the original version's unnecessarily strong smoothness hypothesis on compact annuli. The theorem and canonical-trial application remain OPEN pending those checks, an actual Claude Opus5.5 review and later own adjudication.

## Exact statement

Assume an even-x, odd-y canonical background rho has, near0,

 rho=x^2 y+R,  |grad R|<=C r^4,  |D^2 R|<=C r^3,

and smoothness sufficient for these derivatives. Assume at infinity |grad rho|<=C r^(k-1), |D^2 rho|<=C r^(k-2), with k<1, and that rho is C^2 and U[rho] is C^1 on compact annuli. Here U[h]=(-psi[h]_y,psi[h]_x), -Delta psi[h]=partial_x h, with the canonical full-plane inverse and Sigma(h)=psi[h]_xy(0). Define

 L_rho h=(ell X+U[rho]).grad h-h+U[h].grad rho+(Sigma(h)/3)D rho,

with any real ell and the PLUS strain sign. Let J(h) denote any center cubic-jet normalization used for this run, in particular J(h)=partial_xxy h(0)/2.

There is h in C_c^infinity(R^2), supported in1<r<2, even in x and odd in y, with a global smooth factor x^2 y, J(h)=Sigma(h)=0, and

 L_rho h=2(x^4 y+5x^2 y^3)+O(r^7),
 grad(L_rho h)=grad[2(x^4 y+5x^2 y^3)]+O(r^6).               (1)

For the weight w_m=L^(2m+2)r^(-2m-2)(1+r^2/L^2)^(m-k-1/2), L>0, and norm squared integral w_m(h^2+r^2|grad h|^2)dX, this h belongs to X_m for every fixed integer m>=2, but L_rho h does not belong to X_m for m>=5. Under the stated far regularity it does belong to X_m for m=2,3,4. Hence the two constraints J=Sigma=0 alone do not ensure that the full linearized operator maps every smooth annular perturbation into X_m when m>=5. This does not contradict higher_center_weight_quasimodes: that construction imposes further harmonic-moment constraints, including Gamma_4=0 when m>=5.

## Construction and factor

Choose eta in C_c^infinity((1,2)), eta>=0, with integral eta(r)dr=1. Such a function is obtained by normalizing any nonzero nonnegative smooth bump on(1,2); its integral is strictly positive and finite. Set chi(r)=r^4 eta(r) and

 h(r,theta)=chi(r)(sin(5theta)+sin(7theta)).

It is smooth on the plane after setting it to0 off its compact annulus. The exact identity

 sin(5theta)+sin(7theta)=4x^2y(3x^4-10x^2y^2+3y^4)/r^7

proves the global smooth x^2y factor: define the quotient by the displayed smooth expression on r>0 and by0 near0. Its parity is also explicit. All center jets vanish, so J(h)=0. Its third density sine coefficient is zero, so the canonical moment formula gives Sigma(h)=integral r^(-2)F_3(r)dr=0.

## The interior harmonic polynomial and its coefficient

For a compact annular density sum F_l(r)sin(l theta), the source's n-th sine coefficient is

 f_n=[F_(n-1)'-(n-1)F_(n-1)/r+F_(n+1)'+(n+1)F_(n+1)/r]/2.

The canonical radial Green formula gives psi_n(r)=Gamma_n r^n inside the support, with

 Gamma_n=(1/(2n)) integral r^(1-n)f_n(r)dr
         =(1/2) integral r^(-n)F_(n+1)(r)dr.                 (2)

To obtain the second equality, integration by parts replaces integral r^(1-n)F_l' by (n-1)integral r^(-n)F_l. The lower angular mode cancels, and the upper mode gains the factor2n. All boundary terms vanish since the density is compactly supported inside the annulus. This also proves that no other regular harmonic components appear.

Here F_5=F_7=chi and all other F_l vanish. Consequently, for r<1,

 psi[h]=(1/2)r^4 sin(4theta)+Gamma_6 r^6 sin(6theta),
 Gamma_6=(1/2)integral r^(-2)eta(r)dr,  1/8<Gamma_6<1/2.     (3)

The strict bounds follow from1/4<r^(-2)<1 wherever eta is nonzero and from integral eta=1. The coefficient in front of the Cartesian quartic x^3y-xy^3 is2, because r^4 sin(4theta)=4(x^3y-xy^3). For an arbitrary unnormalized nonnegative chi, that coefficient is C=2 integral r^(-4)chi(r)dr. The formula C=(1/2)integral r^(-4)chi dr is the coefficient of the polar harmonic r^4 sin(4theta), and would be off by a factor4 if assigned to the Cartesian quartic. The sign here is fixed by -Delta psi=partial_x h and U=(-psi_y,psi_x), not left ambiguous.

For psi_4=C(x^3y-xy^3), direct differentiation gives

 U_4=(-C x^3+3C xy^2, 3C x^2y-C y^3),
 U_4.grad(x^2y)=C(x^4y+5x^2y^3).                            (4)

The degree-six harmonic in(3) contributes velocity of degree5, so its product with grad(x^2y) has degree7. The quartic harmonic velocity times grad R is O(r^7). Differentiating these terms uses the assumed Hessian remainder and gives O(r^6). On r<1 the local terms h and grad h vanish and Sigma(h)=0, so L_rho h=U[h].grad rho there. With C=2, equations(3)-(4) prove(1).

## Weighted membership and nonmembership

On every compact annulus the weight is smooth and strictly positive. Hence h is in X_m for every fixed m. Near0 the leading homogeneous polynomial in(1) is strictly positive on every closed arc strictly inside the first quadrant. Its minimum on a chosen unit-circle arc is positive. For sufficiently small r, the O(r^7) remainder is at most half that positive leading lower bound, so |L_rho h|>=c r^5 on the corresponding sector. Since w_m is comparable to r^(-2m-2) near0, the zeroth-order contribution dominates a positive multiple of

 integral_0^r0 r^(9-2m)dr.

This diverges exactly when m>=5 among the stated integers. The zeroth-order term alone proves nonmembership; it does not rely on an upper bound as evidence of divergence. At m=5 the divergence is logarithmic. For m=2,3,4, equation(1) and its differentiated form give integrable upper bounds for both terms near0.

Outside the annulus, h and its derivatives vanish. The canonical kernel for a compact density gives U[h]=O(r^(-2)) and grad U[h]=O(r^(-3)) at infinity; sharper cancellation is unnecessary. Thus L_rho h=O(r^(k-3)) and its gradient is O(r^(k-4)). Since w_m is comparable to r^(-2k-3) there, both squared radial integrands are O(r^(-8)), which is integrable. On the intervening compact annuli, rho in C^2 and U[rho] in C^1 suffice: differentiating (ell X+U[rho]).grad h-h uses one derivative of U[rho] and the smooth derivatives of h; differentiating U[h].grad rho uses at most two derivatives of rho. Sigma(h)=0, so the rank term vanishes. Thus L_rho h is C^1 there. No C^infinity regularity of the background is required. This completes the m=2,3,4 membership assertion.

## Canonical application, dependencies and limits

The exactly joined and normalized modal trial is an instance of the background assumptions, via the center and far estimates mapped in notes/185_186_operator_background_scope_20261022.md and the accepted higher_center_weight_quasimodes parent. The canonical modal background has the required finite regularity on positive-radius annuli: exact C^6 joins and degree-seven clamped B-splines give C^6 density, and the accepted local canonical velocity regularity supplies C^1. It is not asserted to be C^infinity at all knots. Its accepted complete parent pins must be checked again before claiming this application. No floating joining or normalization assertion is used.

The symbolic verification will independently reconstruct the sine-to-Cartesian identity, the source-moment cancellation, the velocity and polynomial in(4), and the two radial integrability exponents. One path uses exact rational polynomial dictionaries; another uses independently assembled Sympy expressions and derivative operations. No numerical integration is necessary: the normalized bump gives an exact quartic coefficient and an analytically proved interval for Gamma_6. No large table or external source is hardcoded.

This is an explicit mapping obstruction for the stated stronger center weights, not an exact kernel, nonexistence theorem, inverse estimate in a different norm or a PDE endpoint. It does not establish the lead's broader unverified threshold or anisotropic-space claims. The exactly joined background is essential to the stated application and is not replaced by the unjoined stored representation.
