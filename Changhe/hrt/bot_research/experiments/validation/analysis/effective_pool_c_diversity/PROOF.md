# Effective variation in reserved pool C

Written 2026-10-31T16:28:49.288680+00:00, after the complete-game results and before this independent trajectory audit.

## Statement and hypotheses

Let a complete log be the unchanged engine's ordered per-player records, including submitted actions, action results, combat events, snapshots and terminal result. Let N(L,s) relabel physical player s as candidate and 1-s as opponent, replace their display names with these roles, remove the match identifier and the global action-order event field, and sort the records by (round, role). All other fields and all within-record list orders remain unchanged.

For the 72 declared conditions for each of best_v9e and P5TNUBM, compute the SHA-256 digest of a canonical JSON encoding of N. Equal digests are used as a practical equality check, and the checker also compares the normalized objects when grouping. A group represents one observed complete trajectory modulo those named labels, not an independent random observation. The count of these groups is an empirical property of these logs. It is not a count of possible behaviors or a sample-size justification for confidence intervals.

## Argument

The transformation removes only the stated labels and event-order metadata. It preserves each player's ordered actions, accepted or rejected outcomes, visible state and combat records at every round. Consequently equality of normalized objects proves equality of those retained trajectories. Equality after exchanging physical player identifiers is the intended assignment-control equivalence; it does not test a new opponent. The original-engine replay audits establish separately that the recorded actions produce these states under the current engine.

A second equality is structural for two pool-C guard variants. In bots/counters/guard_geometry.py, the parameters roster, x and y are read only in the round-one branch. Both constructors otherwise create the same frozen economy17 delegate with the same default parameters. Under the pool-C continuation wrapper, policy calls are skipped during the scripted opening. The first real call is after round one. Therefore, given the same continuation observations and assuming the same deterministic delegate decisions, the two variants produce the same actions by induction: the first delegate states and observations agree, their actions agree, the unchanged engine gives the same next observations, and the induction continues. This is a conditional policy argument because any delegate wall-clock cutoff can defeat unconditional machine-load independence. Full observed trajectory equality is checked directly, without that extra assumption.

## Dependencies and scope

Dependencies are the existing strict source and replay audits, both complete pool-C logs, the unchanged normalization convention, the guard source, and the skipped-call wrapper. The script records every input digest and checks its normalized hashes against the earlier strict audit. It groups within each start and compares the two declared candidates on matched conditions. A duplicate pair found elsewhere, such as two budget-timing parameters, is an observed result unless a separate policy proof is given.

The parameter and scripted-history separation audits remain separate. A novel parameter tuple can produce behavior already represented by another tuple. This audit must not turn exact parameter non-overlap into a stronger claim of behavioral novelty. It also does not silently remove duplicate games from the published predeclared totals.
