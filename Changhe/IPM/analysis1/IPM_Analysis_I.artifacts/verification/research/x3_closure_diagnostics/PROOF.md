# Topic150. X3 far powers and finite-grid closure diagnostics

Written2026-10-21 before the new numerical audit. This is an asymptotic identity and an audit of saved floating observations, not a residual enclosure or an IPM endpoint.

## Statement and conventions

Let L>0,0<k<1/3,a=1-k,p=6+2k/(2-k),u=r/L and let X3 be the exact coefficient interpretation of the finite stored formula

rho=L^3 u^3 cos(theta)^2 sin(theta) exp(H),
H=(k-3)log(1+u^2)/2 + sum_m chi^max(m-1,0) b_m(q) cos(2m theta) + s^(p/2)T(2q-1)g(theta),
q=1-(1+u^2)^(-a/2), chi=u^2/(u^2+r0^2), s=u^2/(1+u^2),
g=|cos(theta)|^(p-2)sin(theta)^2.

Here r0>0, T is a finite polynomial and each of finitely many b_m is a spline, hence a polynomial on its last nonempty span ending at1. All stored coefficients have their exact dyadic meanings. Angular functions are periodic on the complete circle. In particular g is C1 since p>6. No stationarity is assumed.

The first four allowed powers of the sine modes of rho_x, in decreasing order, are k-1,2k-2,3k-3,k-3. More precisely, uniformly in theta,

rho_x(r,theta)=D00(theta)r^(k-1)+D10(theta)r^(2k-2)+D20(theta)r^(3k-3)+D01(theta)r^(k-3)+O(r^(4k-4)). (1)

Each sine coefficient obeys the corresponding expansion by integration. A displayed coefficient can vanish for an individual mode or for particular data. Thus allowed leading powers does not mean four nonzero leading terms in every mode. The constants in O are finite but unevaluated; (1) is not a quantitative tail error certificate at a supplied finite R.

## Proof of the expansion

Set z=u^(-a),w=u^(-2). Then q=1-z(1+w)^(-a/2), chi=(1+r0^2 w)^(-1), s=(1+w)^(-1), and

H=(k-3)log u + Hhat(z,w,theta),
Hhat=(k-3)log(1+w)/2 + sum_m(1+r0^2 w)^(-max(m-1,0))b_m(1-z(1+w)^(-a/2))cos(2m theta)
  +(1+w)^(-p/2)T(1-2z(1+w)^(-a/2))g(theta).

For sufficiently small z,w the spline arguments remain on their last spans. The polynomial expressions in that formula extend analytically to a complex bidisc about(0,0), with values in the Banach algebra C1 of the circle. The fractional powers and logarithm use their analytic branches at1. Finite sums, products and exponential preserve analyticity, and their power series converge absolutely in C1 on a smaller bidisc. Consequently

rho=L^3 u^k sum_(j,l>=0) Cjl(theta) z^j w^l,
Cjl the coefficients of cos(theta)^2 sin(theta)exp(Hhat).

For0<a<1 with3a>2, the first four exponents ja+2l are0,a,2a,2. Every omitted pair has exponent at least3a: for l=0 it has j>=3; for l=1 the next j is1 and a+2>3a; for l>=2 it is at least4>3a. Absolute convergence on a smaller bidisc bounds the omitted series by a constant u^(-3a). The same holds after theta differentiation and the Euler derivative u partial_u: differentiate the convergent series on a still smaller bidisc, absorbing the polynomial factors j,l by its geometric convergence.

Apply partial_x=L^(-1)(cos(theta)partial_u-sin(theta)u^(-1)partial_theta) term by term. The contribution of(j,l) is

L^2 u^(k-1-ja-2l)[(k-ja-2l)cos(theta)Cjl(theta)-sin(theta)Cjl'(theta)].

Absorbing fixed powers of L gives(1), including its uniform remainder. Angular mode integration preserves a uniform O bound. This proves the claim without assuming nonzero coefficients or bounding its finite-R constant.

## Exact influence of an exterior source continuation

Let f_n(r) be the coefficient of sin(2n theta) in a source f=rho_x, with canonical Green inverse

psi_n(r)=[r^(-2n)int_0^r s^(2n+1)f_n(s)ds + r^(2n)int_r^infty s^(1-2n)f_n(s)ds]/(4n).

Assume two integrable source continuations agree for r<R and differ for r>=R by delta f_n(s)=sum_j delta A_nj(s/R)^qj, where qj<0. For0<r<R direct integration gives

delta b_n(r)=r^(2n)R^(2-2n)sum_j delta A_nj/(2n-2-qj),
delta psi_n=delta b_n/(4n), delta psi_n'=delta b_n/(2r). (2)

Indeed the inner Green integral is unchanged, and the outer power integral is R^(2-2n)/(2n-2-qj), with its denominator positive. At n=1 the contribution to c=psi_xy(0) is

delta c=(1/2)sum_j delta A_1j/(-qj),
delta U_1mode=(-delta c x,delta c y). (3)

The last identity follows from delta psi_1 sin(2theta)=delta c xy and U=(-psi_y,psi_x). There is no freely adjustable harmonic strain in the canonical inverse; the strain in(3) is fixed by the changed exterior source. If the density inside R is kept fixed, the residual at stored c_l changes by delta U dot grad rho. If instead c_l=(1+c)/3 is recomputed, add(delta c/3)X dot grad rho. At a normalized center rho=x^2y+o(r^3) with compatible differentiated remainder, the n=1 strain term contributes -delta c x^2y while this scalar feedback contributes +delta c x^2y. They cancel at leading degree3. This is a local identity, not a bound for the remaining terms.

The numerical tail_start routine fits the modes of the source rho_x, not rho. Setting this tail start to zero represents a zero exterior SOURCE continuation in that mode inversion. It does not assert that a cutoff density has that derivative; a density cutoff generally contributes additional derivative terms. A leading-power least-squares fit also need not equal the exact asymptotic leading coefficient. These distinctions are essential when interpreting sensitivity tests.

## Evidence and scope of the finite audit

The new audit will check the saved two-resolution maxima and locations and eight closure/sampling variants using independent exact-rational ratios and rounding comparisons, with separate interval arithmetic checks. It will verify the wrappers and the current evaluator's relevant source expressions, and record the source timestamps. Current source was edited after several runs; static agreement is not historical execution attestation. No stored full residual fields are available in these outputs, so reading their argmax records does not independently recompute the physical sampled maxima. An aligned far-grid extension tests sensitivity within this numerical recipe, not the rigorous canonical tail error. Finite sample stability gives neither a supremum enclosure nor an infinite-dimensional inverse. The 48-hour decision remains OPEN.
