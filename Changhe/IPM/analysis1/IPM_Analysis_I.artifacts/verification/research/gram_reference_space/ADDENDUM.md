# Source interpretation and response to the first model review

2026-10-21. Read with PROOF.md. The first actual Opus5.5 response stopped
at max_tokens and is not a completed acceptance. Its available reasoning
agrees with both analytic calculations but requests broader reference
scope and the missing ExpPolyBasis implementation. Both are addressed here.

The notation J_exp(t0) in the proof means J_R evaluated at R=exp(t0),
not a Python identifier. The frozen src__lin_assembly.py is now included:
ExpPolyBasis.eval initializes zero everywhere and adds the exponential
polynomial only on its indicated half-open pieces. Its derivative option
differentiates that polynomial within the piece. This supplies the support
semantics missing from the first review bundle. Fourteen selected AST
statements and an independent structural parse bind the assertions to the
current frozen sources. Historical execution of the large finite matrices
is not authenticated by this check.

The objection applies to every claimed X-projection onto a raw span that
contains a function with a nonzero value jump. The proof of (1) applies
verbatim to a piecewise smooth function with unequal traces: its weak
gradient contains the trace difference times the circle measure, and the
same test functions exclude a locally L2 gradient whenever that difference
is nonzero on an open arc. Thus the two J principal-cosine fields and
cos2_Jcode_Jinner have the same problem. The inner-power columns have
left trace1 and right trace0 at tmin, while the outer-power columns have
left trace0 and right trace1 at t0. For each angular mode the trace is
p cos(2m theta), not identically zero on a circle. Raw inner/outer kind
spans and raw per-mode spans containing these columns are also not
subspaces of X. The raw spline span would require its endpoint traces
to be checked separately; that check is not needed for this verdict.

The finite piecewise-gradient quadratic form is a coherent diagnostic
form on a space permitting jumps. It can define correlations there after
dependent vectors are quotiented. It is not the global weak-gradient
norm in the report's displayed definition. A remedy is to label these
numbers explicitly as piecewise-gradient Gram correlations. Alternatively
use specified continuous reference functions and project onto conforming
subspaces. A central jet alone does not specify a distinguished bounded
reference direction in the H1m norm, by the concentration theorem.

The tail and KP/TAU references do not have the deliberate unit jump of
these J definitions. If they and the retained combinations are exactly
continuous and have the stated finite tails, their X-angles are legitimate.
This conditional sentence is the scope needed here. The first review's
unqualified claim that their actual floating representations are C6 is
not adopted. Their source builds polynomials by floating spline derivatives
and discards pieces below1e-14, and no exact conformity or quadrature
certificate for them was produced in this topic. Similarly, the computed
nullspace satisfies constraints numerically; a rigorous global-H1 result
would require exact conformity or a controlled conforming reconstruction.
The existing floating diagnostic spectrum is not rejected by this topic.

The two arithmetic methods are independent expanded-polynomial/Gaussian-
rational Laurent algebra and beta-recurrence/Cartesian angular moments.
They agree exactly on1/26,-1/26,12/143,123/286 and both angular integrals.
The radial nonnegative-square identity is checked as an exact polynomial.
Nine JSON result records are checked only as reported floating records.
Their values called Xnorm2 are squared piecewise energies. The report's
5.4e9 and5.9 are approximate square roots, so there is no norm-versus-
squared-norm transcription objection in those two particular displays.

The archived H1m/NJ0 minimum singular values increase by factors greater
than7/5 between ppc2 and ppc4 or6, while the corresponding largest values
increase by factors less than11/10. These are exact comparisons of the
stored decimal records. They do not scale by a common factor. Three finite
row densities can provide evidence of stability; they do not establish
convergence of a continuum quadratic form. No new spectrum is computed,
and no finite-section or global lower bound is certified here.

An initial static-source checker expected only the first component of the
Gram return tuple and failed before writing an output. The corrected
expected statement includes len(tq). The original checker and failure
record are retained. No analytic calculation or source was modified.
