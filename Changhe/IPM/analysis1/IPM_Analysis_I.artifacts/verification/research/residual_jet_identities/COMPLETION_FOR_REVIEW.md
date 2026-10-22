# Completed finite algebra for review

Date: 2026-10-21. This document fixes the proposed limited conclusion;
it becomes final only after the executed audit and independent follow-up.

The two angular methods have checked all 68121 pairs and both terms.
The second method uses exact integer polynomials and verifies 71254566
coefficient equalities. It covers all j=0..260 in seven contiguous batches,
with every n=1..261 in each batch. The first method executes the current
AST index expressions and compares to integer Laurent products. All 523
scatter multiplicities match an independent counting formula: the sum
branch at index N has

    max(0,min(M+1,N)-max(1,N-M)+1)

pairs; the two difference branches have max(0,M-N) and max(0,M-N+1).
For M=260 the last allocated row522 has no exact contribution.

All261 modes and all five orders pass a separate smooth-function
calculation. One expansion first constructs A and B derivatives by their
ODE recurrences, then applies the source's binomial splitting. The other
repeatedly differentiates e^(-2t) times the raw bilinear mode product,
reducing A'=-2nA+g and B'=2nB-g immediately. The 2610 radial/tangential
identities compare every coefficient of the abstract derivatives. The
angular weight w_j remains an arbitrary scalar; its coefficient is
compared symbolically, so this is not sampling j. The actual source's
261 odd weights are checked separately. The highest R derivative is5
and highest g derivative used is3. The current source computes 30
convolutions per parent across the five orders.

The polynomial rule (D+beta)^i has been checked on every degree0..7
monomial with symbolic beta through order13, by repeated polynomial
recurrence versus the exact closed binomial formula. Source poly_deriv
also executes on a complete monomial basis in a zero-radius exact object
array interpretation. This checks its linear algebra, not its floating
radius rule. The 261 explicit reciprocal boxes for1/(4n) contain their
exact rational targets. Thirty actual binomial constants are checked
exactly. The source's local function-model products, truncations and
errors are still hypotheses.

Thirty-seven selected AST statements, their loop placement, the actual
Green input headers and both forcing call sites pass. The arrays have
T shape(7809,8,260) and A,B shape(7810,261), including matching radius
arrays. The global source default remains nder=2; both frozen forcing
versions explicitly pass the pinned imported NDER=4 and immediately read
C._last_eps from that same call. There is no assertion that the default
produces five jets. External Green bytes are hashed before and after
header reading.

The value-path convention is checked by evaluating its actual dpsi,Pn,Qn
expressions and the derivative path's order-zero prefactor expressions
on the generic ring Q[A,B,v,z], with v=e^(-t_a),z=e^(-sigma). All1305
identities hold for all261 mode numbers and arbitrary symbols A,B,v,z.
In particular dpsi=(B-A)vz/2 is the radial derivative; Qn=(B-A)v^2z^2/4.
This is a generic polynomial identity, not a rational test sample. It is
a selected-expression check, not execution of the complete cell_core
or _cell_core_deriv numerical paths.

The first review proposed a complete exact-surrogate execution of both
paths. We instead make the narrower selected-expression claim just stated.
The exact differential-algebra and monomial-basis proofs supply the
universal mathematical identities; the source checks bind only the
recorded expressions and loops. No full numerical-path verification is
inferred from that substitution. Full function-model arithmetic, data
ancestry and physical jets remain outside this result. The final wording
must not say that all source execution or all jet enclosures are verified.
