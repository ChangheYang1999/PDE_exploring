# Independent factored Cartesian high-angular weak certificate

## Statement and exact hypotheses

Use the S1-symmetric stationary equation (cX+U[rho]).grad rho-rho=0 on
R2. The exact reference R=-partial_y Delta chi and velocity
u=(-chi_xyy,chi_xxy) come from the audited immutable candidate013 with
c=4076476460239181/2251799813685248 and gamma=1/c<1. Its smooth canonical
fields have growth O(r^gamma); its exact source and forbidden sectors
must match the candidate197 audit. Let h be an S1-symmetric L2 correction
solving this equation distributionally at the same c. Require the canonical
velocity decomposition U[R+h]=u+U[h], divergence-free U[h], and
||U[h]||2<=||h||2. All weak products must be locally integrable.

For odd n>0 and integer K>=(n-1)/2, put t=r2/(1+r2), v=1-t and
phi=r v2 t^K sin(n theta). Define

    I=int F phi, F=(cX+u).grad R-R,
    M=(2c+1)phi+(cX+u).grad phi,
    Cx=phi R_x, Cy=phi R_y,
    D=||M||2+sqrt(||Cx||2^2+||Cy||2^2).

For an explicitly checked Hbar>=||grad phi||infinity, Hbar>0,

    ||h||2>=2|I|/[D+sqrt(D^2+4 Hbar |I|)].

This is a necessary correction distance, not existence. A strict rational
floor is asserted only after a positive enclosing ball and independent
candidate-level comparison. The actual application is n=21,K=522. The
all-c extension requires the separately audited canonical leading-tail chart.

## Complete weak proof

Subtract the reference equation and test first with a smooth compact cutoff
of phi. Integrating the divergence-free transport terms by parts gives

    I=int h M-int phi U[h].grad R+int h U[h].grad phi.

The origin is smooth because r^(2K+1)sin(n theta) equals a homogeneous
harmonic polynomial times a nonnegative integer power of r2. At infinity
phi=O(r^-3), grad phi=O(r^-4), while reference fields grow O(r^gamma).
Cauchy-Schwarz and the escaping-annulus L2 mass make cutoff errors vanish.
The same estimates show the displayed integrals converge. Cauchy-Schwarz
and the velocity bound give |I|<=D||h||2+Hbar||h||2^2. The positive
root yields the result. Integrating the reference transport also gives
I=-int R M, a separate numerical pairing path.

## Factored Cartesian construction

Keep t^K outside every polynomial. Polar differentiation gives

    phi_r=v2 t^K G(t)sin(n theta),
    phi_theta/r=n v2 t^K cos(n theta),
    G(t)=(2K+1)-(2K+4)t.

Cartesian conversion gives the sine amplitudes (G+n)/2 at n-1 and
(G-n)/2 at n+1 for phi_x. The cosine amplitudes for phi_y are
(G+n)/2 at n-1 and (n-G)/2 at n+1. Multiply these by every Cartesian
background velocity mode using exact sine/cosine product identities.
Multiply phi by every density derivative for Cx,Cy. The complete fields
have the form r v2 t^K sum_ell v^(ell delta/2) P_ell(t) trig(theta),
where delta=1-gamma and all P are exact rational polynomials.

The implementation checks its factored field maps coefficientwise against
the already audited polynomial constructor at K=3,n=7 after multiplication
by t^3. This detects a missing radial power in the new factoring. Evaluate
the actual n21 fields at three independent Cartesian points and compare
them with directly differentiated phi and the exact reference fields.
No peer polar implementation is executed.

## Whole-plane integrals

For either squared norm, angular orthogonality gives pi per nonzero
sine or cosine mode. Sum diagonal products and twice each unordered
cross product in the same frequency. After t=1-v, each radial moment is

    (pi/2) int_0^1 v^(1+(ell+k)delta/2)
                            (1-v)^(2K+1) P_ell(1-v)P_k(1-v)dv.

Every angular mode and radial branch cross term is retained. Outward
polynomial products and the independent Gamma-based Beta recurrence
from successor_monomial_probes enclose these moments. This differs from
the peer's t-endpoint rational recurrence with factored t^K. All exact
endpoint exponents exceed -1; positive squared norms must have at least
150 relative accuracy bits. Both I formulas use the same complete moments
with exponent ell delta/2-1 and power K+1. The direct formula uses the
complete exact Cartesian sine-n residual projection. The parts formula
uses R and M and no residual derivative.

## Independent gradient maximum in v

The angular amplitude is n v2(1-v)^K, whose maximum is at v=2/(K+2).
The radial amplitude is g(v)=v2(1-v)^K[-3+(2K+4)v]. For K>0 both vanish
at v=0,1. Dividing g'(v) by v(1-v)^(K-1) gives

    -6+(9K+18)v-(2K+4)(K+3)v2.

Check this polynomial identity exactly. Its discriminant is positive for
the specified K, and its two distinct roots lie in(0,1), as verified by
outward balls. Evaluating |g| at both roots and the angular amplitude at
its critical point bounds the entire gradient. At each radius the angular
maximum equals the larger squared radial/angular amplitude because
sin(n theta)^2+cos(n theta)^2=1. All endpoints and critical points are
accounted for. Verify every amplitude is strictly below the frozen rational
Hbar. Compare the transformed peer roots and amplitude enclosures, with
no floating numerical maximizer used as evidence.

## Source and independent acceptance

Independently bind every1922 exact canonical coefficient and c from the
peer conversion to the audited own conversion, allowing different JSON
serialization. Require identical raw hash. Freeze peer proof, code, helper,
probe, build and result hashes. Compare both pairings, both energies, M,C,D,
the gradient certificate and final radius with peer containing intervals.
The original weaker monomial denominator is also retained for calibration:
its pairing must agree and its upper D must exceed the sharper D. The
strict peer rational floor must lie below both containing radius balls.
These comparisons accept only the precisely stated necessary distance.
They do not produce a full residual norm, inverse or nonlinear closure.

The proof was written before this implementation. Dependencies are the
audited successor_weak_probes, successor_monomial_probes and Cartesian
radial Fourier constructions in this lane. Formal source means executable
exact arithmetic here; no Lean or Lake build is used.
