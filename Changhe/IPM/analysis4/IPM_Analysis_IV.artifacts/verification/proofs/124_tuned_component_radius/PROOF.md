# Componentwise constructive radii for tuned series

Status: PROVED. The complete argument and finite certificates were independently reviewed and confirmed by the theory part at2026-10-31T10:07Z. Exact hypotheses and scope remain as stated below.

## Statement

Use the tuned recurrence and majorant system of topic119 with fixed upper bounds a on the leading coefficient norm and kappa on its nonlinear constant, and a positive lower bound s on every response modulus. Require the compatibility O6=0. Write its four polynomial equations as Y=Phi(z,Y), where Y=(W,U,V,E). Set c=Phi(0,0), J=partial_Y Phi(0,Y), Q=I+J+J^2+J^3 and Y0=Qc. The matrix J is the constant strictly lower triangular matrix in topic120.

Let B be a positive vector with B>=Y0 and let z0>0. If the exact componentwise inequality

    Y0+Q[Phi(z0,B)-c-JB] <= B                              (1)

holds, then the density and stream series, with all weighted spatial derivatives, converge on every closed exterior r>=R with R>z0^(-3/2). Under amplitude scaling by epsilon, the radius becomes z0^(-3/2)|epsilon|^(3/2).

The same conclusion applies uniformly to the compatible finite-band family of topic122 when a, kappa and s are common bounds for that family. A pure potential expansion with only the exceptional finite logarithmic corrections has the same radius if topic121 is established.

## Proof

The polynomial remainder Phi-c-JY vanishes at z=0 and has nonnegative coefficients. Since J is strictly lower triangular and nonnegative, J^4=0 and Q=(I-J)^(-1) is nonnegative. The original formal equations are therefore equivalent to

    Y = G(z,Y) := Y0+Q[Phi(z,Y)-c-JY].

Every term in G-Y0 has a positive power of z. Start the formal iteration Y^(0)=0 and Y^(j+1)=G(z,Y^(j)). Nonnegative coefficients make the iteration coefficientwise increasing. The positive z factor implies that each fixed coefficient eventually stabilizes to the unique formal solution. This can also be proved by induction on the power of z: the constant term is Y0, and the coefficient of z^n depends only on lower coefficients.

For real 0<=z<=z0 and componentwise 0<=Y<=B, monotonicity and (1) give G(z,Y)<=G(z0,B)<=B. Every iterate evaluated at z0 is therefore bounded by B. By monotone convergence of the nonnegative sums, the limiting formal series converges absolutely at z0 and its component coefficients obey |Y_n|<=B z0^(-n).

The reconstruction of the original scalar majorants uses only finitely many shifts in the series index and fixed low-order coefficients. It follows that the density and stream angular norms have a common geometric bound with base z0^(-1). Their frequencies grow at most linearly with n, so every fixed spatial derivative costs only a polynomial factor in n. At any strictly smaller z disk these factors are summable. For z=r^(-2/3), this gives the stated uniform weighted derivative convergence and termwise stationary equation. Homogeneity of order n in the leading amplitude gives the scaling factor.

This is a monotone supersolution proof. It needs no contraction estimate, no extrapolated coefficient fit, and no claim that z0 is an optimal analytic radius.

## Exact applications

Take B=2Y0. Evaluate (1) by rational arithmetic on the grid z0=2^(-q) with nonnegative even q, retaining both the successful inequalities and all preceding tested failures. The following four choices are checked:

- Both algebraic roots together: a=2, kappa=10, s=1/100000, using topic120.
- First root: a=1281/1000, kappa=28/3, s=38124/10^9, using the exact minimum certificate in topic123.
- Second root: a=1647/1000, kappa=28/3, s=15683/10^7, using topic123.
- The compatible three-mode family in topic122: a=3, kappa=14, s=1/200000.

These a bounds follow from the exact isolating intervals for the two roots; the s bounds must be checked against the exact rational interval minima. All arithmetic and the polynomial maps are retained in verification. Success of this box does not assert that the preceding failed boxes preclude convergence.

Dependencies: topic119 for the majorant domination and bandwidth; topic120 for the uniform common response bound; topic123 only for the refined root-specific values; topic122 for the compatible family. The exact certificate also checks every refined input bound against the certified root intervals and response lower bounds. The successful disks and resulting strict exterior radii are:

| Input class | z0 | Sufficient exterior radius |
| --- | --- | --- |
| Both roots, common bound | 2^(-42) | R>2^63 |
| First root, refined bound | 2^(-38) | R>2^57 |
| Second root, refined bound | 2^(-34) | R>2^51 |
| Compatible three-mode family | 2^(-48) | R>2^72 |

For an amplitude epsilon, multiply the first three displayed radii by |epsilon|^(3/2). For the family, the displayed bound is for its normalized profiles as stated in topic122. Every successful inequality is strict. The largest of the four component ratios G_i(z0,B)/B_i is approximately 0.86835, 0.69743, 0.70983 and 0.72387, respectively; exact rational ratios are stored. These results improve the earlier scalar-box radii but still make no optimality claim.
