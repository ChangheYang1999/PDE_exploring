# Precise conventions and response to the proof review

Read this with PROOF.md. The first actualOpus5.5 review at02:44:07Z accepts
the analytic construction subject to conventions and linkage obligations.
The following resolves those points; the code is not yet run.

1. Throughout, t=log r and D_t=r partial_r. Original polynomial center
t_c=(a+b)/2 is in this same logarithmic variable. For a radial power
r^e, use exp(e*b) if e>=0 and exp(e*a) if e<0. Thus negative powers at
orders above beta use the smaller radius. The implementation verifies
contiguous exact spans and directed inequalities
exp(a_first)<p_min-3delta and exp(b_last)>p_max+3delta, which imply the
whole disc's radial coverage for every p in its exact bracket.

2. Every derivative bound expands a polynomial Q(D_t) and uses
sum_j |Q_j| M_j, with M_j a certified magnitude bound for D_t^j F.
No signed polynomial is evaluated on nonnegative magnitudes. In the
moment derivative identity lambda_J=2n-4 is the forward t coefficient;
the backwards envelope uses its negative4-2n. Both are kept explicitly.

3. Topic89 proves the exact normalized spline has1557 simple interior
knots and degree7, hence is C^6 across all these knots, with the usual
finite one-sided seventh derivatives. This assertion and its exact knot
audit are imported, not inferred from arbitrary interval coefficient
boxes. The seven spans here are strictly inside the finite middle region,
away from the center and tail joins. Therefore rho is C^6 there, the
canonical Poisson modes are at least C^7, and U has the C^4 regularity
needed here. In particular the fourth derivatives of grad rho and U
are continuous across the seven-span joins; no surface delta appears.
The span envelopes alone would not prove this without that imported
spline interpretation. This is an explicit dependency.

4. The exact facts V(P)=0,DV(P)=D,grad rho(P)=(0,g) are the conclusion of
topic89. They justify each Taylor base estimate in section4. The canonical
physical velocity is U=grad_perp psi, while V=c_l X+U. The latter is not
itself grad_perp psi. Since the added c_l X is linear, derivatives of V
of orders3,4 equal those of U. No other affine or harmonic term is added.
The imported normalized modal representation is rho=r^3 sum H_j sin(...)
and psi=r^4 sum(J-I)sin(...)/2 with precisely that normalization.

5. The first algorithm uses Bernstein ranges, exact endpoint scalar
majorants, and complex ladder polynomials. The second uses absolute
monomial ranges, a Gronwall envelope, and ordinary Cartesian recursions.
These are two independent enclosure calculations of the same imported
canonical input boxes. They do not independently reintegrate the entire
canonical inverse. That limitation was already part of the proof and
remains mandatory. A changed input could invalidate both simultaneously.

6. The cutoff is C^4, generally not C^5, and C^4 is sufficient for this
auxiliary operator theorem. No assertion about a distinct localization
estimate requiring a fifth cutoff derivative is made. The original
plain-text "nu" in the cutoff constants is the dimensionless first
quadratic-derivative bound. Its meaning is unchanged by typography.

The resulting norm will be deliberately coarse and possibly enormous.
It supplies a finite numerical bound for this explicit auxiliary operator,
not a practical fixed-point constant and not the physical rank-one inverse.

7. Section2's phrase "derivative order0,...,4" suffices for the moment
ODE recurrence through order5, but the direct density derivative of order5
requires H through order5. The actual algorithm computes all polynomial
derivatives0,...,5. Both polynomial enclosure proofs hold for every order
through degree7. Also the displayed definition "u=2*(23/8)/a" in section1
is the same constant denoted nu in the next lines, not a second variable.
