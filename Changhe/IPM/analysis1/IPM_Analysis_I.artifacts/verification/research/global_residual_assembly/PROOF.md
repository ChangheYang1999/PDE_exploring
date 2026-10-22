2026-10-21T10:54:26.971858+00:00

# Joining the three canonical residual regions

This proof precedes the assembly code. It is a conditional enclosure theorem. Its numerical application with the complete independent middle method remains OPEN until that method, its final output audit and its separate mathematical verdict are complete. A finite primary assembly is a different evidence level and must be labelled accordingly.

## Statement, notation and hypotheses

Let rho be a real C1 density on the full plane, even in x and odd in y, with a canonical full-plane velocity U=(-psi_y,psi_x), -Delta psi=rho_x. The inverse must be the unique parity-compatible sublinear velocity. No region may use an artificial wall or a different harmonic xy strain. Assume that the accepted canonical construction makes the residual

    epsilon(X)=(c_l X+U(X)) dot grad rho(X)-rho(X)

continuous. Fix exact L>0, 0<k<1/2 and c_l=1/k. In the application the same density has the exact center normalization rho=x^2 y a, a(0)=1, and psi_xy(0)=3/k-1. This normalization is an independently established dependency, not a consequence of assembling norms.

For r>0 put u=r/L, m(r)=u^3(1+u^2)^((k-3)/2), and let

    epsilon(r,theta)=sum_(j=0)^521 epsilon_j(r) sin((2j+1)theta),
    W(r)=sum_(j=0)^521 |epsilon_j(r)|.

All three regions must use these same coefficients of this same global residual. The finite sum has highest frequency1043. Suppose exact t_-<t_+ give R_-=exp(t_-), R_+=exp(t_+). Define the closed inner disk, closed middle annulus and closed exterior by r<=R_-, R_-<=r<=R_+, and R_+<=r respectively. Their interiors are disjoint and their union is the full plane. Regional proof files must identify precisely these joins, including finite endpoint values, full origin disk and infinite tail.

For each region J in {inner,middle,outer}, assume proved nonnegative exact upper bounds b_(J,d) for

    sup_(r in J,r>0) (1+r/L)^d W(r)/m(r),

for d=0,1/2,1/2-k, and b_(J,abs) for sup W(r). Assume a proved exact upper bound E_J for

    integral_J |epsilon(X)/m(|X|)|^2 dX/[1+(|X|/L)^2].

These hypotheses concern full regions and full angular intervals, not sample points. In the inner disk also assume the proved local majorant W(r)<=B r^5. In the exterior assume the proved finite majorant W(r)<=sum_(gamma,l) D_(gamma,l) tau^l exp(gamma tau), tau=log(r/R_+), for all sufficiently large tau, where each D>=0, l is a nonnegative integer and gamma<=2k-1<0. Canonical homogeneous transients are included in this majorant.

Then epsilon/m extends continuously by0 at the origin. Each of its three weighted suprema is bounded by max_J b_(J,d); sup|epsilon|<=sup W<=max_J b_(J,abs). The full-plane weighted norm

    N2(epsilon)=[integral_R2 |epsilon/m|^2 dX/(1+(r/L)^2)]^(1/2)

satisfies N2(epsilon)^2<=E_inner+E_middle+E_outer. All three normalized weighted residuals tend to0 at infinity, as does epsilon. These conclusions give zeroth residual bounds only. They give no inverse, nonlinear estimate, norm distance to X3, exponent enclosure or decisive IPM endpoint.

## Proof

The weight is strictly positive for r>0. As r tends to0, m(r)/(r/L)^3 tends to1. The inner bound therefore implies W/m=O(r^2), uniformly in theta, and epsilon/m tends to0. Multiplication by (1+r/L)^d preserves this limit. At any positive radius, continuity follows from the assumed global residual and the positive continuous weight. Thus the definition at0 is compatible with the full-plane supremum and with the Lebesgue integral.

For each angle the triangle inequality gives |epsilon|<=W. The finite union of the three closed radial regions then proves the maximum formulas. A join radius belongs to both adjacent certificates; it cannot be omitted. The reported maximizing certificate cell is the location of the largest computed upper bound. It need not be the location of the actual residual maximum.

For completeness, orthogonality on the full circle gives

    integral_0^(2pi) |epsilon(r,theta)|^2 dtheta
      =pi sum_j |epsilon_j(r)|^2 <= pi W(r)^2.

If W/m<=M on a closed annulus r_a<=r<=r_b, its squared norm is at most

    pi M^2 L^2/2 * log((1+(r_b/L)^2)/(1+(r_a/L)^2)).

This follows by integrating r/[1+(r/L)^2] exactly. It explains the regional scalar integrals but does not replace their infinite-tail proofs. The circles r=R_- and r=R_+ and the origin have planar measure zero. Additivity of the nonnegative integral over disjoint interiors gives the squared-norm sum, even before invoking finiteness. The regional hypotheses make the sum finite. Taking its positive square root proves the asserted bound. Summing regional unsquared norms would also be valid but weaker; taking a maximum of the squared norms would be invalid.

At infinity, m(r)/u^k tends to1 and (1+u)^d/u^d tends to1. Each exterior normalized weighted term is bounded by a constant times a polynomial in tau multiplied by exp((gamma-k+d)tau). Since gamma<=2k-1 and d<=1/2, gamma-k+d<=k-1/2<0. Every such polynomial-exponential term tends to0. The finite sum does too. The absolute residual tends to0 because gamma<0. This proves the decay claims without numerical sampling of an unbounded interval.

## Exact application and dependencies

The density is the normalized finite modal trial specified by data_exact/modal_v2.json, SHA25657f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6, together with the exact canonical normalization scalar from modal_repair and modal_green. It is not asserted to be the original nonlinear X3 ansatz. The application uses

    k=1615536043799051/9007199254740992,
    L=8614738245908811/1125899906842624.

The joins t_- and t_+ must be read as exact rationals from the original modal knots and checked against every regional certificate. Rounded displayed radii are insufficient. Topic45 (inner_cells) and topic43 (outer_cells) provide complete independent regional bounds, including the small disk and infinite tail, with their existing canonical dependencies. Topic31 (middle_residual) provides the accepted full primary7809-cell assembly. Topic46 (middle_second), when complete and separately accepted, supplies the additional independent middle representation. All use the same canonical archive as expressly declared in their proofs. Agreement of interval methods is not a second proof of that shared archive.

The assembly must read exact rational endpoints, check accepted status, rehash the complete cited pin maps, check full-cell counts and source/footer bindings, verify the exact region joins, and compare all public decimal ceilings as exact rationals. The squared-norm sum will be formed exactly. Two new scalar evaluations, Arb and mpmath.iv, plus an exact integer-square-root ceiling will independently enclose its square root. They do not regenerate regional enclosures or close any missing regional hypothesis. Numerical output may be marked FINAL for this assembly only after actual Opus5.5 collaboration and separate verifier review; a future independent-mode run additionally requires the complete topic46 verdict. Until then this is an explicit conditional theorem and preparation.
