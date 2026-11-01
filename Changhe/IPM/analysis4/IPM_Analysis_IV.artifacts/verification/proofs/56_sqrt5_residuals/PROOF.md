# Independent interval residuals at delta = 1/sqrt(5)

Status: CONFIRMED finite validated computation. The original statement written before computation is retained in sources/certificate_statement_before_computation.md.

## Exact data and claim

Take delta = 1/sqrt(5), c = (5+sqrt(5))/4, gamma = 1-delta and f_1(theta)=sin(theta). Let rho_N and psi_N be the first N coefficients of the unique nonresonant pure stationary recursion. At the radii R listed in verification/checks.json, the artifact encloses the supremum over the full circle of R^(-gamma) times the stationary residual of (rho_N,psi_N), its first two angular derivatives, its first weighted Cartesian derivatives, and the next density increment. All assertions concern finite truncations on those circles. They do not assert an exterior convergence radius.

The input is the exact algebraic parameter, enclosed by interval arithmetic. It is neither Candidate007's stored rational parameter nor Candidate007's ten-mode input.

## Independent coefficient construction

A field r^(a-n delta) times a trigonometric polynomial is represented by the exact integer pair (a,n) for its radial exponent and a finite signed Laurent polynomial for its angular coefficients. The variable exponent is evaluated by interval arithmetic only when multiplied or divided. Thus equal exponents are identified exactly, not by overlap of floating intervals.

The representation for a physical sine polynomial f is i*f = sum_m a_m (w^m-w^(-m))/2 with w=exp(i theta). Define X = partial_x and Y = -i partial_y on these representations. For each monomial the derivatives have the usual shifted Fourier coefficients (q-m)/2 and (q+m)/2. Nonlinear forcing in the sine representation is

    X(G_i) Y(F_j) - Y(G_i) X(F_j).

The stream is obtained from the independently differentiated X(F_n) by division by m^2-(2-n delta)^2. Every divisor is nonzero because delta is irrational; the computed enclosure is checked to exclude zero. The next density is the ordered Cartesian forcing divided by (n-1)(c-1). Known exact S1 symmetry and the previously proved support bounds justify discarding forbidden modes. Interval inclusion of zero in those discarded components is an additional consistency check, not a proof that they vanish.

Arb inclusion arithmetic, starting from the exact first sine and the enclosed positive square root of5, inductively encloses the exact coefficients at every retained order. Poisson residual enclosures are checked independently. At this irrational parameter the pure potential reconstruction has no exceptional homogeneous exponent, so the finite stream and density come from the same finite potential, by the confirmed algebraic reconstruction theorem. No high-order numerical potential inversion is needed for the residual computation.

## Structural residual cancellation

The exact stationary recurrence cancels all orders through N. The full residual is therefore exactly

    R_N(r,theta) = sum_(n=N+1)^(2N) r^(1-n delta) E_n(theta),
    E_n = sum_(i+j=n, i,j<=N) [X(G_i)Y(F_j)-Y(G_i)X(F_j)].

This identity is used before interval evaluation. Computing a small residual by subtracting separately rounded order-one linear and nonlinear expressions would discard the available exact cancellation. The first remaining coefficient also satisfies E_(N+1) = N(c-1) f_(N+1), and its independently recomputed interval is checked against this identity.

On a fixed circle, the weighted residual is the real trigonometric polynomial sum_n R^(-delta(n-1)) E_n. Angular derivatives multiply its Fourier modes by the exact appropriate frequency powers. Weighted Cartesian derivatives use X or Y before radial evaluation; the same factor R^(-delta(n-1)) then remains.

## Certified supremum enclosure

For h(theta)=c_0+2 Re sum_(k>=1) c_k exp(ik theta), put D=2 sum_(k>=1) k |c_k|. Evaluate h at J equally spaced full-circle points with interval arithmetic. Every angle is within pi/J of a grid point. Hence

    max_j |h(2pi j/J)| <= ||h||_infinity
      <= max_j |h(2pi j/J)| + pi D/J.

Lower endpoints of grid magnitudes give the lower bound; upper endpoints plus the Lipschitz correction give the upper bound. This is a full-circle enclosure, unlike a sampled floating maximum. All evaluated Fourier coefficients and their exact dyadic ball encodings are retained, together with implementation and input hashes.

## Dependencies and scope

Dependencies are the independently proved Cartesian recurrence and symmetry/support bounds in topic01, the nonresonant potential correspondence, and the elementary grid estimate above. The numerical dependency is python-flint's Arb inclusion arithmetic. This is not a proof-assistant certificate. It complements the all-order convergence theorem at this parameter, but its finite small-radius observations do not improve that theorem's explicit radius.

## Completed results

The separate Cartesian recurrence was computed through161 at1024 bits. It passes all161 Poisson and stationary enclosure checks. The full-circle residual and derivative calculations used2048 angular samples plus the proved Lipschitz correction. The complete coefficient construction and all36 supremum enclosures took188.4734822907485 actual seconds, from2026-10-31T04:32:46Z to04:35:55Z.

The following bounds use directed decimal rounding and enclose ||R^(-gamma) R_N(R,.)||_infinity. They are strict positive finite-truncation bounds.

| N | R | Lower bound | Upper bound |
|---|---|---|---|
| 80 | 0.25 | 1.26281e-7 | 1.56062e-7 |
| 80 | 1 | 3.99925e-29 | 4.94430e-29 |
| 80 | 4 | 1.20563e-50 | 1.49076e-50 |
| 160 | 0.25 | 1.10038e-12 | 1.62109e-12 |
| 160 | 1 | 1.01083e-55 | 1.49041e-55 |
| 160 | 4 | 8.81669e-99 | 1.30062e-98 |

The same artifact includes the first two angular residual derivatives, R^(1-gamma)partial_x R_N and R^(1-gamma)partial_y R_N, and R^(-gamma)(rho_(N+1)-rho_N). For each of the six quantities and each listed radius, the upper bound at160 is strictly below the lower bound at80. This is a rigorous comparison of those two truncations, not an infinite-series convergence proof at these radii.

A separate cross-check compares26243 physical density and stream amplitudes through161 with the numerical experiments. All serialized ball pairs overlap, and their largest norm-scaled midpoint discrepancy is less than2.308e-253. All30 density/stream entries through order5 also overlap the previously independent exact Q(sqrt5) calculations, which included potential reconstruction. The24 overlapping sampled-value comparisons from the numerical report lie inside the full-circle certified ranges. The cross-check took1.5383393061347306 actual seconds.

The older numerical checkpoint uses rounded decimal radii for26081 entries in this prefix. Those radii are not assumed to preserve the original enclosures. The rigorous claims here use only this verification's independent exact-dyadic ball serialization; the peer data are an independent agreement check. The retained prefix, evaluation data, source hashes, exact directed endpoints and code snapshots are all alongside the proof.
