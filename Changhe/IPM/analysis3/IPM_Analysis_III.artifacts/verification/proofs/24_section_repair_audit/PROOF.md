# Repaired test space and remaining Phase2 certification defects

## Object and claims

This audit applies only to the exact files captured at the real time in
`evidence/snapshot.json`, 2026-10-28T02:08:51.258836+00:00. It does not
silently apply to later revisions. The original modal NPZ supplies the
angular coefficients used in the independent check. No new finite
singular value or off-basis norm is certified here.

## Confirmed repairs

`TestSplines` now keeps indices1 through nb-2. For a degree7 clamped
B-spline basis, only the first spline is nonzero at the left endpoint and
only the last at the right endpoint. Every retained spline is continuous
on the finite interval, vanishes at both endpoints, and is piecewise
smooth with square-integrable derivative. Its zero extension therefore
belongs to global H1. The finite endpoints have finite positive weights,
so the same statement holds in the specified weighted forcing norm.
The exact small-mesh check independently confirms the retained indices,
the two zero endpoint values and the absence of infinite-cell pieces.

Both `certify.py` and `offbasis.py` zero the two discarded rows in B, BK
and BT, zero their Gram row and column, and put1 on each discarded Gram
diagonal. This is exactly the orthogonal direct sum of the retained test
Gram with an artificial identity block whose data rows are zero. Its
quadratic projection expression is the expression on the retained test
space. Thus this repair restores the interpretation invalidated in V020.
It does not verify any of the individual integral entries.

`green_A_on_cell` now uses the canonical primitive directly on the inner
half-line. If fhat is a sum of e^(e sigma) times polynomials and
lambda=2n+4+e>0, the primitive from minus infinity is e^(lambda sigma)
S(sigma), where S'+lambda S is the polynomial. Multiplication by
exp(-2n sigma) gives the stored term. There is exactly no free
exp(-2n sigma) component. The supplied boundary-value comparison is a
consistency check, not the definition of that zero coefficient.
The independent model fhat=1,n=1 gives exactly the sole exponent4,
with coefficient enclosing1/6. The outer B primitive likewise has no
free exp(2n sigma) component; fhat=exp(-3sigma),n=1 gives the sole
exponent1 with coefficient1. Both checks pass.

The TAU docstring now explicitly defines the truncated angular direction.
This is a permissible chosen direction. It remains different from the
full product Theta_0 cos(2theta); no assertion of equality is restored.

## The aggregated angular direction is lost in a tail-bound term

`Column` supports a multi-mode density. Its exact factor coefficients are

 Pcol_j=sum_m P_jm coef_m,

and its velocity is computed from these coefficients. `Section` now
represents all of KP, and all of the defined TAU direction, as one such
column each, with the label m=0 and a nontrivial coef dictionary.

However, `run_tailbound2.py` workerB reconstructs Pj as P_j0 for the
background-velocity-on-column part. It does not use `colobj.Pcol`. That
replacement is false. A single input cos(8theta) already gives sine
indices2,3,4,5 with coefficients -1/8,-1/8,1/8,1/8, whereas P_j0 has only
indices0,1. With a background velocity of angular index1, the omitted
products feed higher output modes even when the wrong P_j0 expression
feeds none of them. This is an error in the algebraic object being
bounded, independent of rounding accuracy.

The original modal leading tail has259 nonzero sine coefficients with
j>=2. All259 are absent from the wrong m=0 lookup. The independently
computed first missing coefficient is

 Pcol_2=-545034991089349/604462909807314587353088.

The scalar normalization repair changes only angular mode0 and does not
change this coefficient or the other j>=2 values. Thus the discrepancy
applies to the actual exact tail, not just a synthetic test. The repair
is to use the full Pcol dictionary consistently in this part as is
already done in the exact operator's transport-self calculation.
No conclusion that the final numerical bound is necessarily too small
is needed: its claimed term-by-term proof currently bounds a different
expression and is invalid.

## Nearest rounding is not outward rounding

For an exact nonnegative ball v=1+2^(-54),

 arb(float(v.upper())).sqrt()=1 < sqrt(v).

This is the expression used by `offbasis.py` t_of. The equality and strict
inequality are independently checked at256 bits. Similarly the infinity
norm routine returns1 for the one-by-one exact matrix[v], so that return
value is not an upper bound. Substitution of such a value into
1/sqrt(1-nE) is not a rigorous norm comparison. The final conversion of
an upper endpoint to a JSON float also requires outward rounding.

There is a useful distinction: a nearest-rounded nonnegative number
strictly less than the exactly representable threshold1 could not have
come from a number >=1. Thus the strict boolean test used for positive
definiteness is still safe under ordinary finite nearest rounding. This
specific rounding counterexample refutes the quantitative upper-bound
interpretation, not that boolean threshold test.

For a signed ball p, abs(p.upper()) need not bound abs(p). For example
p centered at-1 with positive radius has the larger absolute value at
its lower endpoint. This is checked independently and matters when the
aggregate Pcol coefficients are used. Take abs(p).upper() instead, then
round outward if converting to a floating point bound.

The tail driver includes multiplicative safety factors. A complete proof
of that route must count every unfudged addition and multiplication,
including `np.add.at` and the final reduction, and treat subnormal and
underflow cases. A nearest conversion of the exact positive number
2^(-1100) is zero; a later finite multiplicative inflation cannot repair
that underflow. This audit does not assert that this toy value controls
the actual final bound. It shows why the safety-factor claim needs a
range and operation-count proof or replacement by direct interval
arithmetic. That issue remains open at this snapshot.

## Scope of the identity test and the final certificate

The latest identity test records whether difference balls contain zero,
but still does not assert success. A fixture made of rounded coefficients
is not exactly normalized; its strain defect must not be treated as an
exact-trial defect. Conversely a small midpoint difference alone does not
verify an identity. No new full-trial matrix or off-basis certificate is
available in this snapshot. After these repairs, entries, compensated
half-line norms, angular tails, Gram positivity and outward scalar
outputs must be checked against one fixed set of inputs and code hashes.
The analytic complement inverse is an additional theorem and is not
supplied by any finite-section result.
