# Static review of the late reserved-wall counter

Reviewed 2026-10-31T21:36:07Z. Reviewer model: GPT-6 Astra, distinct from the team's Opus collaboration. This review uses source and retained-artifact reads only. No policy decisions, games, replay execution or tests were run. The S declaration and outcomes were not yet available. The author of this review also wrote the preceding informal S proof; this is a check of the implementation and evaluation against that argument, not an independent authorship claim for the proof.

The reviewed implementation matches the stated standard-start opening and reservation rule. I found no invalidating source defect. The finite outcome hypotheses remain OPEN until the declared checks finish.

## Implementation and arithmetic

**CONFIRMED by source inspection.** `LateReservedWallGuard` inherits the existing reservation mechanism, changes its own witness's wall round to three, and corrects the inherited trace to report three. `EarlyWallGuard.__init__` parses the witness JSON afresh for each instance. The mutation therefore affects neither shared data nor another guard. The round-five defender and round-four purchase branch remain inherited.

On the stipulated bundled rules, the first two submissions are five factories and four factories. The resulting gold/factory pairs are 97/5 and 174/9. In round three, the ordered 20-wall prefix and splash cost 80, leaving 94 gold. A route survives every construction prefix. After the splash, the row-one and row-three barriers force at least 31 horizontal and 11 vertical edges, and the proof's explicit route attains 42. This establishes exact path income without assuming a particular shortest-path tie break.

The inherited reservation routine applies every non-factory action to a private reconstructed player, requires the original factory actions to form a trailing suffix, and computes

    projected_gold(k) = 94 - 20k + 42 + 15(9+k) = 271 - 5k.

It starts with four affordable factories and decreases the count until the projection reaches 260. Exactly two remain, yielding 261 gold and eleven factories. Three would yield 256. No outgoing roster exists through round three, so the omitted outgoing-hit bounty is exactly zero under these hypotheses. Incoming combat does not remove this player's buildings, factories or gold. At a reached round-four decision, the inherited branch buys one tier4 and no factories. Replacing the factory suffix does not leave stale economic state: the guard reconstructs spending state from the next observation, and its defender has not yet run.

These facts are conditional on the valid standard-rule observation sequence and reaching the relevant decision. The mechanism is not proved optimal over other construction plans, arbitrary rules or arbitrary player states.

## Checks, assignments and terminal handling

**CONFIRMED by source inspection.** The prospective campaign contains ten games: S against R, L, G, B and N in both physical seats. For paired comparisons, `canonical_records` swaps player and winner identities relative to S's seat, replaces player names, removes match identity and event order, and retains actions, snapshots, combat, income and terminal results. Thus H3 concerns normalized histories, not raw named records. S/R and S/L are compared in the same physical S seat, which is the correct transfer comparison.

For both R conditions, the extra checker instantiates fresh R and standalone L, reconstructs the original engine observations, checks observation preservation, and requires both actions to equal the recorded R actions at every reached turn. It compares R's persistent L values with standalone L after each decision, checks that selection remains absent before round three and equals L thereafter, replays each recorded transition, and checks the exact final result. This exercises the already advanced L instance rather than a fresh substitute at selection. The state snapshot is a logical value comparison with the helper's established scope; it is not a comparison of module globals, object alias identity or wall-clock state.

Complete streams require exactly two records per initial/played round, ordered round/player labels, no premature result, and two matching non-null terminal results. Later opening snapshots and action lists become `None` when their rounds are not reached. H2 explicitly requires an observed round-three L selection in each R game; H4 requires the complete declared opening and the actual round-four purchase in all ten cases. Early termination therefore stays in the denominator and makes the relevant empirical hypothesis false. It does not refute a source theorem conditional on survival.

A separate limitation remains: unexpected action, state, branch or replay discrepancies raise assertions before publication. Such failures need their runner output retained and reported; the final receipt is a successful-check path, not a total classifier of every possible failure. Its `all_passed` flag concerns audit completion. H1 through H4 are separate booleans and must be read separately. The publisher's general opening description should be read with the proof's reached-round conditions and the explicit H2/H4 verdicts.

## Pins, receipts and empirical scope

**CONFIRMED for the reviewed declaration code, pending actual declaration.** It collects static Python source closure, explicit configuration and data inputs, the S proof/protocol/review, and the R final result/context supplement. It checks every declared hash before and after analysis. The final checker contains the pre-pin correction that accepts either `input_sha256` or `inputs` when importing audit receipt maps. This closes the specific data-audit map omission identified during review. The forthcoming review is now an explicit pin, as are the R result and context supplement.

Strict, engine replay, data archive and fresh policy receipts are required for both campaigns. Imported receipt input maps are rechecked, each individual result is passed through `checked_row`, and result/replay bytes enter the final input map. The exact fresh-call total is checked against twice the sum of all ten recorded round counts. The extra R and L calls have separate counters. These are finite repeated-execution checks, not independent new games or cold-runtime measurements.

The new S/R transfer claim uses newly measured S/L controls, so it does not depend on silently substituting an older L outcome. The retained R/Q documents supply source and research context; S's declaration does not itself recursively rerun their mathematical or game audits. The optional H/S mixture calculation is absent from the S publisher and remains conditional on separately validated compatible payoff premises. No conclusion about that mixture, unseen opponents or a complete enlarged payoff table follows from these ten games. Whole-game R/L transfer remains conditional on matching decision-relevant deadline branches; observed reproduction cannot remove that condition.

The protocol was recorded at 2026-10-31T21:34:45.393485+00:00. At review time it specifies all ten conditions, H1-H4, explicit early-termination treatment and separate replay-call accounting before S decisions. I have not independently established the eventual declaration timestamp, final declared byte map or any empirical S verdict.

## Reviewed byte identities

| Project-relative file | SHA-256 |
| --- | --- |
| `bot_research/bots/counters/late_reserved_wall_guard.py` | `2c862cb19d15aa563f0a30219ebd501020f75a5096045d60cf018cefdf2b2ce2` |
| `bot_research/experiments/validation/late_reserved_wall_counter_check.py` | `90e8160e148b675c43258199052f8f7796aad98852183719a0e0316e57f46f00` |
| `bot_research/experiments/validation/analysis/late_reserved_wall_counter/PROOF.md` | `e668e99e984b93c5bc615eca53305da2841320cff9a9bdf23111bc9564febdf5` |
| `bot_research/experiments/validation/analysis/late_reserved_wall_counter/PROTOCOL.md` | `07dc6cc903c8cdfaabb20d2e00157f89e82205e505204252415e7bcc32d2e985` |
