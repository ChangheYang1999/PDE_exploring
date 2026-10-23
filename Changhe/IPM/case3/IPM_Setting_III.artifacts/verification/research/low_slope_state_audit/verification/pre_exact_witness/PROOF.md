# Finite diagnostics of two low-slope iterates

Written on 2026-10-21 before the new diagnostic. This is a finite evaluation protocol, not an existence theorem or a classification of the low-slope regime.

For a frozen Q density rho=y w sum_{j=0}^{M-1} s^j B_j(t) cos(2j theta), with s=(1+t)/2, w=1-s, and r=L sqrt(s)/(2w)^kappa, define a=sum_k (-1)^k B_{0,k}, the exact coefficient rho_y(0), and suppose a!=0. Then the continuous quotient away from the origin is

    q=rho/(a y)=(w/a) sum_j s^j B_j(t) cos(2j theta).

The right side extends to the axes without division by y. Since s=O(r^2), w=1+O(r^2), and B_0(-1)=a, it extends smoothly with q(0)=1. It has the density's prescribed reflection symmetries. In particular, sampling only r>=1e-4 omits the values approaching 1 at the origin, so a sampled supremum below 1 is not a global bound below 1. This observation applies irrespective of the solver's parameter history.

The independent Q reconstruction, exact center strain and jets, canonical full-plane inverse, and the prompt's two residual denominators have been established in research/finite_q_exact_jets/PROOF.md, research/q_full_inverse_primitives/PROOF.md, and research/shared_sampling_inverse_audit/PROOF.md. We apply those identities without fitting a strain or altering a center row. If c is the canonical center strain, the exact transport center defect is Delta=ell+c-1; nonzero a Delta rules out this finite formula being an exact nondegenerate profile. This follows by differentiating (ell X+U).grad rho=rho at the origin, where U=0, grad rho=(0,a), and U_{2,y}=c.

The new quotient diagnostic uses independently offset physical radial and angular grids, including both axes and more of the origin and far regions. It separately repeats only the producer's declared sample set, 400 logarithmic radii from 1e-4 to 1e6 and 128 quadrant angular midpoints, without importing its evaluation or differentiation code. At selected extrema the quotient is recomputed by scalar multiprecision Clenshaw and the independent safeguarded radial map at 80 and 120 digits. All normalizations use the exact rational origin coefficient of the saved binary coefficients.

The canonical dense residual and selected multiprecision checks are separate from q. A violation q>1 or q<0 at an independently checked point disproves the corresponding one-sided bound for this finite formula. Absence of sampled violations does not prove a bound throughout the plane. Collapse, drift in ell, or a poor residual at two saved endpoints does not prove that any exact low-slope branch is absent. Far-tail exponents use the saved map exponent; rounding in that exponent is retained and recorded rather than repaired.
