# A selector after one or two shared G/L decisions

Written 2026-10-31T21:25:58Z, before the proposed R implementation or any R decisions. This is an informal source proof and a prospective, selected-development prediction.

Read the definition and hypotheses, then the two prefix lemmas, the state-coupling theorem, the retained predictions, and the conditional finite-game certificate. Implementation validation and new outcomes are open.

## Definition and hypotheses

G denotes `EarlyWallGuard(witness='guard00')`; L denotes `WallSignalRepair()` without overrides. R owns fresh, separate instances of both. A public presence signal means that either the opponent's `buildings` list or its `roster` list is nonempty. Any building counts, including a turret without walls. An inactive roster entry also counts; this is a list-presence test, not an active-wave test.

R has the following proposed transitions.

1. In round one, call each member exactly once on separate deep copies of the public observation. Require equality of the complete ordered action lists, then return that common list.
2. In round two, if the presence signal holds, select G permanently, call the already advanced G once, and return its actions. Otherwise call both already advanced members once on separate copies, require exact ordered-list equality, return their common list, and defer selection.
3. In round three, if selection was deferred, select G exactly when the current presence signal holds, and L otherwise. Call the selected, already advanced instance once. Thereafter call only that instance once per round, with no reset or reselection. A round-two G selection remains G.

Use the bundled standard start: two players, 100 gold, 800 HP, zero buildings, factories and roster; a 12 by 12 board with spawn (0,0), base (11,11), wall cost 1 and factory cost 20. Calls begin at round one, have consecutive integer rounds and retain the same player index. Rules and observations are valid unchanged-engine snapshots, and the game has reached each decision discussed. Source/data and default parameters are fixed. External code does not mutate owned policy fields. A failed call or failed equality check ends supported use of the instance: no retry or rollback after advancing only one member is promised. Midgame initialization and modified rules are outside the claims.

The entire-game comparison below additionally couples all decision-relevant external inputs to each corresponding selected-member and opponent transition. Wall-clock branches, random choices and effects of shared global or cached state must agree whenever they can change decisions. Corresponding public observations, including names, are equal. Using differently named retained histories therefore requires a separately justified normalization. Fixed source and equal public inputs alone do not imply matching deadline branches.

## First shared decision and round-two gold

`early_wall_guard.py` and `wall_signal_timing.py` both read the guard00 witness in `bot_research/bots/counters/data/early_wall_guard_001.json`. Its ordered wall cells are (0,1), (1,1), then (x,1), (x,3) for x from 2 through 9, followed by (10,3), (11,3). They are 20 distinct nonterminal cells. The axis-aligned route through (0,0), (10,0), (10,2), (1,2), (1,4), (11,4), (11,11) avoids every wall. Thus every prefix preserves a route; every prefix is affordable. `td_game/actions.py` consequently accepts the complete ordered list.

G submits these walls in round one, skips its round-three turret and round-four minion branches, and buys four factories with the remaining 80 gold. Its frozen defender is first called in round five.

L first advances its private persistent H model. Its fixed parameters in `shared_prefix_selector.py` specify empty layout, empty bait, growth through round six, factory cap 2000, lead trigger from round eight, handoff round twelve, and no panic trigger. `screened_guard_maze.py`, `staged_guard_maze.py` and `maze_grower.py` consequently make its first prediction five factories, with no roster or guard. `forecast_timing.py` has attack round three and saturation no earlier than round twenty. Its defense call has empty predicted active roster and additional threat budget zero. In frozen economy v2, `threat.packages(0, ...)` is just the empty package; `fastsim.simulate` creates no minions and yields zero damage; `defense_plan.defend` therefore performs no construction. The original L first move is five factories. `WallSignalTiming` verifies that each action is a factory purchase, discards that list, and submits the shared 20 walls followed by four factories. `WallSignalRepair` makes no action change before round four. The complete returned lists are equal. The private H transition is retained despite replacing its predicted-policy user's original first action list.

The final wall map has shortest-path length 40 edges. Any route must reach row one at x at least 10, then row three at x at most 1, before reaching base x=11. Its horizontal steps are at least 10+9+10=29 and its vertical steps at least 11. The displayed route attains 40. This lower bound and witness do not rely on which equal-length path the bundled search returns. By `td_game/engine.py`, income is path edges plus 15 per factory plus outgoing-hit bounty. R's own roster is empty, so its outgoing bounty is zero. After spending all 100 gold, it receives 40+4*15=100 gold. Incoming combat can affect HP but does not remove these buildings, factories or gold. Therefore every reached round-two decision has the same 20 own walls, four own factories, empty own roster and exactly 100 gold.

## Second shared decision under the empty signal

Suppose the completed round-one opponent snapshot has no buildings and no roster. This is the only case in which R advances both members at round two. G has no scheduled wall, turret or minion action in that round, and buys exactly five factories with its 100 gold.

L's `PersistentFactoryModel` has consumed exactly round one, so round two is a valid next call. `ForecastTiming.predict` changes the copied observation's player to the opponent and passes that current public snapshot to the same private H object. H is not reset, and does not substitute a privately imagined factory count for the observed one. Neither handoff trigger can fire in round two: the round deadline is 12, the lead condition starts at 8, and panic is disabled. Its empty-layout opening has no round-two construction, empty bait, and no guard until round four. It proposes only affordable factories. The standard completed round-one state cannot approach its cap of 2000 factories. Its legal-action filtering adds no roster.

The predicted state therefore still has no active roster. The same zero-threat defense argument gives L no defensive action or expense. Round two precedes its round-three attack and all saturation and repair branches. The remaining factory loop has cap 80, which exceeds the five affordable factories. L consequently returns exactly five copies of `{'op': 'buy_factory'}`, equal to G's ordered list. Its private H wrapper now has `last_round=2` and the same opponent player index as on its first call.

This proves the proposed second equality test under its stated empty-signal hypotheses; it makes no claim about G/L equality in round two when the presence signal holds. Buying these five factories leaves nine factories and zero unspent gold; the reached completed round-two own state has 40+9*15=175 gold and still no outgoing roster. The opponent's round-two submission was hidden during this decision. It can now create the presence signal observed in round three, without affecting the proved round-two action equality.

## Conditional selected-member state theorem

Let a successful run select S in {G,L} at round tau, where tau is two or three. Under the standard-start and external-input coupling hypotheses, compare R against a fixed opponent with a fresh standalone S against the same opponent. Then the selected S's corresponding private state, its complete submitted action sequence, the opponent's transitions, and the engine history agree through all successful coupled rounds.

Proof. Before round one, the private S instance and standalone S have equal initial logical state. They consume equal observations and matching external inputs, so their corresponding state transitions and actions agree. R returns S's action list because the explicit common-prefix check succeeds. The opponent has equal observations, state and decision-relevant inputs, and returns equal actions. The deterministic unchanged engine produces equal completed states.

If selection occurs in round two, the already advanced S consumes that equal round-two observation, with no missing call or reset. If selection is deferred, the same argument applies to the shared round-two decision: both members are advanced exactly once, and equality with the returned list is checked. At round three the selected S has therefore consumed exactly rounds one and two on its standalone history. Starting at the selection round, R advances only that S once per consecutive round. Induction proves equality of corresponding selected-member transitions, opponent transitions and engine states. No equality between G's state and L's state is needed or claimed, and R's unused member and bookkeeping are not part of the standalone state comparison.

In particular, an L selection at round three preserves both prior private H transitions and the persistent model's consecutive-call invariant. A G selection after deferral preserves G's own prior traces and leaves its defender uncalled before round five, as in standalone G. No equality of G's and L's round-three actions is asserted: their different turret and attack decisions are precisely why selection must occur before that decision.

G's frozen Fortress38 and L's private H handoff to frozen Fortress34 use three-second planning cutoffs in their frozen `plan.py` sources. H's parameter `deadline=12` is a round trigger, distinct from those elapsed-time limits. The shared early factory paths do not take those planner deadline branches, but extra unused-member work can affect later scheduling or cache warmth. Thus the prefix lemmas establish the exact early actions, while arbitrary-load, cross-execution whole-game equivalence remains conditional. Fresh empirical regeneration can establish equality for the measured executions; it cannot eliminate that universal limitation.

## Retained observations and conditional new row

The old identifiers B,C,D,G,H,I,J,L,M,N are defined by the retained ten-policy certificate. O is `WallPrefixSelector`; P is `DelayedWallGuard`; Q is `ReservedWallGuard`. Only existing records and sources were inspected here, without policy decisions or engine reexecution.

Under `bot_research/runs/validation/wall-prefix-selector-00-001/replays/`, case0000/0001 are O/B, case0002/0003 O/C, case0004/0005 O/D and case0006/0007 O/G. The corresponding `wall-prefix-selector-01-001` cases are O/H, O/I, O/J and O/L. Under `wall-prefix-selector-02-001`, case0000/0001 are O/M, case0002/0003 O/N and case0004/0005 O/O. Each numbered pair contains both physical assignments. In all retained C/D/H/I/J cases, the opponent has empty buildings and roster after each of rounds one and two: its actions are five factories and then four factories. B/N already have 20 walls and three roster entries after round one. G/L/O have 20 walls. M has a splash turret, which must count as presence.

Under `bot_research/runs/validation/delayed-wall-counter-00-001/replays/`, case0000/0001 are P/O and case0004/0005 are P/G. The identically numbered cases in `reserved-wall-counter-00-001` are Q/O and Q/G. P and Q each have only five factories after round one, then place 20 walls and buy three factories in round two. Their source changes preserve exactly this common early behavior. The recorded G controls win against P and draw against Q in both assignments.

| Opponent | Predicted selection | Predicted payoff for R |
| --- | --- | ---: |
| B | G in round two | 1 |
| C | L in round three | 0 |
| D | L in round three | 1 |
| G | G in round two | 0 |
| H | L in round three | 1 |
| I | L in round three | 0 |
| J | L in round three | 1 |
| L | G in round two | 1 |
| M | G in round two | 1 |
| N | G in round two | 1 |
| O | G in round two | 0 |
| P | G in round three | 1 |
| Q | G in round three | 0 |
| R | G in round two | 0 |

Payoff is +1 for a win, 0 for a draw, and -1 for a loss from R's perspective. These are prospective conditional transfers, not R measurements. The old selected G/L baselines used by protocol153 support the first ten entries. The actual O/G records support the O entry, with its physical seat reversed to place G where R will sit. The actual P/G and Q/G records support P and Q with the same careful reversal. R self should select G in both objects, so its control is retained G/G. Under the coupling theorem the predicted row in displayed order is [1,0,1,0,1,0,1,1,1,1,0,1,0,0]. The new information used against P/Q is their completed round-two public construction, not their identity or pending action.

## Conditional pure-support certificate

Suppose future measured R games give the same outcome from R's perspective in both physical assignments for every displayed opponent, give an R/R draw, and give a nonnegative R row. Let A be any finite real skew-symmetric matrix on these fourteen identifiers whose R row matches those outcomes. Unmeasured entries may be any real values compatible with skew symmetry. Then playing pure R for both players is a saddle point of value zero, for every such completion.

Proof. For every probability vector y over columns, e_R^T A y is a weighted average of nonnegative R-row entries, hence is at least zero. Skew symmetry gives A_{iR}=-A_{Ri}<=0 for every i, so for every probability vector x over rows, x^T A e_R<=0. Finally A_{RR}=0. Thus pure R secures at least zero for the maximizing player and at most zero for the minimizing player, attaining zero against itself. Both strategies are optimal and the value is exactly zero. No claim of uniqueness follows, and no entries outside the R row are needed.

This is a conditional certificate for a finite completed payoff game. It neither measures nor asserts a complete 14 by 14 table, and it does not make an unrestricted claim about every executable opponent or arbitrary deadline realization. The six previously missing P pairs remain missing unless separately run; the Q row is sparser still. Already measured Q/G draws and Q/O wins give A_GQ=0 and A_OQ=-1, so the prior half-G/half-O mixture has payoff -1/2 against the added Q column. Its earlier restricted certificate does not extend to that enlarged game. The proposed R certificate is open until its support row is validated.

## Prospective verification and dependencies

The proposed campaign has fourteen opponents including self, two physical assignments each, totaling 28 new standard games. Before any R decisions, pin this proof, the implementation, exact policy specifications, full transitive source/data closure, selected retained baseline references and checker. The baseline mapping must preserve R's physical seat, including reversed P/G, Q/G and O/G records. Preserve unsuccessful calls and failed hypotheses rather than excluding them.

The falsifiable checks are the predicted selection round/member and permanent selection; both exact prefix equalities where required; the displayed payoff row and self draws separately in each seat; and full selected-control history agreement under explicit role normalization. Independently advance a fresh selected member from round one on copied actual observations and compare actions and corresponding private values, including L's private H and last-round/player state. This is distinct from replaying accepted actions. Require strict action accounting, complete unchanged-engine replay, exact stream boundary and terminal status. Retain first divergences, errors and actual timing; deadline-sensitive failure is evidence about the measured run, not a reason to silently relax the claim. These opponents are selected development cases, not held-out or independent random samples.

Principal sources are `td_game/{actions,engine,pathfinding,state,config}.py`, `td_game/balanced.json`; `bot_research/bots/counters/{early_wall_guard,wall_signal_repair,wall_signal_timing,stateful_public,public_factory,forecast_timing,shared_prefix_selector,hp_handoff,screened_guard_maze,staged_guard_maze,maze_grower,delayed_wall_guard,reserved_wall_guard,wall_prefix_selector}.py` and their data; frozen economy v2 `{fastsim,threat,defense_plan}.py`; and frozen defense v34/v38 planners. Earlier standalone arguments are `bot_research/experiments/validation/analysis/{wall_prefix_selector,delayed_wall_counter,reserved_wall_counter}/PROOF.md`. Actual policy definitions and outcome references are their verification receipts and the ten-policy receipt. These references identify dependencies; they are not a replacement for a future complete input pin map.

The inspected receipt SHA-256 values are: O `f0a5549167e83bce3d976c56896a35da675219712b3be8f47dc14d957b23cd15`, P `9be063a9b5a9d2a1a0299e6cd9c3247e105328b96f282a710f2cacacf420c092`, and Q `2f67ad35be4c9b34f2fc97007d34901bfbec2eee00ba9df48714dab035ac7dc1`, each at its analysis directory's `verification/full_games.json`. The guard00 data SHA-256 is `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334`.

The early source lemmas are proved under their fixed hypotheses. The state theorem and pure-support certificate are conditional results with the explicit premises above. R implementation correctness, all 28 prospective outcomes, retained-history reproduction and empirical satisfaction of the certificate premises remain OPEN. No proof-assistant verification or new policy execution is claimed.
