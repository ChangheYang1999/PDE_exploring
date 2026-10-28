# Certified strict separation at two finite exponents

## Statement

Use the real homogeneous Euclidean Hölder seminorm on R^2 and the operators
T_xx=R_1^2+I/2, T_xy=R_1R_2, with kernels and quotient-space definitions in
`../../01_setup/PROOF.md`. Write C_alpha for either trace-free operator norm
and D_alpha for the norm of R_1^2. The same suprema are obtained on smooth
compactly supported real test functions. Then

$$C_{1/10}\le6.8771683924<7.0259799882\le D_{1/10},$$

$$C_{1/5}\le3.7712855933<3.8088065348\le D_{1/5}.$$

In particular D_(1/10)-C_(1/10)>=0.1488115958 and
D_(1/5)-C_(1/5)>=0.0375209415. The values are certified inequalities, not
approximations to exact operator norms.

## Proof and numerical certificate

The upper bounds are the V045 all-phase exterior-circle construction with
the 768-square compact-region enclosure, as recorded in
`../../data/circle_composite_upper_n768.json`.

For the lower bounds take the explicit projection witness in
`../finite_projection_witness/PROOF.md` with a=1, rho=1/6, delta=1/24, R=4096.
Its seminorm is at most the refined constant K_alpha in
`../refined_profile_constant/PROOF.md`. The one-dimensional Arb192
certificate gives K_(1/10)<=1.002471319750 and
K_(1/5)<=1.010555855930.

For each exponent the nonsingular integral is enclosed in the coordinates
u=log r and theta=t theta_max(r), using three radial patches
[delta,1/2], [1/2,2], [2,4096]. Each patch has 1024 equal u-intervals and
1024 equal t-intervals. On every rectangle, Arb160 encloses the exact
kernel, the distance to the vertical segment and both graph rays, the
piecewise clamp amplitude, and the positive Jacobian. Multiplying each
range enclosure by its exact parameter area and summing gives an interval
containing the regular integral. The first outer angular interval uses
its known endpoint pi exactly, so outward error cannot enter arccos below
minus one. The signed amplitude is enclosed by its symmetric hull when a
cell crosses the graph. No cell is discarded.

The resulting regular integrals are in
`../../data/finite_projection_fine_a10.json` and
`../../data/finite_projection_fine_a20.json`. The local leading integral,
local error, and infinite-tail error are the explicit formulas proved in
the finite-witness note. Add the local lower bound, subtract the tail
bound, add the exact identity contribution 1/2, and divide by the certified
positive upper bound for K_alpha. The interval lower endpoints rounded
down to ten decimal places are the stated D bounds.

`code/combine_finite_projection.py` checks exact row coverage from zero to
3072, parameters, source hashes, and the profile certificate before this
combination. `code/check_finite_D_certificates.py` independently recomputes
the endpoint terms with 70-decimal mpmath, checks the real Cartesian and
complex kernel formulas, and compares the regular enclosure with a
separate high-order Gaussian quadrature. All checks passed. These
floating comparisons are diagnostics; the lower-bound proof uses the
Arb range enclosures and the analytic errors.

Each witness lies in the homogeneous Hölder space, and its fixed increment
passes to compact smooth approximations by the theorem in the setup
note. Therefore these are lower bounds for the requested test-function
suprema as well. Subtracting the certified C upper bounds yields the two
positive differences above.
