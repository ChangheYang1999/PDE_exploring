# Independent last-span and source-mode check

2026-10-21, before the second computation. Let the spline degree be p_s=7, its nondecreasing knot vector t have length384, and its376 control coefficients in a fixed angular mode be c_i. Both endpoints have multiplicity8. The final span is[t_375,1]. On that span the de Boor recurrence uses indices i=375 and the eight coefficients c_(i-p_s),...,c_i. At recurrence level ell and index j, replace d_j by

(1-alpha)d_(j-1)+alpha d_j,
alpha=(1+delta-t_(i-p_s+j))/(t_(i+j-ell+1)-t_(i-p_s+j)), delta=q-1.

Every denominator is positive on this fixed last-span recurrence. Starting from constant control polynomials and performing these operations over exact rationals yields the exact polynomial in delta representing the spline. Its coefficients at degrees0,1,2 are b(1),b'(1),b''(1)/2. This is an independent route to the endpoint identities used by the first diagnostic. De Boor's recurrence follows from the affine interpolation representation of B-splines; fixing the last interval removes all branch choices. The derivative identities may also be obtained by differentiating the Cox recursion and collecting coefficients. Here the final polynomial will be checked against the differentiated-control endpoint values in the first result.

For independent source-mode evaluation, write rho_t=r partial_r rho. Integration by parts on the quadrant, using the vanishing sine factor at its endpoints, gives

f_n(r)=(4/(pi r))int_0^(pi/2) [cos(theta)rho_t sin(2n theta)+rho(cos(theta)sin(2n theta)+2n sin(theta)cos(2n theta))]dtheta. (1)

This follows directly from rho_x=(cos(theta)rho_t-sin(theta)rho_theta)/r. It uses no angular derivative in the numerical integrand. The symmetry factor4/pi follows from the even-x, odd-y parity of rho.

To avoid subtracting a compact coordinate close to1, evaluate delta=-exp(-(1-k)log(1+u^2)/2) directly in the exact last-span polynomial. With w=u^-2,
q_t=-(1-k)delta/(1+w), chi=(1+r0^2w)^-1,
(chi^j)_t=2j r0^2w(1+r0^2w)^-1 chi^j.

The regularized density amplitude is
rho=L^3u^k P exp((k-3)log(1+w)/2+sum chi^j b(1+delta)cos(2m theta)+(1+w)^(-p/2)T(1+2delta)g).

Its logarithmic derivative uses k-(k-3)w/(1+w), the spline terms b' q_t and the chi derivative above, and the singular terms p w/(1+w) times its radial coefficient plus2(1+w)^(-p/2)T' q_t. Direct differentiation proves these formulas. Applying (1) with a composite trapezoid rule and comparing a few fixed fit-window radii against the independent de Boor/Gauss derivative calculation checks two distinct numerical representations.

All polynomial identities are exact rational statements about the finite input data. Evaluated densities, source quadrature, condition numbers and fits remain binary64 diagnostics with no claimed remainder or quadrature-error enclosure. Reconstructing logarithmic grid radii from saved endpoints does not attest the historical radius array. The phrase actual saved fit radii in the original plan means this reconstruction; the full arrays were not saved.
