# Source Fourier formula and failure of a local coupled cokernel condition

2026-10-20. Independent verification note written before the arithmetic check. The elementary statements below are proved here. The complete cusp expansion proposed in the lead's pcusp1 note is under separate review and is not accepted by this note alone.

## Exact frozen Fourier inverse

Fix A>1 and g>=0, and let M be the multiplier xi^2/(xi^2+eta^2). Define

L=A s partial_s+y partial_y-1-g M,
a=g/(A-1), Q=A+1, q=A+2-a,
delta_r(xi,eta)=(r^A xi,r eta).

Use hat f(zeta)=integral exp(-i X dot zeta)f(X)dX. Fourier differentiation gives

Lhat=-D-(A+2)-g m,
D=A xi partial_xi+eta partial_eta,
m=xi^2/|zeta|^2.

Since D log|zeta|=1+(A-1)m,

|zeta|^a Lhat |zeta|^(-a)=-D-q.

This identity is pointwise away from zero frequency. For compactly supported smooth f, set G(zeta)=|zeta|^a hat f(zeta) and

I(zeta)=integral_0^1 r^(q-1)G(delta_r zeta)dr.

The lower endpoint is convergent: q+a=A+2>0, and |delta_r zeta|<=r|zeta| for 0<r<=1. Oddness in y supplies an additional factor r at zero. Integration by parts in r gives D I=G-q I, so

hat h=-|zeta|^(-a) I

solves Lhat hat h=hat f away from zero. At low frequency this formula is O(|zeta|) for odd-y f, by the same estimate. For completeness, the Fourier semigroup of L is exp(-(A+2)t-g integral_0^t m(delta_(exp(-v)) zeta)dv) hat f(delta_(exp(-t)) zeta). Integrating D log|zeta| gives the factor exp(-q t)|delta_(exp(-t)) zeta|^a/|zeta|^a. Substitution r=exp(-t) in the negative semigroup integral is exactly the displayed inverse. The ordinary below-threshold H^s generator theorem in ../coupled_thresholds/PROOF.md and ../source_pole/PROOF.md makes this integral converge in H^s for 0<=s<min((g+(A+3)/2)/A,(A+3)/2). Thus it identifies the formula with that unique maximal-graph inverse. The algebra introduces no alternate condition at the Fourier origin and no free homogeneous solution.

For nonzero zeta define the profile integral

B_f(zeta)=integral_0^infinity r^(q-1)|delta_r zeta|^a hat f(delta_r zeta)dr.

The lower endpoint converges as above. At the upper endpoint at least one frequency coordinate grows as a positive power of r, so arbitrary Schwartz decay gives convergence. Substitution t=Rr proves B_f(delta_R zeta)=R^(-q)B_f(zeta). These are exact identities independent of any finite-part prescription.

## A forcing with a nonzero profile integral

Take any nonzero real compactly supported smooth function phi(s,y), even in each coordinate, with integral phi>0. Let phi_tilde(X)=phi(-X), psi=phi*phi_tilde, and f=partial_y psi. Then

hat f(xi,eta)=i eta |hat phi(xi,eta)|^2.

For theta>0,

B_f(1,theta)=i theta integral_0^infinity r^q
 (r^(2A)+theta^2 r^2)^(a/2)|hat phi(r^A,theta r)|^2dr.

Every factor in the real integral is nonnegative. Continuity and hat phi(0)>0 make it strictly positive on a small nonempty r interval. Therefore B_f(1,theta) is nonzero. This proves a nonzero Fourier profile integral for explicit allowed data. Deducing the sharp local regularity of h still requires the finite-part construction, localization and sector bounds in the proposed expansion; those do not follow from positivity alone.

If the proposed leading term has anisotropic physical degree d=1+g and Fourier amplitude |xi|^(-beta)C(eta |xi|^(-1/A)), then beta=(A+1+d)/A. Integrating the squared amplitude on horizontal dyadic shells gives the power N^(2r-2beta+1+1/A). Its zero exponent is

s_fast=(d+(A+1)/2)/A=(g+(A+3)/2)/A.

Multiplication by eta^2/xi^2 improves the shell exponent by 4-4/A, hence improves ordinary Sobolev order by 2-2/A. The corresponding proposed remainder threshold is s_1=s_fast+2-2/A. An L1 shell bound is N^(-d/A), suggesting the noninteger classical threshold d/A. These exponent calculations are exact conditional consequences of the stated sector form. They are not a substitute for proving that form or its uniform angular integrability.

## Compactly supported counterexample to f_y(0)=0

Let chi be a compactly supported smooth cutoff, even in each coordinate and equal to one near zero. Set

p(s,y)=s^2 y-y^3/3,
k=chi p,
u=-Delta k.

The polynomial p is harmonic because p_ss=2y and p_yy=-2y. Thus u is zero on an entire neighborhood of zero, while u is globally compactly supported and smooth, even in s and odd in y. Fourier transformation gives

M u=-partial_s^2 k.

This is an equality of ordinary functions and tempered distributions: hat u=|zeta|^2 hat k, and multiplication by m gives xi^2 hat k. The value of m at the single frequency zero has no effect. Consequently

f=L u=(A s partial_s+y partial_y-1)u+g partial_s^2 k

is compactly supported and smooth. Near zero it equals 2g y. For g>0, f_y(0)=2g is nonzero although every local jet of u vanishes. Hence f_y(0)=0 is not a necessary solvability condition for the frozen coupled operator on compactly supported smooth data.

Differentiation of the equation at the source instead gives

f_y(0)=(mu-1)u_y(0)-g(Mu)_y(0)

for the drift A s partial_s+mu y partial_y. Its last term is nonlocal and cannot be replaced by a quantity determined by the germ of u. The counterexample works for every positive A and mu because u is locally zero. No Fredholm index is determined by this observation.

## Preservation of global IPM symmetry and normalization

The same obstruction can be placed at a pair of nonzero axis points P=(x_*,0) and -P. Choose chi with sufficiently small support that these two translated supports are disjoint and avoid the origin. Define

k_global(x,y)=chi(x-x_*,y)p(x-x_*,y)
             +chi(x+x_*,y)p(x+x_*,y),
h=-Delta k_global.

Because chi and p are even in their first variable and odd parity is supplied by p in y, k_global and h are even in x and odd in y. Both vanish near the origin. Choose the supports to avoid the entire axis x=0 as well. Oddness in y implies h=y b with smooth b, and division by x^2 on these supports gives a global smooth factor h=x^2 y a_h. Since h vanishes near the origin, adding h preserves the exact center factor and every normalization depending on a local density jet there. It also has compact support and leaves every far asymptotic coefficient unchanged.

The canonical IPM stream function of h is psi[h]=partial_x k_global. Indeed -Delta(partial_x k_global)=partial_x h, and the resulting velocity is compactly supported. Canonical uniqueness follows from the same whole-plane growth and parity argument used in ../canonical_inverse/PROOF.md. Therefore

U[h]=(-partial_xy k_global,partial_xx k_global),
sigma[h]=partial_xxy k_global(0)=0, delta c_l=sigma[h]/3=0.

Near P, U[h]=(-2(x-x_*),2y) while h and its gradient vanish. For a C2 background with grad rho_bar(P)=(0,g), use the exact eliminated-normalization IPM linearization

L_bar h=(c_l X+U[rho_bar]) dot grad h-h+U[h] dot grad rho_bar+(sigma[h]/3) X dot grad rho_bar.

Every local differential term in h and the displayed normalization term vanish near P. Thus this full normalized linearization satisfies

L_bar h=U[h] dot grad rho_bar

near P, and differentiation gives partial_y(L_bar h)(P)=2g. The term involving second derivatives of rho_bar vanishes at P because U[h](P)=0. Thus the same proposed local scalar condition fails even with the required global parity, center preservation, compact support and canonical gauge. The regularity of L_bar h follows that of the background on this support; it is smooth when the background is smooth there. The precise normalization functionals covered are the density germ at the origin (including J and its derivatives), the canonical strain sigma, and the specified far-field coefficients. No additional nonlocal modulation functional is claimed to vanish. At a drift source P this refutes the asserted local coupled source solvability condition; the construction itself is valid at any nonzero axis point with the stated background gradient. This proves no existence, exclusion or global inverse statement.

## Dependencies and open claims

Dependencies are Fourier differentiation, elementary integration, the accepted canonical uniqueness and frozen generator theorems, and explicit compactly supported smooth cutoffs. The input decimal parameters used for illustrative exponent arithmetic must be treated as exact illustrative rationals, not as certified source enclosures. The full pcusp1 finite-part expansion, endpoint Holder theorem, sharp local Sobolev failure, profile-map codimension and variable-coefficient extension remain separate audit obligations.

## A certified parameter box for the conditional cusp exponents

The independently verified modal source data are enclosed by the rational rectangle

10.1507252 <= A <= 10.1507253,
29.7494906 <= g <= 29.7494908.

Here both A_trial and the separately listed A_exact_solution_relation (a label inherited from modal_source, not a claim of an exact solution) lie in this rectangle, while g is the modal-trial gradient. This certifies an association with a frozen family having mu fixed to1. It does not identify any exact solution parameter and does not replace the actual modal value mu different from1 by an equality. The actual nonunit mu changes the drift and the cusp exponents, so these margins are not asserted for that distinct operator.

For every point of this rectangle, put d=1+g. Elementary interval bounds certify 3<a=g/(A-1)<4, 3<d/A<4, 2<gamma=g/A<3, q=A+2-a>5/2, and s_1=5/2+(g-1/2)/A>21/4. The only possible nonnegative i in Ai+j=d are i=0,1,2,3, because d-4A<0. For each of these four i, the interval [1+g_lower-i A_upper,1+g_upper-i A_lower] lies strictly between consecutive integers. Thus no nonnegative integer pair (i,j) is resonant. These strict rational checks close the parameter-margin gap for this frozen rectangle, but none of the outstanding analytic finite-part or localization gaps.
