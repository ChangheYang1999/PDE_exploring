# Protocol164: application of the fourth-decision ambiguity theorem

Prepared UTC: 2026-10-31T22:34:53.541447+00:00. Revised UTC: 2026-10-31T22:37:35.943710+00:00.

Read PROOF.md first, this protocol second, and verification/full_check.json when it exists. The existing proof and its independent review remain unchanged. This is a post-result application on retained games, prepared before the V results are available. It does not declare or run another policy, selector or game. The declarations and checks described below are future operations, subject to source review and the root's launch declaration. A hypothesis is not a result.

## Exact retained conditions

The checker selects exactly eight distinct retained results: each arm G or U against each opponent H or V, once in each physical selector seat. It joins full policy specifications, initial state and physical seats, rather than relying on display labels alone.

G is EarlyWallGuard(witness='guard00'). U is BlindFourthRound() with no overrides. H is HPHandoff(layout='empty', growth_rounds=6, bait=[], bait_round=2, tier='tier5', factory_cap=2000, purchase_cap=1000, replan_iters=5000, deadline=12, lead_from=8), with all remaining defaults. V is FourthRoundWall() with no overrides, the literal policy pinned by protocol163. The specification strings use the constructor factories of their respective modules. The declaration records the complete strings, source closure and data hashes.

| Arm/opponent | Retained parent | Original cases | Physical selector seat |
| --- | --- | --- | --- |
| G/H | analysis/delayed_signal_ambiguity/verification/full_check.json | early-wall-transfer-00-001 case0010 and case0011 | original G candidate seat |
| U/H | analysis/blind_fourth_round/verification/full_games.json | blind-fourth-round-00-001 case0000 and case0001 | original U candidate seat |
| G/V | analysis/fourth_round_wall_counter/verification/full_games.json | fourth-round-wall-counter-00-001 case0004 and case0005 | one minus original V candidate seat |
| U/V | analysis/fourth_round_wall_counter/verification/full_games.json | fourth-round-wall-counter-00-001 case0002 and case0003 | one minus original V candidate seat |

Parent paths in this table are relative to bot_research/experiments/validation. Campaigns are under bot_research/runs/validation. Every condition uses the standard initial state, no engine seed, the development pool and the unchanged bundled rules. The original V-first win/loss labels and HP order are inverted into the selector's perspective. The engine winner is authoritative. The checker rejects duplicates, missing conditions and any disagreement among result, job and the exact policy/seat specifications. No additional conditions are substituted after inspection.

The parent audit must have completed. A failed scientific hypothesis in protocol163 is permitted and must not block extraction of an audited contrary outcome. In particular, U beating or drawing V refutes the proposed measured payoff table; it does not invalidate the conditional algebraic theorem. A missing or unauthenticated parent is an audit failure and leaves the application OPEN.

## Authentication before replay

The source-only declaration reads the three parent full receipts and their declarations. It authenticates every input_sha256, source_sha256 and retained_input_sha256 edge that they expose. It authenticates the original campaign manifest through freeze.manifest_sha256, the complete jobs file, individual job, original result, original replay, and all four original strict, replay, data and fresh audit receipts. Each selected old fresh case must contain exact outputs for both external players in every reached round. These are retained reproductions, not new calls in protocol164.

Every original freeze source is read from that campaign's original sources archive with its exact SHA256. If an older working source hash differs from today's file, resolution is allowed only to an archive path explicitly bound by a retained receipt and with the same logical suffix and exact hash. Both the logical edge and resolved archive path are recorded. Gzip fallback verifies the uncompressed hash and records the actual compressed-file hash and uncompressed length. No historical helper is silently replaced by a changed current helper. All resolved physical inputs are rechecked before publication. An additional active_source_sha256 map covers the running checker/helper closure plus G/U/H/V source roots and the five data inputs. This active map must match direct current physical bytes at declaration and at the beginning and end of check, without archive fallback. The reviewed source preparation receipt must pin that same active map. Historical archive resolution never authenticates a changed currently executing helper.

The actual policy and bundled engine source closures must also match the corresponding original freeze. The static roots explicitly include G, U, H and V; H is included despite dynamic construction inside the shadow model. The five existing exact data inputs are early_wall_guard_001.json, maze_layouts_001.json, screened_guard_001.json, screened_roster_guard_001.json and staged_guards_001.json under bot_research/bots/counters/data. Both balanced JSON copies are pinned. Every counter-data file recorded in a selected original freeze is additionally checked. The checker, active replay helper closure, original proof, source-input receipt, source preparation receipt, this protocol, proof review and designated source review are bound before execution.

Declaration invokes neither Engine nor a policy. Importing the checker's engine and audit libraries is permitted after source review; no policy module is imported by the checker. Its static source walker parses policy text without loading it. The declaration writes bot_research/experiments/validation/fourth-round-ambiguity-001.json exclusively.

## Future replay and measured hypotheses

The check command reconstructs each complete retained game with the original bundled Engine and its recorded ordered actions. This checks both initial records, every physical round pair, action acceptance, combat, income, expiry, final HP, declared round count and exact terminal boundary against the original result. No new decision is requested. Original source attestation, errors, rejections and source drift are checked independently. A failed case is retained with its diagnostic and excluded from measured payoffs. Each case receipt is written before continuing, so a subsequent failure cannot erase an earlier case result.

For the public-prefix comparison the checker separately replays the first three completed rounds of each verified retained game. It records the complete actual observations at decisions one, two, three and four, and both full round records for rounds one through three. In each fixed physical selector seat, only the two player snapshot names are changed to 'selector' and 'opponent'. Physical indices, action order, event order, rules, maps, economy, roster, combat and all other public fields remain unchanged. Observation four precedes the pending fourth-round lists. Name normalization is explicit because raw names otherwise reveal policy identity. No cross-seat identity is assumed or required by this theorem.

H1 is that all four arm/opponent prefixes agree within each physical selector seat, and that their first-three closing states have the proof's exact arithmetic: selector gold/factories/path 100/4/40, 175/9/40, 267/14/42; opponent 97/5/22, 174/9/22, 291/17/22; both HP800 with empty rosters. The checker retains full representative prefixes, hashes of every compared prefix, and the first complete-field difference for each failed comparison. An early terminal before decision four, independently established by the complete terminal replay, is a failed reaching/opening premise, not a successful shortened comparison. Unexpected reconstruction exceptions are audit errors: they do not establish a scientific counterexample, leave that prefix unknown and prevent audit completion. Verified arithmetic or complete-field differences remain contrary evidence.

H2 is the proposed measured payoff premise, in each physical selector seat: G/H=-1, U/H=+1, U/V=-1. Payoff is+1 for a selector win,0 for a draw,-1 for a loss. G/V is measured separately as q in{-1,0,1}; no q is preclaimed. Every incompatible audited outcome is retained and yields REFUTED. Missing evidence yields OPEN unless an already verified counterexample establishes REFUTED. Audit completion and H1/H2 are separate fields.

If a seat's complete measured table satisfies H2, the checker calculates the exact rational conditional certificate from PROOF.md:

    probability_G = 2/(q+3)
    probability_H_in_dual = (q+1)/(q+3)
    conditional_value = (q-1)/(q+3).

It verifies the primal and dual equalities with Fraction. For q>-1 the optimizing G probability is unique. For q=-1 every probability is optimal and the value is-1; the displayed probability is only one witness. Every deterministic member choice has worst payoff-1. All three possible q cases are checked as data-only fixtures, along with a gold-field change, action-order change, seat inversion and draw. A certificate derived from a compatible measured table still has the continuation-coupling hypothesis. A failed H1 blocks the overall measured application even if the numerical table has the displayed shape.

A final global integrity failure forces the published H1/H2 verdicts OPEN and deactivates numerical certificates, even if tentative local comparisons agreed. Those tentative observations are retained in a separately labeled field and do not establish the application. The output contains one table and certificate per physical selector seat. If q differs between seats, the checker does not silently merge or average the tables and does not claim one optimal probability for both. No stochastic selector is implemented or run. The exact conditional theorem is unchanged whether the measured hypotheses succeed or fail.

## Accounting, failure preservation and scope

Planned new games:0. Planned policy imports, constructors and decisions:0. Planned complete retained Engine replays:8. Additional opening reconstruction:at most24 replayed round steps, with attempted, completed and exact steps counted separately even if a later step raises an exception. These opening steps reuse the same recorded actions and are reported separately. There are no fresh policy or shadow-model decisions in protocol164. Source/data reads and rational calculations are not counted as policy calls.

The full receipt is verification/full_check.json; the readable measured application is RESULTS.md. The full receipt binds the readable result hash. Both are exclusive writes. Individual case receipts and timestamped command-failure receipts preserve invalid attempts; the checker never overwrites them or replaces failed conditions. It records actual timestamps and elapsed time. Failed audits are not evidence for a win, a draw, an equality or a theorem application.

The source theorem's logical-state coupling includes the correctly advanced U member and its persistent H model. Earlier protocol162/163 private audits are authenticated retained evidence; protocol164 does not freshly repeat their private transitions. More importantly, complete selected-continuation payoff reproduction under changed shadow work or machine load remains an explicit hypothesis. Finite baseline replays do not establish a universal property of time-limited planners. Even a compatible measured table supports only the restricted conditional statement about choosing G or U after their common opening, with irrevocable commitment by decision four from normalized identity-free public information. Changed openings, a third response, later commitment, reselection and side channels fall outside the claim. This is neither a population strength claim nor an impossibility result for arbitrary policies.

This protocol does not inspect reserved D, modify best.py or launch more games. All source work and any authorized later offline execution remain local. JavaScript/TypeScript, servers/listeners, RLScience or other clusters, remote compute, GPU, Lean/lake, protected writes, commits and online posting are prohibited.
