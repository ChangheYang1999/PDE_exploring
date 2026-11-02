# A selector after the shared G/L wall opening

Written 2026-10-31T21:02:15Z, before creation of the proposed selector module. This is a source argument and prospective experiment specification. No calls of the proposed policy or new games have been run for this argument.

Read the definition and hypotheses, then the common-prefix proof, then the finite-table prediction and prospective checks. The retained ten-policy matrix is a dependency, not a conclusion about the new policy.

## Definition and hypotheses

Let G be `EarlyWallGuard(witness='guard00')` and L be `WallSignalRepair()` with no overrides. Define O to own fresh, separate instances of both. On its round-one public observation, O advances G and L once, on separate deep copies of that observation. It requires equality of the two complete ordered action lists and raises an exception if they differ. If they agree, it returns that list. At round two, O selects L exactly when both `opponent['buildings']` and `opponent['roster']` are empty; otherwise it selects G. It advances only the selected instance from round two onward, without resetting it or changing the selection. Selection does not use the opponent's identity, pending submission, private state, or a prediction of its actual next action.

The supported input stream begins at round one of the bundled standard start: two players, 100 gold, 800 HP, no buildings, no factories and no roster, on the 12 by 12 board with spawn (0,0), base (11,11), wall cost 1 and factory cost 20. Calls have consecutive integer rounds and the same player index. Observations and rules are valid engine snapshots. Source files and data are fixed, policy instances are fresh, and outside code does not mutate their fields. Exceptions terminate an instance's supported use; retry or rollback after partial advancement is not promised. Midgame initialization and altered rules are outside this argument.

For comparisons with a standalone selected policy, also assume corresponding external inputs to its transition agree. In particular, any wall-clock deadline comparisons, global randomness or other environmental choices that affect decisions must take matching branches. To transfer an entire game, this hypothesis also applies to the opponent. Counterfactual games use identical player-name fields; a comparison to differently named retained records requires justified name normalization. The theorem below does not assume that fixed source alone makes deadline-sensitive runs identical.

## Exact first move

Both policies read the same `guard00` wall list from `bot_research/bots/counters/data/early_wall_guard_001.json`. Its ordered cells are (0,1), (1,1), then (x,1), (x,3) for x=2 through 9 in increasing order, followed by (10,3), (11,3). These are 20 distinct legal cells. A surviving route follows the axis-aligned segments through (0,0), (10,0), (10,2), (1,2), (1,4), (11,4), (11,11). It avoids every listed wall. Every prefix of the wall list also leaves this route available. None of these cells is spawn or base, and every prefix is affordable. Thus all 20 wall proposals are accepted by `td_game/actions.py`.

G's round-one branch submits this wall list, does not submit its round-three turret or round-four minion, and spends the remaining 80 gold on four factories. Its defender is not called before round five.

L inherits `WallSignalTiming(wall_count=20)`. Before replacing its opening, it advances its persistent private H model once. The fixed H parameters use the empty layout, empty bait, growth through round six, first guard on round four, gun extension on round nine, and no handoff on round one. Consequently the private prediction is five factories and has an empty roster. In `ForecastTiming`, round one is before the attack and saturation triggers. Defense against an empty roster with zero additional threat budget has zero damage and adds no construction: `packages(0, ...)` contains just the empty package. Its original opening is therefore five factories. `WallSignalTiming` verifies that these are factory actions, discards them, submits exactly the shared 20-wall list, then spends the remaining gold on four factories. `WallSignalRepair` does not alter actions before round four.

The complete ordered first moves of G and L are therefore equal under the stated standard-start hypotheses, in either player assignment. This is stronger than equality of their final round-one boards. The implementation will still check list equality at runtime so that a changed dependency or unsupported input cannot silently violate its premise.

## Conditional common-prefix theorem

Fix one player assignment, one standard initial game state, and an opponent policy. Suppose both selector calls on round one succeed and their action lists agree. Suppose the run then selects S in {G,L} on round two. Compare it with a run using a fresh standalone S against the same opponent, with the environmental coupling and public observations specified above. Then O submits the same action sequence as standalone S, and their game states and outcomes agree, for as long as the compared calls succeed and those hypotheses continue to hold.

Proof. Immediately before the first decision, O's private S instance and the standalone S instance have the same initial logical policy state. They receive equal round-one observations and matching decision-relevant external inputs. Their first transitions therefore return equal actions and produce equal corresponding private states. O returns that action list because its explicit common-prefix check succeeds. The opponent receives the same observation in both games and has matching state and external inputs, so it submits the same actions. The unchanged deterministic engine produces the same completed round-one state.

At round two O chooses S using the completed public snapshot. Its private S instance has already consumed round one exactly once. It receives the same round-two observation as standalone S and thus performs the same transition. It is neither restarted nor asked to infer a missing private history. From then on O calls only S, exactly once per consecutive round, with no reselection. Induction gives equality of the selected private policy's transitions and returned action lists, the opponent's corresponding transitions, and the engine states. This establishes the claim. O has extra bookkeeping and an unused second instance; equality of the entire O object with the standalone S object is not asserted.

The environmental premise matters. G's frozen Fortress38 and L's private H handoff to frozen Fortress34 use planners with wall-clock cutoffs. In both frozen `plan.py` files, `TIME_BUDGET` is 3.0 seconds and time comparisons can stop exploration. O's extra round-one work can alter shared-cache warmth or scheduling. Equal public inputs alone do not prove equality across arbitrary execution loads. H's parameter `deadline=12` is a round-number trigger; it is distinct from these planning time limits. Recorded reproductions can test particular executions but cannot remove the premise universally.

## Retained evidence and prediction

The ten policy identifiers and their exact definitions are those in `bot_research/experiments/validation/analysis/ten_policy_game/verification/full_games.json`. Its `RESULTS.md` supplies the existing role-normalized matrix. The following first-round replay records were inspected without policy execution:

- `bot_research/runs/validation/latest-counter-game-00-001/replays/case0000.jsonl`: C buys five factories; B has 20 walls and three tier1 roster entries.
- `bot_research/runs/validation/latest-counter-game-03-001/replays/case0000.jsonl`: D buys five factories in both assignments of its self game.
- `bot_research/runs/validation/eight-policy-extension-001/replays/case0006.jsonl`: L and G each submit the same ordered 20 walls followed by four factories.
- `bot_research/runs/validation/wall-signal-repair-001/replays/case0000.jsonl`, `case0002.jsonl`, and `case0004.jsonl`: J, H and I respectively buy five factories against L.
- `bot_research/runs/validation/screened-guard-transfer-00-001/replays/case0000.jsonl`: M has a splash turret; N has 20 walls and three tier1 roster entries. Here the retained names are `guard` and `AS1C`, with definitions confirmed in the companion result.

The branch reads any building, not only walls. In particular, M must select G despite having no round-one walls. An arbitrary empty-board, empty-roster observation need not come from a pure-factory opponent; the policy makes no identity claim from this signal.

| Opponent | Predicted selected member | Its payoff in the old matrix |
| --- | --- | ---: |
| B | G | 1 |
| C | L | 0 |
| D | L | 1 |
| G | G | 0 |
| H | L | 1 |
| I | L | 0 |
| J | L | 1 |
| L | G | 1 |
| M | G | 1 |
| N | G | 1 |

Payoff is +1 for a win, 0 for a draw and -1 for a loss from the row player's perspective. If these branches and the common-prefix coupling hold for the tested executions, O's predicted row in B,C,D,G,H,I,J,L,M,N order is [1,0,1,0,1,0,1,1,1,1]. Its payoff against uniform G/J/N is then (0+1+1)/3 = 2/3. This is a conditional transfer calculation, not a measured result for O. Both O instances should select G in self play, so the same argument predicts the old G/G draw when the coupling holds.

The old zero-value certificate concerns the closed ten-policy game. Adding O could defeat its proposed mixture without invalidating that restricted certificate. No unrestricted equilibrium or global dominance conclusion follows.

## Prospective checks and present status

H1 is that O has no loss against each of G, J and N in either physical player assignment, and has strictly positive average payoff against their uniform mixture separately in each assignment. H2 is that O has no loss against any of the ten old policies in either assignment. Both are OPEN before execution. The predicted complete row and self draws are additional falsifiable checks, not criteria to be relaxed after observing outcomes.

The prospective experiment has 22 new games: the ten old opponents and O self, each in both physical assignments, on the unchanged standard bundled engine. Before calls, pin the selector, this argument, the full transitive source and data dependencies, the exact opponent definitions and the evaluation inputs. Retain ordered actions, completed-round observations, branch traces, strict action accounting, errors, terminal outcomes and actual timing. Check round-one action equality, the branch from the actual public round-two snapshot, its permanence, and legal submissions. Replay every complete record through the unchanged engine and verify complete-stream shape and terminal status. Compare the paired physical assignments after explicit role normalization, without averaging away a seat-specific loss. Where a new history differs from the selected old member's retained history, report the first divergence and inspect timing-dependent branches rather than assuming transfer. These selected development games are neither held-out evidence nor independent population samples.

The first-move source argument is CONFIRMED under its stated fixed standard-start hypotheses. Full-game equivalence is CONDITIONAL on the stated external-input coupling. H1, H2, the predicted new row and self draws remain OPEN. At writing, no selector module yet exists and no policy calls or new games have been run by this task.

## Dependencies inspected

The argument uses `td_game/actions.py`, `td_game/balanced.json`; counter modules `early_wall_guard.py`, `wall_signal_repair.py`, `wall_signal_timing.py`, `shared_prefix_selector.py`, `stateful_public.py`, `public_factory.py`, `forecast_timing.py`, `hp_handoff.py`, `screened_guard_maze.py`, `staged_guard_maze.py`, `maze_grower.py`; the guard/layout data they read; frozen economy v2 defense and threat helpers; and frozen defense v34/v38 planners. Parent evaluation must pin the full source closure, not just this list.

The principal inspected bytes have these SHA-256 values:

| Project-relative path | SHA-256 |
| --- | --- |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/wall_signal_repair.py` | `d82b22386b5973ecfc6cbcb984eb6d91d1ca5ede4c6c16ffa693c05b32e81226` |
| `bot_research/bots/counters/wall_signal_timing.py` | `63d7681bec8ac9fb5c3855d172be8c2e3a6b3a591bdf8e746efc1d9b4e754146` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/experiments/validation/analysis/ten_policy_game/verification/full_games.json` | `1405369c8e80081e4177f74fdbffaca454c0ba7f5f5d63e301c5e1d69d343b00` |
