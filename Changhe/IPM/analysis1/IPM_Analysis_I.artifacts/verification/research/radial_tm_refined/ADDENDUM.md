# Exact endpoint and execution conventions

This addendum resolves the pre-implementation review without enlarging
any candidate. The criterion remains OPEN until a complete run and its
independent output audit finish.

1. A producer coefficient midpoint m and radius r mean the exact real
interval [m-r,m+r], where both stored binary64 numbers are exact dyadics.
No floating addition is used for either endpoint. Its independent
remainder budget is likewise the exact nonnegative stored binary64
number. The polynomial variable is u=t-t_i, with ordinary powers u^j,
not powers of u/h. The source's psi_tms docstring and construction use
that convention. The runtime candidate, its dtype, shapes and bytes are
pinned separately on every cell.

2. In the proof's section 5, use b_i for the enlarged cell width and d
for the derivative order. The earlier H_j denotes a density mode only.
The permitted remainder schedule is K=20 at b_i=ceil(2^40 h_i)/2^40,
followed, only if needed, by K=20 at b_i=h_i. There is no automatic
increase of K or of a candidate budget. A failed enlarged test is saved.
The width guard 522 b_i<1 is a convenient preserved producer hypothesis,
not necessary for the variation-of-constants or Taylor formulas. It is
required by the second engine's present implementation, which calls
the rational exponential bracket only with an argument below1. A failed
guard cannot yield acceptance.

3. The second engine uses mpmath.iv at 180 decimal digits for directed
basic arithmetic. Its exponential enclosure is constructed without
iv.exp: for 0<=x<1, let t_j=x^j/j!, S_N=sum_(j=0)^N t_j. Then

 S_N <= exp(x) <= S_N + t_(N+1)/(1-x/(N+2)).

Indeed the ratio of every consecutive omitted term is at most x/(N+2).
Use N=64 and directed evaluation of this positive rational expression.
It has no unquantified asymptotic remainder. For general rational y in
the same-point scalar check, reduce |y| by a power of 2 until it is below
1, apply this bound, square back the recorded number of times, and invert
if y<0. All operations have positive denominators. Integer coefficient
weights stay exact until interval substitution. Arb remains an independent
first engine using its own exponential enclosures.

4. Exact rational checks require 7810 strictly increasing partition
points, consecutive parent spans with matching endpoints, exactly 7809
cells, and 0<t_(i+1)-t_i<=h_i<=b_i with E_lo>0. Every E interval is checked
against exp(t_i) with both engines. For canonical interpretation, topic99
must place the degree7 spline's ordinary Taylor polynomial in T on the
entire closed exact cell. Topic81 identifies f_n=r^2 F_n there, with
r=exp(t_i)exp(u) using this same E. The initial q values divide the same
Z=exp(2t_i). These are linkage requirements, not consequences of a shared
source hash.

5. Exact comparison of an independent dyadic endpoint m*2^e with c*eta,
eta=2^-1074, shifts m if e+1074>=0 and otherwise shifts c. Both integers
are signed; no absolute value or float conversion enters the comparison.
The audit includes zero, negative, subnormal, and below-eta endpoints.

6. The predeclared complete-cell replay seed is the exact ASCII string
'ipmA-ver/topic162/radial-refined/replay/v1'. Its initial required set is
{0,2955,7808} union the first two distinct cell indices obtained by taking
successive four-byte big-endian words of SHA256(seed) modulo7809.
Add the last completed and first uncompleted cells on each actual resume,
when present. An initial empty --resume adds no interruption neighbors.
The auditor's required set and replay's completed set must match this
union explicitly before any final publication. Fresh high-precision
particular-solution checks use all replay cells plus a reproducible
one-cell-per-257 rule, modes1,2,3,64,135,261, and every recorded worst-case
mode. This selection is supplementary to the exhaustive two-engine run.

7. In the third method, particular coefficients are rational linear
functionals of formal F symbols. Combine the homogeneous subtraction
and the exp(2u) particular contribution before interval substitution.
In particular the F contribution at j=0 is identically zero. The
nonresonant calculation and the special n=2 plus branch use real
arithmetic. There is no complex arithmetic requirement.

8. The proof review's prediction that width enlargement might fail more
often at cell7808 is exploratory only. No such failure has been observed
in this not-yet-run exhaustive checker. The three-cell topic93 K=20 run
passed the unchanged budgets at its exact widths.

9. Section8 of PROOF.md defines the permitted exact endpoint refinements.
The original 101 failed run is historical evidence only. Every new full
cell and method is recomputed in this topic.
