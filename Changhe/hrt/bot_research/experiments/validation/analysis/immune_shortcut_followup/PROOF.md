# Closing the record boundary and timing gaps

Written 2026-10-31T21:01:24.918578+00:00, before this supplement's implementation and calls.

## Statement and hypotheses

Use the exact74 input histories and receipts pinned by protocol151. Let r be a history's reported last round. If its record stream contains exactly2(r+1) records, the records are ordered by round0 through r with player0 then player1, every record before the last pair has no terminal result, and both last records have the same non-null result equal to the result summary, then protocol151's initial-header and per-round replay checks cover every record and finish at a terminal state. This is a finite log-completeness statement, not a new gameplay theorem.

H1: all74 pinned streams satisfy these boundary conditions. H2: in two separate fresh processes, the research shortcut reproduces every one of the100 candidate decisions in the retained high-factory histories and each entire history replays through the original Engine. H3: the largest of those100 shortcut calls takes less than3 process-CPU seconds. H4: at seat0 round50, the parent's isolated _worst_leak call returns0 while taking more than3 process-CPU seconds without profiler instrumentation. H4 is an empirical component prediction, not a fixed runtime guarantee.

## Argument

The exact length and pair ordering place every record either in the initial pair or in one of the r round pairs already compared by protocol151. There can be no trailing unexamined record or missing pair. The non-null final result and absence of an earlier terminal result establish the claimed terminal boundary. Comparing it with the summary removes the possibility that two absent results passed an equality test. The previous fresh action and state comparisons retain their original finite scope; this supplement changes no policy or input record.

For H2, start a new Engine with the two recorded names. Add only the same three research metadata fields that the harness put in the initial records, and compare the whole initial pair. Start a fresh shortcut instance and, in order, call it once on each engine observation for its assigned side. Time the call itself without any prior eligibility call and without instantiating or invoking the parent policy. Check no observation mutation, exact recorded actions and legal sequential action application. Then feed both recorded action lists to Engine.play_round and compare the whole returned pair. At the end compare HP and the terminal result. Induction on the round gives exact reproduction of this recorded trajectory; it does not establish behavior on unseen observations.

For H4, reconstruct the seat0 round50 observation from the unchanged initial Engine and49 retained pairs, without calling a policy. Materialize the parent's exact sampled rosters outside the timed interval, then time one _worst_leak call. A separate call under cProfile records which functions account for instrumented work. Keep the profiled and unprofiled measurements distinct. Serialize only relative project paths or Python basenames, not machine paths. A zero leak is expected because the retained map's splash exposure is1550 and every catalog type has HP at most1500. The measured time explains this exact execution only.

## Method and boundaries

Pin the supplement, all151 declared inputs, all74 result receipts, the151 certificate, both150 unpaired parent timing receipts and this proof before supplement checks. Each high-factory shortcut history runs in its own process with low priority and one allowed core. No external eligibility preflight, parent policy calls or repeated synthetic strength games occur. Shared module caches may still warm naturally over the50 sequential decisions. Thus the first call is process-fresh, and later calls are ordinary stateful execution, not individually cold calls. Parent comparison uses separately measured protocol150 timings, so it is descriptive and uncontrolled across time.

The151 timing setup used an untimed eligibility preflight before both timed policies. That preflight could warm caches, in addition to the documented alternating shared-process calls. Preserve that limitation explicitly; do not rewrite the original pinned checker. H1-H4 are CONFIRMED or REFUTED by complete receipts, otherwise OPEN. A failure is retained and amended separately. No changes to the installed candidate, final selection or terminal poolD are authorized.

## Dependencies

Protocol151's PROOF.md, all input hashes and finite receipts; the original Engine and action checker; frozen best_v9e's _worst_leak and threat sampler; the research shortcut; protocol150's two unpaired parent receipts. Formal sources: none. Supplement verification belongs in verification/.
