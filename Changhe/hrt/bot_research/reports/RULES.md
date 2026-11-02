# Game contract under the bundled rules

This file records the rules the research uses. Every statement is taken from
the bundled source (file and line numbers refer to the working copy as
received) and, where marked [repro], is checked by
`bot_research/experiments/lead/rule_repros.py` on the unchanged engine
(10 of 10 checks pass). Where the documentation and the code disagree, the
code is authoritative, as the task requires.

## 1. Source and integrity baseline

- Authoritative configuration: `td_game/balanced.json` (loaded by
  `td_game.config.balanced_config`, config.py:152); `configs/balanced.json` is
  byte-for-byte identical. `--balanced` uses the bundled copy.
- The protected-file manifest `bot_research/protected_files.sha256.json` lists
  1041 files. At the start of the research (2026-10-31, first shift) the working
  copy differed from it as follows; this is the starting state and was not
  repaired: 1002 entries absent (1000 historical records under `data/games/`;
  only `data/games/game_000001.jsonl` is present, plus `.DS_Store` and
  `td_view/.DS_Store`), and three files with hashes different from the
  manifest: `td_game/combat.py`, `tests/test_engine.py`, `tests/test_rules.py`.
  One file outside `bot_research/` is not in the manifest:
  `bot_research.prompt.md` (the task prompt). The full starting state, with the
  SHA-256 of every file outside `bot_research/`, is
  `bot_research/reports/integrity_baseline.json`; the check is
  `python -B -m bot_research.harness.integrity`.
- The existing tests pass on the copy as received: 59 run, 9 skipped (the
  skipped tests need the optional pandas extra).
- The supplied historical record uses an older balance (wall cost 5; minions
  scout/brute/titan; turrets gun/mortar/laser) and says nothing about current-
  rules strategy. The historical bots' source is not available.

## 2. Exact parameters (td_game/balanced.json)

| Global | Value |
| --- | ---: |
| map | 12 x 12, spawn (0,0), base (11,11) (config.py:97 rejects anything else) |
| initial HP / gold | 800 / 100 |
| max rounds | 50 |
| ticks per round | 250 (ticks 0..249) |
| roster lifespan | 12 rounds including the purchase round |
| factory cost / income per round | 20 / 15 |
| path income per step | 1 |
| base-hit bounty | 5 |
| wall cost | 1 (walls never attack: damage 0, range 0.0, cooldown 1) |

| Minion | Cost | HP | Damage on arrival | Speed |
| --- | ---: | ---: | ---: | ---: |
| tier1 | 15 | 20 | 5 | 1 cell/tick |
| tier2 | 40 | 70 | 12 | 1 |
| tier3 | 100 | 180 | 26 | 1 |
| tier4 | 260 | 560 | 60 | 1 |
| tier5 | 650 | 1500 | 140 | 1 |

| Turret | Cost | Damage per tick | Range (Euclidean) | Targets |
| --- | ---: | ---: | ---: | --- |
| gun1 | 30 | 8 | 2.5 | one copy: the frontmost in range |
| gun2 | 80 | 22 | 3.0 | one copy: the frontmost in range |
| gun3 | 200 | 55 | 3.5 | one copy: the frontmost in range |
| splash | 60 | 10 | 0.0 (aoe 8) | every copy on the 8 neighbouring cells |

All turrets have cooldown 1 (attack every tick). The engine rejects other
speeds, cooldowns, AOE values or a splash range other than 0.0 (config.py:123-135).

## 3. Round structure (engine.py:70-109)

1. Observation. Both bots receive `Engine.observation(p)` built from the state
   after the previous round settled: `round` (the round about to be played,
   1-based), `player`, full snapshots of both players (HP, gold, factories,
   turret and wall counts, current route length, all buildings, the whole
   roster with `remaining_rounds`), and the full rules. The adapter deep-copies
   both observations before calling either bot (protocol.py:39), so a bot cannot
   change the engine or the other bot's input [repro].
2. Hidden simultaneous decisions. Both returns are collected before any action
   is applied; neither bot sees the other's current submission. The adapter
   calls bot A then bot B in the same process without sandboxing; inspecting the
   caller's frames would reveal A's pending list to B. Research bots must not
   do this (task rule) and ours do not.
3. Actions. The two lists are applied interleaved A[0], B[0], A[1], B[1], ...
   (engine.py:81-87). Each action changes only its own player's gold, roster,
   factories or map, so the interleaving cannot change any outcome; it only
   sets the `order` field of action events.
4. Combat on both maps with the routes recomputed after all actions
   (engine.py:88-90). Both maps are always simulated completely.
5. Income for each player: `(own route length) * 1 + factories * 15 + own
   successful hits on the opponent's base * 5` (engine.py:97-101). Factories
   bought this round already pay this round. Route length is that of the
   player's own (defensive) map after this round's construction [repro].
6. Roster expiry: entries with `expires_after_round <= round` are removed
   after income (engine.py:103-105).
7. Outcome (engine.py:111-119): if both HP <= 0, draw (`both_bases_destroyed`);
   if one HP <= 0, the other wins (`base_destroyed`); otherwise after round 50
   the higher HP wins and equal HP is a draw (`round_limit`). HP may be
   negative [repro]. Income is still credited in the final round.

## 4. Actions and construction legality (actions.py)

- `buy_minion {type}`, `buy_factory`, `build_turret {type,x,y}`,
  `build_wall {x,y}`. There is no limit on the number of actions, walls,
  turrets or factories. Each action is validated on its own; a rejected action
  costs nothing and later actions still apply.
- Check order (actions.py:16-51): object, known op, known type, then for
  buildings integer coordinates (booleans and floats rejected), inside the map,
  not spawn/base, cell not occupied by one of the player's buildings, a route
  must still exist with the new cell blocked, and only then gold. So a placement
  that is illegal is reported with its placement reason even if gold is also
  insufficient [repro].
- Turrets and walls both block movement. Buildings are permanent: no selling,
  replacement, upgrade or removal. Factories occupy no cell.
- A minion purchase charges its cost once and appends a roster entry with
  `bought_round = r`, `expires_after_round = r + 11`. The entry fights in round
  r (the purchase round) and in the next 11 rounds [repro].
- Practical limit (not a rule): factory compounding makes unbounded
  "buy as many as possible" policies produce millions of actions per round; an
  uncapped factory-only bot produced a 1.1 GB log in one match. All research
  bots cap their action counts.

## 5. Routes (pathfinding.py)

- Breadth-first search from spawn with neighbour order right, down, left, up;
  a cell's parent is the first cell that discovers it; the route is the BFS tree
  path to the base. It is a shortest route and is unique and deterministic for a
  given set of blocked cells (independent of building order). The empty map
  gives row 0 rightwards then column 11 downwards, length 22.
- Route length (`length_path`) counts moves (cells - 1). Minions never block
  each other and never affect routes. Routes are recomputed every round after
  construction and are never stored in logs.

## 6. Combat (combat.py)

- Spawning: the active entries (bought_round <= r <= expires_after_round) are
  taken in roster (purchase) order and densely indexed k = 0, 1, ... after
  skipping expired ones; entry k spawns at tick `k % 250` (combat.py:19-24).
  More than 250 active entries put several copies on the same tick and cell.
- Each copy is a fresh full-HP copy every round; deaths do not remove roster
  entries; copies still alive after tick 249 are discarded without base damage
  (`cleared`) [repro].
- Tick order (combat.py:27-66): (1) spawn scheduled copies at path index 0;
  (2) every copy that existed before this tick advances one cell; (3) a copy that
  reaches index L (the base) deals its damage immediately, scores a hit and is
  removed, before any attack; (4) every turret selects and accumulates damage
  against the remaining copies; (5) copies with HP <= 0 are removed.
- Consequences: a copy spawned at tick s is at index t - s at tick t and arrives
  at tick s + L, which counts only if s + L <= 249 [repro]. On a route of length
  L only spawn ticks 0..249-L can ever reach the base. Every copy that survives
  is attacked exactly once at each index 0, 1, ..., L-1 (the spawn cell on its
  spawn tick included) and never at the base cell.
- Guns (aoe 0) are single-target: each gun damages only the copy with the
  greatest path index among copies within Euclidean distance <= range
  (boundary included); ties go to the earlier copy in spawn order
  (combat.py:51-60). All turrets select before damage is applied, so several
  guns can hit the same frontmost copy and damage beyond its remaining HP is
  wasted [repro]. tests/test_engine.py (`test_guns_target_furthest_progress_in_range`,
  `test_same_cell_copies_are_not_splash_targets_for_guns`) asserts this.
  docs/game.md says "Every gun attacks every target in range each tick"; that
  sentence does not describe the bundled code.
- Splash (aoe 8, range 0.0) damages every copy whose cell is at Chebyshev
  distance exactly 1 from the splash cell: the 8 neighbours including diagonals,
  not its own cell (which is a building and can never hold a copy). Copies
  sharing a cell are all damaged [repro].
- Damage from all turrets accumulates per copy within a tick; there are no
  projectiles, armor, slowing, line of sight or kill rewards.

## 7. Derived facts used by the research (proved from the rules above)

- P1 (splash immunity). Let S(map) = 10 x sum over route indices i = 0..L-1
  of the number of splash turrets adjacent (Chebyshev distance 1) to route cell
  i. Every copy that is still alive at index i receives that index's splash
  damage, regardless of how many copies exist. Hence no copy whose type has
  HP <= S(map) reaches the base: a copy with enough ticks left to traverse the
  route dies on it, and a copy that spawns too late to traverse it is cleared,
  possibly alive, when combat ends. So the map takes zero base damage in that
  round from any roster made only of such types, of any size and order. (Proof:
  a copy is attacked at each index 0..L-1 it occupies alive; the splash part of
  the damage at index i does not depend on other copies; the sum over all
  indices is S(map) >= HP. Gun damage only adds.) The literal statement "every
  such copy dies" is false: the validation worker executed a legal game with one
  splash (S = 30)
  and 250 tier1 bought in round 9, in which 249 copies die and one is cleared
  alive with 10 HP, with zero base damage
  (experiments/validation/analysis/late_copy_cleanup/PROOF.md).
- P2 (visible threat bound). At decision time a player sees the opponent's
  gold g and roster. Any entry that can fight in this round is either in the
  visible roster (and active this round) or bought this round with cost <= g.
  So if S(map after this round's own construction) >= max HP over the active
  visible entries and over every type with cost <= g, the player takes no base
  damage this round (from P1).
- P3 (interleaving irrelevance). The final state after the action phase does
  not depend on the interleaving order, because each action reads and writes
  only its own player's state (actions.py).
- P4 (route invariance). The route depends only on the set of blocked cells,
  not on the order or type of buildings.
- P5 (arrival window). A route of length L admits at most 250 - L spawn ticks
  that can reach the base; entries whose index k satisfies k % 250 > 249 - L
  never hit.

## 8. Discrepancies and open points

- docs/game.md (Paths and combat) describes guns as hitting every target in
  range; the bundled combat.py and tests implement single-target, frontmost.
  The manifest hash of `td_game/combat.py` (and of the two test files) differs
  from the working copy, consistent with the targeting rule having been changed
  after the manifest was made; the bundled code is used.
- docs/game.md calls the splash neighbourhood "provisional"; the code fixes it
  to the 8 neighbours.
- The adapter has no time limit and no sandbox; decision time is measured and
  reported by the harness instead.
