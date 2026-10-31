# A stale log line cannot acknowledge a later closure

Statement. Consider two sequential processes sharing a configuration file C and an append-only log L. A supervisor reads C into a private value, logs a change if needed, and then installs that value as its cached permitted-resource list S. A governor reads the last change line of L, writes C = [], and returns a closure acknowledgment if the line it read ended in `-> []`. There is a legal interleaving in which the governor returns acknowledgment while S is nonempty. This remains true with atomic configuration writes and immediate log flushing.

Proof. Initially C = [4], S = [], and the last change line ends in `-> []` from an earlier closure. The governor reads that old line. The supervisor now reads C = [4], appends the change `[] -> [4]`, and installs S = [4]. The governor next writes C = [] and returns acknowledgment using the line it read earlier. At this instant S = [4], since the supervisor has not read the new C. All per-process program orders are respected. Atomicity and flushing do not invalidate this ordering. Thus an old line is insufficient. No worker launch is needed for this counterexample.

A second counterexample uses a supervisor restart. If its initial cache is loaded from C = [4] and the restart logs a `supervisor started` line but no `GPU list changed` line, a scan restricted to change lines still returns a previous `-> []`. The governor again acknowledges a closure without evidence that the restarted cache read it.

Scope and dependencies. This is a finite transition-system argument about the quoted source ordering, not a claim that the actual run exceeded its resource limit. A new acknowledgment must be causally tied to the new closure or to a documented bound that guarantees a subsequent read. Finite waiting without such a bound is not itself an acknowledgment. The verification directory binds the exact governor and supervisor sources. No formal proof assistant was run.

## A guard that omits a disqualifying input cannot certify its absence

Statement. Let a record x contain a real coordinate N_core. Define a registered exclusion E(x) by N_core < 1/100. Let a Boolean program G depend on a subset of the record coordinates that omits N_core. Suppose G(x_0) = true for some input x_0. There is a record x_1 with the same consulted coordinates for which G(x_1) = true and E(x_1) holds.

Proof. Keep every coordinate of x_0 except set N_core = 1/200. Since G does not consult this coordinate, it follows the same operations and returns the same true value. Since 1/200 < 1/100, E(x_1) holds. Consequently G(x) = true does not imply the absence of E(x). No assertion that x_1 is a realizable Euler field is needed for this interface counterexample; the proposition concerns certification from a record.

Application and scope. The captured segment_guard.py of the 2026-10-29 review has such an input omission and a baseline record returning clean=true. Other omitted criteria give analogous counterexamples. The actual saved segment-three records and their independent physical diagnostics must be evaluated separately; this argument alone does not exclude those states. Exact source and fixture evidence is in verification/SEGMENT_GUARD_v1.md and artifacts/segment_guard_audit_v1. No numerical observation is promoted to a theorem about Euler solutions.
