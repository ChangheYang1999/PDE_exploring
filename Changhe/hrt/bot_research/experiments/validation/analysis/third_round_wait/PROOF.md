# Waiting for the completed third round

Written 2026-10-31T21:56:36Z from source and retained-record inspection. This is a prospective design and standalone informal proof. No policy was instantiated, no decision was called, and no game or engine replay was executed for this document. The proposed composite has no measured full-game result. Its implementation and full-game performance remain OPEN.

Revised 2026-10-31T22:01:10Z after source review, before declaration or policy calls: the standalone G/H round-four control is explicit, and prefix coupling against an arbitrary opponent retains matching-input and deadline hypotheses. The bot source and prospective protocol now exist; their behavior has not been executed.

Read the exact policy definition first, followed by the public-information and state arguments, the two opening calculations, and the scope and verification requirements. The opening statements are source deductions under explicit hypotheses. Retained measurements are identified separately.

## Exact prospective policy

G is `EarlyWallGuard(witness='guard00')` from `bot_research/bots/counters/early_wall_guard.py`. L is the unchanged `WallSignalRepair()` from `bot_research/bots/counters/wall_signal_repair.py`. Define L4 by constructing a fresh L instance and, before its first decision, setting that instance's `attack_round` field to the integer 4. No other field changes. This changes the inherited `ForecastTiming` attack trigger; it does not reschedule construction, repair, saturation or any opponent-model transition. L4 is a new parameter variant, not an alias for L.

S is `LateReservedWallGuard()` from `bot_research/bots/counters/late_reserved_wall_guard.py`. H is `HPHandoff` with the exact `HP_PARAMETERS` in `shared_prefix_selector.py`:

    layout='empty', growth_rounds=6, bait=[], bait_round=2,
    tier='tier5', factory_cap=2000, purchase_cap=1000,
    replan_iters=5000, deadline=12, lead_from=8.

Its other arguments retain their current defaults: lead_margin=0, panic_hp=None and panic_from=2. H fixes upgrade_round=9 and splash guard rounds (4,6). Its eventual defender is frozen Fortress34 with attack='none', round1_poke=0 and replan_iters=5000. L4's persistent private model is exactly this H specification.

The proposed composite T owns fresh G and L4 instances, an initially unset permanent selection, and round/player bookkeeping. It requires consecutive calls from round one for a fixed physical player index. Let the presence signal at a decision be whether the opponent's current public snapshot has any buildings or any roster entries. A factory alone is not presence. The following order resolves when an unused member stops being advanced.

| State entering a decision | Transition and returned proposal |
| --- | --- |
| Already selected G or L4 | Advance that member once on a copied current observation and return its complete ordered action list. Never reselect. |
| Unselected, round one | Advance G and then L4 once each on separate copies. Retain both states. Return G's list. |
| Unselected, round two or three, presence | Select G before member calls; advance only G once and return its list. |
| Unselected, round two or three, no presence | Advance G and then L4 once each on separate copies. Retain both states. Return G's list. |
| Unselected, round four, presence | Select G before member calls; advance only G once and return its list. |
| Unselected, round four, no presence | Select L4 before member calls; advance only L4 once and return its list. |

Thus T always submits G through round three. The unused L4 proposal is discarded, even when it differs from G's. T does not apply discarded actions to the engine, merge lists, roll back member state, replay fabricated observations or patch the observed economy to match a discarded proposal. There is no equality requirement at round three. An unsuccessful call ends supported use of that instance; retrying after a partial member transition is outside this definition. The operational choice to stop the unused member on the commitment decision avoids an unnecessary call and makes the call schedule exact.

This definition is preferable to resetting L4 at round four: its persistent model explicitly rejects a first call whose round is not one. Advancing a fresh model on invented observations would define another policy. No simpler replacement is established to preserve the intended continuation.

## Rules, notation and hypotheses

Use the unchanged bundled standard engine and `td_game/balanced.json`: a 12 by 12 grid, spawn (0,0), base (11,11), 800 initial HP, 100 initial gold, no buildings, factories or roster, wall cost 1, factory cost 20, factory income 15, path income 1 per edge and outgoing-hit bounty 5. Splash costs 60 and deals 10 damage to every copy on any of its eight neighboring cells. Tier2 costs 40, has 70 HP and deals 12 base damage; tier4 costs 260, has 560 HP and deals 60 base damage. There are 250 ticks per round and at most 50 rounds. The engine completes both combats and income settlement before checking the terminal outcome.

All source and data dependencies are fixed; member calls succeed; no external code mutates their owned state. Midgame initialization and modified rules are excluded. Statements about a reached decision require that the game has not terminated earlier. Against the exact H and S defined here, the empty early rosters below prove that rounds one through four are reached.

Write F for one factory purchase, X for a splash at (1,3), and W for the ordered guard00 walls: (0,1), (1,1), then (x,1),(x,3) for x=2 through 9, then (10,3),(11,3). A power such as F^5 means five consecutive copies of the same action. Closing gold includes unspent gold and the round's income.

`Engine.observation` at decision r contains the state after completed round r-1. It never contains either round-r submission. For comparisons between differently named records in a fixed physical seat s, normalize only the two snapshot names to 'selector' at s and 'opponent' at 1-s. Do not exchange physical player indices or remove other state fields. Names are carried by reconstructed player states but are not a condition in the displayed selector or early policy branches. A whole-game comparison involving a name-sensitive opponent additionally requires equal raw names or a separately justified name invariance.

## Public-information and private-state claims

**Claim 1. T's selection is a public-history decision, and its forecast does not inspect the live opponent.**

Proof. The selection examines only the current round, fixed player index, the opponent snapshot's buildings and roster, and T's own prior selection. Its member calls receive separate copies of the actual public observation. `ForecastTiming.predict` makes another copy, changes only its `player` to the enemy index, and calls L4's own persistent H model. It reconstructs a private `PlayerState` from the public enemy snapshot and applies that model's proposed actions to the private state. Neither the live opponent object nor a pending submission is passed to this code. Source and witness files used by the members are fixed prior information, not per-condition labels. T's selector does not inspect names, result filenames, bot specifications, process identities, elapsed runtime or the model's predicted actions to identify the opponent. Predicting the exact H action from its known source and public state is a deduction, not observation of its hidden pending submission. This proves the claim.

This is a statement about the inputs to policy decisions and selection. Later inherited planning uses elapsed-time cutoffs, so it is not a claim that the complete executable is a mathematical function of public state alone under arbitrary scheduling.

**Claim 2. If T selects L4 at round four, its persistent H has already consumed the actual observations for rounds one, two and three exactly once, in order.**

Proof. Reaching that branch means neither earlier presence test selected G. The transition table therefore calls L4 once in each of rounds one through three and retains its state each time. `StatefulPublicTiming` constructs one `PersistentFactoryModel`; that wrapper constructs one private H policy and requires each new round to equal `last_round+1` with a fixed player index. `ForecastTiming.decide` calls `predict` once. `WallSignalTiming` may replace its parent's round-one action list, but does not repeat or undo prediction. `WallSignalRepair` uses the stored predicted actions and imagined state; it does not make another call to H. Consequently the wrapper's `last_round` is three immediately before the selected round-four call, and four immediately afterward. Its `player` is always the opponent's physical index. Continuing L4 thereafter preserves the consecutive-round invariant.

The discarded round-three proposal still leaves private effects: the model's transition, forecast trace and repair trace remain. Those effects are part of T's state, even though the proposed factories were not purchased. Conversely, actual own buildings, factories, roster and gold on the next call come from the next actual observation. They are not reconstructed from L4's past proposed actions. This proves a valid state history for the new composite. It does not prove equality with a standalone L or L4 history that submitted different actions.

If G is selected earlier, L4 need not be advanced again; its unused model may stop at round one or two. If G is selected at round four, that model stops at three. No later consecutive-call requirement applies to a member that is never called again.

**Claim 3. Under a matching-input coupling, every T run that selects G reproduces a standalone G run against the same opponent. All T runs reproduce its G prefix through round three.**

Proof. Initially T's G and the standalone G have the same logical state. Before a possible L4 selection, T always returns G's own complete ordered action list. Assume the corresponding public observations and decision-relevant external inputs agree. The corresponding G transitions then agree; the opponent transitions agree under the same assumption; and the unchanged deterministic engine produces equal next public states. Induction proves equality through round three. If T selects G, every later return is again that already advanced G's list, so the induction continues through termination. G is never reset, and its defender is first called at round five just as in standalone G. Discarded L4 work is not part of the corresponding G logical state.

The coupling hypothesis includes names where relevant, opponent state, random inputs, mutable shared state and any deadline outcomes that can alter actions. Extra shadow work can change cache warmth or scheduling. Frozen Fortress38 and H's frozen Fortress34 contain three-second planning cutoffs; equal sources and equal observations do not alone force equal future deadline branches. The early displayed G branches do not invoke those timed planners. For the displayed H and S early branches, the source calculations below establish exact prefix coupling under the standard successful-call conditions. For an arbitrary opponent, even prefix coupling through round three retains the matching-input and deadline conditions above: an opponent may already use a timed planner in those rounds. Universal full-game equivalence under arbitrary load is not claimed.

## Exact early separation of H and S

**Claim 4. Against either H or S, T stays unselected through round three, ends that round with W+X, 14 factories, 267 gold, empty roster and 800 HP, and sees a separating public signal at round four.**

Proof. Until round four, H's empty layout, empty bait and guard schedule produce only factory purchases. Its handoff cannot fire: the lead trigger starts at eight, the round trigger is twelve and panic is disabled. S's scheduled walls and splash both occur in round three; its minion purchase is in round four. Both therefore submit F^5 in round one and F^4 in round two. Their empty-map path has length 22, giving closing gold 97 and then 174 with five and nine factories. Neither presence test in rounds two or three fires.

T's G first submits W F^4. Every wall prefix is affordable and leaves a path: the route through (0,0), (10,0), (10,2), (1,2), (1,4), (11,4), (11,11) avoids even the final W. Any path must cross row one at x at least 10 and row three at x at most 1. It therefore uses at least 10+9+10 horizontal edges and 11 vertical edges. The witness attains 40. All 100 gold is spent, and income 40+4*15 gives closing gold 100. Round two buys F^5 and closes with nine factories and 40+9*15=175 gold.

In round three G builds X and buys F^5. The only gap in row three is now x=0. The corresponding lower bound is 10+10+11 horizontal edges and 11 vertical edges, or 42. A route through (0,0), (10,0), (10,2), (0,2), (0,4), (11,4), (11,11) attains it. The splash is legal. Spending 60+5*20 leaves 15 gold; income is 42+14*15=252. Closing gold is therefore 267, not merely the income 252.

L4's first two proposals agree with these G lists. Its H model predicts only factories and no active roster, so the inherited defense routine receives empty threat and zero additional threat budget. `threat.packages(0, ...)` contains only the empty package, whose simulated damage is zero; the builder returns no actions. Round one is replaced by W F^4; round two yields F^5. At round three the same empty-threat argument applies, its attack has been moved to four, repair starts at four, and saturation starts at twenty. L4 therefore proposes F^8 using the actual 175 gold. T discards that different list and returns G's X F^5. The private H prediction and traces remain advanced.

H submits F^8 in round three, ending with 17 factories and 174-160+22+17*15=291 gold on an empty map. S instead submits W X F^2. Before factories it has 94 gold; closing gold after k factories would be 94-20k+42+15*(9+k)=271-5k. Its parent could afford four factories, but the reservation reduces this to the largest count reaching the tier4 target 260: k=2, giving 261 gold and 11 factories. Thus at decision four H still has no buildings or roster, whereas S has 20 walls and X. T selects L4 against H and G against S.

All rosters on both sides were empty through round three. There are no outgoing hits, no bounties and no incoming damage, so HP remains 800 and these decisions are reached. The observations through decision three agree between H and S after the stated name normalization. Their decision-four observations differ. This proves the claim.

| End of round | T gold / factories / path | H gold / factories / path | S gold / factories / path |
| --- | --- | --- | --- |
| 1 | 100 / 4 / 40 | 97 / 5 / 22 | 97 / 5 / 22 |
| 2 | 175 / 9 / 40 | 174 / 9 / 22 | 174 / 9 / 22 |
| 3 | 267 / 14 / 42 | 291 / 17 / 22 | 261 / 11 / 42 |

These are separate T/H and T/S games, not one three-player game.

## The new round-four continuation against H

**Claim 5. Under the exact T/H definitions, round four submits six tier2 purchases followed by one factory for T, and a splash at (10,1) followed by eleven factories for H. Closing state is T gold 304, factories 15, HP 800 and six tier2 roster entries; H gold 453, factories 28, HP 728 and empty roster. T's map remains W+X; H's map has only its new splash.**

Proof. T selects the already advanced L4. Its private H has consumed the same actual public states as the real H, with the player index set to H's seat. Before round four, both have made the same deterministic factory-growth transitions and neither can have handed off. At round four, `StagedGuardMaze` prepends its first empty-layout guard (10,1), then filters its parent's factory list against the remaining budget. Starting from 291 gold, it pays 60 and retains eleven affordable factory purchases, leaving 11 gold and 28 factories. The private model predicts exactly the same legal list. It creates no roster.

After the predicted splash, the route used by the bundled right/down/left/up BFS runs along row zero to (11,0), then down column eleven to (11,11). The single blocked cell (10,1) does not obstruct this shortest, right-first route. The splash is adjacent to precisely (9,0), (10,0), (11,0), (11,1) and (11,2) on its attackable cells. A traversing copy receives five hits of 10 damage. Each tier2 therefore survives with 20 of its 70 HP. Six such entries spawn on ticks zero through five, arrive on ticks 22 through 27, and each deals 12 base damage. Splash attacks all adjacent copies, so these six do not compete for its attacks. The empty baseline wave deals zero. Both the displayed frozen simulator and the original combat loop consequently give positive incremental damage 72 for this particular wave and map, without a general simulator-equivalence assumption.

L4 uses its actual own gold 267, not a hypothetical factory-only balance. Its count is min(200, floor(267/40))=6. Positive predicted gain retains all six purchases. No predicted active enemy roster exists, so its defense builder adds nothing. Saturation is inactive. The remaining 27 gold buys one factory and leaves 7. `WallSignalRepair` recomputes damage against the same empty predicted incoming roster, obtaining zero; it does not invoke the replacement planner or remove the attack. Thus the complete returned list is exactly the stated one.

The real H constructs the predicted map simultaneously. There is no incoming attack on T, and all six T copies hit H, giving HP 800 and 728. T income is 42+15*15+6*5=297 and closing gold 7+297=304. H income is 22+28*15=442 and closing gold 11+442=453. The six entries were bought in round four and expire after round fifteen under the standard twelve-round lifespan. Neither base is destroyed. This proves the claim.

This proves a specific legal opening, not a winning continuation. A generic empty-signal opponent may submit an unexpected round-four attack or defense. L4's one-model forecast may then be wrong. Its generic repair branch can replace the entire original action list if a legal replacement lowers predicted incoming damage, so merely setting attack_round=4 does not guarantee an attack against every opponent.

For the corresponding standalone G/H control, the shared G prefix also starts round four with 267 gold and fourteen factories. G buys one tier4 and no factory, leaving 7 gold. H makes the same splash-and-eleven-factory move proved above, since its opening has no round-four response to the enemy roster or map. The five splash exposures cannot kill a tier4, so that single copy hits for 60 damage. G/H therefore closes round four with gold 264/453, factories 14/28 and HP 800/740, in G-first order. T/H agrees with this control through the observation at decision four, then diverges in its fourth submission and completed state. The comparison explains exactly where G coupling ends on T's L4 branch.

Against S, T chooses G and both sides purchase exactly one tier4 at round four with no factory. A shortest simple route encounters at most eight cells adjacent to the only splash, giving at most 80 damage to a 560-HP tier4; its 42-edge route finishes before tick 250. Both copies therefore hit. T and S close with HP 740 each, gold 264 and 213, and factories 14 and 11 respectively. This round-four result is source-derived and agrees with the retained G/S opening. Continuing to transfer the retained full-game draw still requires Claim 3's later coupling conditions.

## Why this escapes the restricted selection result

Protocol159's result in `analysis/delayed_signal_ambiguity/PROOF.md` restricts selection to G or unchanged L, with commitment by decision three and a shared submitted prefix. T does not meet that definition. It waits until decision four on the H/S prefixes and can choose a new L4 continuation after having discarded its different third proposal. It therefore does not contradict the conditional -1/3 bound for that restricted class.

Nor does T inherit L's H win. In the retained L/H games, L bought four tier2 entries at round three, ended that round with 210 gold and nine factories, and had already reduced H to 752 HP. T instead ends round three with 267 gold, fourteen factories, X, no roster and H at 800 HP. At the end of round four the retained L/H state had H at 704 HP; the new T opening has H at 728 HP. T has traded away earlier damage for a different map, economy and later roster lifetime. Even a standalone L4 would have submitted its eight factories at round three and created a different own state. None of those baselines is a full continuation control for the L4 branch of T.

The useful property is narrower: completed third-round construction can select G against S without giving up the option of a six-copy tier2 strike against H. Whether this is enough to avoid a loss against H, or improves performance elsewhere, is OPEN.

## Retained evidence and future verification

The six existing result files below and their corresponding `replays/caseNNNN.jsonl` streams were inspected through completed round four, reading stored records only. These are disclosed development conditions, not new or held-out T games. Paths below are relative to `bot_research/runs/validation/`.

| Existing pair | Result paths | Physical mapping |
| --- | --- | --- |
| G/H | `early-wall-transfer-00-001/results/case0010.json`, `case0011.json` | G is respectively seat zero and one. |
| S/G | `late-reserved-wall-counter-00-001/results/case0004.json`, `case0005.json` | S is respectively seat zero and one, so G is respectively seat one and zero. |
| L/H | `wall-signal-repair-001/results/case0002.json`, `case0003.json` | L is respectively seat zero and one. |

Both seats show the G, H and S opening actions and balances used above. The previously completed protocol159 `RESULTS.md` reports G/H losses, G/S draws, L/H wins and L/S losses, separately in both seats. That existing audit is prior evidence. Its games were not rerun here, and it does not measure T.

Before any T policy call, pin this proof, exact transition order, implementation, policy specifications, all source/data dependencies and prospective checks. A minimal targeted experiment uses both physical seats against H and S, retaining every failure. Test selection and permanent commitment; actual submitted G prefix; discarded round-three F^8 proposal; persistent-model round/player state and single-call counts; the complete Claim 5 opening; strict action acceptance; and complete replay to the exact terminal boundary. A T/S control can compare the entire canonical history with the matching-seat G/S baseline, while recording the first deadline-sensitive or other divergence. Do not demand false full-history equality with L/H or standalone L4/H. Independently advancing an L4 object on T's actual observations is a valid private-state check; replaying its discarded proposals as if submitted is not.

Full-game outcomes and action histories must remain separate from audit completion. Nonnegative T payoff against H and S is a falsifiable new hypothesis. Broader performance needs a separately declared opponent set and both-seat games; no complete payoff table or unrestricted game value follows from four targeted games. Timeouts, exceptions, early termination or contrary outcomes must remain recorded rather than being filtered into a success statement.

Later runtime risks are substantive. G's defender can plan from round five. H's lead-based handoff can begin at round eight and its fixed handoff occurs at round twelve; `deadline=12` denotes that round threshold, not seconds. Its frozen planner and G's frozen planner have three-second cutoffs. L4's outer repair planner also introduces extra computation when predicted damage remains, and global route caches can change runtime without changing the mathematical route. Fresh calls and complete histories can establish equality in measured executions, but cannot prove equality for every scheduling environment.

## Dependencies and inspected identities

The source argument depends on `td_game/{engine,actions,combat,pathfinding,state,config}.py`, `td_game/balanced.json`; counters `{early_wall_guard,late_reserved_wall_guard,reserved_wall_guard,delayed_wall_guard,wall_signal_repair,wall_signal_timing,stateful_public,public_factory,forecast_timing,shared_prefix_selector,hp_handoff,screened_guard_maze,staged_guard_maze,maze_grower,visible_search}.py`; frozen economy v2 `{defense_plan,fastsim,threat}.py`; frozen economy v17 `freeplan.py`; the latter's frozen defense v15 and harness dependencies; frozen defense v34/v38 planners; and fixed guard, maze-layout and screened-guard JSON files. The inherited planner constructed and then replaced by `StatefulPublicTiming` also belongs in a future complete runtime closure. Source reading here is not a substitute for that prospective transitive pin map.

Earlier supporting arguments are `analysis/two_round_wall_selector/PROOF.md`, `analysis/late_reserved_wall_counter/PROOF.md` and `analysis/delayed_signal_ambiguity/PROOF.md`, relative to `bot_research/experiments/validation/`. They provide context; the opening and state arguments needed for T are given above.

Selected SHA-256 identities inspected for this proof:

| Project-relative source or data | SHA-256 |
| --- | --- |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/combat.py` | `17265171d1e2ab4c60b07f9b4f473a19667aef4a2110aeb2c07f1cb39f965228` |
| `td_game/pathfinding.py` | `5ecce5a8737d43e3add703e4143f28a1d2bb8fb62e84a2d7f29be441749ae8b2` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/wall_signal_repair.py` | `d82b22386b5973ecfc6cbcb984eb6d91d1ca5ede4c6c16ffa693c05b32e81226` |
| `bot_research/bots/counters/wall_signal_timing.py` | `63d7681bec8ac9fb5c3855d172be8c2e3a6b3a591bdf8e746efc1d9b4e754146` |
| `bot_research/bots/counters/stateful_public.py` | `c2cde121ecf8c1475daee2958f97a1a1b9c08794bee4cf6ead7a05924b4c2c7b` |
| `bot_research/bots/counters/forecast_timing.py` | `31e73f1a98f8cb70b9ddacfd2067a34e752450c53648a42482d934fcc92be78a` |
| `bot_research/bots/counters/hp_handoff.py` | `c5baa3d7af48508d0cf10cbac0950a018673c45e3b3cba3f0522324da5ea8ee6` |
| `bot_research/bots/counters/shared_prefix_selector.py` | `7b2c2a0c570f140cf84a5908293bc7835718652a4c71ec2071745e3e61c1c5e7` |
| `bot_research/bots/counters/late_reserved_wall_guard.py` | `2c862cb19d15aa563f0a30219ebd501020f75a5096045d60cf018cefdf2b2ce2` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/bots/counters/data/staged_guards_001.json` | `fdc86066da88290d4d0c82f1c53895174f0ee38250ee18fb29fd425eba8c8398` |

The exact successful-call opening lemmas and the conditional coupling argument are the proved statements. Implementation correctness, new full games, practical robustness to extra computation and any claim of improved worst-case payoff remain OPEN. No proof-assistant or new empirical validation is claimed.
