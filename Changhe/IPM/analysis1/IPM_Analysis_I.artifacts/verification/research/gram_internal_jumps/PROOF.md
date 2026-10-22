# Internal continuity of the saved C2 polynomial pieces

## Statement and hypotheses

This note fixes a finite-data test before computation. For any finite list
of disjoint intervals [a_i,b_i) with finite dyadic endpoints, and real
polynomial coefficients c_ij, define

    B(t)=sum_i 1_[a_i,b_i)(t) sum_j c_ij(t-a_i)^j,
    h(x,y)=x^2y B(log r), r=|(x,y)|.

Assume all intervals lie strictly inside (tmin,t0), with finite tmin<t0.
Interpret every stored binary64 endpoint and coefficient as its exact
rational value. No floating evaluation error changes this definition.
The following implication is the data-verification target:

If the two traces at any endpoint tstar differ by an exactly nonzero
number Delta, then h is outside the weak-gradient H1m space X of topics127
and128. Nevertheless h and all of its derivatives vanish on neighborhoods
of the two external circles r=exp(tmin), exp(t0). Thus h satisfies every
external join condition imposed only at these two circles. It also has
zero central density coefficient and vanishes in the far field.

This does not assert that any actual stored column has such a jump until
the finite check has passed. A final result must name its exact source
snapshot, column, intervals, polynomial coefficients and nonzero rational
trace difference. The final retained Gram eigenspace and singular vectors
are not stored in these inputs and will not be inferred from them.

## Proof of the implication

At tstar set R=exp(tstar)>0. The value jump in h on r=R is
R^3 cos^2(theta)sin(theta) Delta. It is nonzero on an angular arc whenever
Delta is nonzero. Near that circle the piecewise classical derivatives
are bounded. Distributional integration by parts gives its weak gradient
as the piecewise gradient plus this jump times the radial unit normal
and circle measure. This singular term is not locally L2: test against
F_d=nu(theta)phi(theta)eta((r-R)/d), where phi is smooth and supported
in a fixed-sign arc of the jump, phi>=0 is not identically zero, and
eta is smooth, compactly supported in(-1,1), with eta(0)=1. The singular
pairing is a nonzero constant, the piecewise gradient pairing is O(d),
and the L2 norm of F_d is O(sqrt(d)). An L2 weak gradient would give a
pairing tending to0, a contradiction.

The H1m weight is bounded above and below by positive constants on a
compact annulus about R, as is the extra factor r^2 on its gradient term.
Hence the contradiction excludes X. The same argument excludes any
weighted first-gradient space with a nondegenerate local weight there.
It is unaffected by the size of a nonzero Delta.

Since the whole support in t lies a positive distance from both external
joins, B is identically zero on neighborhoods of those joins. Every
classical trace derivative there is zero. If C is an exact matrix whose
rows consist only of these external trace differences, the coordinate
vector selecting this column lies in ker C. Nonzero diagonal column
scaling preserves existence of this direction in the constrained span.
An exact nullspace parametrization of the full kernel does so as well.
A subsequent eigenvalue truncation may remove it; no assertion about
that retained subspace follows without checking the actual map.

## Exact verification method

For every candidate stored polynomial column with angular index m=0,
strict interior support, finite coefficients and alpha=0, sort its piece
endpoints. The left trace at tstar is the sum of polynomials of pieces
ending there, and the right trace is the sum of constants of pieces
starting there. Missing sides contribute zero. The primary checker uses
exact rational Horner evaluation. The independent checker uses a direct
power sum after extracting each binary64 sign, integer mantissa and
exponent from the stored bits. It also reconstructs the tiny selected
coefficient record from the frozen pickle using a restricted reader.
No numerical lane function, matrix assembly, SVD, network service or
large process is executed.

Stored source is inspected as text to identify the only two join locations
and the polynomial evaluation convention. No source-text agreement is a
claim that a historical computation used the current source unchanged.
The result concerns the exact-real functions encoded in the frozen piece
records. It is not an obstruction to using continuous B-splines directly
or to rigorously reconstructing a continuous section. It is not a PDE
nonexistence theorem, a residual bound, or a decisive endpoint.
