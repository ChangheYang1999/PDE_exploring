# Two indistinguishable opening rounds and a restricted selection bound

Written 2026-10-31T21:37:43Z from source and retained-artifact inspection, before prospective verification code for this result. No policy decisions, games or replay execution were performed. The S payoff premises below are unmeasured at this stage.

Read the definitions and selector class first, then the opening and private-state lemmas, the conditional payoff theorem, and the verification requirements. The source lemmas concern a fixed standard start. The numerical bound is an exact conditional theorem, not an empirical S result.

## Policies, observations and rules

G is `EarlyWallGuard(witness='guard00')` from `bot_research/bots/counters/early_wall_guard.py`. L is `WallSignalRepair()` from `bot_research/bots/counters/wall_signal_repair.py`, with no overrides. S is `LateReservedWallGuard()` from `bot_research/bots/counters/late_reserved_wall_guard.py`. S uses its own guard00 witness with `wall_round=3` and retains the round-three reservation routine inherited from `ReservedWallGuard`. Its detailed construction and reservation proof is `bot_research/experiments/validation/analysis/late_reserved_wall_counter/PROOF.md`.

H is `HPHandoff` with exactly the `HP_PARAMETERS` in `bot_research/bots/counters/shared_prefix_selector.py`:

    layout='empty', growth_rounds=6, bait=[], bait_round=2,
    tier='tier5', factory_cap=2000, purchase_cap=1000,
    replan_iters=5000, deadline=12, lead_from=8.

Other arguments have their current defaults: lead_margin=0, panic_hp=None and panic_from=2. `HPHandoff` fixes upgrade_round=9; its screen-aware opening fixes splash guard rounds to (4,6). Its defender is frozen Fortress34, constructed with attack='none', round1_poke=0 and replan_iters=5000. The parameter deadline=12 is a round-number trigger, not a twelve-second runtime allowance. These specifications match the H definition in `bot_research/experiments/validation/ten-policy-game-declaration-001.json`.

Use the unchanged bundled standard rules: 12 by 12 grid, spawn (0,0), base (11,11), 800 initial HP, 100 initial gold, no buildings, factories or roster, wall cost 1, factory cost 20, factory income 15 and path income 1 per edge. The round limit is 50. Calls start in round one and use consecutive valid engine observations for a fixed physical player index. All calls succeed; no external code mutates owned member state. Midgame initialization, retries after partial state updates and modified rules are outside the statements.

Fix a physical selector seat s in {0,1}. Let N_s replace only the two `players` snapshot names in an observation by 'selector' at index s and 'opponent' at index 1-s. It preserves the player indices, round number, rules and every other public field. Comparing H with S always keeps the same physical seats. `Engine.observation` exposes names, so equality after N_s is not equality of arbitrarily named raw observations. Initial record metadata can also expose bot specifications; such metadata is excluded from the selector's information.

## The observation-only selection class

A selector in the class has fresh G and L instances and may use normalized public observation history, its own past submitted actions, fixed prior information about this policy family, and private randomness. It may maintain arbitrary memory or perform computations determined by those inputs. It may not inspect opponent identity, names, file names, process identity, another policy object, pending submissions, experiment condition labels or identity-correlated side channels. In particular, elapsed runtime and scheduling observations are not additional identifying inputs to its choice.

Before commitment it returns the shared G/L action list proved below. It permanently commits to one member at some decision no later than round three, before the opponent's round-three submission becomes visible. It then returns that member's actions without alteration or later reselection. The selected member receives exactly the public history it would have received as a standalone policy, with every earlier required transition retained. A concrete implementation can call both private members once per uncommitted round on separate copies, require exact ordered-list equality, and retain both updated states. If it commits earlier, the selected member must still advance once per subsequent round; continuing the unused member is unnecessary.

The selector's private random source has the same distribution against H and S and is independent of which opponent was chosen. A coupling may use the same seed in both comparisons. This independence applies to all random information available for selection, including any randomized member computations inspected before commitment. The adversary chooses a fixed H or S without observing the selector's realized private random choice. The objective will be the minimum of two expected payoffs, not the expectation of a minimum chosen after seeing that choice.

Matching public inputs must induce matching decision-relevant private transitions in the compared prefix executions. This is automatic for the displayed early deterministic branches when sources and initial logical states agree. If external randomness, mutable globals, cached state or deadline branches can affect a corresponding transition, they must be coupled to agree, or be excluded from the selector's available information as appropriate. A fresh seed or extra unused-member computation cannot be assumed harmless to later time-dependent planning without such a condition.

These conditions define a restricted observation-only class. Merely ignoring the string name while consulting an identity-bearing timing or process signal does not meet the definition. A strategy that changes the shared opening, constructs a third response, resets its selected member or switches responses later also lies outside it.

## Lemma 1: H and S have the same two-round public prefix

Let F denote the action `{'op': 'buy_factory'}`. Let W be the ordered guard00 wall list: (0,1), (1,1), then (x,1),(x,3) for x=2 through 9, followed by (10,3),(11,3). There are 20 distinct wall cells. Against either H or S, the selector's common first two lists are W followed by four copies of F, then five copies of F. H and S both submit five copies of F, then four copies of F.

Proof. H's empty layout has no round-one walls and its empty bait has no purchases. In rounds one and two it is still in factory growth, far below the factory cap. Its guards start in round four and its gun extension in round nine. None of its handoff conditions can fire: the round trigger is twelve, the lead condition starts at eight and panic is disabled. It therefore spends only on affordable factories. S's wall round is three, its turret round is three and its minion round is four. Its inherited reservation routine changes only round three. Thus it too spends only on factories in rounds one and two.

An empty map has shortest path length 22 by Manhattan distance, attained by a monotone route. Both H and S therefore buy five factories with the initial 100 gold and finish round one with 22+5*15=97 gold. Round two buys four factories, retains 17 gold and receives 22+9*15=157 income, producing 174 gold and nine factories. Neither has buildings or roster after either round.

G submits exactly W and four factories in round one. Every wall prefix is legal: the route through (0,0), (10,0), (10,2), (1,2), (1,4), (11,4), (11,11) avoids the final walls and hence every prefix. The final map's first wall row can only be crossed at x>=10 and its second at x<=1. Any path has at least 10+9+10=29 horizontal and 11 vertical edges. The displayed route attains 40, so its path income is exactly 40, independently of shortest-path tie breaking. Spending all 100 gold gives round-one closing gold 40+4*15=100. G has no scheduled construction or attack in round two, so it buys five factories and finishes with 40+9*15=175 gold.

For L, `WallSignalTiming` inherits `StatefulPublicTiming`, whose persistent private model is the same H specification. `ForecastTiming.predict` gives that model a copied current observation with the player index changed to the opponent. In round one the model predicts five factories. In round two its already advanced H sees the actual opponent's 97 gold and five factories and predicts four. Neither predicted state has a roster. The defense call has both empty active threat and zero additional threat budget. In frozen economy v2, `threat.packages(0, ...)` reduces to the empty package and `fastsim.simulate` returns zero damage for the empty wave. Consequently `defense_plan.defend` performs no construction. L's attack begins in round three, saturation no earlier than twenty, and repair no earlier than four.

The underlying first list is therefore five factories. `WallSignalTiming` verifies that it contains only factories and replaces it with exactly W followed by four factories. The persistent H transition is retained. In round two L has the same 100 gold as G, returns five factories, and does not replace the list. `WallSignalRepair` leaves both early returned lists unchanged. This proves exact ordered-list equality for G/L and the stated H/S lists.

All rosters remain empty on both sides, so combat causes no damage or bounty. HP stays 800 and the game reaches round three. In each fixed physical assignment, the deterministic engine has the same legal actions, income, building order, roster and rule fields against H and S. Only externally supplied labels may differ. Thus the normalized public observations at decisions one, two and three agree, as do the first two complete public rounds after consistent label normalization. The resulting states are:

| End of round | Selector gold/factories/path | H or S gold/factories/path | HP and roster on both sides |
| --- | --- | --- | --- |
| 1 | 100 / 4 / 40 | 97 / 5 / 22 | 800, empty |
| 2 | 175 / 9 / 40 | 174 / 9 / 22 | 800, empty |

No claim is made about equality after the third submissions. S's round-three construction is new information revealed only after the commitment deadline.

## Lemma 2: both options retain their correct private prefix state

Suppose both private members are advanced once in each of the two shared rounds on separate copies of the actual public observation. Under the transition-coupling conditions above, each member's logical state after either round equals its corresponding fresh standalone member's state on that same history. This compares G with G and L with L; it does not equate G's state with L's.

Proof. Initial corresponding member states agree. In round one each corresponding pair consumes equal observations, with names consistently relabeled if necessary, and matching decision-relevant external inputs. Its actions and next logical state agree. The selector returns that member's exact list because the two lists are shared. The opponent therefore receives the same next public state as in the standalone comparison. The unchanged engine produces the same round-two observation. Repeating the argument proves the second transition and state equality.

L's internal model is not restarted. `PersistentFactoryModel` records last_round=1 and then last_round=2 and retains the same opponent player index. Its same private H object consumes both observations. Replacing L's returned first action list does not discard that model transition, and H reconstructs its spending state from the observed opponent snapshot on the next call. G retains its own witness and traces; its defender is uncalled before round five. These are the corresponding standalone states required to continue either option at round three. If commitment occurred earlier, the same induction applies to the selected member alone.

Inductively continuing a selected member yields whole-game equality with its standalone baseline only when the selected member's and opponent's later decision-relevant inputs are also coupled. Frozen Fortress34 and Fortress38 planning includes wall-clock stopping conditions. Extra shadow work or altered scheduling can change those conditions even with identical source and observations. Equal early states alone do not establish unconditional cross-execution equality for the remainder of the game.

## Conditional theorem: the restricted optimal worst payoff

For each fixed physical selector seat, suppose compatible validated baseline outcomes and continuation coupling give the following payoffs from the selected member's perspective:

| Member | H | S |
| --- | ---: | ---: |
| G | -1 | 0 |
| L | +1 | -1 |

Payoff is +1 for a win, 0 for a draw and -1 for a loss. The continuation condition is substantive: conditional on selecting a member, its full game and the opponent's transitions must reproduce the specified baseline payoff. It is sufficient that corresponding full transitions reproduce the fixed baseline actions, state and terminal result. Matching unconditional averages from unrelated random executions would not by itself supply this condition if member selection were correlated with later outcomes.

Then the supremum, over the defined observation-only selectors, of the minimum expected payoff against H and S is exactly -1/3. It is attained precisely when the probability of choosing G is 2/3. This uniqueness is of the induced probability, not of the selector implementation, private seed representation or commitment round.

Proof. Couple H and S comparisons with the same private selection seed. By Lemma 1 every allowed public input before commitment agrees. Lemma 2 and the prefix transition conditions give corresponding member and selector state. Therefore every allowed computation and commitment event has the same result in the two comparisons. This remains true for a stopping rule that commits in round one, two or three: before any such choice the allowed histories coincide. Hence there is one probability p in [0,1] of selecting G against either opponent, within the fixed physical seat.

By the conditional baseline-payoff premise and the law of total expectation, the two expected payoffs are

    u_H(p) = p*(-1) + (1-p)*(+1) = 1 - 2p,
    u_S(p) = p*0 + (1-p)*(-1) = p - 1.

The restricted worst payoff is f(p)=min(1-2p,p-1). The increasing and decreasing affine terms intersect at 1-2p=p-1, equivalently p=2/3, and both equal -1/3 there. If p<2/3, then p-1<-1/3. If p>2/3, then 1-2p<-1/3. This proves the upper bound and uniqueness of its maximizing probability. Attainment follows by using independent private randomness to choose G with probability 2/3 and L with probability 1/3, preserving the shared prefix and permanently continuing the chosen member with its correct state. This proves the theorem.

Equivalently, an adversary mixing H with probability 1/3 and S with probability 2/3 gives either pure member expected payoff -1/3. This is a certificate only for the displayed two-by-two restricted payoff problem. A deterministic selector has p either zero or one and restricted worst payoff -1. If the same baseline table holds separately in both physical seats, the theorem applies separately in each; allowing seat-dependent selection probabilities does not improve it. Taking the minimum over both seats as well requires p=2/3 in each seat to attain -1/3.

## Evidence requirements and limits

The retained ten-policy receipt `bot_research/experiments/validation/analysis/ten_policy_game/verification/full_games.json` reports G/H losses and L/H wins in both physical assignments. Its declared H parameters match those fixed above. That report is existing evidence, not a fresh replay performed for this proof. No G/S or L/S empirical value is asserted here. In particular, the planned S/G and S/L outcomes must be interpreted from G's or L's perspective, reversing both the payoff sign and the physical member seat when S is the recorded candidate. A future checker must verify exact policy specifications and data/source identities rather than infer compatibility merely from the letters G, H, L and S.

Prospective verification should pin this proof before implementing its checker; identify both-seat G/H, L/H, G/S and L/S controls; recheck their retained source/data and terminal-game receipt edges; and extract the four payoff premises independently. It should compare the full normalized two-round public prefix, retain G and L private prefix-state evidence, and distinguish exact rational algebra from empirical game replay. All eight physical baseline conditions must remain accounted for, including failures or contrary outcomes. If a payoff premise fails, the particular -1/3 application is inapplicable and the observed two-by-two table must be reported instead. The conditional theorem remains a statement about its explicit hypotheses.

The source opening and state arguments are proved under the stated hypotheses. The algebraic theorem is proved conditional on compatible baseline outcomes and continuation coupling. Its application to S remains OPEN. Finite receipts cannot establish all future wall-clock branches. Raw player names can distinguish the policies; later public construction can distinguish them; another opening or response can evade the class. There is no bound here for arbitrary executable policies, unrestricted opponents, all deadline realizations or a global game value. No complete enlarged payoff matrix or formal proof-assistant verification is claimed.

## Dependencies and inspected identities

The source argument uses `td_game/{engine,actions,pathfinding,state,config}.py` and `td_game/balanced.json`; counters `{early_wall_guard,late_reserved_wall_guard,reserved_wall_guard,delayed_wall_guard,wall_signal_repair,wall_signal_timing,stateful_public,public_factory,forecast_timing,shared_prefix_selector,hp_handoff,screened_guard_maze,staged_guard_maze,maze_grower,visible_search}.py`; the corresponding guard and layout JSON files; frozen economy v2 `{defense_plan,threat,fastsim}.py`; and frozen defense v34/v38 planners. Earlier standalone arguments are `analysis/two_round_wall_selector/PROOF.md` and `analysis/late_reserved_wall_counter/PROOF.md`, relative to `bot_research/experiments/validation/`.

The following inspected SHA-256 values identify central dependencies. They are not a substitute for the future declaration's complete transitive source/data and evidence map.

| Project-relative dependency | SHA-256 |
| --- | --- |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `bot_research/bots/counters/shared_prefix_selector.py` | `7b2c2a0c570f140cf84a5908293bc7835718652a4c71ec2071745e3e61c1c5e7` |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/wall_signal_repair.py` | `d82b22386b5973ecfc6cbcb984eb6d91d1ca5ede4c6c16ffa693c05b32e81226` |
| `bot_research/bots/counters/late_reserved_wall_guard.py` | `2c862cb19d15aa563f0a30219ebd501020f75a5096045d60cf018cefdf2b2ce2` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/experiments/validation/analysis/two_round_wall_selector/PROOF.md` | `8184e77444af537621858e15effca9f43424be66b87a66933d445edbde25430f` |
| `bot_research/experiments/validation/analysis/late_reserved_wall_counter/PROOF.md` | `e668e99e984b93c5bc615eca53305da2841320cff9a9bdf23111bc9564febdf5` |
| `bot_research/experiments/validation/analysis/ten_policy_game/verification/full_games.json` | `1405369c8e80081e4177f74fdbffaca454c0ba7f5f5d63e301c5e1d69d343b00` |
