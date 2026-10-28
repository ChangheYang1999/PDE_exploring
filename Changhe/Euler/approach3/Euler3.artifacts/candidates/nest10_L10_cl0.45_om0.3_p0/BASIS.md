# Basis definition (copy of reports/CONVENTIONS.md at export time)

# Numerics lane: conventions of the primary spectral route (for the lead and the verifier)

Status: implemented and tested (tests/ directory); this file records the exact conventions used by the code so the
verifier can map coefficients to fields independently.

## Equations (Cartesian components, y in R^3)
    J y = (-y_2, y_1, 0),  J U = (-U_2, U_1, 0),  W = (c_l I - omega J) y + U,  alpha = (1 - c_l)/c_l
    R_u     = (1 - c_l) U + (W . grad) U + omega J U + grad P
    R_Omega = Omega + (W . grad) Omega + omega J Omega - (Omega . grad) U
Tested identities: curl R_u0 = R_Omega (R_u0 = R_u without grad P), div W = 3 c_l, the spiral tail
U_0 = r^-alpha F(theta, phi + (omega/c_l) log r) annihilates the linear part exactly, and flipping the sign of
either rotation term breaks that identity (tests/test_residuals.py).

## Representation
    U = curl(T y) + curl curl(S y),  no l = 0 modes (they are null), so U is exactly divergence free.
    T = sum_q T_q(r) Y_q,  S = sum_q S_q(r) Y_q,  q = (l, m, t), t = c (cos m phi) or s (sin m phi), m even by default.
Real orthonormal spherical harmonics without Condon-Shortley phase:
    Y_{l,0} = N_{l0} P_l(cos theta), Y_{l,m,c} = sqrt2 N_{lm} P_l^m(cos theta) cos(m phi), Y_{l,m,s} = ... sin(m phi),
    N_{lm} = sqrt((2l+1)/(4 pi) (l-m)!/(l+m)!).
They are evaluated as regular solid harmonics P_q(y) = r^l Y_q, exact Cartesian polynomials (recurrences in
src/bases/solid_harmonics.py), with Cartesian gradients and Hessians from exact ladder identities, so all fields
and derivatives are regular at the origin and on the axis (no 1/sin theta anywhere).

Radial functions (rho = r^2, s = sqrt(rho + R0^2), x = (s - R0)/(s + R0) in [0,1), Phi_k(x) = T_k(2x - 1)):
    T_q(r) = r^l (s/R0)^-(alpha + l)     sum_k a_kq Phi_k(x)      (untwisted)
    S_q(r) = r^l (s/R0)^-(alpha + l - 1) sum_k b_kq Phi_k(x)
Twist (same for T and S, applied to each (l, m) cos/sin pair with m > 0):
    field uses cos(m(phi + beta)), sin(m(phi + beta)),  beta(r) = omega/(2 c_l) log(1 + r^2/R0^2),
    i.e. T_q^c(r) cos(m phi) + T_q^s(r) sin(m phi) with
    (T^c, T^s)_twisted = (T^c cos(m beta) + T^s sin(m beta), -T^c sin(m beta) + T^s cos(m beta)).
Consequences: smooth at the origin (every factor is smooth in rho; x ~ rho/(4 R0^2)); U ~ r^-alpha F(theta, chi) with
chi = phi + (omega/c_l) log r - (omega/c_l) log R0 + O(r^-2) at infinity; the exterior remainder is a series in 1/r.
Known limitation: non-integer relative corrections r^-(alpha+1) (the first nonlinear correction G) and r^-(4-alpha)
are approximated algebraically by the Chebyshev series in x (truncation error ~ N^-4 in the far field).

Tail amplitudes: T_q -> t_q r^-alpha with t_q = R0^(alpha+l) sum_k a_kq; S_q -> s_q r^(1-alpha), s_q = R0^(alpha+l-1) sum_k b_kq.
    int_S2 |F|^2 dS = sum_q [ t_q^2 l(l+1) + s_q^2 ( l^2 (l+1)^2 + l(l+1) [ (2 - alpha)^2 + (m omega/c_l)^2 ] ) ]   (dilation gauge = 1)
    (F = -Lap_S2 sigma e_r + grad_S2[(2-alpha) sigma + (omega/c_l) d_chi sigma] - e_r x grad_S2 tau, SPEC 3.2; the
    (m omega/c_l)^2 term comes from the radial derivative of the twist in d_r(r S); it was missing before 2026-10-24T19:40Z,
    found by the astra review; records with gauge_version = 2 use the corrected norm, earlier ones an equivalent
    alternative dilation gauge, so dimensionless ratios are unaffected)
Phase gauge: for the (l, m) pair with the largest tail amplitude (chosen at the start, re-chosen if it decays),
the sin-type tail amplitude is set to zero.
Unknown vector z = [a (Nk x Nq), b (Nk x Nq), optionally c_l, omega].

## Index conventions in exported samples (SPEC 10)
DU[i, j] = partial_i U_j (first index: derivative direction); Omega_i = eps_ijk d_j U_k; the verifier's convention is the
transpose (partial_j U_i). Cartesian components throughout; grid arrays are indexed (radius, theta, phi, component).

## Pressure
Full-space decaying pressure from -Lap P = sum_ij d_i U_j d_j U_i by the spherical-harmonic Green's function
(src/pressure/poisson_sh.py) on the same radial nodes. Twisted frame (SPEC 5.3): every field of this representation
is, in spherical components, a function of (r, theta, phi + beta(r)), so the true-azimuth source coefficients are
f^c_lm = ftw^c cos(m beta) + ftw^s sin(m beta), f^s_lm = -ftw^c sin(m beta) + ftw^s cos(m beta) with ftw smooth in x.
The solver analyses f in the true azimuth, rotates to the twisted frame per node, factors
ftw_lm = (s/R0)^-p0 (r/s)^l_eff fhat_lm, interpolates fhat in x, and integrates the Green kernels with the
oscillating factors cos(m beta(s)), sin(m beta(s)) inside, by composite Gauss-Legendre in log s with panel phase
<= pi (in r on [0, r_0]; exterior in log s until the integrand decays below 1e-18); kernels in log space.
p0 = 2 alpha + 2. Tests: manufactured twisted sources (decay r^-alpha, m up to 6, omega/c_l up to 24): P and grad P to
1e-13 (tests/test_pressure_twisted.py); untwisted m = 0 sources 5e-15; an earlier version without the twisted frame
was wrong by 1e-3 to 1e-1 in grad P for m != 0 content (found by the independent ray-integral cross-check, SPEC 5.4,
src/pressure/ray_integral.py). Class assumption: sources must have the twisted-frame structure, which holds exactly
for products of this representation's fields. grad P from the exact radial derivative formula; grad P(0) from the
l = 1 moments. For free (c_l, omega) the kernels depend on omega/c_l and alpha and are rebuilt after accepted steps
(frozen inside an LM iteration: their parameter derivative is not in the Jacobian; recorded deviation from SPEC 4.5).

## Grid and weights
Radial nodes: Chebyshev-Gauss in x (Nr = 1.5 Nk by default); angular grid Gauss-Legendre x uniform with
ntheta = 2L+6, nphi = 4L+10 (exact for products up to degree 2L+4; the pressure source is analysed up to 2L+4).
Loss: shells = core ball [0, R0) and dyadic shells [R0 2^k, R0 2^(k+1)); each shell containing nodes has total
weight 1/N_shells; angular mean; fixed-gauge scalings (1 + r^2/R0^2)^(alpha/2) on R_u and (1 + r^2/R0^2)^(1/(2 c_l))
on R_Omega. Reported: per-shell RMS of the residual and of every term, maximum scaled residual, relative defect
per shell with zero-denominator flags, weighted RMS. Gauges enter as two extra residual rows.

## Training-only devices (acceptance always uses the unweighted SPEC diagnostics)
- nonlinear-balance reweighting: per-shell factor 1/(RMS_k(T4)+RMS_k(T5))^2, mean-normalized over nodes, frozen inside an LM
  iteration and refreshed after accepted steps (a shell rebalancing; it cannot penalize the amplitude).
- Sigma_Z constraint row: sigmaZ_weight * gauge_weight * (I/Z - sigmaZ (1 - 3 c_l/2)), I = int Omega.S Omega, Z = int |Omega|^2
  (training-node quadrature with the factored exterior); continuation target sigmaZ (exact profile: 1).
- e_F constraint row: m != 0 tail energy fraction fixed (continuation in non-axisymmetric content).
- far-field anchoring: pressure-free vorticity residual rows at far checkpoint radii (default 4096, 16384, 65536 R0; angular grid
  (L+3) x (2L+4)), fixed-gauge scaled, one shell each; they force the field beyond the last node into the exact tail form
  (removes the decoupling of the x = 1 limit F from the resolved field).
- affine-core seeds (SPEC 11 v1.5 iv) via projection of U = chi (M y - eps |y|^2 J y) + (1 - chi) U_tail onto the basis.
- exact F-gauge projection of every reported state (coefficients scaled by 1/||F||; both defects recorded).

## Optimizer
Levenberg-Marquardt, dense Jacobian by chunked forward-mode AD (torch.func.jvp under vmap), Cholesky on the
normal equations, float64 throughout. AD Jacobian checked against central differences at four step sizes and
against 4th-order differences in c_l and omega (1e-12). Manufactured recovery converges to 1e-15 in 8-10 iterations.
