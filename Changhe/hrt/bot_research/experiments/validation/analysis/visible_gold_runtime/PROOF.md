# Visible-gold cost in the frozen best_v9e policy

Written 2026-10-31T20:47:17.089444+00:00, before implementing or running this audit.

## Exact questions

The defense lane reports unusually slow decisions of the frozen best_v9e against its high-factory policy in x202a_fcap_vs_best9e. Select exactly the two standard-start records with factory_cap=1200, one per player assignment. Copy the original records and replays into this topic before running fresh policy calls. Regenerate the frozen best_v9e instance from round1 through round50, compare every action list with its recorded list, and replay both recorded streams through the unchanged Engine. This is a reproducibility and runtime audit of two existing games, not two new games or new held-out evidence.

H1: all100 candidate decisions agree exactly and both original-engine replays agree completely. H2: at least one of these regenerated decisions takes more than3 wall-clock seconds on an assigned low-priority core. H3: at least one takes more than3 process-CPU seconds. These are falsifiable measurements, not hardware-independent bounds. Neither output should be silently replaced by a faster retry. Record every round's public opponent gold, roster size, own splash exposure, wall time, process CPU time and action count.

At rounds10,20,30,40,50 also measure the unchanged threat-composition component in a separate fresh process, using the exact retained public observations. Report generated list counts, total type slots, maximum list length, maximum HP and component times. These calls are diagnostic, not legitimate extra turns or independent games. Do not read pending enemy actions when invoking the policy or component.

## Informal argument about the cost

Let G be nonnegative visible opponent gold, and let c be the bundled tier1 cost15. In affordable_bundles, the pass whose lead is tier1 allocates floor(G/c) copies before filling with more expensive tiers. For the current ascending costs, the remainder is less than c and cannot buy any further tier. This list is either appended or equal to an existing list that is retained. There are at most five lead passes, and the default output cap is nine, so this list is not removed by the final slice. When G>=c, threat_compositions appends the same visible active prefix to each bundle, retaining this all-tier1 suffix. Consequently its maximum output length is at least floor(G/c) plus the number of visible active entries. All sampled lists have purchase cost at most G, so that quantity is also an upper bound on their length. Thus the maximum length equals that quantity.

This proves a linear-in-G materialized list-size cost for the selected component with the stated rules and defaults. It does not prove a particular wall time, an exact asymptotic cost for the whole bot under a growing family of reachable games, or a reachable unbounded G within the50-round game. The gun_cap parameter only switches allow_guns off after the lists have been constructed. It does not cap their length. plan_defense also copies the supplied lists and obtains their maximum HP before testing whether the current splash exposure already suffices. A mature immune map therefore need not avoid this list-processing cost. Check these source statements against the pinned files.

## Evidence, dependencies and scope

The original x202a results provide provenance and the selected-condition labels. The live opponent module may have changed since those games; this audit makes no new source-equivalence claim for that opponent. Original-engine replay validates the recorded actions and result. Fresh candidate calls use the frozen best_v9e source whose hash equals the selected final bot. Its entire imported source closure, the audit source, current rule JSON and copied inputs are pinned. The final entry and poolD remain unchanged. All timing uses cores28-30 with nice19 and one thread. Use original perf_counter and process_time, without patching clocks, planners or the engine. Peak resource use remains bounded by the actual retained observations and a per-process timeout.
