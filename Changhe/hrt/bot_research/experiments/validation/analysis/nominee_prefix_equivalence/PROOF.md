# The nominees have the same gameplay prefix through round four

## Statement and hypotheses

Let A be the exact P4TNUB instance of lead v28, and B the exact P5TNUBM instance of lead v30, with the parameter dictionaries in the nominee-handoff declaration. Start two copies of the unchanged balanced engine from the standard empty-map initial state. In both copies give each physical player the same public name, put the nominee in the same physical seat, and use the same other policy with the same initial private state. Calls occur once per round from round 1. Assume every call terminates, the other policy uses only its observations and legitimate private state, and its random choices, if any, are coupled between the two copies.

Then the returned nominee action lists, other-policy action lists, engine states and observations are identical through settlement of round 4. In particular, the other policy's observation and private state before submitting its round-5 actions are identical. No rule that uses only this gameplay history and the equal public labels can distinguish A from B before that submission. This does not say that no fixed policy can beat both nominees.

The equal-name hypothesis matters. Engine.snapshot includes the player's public name, and development runners often use the full bot specification as that name. Those named experiments can disclose identity immediately. This result concerns information from gameplay under equal labels, not secrecy guaranteed by the benchmark interface.

## Proof

The inspected source difference between v28 and v30, apart from documentation, adds two optional gates: strike_until and passive_mid_from. The tested B parameters leave strike_until=None, so the pre-insurance strike condition is false in every round. The added _quiet method is never called by that disabled branch. Thus no extra action or state update is produced there.

For B, passive_mid_from=5. At rounds 1 through 4, the passive_mid expression is false because it requires round>=5. Its guarded replacement of the threat list is skipped, and every added 'not passive_mid' conjunct is true. Deleting these inactive branches leaves the same decision program as A. Both instances have identical values for every shared parameter except passive_until: A uses 4 and B uses 5. At a round r<=4 the initial _passive guard, which tests whether r is greater than that limit, is false in both instances. The remainder of _passive uses equal parameters and observations. Its result therefore agrees whether the opponent is passive or active.

All other shared methods, imports and initial mutable fields are identical in the two inspected versions. Both use the same fixed layout and the same deterministic frozen v7 planner on the standard branch. The requested-cell invariant from ../forecast_standard_scope/PROOF.md keeps the foreign-map fallback unreachable: every building on a nominee's map comes from one of its own returned construction requests. Thus neither version calls the separate foreign planner.

Induct on completed rounds. Initially the engine states agree and all shared nominee fields agree; the two extra B parameters have the fixed inactive values just considered. Equal current observations and shared fields yield equal nominee actions and equal next shared fields. The other policy also has equal observation, private state and coupled randomness, so it returns equal actions and updates its state equally. The unchanged deterministic engine receives equal submissions and produces equal settled states. This proves the induction through round 4, and hence equality of the next observations before round-5 submissions. Applying any observation-based decision rule to equal information gives equal decisions, which proves the stated inability to distinguish.

## Verification and scope

The verifier checks the exact source hashes and parameter dictionaries, mechanically removes only the two known inactive source branches, and compares the remaining Python syntax trees. It also checks representative four-round prefixes with fresh policies on the original engine and equal labels. Those samples check the implementation; they are not the universal proof. The proof is conditional on the stated source inspection, deterministic standard planner, sequential-call protocol and equal-label information boundary. It excludes external identity knowledge, unequal names, foreign maps, skipped-call prefixes and later rounds. It makes no claim about a best response or a universally winning strategy.
