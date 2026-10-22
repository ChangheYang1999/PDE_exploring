# Finite scalar inputs to the flow Taylor models

Status: proof of the finite verification criterion; its execution is initially OPEN.

## Statement and exact inputs

This result concerns the scalar operations in the frozen `cert_flow.py` and
`cert_resid.py` of topic 69. It does not establish the modal Taylor remainders,
matrix arithmetic, angular coverage, or any resulting flow inequality.

Use Q = 12, u = 2^(-53), and eta = 2^(-1074). Every stored binary64 midpoint
and radius denotes its exact dyadic rational. A pair (m,r) denotes [m-r,m+r].
`succ` is the next representable binary64 number towards positive infinity;
`pred` is the corresponding operation towards negative infinity. The finite
reconstruction uses the currently installed runtime and records its identity.
It is not evidence of the runtime used by a historical computation.

The middle partition has 7809 cells. Its exact rational points are specified
by the spans in topic 31's `partition_exact.json`. The outer partition has
8948 cells, with tau_i = 17 i/8948 and t_i = t0 + tau_i. The inner partition
has 2632 cells, with tau_i = -5 + 5 i/2632 and t_i = tmin + tau_i. The base
times t0 and tmin are the exact dyadic trial knots; their equality to the
middle endpoints is checked. These formulas follow from the frozen
`cert_green_outer.py`; finite containment of every point in the exported
input ball is checked separately. No assertion about the Green moments or
exponential-polynomial coefficients in those files follows from this check.

For each of the 19389 cells, reconstruct the following source operations:

1. h = mag(MR(tau_(i+1)) - MR(tau_i)) (middle uses t directly).
2. E = MR.from_arb(exp(t_i input ball)), with Arb precision 128, as in the
   source constructor. In the outer and inner regions the source first
   adds the base-time ball and the tau ball in Arb at precision 128.
3. I = (1/E.m, succ(E.r/mig(E)^2 + u abs(1/E.m))).
4. H_0 = 1 and H_j = succ(h^j (1+2 j u)), 1 <= j <= 26.
5. rlo = pred(E.m-E.r), rhi = succ((E.m+E.r) succ(1+h+h^2)).
6. M = MR.from_arb(hull(mu(rlo),mu(rhi))) at precision 128, where
   mu(r) = 1129/1000 + (952/100 - 1129/1000)/(1+(r/6)^4).

The finite acceptance conditions are: all values are finite, rlo > 0,
0 < h < 1/522, the exact cell length is at most h, the full exponential
of the exact exported start-time interval is contained in E, the exact
reciprocal of the entire E interval is contained in I, H_j >= h^j for
every j, exp(t_i) >= rlo and exp(t_(i+1)) <= rhi, and M contains mu over
[rlo,rhi]. We also check the scalar divisions used by the source: 1/i
for 1 <= i <= 13, 1/(4n) for 1 <= n <= 261, 1/k, and every Bernstein
ratio binom(k,i)/binom(12,i), 0 <= i <= k <= 12, with their stated source
radii. The upper triangular zero entries are exact. Here k in 1/k is the
trial parameter, whereas the integer k in the Bernstein ratio is a row index.
These are distinct uses of a letter in the source.

## Why these conditions suffice for the stated scalar claims

A finite exact rational comparison establishes membership in an interval
without a floating-point rounding assumption. In particular, if 0 < m-r,
the reciprocal image is exactly [1/(m+r),1/(m-r)], because reciprocal is
strictly decreasing on the positive real axis. Testing both rational
endpoints against I proves the reciprocal statement even if a heuristic
error estimate for the source division or square were inadequate.

For nonnegative h and an integer j, h^j is an exact rational. Comparing it
to the stored H_j proves an upper bound on tau^j throughout 0 <= tau <= h.
This check does not assume correct rounding, or any error bound, for libm
or NumPy powers. It also does not certify the distinct powers occurring
inside `tm_exp` and `ode_tm`; those remain separate obligations.

Exponential is increasing. Enclosing exp at both exact rational endpoints
of a start-time interval therefore encloses its full image. Two independent
interval implementations, Arb balls and mpmath.iv, compute these endpoint
enclosures. The audit accepts only when each complete computed enclosure
lies inside the stored E interval; overlap of the enclosures alone is not
sufficient. The endpoint comparisons for rlo and rhi are treated in the
same way. Exact rational partition comparisons prove abutment and coverage
of the three finite regions; the far and centre extensions are outside
this finite statement.

Since 952/100 > 1129/1000, differentiation gives

    mu'(r) = -4 (952/100-1129/1000) r^3 / (6^4 (1+(r/6)^4)^2) < 0

for r > 0. Hence the exact image of [rlo,rhi] is [mu(rhi),mu(rlo)]. Both
endpoints are rational for dyadic rlo,rhi. Exact rational evaluation and
fresh high-precision interval evaluation each check containment in M.

Finally, the constants and Bernstein coefficients above are rational.
Exact containment proves their use as scalar enclosures. The Bernstein
identity itself follows from
x^i = sum_(j=i)^Q binom(j,i)/binom(Q,i) binom(Q,j) x^j(1-x)^(Q-j),
which is the binomial theorem after factoring x^i. This result checks
only the rational coefficients, not the subsequent matrix product.

## Independent execution and limitations

The first checker reconstructs source scalar expressions with the frozen MR
implementation and saves every binary64 scalar, its provenance, and counts.
It checks the finite inequalities by Fraction, Arb512 and mpmath.iv180.
A separate checker imports neither the source MR class nor the first
checker. It reconstructs the exact rational partition from the source data,
reads the saved arrays once, and checks all required containments using
fresh Arb1536 and exact rational arithmetic. Source expressions and array
column meanings are recorded for an adversarial model review.

No import is a proof. Acceptance requires both complete runs, unchanged
input hashes, exact total counts, and a substantive actual Opus 5.5 review
of the proof and the implemented criteria. The final evidence must state
any excluded operation explicitly. This is a finite scalar result about
reconstructed computations, not a certificate of the full flow field or
of the historical reported aggregates.
