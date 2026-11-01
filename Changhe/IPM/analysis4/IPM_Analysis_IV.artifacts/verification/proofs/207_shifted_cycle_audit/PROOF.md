# Independent finite shifted-cycle diagnostics

Status: CONFIRMED for orders330 through350 and358 through365, V422. All statements remain conditional on the midpoint-reset input.

## Exact statement and scope

At delta=2/3, the numerical continuation after order329 resets the earlier coefficient balls to their midpoints. Let x_n denote the real vector of coefficients of its density or stream polynomial, indexed by logarithmic power and angular sine-mode index. This audit concerns only that conditional continuation. It does not restore the discarded input uncertainty or identify the true canonical series.

Let T shift the angular mode index upward by one, leaving the logarithmic index unchanged and inserting zeros. For either S=identity or S=T, define

    a_n(S)=<S x_(n-3),x_n>/||S x_(n-3)||_2^2,
    e_n(S)=||x_n-a_n(S)S x_(n-3)||_2/||x_n||_2,
    e1_n(S)=||x_n-a_n(S)S x_(n-3)||_1/||x_n||_1.

All vectors are zero-padded before taking these finite sums. Norms in the denominators must be certified positive. These definitions quantify a finite agreement with a shifted preceding vector. They do not define an eigenvalue of a fixed linear operator governing the nonlinear recurrence.

## Complete enclosure argument

Decode every stored dyadic ball without replacing it by its midpoint. Directed additions and products enclose the three real quadratic sums ||A||_2^2, ||B||_2^2 and <A,B>, where A=S x_(n-3) and B=x_n. A positive lower bound for the first two sums permits the directed division defining a. Compute the residual coefficient by coefficient as B-a A. Directed sums of its squares, square root, and division by the positive norm of B enclose e. Directed absolute values and sums similarly enclose e1. Dependence of a on A and B can widen the interval but cannot invalidate containment.

For the shifted case, retaining the full shifted support avoids truncating any nonzero coefficient. The implementation constructs the union of the two finite supports explicitly. Because the initial ball widths in this conditional run are small, successful narrow output bounds are possible without dropping any uncertainty. Every comparison with a printed decimal uses a stated tolerance derived from that decimal's rounding precision.

Compare the retained arrays at348,349,350 and358,359,360 with their earlier archived copies. Require exact equality of their dyadic midpoints and require the newer dyadic radii to be at least the archived radii. This permits outward rounding when a checkpoint is reloaded, while verifying that no conditional center was changed or uncertainty discarded. Count all radius changes explicitly. The full mutable checkpoint is identified by a hash, byte count and maximum order. Only the audit outputs and selected historical arrays are retained locally. Repeating all earlier-order diagnostics requires the stated external data dependency or a fresh recurrence reconstruction.

## Interpretation

Negative a_n(T) establishes a sign reversal relative to the shifted preceding vector at that finite order. Small e_n(T) establishes a small relative Euclidean residual in that comparison. Neither fact implies convergence of the multipliers, persistence of the pattern, an asymptotic expansion, or singularity locations. Topic206 supplies an exact counterexample to omitting the angular phase when inferring singularities from a shifted negative cycle.

## Outcome, 2026-10-31T15:18:19+00:00, V422

At768 bits, all348 comparisons with printed diagnostics pass across3061534 coefficient positions. The density shifted multiplier and relative residual are approximately(-0.0229280213162,0.0141312269168) at350,(-0.0235551191163,0.000560289870039) at360, and(-0.0236518887701,0.000945450592391) at365. These values do not establish a limit. The earlier348..350 arrays retain identical dyadic centers with159891 outward-rounded radii; the358..360 archived arrays are unchanged. Actual runtime41.169 seconds.
