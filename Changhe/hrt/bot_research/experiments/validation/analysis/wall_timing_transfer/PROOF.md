# Moving the reserved guard from round two to round three

Written 2026-10-31T21:46:40Z. This is the informal source proof and prospective specification for protocol 160. No new transfer game or policy decision was run to write it.

Read the definitions and hypotheses first, followed by the route proof, the opening calculation, its limits, and the proposed finite comparison. The mathematical opening claim is proved below. The new full-game comparisons remain unmeasured here.

## Definitions, hypotheses and dependencies

Let Q be a fresh `ReservedWallGuard()` from `bot_research/bots/counters/reserved_wall_guard.py`, and S a fresh `LateReservedWallGuard()` from `bot_research/bots/counters/late_reserved_wall_guard.py`. Both inherit `EarlyWallGuard(witness="guard00")` through `DelayedWallGuard`. Q changes its private witness to build walls in round two; S changes that same instance field to round three. Each constructor reads a fresh JSON object, so neither change edits shared witness data. Both retain the splash purchase in round three, one tier4 purchase in round four if affordable, and the frozen Fortress38 defender from round five.

In round three, both policies first obtain their parent's proposed list. They keep its non-factory prefix and choose the largest prefix of its trailing factory purchases whose projected settlement leaves at least 260 gold. Their projection uses exact own path income and factory income, with zero outgoing-hit bounty. The implementation decreases the proposed factory count until the target is met, or stops at zero. Only the returned round-three factory count changes; subsequent decisions reconstruct spending state from the real observation.

Assume the unchanged bundled standard start and rules: a 12 by 12 board with spawn (0,0), base (11,11), 100 initial gold, 800 initial HP, empty buildings and roster, and no factories. Walls cost 1, a splash costs 60, factories cost 20 and earn 15 per round, own path income is 1 per edge, outgoing base hits earn 5 each, and tier4 costs 260. Use valid consecutive observations of one player from round one, with no external mutation of the policy or engine state. An opponent can choose any legal actions allowed by these rules. Claims about a decision are conditional on reaching that decision.

The semantic dependencies are `td_game/engine.py`, `td_game/actions.py`, `td_game/combat.py`, `td_game/pathfinding.py`, `td_game/config.py`, `td_game/state.py`, and `td_game/balanced.json`. The opening additionally uses the four guard policy files named above, `bot_research/bots/counters/visible_search.py` for snapshot reconstruction, and `bot_research/bots/counters/data/early_wall_guard_001.json`. The retained continuation is `bot_research/bots/defense/frozen/v38/fortress.py` and its dependencies. The earlier proofs at `bot_research/experiments/validation/analysis/reserved_wall_counter/PROOF.md` and `bot_research/experiments/validation/analysis/late_reserved_wall_counter/PROOF.md` provide related calculations; this argument spells out the comparison without assuming their empirical conclusions.

## Exact route lengths and construction legality

The ordered guard00 walls are (0,1), (1,1), then (x,1),(x,3) for x=2 through 9 in increasing order, then (10,3),(11,3). There are 20 walls. Its only turret is a splash at (1,3).

An empty board has shortest path length 22 edges: the horizontal and vertical displacements are each 11, and a monotone route attains their sum. With the walls, row one is blocked at x=0 through 9 and row three at x=2 through 11. Every route must first cross row one at x at least 10 and subsequently first cross row three at x at most 1. Its horizontal travel is at least 10+9+10=29 and vertical travel at least 11. The axis-aligned route through

    (0,0), (10,0), (10,2), (1,2), (1,4), (11,4), (11,11)

avoids the walls and has 40 edges. Thus the walls alone give shortest path length exactly 40.

After the splash occupies (1,3), row three is traversable only at x=0. Horizontal travel is now at least 10+10+11=31, while vertical travel remains at least 11. The route through

    (0,0), (10,0), (10,2), (0,2), (0,4), (11,4), (11,11)

avoids every building and has 42 edges. Backtracking cannot lower either coordinate-variation bound, so the final shortest path length is exactly 42. These length claims do not require any particular choice between tied shortest routes.

The final route also survives every construction prefix. All proposed cells are distinct, in bounds, and different from spawn and base. The budgets below cover each prefix. Therefore the engine's placement, affordability and route checks accept every proposed wall and splash. Factory purchases do not occupy cells or change the route.

## Conditional opening theorem and proof

For any legal opponent and either physical player assignment, the following values hold at the end of every listed round that is played to settlement. If the game reaches round four, the entire table applies. Here F is cumulative factory count and path length is measured in edges.

| Policy | Round | Submitted opening actions | End gold | End F | Path |
|---|---:|---|---:|---:|---:|
| Q and S | 1 | 5 factories | 97 | 5 | 22 |
| Q | 2 | 20 walls, 3 factories | 177 | 8 | 40 |
| S | 2 | 4 factories | 174 | 9 | 22 |
| Q | 3 | splash, 3 factories | 264 | 11 | 42 |
| S | 3 | 20 walls, splash, 2 factories | 261 | 11 | 42 |

Neither policy buys a minion in rounds one through three. Their own rosters remain empty, so their outgoing spawned-minion and base-hit counts are zero. Thus no omitted outgoing-hit bounty can affect these balances. Under `combat.py`, incoming combat subtracts HP and modifies ephemeral combat copies; it does not destroy buildings, remove factories, or deduct gold. The engine completes combat and credits path, factory and outgoing-hit income before checking the round's outcome. Opponent purchases occur on the opponent's own state. Consequently incoming attacks do not alter the following economic calculation, even if the completed round is terminal.

In round one both factory loops spend 100 on five factories, then receive 22+5*15=97. In Q's round two, walls cost 20; three factories cost 60 and leave 17. Settlement gives 17+40+8*15=177. In S's round two, four factories cost 80 and leave 17. Settlement gives 17+22+9*15=174.

Q starts round three with 177 and eight factories. The splash leaves 117. Its parent would propose five factories. For a retained count k in {0,1,2,3,4,5}, the exact projected and actual settlement gold is

    q4(k) = 117 - 20k + 42 + 15(8+k) = 279 - 5k.

The requirement q4(k)>=260 holds precisely for k<=3 among these integers. The descending reservation loop therefore retains three factories, giving 264 gold and eleven factories. Four factories would leave 259, and five would leave 254.

S starts round three with 174 and nine factories. The walls and splash cost 80 and leave 94. Its parent would propose four factories. For k in {0,1,2,3,4},

    s4(k) = 94 - 20k + 42 + 15(9+k) = 271 - 5k.

The requirement s4(k)>=260 holds precisely for k<=2. The loop therefore retains two factories, giving 261 gold and eleven factories. Three would leave 256, and four would leave 251. Each policy withholds exactly two of its parent's proposed factories. Maximality here is only among prefixes of that parent's fixed factory list with its fixed construction; it is not an optimality claim over all possible openings.

At the end of round three, the own building lists agree, including insertion order: the same 20 walls followed by the splash. Both rosters are empty and both factory counts are eleven. Q has three more gold. If round four is reached, each retained parent branch buys exactly one tier4 for 260. Q then has four gold and S one, both below the 20-gold factory cost. Hence neither buys a round-four factory. This proves the claimed opening comparison.

## What the theorem does not establish

The theorem does not require or imply equal HP. Q's round-two path is longer, and the opponent can react to its walls in round three. S exposes an empty map for another completed round. Different visible factories and gold are additional observations. Even if both maps later agree, their past observations and the opponent's private state can differ. Opponent purchases can therefore fork, as can its map, roster, economy and HP. S also changes the spending and income schedule, so this comparison does not isolate a public signal alone.

Equal maps and factory counts at the start of round four do not prove equal future histories or WDL, and Q's three-gold advantage does not prove dominance. An opponent can exploit information or HP differences in either direction. Early termination is possible under the theorem's hypotheses; a future empirical assertion that every declared game reaches round four must test that additional condition explicitly.

## Concrete prospective transfer comparison

The fixed opponent set contains F44, F45, V29, V29_g1, V31_g1f, H, G and N. Constructors below use fresh instances, with unspecified parameters equal to the inspected frozen defaults.

F44 is `bot_research.bots.defense.frozen.v44.fortress:@make`; F45 is `bot_research.bots.defense.frozen.v45.fortress:@make`, each without overrides.

For the economy opponents, define parameter block E by the following exact JSON values:

```json
{
  "free_fallback": "zero", "foreign_attack_from": 11, "doom": "next",
  "fac_cap": 400, "sat_reach": true, "replan": true,
  "foreign_sat_from": 11, "replan_gain": 400, "replan_base": true,
  "own_in_layout": "replan", "own_min_s": 1200,
  "min_cap": 3000, "active_cap": 4000,
  "fill": true, "fill_reserve": true, "fill_threat": true
}
```

V29 is `bot_research.bots.economy.frozen.v29.econ29:@make` with E, retaining its default `attack_from=2`. V29_g1 uses the same constructor and E plus `attack_from=7`. V31_g1f is `bot_research.bots.economy.frozen.v31.econ31:@make` with E plus `attack_from=7` and `fill_own=true`. In particular, the label V29 here does not mean a constructor with no overrides. The E block and g1 setting retain the screened-transfer convention recorded in `bot_research/experiments/validation/screened-guard-transfer-02-001.json`.

H is `bot_research.bots.counters.hp_handoff:@make` with `layout="empty"`, `growth_rounds=6`, `bait=[]`, `bait_round=2`, `tier="tier5"`, `factory_cap=2000`, `purchase_cap=1000`, `replan_iters=5000`, `deadline=12`, and `lead_from=8`. Remaining defaults include `lead_margin=0`, `panic_hp=null` and `panic_from=2`. Here deadline is a round trigger. G is `bot_research.bots.counters.early_wall_guard:@make` with `witness="guard00"`. N, also named AS1C, is `bot_research.experiments.lead.frozen.best_v9e:@make` with `attack_share=1.0` and `catch_up_share=0.5`.

Run Q and S against the first six opponents, once in each physical assignment: 2 candidates times 6 opponents times 2 assignments gives 24 new games. Reuse the eight already existing Q/S versus G/N games, identified through the full-game receipts in `analysis/reserved_wall_counter/verification/full_games.json` and `analysis/late_reserved_wall_counter/verification/full_games.json`, relative to `bot_research/experiments/validation/`. These reused records are prior evidence, not new observations. Their exact source, parameter, action and terminal-history compatibility must be checked before pooling them. The full comparison then has 32 records and 16 matched conditions, one condition per opponent and candidate seat.

The falsifiable hypotheses are:

1. H1: in every one of the 16 matched conditions, S's WDL is at least Q's, ordering win above draw above loss. Any strictly lower S result refutes H1; wins elsewhere do not compensate for it.
2. H2: for each of the 12 new candidate/opponent pairs, complete normalized histories agree between the two physical assignments. Normalize by candidate/opponent identity consistently, retaining ordered actions and receipts, snapshots, combat and income values, and terminal result. Exclude only declared non-game metadata such as wall-clock timing and consistently relabeled player names. This compares seats within a fixed candidate/opponent pair, not Q's history with S's.
3. H3: all 32 declared games reach round four and exhibit the exact opening table and round-four purchase above. Any early terminal game refutes this full-reaching empirical hypothesis. It must remain in the denominator, even though it does not contradict the conditional theorem.

Before the new calls, pin the exact candidate/opponent specifications, full source and data dependency closure, checking code and this proof. Preserve each raw action transcript and complete terminal record. Validate actions with the unchanged engine, replay every completed history through the true terminal outcome, and independently regenerate both policies' decisions on every recorded observation of each new history, starting with fresh policy state and advancing it consecutively. A mismatch is an evidence-validity failure requiring investigation; it is not a passing WDL comparison. Check reused controls against their original pinned artifacts and distinguish fresh checks from retained earlier receipts.

Later frozen planners contain wall-clock stopping branches. Source identity and equal initial states alone do not prove reproducible decisions or seat symmetry. H2 and the decision checks therefore remain empirical obligations. The 32 records are a selected finite development comparison, with paired deterministic conditions and eight reused records, not 32 independent random draws. Even confirmation of all three hypotheses would establish only their exact finite claims. It would not establish global superiority, held-out strength, or optimality of either policy. No final `best.py` or reserved D validation is changed by this proposed experiment.

## Source identity and current status

The inspected opening inputs have these SHA256 values:

| Project-relative file | SHA256 |
|---|---|
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/actions.py` | `d3b482371c4bf43f3da0028b4425d899be1b949a97a2c786617ee813a15f5f66` |
| `td_game/combat.py` | `17265171d1e2ab4c60b07f9b4f473a19667aef4a2110aeb2c07f1cb39f965228` |
| `td_game/pathfinding.py` | `5ecce5a8737d43e3add703e4143f28a1d2bb8fb62e84a2d7f29be441749ae8b2` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/delayed_wall_guard.py` | `95302b8c25266b38c9e5a3b195c32d7715d7e95a4d5ca058d1a222437d119f82` |
| `bot_research/bots/counters/reserved_wall_guard.py` | `f8e7c59d719c601fd7985dc7a9ba5ff5784a3175ae2a58beb0f597153a95da7e` |
| `bot_research/bots/counters/late_reserved_wall_guard.py` | `2c862cb19d15aa563f0a30219ebd501020f75a5096045d60cf018cefdf2b2ce2` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |

These hashes identify central inspected inputs, not the complete future declaration map. This proof uses the bundled current combat rules, including their known difference from the repository's historical protected-file manifest; it makes no repair to that baseline. The opening theorem is established under its stated hypotheses. H1, H2 and H3 remain OPEN pending the declared transfer experiment and its verification. Existing G/N outcomes do not supply the missing six-opponent results.
