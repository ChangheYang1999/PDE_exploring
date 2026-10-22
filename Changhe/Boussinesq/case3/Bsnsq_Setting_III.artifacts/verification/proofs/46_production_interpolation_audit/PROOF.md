# Independent modal integration for an interpolation error audit

Date:2026-10-20. Status: analytical inverse formulas derived here;
manufactures and production-source numerical measurements complete.
See verification/SUMMARY.md for measured defects and exact limitations. This is an evaluator theorem,
not a theorem asserting a B2 solution. No teammate code is executed.

## 1. Exact hypotheses and source conversion

Use x=r sin(phi), y=-r cos(phi), and write the saved source as
Omega=x sum_{j=0}^{K-1} g_j(r) cos(j phi). The coefficients g_j are
evaluated independently from the serialized B-splines. Missing indices
mean zero. The elementary product identity for sin(phi) cos(j phi) gives

    omega_1=r(g_0-g_2/2),
    omega_k=r(g_{k-1}-g_{k+1})/2, 2<=k<=K,
    Omega=sum_{k=1}^K omega_k sin(k phi).

Assume the source has the saved origin mask, so each omega_k=O(r^k),
and omega_k=O(r^{-nu}) at infinity, 0<nu<1. These bounds ensure all
integrals below converge. Smoothness away from the spline interfaces
is sufficient for these evaluator formulas. Finite spline regularity
is not being reclassified as full smoothness.

## 2. Relative full-plane inverse and its derivative

For k>=2 solve the radial equation

    -P_k''-P_k'/r+k^2 P_k/r^2=omega_k.

Variation of parameters and regularity at0 and sublinear velocity at
infinity give, uniquely,

    P_k=(r^{-k} int_0^r s^{k+1} omega_k(s) ds
          +r^k int_r^infty s^{1-k} omega_k(s) ds)/(2k).

The derivative is

    P_k'=(-r^{-k-1} int_0^r s^{k+1} omega_k(s) ds
            +r^{k-1} int_r^infty s^{1-k} omega_k(s) ds)/2.

The two differentiation boundary terms cancel. For k=1 the ordinary
center velocity may diverge; subtracting its linear stream term first
gives the canonical relative inverse

    P_1=(r^{-1} int_0^r s^2 omega_1(s) ds
           -r int_0^r omega_1(s) ds)/2,
    P_1'=(-r^{-2} int_0^r s^2 omega_1(s) ds
             -int_0^r omega_1(s) ds)/2.

The relative velocity at0 vanishes. Any other smooth full-plane inverse
with sublinear velocity differs by a constant velocity: each component
of the difference is an entire sublinear harmonic function. Subtracting
its center value removes it. No affine strain or exterior mode is free.

For numerical stability define I_k=int_0^r(s/r)^{k+1}omega_k(s)ds and
J_k=int_r^infty(s/r)^{1-k}omega_k(s)ds for k>=2, while
J_1=-int_0^r omega_1(s)ds. Then P_k=r(I_k+J_k)/(2k) and
P_k'=(-I_k+J_k)/2. All ratio powers in their integration ranges are
bounded by1. This avoids large inverse radial moments.

The stream Psi=sum P_k sin(k phi) produces

    U_r=-sum k P_k cos(k phi)/r,
    U_phi=sum P_k' sin(k phi),
    U1=sin(phi) U_r+cos(phi) U_phi,
    U2=-cos(phi) U_r+sin(phi) U_phi.

These identities fix both the orientation and vorticity sign. Deriving
the modal law afresh is a diagnostic second inverse here; the principal
independent audit already uses Cartesian Duffy quadrature on the whole
plane and does not use this modal discretization.

## 3. Independent quadrature and interpolation diagnostic

Map t=1-(1+r^2/L^2)^(-1/(2b)), b>0. Then
r=L sqrt(expm1(-2b log(1-t))) and dr/dt=b(L^2+r^2)/(r(1-t)).
For every target radius, split the exact source-knot partition at that
target and apply Gauss-Legendre quadrature in t on every resulting
interval, including the last interval ending at1. Interior quadrature
nodes never evaluate infinity. This integrates the actual saved source
on all radii; it does not impose a boundary condition at finite r.
Increase quadrature order independently to assess floating-point error.
No rigorous remainder enclosure is asserted by order comparison.

The fitting lane interpolates S_k=P_k/r^{p_k}, p_k=2+(k mod2), at7
Gauss nodes separately in each t cell. Independently fit the same nodal
values as a Legendre series, not a monomial Vandermonde/Horner routine.
Let Delta denote right minus left trace at a cell boundary of radius r.
Then the ordinary piecewise velocity jumps satisfy exactly

    [U_r]=-sum k r^{p_k-1} Delta S_k cos(k phi),
    [U_phi]=sum Delta[p_k r^{p_k-1} S_k
                        +r^{p_k}(dt/dr) partial_t S_k] sin(k phi).

A nonzero first jump gives a distributional divergence measure there;
a nonzero second jump gives a curl measure. This diagnoses the ordinary
piecewise velocity actually used, not the distributional derivative of
a discontinuous stream including its singular measure.

At0 an even stream mode k>=4 with S_k(0) nonzero contributes
r^2 S_k(0) sin(k phi), which is not a quadratic polynomial. Its velocity
is not differentiable at0. For k=4 alone the discrepancy between the
diagonal directional velocity derivative and the linear map inferred
from the coordinate axes has norm8|S_4(0)|. Other even modes can also
contribute; report individual coefficients and the combined angular
linearization defect rather than attributing every defect to mode4.

## 4. Manufacture and scope

Test the integral formulas first on the separately specified smooth
stream modes P_k=r^k(1+r^2)^a, a=(2-nu-k)/2, and for k=1 subtract r.
Their exact sources follow from

    -Delta[P_k sin(k phi)]
      =-r^k[4r^2 f''(r^2)+4(k+1)f'(r^2)] sin(k phi),
    f(q)=(1+q)^a.

The subtracted r sin(phi)=x is harmonic. Thus the inverse must recover
the given relative stream and derivative. The manufacturing fields do
not solve the Boussinesq transport equations.

Production traces computed from independent near-exact nodal inverse
values isolate interpolation truncation. They are not bit-for-bit
outputs of the solver's own approximate modal quadrature. A discrepancy
smaller than our inverse quadrature uncertainty remains OPEN; a stable
nonzero discrepancy tests the interpolation of the actual source, with
that stated qualification. No measurement here establishes nonexistence.

Dependencies: product-to-sum identity, variation of parameters, harmonic
Liouville uniqueness, Gaussian quadrature and polynomial interpolation;
packet37 gives exact smooth counterexamples to the representation rule.

## 5. Between-node elliptic defect and last-cell asymptotics

For P=r^p S(t(r)), direct differentiation gives

    Delta_k P = r^{p-2}[(p^2-k^2)S+(2p+1)r t' S_t
                          +r^2((t')^2 S_tt+t'' S_t)],
    t' = r z/[b(L^2+r^2)],
    t''=z/[b(L^2+r^2)] [1-(2+1/b)r^2/(L^2+r^2)],
    z=1-t.

Indeed P'=p r^{p-1}S+r^p t'S_t. Differentiate once more,
add P'/r and subtract k^2 P/r^2 to obtain the displayed expression.
The defect of the reconstructed stream against the actual saved source
is -Delta_k P-omega_k. This is separate from any transport defect.

The last-cell interpolant is a finite polynomial in t, hence a finite
polynomial in z=1-t. If its first nonzero coefficient in z is of order
m, then P behaves as const*r^{p-m/b}; its velocity behaves as
r^{p-1-m/b}. This coefficient is not free exterior data in the canonical
inverse. For sublinear velocity one must have m>b(p-2), except that
a k=1,p=1 harmonic linear stream has constant velocity, a case not
used by this representation. In particular a nonzero S_k(1) gives an
affine velocity when p=2 or quadratic velocity when p=3; both violate
U=o(r). The polar radial component -kP/r prevents cancellation of
the leading growth within a single nonzero angular mode. Distinct
Fourier modes cannot identically cancel it.

This tail analysis treats the polynomial as a real-valued function for
0<=t<1. A floating-point implementation may clamp t or fail at still
larger radii; that is an additional numerical limitation and not an
allowed mathematical change to the inverse. Nonzero measured endpoint
coefficients with quadrature uncertainty assessed are numerical evidence
of this defect for saved states, not an interval proof about exact
interpolation of exact nodal values.
