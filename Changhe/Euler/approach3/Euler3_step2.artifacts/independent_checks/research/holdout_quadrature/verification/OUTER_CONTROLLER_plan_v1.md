# Final-cohort controller: protocol v1

The scientific evaluation and scalar-audit sources remain unchanged. A new outer
controller will hold the existing side execution lock for the complete cohort.
It will invoke a small operation worker which calls the existing preparation,
command construction and result-audit functions without entering an old wrapper's
inner lock or timer. This is necessary because several old wrapper timers omit
preparation and final auditing. Primary, far, Cartesian, vorticity, energy/helicity,
first-nonlinear and optional centered operations are supported.

The cohort plan, controller, operation worker, process-control helper, this plan,
and successful qualification record must all be bound before final entropy.
The plan fixes operation order, state identifiers, dependencies, output paths,
per-operation caps and aggregate cap. No shell commands or caller-selected
executable files are accepted in the plan. Test cohorts are always refused by
production entry points. No final entropy is drawn during qualification.

Monotonic elapsed time is charged from controller module entry, including plan
and cohort admission, setup, child evaluation, auditing and result processing.
Every operation has an elapsed cap from its own admission entry. An operation is
not launched unless its complete nominal cap fits both the aggregate remainder
and its absolute UTC cutoff, which is never later than 19:00:31Z on 30 October.
A result received after a cap is exhausted is OPEN, even if a child wrote an
apparently complete file. Five seconds of every operation cap are reserved for
cleanup and final receipt handling, and the child work deadline is shortened
accordingly. Partial files are preserved. Caps govern attempted
execution and admission; they are not an operating-system scheduling guarantee.

The controller holds the side execution lock while running or auditing any
operation. All numerical work is in one child tree on CPU35, one numerical thread,
low priority and with at most 48 GiB virtual address space. Parent monitoring is
limited to lightweight clock and process metadata checks while a child is active.
The sampled sum of controller and live-descendant RSS is checked every poll
(approximately 0.25 seconds) against 45 GiB, allowing headroom below the side
limit. Shared pages can be counted more than once; this is a conservative sampled
guard, not a bound between samples.
The controller becomes a Linux child subreaper so that grandchildren which start
new sessions and lose their immediate parent remain identifiable descendants.
Cleanup freezes identified descendants, discovers their children and signals them
through process descriptors tied to process identity, then reaps them. Failure to
establish containment or confirm cleanup aborts the cohort and leaves its result
OPEN. SIGKILL of the controller and arbitrary OS failures cannot be guaranteed
recoverable; no stronger containment claim will be made.

Qualification before admission covers rejected test cohorts, missing or changed
source bindings, stale and incomplete results, malformed plans, unmet dependencies,
resource and clock exhaustion before launch, setup and post-audit overruns,
serialization, normal completion, child failure, and cleanup of an orphaned
new-session grandchild. Tests use only local inert processes and development
fixtures. The no-JavaScript/TypeScript, no-servers/listeners, no-RLScience-cluster,
no remote compute and side-only-write restrictions apply throughout.
