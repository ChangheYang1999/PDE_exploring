# Independent audit of cached logarithmic products

Status: CONFIRMED for the fixed-target cases below. A changing-target API claim is REFUTED. No infinite-order correctness theorem is inferred from these tests.

## Statement and scope

The numerical experiments' `LogFarField.step_fast2(N)` packs angular and log indices into one polynomial with a stride selected from the final target N. With that target held fixed throughout construction, its exact rational density and stream arrays agree with an independent Cartesian implementation for every order in these cases:

- delta=2/3, leading sin(theta), orders1 through30.
- delta=4/9, leading sin(theta), orders1 through30.
- delta=1/2, leading (2/3)sin(theta)-(1/5)sin(3theta)+(1/11)sin(5theta), orders1 through16.

All use the canonical normalization that the entire resonant stream coefficient has constant term zero. The arrays contain polynomials in t=log r. Thus this audit crosses several resonances and checks76 complete density/stream pairs.

## Independent method

The verifier represents radial-homogeneous terms as Laurent polynomials in the angular variable and ordinary polynomials in t. Cartesian differentiation generates the nonlinear term directly as psi_x rho_y-psi_y rho_x. The density polynomial is obtained from the finite inverse of lambda-c partial_t, and its Poisson inverse is obtained by exact triangular polynomial solution, with a separate resonant integration branch. Both original differential identities are checked exactly before comparison with the cached implementation. This path does not call its packed product or its angular recurrence.

The source modules are retained under sources/ with SHA256 hashes in verification/checks.json. The reproducible driver is ../../code/cached_log_audit.py. Actual elapsed computation was10.87225754885003 seconds.

## Changing-target counterexample

Create an exact object with delta=2/3 and leading sin(theta). Compute through order5 by calling step_fast2(5), then call step_fast2(13) on the same object. Its order6 density differs from the object that used target13 from the start. The method `_ensure_stride` initializes its stride, reversal length and packed cache only when no stride exists; it does not enlarge them when N increases. The too-small stride aliases angular and log positions.

Consequently the fixed target is a necessary API precondition for this version. A repair can either reject changes or rebuild the cache with a sufficient stride. Fresh objects loaded from coefficient checkpoints are safe if their packed cache is newly initialized for the final target. The current `run` source selects `step_fast`, not `step_fast2`; this counterexample is not evidence of corrupt production checkpoints.

## Dependencies

The stationary Cartesian identities and the exact polynomial-log inverse are established in topics01 and10. Topic33 audits the alternative per-order packed implementation. No numerical threshold or floating-point comparison is used here.
