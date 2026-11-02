# A fourth-round wall counter to the delayed selector

Prepared UTC: 2026-10-31T22:21:25.023265+00:00.

This standalone source argument defines a prospective counter V and proves its first five rounds against the exact T and U policies below. V has not been implemented or executed at this preparation time. No policy, constructor, engine, replay or game calls were made for this argument. Statements about later outcomes are OPEN. The proof uses the unchanged bundled rules, not historical manifest hashes or a hypothetical replacement engine.

Read the policy definition and hypotheses first, then the routing argument and five-round calculation. INDEX.md gives the reading order. The final section records the source identities and the limits of the argument. This is an informal proof of a conditional opening, not a formal verification or a general equivalence theorem for the planning simulator.

## Exact prospective policy and compared policies

V owns a fresh callable returned by `bot_research.bots.defense.frozen.v38.fortress.make()` with no arguments, created once at V construction. It does not call this defender on rounds one through five, even to discard proposals. Its first possible defender call is at decision six, on the actual round-six observation. It retains that callable afterward and never resets it. The factory defaults are part of this specification. In particular, this is the existing Fortress38 with default opportunistic attack, attack_share=0.25 and replan_iters=5000, not a separately specified pure defender with attack='none'.

V requires exactly one successful call per reached round, consecutively from round one, at a fixed physical player index in {0,1}. It copies the observation and reconstructs its own private state for legal filtering. A proposed action is appended only if applying it to this evolving private state succeeds; rejected proposals are retained in a trace. An unsuccessful call ends supported use of the instance; retries after a partial private transition are outside this definition.

The complete action rule is:

| Decision | Ordered proposal and return rule |
| --- | --- |
| 1, 2, 3 | Buy factories while the reconstructed own state can afford one. No buildings or minions. |
| 4 | Propose all twenty guard00 walls in witness order, then its splash at (1,3), then affordable factories. |
| 5 | Propose exactly one tier4 purchase if currently affordable, then affordable factories. No additional minions or buildings. |
| 6 and later | Call the retained fresh Fortress38 callable exactly once on a deep copy of the current actual observation. Filter its complete ordered list against the reconstructed actual own state and return accepted actions in that order. No extra opening actions or factory fill. |

This gives a concrete rule outside the exact comparison too: failed opening builds are skipped and recorded, factories use the remaining budget, and the heavy purchase is omitted if unaffordable. Such exceptional cases are not part of the theorem below. In the theorem, all listed actions are legal and no filter removes an action. The twenty walls and the splash are read from the existing guard00 entry of `data/early_wall_guard_001.json`; no new layout or searched parameter is introduced.

G is `EarlyWallGuard(witness='guard00')`. L4 is a fresh `WallSignalRepair()` whose `attack_round` alone is set to integer 4 before its first call. Its other fields remain tier='tier2', attack_share=1, count_cap=200, defense_first=False, saturate_round=20 and max_factories=80, with its unchanged persistent private H model.

T is the pinned `ThirdRoundWait()` and U is the pinned `BlindFourthRound()`. Both construct fresh G followed by fresh L4. While T is uncommitted, and through round three for U, they call G then L4 once each on separate copies of the actual current observation and return only G's entire ordered list. Discarded L4 proposals do not become submitted actions or fabricated observations. T selects G before calls at the earliest decision two, three or four where the enemy snapshot contains any building or roster entry; otherwise it selects L4 at decision four. U selects L4 unconditionally at decision four. Once either selects L4, it calls only that same L4 instance thereafter. Their exact implementations and prior proofs are pinned below.

H, the private forecast policy inside L4, is `HPHandoff` with the exact `shared_prefix_selector.HP_PARAMETERS`:

    layout='empty', growth_rounds=6, bait=[], bait_round=2,
    tier='tier5', factory_cap=2000, purchase_cap=1000,
    replan_iters=5000, deadline=12, lead_from=8.

Other defaults are lead_margin=0, panic_hp=None and panic_from=2. The opening fixes guard_rounds=(4,6) and upgrade_round=9. Its eventual private Fortress34 uses attack='none', round1_poke=0 and replan_iters=5000. A lead handoff cannot occur before round eight and its deadline cannot occur before twelve. Thus no H handoff occurs in the five-round proof. V does not construct or impersonate an H instance; its first three submitted lists happen to equal this H opening under the stated conditions.

## Hypotheses and notation

Use a standard start under the unchanged `td_game/balanced.json` rules: 12 by 12 grid, spawn (0,0), base (11,11), 100 gold, 800 HP and no buildings, factories or roster. A wall costs 1. A factory costs 20 and pays 15 per round. Path income is one per edge, and each outgoing base hit pays a bounty of 5. Splash costs 60 and deals 10 damage to every copy on any of its eight neighboring cells. Tier2 costs 40, has 70 HP and deals 12 base damage; tier4 costs 260, has 560 HP and deals 60 base damage. Roster life is twelve rounds and each round has 250 ticks. There are at most fifty rounds. Both combats and both incomes settle before terminal evaluation.

All source and data inputs are fixed. Calls succeed and no external code mutates private state. These exact early branches ignore names and do not invoke time-limited planning; an independent observation comparison may normalize only the two snapshot names. Modified rules, scenario patches, prepopulated maps, midgame construction of a policy, failed calls and later full-game equality without matched deadline behavior are excluded.

Write F for one factory action, X for splash(1,3), Y for splash(10,1), and W for the ordered guard00 walls: (0,1),(1,1), then (x,1),(x,3) for x=2 through 9, then (10,3),(11,3). A power means that many successive actions. A map written W+X contains exactly those walls and splash. Gold in closing-state statements includes the just-completed income.

A decision-r observation is the completed round r-1 state. It contains neither pending round-r list. The T/V and U/V statements are two separate games, in either physical assignment. The engine interleaves submitted actions, but each listed action mutates only its owner's state; combat starts after all actions.

## Routing and combat lemma

**Lemma 1. The empty map and the map containing only Y have right-first shortest path length 22. W has length 40 and W+X has length 42. Every tier2 copy that traverses W+X dies before arrival; a single tier4 copy traverses it and hits. On the map containing only Y, six tier2 copies all hit. These claims apply to the specific spawn schedules used below.**

Proof. The bundled BFS explores right, down, left, up. On an empty map, or with only blocked cell (10,1), the right-first shortest route goes along row zero to (11,0), then down column eleven. Its length is 22. Y is adjacent to exactly five attackable route cells: (9,0),(10,0),(11,0),(11,1),(11,2). A copy receives 50 total splash damage there.

Any W route must cross row one at x at least 10 and row three at x at most 1. Its horizontal travel is at least 10+9+10 and its vertical travel at least 11, giving lower bound 40. The route through (0,0),(10,0),(10,2),(1,2),(1,4),(11,4),(11,11) attains it. With X blocking (1,3), the only row-three opening is x=0. The lower bound becomes 10+10+11+11=42 and the route through (0,0),(10,0),(10,2),(0,2),(0,4),(11,4),(11,11) attains it. The right-first BFS uses straight segments between those waypoints: at any remaining shortest-path choice it prefers right to down. This also agrees with the full route stored in the guard00 JSON witness. Since this final path avoids every W and X cell, it certifies path existence after every preceding build prefix. None of these build cells is the spawn or base or duplicates another cell.

On W+X the seven adjacent route cells for X are (2,2),(1,2),(0,2),(0,3),(0,4),(1,4),(2,4). They are path indices 20 through 26. Thus each traversing copy receives 70 splash damage. A tier2 reaches zero HP at index 26 and is removed before its would-be base arrival at index 42. Splash hits all neighboring copies independently, so the six copies cannot shield one another. They spawn on ticks zero through five and die on ticks 26 through 31, comfortably inside 250 ticks. Their combat copies die; their permanent roster entries are not deleted by combat.

A tier4 instead has 490 HP after those seven exposures and reaches index 42 on tick 42 when it is the sole roster entry. It deals 60 base damage. On the Y-only map a tier2 retains 20 HP after five exposures. Six tier2 entries spawning on ticks zero through five arrive on ticks 22 through 27 and deal 72 damage in total. The original combat loop removes arriving copies before turret attacks, but none of the cited exposure cells is the base. The displayed `fastsim` code uses the same per-index splash sums and spawn ticks for these cases, so its particular gain calculation agrees by this direct argument. No general simulator-equivalence assumption is needed. This proves the lemma.

## Public information and model history

**Claim 1. V uses only public observations and fixed source/data knowledge. Against V, both T and U select their already advanced L4 at decision four, and L4's H model consumes actual observations once per round without a reset.**

Proof. V's first five decisions consult only round, own public snapshot, rules and its fixed witness. Its later callable receives a copied public observation. No branch receives the other policy object, hidden action list, evaluation label, condition filename or game result. The later Fortress38 also has its own timing and persistent planning state, which is why public-observation use does not imply schedule-independent full-game determinism.

Through completed round three V has built nothing and bought no minion. Therefore T sees neither a building nor a roster entry at decisions two, three or four. Factories do not satisfy its presence predicate. Both composites call G then L4 on decisions one through three and only L4 at decision four. Once the newly built V walls become visible at decision five, T is already permanently committed. It does not re-run its selection test to change member.

`ForecastTiming.decide` calls `predict` exactly once. `predict` deep-copies the actual observation, changes its player index to the opponent, calls the retained `PersistentFactoryModel`, reconstructs the opponent's actual public snapshot and applies only the forecast action list to that private reconstruction. The persistent wrapper has one H policy and enforces consecutive rounds and a fixed opponent index. `WallSignalTiming` replaces a round-one outgoing proposal without repeating prediction; `WallSignalRepair` reuses the recorded predicted list without another H call. Hence the H wrapper reaches last_round=3 before commitment, then 4 and 5 after the next calls.

The unused round-three L4 proposal is F^8, while G submits X F^5, as calculated below. Its discarded actions never affect engine gold or buildings. Its private H transition and traces nevertheless remain. On round four and five the own and opponent economies come from the new actual observations, not a simulated rollout of those discarded proposals or of earlier H predictions. This distinction is essential: the round-five H prediction starts from V's actual W+X map and 458 gold even though the previous prediction was a Y-only map. This proves the claim.

## Exact first five rounds

**Claim 2. Under the hypotheses, each T/V and U/V game reaches the end of round five with the following closing states. Until the end of round three the roster on both sides is empty.**

| Completed round | T or U: gold / factories / HP / map | V: gold / factories / HP / map |
| --- | --- | --- |
| 1 | 100 / 4 / 800 / W | 97 / 5 / 800 / empty |
| 2 | 175 / 9 / 800 / W | 174 / 9 / 800 / empty |
| 3 | 267 / 14 / 800 / W+X | 291 / 17 / 800 / empty |
| 4 | 274 / 15 / 800 / W+X | 458 / 27 / 800 / W+X |
| 5 | 476 / 28 / 740 / W+X | 605 / 36 / 800 / W+X |

At round four T or U buys six tier2 entries, all retained in its roster through round five, while V's roster remains empty. At round five V buys exactly one tier4 entry. The tier2 entries are bought at four and expire after fifteen; the tier4 entry is bought at five and expires after sixteen. No other roster entry exists in these states.

Proof, rounds one through three. V buys F^5, spending all 100 and earning 22+5*15=97. It next buys F^4, leaving 17 and earning 22+9*15=157, so closes with 174. It then buys F^8, leaving 14 and earning 22+17*15=277, so closes with 291. This is the exact H empty-growth opening: no bait is configured, guard construction first occurs at four, and no handoff can occur this early. It therefore produces the same numeric first-three public states as H against either composite.

G buys W F^4 in round one and spends all 100. Lemma 1 gives income 40+4*15=100. In round two it buys F^5 and earns 40+9*15=175. In round three it builds X and buys F^5, spending 60+100 out of 175. The remaining 15 plus income 42+14*15 gives 267. These actions are all affordable and their builds are legal by Lemma 1.

Every L4 prediction in these rounds contains only factories and an empty incoming roster. `defend` is passed empty threat and zero additional threat gold. `packages(0,...)` reduces to the single empty package, whose damage is zero, so it adds no action. L4's timed attack is deferred to four and repair starts at four. Its proposed own actions are W F^4, F^5 and F^8. Only the third list differs from G and is discarded. The engine has no attacker roster, so neither side takes damage or earns a hit bounty. Both games necessarily reach decision four with the first three displayed rows.

Proof, round four. Both composites select L4 by Claim 1. From V's actual 291 gold and 17 factories, the private H has not switched and forecasts its scheduled first guard Y. `MazeGrower` first proposes fourteen factories from 291 gold, then `StagedGuardMaze` prepends the 60-cost guard and accepts eleven affordable factories. The result is precisely Y F^11, leaving 11 private gold and 28 factories on a Y-only map. There is no predicted roster.

L4 calculates min(200,floor(267/40))=6 tier2 purchases using its actual own balance. The forecast baseline roster is empty. By Lemma 1 the six-copy forecast gain on Y is 72, which is positive, so all purchases are kept. Empty predicted incoming threat means no defense. Saturation starts only at twenty. The remaining 27 gold buys one factory, leaving 7 and fifteen factories. `WallSignalRepair` obtains zero residual incoming damage and does not call its replacement planner. The complete submitted list is six tier2 actions followed by F.

V actually submits W X F^10. It spends 20+60+200=280, leaving 11 and twenty-seven factories. Both actual maps are W+X. All six tier2 combat copies die by Lemma 1; V has no attacking roster. There are zero base hits and zero bounty income. T or U closes with 7+42+15*15=274, while V closes with 11+42+27*15=458. Both HP remain 800. Their actual observations first differ from the corresponding H game after this round. In particular, the previous private forecast was wrong, despite using only permissible public information.

Proof, round five. The persistent H model now receives V's actual completed round-four snapshot: 458 gold, twenty-seven factories, W+X and empty roster. Round five is still within H's growth phase. It is neither guard round four or six nor upgrade round nine, and no handoff is possible. Its entire forecast is therefore F^22, leaving 18 private gold and forty-nine factories. It does not add a missing Y at round five. It again predicts no active enemy roster and no incoming damage.

L4 has passed its one attack round. It adds no new minions, receives zero threat in its defense routine and has not reached saturation. It buys F^13 from actual gold 274, leaving 14 and twenty-eight factories. The repair recomputation again sees empty incoming threat and leaves this list unchanged. The six actual tier2 entries remain active, but that is the composite's outgoing roster; it is not an incoming threat to itself.

V has 458 actual gold and buys its one tier4 for 260, leaving 198. It buys F^9 for 180, leaving 18 and thirty-six factories. Its map stays W+X. The six renewed tier2 combat copies again die on V's map. V's sole tier4 crosses the composite's unchanged W+X and hits exactly once, giving V a bounty of 5 and reducing the composite to 740 HP. No other hit occurs. Closing balances are 14+42+28*15=476 for T or U and 18+42+36*15+5=605 for V. The roster dates follow directly from `apply_action` and the twelve-round lifespan. No HP is zero and round five is below the round limit, so no early terminal can invalidate this row. This proves Claim 2.

## Coupling, handoff and unproved outcomes

**Claim 3. T/V and U/V have identical complete engine histories through completed round five after only consistent snapshot-name normalization, in each fixed physical assignment. Conditional on equal corresponding future decision-relevant inputs and deadline outcomes, their complete histories remain equal thereafter.**

Proof. Fresh G and L4 states start equal. Through round three both composites execute the same ordered member calls on the same numeric actual observations and submit the same G lists. Both select L4 at four, stop calling G and call the same retained L4 transition thereafter. The displayed early branches ignore names and contain no timed search. Claim 2 and the deterministic engine establish equal transitions through five, including ordered actions, roster identities, combat and income. The wrappers' trace labels or diagnostic fields need not be byte-identical to each other; those are not engine histories or member inputs.

For later rounds, assume corresponding retained L4 and V states, observations, names where read, random inputs, shared external state and time-cutoff decisions agree. The corresponding actions then agree, and the unchanged engine produces equal next states. Induction proves the conditional extension through termination. Source equality and equal initial states alone do not discharge the external-input and deadline hypotheses. This proves the conditional claim.

V's earliest Fortress38 decision is six, from actual gold 605, thirty-six factories, 800 HP, W+X and one active tier4 against 476 gold, twenty-eight factories, 740 HP, W+X and six active tier2 entries. Its closure was constructed earlier but has consumed no observations. Its history therefore still has the factory's initial values, including empty own_cells and no previously selected replanned layout. The scripted W+X cells were not requested by that closure. Its foreign-map detection can treat them as foreign and invoke replanning if the existing layout fails its capacity condition. Creating a new defender at six would require separate constructor-equivalence justification; advancing it and discarding decisions during the first five rounds would define a different policy. This proof specifies neither alternative.

Round six is also H's second guard round, now predicting from V's actual state including the visible tier4. The empty-threat calculation used for round five no longer applies. L4 may build defenses or invoke its repair replacement, while V may defend, replan or attack through Fortress38. H's lead and deadline triggers and its later frozen Fortress34 planning also remain active in the model. Fortress38 and Fortress34 `plan_defense` use three-second default search budgets; this matters for later matched-history tests even if no engine call fails. There is no proved continuation value from the five-round table.

The proposal that V removes the six round-four hits is proved under the hypotheses. The proposal that V's round-five heavy purchase hits once is also proved, rather than left as an unexamined assumption. The stronger statement that V removes the purchased tier2 roster is false: only the per-round combat copies die. The statements that V wins the complete game, always preserves its 60-HP advantage, or establishes an unrestricted counter-strategy cycle are OPEN. No full-game empirical result for V is used here. No failed arithmetic deduction was hidden or replaced by a favorable measured case.

This is a targeted counter designed after examining the disclosed T/U mechanism. It is not a held-out opponent. Any future experiment should declare exact V/T and V/U specifications, both physical assignments, the opening predicates above and failure rules before calls. It should keep a failed opening or timed-history comparison visible, and separate successful audits from favorable WDL hypotheses. An independent full-engine replay and a fresh model-state audit remain future verification tasks. No such task is claimed complete by this source proof.

## Dependencies and identities

The rules and source paths below are relative to the project. Hashes were read at preparation without importing these modules. The data rows identify constants and witnesses; the argument above proves the relevant route, exposure and arithmetic facts instead of treating stored simulation outcomes as proofs. Prior T/U proofs supply development context; the current argument states and proves its own five-round conclusion.

| Source or data | SHA256 |
| --- | --- |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `configs/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/actions.py` | `d3b482371c4bf43f3da0028b4425d899be1b949a97a2c786617ee813a15f5f66` |
| `td_game/combat.py` | `17265171d1e2ab4c60b07f9b4f473a19667aef4a2110aeb2c07f1cb39f965228` |
| `td_game/pathfinding.py` | `5ecce5a8737d43e3add703e4143f28a1d2bb8fb62e84a2d7f29be441749ae8b2` |
| `td_game/state.py` | `5d6df44f76a0f84d95d130e080a2e966bad02d06e08824cc818d6b08185b375f` |
| `td_game/config.py` | `ab1ca08d78081382e9f9a4ca7bff4985d101ec7b7621ecddfa48e46418701716` |
| `bot_research/bots/counters/third_round_wait.py` | `25e84fb1ec28ece5e2e8b9d32be2f1d962794069a1b3c8ac6b824afb5a3b7cc2` |
| `bot_research/bots/counters/blind_fourth_round.py` | `2a064ba6d912c8ac177263b552b4c19e030f9e9168e3575704ac20c7e41cfea7` |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/wall_signal_repair.py` | `d82b22386b5973ecfc6cbcb984eb6d91d1ca5ede4c6c16ffa693c05b32e81226` |
| `bot_research/bots/counters/wall_signal_timing.py` | `63d7681bec8ac9fb5c3855d172be8c2e3a6b3a591bdf8e746efc1d9b4e754146` |
| `bot_research/bots/counters/forecast_timing.py` | `31e73f1a98f8cb70b9ddacfd2067a34e752450c53648a42482d934fcc92be78a` |
| `bot_research/bots/counters/stateful_public.py` | `c2cde121ecf8c1475daee2958f97a1a1b9c08794bee4cf6ead7a05924b4c2c7b` |
| `bot_research/bots/counters/public_factory.py` | `c9bbd0886fbd03c15fdb7c5b716abfce5e92e94eedd0658f459daf2a37597d32` |
| `bot_research/bots/counters/shared_prefix_selector.py` | `7b2c2a0c570f140cf84a5908293bc7835718652a4c71ec2071745e3e61c1c5e7` |
| `bot_research/bots/counters/hp_handoff.py` | `c5baa3d7af48508d0cf10cbac0950a018673c45e3b3cba3f0522324da5ea8ee6` |
| `bot_research/bots/counters/screened_guard_maze.py` | `d0df94929a24405a959a0f686a4dadf16da8317176b3bf9074fd82562afe4cc4` |
| `bot_research/bots/counters/staged_guard_maze.py` | `32778c35fda27c0432aa9f4931756bde33f156adabf44306e2548c773a977351` |
| `bot_research/bots/counters/maze_grower.py` | `d541a6f2de7b44e6280c7296b58f6844bb2bebf574dcf8f0f32e7c1a7dbfd5f0` |
| `bot_research/bots/counters/visible_search.py` | `107fc8d7a13fdad496c2316f969e3ba59b70f69d3dbdc106904edcbe653015c5` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/bots/counters/data/maze_layouts_001.json` | `1f290c5da4b90c151c15ddf98e54055b427678addd8441363fead6163b812dd7` |
| `bot_research/bots/counters/data/staged_guards_001.json` | `fdc86066da88290d4d0c82f1c53895174f0ee38250ee18fb29fd425eba8c8398` |
| `bot_research/bots/counters/data/screened_guard_001.json` | `c0980d0c46cf813f82d3eae5e26e18fab2d74f8135a87d4ad550eddc804ffde6` |
| `bot_research/bots/counters/data/screened_roster_guard_001.json` | `d0e5fc4db60129a26d5e851dc9b9faf4231c609adc412dbea11cf1b9144900f0` |
| `bot_research/bots/economy/frozen/v2/defense_plan.py` | `7ac8fdac9804db47e56896a3f9a97f602a8aed23acbc6aca9e0cb85e3bcfe5f4` |
| `bot_research/bots/economy/frozen/v2/fastsim.py` | `01563acb71ad0485c602266584ca4a0ec01783a7f239b03a4c1603feb160f83a` |
| `bot_research/bots/economy/frozen/v2/threat.py` | `ee63f0050f43fe9a2e488ae16b78129b1eba1ae3ad725a2ebf129ddff96b972b` |
| `bot_research/bots/economy/frozen/v17/freeplan.py` | `337be65fc35f6534581cfecb48a648758337dfbd1b6f50d33fef155a848648fb` |
| `bot_research/bots/counters/snapshots/lead_planner_003.py` | `49db78389fc2e32748da1315d0eedd8b2b4e4511c8b4a57c17708c9ebbc7ee93` |
| `bot_research/bots/defense/frozen/v38/fortress.py` | `a6a8f2aec2a97f31779f3caa98951ab81c12ac2d632a989683313b3e7c69c72c` |
| `bot_research/bots/defense/frozen/v38/plan.py` | `6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f` |
| `bot_research/bots/defense/frozen/v38/replan.py` | `3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994` |
| `bot_research/bots/defense/frozen/v34/fortress.py` | `108a4e2e943031faa50ebb20dd2c892e53937f53a932f06d4cd57c5070d93747` |
| `bot_research/bots/defense/frozen/v34/plan.py` | `6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f` |
| `bot_research/experiments/validation/analysis/third_round_wait/PROOF.md` | `7a14fb1e7b062493555761a72aca55e8d21a88393fcb09d65364c98705468ca9` |
| `bot_research/experiments/validation/analysis/blind_fourth_round/PROOF.md` | `878f134149895df9d5672a93142a9533df3bdf9d0b9cca387c5ad77b564b3d2f` |

This inventory pins direct opening dependencies, the five existing counter data files and sources identifying the later handoff and time-budget caveat. It is not a substitute for a complete transitive executable-source and data closure in a future experimental declaration. In particular, no new V policy source exists at this preparation time.
