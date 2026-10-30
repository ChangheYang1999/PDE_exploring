# Complete-norm dyadic cell test for candidate 007

## Statement and hypotheses

Let \(c=4076476460239181/2251799813685248\) and
\(A=1+1/c\). Let \(F\) be the exact residual of
`C1-N1-007-d2w-j7-e2bal`, with coefficient hash
`ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`.
For \(0\leq a\leq3/2<A\), put

\[
N_a=\|(1+r^2)^{(2-a)/2}\Delta F\|_{L^2(\mathbb R^2)},\qquad
B(a)=\frac{\sqrt{8\pi}(1+c-ca)^2}{1+a}.
\]

Assume all the domain, cutoff, decay, canonical-velocity, inverse-floor and
absorption hypotheses of `NC-T-DYADIC-LAP` in the frozen `theory_v02.md`,
Section 5.2. In particular, closure in the registered
`FW-T-DYADIC-Y-v1` scheme requires

\[
5^{(a-2)/2}N_a<B(a).
\tag{1}
\]

Using only independently confirmed whole-plane norm enclosures from N4-161,
the accompanying arithmetic proves failure of (1) for every
\(0<a\leq3/2\). Its smallest certified cell ratio exceeds \(1.386\).
This is a second conditional exclusion of this sufficient scheme; it does
not prove profile nonexistence or replace any analytic inverse hypothesis.

## Continuous cell argument

The squared integrand defining \(N_a\) decreases pointwise with \(a\).
Consequently \(N_a\) is nonincreasing. The factor \(5^{(a-2)/2}\) is
increasing. Set \(z(a)=1+c-ca\). On \([0,3/2]\), \(z(a)>0\) and

\[
B'(a)=
-\frac{\sqrt{8\pi}\,z(a)\,[2c(1+a)+z(a)]}{(1+a)^2}<0.
\]

For a cell \([l,h]\) and every \(a\) in that cell,

\[
\frac{5^{(a-2)/2}N_a}{B(a)}
\geq \frac{5^{(l-2)/2}N_h}{B(l)}.
\tag{2}
\]

Use the exact partition

\[
0,\;1/5,\;1/4,\;2/5,\;1/2,\;3/5,\;3/4,\;4/5,\;1,\;5/4,\;3/2.
\]

The retained norm balls contain the actual full norms, so an outward
evaluation of the right side of (2) contains its true value. A strict
comparison of the entire resulting ball with one proves exclusion on that
cell. All ten comparisons are required; a finite list of point exclusions
alone would not cover a continuum.

The norm data include all 160 odd angular modes and all radial branch
products, with no radial truncation. Their independent Cartesian and polar
agreement was established in N4-161. This calculation checks their hashes
and exact candidate identity and does not rerun the large integral assembly.

## Lower versus upper norm enclosures

For a general input \(L_h\leq N_h\leq U_h\), a necessary-test exclusion
requires the lower quantity \(L_h\):

\[
\frac{5^{(l-2)/2}L_h}{B(l)}>1.
\]

Using \(U_h\) in this test is invalid. For example, \(F=0\) has \(N_a=0\)
for every \(a\), and the interval \([0,1000]\) is a valid enclosure of
every such norm. Substitution of its upper endpoint into the frozen N3
checker reports exclusion at \(a=0\) and on \([0,1/5]\), although (1)
holds strictly for the zero residual.

This counterexample concerns the generic input logic of that checker.
The actual candidate007 intervals are much tighter, and the independent
calculation here proves all ten exclusions using valid containing norm
balls. The bug therefore does not undo the candidate-specific conclusion.

## Evidence and dependencies

The proof precedes execution. Frozen inputs include the N3 checker, its
dated note, the published theory version, and the accepted N4-161 comparison.
One verification record retains the exact counterexample and the frozen
checker's stdout. A second retains all ten outward cell ratios and eleven
point ratios, their input hashes, and strictly downward decimal floors.
No inference about an exact solution is drawn from a numerical loss.
