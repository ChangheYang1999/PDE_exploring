# Final-cohort controller: protocol v2

This version retains the scientific operations and nominal caps of v1. It changes
only outer execution, failure handling and memory measurement, following the
lead's review at 2026-10-30T02:28:33Z. Version 1 remains preserved and is not
operationally admitted.

The controller holds the side execution lock from admission through all work,
audits and cleanup. Entry, preparation, computation and final audit are charged
to each operation and to the aggregate elapsed budget. A full nominal operation
cap must fit before launch. Five seconds within each operation cap are reserved
for cleanup and receipt checks. Nothing runs after the 19:00:31Z numerical cutoff.
These are admission and execution controls, not OS scheduling guarantees.

A failed, late, incomplete or unlaunched operation is OPEN. Once its identified
child tree has been cleaned up and confirmed absent, the controller proceeds in
plan order. An independent later operation can run. A complement whose primary
is not AUDITED is refused with its dependency reason. No operation is retried,
reordered or silently replaced. Individual successful operations retain their
AUDITED verdict even if another member is OPEN. A completed traversal with an
OPEN member has execution_complete=true, complete=false and cohort status OPEN.

Continuation requires the same locked file and lock ownership, unchanged exact
plan and cohort hashes, passing machine checks, remaining aggregate time and time
before the UTC cutoff. Failure of any of these checks, unconfirmed cleanup or a
termination signal aborts the cohort. A sampled RSS excess is a machine failure,
not a reason to attempt another numerical job.

All scientific work runs in one identified child tree on CPU35, at low priority,
with one numerical thread and hidden GPUs. Child RLIMIT_AS is 48 GiB of virtual
address space per process. This is not a resident-memory limit. Each poll records
the sum of sampled RSS, sum of sampled virtual sizes and maximum sampled virtual
size of one live process, including the outer controller. The RSS stop threshold
is 45 GiB. Shared pages may be counted repeatedly. No sampled maximum is claimed
as an exact peak or a between-sample bound.

The subreaper and process-descriptor cleanup preserve the v1 protections, including
identification of grandchildren which create new sessions. Cleanup occurs after
every operation, including refusals, before a later operation can begin, and again
at final exit. Failure to confirm cleanup aborts further launches. Arbitrary OS
faults or SIGKILL of the controller have no guaranteed recovery.

Before final admission, inert tests must include failure followed by independent
success, failure followed by a refused dependent complement, timeout followed by
independent success, nominal-cap refusal followed by a smaller eligible operation,
and aborts on unsafe continuation. A real legacy development evaluation must
also run under the identical child virtual-address limit and controller memory
sampling. This replay may use a qualification harness that replaces only cohort
admission and dispatch with fixed development inputs; that replacement must be
explicitly recorded, and must not relax production refusal of test cohorts.
No final entropy is drawn by this qualification. Final admission requires the
exact source-bound inert qualification and the subsequent real replay, both
reviewed by the lead. The final plan and these receipts must be bound before
final entropy.

The no-JavaScript/TypeScript, no-servers/listeners, no-RLScience-cluster, no remote
compute, single busy CPU computation and side-only-write restrictions apply.
