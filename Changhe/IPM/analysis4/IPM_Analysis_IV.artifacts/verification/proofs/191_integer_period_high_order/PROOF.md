# Independent Cartesian consistency audit of the high-order tuned prefixes

Status: CONFIRMED for roots1 and6 of both Q5 and Q6 through300, V386/V387/V411/V417. This is a finite consistency audit. It does not, by itself, prove an infinite convergence radius or turn residual containment into a proof of existence.

## Exact statement and hypotheses

Let Q be 5 or 6, delta=2/Q, c=Q/(Q-2), and p_n=1-2n/Q. Let b be one of the six certified real roots of the corresponding first-obstruction polynomial in topics130 or154. The exact tuned solution begins with f_1=sin(theta)+b sin(3theta); its existence and uniqueness, including the infinitely many tuned harmonics, follow from131 and the corresponding all-index response bounds. Topics180 and185 independently enclose its low-order coefficients by a separate Cartesian construction.

For a specified numerical checkpoint through order300, the present audit checks: the stored first coefficient contains this same algebraic root; all previously archived coefficients agree byte-for-byte; every stored Poisson equation has zero in every independently computed residual coefficient; and every nonlinear density equation beyond the independently reconstructed prefix does too. Directed sums also enclose each stored coefficient-vector norm. All claimed bounds are relative to the exact saved interval data. The final free stream harmonic at300 is excluded from stream-norm reports if it has not been tuned.

## Notation and independent equations

Put z=exp(i theta). Represent a real sine polynomial sum_m a_m sin(m theta) by the real Laurent polynomial F(z)=sum_m a_m(z^m-z^(-m))/2, so that the physical sine polynomial equals -i F. For a homogeneous term r^q F(z), Cartesian differentiation acts as

X_q(z^m)=[(q+m)z^(m-1)+(q-m)z^(m+1)]/2,
Y_q(z^m)=[(q+m)z^(m-1)-(q-m)z^(m+1)]/2,

where the physical y derivative is iY_q. Differentiation lowers the radial exponent by one. These identities follow by inserting cos(theta)=(z+z^(-1))/2 and sin(theta)=(z-z^(-1))/(2i) in partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r.

Write F_n and G_n for the Laurent representatives of density and stream, of radial degrees p_n and p_n+1. The Poisson equation -Delta psi=partial_x rho is equivalent to

-X_(p_n) X_(p_n+1) G_n + Y_(p_n) Y_(p_n+1) G_n - X_(p_n) F_n = 0.

Indeed, two x derivatives retain the physical factor -i, whereas two y derivatives reverse it. For velocity (-psi_y,psi_x), the nonlinear coefficient is

sum_(i+j=n) [X_(p_i+1) G_i Y_(p_j) F_j - Y_(p_i+1) G_i X_(p_j) F_j].

The stationary linear coefficient is -(n-1)(c-1)F_n. Thus the displayed nonlinear sum must equal 2(n-1)F_n/(Q-2). This formula uses every ordered pair once, with ordinary Laurent-polynomial multiplication and no sine-product routine from the producing implementation.

## Complete verification argument and scope

Exact rational radial multipliers, directed interval arithmetic and Laurent convolution enclose the residuals of the interval coefficient vectors. If a residual interval excludes zero, no selection from those input intervals can satisfy that equation. If every residual interval contains zero, the intervals pass this necessary finite consistency check; this fact alone does not establish a simultaneous exact solution in the Cartesian product of all intervals. The independent low-prefix induction and the audited producer's interval recurrence are separate sources of enclosure guarantees. They must not be replaced by residual containment.

For an interval vector (a_j), the directed sum of |a_j| encloses its sine-coefficient l1 norm. The source first harmonic is exact1; exact rational bisection of the certified isolating interval supplies a narrower enclosing ball for b. All retained low-order checkpoint coefficients are checked for identity with the archived evidence already audited in180 or185. The companion harmonic table identifies which final stream coefficient remains provisional. The source checkpoint and its producing code are hashed before checking. No coefficient radii are reset in this audit.

The large source checkpoints remain in the read-only numerical experiments. Compact hashes, counts, bounds and selected norms are retained here; reproducing the full high-order check requires the stated external checkpoint with the stated hash. This dependency is explicit. No high-order numerical finding is asserted before its dated evidence is admitted.

## Q5 root6, 2026-10-31T14:31:28+00:00, V386

All362700 Poisson residual coefficients pass through order300. Above the independently reconstructed order50 prefix, all351750 density residual coefficients from43625 ordered pairs contain zero. All58 tuned harmonic-table comparisons and59 compatibility-coordinate checks pass. The exact algebraic initial root is contained, and every previously retained coefficient is byte-identical. Maximum relative density-equation residual: [+/- 6.58e-208]. The source remains hash-identical on this replay. Runtime 866.716582744848 seconds at1536bits. Full stream order300 is excluded because its harmonic is not yet tuned.

CONFIRMED as finite equation consistency for the stored interval data. These necessary residual checks alone do not prove simultaneous solvability or an infinite radius; the separate enclosure induction and all-order theorem supply those claims.

## Q6 root6, 2026-10-31T14:31:28+00:00, V387

All362700 Poisson residual coefficients pass through order300. Above the independently reconstructed order60 prefix, all347280 density residual coefficients from43080 ordered pairs contain zero. All48 tuned harmonic-table comparisons and49 compatibility-coordinate checks pass. The exact algebraic initial root is contained, and every previously retained coefficient is byte-identical. Maximum relative density-equation residual: [+/- 1.22e-207]. The source remains hash-identical on this replay. Runtime 875.6704305042513 seconds at1536bits. Full stream order300 is excluded because its harmonic is not yet tuned.

CONFIRMED as finite equation consistency for the stored interval data. These necessary residual checks alone do not prove simultaneous solvability or an infinite radius; the separate enclosure induction and all-order theorem supply those claims.

## Q6 root1, 2026-10-31T14:58:44+00:00, V411

All362700 Poisson residual coefficients, 347280 density residual coefficients from43080 ordered products, 49 compatibility coordinates and48 harmonic-table overlaps pass. The maximum relative density residual is [+/- 4.94e-220]. Runtime 900.9072753498331 seconds. The untuned final stream harmonic at300 is excluded.

CONFIRMED as finite interval consistency, with the scope stated above.

## Q5 root1, 2026-10-31T15:14:42+00:00, V417

All362700 Poisson coefficients,351750 density residual coefficients from43625 products,59 compatibility coordinates and58 harmonic comparisons pass. The maximum relative density residual is [+/- 1.31e-208]. Runtime891.408 seconds. The final untuned stream harmonic at300 is excluded. The scope remains finite interval consistency, as stated above.
