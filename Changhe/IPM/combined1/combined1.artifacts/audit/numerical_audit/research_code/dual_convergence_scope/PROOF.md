# Agreement of two Galerkin lower bounds does not certify completeness

## Statement and hypotheses

Let H be a real Hilbert space and let V1 be a finite-dimensional subspace
of another finite-dimensional subspace V2. For f in H define
L_i=||P_(V_i) f||, where P denotes orthogonal projection. Agreement of
L_1 and L_2, even exact agreement, does not bound ||f||-L_2 or establish
that a separately known upper bound has the displayed amount of slack.
This applies to exact dual test-space bounds as well as numerical ones.

## Complete counterexample

Take H=R3 with its Euclidean norm, V1=span(e1), V2=span(e1,e2), and
f=(3/8,0,1/4). The two projections both equal(3/8,0,0), so
L_1=L_2=3/8 exactly. Nevertheless ||f||^2=13/64, strictly greater
than9/64=L_2^2. In particular ||f||>7/16 because13/64>49/256.
An arbitrary number of extra orthogonal coordinates in V2 leaves the
same construction valid. Enlarging a basis by any finite factor and
obtaining agreement to twelve decimal places supplies less information
than this exact agreement and therefore cannot prove completeness.

The general reason is the exact Pythagorean identity
||f||^2=||P_(V2)f||^2+||(I-P_(V2))f||^2. Comparing two projections does
not control the second summand. A rigorous upper estimate for the
unresolved summand, or another complete inverse calculation, would do so.

## Scope of the candidate016 notice

The frozen N3 note reports close values from two nested test families
for the first and third angular modes of the candidate016 residual. The
finite values can be checked independently and remain valid lower
bounds. The sentence inferring from this agreement that the displayed
mode-1 ratio is intrinsic Hardy slack rather than a basis defect is not
a certified consequence. The counterexample refutes that inference as
a general rule; it does not assert that the actual candidate's omitted
component is large, nor that the actual Hardy bound is sharp.

Strict nonattainment of the Hardy constant, if proved by a separate
Fourier argument, would show strict slack. It would not identify its
size from a lower bound alone. An explicit different profile having a
similar ratio is also not an upper bound for candidate016's exact norm.
Treat the observed basis stability as numerical evidence until its
unresolved component is bounded. No existing directed lower bound,
whole-plane norm certificate, correction exclusion or existence status
changes from this logical correction.

## Evidence

Freeze the dated source paragraph and verify the exact counterexample
with rational arithmetic. Read peer code as text only. Record the claim,
method, result, verdict and actual time in verdict ledger. No numerical
IPM integration is required for this scope check.
