# Two-round wall selector implementation review

Date: 2026-10-31T21:29:56Z. Actual model: GPT-6 Astra. Source and artifact inspection only; no policy calls, games, replays, tests or substantial computation. The prior proof and review were left unchanged.

Reviewed `bot_research/bots/counters/two_round_wall_selector.py`, `bot_research/experiments/validation/two_round_wall_selector_check.py`, declaration `two-round-wall-selector-001.json`, its proof/protocol, and the source of the state, normalization, replay, fresh-policy and archive helpers. Opus collaboration remains through the research team notes; this review does not claim a separate Opus assessment.

The implementation follows the proved proposed algorithm. Fresh G and L instances receive separate copied observations. Round one advances both and checks complete ordered action equality. Round two immediately selects G when any enemy building or roster entry exists; otherwise it advances both, checks equality and defers. Round three selects once if needed. Consecutive rounds and a fixed player are enforced, and an earlier G selection is permanent. Private H is retained inside L throughout. Failure recovery is not supported, consistently with the proof.

The declared baseline orientation is correct. For targets O, P and Q, the checker selects an existing target/G case with `1 - case['side'] == R_side`. Thus the original G occupies R's physical seat, and `reference_side=R_side` correctly normalizes that replay. Specifically, R seat zero uses O/G case0007, P/G case0005 and Q/G case0005; R seat one uses cases0006,0004,0004 respectively. R self uses the inherited O-self baseline entries, which actually reference the two retained G/G controls. The first ten targets retain the existing selected-member controls. The selected G specification explicitly includes guard00, and L has no override.

The branch checker derives the actual member and selection round from completed round-one and round-two enemy snapshots. It uses that observed member for fresh standalone regeneration, rather than assuming the predicted branch. Before and after selection, it compares the corresponding member's state after every call. This catches missing private H history as well as action differences. Baseline applicability is checked explicitly; a different observed member produces an inapplicable baseline rather than falsely claiming transfer.

| Claim | Static evidence and scope | Verdict |
| --- | --- | --- |
| Implementation matches the proposed prefix transitions. | Exact-list equality is checked inside the selector on each shared round; selection occurs before the first unshared decision and is permanent. | CONFIRMED under the proof's valid-stream hypotheses. |
| Fresh selected-reference actions and logical state are checked every round. | Both instances begin fresh and consume each actual observation from round one; actions must equal each other and the recorded submission. `freeze_state` recursively includes nested objects, bound-method owners, function defaults and closures. | CONFIRMED for the checker logic; empirical passage OPEN at review. |
| Complete terminal streams are checked. | Exact length `2*(rounds+1)`, round/player order, no early result, matching final non-null results, initial engine records, every original-engine round and final result are asserted. Separate replay auditing also checks rules, HP, action accounting and no continuation after termination. | CONFIRMED for successful checked streams. |
| Both physical assignments and all fourteen support entries are covered before publishing. | The publisher requires 28 cases, exactly seats zero and one for each named target, matching policy specifications, 28 valid strict conditions across 10/10/8 shards, fresh external-call totals and selected-reference-call totals. | CONFIRMED as acceptance conditions; outcomes OPEN. |
| H4 supports the stated finite-game certificate. | It requires equal paired outcomes, nonnegative R payoffs and both R/R draws. A pure-R exact rational certificate is checked on the zero-filled completion; the separate proof shows why every real skew-symmetric completion of the same support row has the same pure saddle point. | CONFIRMED conditionally; checking one completion alone would not establish the universal statement. |

Limits requiring precise reporting remain:

- `freeze_state` compares logical values, not shared-alias identity, process globals, cache state or wall-clock inputs. Unsupported values and cycles fail. The resulting receipt does not remove the proof's deadline/environmental coupling premise or establish equivalence of whole interpreter states.
- The branch checker requires `rounds >= 3`. A game ending earlier, or an action/state assertion failure, stops that shard before a successful branch receipt can be published. Such a failure must be retained and reported; this checker is not a general early-termination classifier. The declared fixed opponents are prospective conditions, not a justification to discard a failure.
- `all_passed=True` in the final receipt denotes successful audit machinery. H1-H4 are separate booleans and can be false. A non-null support certificate depends specifically on H4, not on `all_passed` alone. The prose must retain those distinctions if a hypothesis fails.
- The declaration pins current parent O/P/Q receipt bytes, proofs, declarations, selected result/replay bytes, the new Python closure, both balanced configurations and the five inherited data JSON files. It does not reverify every parent receipt's input map when declaring, nor explicitly carry the protocol153 amendment JSON and later provenance supplement. This is a remaining ancestry-verification gap, not a detected mismatch in the new records. The parent acknowledged it before this review. New branch receipts do include the new declaration and all its pins; publishing reverifies those inputs, imports audit input maps and records the final report hash. The new v2 canonicalizer and logical-state helper themselves are directly pinned.

No invalidating source defect was identified in the selector, physical-side mapping or successful-path support checks. These are source findings, not a claim that the running campaign has passed. No complete 14 by 14 measurement, unique equilibrium, held-out validation or universal best-response result follows.

Reviewed SHA-256 values:

- Selector: `cf6f23c0d9ee53973b5301646aa08032255a602ce4dafa2ab843bb34de6d7cb5`.
- Checker: `6dd3cfe7f4b6d38044dd24cd8cfe264de88fddf42c0155b80a40808650ede463`.
- Declaration: `29e11b005eeef654964a0d36a1b7b3c5732ffb6e37114695b1884acd6a600c27`.
