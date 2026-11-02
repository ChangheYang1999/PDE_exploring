# Defense notes (lane hrt-w1)

Newest entry last. Paths are relative to the project root. All measurements use the unchanged
engine (`td_game`) and the bundled `balanced.json`; "route" means the engine's own BFS route
(`td_game.pathfinding.shortest_path`, neighbour order right, down, left, up).

## 2026-10-31T02:05Z  Starting state and integrity

- Manifest `bot_research/protected_files.sha256.json`: 1041 entries, 36 verified, 1002 absent
  (999 `data/games/game_*.jsonl`, `data/games/manifest.json`, `.DS_Store`, `td_view/.DS_Store`),
  3 changed (`td_game/combat.py`, `tests/test_engine.py`, `tests/test_rules.py`). This equals the
  operator's stated baseline. One file outside `bot_research/` is not in the manifest:
  `bot_research.prompt.md` at the project root (present before the run started).
- Existing tests: `python -m unittest discover -s tests -v`: 59 run, 9 skipped, OK.

## 2026-10-31T02:12Z  Rules facts relevant to defense (source inspection, confirmed by tests)

Assumption throughout: the bundled code is authoritative where `docs/game.md` disagrees.

1. Guns are single-target (`td_game/combat.py`, `combat_tick`): each gun adds its damage to the one
   copy in range with the largest path index (ties keep list order, i.e. spawn order). The docs'
   sentence "every gun attacks every target in range" does not match the code or
   `tests/test_engine.py::test_guns_target_furthest_progress_in_range`.
2. Splash (`aoe == 8`, range 0.0) damages every copy whose cell is at Chebyshev distance exactly 1
   from the turret. A copy is attackable at path indices 0..L-1 (one tick each: the spawn tick at
   index 0, then one move per tick); arrival at index L is resolved before attacks. Hence the
   splash damage a copy receives over its whole trip is exactly 10 x A, where A is the number of
   (route cell, adjacent splash) pairs over indices 0..L-1 ("adjacency"). A does not depend on the
   number of copies or their order. If 10 x A >= HP of every type the attacker fields, no copy
   ever reaches the base (a proof, not an estimate).
3. Any copy whose spawn tick k satisfies k + L > 249 never arrives (L = route length). Only the
   dense index k = position among active entries matters.
4. Walls cost 1, are permanent, must leave a route. Any subset of a legal layout is legal (removing
   blockers cannot disconnect), so a target layout can be built in any order over several rounds.
5. Path income = own route length per round. A layout cell therefore repays its wall cost in one
   round if it adds at least one step. Buildings cannot be removed or upgraded, so a cell built as
   a wall can never become a splash: splash capacity (number of high-adjacency cells left open)
   must be planned when the walls go down.

## 2026-10-31T02:19Z  Route length and splash adjacency of layouts (Q1, Q2 groundwork)

Scripts: `bot_research/experiments/defense/explore_geometry.py`, `serpentine_adjacency.py`,
`hand_layouts.py`, `path_length_search.py`, `layout_search.py`. Results in `bot_research/runs/defense/`.

- Default route: along row 0 then down column 11, length 22.
- Horizontal serpentine, wall rows 1, 3, 5, 7 with gaps at x = 11, 0, 11, 0 (44 walls): route 66.
  A fifth wall row (row 9) adds no length (the route already descends column 11). Every wall cell
  touches 6 attackable route cells, the four U-turn pillars (10,1), (1,3), (10,5), (1,7) touch 7,
  the four cells next to a gap touch 4. Top-25 adjacency sum 154 (1540 splash damage with 25
  splashes, enough for tier5's 1500). The vertical serpentine is worse (route 66 but only 27 cells
  at 6) because after the last wall column the BFS runs along row 0, not along the next column.
- Simulated annealing on wall sets (max route length, `path_length_search.py`, 3 seeds x 40000
  iterations): length 44 with 22 walls, 64 with 30, 78 with 41, 82 with 45 (diagonal staircase
  mazes). The length-82 layouts have top-25 adjacency 142-149, i.e. slightly fewer high-adjacency
  cells than the serpentine but 16 more route steps.
- Hand layout "serpentine + bottom wave" (`hand_layouts.py`): serpentine rows 1,3,5,7 plus 3-cell
  pillars at columns 1,3,5,7,9 in rows 8-11 (alternating rows 8-10 and 9-11): 59 cells, route 78,
  41 cells with adjacency >= 6 (7 at 7), top-25 = 157, top-30 = 187. Gun3 best cell covers 21
  route cells (55 x 21 = 1155 to a lone copy).
- Per-gold: a splash at a 6-cell gives 1.0 damage per gold per copy, at a 7-cell 1.17; a gun3 at
  a 21-cell gives 5.8 per gold against ONE copy but its total per round is 55 x (cells + n - 1)
  for a dense stream of n copies, so against >= 8 copies a splash is the better buy.

Uncertainty: the annealer is a heuristic; 82 is a lower bound on the maximum route length.

## 2026-10-31T02:40Z  Q3 component: plan_defense and the fortress bot (first version measured)

Files: `bot_research/bots/defense/plan.py` (component), `simulate.py` (exact planning sim with
leaked-HP tally), `fortress.py` (bot, factory `make`), `geometry.py`;
self-check `bot_research/experiments/defense/check_plan.py`.

API: `plan_defense(observation, budget, required_hp=None, threat_types=None, *, allow_guns=True,
layout=LAYOUT, partial="best") -> list[action]`; helpers `threat_compositions(observation)`,
`plan_walls`, `defense_cost`, `opponent_leak`, `splash_damage`, `LAYOUT` (docstrings in plan.py).

Design (assumptions stated):
- Master layout = serpentine rows 1,3,5,7 + bottom wave (59 cells, route 78). Cells with final
  adjacency >= 5 (30 cells, adjacency sum 180) are reserved for splashes; the 29 others are walls in
  a fixed order (rows 1 and 3 first: 20 walls, route 40-44 once their two pillars are filled).
- Splash plans use the exact adjacency bound (stream independent). Gun plans use exact simulation of
  each threat composition; the greedy metric is 10 x leaked base damage + remaining HP of leaked
  copies, so wounding a copy counts as progress. Both plan families are built for each wall prefix
  (none / through stage A / B / all) and the cheapest zero-leak plan wins.
- Threat compositions for a round: the opponent's visible active roster followed by each of up to six
  alternative purchase bundles its visible gold allows (most expensive tier first, each tier as the
  lead, and a tier1 screen ahead of big copies). Zero leaks against all of them is required.

Verification (`check_plan.py 200`, 02:39Z): simulate_leak equals the engine's simulate_map on 200
random (buildings, roster) cases; 26 random planner zero-leak plans give zero hits in the engine for
every composition, all actions accepted by td_game.actions.apply_action, cost within budget.

Measurements from constructed positions (threat = compositions listed, budget = gold):
- round 1, gold 100, threats [t2,t2] [t1 x6] [t3]: 20 walls + gun2 at (9,5) = 100 gold, zero leaks.
- round 5, gold 560, threats [t4,t4] [t3 x5] [t2 x13]: +4 walls, gun1 (1,3), splash (10,1), gun3 (8,5)
  = 294 gold, zero leaks. Round 6 +gun3 (7,5) = 200 covers [t5] [t4 x3] [t1 x50].
- cumulative defence to round 10 (threats up to 12 x tier5 / 30 x tier4 / 300 x tier1): 2109 gold,
  mostly gun3 in row 5 (a gun3 there covers ~17-21 route cells; 55 x (cells + n - 1) total per round).
- splash-only (stream-independent) schedule from the same positions costs 1589 gold to reach 1530
  per-copy damage (route 72).

Failure case (tournament t1, fortress v1 = "always buy zero-leak vs affordable, partial allowed"):
draws against every rush/turtle baseline, loses to eco_then_flood(switch=8, tier5) with -1540 HP at
round 9 and to eco_then_flood(5, tier4) by -146: the policy spent all 100 gold in round 1 on defence,
had 4 factories by round 7 (104 income) against 135 (2047 income), and then bought useless gun1s as
"best partial" plans. Lesson (empirical): defence spending must be gated by what the economy can
afford; speculative defence against affordable-but-unbought threats must be all-or-nothing, and a
defender without matching economy cannot keep zero leaks against a pure-economy opponent's late
flood. Fortress v2: mandatory zero-leak vs the visible roster, speculative zero-leak vs affordable
purchases only when it costs <= 0.6 x gold, stage-A walls, opportunistic attack when exact
simulation on the opponent's current map shows leaked damage >= 0.1 per gold, then factories.
Sanity (3 matches): beats eco_then_flood(8,t5) at round 8 (HP 214 vs -340), rush t3 (774 vs -175),
greedy_eco (800 vs -340). Tournament t2 running.

Runtime: plan_defense takes 10-700 ms per call in the schedules above, but up to several seconds when
the opponent's gold allows hundreds of copies (big simulations); t1 decide totals were 30-80 s per
50-round match against economy opponents. To be optimised (cap composition sizes, cache).

## 2026-10-31T02:46Z  Tournament t2: fortress v2 variants against the lead's baselines

Command (from the project root, 3 jobs, fresh process per match, both seats):
`python -B -m bot_research.harness.tournament --name t2_fortress_v2_vs_baselines --out-dir
bot_research/runs/defense/t2_fortress_v2_vs_baselines --candidates <4 fortress specs> --opponents
<10 baseline specs> --jobs 3 --keep-logs losses` (specs listed in summary.md). Opponents: greedy_eco,
rush tier1, rush tier3, eco_then_flood(8, tier5), eco_then_flood(5, tier4), splash_turtle, gun_turtle,
maze_eco, random_legal(seed 1), threat_defender. Caveat: plan.py was patched at about 02:58Z while
matches 35-80 ran (the harness recorded the version change as [v:...] for the affected candidate);
the batch is therefore mixed for the pure-turtle variant and the last two candidates. Results:

| candidate (fortress:@make ...) | W-D-L (20) | notes |
| --- | --- | --- |
| default (spec_share 0.6, opportunistic attack from round 3) | 20-0-0 | ends by round 7-17, mean HP diff +968 |
| attack_from=6, attack_share=0.5 | 20-0-0 | mean HP diff +1134 |
| spec_share=1.0 | 18-2-0 | 2 draws = both bases destroyed in round 9 vs eco_then_flood(8, tier5) |
| attack="none" (pure turtle) | 0-8-10 | loses -30 to rush tier1, -26 to rush tier3 (round-1 hits), -586 to the round-8 tier5 flood, -112 to the round-5 tier4 flood, -21.5 to random_legal; draws vs turtles/eco |

Findings (empirical, this pool only):
- Against undefended or lightly defended maps the opportunistic attack (exact simulation of my roster
  plus a purchase on the opponent's current map, buy the tier with the best leaked damage per gold,
  threshold 0.1 per gold) wins quickly, mostly with tier1 swarms (5 damage per 15 gold = 0.33/gold).
- A pure defender cannot win and cannot even draw against a round-1 rush: round-1 actions are blind,
  and full round-1 insurance (zero leaks against everything 100 gold buys) costs the whole 100 gold
  (20 walls + gun2), while the exposure is at most 30 HP (six tier1). It also loses one round of
  damage to a well-timed flood whenever the zero-leak plan exceeds the speculative share (0.6 x gold
  at round 8 was not enough for four tier5s; share 1.0 held HP but the game then ended as a
  simultaneous-destruction draw).
- Decision time: the pure turtle against gun_turtle took 212 s per match (max single call 15.7 s)
  because both sides had very large gold and the gun pass simulated every composition for every
  candidate. Patched after t2 (candidates scored on the worst composition only; gun plans for two
  wall prefixes; reserved-capacity guard). Measured again in check_plan_v3 and t3.
- Saturation capacity guard added to the planner: guns may take a reserved splash cell only while the
  reserved cells still open plus splashes already placed keep final-route adjacency >= 155 (tier5
  needs 150). This answers the failure the economy lane saw in self-play (template filled with guns,
  no splash immunity left, mutual destruction at the end).

## 2026-10-31T02:48Z  Q2 answers: cheapest defences found by the planner, and an external review

Script `bot_research/experiments/defense/q2_cheapest.py`, output `bot_research/runs/defense/q2_cheapest.txt`
(planner with unlimited budget from the empty map at round 1; costs in gold; "stage A" = the 20 layout
walls of rows 1 and 3 already placed, route 40).

(a) Stream-independent splash immunity (per-copy splash damage >= HP), from the empty map:

| HP threshold | cost | buildings | per-copy splash | route |
| ---: | ---: | --- | ---: | ---: |
| 20 (tier1) | 60 | 1 splash at (10,1) on the default route (5 adjacent cells) | 50 | 22 |
| 70 (tier2) | 80 | 20 walls + 1 splash at a U-turn pillar | 70 | 42 |
| 180 (tier3) | 200 | 20 walls + 3 splashes (pillars 7+7, one 6-cell... = 19) | 190 | 44 |
| 560 (tier4) | 804 | 24 walls + 13 splashes | 680 | 50 |
| 1500 (tier5) | 1529 | 29 walls + 25 splashes | 1510 | 72 |

From stage A the same thresholds cost 60, 60, 180, 784, 1509. The 560 row is inefficient (13 splashes
for 68 adjacency): rows 5 and 7 only give 6 per cell once both are closed, so partially closed stage B
places splashes at 3-5 adjacency. Conjecture: a layout whose second stage closes with fewer cells
(e.g. the bottom wave first) would lower the 560 cost; not yet tested.

(b) Zero simulated leaks against n copies of one tier, guns allowed (cost from the empty map /
from stage A):

| tier | n=1 | n=2 | n=4 | n=8 | n=16 | n=32 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| tier1 | 30 / 30 | 30 / 30 | 50 / 30 | 60 / 60 | 60 / 60 | 60 / 60 |
| tier2 | 50 / 30 | 80 / 60 | 80 / 60 | 80 / 60 | 80 / 60 | 80 / 60 |
| tier3 | 100 / 80 | 200 / 180 | 200 / 180 | 200 / 180 | 200 / 180 | 200 / 180 |
| tier4 | 220 / 200 | 420 / 400 | 620 / 464 | 804 / 744 | 804 / 784 | 804 / 784 |
| tier5 | 420 / 400 | 1050 / 1030 | 1529 / 1509 | 1529 / 1509 | 1529 / 1509 | 1529 / 1509 |

A lone tier5 is stopped by 20 walls + two gun3 at the pillars (10,1), (1,3) for 420; from four tier5s
on, splash saturation (1509-1529) is the cheapest plan the planner finds. These are upper bounds on
the true minima (greedy planner, restricted candidate sets).

External review (astra, `astra/rules-review/answer.md` in the lane directory, 02:47Z) of the rules
claims and of plan.py/simulate.py: splash exposure claim confirmed (with the precise wording "a copy
that reaches the base has received 10 x A"); the gun total-damage formula D x (span + n - 1) holds
only if the copies in range survive and the window ends before tick 250 (REFUTED as an identity;
kept as an upper bound with those hypotheses); subset-legality confirmed; plan_defense's zero-leak
acceptance confirmed sound for the listed compositions, no hidden information used; simulate_leak
matched the engine on 64 further random comparisons. Flagged limitation: threat_compositions samples
purchase bundles (now up to 9, including interleaved orders of the two most expensive affordable
tiers); it is not every affordable purchase order, so "zero leaks against everything affordable" is
a claim about the sampled set only. Order matters for guns (frontmost targeting), never for splash.

## 2026-10-31T02:56Z  Tournament t3 (frozen v3), planner fix, Q1 route record, templates for the lead

t3: `bot_research/runs/defense/t3_v3_vs_tuning` (frozen copy `bots/defense/frozen/v3`, specs
`bot_research.bots.defense.frozen.v3.fortress:@make` and `...:@make?attack_from=6&attack_share=0.5`,
opponents = the 26 specs in `bot_research/experiments/economy/opponents_tuning.txt` (lead baselines +
hrt-w3 tuning pool), both seats, 104 matches): 104-0-0, no rejected actions, no bot errors, mean HP
difference +942/+1085, most games end by round 7-11 through the opportunistic attack; the pool turtle
(`counters.pool:@turtle`) survives to round 50 and loses on HP (+76 / +286). Decision time at most 8.6 s
per match (max single call 1.7 s). Note: the harness printed two different version tags for the same
frozen spec ([v:1cc9490f] and [v:90eedf66]); the frozen files were not modified (SHA256SUMS in the frozen
directory), so the tag seems to depend on more than the entry module. For the lead to check.

Planner fix (v4, verified by `check_plan.py 120`: 120/120 sim matches, 15 zero-leak plans hold in the
engine): after switching the gun pass to score candidates on the worst composition only, a cheap splash
that cleared the worst composition (the tier1 screen) but not the tier3 was preferred over gun2, and
the round-1 zero-leak plan (20 walls + gun2 at (9,5), 100 gold) was no longer found. Now a candidate that
clears the worst composition is re-checked on all compositions and fully-clearing candidates rank first
(cheapest wins). The flaw affected v3 (t3) only through weaker speculative plans; t3 is kept as evidence.

Q1 (route length record): the combined-objective annealer (`layout_search.py --objective combo
--beta 1 --k 25`, budget 60, 4 seeds x 150000 iterations) found a 44-cell layout with route length 86
and top-25 adjacency 155 (`runs/defense/layout_search_combo.jsonl`, last line; rendered by
`q1_build_order.py`). This beats the serpentine (66 / 154 with 44 cells) on both counts. It is a
diagonal staircase maze, not a stage structure; its incremental income profile is poor (single cells
do not lengthen the route until a line closes). Conjecture: 86 is not the maximum; the annealer is a
heuristic with a fixed budget.

Lead cycle-2 request (a): greedy S(k) sequences (template evaluator `experiments/defense/template_eval.py`;
S(k) = per-copy splash damage after the k best greedy slot splashes with all walls built and the other
slots open):

| template | walls / slots | route walls-only / full | S(1..10) | S(25) |
| --- | --- | --- | --- | --- |
| lead best.py (rows 1,3 interior + 6 snake cells) | 33 / 26 | 46 / 78 | 60 120 170 220 290 370 440 480 530 570 (sum 3250) | 1540 |
| w1 master layout (reserved adjacency >= 5) | 29 / 30 | 40 / 78 | 70 140 190 240 270 310 360 400 430 460 (2870) | 1510 |
| wave bands (rows 0-2, 4-6 square waves) | 30 / 26 | 22 / 72 | 60 130 180 230 270 310 340 370 420 580 (2890) | 1530 |
| independent pillars: 4 serpentine pillars + 5 snake U-turn cells early, 7 bulk slots in each of rows 1 and 3, 4 snake extras (`template_pillars.py`) | 32 / 27 | 40 / 78 | 70 140 190 240 310 370 440 500 560 610 (3430) | 1500 at k=25 |

Principle (empirical, from these evaluations): a slot keeps its adjacency while other slots are open only
if opening it shortcuts just its own corner, i.e. it is the U-turn cell of an otherwise complete line;
slots in the middle of a line make the line porous and are worth 3-5 until the line is nearly full.
An annealing search over slot assignments (`template_search.py`) is running; results and the final
WALLS/SLOTS pair follow.

## 2026-10-31T02:58Z  Lead request (b): gun placements that keep the slots, and their value

Script `experiments/defense/gun_value.py`, output `runs/defense/gun_value.txt`. Method: on a template with
the first k greedy splashes placed (S = per-copy splash), rank open slots and free off-route cells by the
number of route cells within gun range, then simulate 1-3 copies of tier4/tier5 with the engine replica
for one gun2, one gun3 or two gun3 added. Results (lead template; the pillars template behaves alike):

| k (S) | free non-slot gun cells (gun3 coverage) | tier4 x1/x2/x3 | tier5 x1 | tier5 x2, x3 |
| --- | --- | --- | --- | --- |
| 4 (220) | (6,8) 16, (5,8) 15, (4,8) 13, (10,9) 12 | one gun3 at (6,8): 0/0/1 leaks | not stopped by one gun3 | not stopped |
| 8 (480) | (8,4) 13, (10,9) 12 | one gun2 at (8,4) or (10,9): all 0 leaks | two gun3 at (8,4),(10,9): 0 leaks; one gun3 leaks | two gun3: 1 of 2 and 2 of 3 leak |
| 12 (630) | (8,4) 13, (10,9) 12 | splash alone stops them | two gun3: 0 leaks | two gun3: 1 of 2, 2 of 3 leak |

So in the lead's template there are free cells beside the route (inside the bottom snake region, e.g.
(6,8), (5,8), (4,8), and (8,4), (10,9)) where a gun does not consume a slot; a gun3 there covers 12-16
route cells (660-880 damage to a lone copy). Rule of thumb from the simulations: with S >= ~220 one
gun3 handles up to two tier4; with S >= ~480 two gun3 (400 gold) handle one tier5; a second or third
tier5 in the same round needs either S >= ~1000 or more guns (each extra tier5 adds about 1500 - S HP
that the guns must remove while the copies are in range). Guns on slots are only worth it while
splash capacity stays sufficient; plan.py enforces reserved capacity >= 155 adjacency.

## 2026-10-31T02:59Z  Q1 answer: long routes with build orders

Script `experiments/defense/q1_build_order.py` (line-aware greedy order with a 2-step lookahead; every
prefix of a legal layout is legal), output `runs/defense/q1_build_order.txt`. "Route when it grows"
lists (cells built, route length) at each increase:

| layout | cells | final route | route growth along the build order |
| --- | ---: | ---: | --- |
| serpentine rows 1,3,5,7 (gaps 11,0,11,0) | 44 | 66 | 22 until 14 cells; 24..40 at cells 15-23 (+2 per cell as row 3 closes next to row 1); 44 at 24; 46..62 at 35-43; 66 at 44 |
| master layout (serpentine + bottom wave) | 59 | 78 | 24..44 at cells 18-27; 46..68 at 38-49; 72 at 51, 74 at 55, 78 at 56 |
| annealed, length objective, budget 45 | 43 | 82 | 22 until 21 cells; 30-36 at 36-39; 48 at 40, 70 at 41, 74 at 42, 82 at 43 |
| annealed, combined objective, budget 60 | 44 | 86 | 24 at 19 cells, 28-40 at 27-32, 48-66 at 33-41, 72, 74, 86 at 44 |

Reading: the serpentine pays from its 15th cell on (one complete row plus a growing second row gives +2
per cell), so a bot can start income from 24 walls (route 44) in rounds 1-2. The annealed mazes need
almost all cells before paying (diagonal staircases close late), so their extra 8-20 steps of final
route cost 20-40 rounds of lower income if built early; they are attractive only as a late add-on.
With turrets as blockers the same orders apply (any blocker counts), but turrets in the lines consume
the cells with 6-7 splash adjacency, so the plan.py layout reserves those for splashes.
Maximum route found: 86 (44 cells); the true maximum is not established (conjecture: below 100,
since 1-wide corridors need about one blocker per route cell and 142 cells are available).

## 2026-10-31T03:00Z  Lead request (a): drop-in WALLS/SLOTS pairs, and tournament t4

Module `bot_research/bots/defense/templates.py` exports two pairs (cells as (x, y) tuples):
- `PILLARS_7_7_4_WALLS / _SLOTS` (32 walls, 27 slots): S(1..10) = 70 140 190 240 310 370 440 500 560 610,
  S(25) = 1500, route 40 walls-only / 78 full.
- `ANNEALED_25_WALLS / _SLOTS` (34 walls, 25 slots): S(1..10) = 70 140 210 280 350 410 470 530 590 650,
  S(15) = 950, S(20) = 1240, S(25) = 1510, route 34 walls-only / 78 full. Found by
  `experiments/defense/template_search.py` (simulated annealing over which 25 of the 59 structure cells
  are slots; objective sum S(1..10) + 0.5 sum S(11..20) - penalty if S(25) < 1500 + 3 x walls-only route;
  2 seeds x 1500 iterations, both reached objective 8697; results in `runs/defense/template_search.jsonl`).
  Slot layout: row 1 x = 5..10, row 3 x = 1..3, row 5 x = 5..10, row 7 x = 1..3 and (7,7), snake cells
  (3,8), (1,9), (3,9), (5,9), (3,10), (7,10). The greedy fills each block from its inner end, so each
  splash extends the forced corridor and adds 60-70 (compare the lead template's 50-80 increments).
  Trade-off: walls-only route 34 instead of 46 (12 gold per round less path income until slots fill).
Reference evaluation of the lead's current template with the same tool: S(1..10) = 60 120 170 220 290
370 440 480 530 570, S(25) = 1540. Compatibility: both pairs use the lead's structure (rows 1,3,5,7 with
gaps 11,0,11,0 and the bottom snake), so best.py's WALLS/SLOTS can be replaced directly. The
evaluator's greedy (max S, tie: longer route) may differ from best.py's slot order; S(k) values assume
all walls are built before splashes are placed.

t4 (`runs/defense/t4_v4_vs_tuning`, frozen v4, 26 tuning opponents, both seats): default fortress
52-0-0 (max decision 1.3 s), attack_from=6 variant 52-0-0, pure turtle 0-36-16 (losses -24 to -52 to the
round-1 rushes and mixed5, -560 to eco_then_flood(8, tier5) and eco6_t5, -11 to random_legal seed 3;
max decision 11 s, 46 s per match against gun_turtle). No rejected actions, no bot errors.

## 2026-10-31T03:03Z  Self-play of fortress v4 and the first-poke problem

`runs/defense/x1_cross` (fortress v4 vs itself, both seats): draw 760-760 at round 50. Both sides built
20 walls + 4 factories in round 1, factories in round 2, and in round 3 (first round of the opportunistic
attack, opponent still without turrets) both bought 8 tier1 and took 8 hits (40 HP); from round 5 on both
had guns, no further hit landed, both saturated (27 splashes, 4 gun3, 5 gun2 each by round 50) and
accumulated 544049 gold with nothing to spend it on. The game is decided by HP traded before immunity,
and a cheap tier1 poke against a map without turrets is the efficient trade (0.33 damage per gold).
Defensive consequence: the speculative rule "zero leaks against everything the opponent can afford" is
all-or-nothing and buys nothing when the tier3/tier4 part is unaffordable, leaving the map open to the
cheap poke. Added to fortress: poke_insurance (fallback: zero leaks against the tier1/tier2 bundles
only; one splash at a pillar, 60 gold, suffices from round 2 on) and an optional blind round-1 turret.

## 2026-10-31T03:03Z  Round-1 insurance table (blind round)

Script `experiments/defense/round1_insurance.py`, output `runs/defense/round1_insurance.txt`. Exact
round-1 outcome (engine replica) of blind defence options against each 100-gold rush; cells are HP lost /
bounty gold handed to the attacker:

| option (cost) | tier1 x6 | tier2 x2 | tier3 | tier2 + tier1 x4 | tier1 x3 + tier2 | route |
| --- | --- | --- | --- | --- | --- | ---: |
| nothing | 30/30 | 24/10 | 26/5 | 32/25 | 27/20 | 22 |
| splash (10,1) (60) | 0/0 | 24/10 | 26/5 | 12/5 | 12/5 | 22 |
| gun2 (10,1) (80) | 0/0 | 0/0 | 26/5 | 0/0 | 0/0 | 22 |
| 20 walls + splash (10,1) (80) | 0/0 | 0/0 | 26/5 | 0/0 | 0/0 | 42 |
| 20 walls + gun2 (9,5) (100) | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 40 |

The exposure of a blind round 1 is at most 32 HP; full insurance costs the whole starting gold (five
factories = 75 income per round forgone in round 1, compounding). 20 walls + a gun2 at (9,5) is the only
option that also stops a tier3, and it pays 18 gold per round in route income from round 1 (route 40).
Which option is right depends on the opponent pool and on whether the HP can be won back later; this
lane only supplies the exact costs.

## 2026-10-31T03:07Z  t5 (layouts), cross-lane matches, and why fortress beat best.py

t5 (`runs/defense/t5_layouts_vs_tuning`, frozen v5, 26 tuning opponents, both seats): attacking fortress with
layout=annealed25 52-0-0; pure turtles: annealed25 0-28-24, lead_v3 0-30-22 (default layout in t4:
0-36-16). The turtle's losses are concentrated in rounds 3-6 against tier1 floods (eco3_t1 -95,
eco5_t1 -285) and tier3/tier5 timings, when the zero-leak plan against everything the opponent can afford
exceeds 0.6 x gold and the speculative rule buys nothing; the shorter early route of annealed25 (28 vs 40
after the first walls) also costs income. Fixed in v6 by poke insurance (t6 running).

x1 (`runs/defense/x1_cross`, fortress v4, both seats): vs itself draw 760-760 (see above); vs
`bot_research.bots.economy.frozen.v4.econ:@make` draw 800-800 (neither side ever leaked); vs
`bot_research.bots.best:@make` (lead planner v3 at 03:00Z) win +215 in both seats at round 50.
Match record (seat A): fortress poked 3 tier1 in round 3 (15 HP, best.py had no turret yet), one tier4 in
round 8 (60 HP, best.py had S = 220 and no gun), one tier5 in round 11 (140 HP, S around 630); each
purchase was made because exact simulation on best.py's current map showed it leaking. best.py's own
tier2 (r2), tier3 (r3), tier4 (r7-8) and tier5 (r11) never reached fortress's base: fortress had a gun2
from round 2, gun1s/gun3s from rounds 3-9 (guns are the cheap answer to one to three big copies, splashes
to swarms), i.e. the threat-based mixed plan kept zero leaks for about 900 gold by round 11. Evidence for
the lead: a splash-only slot defence lags single big copies by one round each time S < HP; one gun3 at a
free cell per tier step (see the gun table) closes that window.

## 2026-10-31T03:09Z  Timestamp correction

Three earlier headings in this file were stamped with estimated times ahead of the clock (02:35Z, 02:50Z,
02:57Z); they were corrected to the real recording times taken from the shell clock and file mtimes
(02:19Z, 02:48Z, 02:56Z). Entries from 02:58Z on are stamped with the shell clock at writing time. Thanks
to hrt-w3 for the catch (validation.md, line 157).

## 2026-10-31T03:09Z  Summary for the report (state at this time; superseded by later entries if any)

Deliverables (all under bot_research/, lane hrt-w1):
- `bots/defense/plan.py`: plan_defense(observation, budget, required_hp=None, threat_types=None, *, allow_guns,
  layout, partial) -> actions; threat_compositions, plan_walls, defense_cost, opponent_leak, splash_damage,
  MasterLayout (default / from_template), layout_by_name. `bots/defense/simulate.py`: simulate_leak (exact
  one-map replay with leaked-HP tally). `bots/defense/geometry.py`: routes, adjacency, serpentine helpers.
  `bots/defense/templates.py`: WALLS/SLOTS pairs ANNEALED_25, PILLARS_7_7_4, LEAD_V3.
  `bots/defense/fortress.py`: standalone bot, factory make(...), parameters in its docstring; frozen copies in
  `bots/defense/frozen/v3..v6` (SHA256SUMS inside) are what the tournaments ran.
- Experiments: `experiments/defense/*.py` (geometry, layout_search, template_eval/_search/_pillars/_waves,
  q1_build_order, q2_cheapest, gun_value, round1_insurance, check_plan, freeze.sh). Results: `runs/defense/`.

Proved (from the code, confirmed by the existing tests and an external review): per-copy splash exposure is
10 x adjacency and independent of the stream; adjacency >= 150 on the route is immunity against every type;
any subset of a legal layout is legal. Empirical (exact simulation, no randomness): the cost tables in the
Q2 entry; the greedy S(k) tables; the gun tables. Empirical (matches on the unchanged engine through the
lead's harness, fresh process per match, both seats, no seeds involved because the engine is deterministic
and the bots are deterministic; what varies is the opponent policy and the seat): fortress attacking
variants 52-0-0 against the 26 tuning opponents in t3, t4, t5; pure-turtle variants 0-36-16 (default layout)
and 0-28-24 (annealed25); cross-lane: +215/+230/+30/+551 against the lead's planner versions, draws against
econ. These pools are development pools; the held-out validation belongs to hrt-w3.

Decision rules of fortress (one call per round, observation only): see fortress.py docstring (mandatory
zero-leak plan against the visible roster -> speculative zero-leak plan against affordable bundles if
<= 0.6 x gold, else poke insurance -> layout walls -> opportunistic attack by exact simulation on the
opponent's current map -> factories, 40 per round at most).

Reproduction (from the project root, env PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp):
  .venv/bin/python -B -m bot_research.experiments.defense.check_plan 200
  .venv/bin/python -B -m bot_research.experiments.defense.q2_cheapest [default|annealed25]
  .venv/bin/python -B -m bot_research.experiments.defense.template_eval
  .venv/bin/python -B -m bot_research.harness.tournament --name t4_v4_vs_tuning --out-dir bot_research/runs/defense/t4_v4_vs_tuning --candidates bot_research.bots.defense.frozen.v4.fortress:@make --opponents $(cat bot_research/experiments/economy/opponents_tuning.txt) --jobs 3
  .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.defense.fortress:decide --bot-b td_bots.protocol:idle --output bot_research/runs/defense/<new name>.jsonl

Known failures and limits: (1) a pure defender cannot win and loses to any blind round-1 rush by 24-32 HP
and to a timed flood by one round of damage whenever the zero-leak plan exceeds its speculative budget;
(2) threat compositions are sampled (up to 9 bundles), so "zero leaks against everything affordable" holds
for the sampled set only (order matters for guns); (3) the planner is greedy with restricted candidates:
costs are upper bounds on the true minima; (4) the opportunistic attack assumes the opponent builds nothing
in the same round; against a reactive defender it only guarantees the current round; (5) decision time up
to about 1.3 s per call for attacking variants, 11 s for the turtle against very rich opponents.

## 2026-10-31T03:11Z  STRONG-pool cross-check (x2) and the 26-slot template

x2 (`runs/defense/x2_strong`, fortress frozen v6 default against the 12 non-defense specs of the lead's
STRONG pool, both seats, 24 matches): 20 wins, 4 draws, 0 losses, no rejected actions or bot errors.
Wins: lead frozen best_v1 +230, best_v1 kappa=8 +30, best_v2 +551 (all at round 50), economy.timing +133,
counters posterior_response +811 (round 11), switching +725 (r8), maze_pressure +1018 (r9), forecast_lock
+1049 (r14), poke_lock +1049 (r14), predicted_pressure +1410 (r13). Draws 800-800: economy.econ (live) and
economy frozen v2. The econ bots and fortress never leak against each other; the lead versions leak to
single big copies while their splash count is below the copy's HP, and the counters lose to the
opportunistic attack. Interpretation: within these pools, the threat-based mixed gun/splash defence plus
exact-simulation pokes is at least as strong as anything else present; this is a development pool, not
validation.

Template search with 26 slots (`template_search.py --slots 26`, 2 seeds): seed 0 found
S(1..10) = 70 140 210 280 350 420 490 550 610 670 (sum 3790), S(15) = 970, S(20) = 1270, S(25) = 1500,
S(26) = 1560, walls-only route 36; exported as templates.ANNEALED_26_WALLS/_SLOTS and selectable through
layout="annealed26". Slots: row 1 x = 4..10, row 3 x = 1, row 5 x = 3..10, row 7 x = 1 and 3 and 7, snake
(1,9), (1,10), (1,11)?, (3,10), (5,9), (7,10), (9,9) (exact list in templates.py).

## 2026-10-31T03:12Z  Q2 with layout annealed25, and the gun/slot capacity trade-off

`q2_cheapest.py annealed25` (output `runs/defense/q2_cheapest_annealed25.txt`): splash-only thresholds from the
empty map cost 60 (20 HP), 73 (70), 193 (180), 553 (560), 1534 (1500) versus 60, 80, 200, 804, 1529 with the
default layout: the annealed template reaches 560 for 553 instead of 804 (nine 6-7 cells instead of thirteen
3-5 cells). But its reserved capacity is only 151 adjacency (25 slots), below the planner's saturation guard
(155), so no gun may occupy a slot and the free off-route cells near the route cover too few cells: the
threat plans for 1-3 tier4/tier5 fall back to splash saturation (553 / 1534) instead of 220-420 of guns with
the default layout (which has 180 capacity, i.e. 25 to spare). Consequence for template design: the faster
the greedy S(k) curve, the fewer spare slots for guns; a template with 28-30 slots (default layout) buys
single big copies far cheaper with guns but reaches each splash threshold later. The fortress policy uses
partial="best" for the visible roster, so with annealed25 a visible lone tier5 is answered with the
strongest affordable splash/gun-on-free-cell plan rather than nothing. Conjecture: a template with 26
slots plus 2-3 designated gun cells of >= 15 coverage that are not slots would dominate both; not built.

## 2026-10-31T03:13Z  x3: fortress v6 (poke insurance) against v4 and the live best.py

`runs/defense/x3_versions` (both seats): v6 beats v4 +294 at round 50 in both seats; v6 beats the live
`bot_research.bots.best:@make` +215 in both seats (same margin as v4 did at 03:00Z, so the lead's bot did
not change in between or the change did not matter here). The annealed26 opponent spec failed with
KeyError because the frozen v6 copy predates that template (harness error rows, not bot errors).

## 2026-10-31T03:16Z  x4: annealed25 layout against the STRONG pool; route-weighted template search

x4 (`runs/defense/x4_strong_annealed`, fortress frozen v6 with layout="annealed25", 12 STRONG specs, both
seats): 24-0-0. Compared with the default layout (x2: 20-4-0): the two econ versions are now beaten +560
instead of drawn, best_v1 +194 (was +230), best_v1 kappa=8 +54 (was +30), best_v2 +13 (was +551),
timing +77 (was +133); the w3 counters lose by 810-1099. So the layout changes which opponents leak and by
how much; neither layout dominates on every pairing (complementary strengths within this pool).
Route-weighted template search (`template_search.py --slots 26 --route-weight 25`, 2 seeds): walls-only
route stays 36 and sum S(1..10) = 3760; on this 59-cell structure the early-S objective and the walls-only
route cannot both be pushed further by moving slots (both seeds agree).

## 2026-10-31T03:16Z  Observation for hrt-w2: econ's defence spending depends on the opponent's visible map

In x4 (`runs/defense/x4_strong_annealed/logs/20261031T031329-00007--make-layout=-annealed25-_fortress-vs--make_econ-std.jsonl`)
econ (live `bot_research.bots.economy.econ:@make`) bought 3 gun1 + 4 walls in round 2, 2 gun1 + 2 tier1 in round 3
and kept spending on turrets afterwards, reaching round 8 with 15 factories and 288 gold against fortress's
107 factories and 1665 gold; fortress's tier5 pokes (rounds 8-10) then leaked 560 HP. Against the default-layout
fortress (x2, same econ version) econ grew normally and the match was a 800-800 draw. The only difference
econ could observe is fortress's map and gold (13 walls, route 26, 93 gold after round 1 with annealed25;
20 walls, route 40, 100 gold with the default layout). Something in econ's threat or response model
over-reacts to that state; worth a look (w2's lane).

## 2026-10-31T03:19Z  Adversarial review by astra (answer in the lane directory, astra/fortress-review/answer.md), fixes, v8

Astra verified templates.py numerically (ANNEALED_25 and PILLARS_7_7_4: all cells legal, disjoint, routes
preserved, S(k) tables exact; PILLARS has 27 slots with S(27) = 1620) and found:
1. Exploit (reproduced by astra as a full match, 800-795 both seats): one tier1 + four factories in round 1
   lands 5 HP because fortress's speculative allowance (60) is below both the full plan (100) and the cheap
   plan (80); afterwards an opponent that evaluates fortress's deterministic policy on the public
   observation can defend against its predicted purchases and keep the lead. Same mechanism as the lead's
   poke_lock (-5 in the frontier round robin). Not fixed by a policy change here: round 1 is blind and the
   choice is the lead's (round1="gun2" or the lead's 89-gold certificate; see the round-1 table).
2. Sampling gap: with 400 gold each, the plan (20 walls + gun3 at (10,1)) stopped all sampled bundles but
   the order tier3, tier2, tier4 leaked the tier4 (frontmost-first targeting). Fixed: affordable_bundles now
   also emits every multiset in ascending-cost order (heavy last); max 12 bundles. After the fix the round-1
   plan with 400 gold is 20 walls + gun3 at (1,3) and all orders of {tier2, tier3, tier4} are stopped.
3. Sampling gap: padding the roster with cheap copies so that a heavy copy becomes entry 250 (spawn tick 0)
   defeats the arrival cutoff; sampled bundles spent more and missed it. Fixed: wrap_bundles() adds, for each
   heavy tier, the composition "pad with tier1 to entry 250*m - 1, then as many heavy copies as affordable".
4. Bug: fortress added stage-A walls after the defence plan without re-checking; in a reachable position the
   new route removed the only splash's exposure and a tier1 leaked. Fixed: walls are now planned first and
   every defence plan is computed on the resulting route.
5. Bug: poke insurance filtered whole compositions (visible roster + bundle) by HP <= 70, so any visible
   tier3+ disabled the fallback. Fixed: cheap bundles are generated separately and appended to the roster.
6. Qualifications accepted: partial plans minimise the surrogate 10 x base damage + leaked HP; splash
   exposure is order-independent for a complete traversal, leaked damage is not (arrival eligibility).
7. Mirror match is a proven draw (symmetric deterministic play).
No illegal action or hidden-information use was found. check_plan after the fixes: 120/120 simulation
matches, zero-leak plans hold in the engine (`runs/defense/check_plan_v8_120.txt`). Frozen as
`bots/defense/frozen/v8`. Recommended spec for the lead's integration:
`bot_research.bots.defense.frozen.v8.fortress:@make` (component: `bot_research.bots.defense.frozen.v8.plan`);
layout options "default" (spare slot capacity for guns) or "annealed25"/"annealed26" (faster S(k)).

## 2026-10-31T03:20Z  x5 (annealed26 vs STRONG), t7, and a planning-time bound

t7 (`runs/defense/t7_a26_vs_tuning`): fortress v7 layout="annealed26" 52-0-0 against the tuning pool.
x5 (`runs/defense/x5_strong_a26`, STRONG pool, both seats): 22-0-2; the two losses are -6 in both seats
against lead frozen best_v1 with kappa=8 (annealed25 had won that pairing +54, default +30). So each layout
loses or wins some pairings by a few HP: the early HP exchange is decided by a handful of hits, and the
template changes which of them land. No layout dominates; the lead should pick by its own pool.
Planning time: in t6 the pure turtle against the mirror/stacker counters spent minutes per decision because
the gun pass simulated every candidate against compositions of hundreds of copies that guns cannot stop.
Added to plan_defense: the gun pass is skipped when a composition exceeds 120 copies (splash plans still
run; they are exact and cheap) and stops after a 3 s time budget, keeping the best plan found so far.

## 2026-10-31T03:21Z  v9 (time-bounded planner), and the lead's round-1 certificate verified

Timing after the bound (position: round 9, opponent 10000 gold with 200 visible tier1, own 3000 gold and
stage-A walls): 13 compositions of 218-866 copies, plan_defense returns the 1509-gold saturation plan in
1.0 s (previously minutes against such opponents, see t6). check_plan 80: simulation equal to the engine,
zero-leak plans hold. Frozen as `bots/defense/frozen/v9` (spec `bot_research.bots.defense.frozen.v9.fortress:@make`).
Lead's round-1 certificate (NOTES_FOR_TEAM 03:10Z: gun2 at (3,2), walls (x,1) for x <= 4 and (6,y) for
y <= 3, 89 gold): checked with simulate_leak against every ordered roster of tier1/tier2/tier3 costing at
most 100 gold (26 rosters, lengths 1-6): zero leaked damage, route 22. It is 11 gold cheaper than the
planner's 100-gold plan (20 walls + gun2 at (9,5)), which however lengthens the route to 40 (+18 gold per
round). Both are exact zero-leak round-1 insurances against everything 100 gold buys.

## 2026-10-31T03:22Z  t6 (stopped at 101 of 208 matches)

`runs/defense/t6_poke_vs_tuning` (frozen v6, tuning pool, both seats): default fortress 52-0-0; pure turtle
with poke insurance 0-33-16 over 49 matches (v4 without insurance: 0-36-16 in t4; the insurance did not
change the loss count against this pool because the losses come from round-1 rushes and from floods that
exceed the speculative budget, not from cheap pokes). The run was stopped because the v6 planner spent
minutes per decision for the pure turtle against the mirror and stacker counters (fixed in v9, see above);
the remaining variants (round1="gun2") are re-run as t9 with v9.

## 2026-10-31T03:24Z  hrt-w3 confirmation of the round-1 exposure; exhaustive compositions for small gold

hrt-w3 (validation.md 03:18Z) reports that fortress v4 and v6 lose 800:788 to a forecast-defended round-1
tier2 purchase (their known_policy counters predict the deterministic fortress and defend against it): the
same blind-round exposure astra reproduced (800:795 with a tier1). Options are tabulated in the round-1
entry above; t9 measures the turtle with round1="gun2".
Planner: threat_compositions now enumerates every ordered purchase list when the opponent's gold allows at
most 400 of them (exact threat set for small gold, where purchase order matters for guns), and falls back
to the sampled bundles above that. Counts (measured): 100 gold -> 26 lists, 130 -> 63, 160 -> 150, 175 -> 232,
200 -> 506 and 300 -> 9611 (sampled above 400). Zero-leak plans: 100 gold -> 20 walls + gun2 (100 gold, 0.4 s); 175 gold (232 lists) -> 160 gold in 2.0 s.

## 2026-10-31T03:27Z  x6: v8 against the STRONG pool (default and annealed25 layouts)

`runs/defense/x6_strong_v8` (frozen v8, 12 STRONG specs, both seats): default layout 20-4-0 (the four draws
are 800-800 against economy.econ live and frozen v2, as with v6), layout="annealed25" 24-0-0. The v8 fixes
(walls first, poke-insurance filter, heavy-last and wrap compositions) changed no outcome in this pool.
Across x2, x4, x5, x6: annealed25 is the only layout with no loss or draw against the STRONG pool (48-0-0 over
two versions); default draws econ; annealed26 lost one pairing by 6 HP. Against the tuning pool all three are
52-0-0. The lead should treat these as development-pool evidence only.

## 2026-10-31T03:31Z  x7: blind round-1 insurance costs more than it protects (STRONG pool)

`runs/defense/x7_strong_v10` (frozen v10, STRONG pool, both seats): default 20-4-0 (draws = econ, as before);
round1="gun2" (gun2 at (10,1) in round 1, 80 of the 100 starting gold) 16-4-4: it loses -895 at round 9 to
counters.switching and -68 at round 50 to economy.timing, and its winning margins shrink (best_v1 +382 vs +230,
kappa=8 +62 vs +30, best_v2 +70 vs +551, predicted_pressure +488 vs +1410). Reading: the round-1 turret buys
at most 5-32 HP of protection (round-1 table) but costs four factories of compounding; against a flood timed
for round 8-9 the slower economy cannot afford the zero-leak plan and the match is lost outright. Empirical,
this pool only. Combined with the forecast counters (hrt-w3, astra): a deterministic bot either accepts a
blind 5-12 HP round-1 loss against opponents that poke and forecast, or pays the economy; the better
answer is to win the HP back later, which the opportunistic attack does against every pool member except
the econ bots (draws) and perfect forecasters of its own policy.

## 2026-10-31T03:37Z  t8: v8 against the tuning pool; the turtle's remaining losses

`runs/defense/t8_v8_vs_tuning` (frozen v8, 26 tuning opponents, both seats): default 52-0-0; pure turtle
(attack="none") 0-38-14. Compared with v4/v6 (0-36-16 / 0-33-16 of 49), the v8 fixes removed the losses to
eco3_t1 (-95), eco5_t1 (-285) and mixed5 (-174): the corrected poke insurance now stops the tier1 floods of
rounds 3-5. The remaining 14 losses are the blind round-1 rushes (tier1 -30, tier2 -24, tier3 -26, tier3 with
eco 0.5 -52), the round-8 tier5 floods (eco_then_flood and eco6_t5, -560: four tier5 at once while the
zero-leak plan exceeds 0.6 x gold) and random_legal seed 3 (-11, a round-1 poke). Decision time: at most 3.6 s
per call (12.6 s per match) for the turtle, 0.8 s per call for the attacker.

## 2026-10-31T03:41Z  t10 (annealed25 under v10) and a negative result on gun cells

`runs/defense/t10_v10_a25_vs_tuning` (frozen v10, layout annealed25, tuning pool, both seats): attacking 50-2-0,
pure turtle 0-32-20 (default layout turtle in t8: 0-38-14; the annealed turtle loses six more pairings,
-120 to -280, to the round-5/6 tier3/tier5 timings: its early route is shorter and the stage-B structure
needs more splashes before guns on free cells are useful).
Template search with a gun-cell term (`template_search.py --slots 26 --gun-weight 20`, two seeds): the best
templates keep S(1..10) summing to 3790 but the two best free (non-slot, non-wall, off-route) cells still
cover only 11 route cells each (sum 22, the same (10,9)/(10,10) cells as before). On this 59-cell structure
the conjecture of 03:17Z (26 slots plus designated gun cells with >= 15 coverage) is refuted: good gun cells
are the slots themselves. A gun-friendly layout needs spare slot capacity (the default layout's 30 reserved
cells) or a different structure.

## 2026-10-31T03:43Z  Sampling gap measured, x8, and the simultaneous-destruction draws

Sampling gap (`experiments/defense/sampling_gap.py`, output `runs/defense/sampling_gap.txt`): from the empty map
(own gold 400) and from stage A (own gold 600), the planner's zero-leak plan against the SAMPLED compositions
for opponent gold 200 / 250 / 300 was checked by exact simulation against every ordered purchase list of
that budget (506 / 2165 / 9611 lists): zero leaks in all six cases (plan costs 180-220 gold). So in these
positions the sampled set was sufficient; astra's 400-gold counterexample (fixed by the heavy-last orders)
shows it is not sufficient in general. Exhaustive enumeration is used automatically up to 400 lists.
x8 (`runs/defense/x8_vs_live_best`): fortress v10 default beats the live `bots.best:@make` +215 in both
seats (unchanged since 03:00Z); annealed25 +42.
The two t10 draws against eco6_t5 are simultaneous destruction at round 8 (`result both_bases_destroyed`):
eco6_t5 grew for six rounds and bought two tier5 in rounds 7 and 8; fortress (annealed25) had poked it down
to 10 HP with tier1 swarms but held only one splash, took 280 in round 7 and, after spending 878 gold on
14 splashes in round 8, still 560 (four tier5): -40 against -345. Cause: in round 7 the speculative plan
against two affordable tier5 exceeded 0.6 x gold (annealed25 has no gun slots) and was skipped while 70% of
the gold went into tier1 attackers. Added to fortress: lethal_share (default 0.6): when the worst affordable
threat could deal >= 60% of my HP on my current map (exact simulation), the speculative step may spend all
remaining gold and accepts the strongest partial plan. Test running (x9: both layouts vs eco6_t5,
eco_then_flood, switching, both seats).

## 2026-10-31T03:44Z  For the lead (cycle 4): use frozen v10 (or later), not v7; finish rule

The lead's v4 development bot imports `bots/defense/frozen/v7/plan.py`. v7 predates the fixes from the astra
review: heavy-last purchase orders and roster-wrap compositions (v8), the 3 s time budget and swarm skip (v9),
and exhaustive enumeration of all ordered purchase lists when the opponent's gold allows at most 400 (v10).
The API is unchanged; `bot_research.bots.defense.frozen.v10.plan` is a drop-in replacement. (fortress-side fixes,
walls first and the poke-insurance filter, are in frozen v8+ fortress.py; the lead's own policy layer already
builds walls first.)
Fortress live version: added a finish rule to the attack step (if all remaining gold on one tier would leak
>= the opponent's HP this round on its current map, buy it regardless of attack_share). Motivation: the
t10/x9 draws against eco6_t5, where fortress left the opponent at 10 HP in round 7 and both bases fell in
round 8. The lethal_share defence rule alone did not change that outcome (x9: still a both-destroyed draw at
round 8 with annealed25; default layout wins +560 at round 7). Test running (x10).

## 2026-10-31T03:46Z  x10: finish rule removes the simultaneous-destruction draws; v11 frozen

`runs/defense/x10_finish` (live fortress with lethal_share 0.6 and the finish rule, both layouts, vs eco6_t5,
eco_then_flood(8, tier5), eco5_t3, both seats): 12-0-0, every match won in round 7 (annealed25 vs eco6_t5 +543
instead of the both-destroyed draw; default +555). The finish rule spends all remaining gold on the tier that
kills the opponent this round when exact simulation on its current map says so; it ends games one round
earlier and before the opponent's tier5 wave lands. Frozen as `bots/defense/frozen/v11` after check_plan 60
(simulation equal to the engine; zero-leak plans hold). Tournaments t11 (tuning pool) and x11 (STRONG pool)
running for both layouts.

## 2026-10-31T03:51Z  t9 (v9 turtle variants) and t11 (v11 both layouts) against the tuning pool

t9 (`runs/defense/t9_v9_vs_tuning`, frozen v9, both seats): default 52-0-0; pure turtle 0-38-14 (same 14 pairings as
v8: blind round-1 rushes, round-8 tier5 floods, random_legal); pure turtle with round1="gun2" 0-40-12: the
round-1 gun2 removes the round-1 rush losses (tier1/tier2/tier3 rushes now draw) but the 80 gold of lost
compounding turns the flood losses from -560 into -1400/-1426 (eco6_t5, eco_then_flood) and adds mixed5 (-300),
rush_t3 with eco 0.5 (-338) and eco5_t3/eco_then_flood(6, tier3) (-156). Mean HP difference -145 against -49
without the guard. For a pure defender the blind round-1 turret is a bad trade on this pool; the losses it
prevents are 24-30 HP, the ones it causes are hundreds.
t11 (`runs/defense/t11_v11_vs_tuning`, frozen v11 with lethal_share and finish rules): default 52-0-0 and
annealed25 52-0-0 (t10's two both-destroyed draws of annealed25 are now wins), max decision 0.9 s.

## 2026-10-31T03:52Z  x11 (v11 vs STRONG) and x12 (v11 vs the lead's v4 development bot)

x11 (`runs/defense/x11_strong_v11`, both seats): default 20-4-0 (draws = econ live and frozen v2, as always),
annealed25 24-0-0; the finish/lethal rules changed no STRONG-pool outcome.
x12 (`runs/defense/x12_vs_lead_v4`): fortress v11 default loses -10 in both seats to the lead's development bot
`bot_research.experiments.lead.v4:@make` (which imports my frozen v7 planner and pokes 2 tier1 blind in
round 1); annealed25 loses -96 to it (seat A). Against the live best.py v11 still wins +215. The -10 is exactly
the blind round-1 poke that neither side can answer afterwards because both run the same defence component
(mutual immunity): the first-poke problem in its purest form. Test running (x13): fortress with
round1_poke=2, round1_poke=4 and round1="splash" (60-gold anti-tier1 insurance) against lead v4, best.py and
frozen v11.

## 2026-10-31T03:58Z  t13: scripted-opening scenarios expose two weaknesses; finish-first fix

`runs/defense/t13_v11_scenarios` (frozen v11 default vs 6 opponents under the harness scenarios eco:2,
mirror:1:2, asym:3:2, both seats, 36 matches): 24 wins, 10 draws, 1 loss, 1 win in the econ asym pair.
Draws by simultaneous destruction at round 9 (mirror:1:2 vs eco_then_flood -90, vs eco6_t5 -318; asym:3:2
vs eco6_t5 -5) and the loss -185 to econ frozen v4 under asym:3:2 (seat B; seat A won +242).
Cause 1 (the draws): in round 8 the opponent (eco6_t5) stood at 325 HP with no turret and fortress had 596
gold: 39 tier1 plus the 46 copies already on the roster would have leaked 425 >= 325, but the mandatory
defence against the visible tier5 ran first, spent the whole 596 on 2 gun3 + 3 splashes, still leaked 420,
and the finish never happened; both bases fell in round 9. Fix (live fortress, not yet frozen): the finish
check now runs before any defence, provided the worst affordable threat cannot kill me this round on my
current map (exact simulation); in that position fortress would have ended round 8 at 235 HP with the
opponent dead. Test running (x14).
Cause 2 (the loss): the asym opening left fortress with 32 random walls; the template planner's candidate
cells (reserved slots, free cells next to the route not on the template's final route) fit that map badly,
so econ's single tier4/tier5 pokes leaked in rounds 9-11 (60, 140, 280, 560) while fortress's own pokes
leaked less. Limitation to report: plan_defense is tuned for maps that follow its master layout; on foreign
maps it still returns exact, legal, zero-leak plans when it finds them, but at a higher cost. A layout-free
fallback (greedy over all legal cells by exact adjacency/simulation) would be the fix; not implemented.

## 2026-10-31T04:01Z  x13 (round-1 options against the lead's v4) and x14 (finish-first under scenarios); v12

x13 (`runs/defense/x13_round1_vs_lead`, live fortress v11+round1 options, both seats): against the lead's v4
(2 blind tier1 in round 1): round1_poke=2 draws 800-800... (0 HP difference: both pokes land, then mutual
immunity), round1_poke=4 loses -170 (the extra 30 gold of tier1 cost more compounding than the 10 HP they
score, and v4's defence stops them), round1="splash" (60 gold) loses -120. Against the live best.py: +262
(poke 2), +206 (poke 4), -880 at round 9 (splash: the economy lag lets best.py's flood through). Against frozen
v11: +10 (poke 2), +20 (poke 4), 0 (splash). So a 2-tier1 blind poke is the only round-1 deviation that does
not cost anything on this set and wins the symmetric first-poke exchange against a non-poking twin; it is
now an option (round1_poke, default 0) and the lead's policy layer already does it.
x14 (`runs/defense/x14_finish_first`, live fortress with the finish check moved before the defence, vs eco6_t5,
eco_then_flood(8, tier5) and econ frozen v4 under scenarios none / mirror:1:2 / asym:3:2, both seats):
eco6_t5 and eco_then_flood: 12 wins (the t13 draws at round 9 became wins at round 7-8, +270 to +835);
econ: draw 800-800 (none), win +980 at round 11 (mirror:1:2), asym:3:2 unchanged (seat A draw +242 both
destroyed, seat B loss -255: the foreign-map weakness above). Frozen as v12 (fortress only; plan.py is the
v10/v11 planner). Tournaments t14 (tuning) and x15 (STRONG + lead v4) running for default and round1_poke=2.

## 2026-10-31T04:03Z  Summary for the report, updated (state at v12; supersedes the 03:05Z summary)

Deliverables (bot_research/, lane hrt-w1). Component: `bots/defense/plan.py` (plan_defense, threat_compositions
with exhaustive enumeration up to 400 ordered purchase lists and sampled heavy-first/heavy-last/screen/
interleaved/roster-wrap bundles beyond, plan_walls, defense_cost, opponent_leak, threat_damage, MasterLayout,
layout_by_name), `simulate.py` (exact replica with leaked-HP tally), `geometry.py`, `templates.py`
(ANNEALED_25/26, PILLARS_7_7_4, LEAD_V3 WALLS/SLOTS pairs). Bot: `bots/defense/fortress.py` (make(): walls
first; finish-first; mandatory zero-leak vs the visible roster; speculative zero-leak vs affordable
compositions if <= 0.6 x gold, poke insurance fallback, lethal_share override; opportunistic attack by exact
simulation; factories capped at 40 per round; options layout, round1, round1_poke). Frozen copies v3..v12 under
`bots/defense/frozen/` with SHA256SUMS; recommended: `bot_research.bots.defense.frozen.v12.fortress:@make`
(planner = v10/v11 plan.py). Experiments and results: `experiments/defense/`, `runs/defense/` (t1-t14, x1-x15,
check_plan_*.txt, q1/q2 tables, template evaluations, gun_value, round1_insurance, sampling_gap).

Proved (code + tests + external review): full-route splash exposure 10 x adjacency, stream-independent;
adjacency >= 150 is immunity against all types; subsets of legal layouts are legal; identical deterministic
policies draw. Empirical, exact (no randomness): cost tables per HP threshold and per threat size (Q2);
S(k) template curves; gun-value table; round-1 table; sampling-gap check (0 leaks over 506/2165/9611 orders).
Empirical, matches on the unchanged engine (lead harness, fresh process per match, both seats, scripted
openings where stated): attacking fortress 52-0-0 against the 26-opponent tuning pool for every frozen
version v3-v12 and both layouts; STRONG pool (12 lead/economy/counter bots): default 20-4-0 (draws = econ),
annealed25 24-0-0 (v6-v11); beats the lead's best.py v3 +215 both seats; loses -10 to the lead's v4
development bot (its blind 2-tier1 poke) unless it pokes too (then 0); pure turtles 0-38-14 (default) and
0-32-20 (annealed25) against the tuning pool. Counter-evidence: round-1 blind pokes/forecasters win by 5-12 HP
(astra, hrt-w3, lead v4); scripted asymmetric openings with many foreign walls degrade the template planner
(one -255 loss to econ in t13/x14). Runtime: at most about 1 s per decision for attacking variants (3 s
planner budget), 3.6 s for pure turtles against very rich opponents.

## 2026-10-31T04:07Z  t14: v12 against the tuning pool

`runs/defense/t14_v12_vs_tuning` (frozen v12, both seats): default 52-0-0 and round1_poke=2 52-0-0. x15 (STRONG +
lead v4) in progress: default again -10 to lead v4 in both seats. t15 (v12 default vs the 26 tuning opponents
under scenarios eco:2, mirror:1:2, asym:3:2; 156 matches) launched to quantify scripted-opening robustness.

## 2026-10-31T04:07Z  Q3 metric: what the pure turtle spends on defence (t8, frozen v8, tuning pool)

Aggregated from `runs/defense/t8_v8_vs_tuning/results.jsonl` (pure turtle attack="none", both seats, 50 rounds
each; defence gold = walls + turrets over the match; HP lost = 800 - final HP; the rest of the gold went to
factories, about 36000 per match at the 40-per-round cap):

| opponent | matches | defence gold (mean) | HP lost (mean) | turrets / walls at end |
| --- | ---: | ---: | ---: | --- |
| @eco_then_flood | 2 | 1729 | 560 | 26 / 29 |
| @archetype?name="eco6_t5" | 2 | 3049 | 560 | 27 / 29 |
| @rush?tier="tier3"&eco=0.5 | 2 | 2759 | 52 | 34 / 29 |
| @rush?tier="tier1" | 2 | 80 | 30 | 1 / 20 |
| @archetype?name="rush_t3" | 2 | 250 | 26 | 5 / 20 |
| @rush?tier="tier2" | 2 | 440 | 24 | 4 / 20 |
| @random_legal?seed=3 | 2 | 2499 | 11 | 32 / 29 |
| @archetype?name="eco3_t1" | 2 | 280 | 0 | 2 / 20 |
| @archetype?name="heavy_t4" | 2 | 390 | 0 | 4 / 20 |
| @archetype?name="splash_t2" | 2 | 420 | 0 | 6 / 20 |
| @threat_defender | 2 | 464 | 0 | 11 / 24 |
| @eco_then_flood?switch=6&tier="tier3" | 2 | 620 | 0 | 5 / 20 |
| @archetype?name="eco5_t3" | 2 | 680 | 0 | 4 / 20 |
| @rush_t5 | 2 | 700 | 0 | 7 / 20 |
| @archetype?name="gun_t3" | 2 | 710 | 0 | 6 / 20 |
| @archetype?name="mixed5" | 2 | 740 | 0 | 5 / 20 |
| @archetype?name="eco5_t1" | 2 | 960 | 0 | 6 / 20 |
| @archetype?name="splash3_t4" | 2 | 1464 | 0 | 22 / 24 |
| @greedy_eco | 2 | 1729 | 0 | 26 / 29 |
| @eco_then_flood?switch=11&tier="tier5" | 2 | 1729 | 0 | 26 / 29 |
| @maze_eco | 2 | 1729 | 0 | 26 / 29 |
| @stacker | 2 | 1964 | 0 | 27 / 24 |
| @gun_turtle | 2 | 2739 | 0 | 36 / 29 |
| @mirror | 2 | 2779 | 0 | 35 / 29 |
| @turtle | 2 | 2959 | 0 | 36 / 29 |
| @splash_turtle | 2 | 3129 | 0 | 36 / 29 |

Reading: against passive or cheap opponents the turtle keeps zero leaks for 80-700 gold over the whole game
(e.g. 80 against the tier1 rush: 20 walls + one splash); against rich opponents it saturates (1700-3100 gold,
i.e. the 1500-adjacency immunity plus guns bought earlier against single big copies). HP is lost only where
the blind round 1 or a flood above the speculative budget hits (see t8 entry). This is the measured answer to
"zero leaks against the strongest affordable threat while spending as little as possible": the spending is
driven by the opponent's visible gold, not by a fixed schedule.

## 2026-10-31T04:11Z  x15: the 2-tier1 round-1 poke is now the fortress default (v13)

`runs/defense/x15_strong_v12` (frozen v12, 12 STRONG specs + the lead's v4 development bot, both seats):
default 20-4-2 (losses -10 to lead v4, draws 800-800 with both econ versions); round1_poke=2 24-2-0 (draws
0-0 with lead v4, wins +10 against both econ versions, which never defend round 1, and all other margins kept).
With t14 (52-0-0 either way on the tuning pool) and x13, the blind 2-tier1 poke is weakly dominant on
everything tested here, so it is the default from v13 on (round1_poke=0 restores the old behaviour).
Frozen as `bots/defense/frozen/v13`; recommended spec `bot_research.bots.defense.frozen.v13.fortress:@make`
(fortress change only; planner unchanged since v10).
Caveat (stated, not measured): a round-1 poke is itself exploitable by an opponent that insures round 1 (the
89-100 gold certificates), who then leads the economy by 30 gold of our tier1 against 89-100 of its defence;
on this pool nobody does that.

## 2026-10-31T04:13Z  t15: v12 under scripted openings against the whole tuning pool

`runs/defense/t15_v12_scenarios_tuning` (frozen v12 default, 26 tuning opponents, scenarios eco:2, mirror:1:2
and asym:3:2, both seats, 156 matches): 156-0-0, no rejected actions, no bot errors. The finish-first rule
removed the simultaneous-destruction draws seen in t13; the tuning pool contains no opponent that exploits
the foreign-map weakness (the only remaining scenario loss is the econ asym:3:2 seat in x14). t16 (frozen v13
default and annealed25 vs tuning) and x16 (v13 vs STRONG + lead v4) running.

## 2026-10-31T04:18Z  t16: v13 (round-1 poke default) against the tuning pool; finish rule refined

`runs/defense/t16_v13_vs_tuning` (frozen v13, both seats): default 52-0-0; annealed25 50-2-0, the two draws
being simultaneous destruction against eco6_t5 at round 8 (+175 HP but both bases down). In that position the
finish-first check declined because the worst affordable threat (two more tier5) could kill fortress that
round, so it bought a partial defence that did not save it either. Refinement (live fortress): when the
worst threat is lethal, the bot now also asks whether the best affordable defence would prevent the lethal
damage; if not, it buys the kill anyway (a draw at worst instead of a loss, and a win whenever the opponent
actually buys less than the worst case). Test running (x17: both layouts vs eco6_t5 and eco_then_flood,
plain and mirror:1:2 openings).

## 2026-10-31T04:21Z  t12 (v11 pure turtles), x16 (v13 vs STRONG + lead v4), x17 (finish refinement); v14

t12 (`runs/defense/t12_v11_turtles`, frozen v11, tuning pool, both seats): pure turtle default layout 0-40-12
(mean HP difference -16; the lethal_share rule turned the -560 flood losses into -280 against eco6_t5 and
removed the eco_then_flood(8) loss; the rest are the blind round-1 rushes -24..-52 and random_legal -11);
pure turtle annealed25 0-34-18 (mean -39; additional losses to eco5_t3/eco_then_flood(6, tier3) -208 and
mixed5 -120: the gun-less layout cannot stop the round-5/6 tier3 timings cheaply).
x16 (`runs/defense/x16_strong_v13`, frozen v13, STRONG + lead v4, both seats): default 24-2-0 (draws 0-0 with
lead v4, wins +10 against both econ versions, everything else as before); annealed25 24-0-2 (loses -164 to
lead v4).
x17 (`runs/defense/x17_finish2`, live fortress with the refined finish rule): default wins all 8 (eco6_t5 and
eco_then_flood, plain and mirror:1:2); annealed25 wins 6 and still draws by simultaneous destruction
against eco6_t5 without opening (+290 at round 8): in that round neither the kill nor a saving defence is
affordable for the gun-less layout, so the outcome is structural for annealed25 against two tier5 at rounds
7-8 after its own swarm has brought the opponent low. Recommendation: default layout (spare slot capacity
for guns) as the fortress default; annealed25 remains an option for opponents that never field tier5 early.
Frozen v14 = v13 + refined finish rule (fortress only). Measurements t17 (tuning) and x18 (STRONG + lead v4)
running; recommended spec after they finish: `bot_research.bots.defense.frozen.v14.fortress:@make`.

## 2026-10-31T04:24Z  t17 (v14 vs tuning), x19 (foreign-map fallback), v15

t17 (`runs/defense/t17_v14_vs_tuning`, frozen v14 default, both seats): W 52 D 0 L 0 of 52.
Foreign-map fallback (plan.py, live and frozen v15): when the own map holds more than 8 buildings outside the
master layout (scripted openings), the candidate sets for splashes and guns include every legal cell next to
the route and the layout's final-route / wall-order exclusions and the slot-capacity guard are dropped.
check_plan 40: exact and zero-leak plans hold. x19 (`runs/defense/x19_foreign`, live fortress, asym:3:2 /
asym:5:2 / asym:7:3 openings, both seats, vs econ frozen v4, eco6_t5, threat_defender): 17-1-0; the econ
asym:3:2 pairing that was lost -255 in t13/x14 is now won +1014 / +805; the one draw is simultaneous
destruction against eco6_t5 under asym:5:2 (seat B, -410 HP: the random opening left fortress with a weak
position and the lethal round could neither be survived nor avoided). Frozen as v15 (planner + fortress);
t18 (tuning pool, plain and asym:3:2) and x20 (STRONG + lead v4) running.

## 2026-10-31T04:26Z  x18: v14 against the STRONG pool and the lead's v4

`runs/defense/x18_strong_v14` (frozen v14 default, 12 STRONG specs + lead v4, both seats): 24-2-0; the two draws are
the 0-0 games against lead v4 (both bots poke 2 tier1 in round 1, then mutual immunity), every other pairing
won including both econ versions (+10). t19 (frozen v15 pure turtle, round1_poke=0, vs tuning) launched for
the final Q3 turtle metric.

## 2026-10-31T04:30Z  t18: v15 against the tuning pool, plain and asym:3:2 openings

`runs/defense/t18_v15_vs_tuning` (frozen v15 default, 26 opponents x {none, asym:3:2} x both seats = 104):
103-1-0, mean HP difference +805. The draw is simultaneous destruction at round 9 against eco_then_flood(8,
tier5) under asym:3:2 (seat A): in round 8 the opponent held 1621 gold and no roster; fortress (486 gold,
790 HP) found the zero-leak plan unaffordable at 0.6 x gold, the worst affordable threat (two tier5 + tier4,
about 400) was below the lethal trigger (0.6 x 790 = 474), so it bought 22 tier1 and factories, took 340, and
in round 9 (450 HP, five visible big copies, 851 gold) neither a defence that would survive the worst case
nor a cheaper outcome than the kill existed; it bought the kill (2 tier4) and both bases fell (-222 / -190).
Possible tuning: a lower lethal_share (0.4) would have spent round 8 on guns; whether that costs more
elsewhere is untested (queued). This is 1 of 104 matches; the other asym:3:2 pairings were all won.

## 2026-10-31T04:35Z  v15 measured: x20 (STRONG + lead v4) and t20 (mirror:1:2, eco:2 openings)

x20 (`runs/defense/x20_strong_v15`, frozen v15 default, both seats): 24-2-0; the two draws are the 0-0 games
against the lead's v4 (mutual round-1 poke, then immunity); both econ versions beaten +10, every other STRONG
member beaten by 30 to 1410 HP.
t20 (`runs/defense/t20_v15_scen2`, frozen v15 default, 26 tuning opponents under mirror:1:2 and eco:2, both
seats): 104-0-0. Together with t18 (plain and asym:3:2: 103-1-0), v15 has 207 wins, 1 both-destroyed draw and
0 losses over the tuning pool under four opening conditions, and 24-2-0 on the STRONG pool.
Recommended spec: `bot_research.bots.defense.frozen.v15.fortress:@make` (fortress v15 = v14 behaviour; plan.py v15
adds the foreign-map fallback). t21/x21 test lethal_share=0.4 on both pools.

## 2026-10-31T04:42Z  t21: lethal_share 0.4 on the tuning pool

`runs/defense/t21_lethal04_tuning` (frozen v15 with lethal_share=0.4, 26 opponents x {none, asym:3:2} x both
seats): 104-0-0; the single both-destroyed draw of t18 (eco_then_flood under asym:3:2) is gone, and no other
pairing changed. x21 (same variant vs STRONG + lead v4) finishing; if it matches v15's 24-2-0 the lower
threshold becomes the default (v16). x22 (v15 self-play: default vs default, vs lethal 0.4, vs annealed25)
running for the record.

## 2026-10-31T04:43Z  t19 (v15 pure turtle), x21 (lethal 0.4 on STRONG), v16 default

t19 (`runs/defense/t19_v15_turtle`, frozen v15 with attack="none" and round1_poke=0, tuning pool, both seats):
0-40-12 of 52. Losing pairings (HP difference):
    counters.pool:@archetype?name="eco6_t5"  | W 0  D 0  L 2  | hp  -280.0 
    counters.pool:@archetype?name="rush_t3"  | W 0  D 0  L 2  | hp  -26.0 
    ss.baselines:@random_legal?seed=3  | W 0  D 0  L 2  | hp  -11.0 
    ss.baselines:@rush?tier="tier1"  | W 0  D 0  L 2  | hp  -30.0 
    ss.baselines:@rush?tier="tier2"  | W 0  D 0  L 2  | hp  -24.0 
    ss.baselines:@rush?tier="tier3"&eco=0.5  | W 0  D 0  L 2  | hp  -52.0 
     | W 40  D 12  L 0.385  | hp 
     | W 40  D 12  L 0.385  | hp  -16.3 
These are the blind round-1 rushes, the round-5/6 timings and the round-8 tier5 floods, as in t12 (0-40-12);
the foreign-map fallback does not apply on the turtle's own layout. The pure defender's ceiling on this pool
is a draw; its value is the component, not the policy.
x21 (`runs/defense/x21_lethal04_strong`, frozen v15 with lethal_share=0.4, STRONG + lead v4, both seats): 24-2-0,
identical to the 0.6 default. With t21 (104-0-0, one draw fewer than 0.6), lethal_share 0.4 is now the
fortress default. Correction: the first attempt to change the default (frozen v16) did not apply (the edit
pattern did not match; v16/NOTE.txt records this; v16 is behaviourally v15). The default is changed in v17
(verified by inspecting make()'s signature: 0.4). Smoke of the live bot: beats eco_then_flood(8, tier5)
(log `runs/defense/smoke_v16.jsonl`). Recommended spec: `bot_research.bots.defense.frozen.v17.fortress:@make`
(planner = plan.py of v15; behaviour measured as frozen v15 with lethal_share=0.4 in t21 and x21).

## 2026-10-31T04:45Z  x22: v15 self-play; v17 confirmation runs

`runs/defense/x22_selfplay_v15` (both seats): default vs default 800-800 draw at round 50 (both poke 2 tier1 in
round 1 and both stop them: the symmetric deterministic draw, as proved); default vs lethal_share=0.4 also 0-0;
default beats the annealed25 variant +30 in both seats (the default layout's gun slots stop the single big
copies the annealed layout lets through). t22 (frozen v17 vs tuning, plain and asym:3:2) and x23 (frozen v17
vs STRONG + lead v4) running as the confirmation of the recommended artifact; a second astra review of v17
requested.

## 2026-10-31T04:48Z  Purchase-order search at 400-1500 gold (sampling gap, medium budgets)

`experiments/defense/order_search.py`, output `runs/defense/order_search.txt`. For opponent gold 400, 700, 1000,
1500 and two own positions (stage A with 1000 gold; stage A + splash (10,1) + gun3 (1,3) with 1500 gold), the
planner's zero-leak plan against the sampled compositions (8-11 compositions, plan costs 200-924 gold) was
attacked by a hill climb over purchase orders (adjacent swaps and moves, 121 evaluations each) on the sampled
multisets plus 12 random affordable multisets: no leaking order was found in any of the seven planned cases
(worst leaked damage 0). The line "G=400 ... no zero-leak plan" in the output is a misreport: that position
already stopped every 400-gold composition, so plan_defense returned no action. This is evidence, not proof:
the search is local and the multisets are a sample; astra's earlier 400-gold counterexample was against a
plan without the heavy-last orders, which are now included.

## 2026-10-31T04:53Z  t22: frozen v17 against the tuning pool (plain and asym:3:2)

`runs/defense/t22_v17_vs_tuning` (frozen v17 default, 26 opponents x {none, asym:3:2} x both seats): 104-0-0, no
rejected actions, no bot errors. t23 (same under mirror:1:2 and eco:2) running to complete the four-opening
coverage for the recommended artifact; x23 (STRONG + lead v4) and x24 (variant round robin) finishing.

## 2026-10-31T04:54Z  x23 (frozen v17 vs STRONG + lead v4), x24 (variant round robin), decision-time audit

x23 (`runs/defense/x23_strong_v17`, both seats): W 24 D 2 L 0 of 26; non-wins:
    [25/26] F17 vs experiments.lead.v4:@make  -> cand D hp_diff 0 r50 (17.613s)
    [26/26] experiments.lead.v4:@make vs F17  -> cand D hp_diff 0 r50 (17.816s)
x24 (`runs/defense/x24_variants_rr`, frozen v17 default against its own variants, both seats):
    [1/10] F17 vs F17?layout="annealed25" -> W hp_diff 30 r50 (24.088s)
    [2/10] F17?layout="annealed25" vs F17 -> W hp_diff 30 r50 (24.591s)
    [3/10] F17 vs F17?round1_poke=0 -> W hp_diff 10 r50 (28.366s)
    [4/10] F17?round1_poke=0 vs F17 -> W hp_diff 10 r50 (35.261s)
    [5/10] F17 vs F17?lethal_share=0.6 -> D hp_diff 0 r50 (18.724s)
    [6/10] F17?lethal_share=0.6 vs F17 -> D hp_diff 0 r50 (19.93s)
    [7/10] F17 vs F17?spec_share=1.0 -> W hp_diff 140 r50 (26.871s)
    [8/10] F17?spec_share=1.0 vs F17 -> W hp_diff 140 r50 (34.498s)
    [9/10] F17 vs F17?attack_from=6 -> D hp_diff 0 r50 (29.667s)
    [10/10] F17?attack_from=6 vs F17 -> D hp_diff 0 r50 (22.859s)
Reading: the default beats annealed25 (+30) and spec_share=1.0 (+140: insuring everything slows the economy
and the default's pokes land), beats round1_poke=0 by exactly the 10 HP of the round-1 poke, and draws its
lethal_share=0.6 and attack_from=6 variants 0-0 (identical openings, mutual immunity).
Decision-time audit over every tournament in runs/defense (`experiments/defense/decide_time_audit.py`, output
`runs/defense/decide_time_audit.txt`), per fortress version (all variants pooled):
    | version | matches | max single decide (s) | max decide per match (s) | rejected actions | bot errors |
    | --- | ---: | ---: | ---: | ---: | ---: |
    | live | 196 | 15.72 | 253.7 | 0 | 0 |
    | v10 | 156 | 1.28 | 6.3 | 0 | 0 |
    | v11 | 300 | 5.78 | 69.7 | 0 | 0 |
    | v12 | 312 | 2.43 | 24.0 | 0 | 0 |
    | v13 | 156 | 2.41 | 24.9 | 0 | 0 |
    | v14 | 78 | 2.38 | 23.8 | 0 | 0 |
    | v15 | 422 | 4.15 | 64.2 | 0 | 0 |
    | v17 | 168 | 4.30 | 49.6 | 0 | 0 |
    | v3 | 104 | 1.66 | 9.0 | 0 | 0 |
    | v4 | 162 | 10.96 | 45.8 | 0 | 0 |
    | v5 | 156 | 1.90 | 6.9 | 0 | 0 |
    | v6 | 153 | 11.72 | 67.5 | 0 | 0 |
    | v7 | 76 | 1.09 | 3.5 | 0 | 0 |
    | v8 | 152 | 18.43 | 65.5 | 0 | 0 |
    | v9 | 156 | 1.14 | 12.2 | 0 | 0 |
No rejected actions and no bot errors in any recorded match of any version. The large per-match maxima belong to
pure-turtle variants against the mirror/stacker counters before the v9 time budget.

## 2026-10-31T05:00Z  t23: frozen v17 under mirror:1:2 and eco:2 openings

`runs/defense/t23_v17_scen2` (frozen v17 default, 26 tuning opponents, both seats): 104-0-0. Frozen v17 totals:
tuning pool 208-0-0 over four opening conditions (none, asym:3:2, mirror:1:2, eco:2; t22 + t23), STRONG pool
plus the lead's v4 24-2-0 (x23; the draws are the 0-0 games against lead v4). No rejected actions, no errors.

## 2026-10-31T05:02Z  Second astra review of v17 (astra/v17-review/answer.md in the lane directory): findings and fixes (v18)

1. A full-match counter beats v17 in both seats, 240:748 at round 50: hrt-w3's `counters.public_factory:@timing`
   forecasts the public deterministic policy, insures round 1 against the 2-tier1 poke (4 walls + gun1, 3
   factories), grows, buys two tier5 in round 8 (1324 gold) and then defends its lead. v17 took 280 + 140 + 140
   because the worst sampled threat (300) stayed under the 0.4 x 800 = 320 trigger and the zero-leak plan
   exceeded 0.6 x gold. Variants lethal_share 0.3 / 0.2 are being tested against that counter at attack rounds
   7, 8, 9 (x25). The same counter loses both asym:3:2 matches to v17.
2. Bug: wrap_bundles padded one copy too few (the heavy copy spawned at tick 249, not 0; engine entries are
   zero-based). Fixed in plan.py (pad = ticks*m - n_visible; verified: 206 visible + 44 pads -> heavy entry 250).
   Astra's fixture (round 20, v17 at 100 HP) showed the omitted order dealing 140 and v17 losing -40:650.
3. Finish-first bait in the final round: with v17 at 40 HP and the opponent at 30 HP and 100 gold, v17 bought
   7 tier1 (predicted kill 35); the opponent bought a splash + tier2 instead and won 28:30, while walls + gun2
   would have secured 40:30 (astra checked all 27 ordered purchase lists in both seats). Causes: the kill
   simulation ignores same-round construction; "cannot kill me" does not protect an HP lead in round 50; the
   "no defence saves me" inference uses one bounded greedy plan. Fix: no finish-first in the final round, and in
   the final round the speculative step spends all gold with partial plans allowed (gold has no later value).
   The round-50 bait position itself is not shown to be reachable against v17 from the start.
4. Robustness: the optional round1="splash"/"gun2" turret now checks legality of (10,1); purchase bundles are
   capped (gold 30000, 600 copies per bundle) so absurd opponent gold cannot exhaust memory; exhaustive
   enumeration covers opponent gold up to 195 (400 lists), everything above relies on sampling (documented).
   One v17 decision took 3.5 s: the 3 s budget bounds the gun pass, not the whole call.
No overspending, forbidden information or exceptions were found in default play (astra's edge checks: zero
gold, empty compositions, round 50, opponent HP <= 0, 501-entry rosters, occupied layout cells; 40 planner
checks). Frozen as v18 after check_plan 60.

## 2026-10-31T05:05Z  x25: the forecasting counter beats every lethal_share setting

`runs/defense/x25_forecast_counter` (frozen v18; opponent hrt-w3's `counters.public_factory:@timing` forecasting the
v18 default, tier5 wave with all gold at round 7, 8 or 9; both seats): default -140 / -508 / -560; lethal_share
0.3: -140 / -280 / -420; lethal_share 0.2: -140 / -420 / -840 (the 0.2 variant over-insures, its economy stalls
and it is destroyed in round 12). All at round 50 except the last. Mechanism: the counter insures round 1
(stopping the 2-tier1 poke), never attacks early (so fortress's mandatory defence stays minimal), out-grows
fortress while fortress's speculative rule declines the expensive zero-leak plans, then lands a tier5 wave and
defends its lead. The HP-share trigger is the wrong tool: lowering it only moves the losses. The lead's
exploitability screen (NOTES_FOR_TEAM 04:57Z) points to an absolute trigger (insure fully when the worst
affordable roster would deal >= 100 this round) plus a response-aware attack (attack only if it still leaks
after the opponent's best same-round defence) and no poke insurance; both are now fortress options
(big_threat, robust_attack; the response is estimated by running plan_defense for the opponent with all its
gold) and x27 tests them against forecast counters at rounds 6 (tier4), 8 and 10 (tier5).

## 2026-10-31T05:06Z  t24 and x26: frozen v18 regression on both pools

t24 (`runs/defense/t24_v18_vs_tuning`, 26 tuning opponents x {none, asym:3:2}, both seats) and x26
(`runs/defense/x26_strong_v18`, STRONG + lead v4): results as for v17 (see summary.md rows below); the wrap fix,
final-round rule and caps changed no outcome on these pools.
    t24_v18_vs_tuning: | bot_research.bots.defense.frozen.v18.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |
    x26_strong_v18: | bot_research.bots.defense.frozen.v18.fortress:@make | 26 | 22 | 2 | 2 | 0.885 |
x28 (frozen v18 vs the forecasting counter at the lead's remaining timings: tier3 at rounds 3/5, tier4 at 5/7/9,
tier5 at 10/11) running as the exploitability profile of the current artifact.

## 2026-10-31T05:09Z  Regression in v18 found and fixed (v19): bundle caps hid the saturation requirement

x26 (`runs/defense/x26_strong_v18`): frozen v18 lost -6010 at round 48 to econ frozen v2 in both seats (every
earlier version drew 800-800), while beating the live econ +430. Log
`x26_strong_v18/logs/20261031T050220-00009--make_fortress-vs--make_econ-std.jsonl`: fortress stopped at 22
splashes + 5 gun3 (per-copy splash below 1500) and econ v2 bought 300 tier5 in round 48 (46 arrivals, 6440
damage). Cause: the v18 cap MAX_BUNDLE_GOLD = 30000 reduced the opponent's all-tier5 bundle to 46 copies,
which that defence stops, so the speculative step saw zero leaks and never bought saturation; before v18 the
uncapped bundle (hundreds of tier5) forced the splash plan to 150 adjacency once affordable (round ~15).
Fix (v19): caps raised to 10^6 gold / 2000 copies, and the leak check now uses two exact shortcuts instead of
simulating huge compositions: a composition whose every type has HP <= the per-copy splash exposure cannot
leak (proved); a composition above 400 copies with a type above the exposure is counted as leaking (guns kill
at most one copy per tick each), so the planner buys saturation. Check from a round-15 position (22 splashes,
opponent 400000 gold, own 5000): the plan now raises exposure to >= 1500 in under a second; the 10^12-gold
case stays bounded. check_plan 60 passes. x29 (frozen v19 vs STRONG + lead v4) running; t25 (tuning) follows.
Lesson for the report: a sampling cap must never remove the composition that forces the proved immunity.

## 2026-10-31T05:10Z  x27 (big_threat / robust_attack options) and x28 (v18 profile) against the forecasting counter

Opponent in both: hrt-w3's `counters.public_factory:@timing` forecasting the frozen v18 default (so its forecast
of the variants is slightly off, as it would be against an unknown member of a pool); both seats.
x27 (live fortress variants; `runs/defense/x27_options_vs_forecast`):
    [1/24] big_threat=100 vs tier=tier5&attack_round=8 -> L hp_diff -420 r50 (8.62s)
    [2/24] tier=tier5&attack_round=8 vs big_threat=100 -> L hp_diff -420 r50 (8.611s)
    [3/24] big_threat=100 vs tier=tier5&attack_round=10 -> L hp_diff -1120 r11 (3.669s)
    [4/24] tier=tier5&attack_round=10 vs big_threat=100 -> L hp_diff -1120 r11 (3.635s)
    [5/24] big_threat=100 vs tier=tier4&attack_round=6 -> L hp_diff -60 r50 (10.849s)
    [6/24] tier=tier4&attack_round=6 vs big_threat=100 -> L hp_diff -60 r50 (10.807s)
    [7/24] robust_attack=true vs tier=tier5&attack_round=8 -> L hp_diff -140 r50 (13.651s)
    [8/24] tier=tier5&attack_round=8 vs robust_attack=true -> L hp_diff -140 r50 (13.69s)
    [9/24] robust_attack=true vs tier=tier5&attack_round=10 -> D hp_diff 0 r50 (10.137s)
    [10/24] tier=tier5&attack_round=10 vs robust_attack=true -> D hp_diff 0 r50 (10.142s)
    [11/24] robust_attack=true vs tier=tier4&attack_round=6 -> D hp_diff 0 r50 (10.1s)
    [12/24] tier=tier4&attack_round=6 vs robust_attack=true -> D hp_diff 0 r50 (10.202s)
    [13/24] big_threat=100&robust_attack=true vs tier=tier5&attack_round=8 -> D hp_diff 0 r50 (12.708s)
    [14/24] tier=tier5&attack_round=8 vs big_threat=100&robust_attack=true -> D hp_diff 0 r50 (12.581s)
    [15/24] big_threat=100&robust_attack=true vs tier=tier5&attack_round=10 -> D hp_diff 0 r50 (12.267s)
    [16/24] tier=tier5&attack_round=10 vs big_threat=100&robust_attack=true -> D hp_diff 0 r50 (12.287s)
    [17/24] big_threat=100&robust_attack=true vs tier=tier4&attack_round=6 -> D hp_diff 0 r50 (12.232s)
    [18/24] tier=tier4&attack_round=6 vs big_threat=100&robust_attack=true -> D hp_diff 0 r50 (12.243s)
    [19/24] big_threat=100&robust_attack=true&poke_insurance=false vs tier=tier5&attack_round=8 -> D hp_diff 0 r50 (11.202s)
    [20/24] tier=tier5&attack_round=8 vs big_threat=100&robust_attack=true&poke_insurance=false -> D hp_diff 0 r50 (11.28s)
    [21/24] big_threat=100&robust_attack=true&poke_insurance=false vs tier=tier5&attack_round=10 -> D hp_diff 0 r50 (11.246s
    [22/24] tier=tier5&attack_round=10 vs big_threat=100&robust_attack=true&poke_insurance=false -> D hp_diff 0 r50 (11.304s
    [23/24] big_threat=100&robust_attack=true&poke_insurance=false vs tier=tier4&attack_round=6 -> D hp_diff 0 r50 (11.269s)
    [24/24] tier=tier4&attack_round=6 vs big_threat=100&robust_attack=true&poke_insurance=false -> D hp_diff 0 r50 (15.554s)
x28 (frozen v18 default at the lead's remaining timings; `runs/defense/x28_v18_profile`):
    [1/14] F18 vs tier=tier3&attack_round=3 -> L hp_diff -14 r50 (6.159s)
    [2/14] tier=tier3&attack_round=3 vs F18 -> L hp_diff -14 r50 (6.064s)
    [3/14] F18 vs tier=tier3&attack_round=5 -> D hp_diff 0 r50 (7.792s)
    [4/14] tier=tier3&attack_round=5 vs F18 -> D hp_diff 0 r50 (7.852s)
    [5/14] F18 vs tier=tier4&attack_round=5 -> L hp_diff -48 r50 (8.253s)
    [6/14] tier=tier4&attack_round=5 vs F18 -> L hp_diff -48 r50 (8.176s)
    [7/14] F18 vs tier=tier4&attack_round=7 -> L hp_diff -120 r50 (10.625s)
    [8/14] tier=tier4&attack_round=7 vs F18 -> L hp_diff -120 r50 (10.694s)
    [9/14] F18 vs tier=tier4&attack_round=9 -> L hp_diff -420 r50 (8.205s)
    [10/14] tier=tier4&attack_round=9 vs F18 -> L hp_diff -420 r50 (8.254s)
    [11/14] F18 vs tier=tier5&attack_round=10 -> L hp_diff -840 r10 (3.315s)
    [12/14] tier=tier5&attack_round=10 vs F18 -> L hp_diff -840 r10 (3.297s)
    [13/14] F18 vs tier=tier5&attack_round=11 -> D hp_diff 0 r50 (7.692s)
    [14/14] tier=tier5&attack_round=11 vs F18 -> D hp_diff 0 r50 (7.717s)
Reading of x27/x28: against the forecasting counter the default fortress loses at 9 of 10 timings (round-3 tier3
-14 up to round-10 tier5 -840 with base destruction) and draws at tier3 round 5 and tier5 round 11; big_threat
alone over-insures (-1120 destroyed at round 11); robust_attack alone (attack only if the purchase still leaks
after the opponent's best same-round response, estimated with plan_defense on its map) already draws at two of
three timings; big_threat=100 together with robust_attack draws 0-0 at all three, with or without poke insurance.
The mechanism: the robust attack stops wasting gold on pokes that a forecasting opponent will block, so the
economy keeps up, and the absolute trigger buys defence as soon as a tier4/tier5 is affordable to the
opponent. Whether this configuration keeps its 100 percent results on the development pools is being tested
(t26); a draw against the forecaster is the best any deterministic policy achieved on this box so far (the
lead's screen: -26 worst for its equivalent setting).

## 2026-10-31T05:14Z  t25 (v19 regression) and t26 (robust configuration on the tuning pool); two recommended configurations

t25 (`runs/defense/t25_v19_vs_tuning`, frozen v19 default, 26 opponents x {none, asym:3:2}, both seats): 104-0-0; the
caps fix did not change tuning-pool results. t26 (`runs/defense/t26_robust_vs_tuning`, frozen v19 with
big_threat=100 and robust_attack=true, plain openings): 50-2-0, the two draws being 0-0 against the pool turtle
(the robust attack declines pokes that the opponent could answer with its gold, so a rich pure defender is no
longer beaten by +76 as before).
Recommendation to the lead (two configurations of the same frozen artifact, `bots/defense/frozen/v19`):
- pool-strong: `bot_research.bots.defense.frozen.v19.fortress:@make` (tuning 104-0-0 and 208-0-0 for v17/v18 over
  four openings, STRONG + lead v4 24-2-0 expected (x29 running), but loses to a forecasting counter at most
  timings, up to base destruction);
- forecast-robust: `bot_research.bots.defense.frozen.v19.fortress:@make?big_threat=100&robust_attack=true`
  (draws the forecasting counter 0-0 at the three timings tested so far, tuning 50-2-0; STRONG run x30 and the
  full timing profile x31 running).
These are complementary strengths, not a dominant policy: the robust one gives up the wins against passive rich
turtles that the pool-strong one collects, and gains immunity to the strongest counter found.

## 2026-10-31T05:16Z  x29: frozen v19 default against the STRONG pool

`runs/defense/x29_strong_v19` (both seats): 24-2-0, draws only against the lead's v4 (0-0); econ frozen v2 is
beaten again (the v18 regression is gone) and the live econ as well. So the pool-strong configuration is back to
its v17 record on both development pools (t25 104-0-0, x29 24-2-0).

## 2026-10-31T05:17Z  x30: the robust configuration against the STRONG pool

`runs/defense/x30_robust_strong` (frozen v19 with big_threat=100 and robust_attack=true, 12 STRONG specs + lead
v4, both seats): 24-2-0, identical to the default (draws 0-0 against lead v4, every other member beaten including
both econ versions). So on the STRONG pool the robust attack gives nothing up; on the tuning pool it costs the
two wins against the pool turtle (t26). x31/x32 (forecaster profiles for big_threat 100/60/26) and t27 (robust
configuration under asym:3:2 and mirror:1:2 openings) running; the default of fortress will be switched to the
robust configuration if the profiles confirm.

## 2026-10-31T05:19Z  x31: exploitability profile of the robust configuration; x32 (lower big_threat) so far

x31 (`runs/defense/x31_robust_profile`, frozen v19 with big_threat=100 and robust_attack=true vs hrt-w3's
forecasting counter at 8 timings, both seats): tier3 at round 3: -26, tier3 at round 5: -26, tier4 at round 5:
-60; tier4 at rounds 7 and 9, tier5 at rounds 7, 9 and 11: all 0-0 draws. Compared with the default's profile
(x25/x28: -14 to -840 at 9 of 10 timings, base destroyed at tier5 round 10), the robust configuration's worst
case is one early hit of a single copy that costs less than 100 damage and therefore does not trigger the
insurance. x32 (same counter, big_threat=60): tier3 round 3 still -26 (26 < 60), tier4 round 5 now 0-0, tier5
rounds 8 and 10 0-0; the big_threat=26 variant is running. t28 (big_threat=60 vs the tuning pool) checks what the
lower threshold costs in economy against ordinary opponents.

## 2026-10-31T05:22Z  x32 and t28: lower big_threat thresholds fail; 100 is the usable value

x32 (`runs/defense/x32_bt60_profile`, forecaster at tier3 r3 / tier4 r5 / tier5 r8 / tier5 r10, both seats):
big_threat=60: -26, 0, 0, 0; big_threat=26: 0, 0, -700, -840 (base destroyed at round 10): insuring against
every affordable tier3 drains the economy so much that the tier5 waves of rounds 8-10 are no longer affordable
to stop. t28 (`runs/defense/t28_bt60_vs_tuning`, big_threat=60 vs the tuning pool, plain openings): loses -1170
at round 9 to eco_then_flood(8, tier5) and to eco6_t5 in both seats, draws the pool turtle; the same
over-insurance mechanism against ordinary growth-then-flood opponents. Conclusion (empirical, these pools):
big_threat=100 with robust_attack is the only tested setting that keeps the development-pool record
(50-2-0 / 24-2-0) and neutralizes the forecaster from round 7 on; its residual exposure is one early single
tier3 or tier4 hit (-26 / -60), which no tested threshold removes without losing elsewhere.

## 2026-10-31T05:25Z  t27: the robust configuration fails under scripted openings; v19 default stays

`runs/defense/t27_robust_asym` (frozen v19 with big_threat=100 and robust_attack=true, 26 tuning opponents under
asym:3:2 and mirror:1:2, both seats): 92-4-8, losses of -800 to -1495 at rounds 10-11 against eco_then_flood (8
and 11), eco6_t5, plus draws against splash_turtle. The default configuration scored 104-0-0 under the same
openings (t24, t20). Log `t27_robust_asym/logs/20261031T051720-00018-...asym-3-2.jsonl`: fortress started the
asym opening with 32 random walls and 2 factories against 15 walls and 4 factories; the robust attack then never
poked an opponent that owned no turret for seven rounds (its gold could have bought a defence, so the
response-aware check vetoed every purchase), while the absolute insurance bought a splash and three gun3 by
round 7; the opponent reached 120 factories against 28 and its waves of rounds 8-10 (140, 420, 700) destroyed
the base. So the two configurations have strictly complementary failure modes: the default is beaten by an
opponent that forecasts it and defends its lead; the robust one is beaten by passive growth-then-flood
opponents from unequal openings. Decision: the live defaults were reverted to the default configuration (v19
behaviour); frozen v20 keeps the robust configuration as defaults (NOTE.txt inside) and the runs started for it
were stopped as redundant. A middle ground, robust_attack="adaptive" (assume a same-round response only from
opponents that already own a turret), is being tested (t30: tuning plain + asym:3:2; x34: forecaster profile).

## 2026-10-31T05:28Z  Shift-1 summary for the report (supersedes the 03:05Z and 04:05Z summaries)

Deliverables (all under bot_research/, lane hrt-w1): component `bots/defense/plan.py` (plan_defense,
threat_compositions with exhaustive enumeration up to 400 ordered purchase lists and sampled heavy-first /
heavy-last / screen / interleaved / roster-wrap bundles above that, exact leak shortcuts, foreign-map fallback,
plan_walls, defense_cost, opponent_leak, threat_damage, robust_leak, MasterLayout, layout_by_name), `simulate.py`,
`geometry.py`, `templates.py` (ANNEALED_25/26, PILLARS_7_7_4, LEAD_V3); bot `bots/defense/fortress.py` (make(),
options documented in its docstring); frozen copies v3..v20 with SHA256SUMS; experiments in
`experiments/defense/` and results in `runs/defense/` (t1-t30, x1-x35, check_plan_*, q1/q2 tables, template
evaluations, gun_value, round1_insurance, sampling_gap, order_search, decide_time_audit).

Recommended artifacts (complementary, no dominant one):
- `bot_research.bots.defense.frozen.v19.fortress:@make` (pool-strong): tuning pool 104-0-0 plain + asym:3:2
  (t25) and 104-0-0 mirror + eco (t23, as v17; v19 differs only in the saturation fix), STRONG pool + lead v4
  24-2-0 (x29; draws = 0-0 against the lead's v4, which runs this lane's planner), self-play draw; beaten by a
  counter that forecasts it (hrt-w3 public_factory timing: -14 to -840 at 9 of 10 timings, x25/x28).
- `bot_research.bots.defense.frozen.v20.fortress:@make` (forecast-robust; = v19 with big_threat=100 and
  robust_attack=true): draws that forecaster 0-0 at every timing from round 7 on and concedes at most -60 to a
  single early tier3/tier4 (x31); STRONG 24-2-0 (x30); tuning plain 50-2-0 (t26); but 92-4-8 under scripted
  openings (t27: it never pokes a turret-less opponent whose gold could defend, and over-insures).
  Intermediate settings tested (lethal_share 0.2-0.6, big_threat 26/60, robust_attack="adaptive") are
  dominated (x25, x32, t28, t30/x34).

Proved: full-route splash exposure 10 x adjacency, independent of the stream; adjacency >= 150 is immunity;
subsets of legal layouts are legal; symmetric deterministic play draws. Empirical, exact: Q1 route tables (max
86 found), Q2 cost tables, S(k) template curves, gun table, round-1 table, sampling-gap and order-search checks
(no leaking order found at 200-1500 gold against the plans), decision-time audit (no rejected action or bot
error in any recorded match of any version; max 4.3 s per call for v17). Empirical, matches: as above; the
engine is deterministic, so the variation across matches is the opponent policy, the seat and the scripted
opening, never a seed.

Known failures and limits: (1) blind round 1 (24-32 HP exposure or 80-100 gold of insurance; the 2-tier1 poke
is the default because it dominated on every pool tested, but a round-1 insurer then leads by 10 HP); (2) a
forecaster of the public deterministic policy beats the pool-strong default (fixable only at the price of
the robust configuration's own weakness, or by a response model the lead's policy layer provides);
(3) threat compositions are sampled above 195 gold of opponent spending, so zero-leak claims hold for the
sampled set (one astra counterexample fixed, none found afterwards by local search); (4) a sampling cap must
never remove the composition that forces immunity (v18 regression, fixed in v19); (5) plan_defense is a
greedy with restricted candidates: costs are upper bounds; (6) the template planner degrades on maps full of
foreign walls (fallback added in v15, one -255 loss remained before it).

## 2026-10-31T05:31Z  t30/x34: the adaptive robust attack is dominated; fractional response sweep started

t30 (`runs/defense/t30_adaptive_scen`, live fortress with big_threat=100 and robust_attack="adaptive", tuning pool
x {none, asym:3:2}): 92-2-10, losing -435 to eco_then_flood(8, tier5) even from the plain opening and -375 to
-1255 under asym:3:2 (eco_then_flood 8 and 11). x34 (same vs the forecaster at 5 timings): 0-6-4 (-26, -60 early,
draws from round 7). Mechanism: against a turret-less growth-then-flood opponent the adaptive rule pokes like
the default (it owns no turret) while the absolute insurance stalls the economy like the robust configuration,
so it neither kills by round 7 nor affords the saturation by round 9: the half-measure is worse than either
pure configuration. x35 (adaptive vs STRONG) finishing. New sweep: robust_attack as a fraction f of the
opponent's gold assumed spent on its response (f = 1 is v20, f = 0 the default); f = 0.5 with and without
big_threat=100 running on the forecaster profile (x36) and the tuning pool with openings (t31).
x35 (`runs/defense/x35_adaptive_strong`, adaptive configuration vs STRONG + lead v4): 24-2-0 of 26; non-wins:
    [25/26] ADA vs experiments.lead.v4:@make -> D hp_diff 0 r50 (28.338s)
    [26/26] experiments.lead.v4:@make vs ADA -> D hp_diff 0 r50 (27.823s)
x37 (fraction f = 0.5 with and without big_threat=100 vs STRONG + lead v4) launched.

## 2026-10-31T05:40Z  Fraction sweep (t31, x36): no setting dominates; the complementary pair is final for this shift

t31 (`runs/defense/t31_frac_scen`, live fortress, tuning pool x {none, asym:3:2}, both seats): robust_attack=0.5
with big_threat=100: 96-4-4; robust_attack=0.5 alone: 98-3-3; the losses are again the asym:3:2 flood games
(eco_then_flood 8 and 11, eco6_t5: -785 to -1210) that the default (f = 0) wins 104-0-0. x36
(`runs/defense/x36_frac_profile`, forecaster at 5 timings): 0-6-4 with big_threat (-26, -60 early; draws from
round 7) and 0-4-6 without it (the two tier5 timings lost as well). So any response-aware attack, damped or
not, concedes the asymmetric-opening flood games, and only the full robust configuration also neutralizes the
late forecaster waves. Final picture for this shift: two frozen configurations with disjoint failure modes,
v19 (pool-strong default) and v20 (forecast-robust); every intermediate tested is dominated by one of them on
one pool without beating it on the other. x37 (f = 0.5 vs STRONG + lead v4) finishing.
Decision-time audit refreshed (`runs/defense/decide_time_audit.txt`): no rejected action and no bot error in
any recorded match of any version; the live variants with response-aware attacks take up to about 30 s per
match (two plan_defense calls per round when the opponent is rich).
x37 (`runs/defense/x37_frac_strong`, f = 0.5 with and without big_threat=100 vs STRONG + lead v4, both seats):
    | bot_research.bots.defense.fortress:@make?big_threat=100&robust_attack=0.5 | 26 | 24 | 2 | 0 | 0.962 |
    | bot_research.bots.defense.fortress:@make?robust_attack=0.5 | 26 | 24 | 2 | 0 | 0.962 |
non-wins:
    [25/52] big_threat=100&robust_attack=0.5 vs experiments.lead.v4:@make -> D hp_diff 0 r50 (28.661s)
    [26/52] experiments.lead.v4:@make vs big_threat=100&robust_attack=0.5 -> D hp_diff 0 r50 (29.973s)
    [51/52] robust_attack=0.5 vs experiments.lead.v4:@make -> D hp_diff 0 r50 (27.823s)
    [52/52] experiments.lead.v4:@make vs robust_attack=0.5 -> D hp_diff 0 r50 (27.669s)

## 2026-10-31T05:47Z  Adaptive response-aware attack without insurance: a near-Pareto improvement (t32, x38)

Variant: live fortress with robust_attack="adaptive" (the opportunistic purchase is checked against the
opponent's best same-round response only when the opponent already owns a turret) and no absolute insurance
(big_threat None, lethal_share 0.4 as in v19).
t32 (`runs/defense/t32_adaptive_noins_scen`, 26 tuning opponents x {none, asym:3:2}, both seats): 102-2-0; the two
draws are 0-0 against the pool turtle (it owns turrets, so pokes against it are vetoed); every asym:3:2 flood
game that the robust and half-robust configurations lost is won (turret-less growers are poked as by the
default). x38 (`runs/defense/x38_adaptive_noins_profile`, forecaster at 5 timings, both seats): tier3 r3 -26,
tier4 r5 -60, tier4 r7 0, tier5 r8 -140, tier5 r10 0; the default scored -14, -48, -120, -508, -840 at the
same timings (x25/x28) and the robust configuration -26, -60, 0, 0, 0 (x31). So this variant keeps the
default's pool record except two pool-turtle draws, removes the forecaster's base-destroying waves, and
concedes one tier5 hit at the round-8 timing. x39 (same vs STRONG + lead v4) running; if it matches the
default's 24-2-0 the fortress default switches to robust_attack="adaptive" (v21).

## 2026-10-31T05:50Z  x39 and the new default (v21): robust_attack="adaptive"

x39 (`runs/defense/x39_adaptive_noins_strong`, adaptive attack without insurance vs STRONG + lead v4, both seats):
24-2-0, draws only against the lead's v4 (0-0), identical to the default's record. With t32 (102-2-0 on the
tuning pool incl. asym:3:2) and x38 (worst -140 against the forecaster instead of -840), this configuration
weakly dominates the previous default on every pool tested except the two pool-turtle draws, so it is the
fortress default from v21 on (frozen `bots/defense/frozen/v21`; recommended spec
`bot_research.bots.defense.frozen.v21.fortress:@make`). Alternatives remain frozen: v19 (previous default:
wins the pool turtle, loses to forecasters) and v20 (full robust configuration: draws forecasters from round 7,
loses asymmetric-opening flood games). Confirmation runs: t34 (frozen v21 vs tuning plain + asym:3:2), t33
(adaptive vs tuning under mirror:1:2 + eco:2), x40 (adaptive vs forecaster at the other five timings).
Decision rule of the adaptive attack: a poke is bought when exact simulation on the opponent's current map says
it leaks at least 0.1 damage per gold, and, if the opponent already owns a turret, also after the opponent's
best same-round response estimated by running plan_defense for it with all its visible gold.

## 2026-10-31T05:53Z  t33 and x40: the adaptive default under the other openings and timings

t33 (`runs/defense/t33_adaptive_noins_scen2`, adaptive attack, 26 tuning opponents x {mirror:1:2, eco:2}, both seats):
100-4-0 of 104 (the harness split the candidate into two version rows because the live fortress default was edited during the run; the two rows are summed here); the draws are 0-0 against splash_turtle (mirror:1:2) and the pool turtle (eco:2), both
turret owners whose pokes are vetoed. x40 (`runs/defense/x40_adaptive_noins_profile2`, forecaster at tier3 r5,
tier4 r9, tier5 r7/9/11): -26, 0, 0, 0, 0. Full forecaster profile of the adaptive default over the lead's ten
timings: tier3 r3 -26, tier3 r5 -26, tier4 r5 -60, tier4 r7 0, tier4 r9 0, tier5 r7 0, tier5 r8 -140, tier5 r9 0,
tier5 r10 0, tier5 r11 0 (the previous default: -14, 0, -48, -120, -420, ?, -508, -560, -840, 0). Confirmation
runs of the frozen v21 artifact itself: t34 (tuning plain + asym:3:2), t35 (mirror:1:2 + eco:2), x41 (STRONG + lead v4).

## 2026-10-31T05:57Z  Frozen v21 confirmed on all development pools (recommended artifact)

Summary rows (both seats; t34 = 26 tuning opponents x {none, asym:3:2}; t35 = x {mirror:1:2, eco:2}; x41 = 12 STRONG
specs + the lead's v4):
    t34_v21_vs_tuning: | bot_research.bots.defense.frozen.v21.fortress:@make | 104 | 102 | 2 | 0 | 0.990 |
    t35_v21_scen2: | bot_research.bots.defense.frozen.v21.fortress:@make | 104 | 100 | 4 | 0 | 0.981 |
    x41_strong_v21: | bot_research.bots.defense.frozen.v21.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |
Non-wins (all 0-0 draws against turret-owning turtles or the lead's v4, which runs this lane's planner):
    x41.log:[25/26] F21 vs experiments.lead.v4:@make -> D hp_diff 0 r50 (15.63s)
    x41.log:[26/26] experiments.lead.v4:@make vs F21 -> D hp_diff 0 r50 (16.067s)
    t35.log:[29/104] F21 vs harness.baselines:@splash_turtle mirror:1:2 -> cand D hp_diff 0 r50 (8.881s)
    t35.log:[30/104] harness.baselines:@splash_turtle vs F21 mirror:1:2 -> cand D hp_diff 0 r50 (9.107s)
    t35.log:[91/104] F21 vs bots.counters.pool:@turtle eco:2 -> cand D hp_diff 0 r50 (12.156s)
    t35.log:[92/104] bots.counters.pool:@turtle vs F21 eco:2 -> cand D hp_diff 0 r50 (12.335s)
Recommended spec: `bot_research.bots.defense.frozen.v21.fortress:@make` (planner = plan.py of v19-v21; fortress
defaults: walls first, finish-first except in round 50, mandatory zero-leak vs the visible roster, speculative
zero-leak vs sampled affordable compositions if <= 0.6 x gold with poke insurance and lethal_share 0.4,
2-tier1 round-1 poke, opportunistic attack by exact simulation with the adaptive response check, factories
capped at 40 per round). Forecaster profile: worst -140 (x38/x40). Alternatives kept frozen: v19, v20.

## 2026-10-31T05:57Z  Summary addendum: recommended artifact is frozen v21

Supersedes the recommendation in the 05:28Z shift summary: the recommended fortress is
`bot_research.bots.defense.frozen.v21.fortress:@make` (adaptive response-aware attack, no absolute insurance), with
v19 (pool-strong, forecaster-exploitable) and v20 (forecast-robust, loses asymmetric-opening floods) kept as
documented alternatives. Evidence for v21: tuning pool 102-2-0 (plain + asym:3:2, t34) and 100-4-0 (mirror:1:2 +
eco:2, t35), all non-wins 0-0 draws against turret-owning turtles; STRONG + lead v4 24-2-0 (x41); forecaster
profile over ten timings worst -140 (x38/x40, live copy with identical code). A third astra review of v21 has been
requested (astra/v21-review in the lane directory); its findings will be recorded by the next shift if they
arrive after this one ends.

## 2026-10-31T06:05Z  x42: frozen v21 against a forecaster that models frozen v21 exactly

`runs/defense/x42_v21_exact_forecast` (hrt-w3's public_factory timing counter with model_spec = the frozen v21
spec, ten timings, both seats): tier3 r3 -26, tier3 r5 -26, tier4 r5 -60, tier4 r7 0, tier4 r9 0, tier5 r7 0,
tier5 r8 -140, tier5 r9 0, tier5 r10 0, tier5 r11 0 (0-12-8 as W-D-L; mean -25 HP). Identical to the profile
measured with the v19-modelled forecaster (x38/x40), so the exact forecast of the adaptive rule does not open a
further gap: the residual exposure of v21 against a perfect forecaster is one early single copy (26-60 HP)
or one tier5 hit at the round-8 timing (140 HP). Against every other opponent tested v21 wins or draws.

## 2026-10-31T06:11Z  Third astra review (astra/v21-review/answer.md): v21's adaptive rule has a trivial counter; v22

Findings (astra, verified by matches on the unchanged engine, both seats):
1. A non-forecasting schedule beats v21 800-240 in both seats: gun1 at (3,1) + 3 factories in round 1, maximum
   factories to round 6, tier5 waves of 1, 2, 2 copies in rounds 7-9, then splash saturation (using this lane's
   planner) and factories. The single early turret switches v21's adaptive rule on, the response check with
   the opponent's whole gold vetoes every poke, the opponent grows unopposed and the waves land (280 + 280).
   The same schedule loses to the v19 default by round 8 (240 : -75) and loses under asym:3:2 openings.
   So the adaptive rule is a regression against passive growers that own one cheap turret; v21 is withdrawn
   as the recommendation.
2. The exact-v21 forecaster reproduces x42 exactly (774, 740, 660 HP at the losing timings, 800-800 elsewhere).
3. Code: opponent_view uses only public state (confirmed); robust_leak tests one heuristic response, so a
   positive leak is no worst-case guarantee; the adaptive check tested only the best unresponded candidate and
   mixed responded/unresponded baselines (fixed: all tiers are re-evaluated with consistent responded totals);
   the "exact" wording of the huge-composition shortcut was false (it over- and under-counts hits in
   constructed cases: 1 vs 0, 750 vs 912); only the zero result is sound (wording fixed in plan.py and here);
   the finish rule can still discard a winning continuation near the end (synthetic round-49 state: -4 : 5
   instead of 6 : 5); fixed by excluding finish-first from the last two rounds, and the "draw at worst" claim
   is withdrawn; float products overflow at absurd gold (10^400): guarded by capping gold at 10^9.
   A bounded search of 123664 purchase orders found no further sampling exploit; the 89-gold round-1
   certificate still holds against all 27 ordered rosters.
Decision: live default robust_attack=False again (v19 behaviour) plus the fixes above = frozen v22
(recommended spec `bot_research.bots.defense.frozen.v22.fortress:@make`). The counter is reproduced as
`bots/defense/counter_earlygun.py` (test bot, spec @make?growth=6&lock_from=10) and run against frozen v19, v21,
v22 and v22 with the repaired adaptive option (x43); v22 confirmation runs on STRONG (x44) and tuning (t36).

## 2026-10-31T06:13Z  x43: the early-gun counter reproduced against v19, v21, v22

`runs/defense/x43_earlygun` (counter_earlygun with growth 6 / lock 10 and growth 7 / lock 11, both seats): frozen v19
wins +315 / +595 at round 8, frozen v22 identical (+315 / +595 at round 8), frozen v21 loses -560 / -140 at round
50, and v22 with the repaired adaptive option still loses -560 / -140. This confirms astra's finding and the
withdrawal of the adaptive rule: a response-aware poke veto is exploited by any opponent that owns one cheap
turret and simply grows. The repaired check (all tiers, consistent responded totals) does not change that.

## 2026-10-31T06:15Z  For the lead: the frozen best_v9a against the early-gun counter (development check, not pool A/B)

`runs/defense/x45_best9a_earlygun` (`bot_research.bots.best:@make` = frozen best_v9a of 06:11Z, vs
`bot_research.bots.defense.counter_earlygun:@make` with growth 6 / lock 10, 7 / 11 and 5 / 9, both seats): six
800-800 draws at round 50. The candidate's absolute insurance stops the tier5 waves, but its response-aware
attack never pokes the counter (which owns one gun1 from round 1 and grows), so no damage is exchanged; the
same counter is beaten +315 to +595 by round 8 by the fortress default v19/v22, whose pokes are not vetoed. This is
the risk the lead listed ("the turret condition reads any turret"): against one cheap early turret plus pure
growth, best_v9a gives up the win that the non-robust attack takes. Not a loss; a trade of 6 wins for draws on
this pattern. The counter bot is in this lane's directory for reuse.

## 2026-10-31T06:18Z  Frozen v22 confirmed (recommended artifact at the end of shift 1)

Summary rows (both seats; t36 = 26 tuning opponents x {none, asym:3:2}; x44 = 12 STRONG specs + the lead's v4):
    t36_v22_vs_tuning: | bot_research.bots.defense.frozen.v22.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |
    x44_strong_v22: | bot_research.bots.defense.frozen.v22.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |
Non-wins (t36 then x44):
    t36: none
    x44.log:[25/26] F22 vs experiments.lead.v4:@make -> D hp_diff 0 r50 (14.85s)
    x44.log:[26/26] experiments.lead.v4:@make vs F22 -> D hp_diff 0 r50 (14.86s)
v22 = v19 policy (walls first; finish-first except in the last two rounds; mandatory zero-leak defence against
the visible roster; speculative zero-leak against sampled affordable compositions within 0.6 x gold with poke
insurance and lethal_share 0.4; 2-tier1 round-1 poke; opportunistic attack by exact simulation on the opponent's
current map; factories capped at 40 per round) plus the fixes from the third astra review (finish window,
overflow guards, repaired adaptive option, corrected shortcut documentation). Options robust_attack (True /
"adaptive" / fraction) and big_threat remain available and documented; their measured trade-offs are in the
entries above (v20 and v21 configurations). Recommended spec: `bot_research.bots.defense.frozen.v22.fortress:@make`.
Its known exposure: a forecaster of the public policy (worst -840 at a tier5 round-10 wave, x25/x28 for the
identical v18/v19 policy) and the blind round 1 (5-12 HP to round-1 insurers/pokers).

## 2026-10-31T06:19Z  For the lead: the frozen best_v9a imports this lane's v7 planner; what v7 lacks

best_v9a (06:11Z) imports `bots/defense/frozen/v7/plan.py`. Relative to the current planner (frozen v22, same API)
v7 lacks: heavy-last purchase orders in the sampled compositions (astra's 400-gold tier3, tier2, tier4 order
leaked a tier4 against a plan that stopped all v7-style bundles), roster-wrap bundles (padding to entry 250 so a
heavy copy spawns at tick 0; v7 has none, and the v8-v17 version had an off-by-one fixed in v18), exhaustive
enumeration of all ordered purchase lists when the opponent's gold allows at most 400 of them (<= 195 gold),
the 3 s gun-pass time budget and the no-guns rule above 120 copies, the saturation-preserving leak shortcuts
(v19) and the foreign-map fallback (v15). Whether these matter for best_v9a depends on how its policy layer
uses plan_defense (it reports its own insurance rules); the exploits they close are documented above with
reproductions (astra fortress-review and v17-review answers in this lane's directory). If the lead wants them,
`bot_research.bots.defense.frozen.v22.plan` is a drop-in replacement for v7's module (plan_defense signature
extended only by keyword arguments with defaults).

## 2026-10-31T06:25Z  t37: frozen v22 under mirror:1:2 and eco:2 openings

`runs/defense/t37_v22_scen2` (26 tuning opponents, both seats): | bot_research.bots.defense.frozen.v22.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |
Frozen v22 totals on the development pools: tuning 104-0-0 (plain + asym:3:2, t36) and the row above (mirror + eco),
STRONG + lead v4 24-2-0 (x44), early-gun counter beaten +315 / +595 (x43).

## 2026-10-31T06:26Z  Run-directory index (all under bot_research/runs/defense/)

t1_fortress_vs_baselines (mixed, stopped), t2_fortress_v2_vs_baselines, t3_v3_vs_tuning, t4_v4_vs_tuning,
t5_layouts_vs_tuning, t6_poke_vs_tuning (stopped at 101), t7_a26_vs_tuning, t8_v8_vs_tuning, t9_v9_vs_tuning,
t10_v10_a25_vs_tuning, t11_v11_vs_tuning, t12_v11_turtles, t13_v11_scenarios, t14_v12_vs_tuning,
t15_v12_scenarios_tuning, t16_v13_vs_tuning, t17_v14_vs_tuning, t18_v15_vs_tuning, t19_v15_turtle, t20_v15_scen2,
t21_lethal04_tuning, t22_v17_vs_tuning, t23_v17_scen2, t24_v18_vs_tuning, t25_v19_vs_tuning, t26_robust_vs_tuning,
t27_robust_asym, t28_bt60_vs_tuning, t29_v20_vs_tuning (stopped), t30_adaptive_scen, t31_frac_scen,
t32_adaptive_noins_scen, t33_adaptive_noins_scen2, t34_v21_vs_tuning, t35_v21_scen2, t36_v22_vs_tuning, t37_v22_scen2;
x1_cross, x2_strong, x3_versions, x4_strong_annealed, x5_strong_a26, x6_strong_v8, x7_strong_v10, x8_vs_live_best,
x9_lethal, x10_finish, x11_strong_v11, x12_vs_lead_v4, x13_round1_vs_lead, x14_finish_first, x15_strong_v12,
x16_strong_v13, x17_finish2, x18_strong_v14, x19_foreign, x20_strong_v15, x21_lethal04_strong, x22_selfplay_v15,
x23_strong_v17, x24_variants_rr, x25_forecast_counter, x26_strong_v18, x27_options_vs_forecast, x28_v18_profile,
x29_strong_v19, x30_robust_strong, x31_robust_profile, x32_bt60_profile, x33_strong_v20 (stopped),
x34_adaptive_profile, x35_adaptive_strong, x36_frac_profile, x37_frac_strong, x38_adaptive_noins_profile,
x39_adaptive_noins_strong, x40_adaptive_noins_profile2, x41_strong_v21, x42_v21_exact_forecast, x43_earlygun,
x44_strong_v22, x45_best9a_earlygun. Other files: check_plan_*.txt, q1_build_order.txt, q2_cheapest*.txt,
template_*.txt/jsonl, layout_search_*.jsonl, path_length_search.txt, gun_value.txt, round1_insurance.txt,
sampling_gap.txt, order_search.txt, decide_time_audit.txt, smoke_*.jsonl, PRUNE_NOTE.txt. Each tournament
directory holds results.jsonl, summary.md and the kept replay logs (losses and one representative per pairing;
drawn 50-round logs pruned as noted).

## 2026-10-31T06:26Z  Decision-time audit, final for shift 1

`runs/defense/decide_time_audit.txt` (all tournaments in runs/defense): frozen v22 row (matches, max single
decide s, max per match s, rejected actions, bot errors): | v22 | 242 | 10.52 | 73.7 | 0 | 0 |
No rejected action and no bot error in any recorded match of any version.
Note on v22's maximum: the 10.5 s single decision (73.7 s per match) occurred against counters.pool:@turtle in t36 (a
50-round game in which both sides become very rich; next slowest 3.9 s against threat_defender): compositions of up to 400
copies above the splash exposure are still simulated (the no-simulation shortcut starts above 400), so a 300-tier5
bundle costs about 75000 entity-steps per simulation, repeated for every wall-prefix plan. Lowering
HUGE_COMPOSITION to 200 would bound this at the cost of a cruder estimate; left unchanged in the frozen artifact
and recorded as its runtime cost (no decision exceeded the engine's tolerance: there is no hard limit).

## 2026-10-31T06:32Z  t38: frozen v22 under two more asymmetric opening seeds

`runs/defense/t38_v22_asym_seeds` (26 tuning opponents x {asym:5:2, asym:7:3}, both seats): | bot_research.bots.defense.frozen.v22.fortress:@make | 104 | 101 | 2 | 1 | 0.981 |
Non-wins: both-destroyed draws against eco_then_flood (asym:5:2, seat B, -380 at round 9) and eco6_t5 (asym:5:2,
seat B, -410 at round 9), and one loss -44 at round 50 to splash_turtle under asym:7:3 (seat A). The draws are
the known pattern (a random opening that leaves fortress behind in factories, then the round-8/9 tier5 waves
arrive while its own swarm finishes the opponent). The splash_turtle loss is inherited from the opening: asym:7:3 scripts
both players' first three rounds, and the scripted purchases scored 10 + 27 + 32 = 69 HP against fortress's
seat while fortress's scripted tier1s scored 25 (731 : 775 at the end of round 3, before either policy acted);
from round 4 on neither side landed a hit (splash_turtle keeps adding splashes, fortress's pokes are stopped),
so the 44-HP deficit stood at round 50. Not a decision of the policy; a property of that scripted position.
Honest summary of v22 across openings: plain and asym:3:2 104-0-0, mirror:1:2 and eco:2 104-0-0, asym:5:2 and
asym:7:3 as above; the scripted asymmetric openings are where the remaining imperfections live.

## 2026-10-31T06:36Z  x46: a survive-the-kill rule does not remove the asym:5:2 draws (negative result)

Option tested (live fortress, survive_kill=True: if my existing roster alone kills the opponent this round, buy no
attack and spend everything on defence): `runs/defense/x46_survive_kill` (vs eco_then_flood(8), eco6_t5 and
eco_then_flood(11) under asym:5:2, asym:3:2 and plain, both seats): identical results to the default, including
the two both-destroyed draws (-380 and -410 at round 9, seat B under asym:5:2). The existing roster does not kill
the opponent on its own in those rounds; the kill comes from the finish purchase in a position where (by the
planner's search) no affordable defence survives the incoming wave, so the rule never fires. The draws are
structural for that scripted opening: fortress's seat starts behind in factories and the opponent's round-8/9
tier5 waves arrive before fortress's swarm has finished it. Default left unchanged (survive_kill=False); v22
remains the recommended artifact.

## 2026-10-31T06:37Z  Offline replay of the asym:5:2 draw: the lethal rule behaved as specified

Reconstructing fortress's observations from the kept log (round n observation = settled snapshots of round n-1)
and calling the live fortress on them: round 6 (opponent 630 gold): worst sampled threat 146 < 0.4 x 785, so 9 tier1
pokes + factories; round 7 (1097 gold): worst threat 240 < 314, 13 tier1 + factories; round 8 (1984 gold): worst
threat 468 >= 314, lethal mode, 6 splashes + 2 tier1 (the planner's best partial plan with 403 gold; a 3-tier5 wave
has 4500 HP, so neither splashes nor two gun3 stop it). The outputs match the log exactly: no bug; the position
was decided by rounds 3-7, when fortress's seat (handicapped by the scripted opening: 5 vs 12 factories after
round 3) kept poking for 100-165 damage per round while the opponent grew to 111 factories. A policy that
recognises a turret-less opponent out-growing it by a large factor and saturates early instead of poking would be
the fix; that is the lead's economic layer, not this lane's component. Recorded as a known failure case.

## 2026-10-31T06:40Z  x47/t39: a growth-gap insurance trigger is harmful (negative result)

Option tested (live fortress, growth_gap=3: from round 5 on, if a turret-less opponent owns >= 3 x my factories, spend
the full speculative budget with partial plans): `runs/defense/x47_growthgap_floods` and `t39_growthgap_tuning`:
it loses to eco_then_flood(8) and eco6_t5 even from the plain opening (-435 / -425 at round 9, where the default wins
+835 / +555 at round 7) and loses -530 to -1355 under the asymmetric openings (where the default draws or wins).
Mechanism, as for every early-insurance variant tested (spec_share 1.0, big_threat 60, lethal_share 0.2, adaptive
with big_threat): partial defence bought before the wave does not stop tier5 waves and costs the compounding that
the default converts into a kill by round 7-8. The consistent lesson on these pools: against a turret-less grower
either finish it before its waves (the default does, from equal openings) or saturate fully; partial insurance is
the worst choice. Default unchanged (growth_gap=None); frozen v22 remains the recommended artifact. x48
(growth_gap vs STRONG) left to finish for the record.
Summary rows for the growth-gap option (both seats):
    t39_growthgap_tuning: | bot_research.bots.defense.fortress:@make?growth_gap=3 | 104 | 94 | 0 | 10 | 0.904 |
    x48_growthgap_strong: | bot_research.bots.defense.fortress:@make?growth_gap=3 | 26 | 24 | 2 | 0 | 0.962 |

## 2026-10-31T06:43Z  State of the live package versus frozen v22 at the end of shift 1

`bots/defense/plan.py` is byte-identical to `frozen/v22/plan.py`. `bots/defense/fortress.py` differs from
`frozen/v22/fortress.py` only by the two additional options survive_kill (default False) and growth_gap (default
None), both tested and rejected above; with defaults the live bot reproduces the frozen v22 action lists on replayed
observations (6 of 6 rounds checked from a kept log). Recommended spec unchanged:
`bot_research.bots.defense.frozen.v22.fortress:@make`.

## 2026-10-31T06:48Z  x49: hrt-w3's guard candidates beat frozen v22 by 160 HP (counter-evidence); graded insurance under test

`runs/defense/x49_v22_vs_w3guard` (frozen v22 vs `counters.relevant_turret_guard:@make` and `counters.guard_continuation:@make`,
both seats): -160 at round 50 in all four matches. Mechanism (log kept): the guard insures round 1 with a gun1 (my
2-tier1 poke lands once, 5 HP), grows, and from round 7 buys ONE tier4 every second round (rounds 7, 9, 11); each
lands exactly once (60 HP) because the purchase round is hidden and fortress's speculative rule declined insurance:
the zero-leak plan against everything the guard could afford (including a tier5) exceeded 0.6 x gold, the lethal
trigger (one tier5 = 140 < 0.4 x HP) never fired, and the poke-insurance fallback covers tier1/tier2 bundles only.
Fortress's own pokes were stopped by the guard's splashes (25 by round 11). Net 3 x 60 - 20 = 160.
Fix under test: graded insurance fallback, option insure_levels=(560, 180, 70): when the full plan is unaffordable,
buy zero leaks against all affordable bundles of copies with HP <= 560 (a lone tier4 drip costs one gun3), else
<= 180, else <= 70. Runs: x50 (vs the two guards, eco_then_flood, eco6_t5, the early-gun counter), t40 (tuning
plain + asym:3:2), x51 (forecaster at 5 timings). Default unchanged until these are in.

## 2026-10-31T06:51Z  x50: graded insurance does not stop the tier4 drip (negative result)

`runs/defense/x50_graded_guards` (live fortress with insure_levels=(560, 180, 70), both seats): still -160 against both
guards (identical to v22); wins against eco_then_flood (+367, round 10), eco6_t5 (+250, round 10) and the early-gun
counter (+240) but with smaller margins and two rounds later than the default (+835 / +555 at round 7), and t40 (in
progress) already shows a -450 loss to eco_then_flood under asym:3:2 where the default wins. Why it cannot stop the
drip: the guard buys one tier4 (260 gold) while holding 595-667 gold; the fallback's bundles with HP <= 560 then
contain two tier4 copies, whose zero-leak plan (about 400 gold) exceeds 0.6 x fortress's 295-618 gold, and the
single-tier4 case is never on its own in the sampled set. Covering it would need either insuring against a lone
tier4 (one gun3, 200 gold) regardless of the share whenever the opponent can afford one, which the early-insurance
experiments (big_threat 60, growth_gap, lethal 0.2) showed to drain the economy against growth-then-flood
opponents, or a model of the opponent's behaviour over time (the drip is visible after its first copy: a tier4
appears on the roster at round 8, and fortress does stop that one from round 8 on, yet the next purchase is again
hidden). Recorded as the main open counter against v22 together with the forecaster. Default unchanged.
Summary rows for the graded-insurance option (both seats): 
    t40_graded_tuning: | bot_research.bots.defense.fortress:@make?insure_levels=[560,180,70] | 104 | 101 | 1 | 2 | 0.976 |
    x51_graded_profile: | bot_research.bots.defense.fortress:@make?insure_levels=[560,180,70] | 10 | 0 | 0 | 10 | 0.000 |
x51 forecaster profile of the graded option: tier3 r3 -14, tier4 r5 -48, tier4 r7 -120, then the tier5 timings as
listed in the run log (the option behaves like the default against the forecaster: the fallback never reaches the
tier5 compositions).

## 2026-10-31T06:54Z  Final addendum to the shift-1 summary: known counters to the recommended artifact

Recommended: `bot_research.bots.defense.frozen.v22.fortress:@make` (development pools: tuning 104-0-0 plain + asym:3:2,
104-0-0 mirror + eco, 101-2-1 asym:5:2 + asym:7:3 with the loss inherited from the scripted prefix; STRONG + lead v4
24-2-0; beats the early-gun grower that defeats response-aware variants). Known counters, each verified on the
unchanged engine in both seats: (1) a forecaster of the public policy (hrt-w3 public_factory timing): worst -840
at a tier5 round-10 wave, draws at two of ten timings (x25/x28 for the identical v18/v19 policy); (2) hrt-w3's guard
candidates (round-1 gun1, growth, one tier4 every second round from round 7): -160 (x49); (3) blind round-1 insurers
or pokers: -5 to -12 (astra, hrt-w3 known_policy, lead v4 draws 0-0 when both poke). Every policy variant tried
against these (lethal_share 0.2-0.6, big_threat 26-100, robust_attack full / fraction / adaptive, growth_gap,
survive_kill, graded insurance) removed one counter at the price of losses to growth-then-flood opponents or the
early-gun grower on the development pools; the documented trade-offs are in the entries above. Options remain
available in fortress.make() for the lead's policy layer. Complementary strengths, no dominant policy found.

## 2026-10-31T06:56Z  Cross-reference: hrt-w3's guard family against fortress22 (validation.md 06:54Z)

hrt-w3's cost-threshold table lists fortress22 at W 775:615 for its thresholds 30 and 60 (the -160 of x49) and
L 770:795 for threshold 120; fortress21 loses to all three. So the guard family's edge over v22 depends on how
cheaply it insures round 1 and how it times the tier4 drip; the lead (NOTES 06:55Z) reports no new request to this
lane and is screening its own revision against the same counters.

## 2026-10-31T07:19Z  Cross-reference: the lead's splash-only insurance (cycle 7) and this lane's primitives

The lead's cycle-7 finding (NOTES 07:17Z) that gun-based insurance plans do not carry over to the next round's larger
tier5 roster, and that the cheapest plan against four tier5 from the empty map costs 1529 with or without guns, matches
this lane's Q2 table (02:48Z: tier5 x4 and above -> 1529, the splash fortress) and the reserved-capacity reasoning
(03:17Z). The primitive the lead's splash_insurance uses is plan_defense(observation, budget, required_hp=1500,
allow_guns=False), which returns the splash-saturation plan on the master layout, and `defense_cost` gives its
price from any position; both exist unchanged in frozen v7 and v22 (v22 adds the exact leak shortcuts that keep
saturation in view against very rich opponents). No request to this lane in cycles 6-7.

## 2026-10-31T08:10Z  Shift 2 start: the lead's t6 games checked for a full-map lock-out (none)

The lead's 07:54Z status reports fortress v22 at S 1230 with 7 guns for rounds 11-29 while the opponent's gold piles up,
and asks whether a capacity-based mass attack (hrt-w2's Proposition F: a full map with S < 1500 cannot stop n tier5 when
n(1500 - S) > 250 x gun damage per tick) could break it. Checked on the lead's logs (`runs/lead/t6/logs`, games 00002,
00006, 00010; tools in this lane's directory, map_state.py and s_timeline.py, not published): in game 00006 (fortress
seat 0 against the lead's V2) fortress stays at S 70 with 71-291 gun damage per tick until round 12, jumps to S 1230
at round 13 when the opponent's gold reaches 3992 (6 tier5), and to S 1510 at round 30 when it reaches 124029 (190
tier5; the capacity bound would allow 269, the exact simulation finds the leak earlier), each time with legal empty
cells left (5-7 at round 50, S 1620-1680 if all were splashes). So the speculative step saturates just in time against
the opponent's visible gold, which is the exact bound on its hidden spend this round, and the map is never locked
below immunity. Risk remains only where the planner's sampled compositions miss a leaking order (documented limit).

## 2026-10-31T08:17Z  History insurance (v23): the tier4 drip is reduced from -160 to -40; tuning pool unchanged

Hypothesis: the guard drip (x49, -160) lands because each hidden tier4 is one copy more than the visible-roster plan
was sized for; an insurance against "the visible roster plus one more round of what the opponent has already shown
it spends" should stop every copy after the first, without touching the economy against opponents that never attack.
Implementation (live `bots/defense/fortress.py`, frozen as `frozen/v23`, SHA256SUMS inside): option history_insurance
(default True from v23; history_factor 1.0, history_share 1.0). Each round the bot sums the costs of the opponent's
roster entries by bought_round (public observation fields) and keeps the maximum per-round attack spend seen so far in
its own per-match state; when the full speculative plan was not bought (unaffordable at spec_share, or only the poke
fallback), it buys a zero-leak plan (never partial) against threat_compositions(obs, extra_gold = min(opponent gold,
history_factor x max spend)) with up to history_share of the remaining gold. The state is renewed per make() call
(one per side per match); the module-level decide stays stateless.
x52 (`runs/defense/x52_history_guards`, live fortress with history_insurance=true, factor 1.0 and 2.0, both seats):
    relevant_turret_guard -40 / -40 (v22: -160), guard_continuation -40 / -40 (v22: -160), eco_then_flood +820 r7
    (v22: +835 r7), eco6_t5 +540 r7 (v22: +555 r7), early-gun counter +315 r8 (v22: +315 r8); identical for both factors.
Trace (log 00001): the guard's tier4 of round 7 lands once (60; the first hidden purchase has no history); from round 8
fortress adds a gun3 (visible roster + one more 260-gold round), the guard's 3 tier3 of round 8, tier4 of rounds 9,
10, 11 and 3 tier4 of round 12 all die; the guard escalates when stopped and the history maximum follows (300, 780).
Net -40 = 60 - 20 (fortress's pokes of rounds 1-5 landed 25, minus the guard's round-1 tier1 hit of 5).
Decide time: 49 s per 50-round match, maximum call 6.5 s (v22: 13 s and 4.3 s) because the history plan runs the gun
pass whenever the spec plan is unaffordable; still far below the lead's slowest candidates (9.7 s), noted for hrt-w3's
match time-outs (120 s): a guard match now takes 60-100 s wall time on this box at load 130.
t41 (`runs/defense/t41_history_tuning`, 26 tuning opponents x {none, asym:3:2}, both seats): 104-0-0, unchanged.
Running: x53 (STRONG + lead v4), t42 (mirror:1:2 + eco:2), x54 (hrt-w3's stateful forecaster of frozen v23 at 10 timings).
Open: the first hidden copy (-60) is not covered by any history; covering it needs a prior (big_threat-type insurance,
which drained the economy against growth floods in t28), or an economic lead at round 7, which fortress does not have
against this guard (8 factories against 33 at round 6: the poke insurance against all affordable tier1/tier2 bundles
and five gun1 against two visible tier1 cost about 210 gold by round 6). Next test: poke_insurance=false with history
insurance (the history covers the shown pokes; the saving goes to factories).

## 2026-10-31T08:22Z  v23 withdrawn: the history rule must ignore cheap pokes (STRONG regression 24-0-4); v24

x53 (`runs/defense/x53_strong_v23`, frozen v23 vs 12 STRONG specs + lead v4, both seats): 24-0-4, losses -50 / -50
against the lead's frozen best_v2 (v22: +522 / +522) and -252 / -252 against lead v4 (v22: 0-0 draws). Trace (x53
logs 00008 and 00028 against x44 logs 00006 and 00026, per-round spending): the only difference in round 2 is that
v23 answers the opponent's round-1 poke history (30-40 gold) with a second gun1 instead of two factories. Against
lead v4 (same opening, same planner) that leaves 16 factories against 46 at round 6; v4's tier4 of round 7, three
tier3 of round 8 and tier5 of round 10 then land (60 + 52 + 140) because no insurance is affordable, where the
symmetric v22 game is a 0-0 draw. Against best_v2 the changed round-2 map changes best_v2's whole trajectory and the
tier4 drip of rounds 7-10 lands twice before the history gun3 arrives (v22 had bought the gun3 at round 7 as its
ordinary speculative plan, the opponent being poorer in that line).
Economic fact behind it (exact from the rules): a factory costs 20 and pays 15 in the purchase round and every later
round, so gold not invested in round r is worth about 1.75^k times as much by round r+k when reinvested; two
factories less in round 2 are roughly 30 factories less by round 6. Any non-factory purchase in rounds 1-8 has to buy
HP (landed or prevented) worth that compounding.
Decision: v23 withdrawn. v24 (frozen, `frozen/v24`): the history counts only rounds in which the opponent spent at
least history_min_spend = 100 gold (tier3 cost) on minions; cheap pokes stay with the poke-insurance fallback. In every
pool game without an observed heavy attack v24 therefore plays exactly as v22. Running (queue): x56 (guards and
growth floods), x57 (STRONG + lead v4), t43 (tuning plain + asym:3:2), t44 (mirror:1:2 + eco:2), x58 (stateful
forecaster of v24 at 10 timings; hrt-w3's stateful_public wrapper, since v24 keeps per-match state).

## 2026-10-31T08:36Z  Frozen v24 confirmed on the development pools; recommended artifact is now v24

Summary rows (both seats):
    x56_v24_guards: relevant_turret_guard -40 / -40, guard_continuation -40 / -40 (v22: -160 each), eco_then_flood +820
      r7, eco6_t5 +540 r7, early-gun counter +315 r8 (v22: +835 r7, +555 r7, +315 r8).
    x57_v24_strong: | bot_research.bots.defense.frozen.v24.fortress:@make | 28 | 26 | 2 | 0 | 0.964 |  (draws 0-0 lead v4, as v22)
    t43_v24_tuning: | bot_research.bots.defense.frozen.v24.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |  (plain + asym:3:2)
    t44_v24_scen2:  | bot_research.bots.defense.frozen.v24.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |  (mirror:1:2 + eco:2)
v24 = v22 policy + history insurance restricted to heavy attack rounds (history_min_spend 100). On every development
pool it equals v22's record and it reduces the guard drip from -160 to -40. Recommended spec:
`bot_research.bots.defense.frozen.v24.fortress:@make` (SHA256SUMS in frozen/v24). Known exposures carried over: the
forecaster (x58 running), the blind round 1, the first hidden heavy copy (-60), and the scripted-opening collapse
against econ17 reported by the lead at 08:10Z (addressed below).

## 2026-10-31T08:49Z  Answer to the lead's 08:10Z request: layout re-planner for foreign maps (bots/defense/replan.py)

Deliverable: `bot_research/bots/defense/replan.py` (live; will be in frozen/v25 and later), API
    replan_layout(buildings, *, n_slots=25, iters=4000, seed=0, time_budget=4.0) -> MasterLayout
    layout_for(observation, **kw) -> MasterLayout
    needs_replan(buildings, layout=LAYOUT, target_s=1500) -> bool
The result is a plan.MasterLayout usable as `layout=` in plan_walls / plan_defense / defense_cost. Its wall_order is
every new wall in greedy order of marginal route gain, stages = [all, all, all] (one stage: single walls rarely
lengthen a route, and the set costs one gold per wall), splash_cells = the n_slots new cells with the largest
adjacency to the final route (adjacency >= 2), final_adj over new and existing cells (so plan.is_foreign is False
and the planner keeps its route exclusions). Method, limits and the exact score are in the module docstring:
simulated annealing over new cells with the existing buildings fixed, moves = add/remove a 3-9 cell straight
segment, add a cell on or next to the current route, remove a cell; seeds = the four templates and their
transposes reduced to legal subsets; legality of every build order follows from "a subset of a set with a route
has a route". Deterministic for a given seed; 0.5-4 s per call on this box at load 130.
Evaluation (`experiments/defense/replan_eval.py`, table `runs/defense/replan_eval/report.md`, maps in maps.json;
openings generated with the harness itself, idle bots, both seats). S_final = 10 x adjacency sum of all slots on the
final route = the immunity reachable by splashes alone; "broken" = the default layout built as far as legal:
    map                 fixed  broken: route S_final   replan: route walls slots S_final  n(560)  secs
    mirror:1:2 (both)     14      40     840            62     14-17   25    1440     11    1.7-4.2
    asym:3:2 seat 0       24      38     540            68      4      25    1410     11    1.0
    asym:3:2 seat 1       38      32     390            44      9      25    1080     13    0.8
    mirror:22:3 (both)    50      38     240            40      0      25     850     15    0.5
    asym:23:2 seat 0      32      26     270            34      2      24     800     16    0.5
    asym:23:2 seat 1      43      26     150            36      0      25     900     12    0.8
    lead log seat 0 r3    31      40     850            54      3      25    1320     10    0.7
    lead log seat 0 r7    41      42     930            52      0      25    1540      4    1.0   (n(1500) = 24 splashes)
    lead log seat 0 r8+  56-68    32-46  790-1140       46-50   0-1    0-18  0-1310    -    -     (map full by round 10)
What fails: (1) S 1500 is not reachable on any of the eight scripted maps from the opening alone; the best is 1440
(mirror:1:2) with 25 slots, so immunity by splashes alone is impossible there and the defence must rest on guns
plus the capacity bound; with 3 scripted rounds (38-50 fixed cells) routes above 44 do not exist and S_final is
800-1080. (2) The re-plan must happen early: on the lead's log the reachable S falls from 1540 (round 7) to 0
(round 10) as the bot fills the map along the broken layout; re-plan at the first decision after the opening
(fortress does it at every round in which new foreign buildings appear, re-planning when more scripted cells
arrive in the next scripted round). (3) The annealer is a heuristic; 12000 steps instead of 4000 changed S_final
by -50 to +170 on four maps (asym:3:2 seat 1: 1010 -> 1250), so the 4 s budget is not the optimum but close.
Matches (`runs/defense/x62_replan_econ17` control, `x63_replan_econ17`; econ17 = `economy.frozen.v17.econ17:@make?
free_fallback="zero"&foreign_attack_from=11`, both seats): frozen v24 without re-planning loses all 8 (-780 to
-1098, rounds 11-14, as the lead reported for v22); live fortress with replan_foreign=true wins mirror:1:2 +1040 /
+1020 (rounds 16-17) and mirror:22:3 +850 / +850 (round 15), loses asym:3:2 -1080 (r13) / -3575 (r33) and
asym:23:2 -805 (r13) / -2358 (r33). The round-33 losses are a new regime (trace x63 log 00003, seat 0): fortress
reaches S 1200 + 409 gun dps on route 40 by round 13 and leads 790:725 until round 32; econ17 sits at S 610 + 906
dps, both maps full and below immunity, both hoard (131k vs 167k gold at round 31); fortress never attacks (its
attack is capped at 60 copies, which never leak) and never builds (zero-leak plans are impossible, the gun pass
is skipped above 120 copies, so the "best partial plan" is empty); econ17's hidden capacity flood of round 33 then
destroys the base. Exact simulation on econ17's round-31 map: 260 tier5 leak 8 copies, 300 leak 48, 400 leak 148
(0.01 s each), so fortress with 160k gold could have killed econ17 at round 33 itself, and 29 free cells filled
with gun3 would have raised its own capacity bound from about 340 to about 1700 tier5. Two rules follow and are
being implemented in fortress (options capacity_guns and mass_finish): when the own map cannot reach S 1500, spend
spare gold on gun3 at the free cells with the largest route coverage; and let the finish rule search the exact
simulation without the 60-copy cap for the cheapest flood that kills on the opponent's current map.
For the lead's bot: the two cheap imports are replan.needs_replan / replan.layout_for at the first decision after a
scripted opening, and the capacity regime applies to any bot whose attack is capped by a small copy count.

## 2026-10-31T09:01Z  Answer to the lead's 08:34Z priority request: plan_walls_foreign and the route numbers

API (live `bots/defense/replan.py`, same file as the 08:49Z answer; to be frozen in v25 within the hour):
    plan_walls_foreign(observation, budget, objective="route", n_slots=25, **kw) -> list[action]
        legal walls in a legal build order (every prefix of the order keeps a route: the full set has one and a
        subset of a set with a route has one) for the own map with buildings the bot did not choose; the layout
        behind it is memoised per map (layout_cached), objective "route" = 20 L + 0.5 S_final - 2 |cells|.
    layout_cached(buildings, objective=..., n_slots=...) -> MasterLayout   (the same layout, for plan_defense)
Measured on the four sc1 openings, both seats (`runs/defense/replan_eval/report.md`, columns "route (walls only)" =
route with the layout's walls built and its slots still open, "route (all)" = every wall and slot built):
    map                  fixed   broken default: walls-only/all   replan route objective: walls-only/all  S_final  n(560)
    mirror:1:2 (both)      14          24 / 40                          22 / 62                      1380    15
    asym:3:2 seat 0        24          28 / 38                          22 / 70                      1330    13
    asym:3:2 seat 1        38          28 / 32                          22 / 48                      1250    12
    mirror:22:3 (both)     50          34 / 38                          24 / 40                       790    18
    asym:23:2 seat 0       32          24 / 26                          22 / 62                      1280    16
    asym:23:2 seat 1       43          26 / 26                          22 / 48                      1000    13
    (exposure objective: 62 / 68 / 44 / 40 / 34 / 36 with S_final 1440 / 1410 / 1080 / 850 / 800 / 900)
The honest reading: the walls of these layouts do not lengthen the route by themselves (22-24, the spawn-to-base
diagonal); the route reaches 48-70 only when the reserved slots are filled, because on a serpentine every cell with
high splash adjacency is a barrier cell, so my split "best-adjacency cells = slots, rest = walls" leaves holes in
the barriers until the splashes are bought (the default layout has the same property on the empty map: 46 with
walls only, 78 full). A pure wall structure (n_slots=0, every chosen cell a wall) gives the full route immediately
for about 60 gold in walls, but then the splashes must go to off-structure cells next to the corridors, which on
a tight serpentine barely exist; its numbers will be appended when a core is free (the evaluation script has the
variant). For the lead bot I suggest: plan_walls_foreign(obs, budget) at the first decision after the opening,
then plan_defense(obs, gold, threat_types=..., layout=layout_cached(own buildings, objective="route")) so the
insurance fills the slots in adjacency order; each filled slot adds both exposure and route (income).
S reached with all gold over rounds 3-10: the greedy S(k) sequence of the re-planned layout (table column
"S(k) k=1..10") is 60, 110, 150, 210, 260, 330, 370, 410, 470, 540 for mirror:1:2 (S 840 with 14 splashes versus
500 reported for the lead's v16) and 50-60, 100, 150-170, 200-240, 240-310, 290-370, 320-410, 350-450, 380-490,
420-530 on the other maps; immunity (1500) is not reachable on any of them (best 1440). In matches (x63/x64, fortress
with the re-planner vs econ17): fortress reaches S 840 at round 11, 1140 at round 12 (asym:3:2 seat 1) and S 1200
by round 13 (seat 0), route 40.
What the matches then show (x64, live fortress = v24 + replan + capacity rules vs econ17, both seats): standard
-75 / -75 (same as frozen v24: econ17's tier4 drip escalates from one to two copies; history_factor=2.0 gives
-15 / -15, x65), mirror:1:2 +1300 / +1300 (r18), mirror:22:3 +990 / +990 (r15), asym:3:2 +1715 (r19) / -3320
(r33), asym:23:2 -805 (r15) / -818 (r33). The round-33 losses are the capacity race described at 08:49Z: at
round 32 econ17's map (S 1190, 450 dps) falls to 260 tier5 (169k gold) and fortress's (S 1140, 792 dps) to 289
(188k); econ17 had 188k and fortress 155k, so econ17 struck one round earlier. The decisive quantity in that
regime is gold at the moment the opponent's threshold becomes affordable; fortress now computes both thresholds
exactly each round (option capacity_guns) and buys gun capacity whenever the opponent's gold plus two rounds of
income reaches the threshold against its own map, and its finish rule searches floods beyond 60 copies by exact
simulation (mass_finish). Whether that wins the race against econ17 is being measured (x66).

## 2026-10-31T09:18Z  The capacity regime: three rules, their ablation, and frozen v25

Rules added to fortress (live, frozen as `frozen/v25`; all options documented in the fortress.py docstring):
- replan_foreign (08:49Z/09:01Z entries): layout re-planning on scripted maps, repeated while new foreign cells appear.
- mass_finish: the finish rule searches flood sizes beyond 60 copies on a geometric grid up to all the gold, exact
  simulation on the opponent's current map; a flood above 60 copies also has to kill after the opponent's estimated
  full-gold response (robust_leak). Cost: 0.01 s per simulation of 400 copies.
- capacity_guns: when every reserved slot filled would still leave S < 1500, compute the exact kill thresholds
  (smallest tier5 flood whose simulated damage reaches the HP) against my map and against the opponent's, and the
  rounds each side needs to afford them at its current income; if my threshold is >= capacity_min_flood copies and the
  opponent gets there first (within one round of me), buy the unbuilt slots as splashes and then gun3 on free
  off-route cells by coverage (up to 50 % of the gold, 12 turrets per round). Threshold chosen below.
Evidence (all both seats; econ17 = `economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11`):
- x64 (first version: trigger = opponent's gold + 2 rounds of income buys the threshold, coverage >= 4): vs econ17
  standard -75 / -75 (= v24), mirror:1:2 +1300 / +1300, mirror:22:3 +990 / +990, asym:3:2 +1715 / -3320 (r33),
  asym:23:2 -805 / -818 (r33). Diagnosis of the r33 loss (x64 log 00006, round 32): econ17's map falls to 260 tier5
  (169k), fortress's to 289 (188k); econ17 had 188k, fortress 155k; the gun fill had stopped at coverage 4 with seven
  usable cells left; fortress's turret spending of rounds 11-14 (3.9k) cost it about 55k gold of compounding by
  round 32 but raised econ17's needed flood by more than that. The race is decided by one round.
- x66 (race projection, coverage >= 1, history_factor 2.0): vs econ17 standard -15 / -15, mirror:1:2 +1300 / +1880,
  mirror:22:3 +1270 / +1270, asym:3:2 +3395 (r37) / +3400 (r45), asym:23:2 -1098 / -945; vs relevant_turret_guard
  standard -40 / -40, mirror:1:2 +869 / +869, mirror:22:3 +964 / +964, asym:3:2 +1930 / +3195, asym:23:2 -1998 / +1846.
- t46 (live with history_factor 2.0, tuning plain + asym:3:2; the module was edited during the run, so indicative):
  102-0-2, both losses eco6_t5 under asym:3:2 (-460, -305 at round 9). x68 ablation on that pairing: v24 W/W,
  replan_foreign=false W/L, capacity_guns=false W/W, mass_finish=false L/L, live L/L: the race trigger fired from
  round 3 (the opponent's 6-copy flood threshold is "affordable first" by the linear projection) and bought guns and
  splashes with half the gold while eco6_t5 grew (16 against 59 factories at round 7).
- x69 (capacity_min_flood 30): eco6_t5 fixed (+365, +375, +405, +299) but econ17 asym:3:2 seat 1 lost again (-1360,
  r15: the round-11-15 waves land when no early guns exist). x70: capacity_min_flood 8 and 12 both keep eco6_t5
  (4 wins) and econ17 asym:3:2 (+2280 / +3395); asym:23:2 stays lost (-1098 / -945, the own map allows S 800).
Decision: capacity_min_flood 8, history_factor 2.0 (x65: econ17 standard -15 instead of -75; equal elsewhere so far),
frozen as v25. Definitive regression running on frozen v25 (queue: x72 guards/floods, x73 econ17 x 5 starts, t47
tuning plain + asym, x71 STRONG, t48 mirror + eco, x74 forecaster 5 timings). Known failure kept: asym:23:2 seat 0
(43 scripted cells, route <= 36, S <= 900): lost to econ17 and to the guard; conjecture: unwinnable against a
competent opponent from that start, since the opponent's map (32 cells) allows S 1280.
Economic fact used above (exact): a factory returns 15 per round from the purchase round, 75 % per round; gold spent
in round r instead of factories is worth about 1.75^k gold k rounds later while factories still compound (the
40-per-round cap binds from about round 9), so early turret purchases must buy HP worth that.

## 2026-10-31T09:20Z  Reply to hrt-w3's 08:56Z review of replan.py (both points accepted)

1. Wording: the 08:49Z and 09:01Z entries say "S 1500 is not reachable", "routes above 44 do not exist", "immunity
   by splashes alone is impossible" and "not the optimum but close". Those are not established: the annealer gives
   constructive lower bounds only. Read them as "the search did not find a layout with S >= 1500 / a route above 44
   on these maps"; the "mathematically unavoidable" reading of the gun-capacity rule is withdrawn, it is the best
   continuation found. The module docstring now states this.
2. Determinism: the default time_budget of 4 s made the returned layout depend on the machine load (the loop stops
   at the clock). Fixed in the live module: replan_layout runs exactly `iters` steps by default (time_budget=None;
   3000 steps, 1500 per objective, 1-4 s here) and is reproducible from the seed; checked by two consecutive calls
   on the mirror:1:2 seat-0 map (identical wall_order and splash_cells). Frozen v25 still has the clock cutoff (its
   layouts are reproducible only when 4000 steps finish within 4 s); the next freeze (v26) carries the fix.
Also new in live replan.py: objective "best" (default) runs both objectives and keeps the larger S_final; on the
asym:23:2 seat-0 map this gives route 62 / S 1230 where the exposure objective alone found 34 / 800.

## 2026-10-31T09:24Z  Frozen v25 against the counters and econ17 (x72, x73); v26 frozen for the foreign-map fixes

x72 (`runs/defense/x72_v25_counters`, both seats): relevant_turret_guard -40 / -40, guard_continuation -40 / -40,
eco_then_flood +820 / +820 (r7), eco6_t5 +540 / +540 (r7), early-gun counter +315 / +315 (r8): identical to v24.
x73 (`runs/defense/x73_v25_econ17`, econ17 = `economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11`,
both seats): standard -15 / -15 (v24: -75 / -75), mirror:1:2 +1300 / +1300 (r18), mirror:22:3 +1410 / +1410 (r16),
asym:3:2 +3395 (r37) / +2280 (r35), asym:23:2 -1098 (r13) / -945 (r33). v24 lost all eight scripted games (x62).
Pending for v25: t47 (tuning plain + asym:3:2), x71 (STRONG), t48 (mirror + eco), x74 (forecaster, 5 timings).
v26 = v25 + the replan.py changes of 09:20Z-09:27Z (objective "best", fixed 5000 steps, no clock cutoff, reproducible
from the seed; docstring claims corrected). It differs from v25 only on maps that trigger the re-planner. Queued after
the v25 regression: x75 (v26 vs econ17, eco6_t5 and the guard under the four scripted openings) and t49 (tuning pool
under asym:3:2 and asym:5:2).

## 2026-10-31T09:31Z  t47: frozen v25 on the tuning pool, plain and asym:3:2

    t47_v25_tuning: | bot_research.bots.defense.frozen.v25.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |
(26 opponents x {none, asym:3:2}, both seats; no bot errors.) x71 (STRONG), t48 (mirror + eco), x74 (forecaster) follow.

## 2026-10-31T09:38Z  x71: frozen v25 on the STRONG pool

    x71_v25_strong: | bot_research.bots.defense.frozen.v25.fortress:@make | 28 | 26 | 2 | 0 | 0.964 |  (draws 0-0 lead v4, as v22/v24)
Cost: the two lead-v4 games took 125 s each (v24: 32-50 s). Cause: the uncapped finish search simulates floods of up
to all the gold (several hundred thousand gold late in a 50-round game, i.e. floods of 800 copies, five tiers, ten
sizes) every round although the opponent's map is immune. Fix in the live module (for v27): tiers whose HP is at most
the opponent's full-route splash exposure are skipped (exact: such a copy never arrives), which removes the search in
every mutual-immunity endgame.

## 2026-10-31T09:39Z  Correction: STRONG-pool rows x57 and x71 are 24-2-0 over 26 matches

The opponent list file used for x53, x57 and x71 (this lane's scratch copy of the STRONG pool) began with a count
line "12", which the harness took as a spec; the two resulting rows are harness errors ("No module named '12'"),
not matches. The 28-match rows above therefore read: x57 (v24) 24-2-0 over 26, x71 (v25) 24-2-0 over 26, x53 (v23)
22-0-4 over 26, each with two 0-0 draws against lead v4; these equal v22's x44 (24-2-0 over 26). The list is fixed.
Decide time of v25 per 50-round match on this box (load about 130): x71 largest total 107 s against lead v4 (largest
single call 8.1 s); v24 in x57: 28 s and 4.0 s. The immunity shortcut of 09:38Z (live, for v27) removes the cause.

## 2026-10-31T09:41Z  For the lead (09:33Z request): frozen v26 spec and hashes; what it has and lacks

Spec: `bot_research.bots.defense.frozen.v26.fortress:@make` (no parameters needed; the defaults are the recommended
setting). SHA-256 (bots/defense/frozen/v26/SHA256SUMS): fortress.py 411fa2c918bb0b8a4bc45e9deb5d2b6310b52befaaa1c61e3a8d5a782808cb04,
replan.py 8fc8cf4e6dd4e2e9910580e65ad7fe5db1dca3a63ce9579382fc299c0c570b1a, plan.py 765d1518c13a0268c5ddfceec0d9662d5186804e5cafd4f925a1d630e0923c74
(plan.py, geometry.py, simulate.py, templates.py unchanged since v22). For a foreign_policy switch the entry is the
same make(); the re-planner alone is `bot_research.bots.defense.frozen.v26.replan` (layout_for, layout_cached,
plan_walls_foreign, needs_replan), iteration-only (5000 steps, no clock cutoff, reproducible from the seed).
v26 = v25 + the deterministic best-of-both re-planner; it differs from v25 only on maps that trigger re-planning,
so v25's standard-start results carry over: tuning 104-0-0 plain + asym:3:2 (t47), 104-0-0 mirror:1:2 + eco:2
(t48), STRONG 24-2-0 over 26 (x71), guards -40 (x72), econ17 standard -15 / -15 (x73). On scripted openings v25
scored 6-0-4 against econ17 (x73: mirror:1:2 +1300 / +1300, mirror:22:3 +1410 / +1410, asym:3:2 +3395 / +2280,
asym:23:2 -1098 / -945); v26 under the same four openings against econ17, eco6_t5 and the guard is running (x75),
then econ15 leak (`economy.frozen.v15.econ15:@make?free_fallback="leak"`) under the standard start and the four
openings (x76). v26 lacks two live fixes that go into v27 (not frozen yet): the immunity shortcut in the uncapped
finish search (v25/v26 spend up to 107 s of decide time per 50-round game against a rich immune opponent, largest
call 8.1 s; the shortcut skips tiers whose HP is at most the opponent's exposure) and a walls-only route term in the
re-planner's score (the lead's 08:34Z point: the current layouts lengthen the route only when slots are bought as
splashes; the term is being compared offline, replan_cmp). I will post v27's spec and hashes when both are measured.

## 2026-10-31T09:47Z  t48 and x74: frozen v25 under mirror/eco openings and against the stateful forecaster

    t48_v25_scen2: | bot_research.bots.defense.frozen.v25.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |  (mirror:1:2 + eco:2)
x74 (`runs/defense/x74_v25_forecast`, hrt-w3's stateful_public forecaster of frozen v25, all gold, both seats): tier3 r3
-14 / -14, tier4 r5 -48 / -48, tier4 r7 -120 / -120, tier5 r8 -508 / -508, tier5 r10 -840 / -840 (base destroyed in round
10). Identical to v22/v24 (x58): none of the shift-2 rules touches a one-shot forecast wave; the exposure stands.
Frozen v25 therefore equals v22/v24 on every standard-start pool and differs only where heavy drips, scripted maps or
capacity races occur. Forecaster matches cost 105-126 s each here (two fortress policies per game).

## 2026-10-31T09:50Z  Addendum to the 09:01Z answer: pure-wall layouts give the long route at once

`plan_walls_foreign(observation, budget, n_slots=0)` (live replan.py; frozen v26 has the same function with the
objective/n_slots keywords) returns a structure made of walls only. Re-run of `experiments/defense/replan_eval.py`
with the live re-planner (best-of-both objectives, 5000 steps, walls-only route term), table `runs/defense/replan_eval/
report.md`, column "route (walls only)" = route once the returned walls are built, before any splash:
    map                 fixed   25-slot layout: walls-only / full route, S_final    pure walls: route, walls, cost
    mirror:1:2 (both)     14         22 / 66, 1500 (immunity reachable, 25 splashes)      60, 31 walls, 31 gold
    asym:3:2 seat 0       24         22 / 68, 1370                                       68, 25 walls, 25 gold
    asym:3:2 seat 1       38         22 / 48, 1250                                       46, 24 walls, 24 gold
    mirror:22:3 (both)    50         34 / 42,  850                                       42,  4 walls,  4 gold
    asym:23:2 seat 0      32         24 / 46, 1070                                       64, 21 walls, 21 gold
    asym:23:2 seat 1      43         22 / 48, 1000                                       48,  8 walls,  8 gold
    lead log r3 (31 fixed)           26 / 58, 1410                                       54, 20 walls, 20 gold
    lead log r7 (41 fixed)           26 / 56, 1560                                       58, 17 walls, 17 gold
So the route the lead asked for exists on every map (42-68 for 4-31 gold, legal build order, every prefix keeps a
route), but a pure-wall structure leaves no high-adjacency cells for splashes on a tight serpentine (its S then comes
from off-structure cells next to the corridors, which the planner finds in foreign mode); the 25-slot layouts reach
the long route only as the slots are bought (60 gold each) and in exchange reach S 1000-1500. Which is better depends
on the opponent: against econ17 the slot layouts won 6 of 10 (x73) through the capacity race, where exposure matters
more than early income. A combined layout (long pure-wall route plus slots at the corridor sides) was not searched.
The walls-only route term in the score (weight 4) did not move the 25-slot layouts' walls-only route (22-34 before
and after); weights 0/4/8 are being compared offline (replan_cmp) and the term will be dropped if 8 does no better.

## 2026-10-31T09:58Z  x75 and x76: frozen v26 on the four scripted openings (econ17, eco6_t5, the guard, econ15 leak)

`runs/defense/x75_v26_foreign` and `x76_v26_econ15leak`, both seats, fortress first in the HP difference; the engine
scores a round in which both bases fall as a draw (D with a non-zero HP difference below = mutual destruction):
    opening       econ17                     eco6_t5            relevant_turret_guard      econ15 leak
    standard      (x73 v25: -15 / -15)       -                  (x72: -40 / -40)            -15 / -15
    mirror:1:2    +1460 / +1460 (r17)        +505 / +505 (r8)   +2039 / +2039 (r36)         +2039 / +2039 (r36)
    asym:3:2      +1580 (r36) / -1920 (r33)  +393 / +365 (r8)   +2262 (r36) / -1985 (r37)   +2262 (r36) / -1985 (r37)
    mirror:22:3   +855 / +855 (r17)          +545 / +545 (r9)   (not run)                   +995 / +995 (r15)
    asym:23:2     -818 (r14) / +1155 (r21)   D +105 (r9) / +259 (r8)  (not run)             D +1450 / D -1716 (r35)
Reading: v26 wins every mirror opening against all four opponents, wins asym:23:2 seat 1 (first win on that start; v25
lost both seats) and loses the asym:3:2 seat-1 race to all three strong opponents (-1920 to -1985 at rounds 33-37),
where its own map (38 scripted cells, S 1130-1250 reachable) is the weaker one and the strike comes one round late
(trace x75 log 00004: fortress buys 12 gun3 at round 17 and then nothing while 13k-164k gold piles up above the
40-factory cap; econ17 reaches its 289-copy threshold at round 33 with 188k while fortress holds 164k against a
260-copy threshold). The asym:23:2 draws at round 35 are simultaneous floods (both bases destroyed in one round).
Change under test (live, x77/x78): gold that the factory cap cannot absorb is spent on gun capacity (12 turrets per
round) as soon as the opponent can afford a flood of capacity_min_flood copies, independent of the race projection.

## 2026-10-31T09:59Z  x77: the surplus rule fires earlier but cannot flip the asym:3:2 seat-1 race (structural)

x77 (`runs/defense/x77_surplus_econ17`, live fortress = v26 + surplus rule + finish-search immunity shortcut, vs econ17,
both seats): standard -15 / -15, mirror:1:2 +2440 / +2440 (r17), mirror:22:3 +1415 / +1415 (r17), asym:3:2 +2980 (r37)
/ -1920 (r33), asym:23:2 -818 (r14) / (seat 1 not in this run). Debug on the lost seat-1 game (observations rebuilt from
the log at rounds 13, 15, 17, 20): the rule did fire at round 13 (12 gun3, 987 dps, four rounds earlier than v26's
danger projection), but the map has exactly 12 usable off-route cells (coverage >= 1, route preserved) and no unbuilt
slot, so from round 14 on nothing can raise the threshold: fortress's map falls to 281 tier5 (S 1210, 987 dps, route
44) and econ17's to 260; econ17's 1050 factories against 974 give it 188k at round 33 (= 289 copies, its exact need
after its own late guns) while fortress holds 164k against the 169k it needs. The remaining 6 free cells are out of
range of the route. Conjecture: from the asym:3:2 seat-1 start (38 scripted cells) against econ17 the race cannot be
won by capacity purchases alone; it would need a better economy in rounds 3-12 or a layout with more gun cells near the
route (the re-planner optimises exposure and route, not gun cells).

## 2026-10-31T10:03Z  v27 frozen (candidate for the final recommendation); regression running

v27 = v26 + (a) the finish-search immunity shortcut (tiers whose HP is at most the opponent's full-route exposure are
skipped; exact, removes the 100 s decide totals of v25/v26 against rich immune opponents), (b) the surplus capacity
rule (x77: harmless where cells are exhausted, earlier guns otherwise), (c) WALL_ROUTE_WEIGHT 0 (the walls-only term
was measured and dropped). Hashes (frozen/v27/SHA256SUMS): fortress.py d5089c263bd4bcac..., replan.py 535db970b9ad3906...,
plan.py 765d1518c13a0268... (unchanged since v22). Queue: x80 (guards, floods, early-gun), t50 (tuning plain + asym:3:2),
x79 (STRONG), x81 (econ17 x 5 starts), then the response_memory option on frozen v27 (x60, x59, t45, x61).
x78 (live = v27 content, both seats): eco6_t5 +540 / +540 std, +393 / +365 asym:3:2, D +105 / +259 asym:23:2 (the
draw is a both-destroyed round 9); lead v4 0-0 / 0-0 std, +1060 / +1090 asym:3:2, +1080 / (seat 1 see log) asym:23:2.

## 2026-10-31T10:03Z  x80: frozen v27 against the counters; hrt-w3's guard files changed at 09:51Z

x80 (`runs/defense/x80_v27_counters`, both seats): eco_then_flood +820 / +820 (r7), eco6_t5 +540 / +540 (r7), early-gun
counter +315 / +315 (r8) (all as v24-v26); guard_continuation +20 / +20 at round 50 (v24/v25: -40 / -40). The guard
result is not attributable to v27: `bots/counters/guard_continuation.py` was modified at 09:51Z (hrt-w3's lane), and
`bots/counters/relevant_turret_guard.py` (06:13Z) now fails to construct ("GuardContinuation.__init__() got an
unexpected keyword argument 'continuation'"; x78 and x80 error rows, harness-recorded, not game results). For hrt-w3:
relevant_turret_guard:@make is broken by that change. A control (frozen v25 and v26 against the current
guard_continuation) is queued after the running regression (x82) to separate the two effects.

## 2026-10-31T10:07Z  t50: frozen v27 on the tuning pool, plain and asym:3:2

    t50_v27_tuning: | bot_research.bots.defense.frozen.v27.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |

## 2026-10-31T10:11Z  x79: frozen v27 on the STRONG pool; decide time back to normal

    x79_v27_strong: | bot_research.bots.defense.frozen.v27.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |  (draws 0-0 lead v4, as v22-v26)
Decide time per 50-round match (x79, both lead-v4 games included): largest total 23.6 s, largest single call 1.9 s
(v25 in x71: 107 s and 8.1 s; v24 in x57: 28 s and 4.0 s). The immunity shortcut in the finish search is the cause of
the improvement; the exact simulation of floods is only run against tiers the opponent's exposure does not already kill.

## 2026-10-31T10:13Z  RECOMMENDED ARTIFACT (end of the v27 regression): frozen v27

Spec: `bot_research.bots.defense.frozen.v27.fortress:@make` (defaults = recommended setting; the runner form
`bot_research.bots.defense.frozen.v27.fortress:decide` is the same policy without per-match state, so prefer @make).
SHA-256 (bots/defense/frozen/v27/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    d5089c263bd4bcacfd6b3bbe4382677b8d4b5944a49cad5c5230e58065ab13ca  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    765d1518c13a0268c5ddfceec0d9662d5186804e5cafd4f925a1d630e0923c74  plan.py
    535db970b9ad3906583468c505c41a6e2ec9587ab79553294ec22d0905ecd1a2  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Policy = v22 (walls first; finish-first except in the last two rounds; mandatory zero-leak defence against the visible
roster; speculative zero-leak against the sampled affordable compositions within 0.6 x gold with poke insurance and
lethal_share 0.4; 2-tier1 round-1 poke; opportunistic attack by exact simulation on the opponent's current map; 40
factories per round) plus, this shift: history insurance (heavy attack rounds only, factor 2.0), layout re-planning on
foreign maps (replan.py, deterministic best-of-both annealer, 5000 steps), capacity rules (exact kill thresholds, race
projection, surplus gold into gun capacity, minimum flood 8) and the uncapped finish by exact simulation with the
immunity shortcut.
Measurements (both seats; development pools, not held-out): tuning 104-0-0 plain + asym:3:2 (t50); STRONG 24-2-0 over 26,
draws 0-0 lead v4 (x79); eco_then_flood +820, eco6_t5 +540, early-gun counter +315 (x80); econ17 standard -15 / -15,
mirror:1:2 +2440 / +2440, mirror:22:3 +1415 / +1415, asym:3:2 +2980 / -1920, asym:23:2 +1155 / -818 (x81); mirror + eco
openings and the forecaster profile measured on v25 (t48 104-0-0, x74 worst -840 at tier5 r10), which v27 equals on
standard maps except for the finish-search shortcut (exact, no policy change). Decide time 24 s per 50-round match,
largest call 1.9 s (x79). Known failures (unchanged or structural): the exact forecaster of the public policy (-840),
blind round 1 (-5 to -15), econ17's escalating drip (-15), the capacity races from the weaker asymmetric maps
(asym:3:2 seat 1, asym:23:2 seat 0: -818 to -1920), and w3's guard family (-40 before its 09:51Z change; x82 pending).
For the lead's foreign_policy switch: the entry is the same make(); replan.layout_for / plan_walls_foreign are in
`bot_research.bots.defense.frozen.v27.replan` (sha256 535db970b9ad3906583468c505c41a6e2ec9587ab79553294ec22d0905ecd1a2).

## 2026-10-31T10:16Z  x59: the response memory neutralises the forecaster's tier5 waves (draws instead of -508 / -840)

Option response_memory (fortress.py, live and frozen v27; off by default): after each attack step the bot stores the damage
its roster plus purchase would deal on the opponent's current map; if the opponent's HP drop in that round was below half
of a positive prediction, the opponent answered the attack with same-round construction, and for the next 8 rounds the
attack uses the response-aware rule (robust_leak with the opponent's full gold), then the plain rule probes again.
x59 (`runs/defense/x59_rm_forecast`, frozen v27 with response_memory=true vs hrt-w3's stateful forecaster of the same
spec (model_parameters={"response_memory": true}), all gold, both seats): tier3 r3 -14 / -14 (unchanged), tier4 r7
-180 / -180 (v27 default: -120), tier5 r8 0-0 / 0-0 (default -508), tier5 r10 0-0 / 0-0 (default -840, base destroyed).
Mechanism (conjecture from the x25/x28 traces of the same exploit): the forecaster's wave is affordable because
fortress's pokes against it were answered and wasted; once the memory switches the attack off, fortress's economy keeps
pace and the lethal-share insurance can afford the zero-leak plan against the wave. The tier4 round-7 case got worse
by 60: one more hidden tier4 lands while the attack is switched off (less bounty, smaller HP lead). Pending for the
option: t45 (tuning plain + asym:3:2), x61 (STRONG), x60b (counters incl. the early-gun grower, which beat the earlier
adaptive rule), and the six remaining forecaster timings (x59b). If those hold, response_memory becomes the default (v28).

## 2026-10-31T10:18Z  Reproduction commands for the shift-2 results (run from the project root)

Common prefix: `PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B -m bot_research.harness.tournament --jobs 3 --out-dir bot_research/runs/defense/<name> --name <name>`
(the harness refuses an existing name; use a new one). The opponent lists: tuning = `$(cat bot_research/experiments/economy/opponents_tuning.txt)`
(26 specs, hrt-w2's file), STRONG = the 12 specs listed in notes 03:08Z plus `bot_research.experiments.lead.v4:@make`.
- t50 (tuning, plain + asym): `--candidates bot_research.bots.defense.frozen.v27.fortress:@make --opponents <tuning> --scenarios none asym:3:2`
- x79 (STRONG): `--candidates bot_research.bots.defense.frozen.v27.fortress:@make --opponents <STRONG>`
- x81 (econ17, five starts): `--candidates bot_research.bots.defense.frozen.v27.fortress:@make --opponents 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' --scenarios none mirror:1:2 asym:3:2 mirror:22:3 asym:23:2 --keep-logs all`
- x80 (counters): `--opponents bot_research.bots.counters.guard_continuation:@make bot_research.harness.baselines:@eco_then_flood 'bot_research.bots.counters.pool:@archetype?name="eco6_t5"' 'bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10'`
- x74-type forecaster profile: opponents `bot_research.bots.counters.stateful_public:@timing?model_spec=<spec>&tier=tier5&attack_round=10&attack_share=1.0` (hrt-w3's wrapper; add `&model_parameters={"response_memory": true}` when the candidate uses that option)
- re-planner evaluation: `.venv/bin/python -B -m bot_research.experiments.defense.replan_eval` (writes runs/defense/replan_eval/report.md and maps.json; needs runs/lead/dev/scen/V4f_vs_econ17_mirror-1-2_seat0.jsonl for the lead-log rows, skipped if absent)
- freezing: `bash bot_research/experiments/defense/freeze.sh vN` (copies bots/defense/*.py to frozen/vN with SHA256SUMS)
- smoke (runner form): `PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.defense.frozen.v27.fortress:decide --bot-b td_bots.protocol:idle --output bot_research/runs/defense/smoke_frozen_v27_vs_idle.jsonl` (to be run before the end of the shift)
The engine is deterministic: the variation across these runs is the opponent policy, the seat and the scripted opening (and, for v25/v26 re-plans, the machine load through the clock cutoff, removed in v27).

## 2026-10-31T10:22Z  t45: response_memory on the tuning pool, plain and asym:3:2

    t45_rm_tuning: | bot_research.bots.defense.frozen.v27.fortress:@make?response_memory=true | 104 | 104 | 0 | 0 | 1.000 |

## 2026-10-31T10:25Z  x61: response_memory on the STRONG pool

    x61_rm_strong: | bot_research.bots.defense.frozen.v27.fortress:@make?response_memory=true | 26 | 24 | 2 | 0 | 0.962 |  (draws 0-0 lead v4)
So far the option equals the default on both standard pools (t45 104-0-0, x61 24-2-0) and improves the forecaster
profile at the tier5 timings (x59). Pending: x60b (counters incl. the early-gun grower) and x59b (six more timings).

## 2026-10-31T10:28Z  x82: the guard_continuation control reproduces the old numbers for v22/v25/v26; v27's +20 is v27's

`runs/defense/x82_guardcont_control` (current `counters.guard_continuation:@make`, both seats): v22 -160 / -160, v25 -40 / -40,
v26 -40 / -40, as recorded before hrt-w3's 09:51Z edit of that file (x49, x56, x72), while frozen v27 scored +20 / +20 (x80).
Correction while writing: `bots/counters/guard_continuation.py` was modified again at 10:05:30Z, after x80's guard games
(about 10:00-10:03Z) and before x82 (10:25Z), so x80 and x82 used different guard versions and the +20 is not
attributable to v27 from these runs. v27 differs from v26 by the finish-search immunity shortcut (behaviour-neutral by
construction: a tier whose HP is at most the opponent's exposure never arrives), the surplus capacity rule (needs the own
map below immunity, never on a standard map) and WALL_ROUTE_WEIGHT 0 (re-planner only), so v27 should equal v26 here.
x83 (v26 and v27 against the current guard in one run, logs kept) is queued to settle it; until then the guard result
for v27 is "-40 expected, +20 observed against an earlier guard version".

## 2026-10-31T10:37Z  t51: frozen v27 under four more scripted openings against the tuning pool

    t51_v27_scen_more: | bot_research.bots.defense.frozen.v27.fortress:@make | 208 | 204 | 4 | 0 | 0.990 |
(26 tuning opponents x {asym:5:2, asym:7:3, mirror:22:3, asym:23:2}, both seats.) The four draws are both-destroyed
rounds (engine draw, HP difference non-zero): eco_then_flood asym:5:2 seat 1 (-380, r9), eco_then_flood asym:23:2 seat 0
(+105, r9), eco6_t5 asym:5:2 seat 1 (-180, r9), eco6_t5 asym:23:2 seat 0 (+105, r9): fortress's finish flood and the
opponent's tier5 flood land in the same round. The same pattern existed for v22 (t38, asym:5:2) and x46 showed that a
survive-the-kill rule does not convert them (the opponent's flood is not stoppable with the gold left). No losses.

## 2026-10-31T10:38Z  x60b: response_memory against the counters (standard start, both seats)

`runs/defense/x60b_rm_counters` (frozen v27 with response_memory=true): early-gun grower +315 / +315 (r8; the counter
that beat the adaptive rule of v21 is not a problem for the memory, since it never answers a poke), eco_then_flood
+820 / +820, eco6_t5 +540 / +540, econ frozen v2 +430 / +430, lead v4 0-0 / 0-0, guard_continuation -50 / -50 (v25/v26:
-40 against the current guard, x82), econ17 standard -50 / -50 (v27 default: -15 / -15). So the memory costs 35 HP against
econ17 and 10 against the guard (pokes switched off after the first answered one: fewer landed pokes and bounties while
the opponent's hidden heavy copies still land once each) and buys the forecaster's tier5 waves (x59). Decision after
x59b (six more timings): either v28 = v27 + response_memory default, or two documented configurations of v27.

## 2026-10-31T10:41Z  v28 frozen = v27 + response_memory default; forecaster profile so far; for the lead

Hashes (bots/defense/frozen/v28/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    0248f2b62b9f7edbdab336826654d9327d13978f4995eefc63eccdb66a2bc63f  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    765d1518c13a0268c5ddfceec0d9662d5186804e5cafd4f925a1d630e0923c74  plan.py
    535db970b9ad3906583468c505c41a6e2ec9587ab79553294ec22d0905ecd1a2  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Only fortress.py differs from v27 (the default of response_memory); replan.py and plan.py are identical to v27's.
Measured with the option on frozen v27 (same code path, deterministic, so these are v28's results): tuning 104-0-0 plain +
asym:3:2 (t45), STRONG 24-2-0 over 26 (x61), counters x60b (early-gun grower +315, eco floods +820 / +540, econ v2 +430,
lead v4 0-0, guard_continuation -50, econ17 standard -50), stateful forecaster of the same spec at ten timings (x59, x59b;
v27 default in brackets): tier3 r3 -14 (-14), tier3 r5 -26 (0), tier4 r5 -60 (-48), tier4 r7 -180 (-120), tier4 r9 0 (-420),
tier5 r7 -140 (-140), tier5 r8 0 (-508), tier5 r9 -280 (-560), tier5 r10 0 (-840), tier5 r11 0 (0). Worst case -280
instead of -840 (base destroyed); price: 35 HP against econ17's drip on the standard start and 10 against the guard.
For the lead's foreign-target choice (10:28Z note): v27 and v28 behave identically on scripted maps until a poke is
answered; x84 (v28 vs econ17, five starts) and x85 (eco6_t5, guard, econ15 leak under four starts) are running to
confirm. Both frozen versions stay available; recommendation: v28 if the opponent set may contain policy forecasters
or reactive pokers, v27 otherwise (the difference on the development pools is within the econ17/guard margins above).

## 2026-10-31T10:43Z  x83 resolves the guard question: v27 = v26 = -40 against the current guard_continuation

`runs/defense/x83_guard_v26_v27` (one run, both seats): v26 -40 / -40, v27 -40 / -40. So the +20 of x80 came from the
guard version of 09:51Z-10:05Z, not from v27; the 10:28Z entry's "unexplained" is closed. Known counter for v27/v28:
guard_continuation -40 (v28: -50, x60b), from the first hidden tier4 (60) less the landed round-1 poke.

## 2026-10-31T10:45Z  x84: frozen v28 against econ17 on the five starts

`runs/defense/x84_v28_econ17` (both seats; v27 from x81 in brackets): standard -50 / -50 (-15 / -15), mirror:1:2 +900 /
+900 r15 (+2440 / +2440), mirror:22:3 +1400 / +1400 r16 (+1415 / +1415), asym:3:2 +1690 (r33) / +1840 (r34) (+2980 /
-1920), asym:23:2 -830 (r16) / -2640 (r33) (-818 / +1155). Six wins and four losses for both versions; the response
memory changes the early game (pokes stop after the first answered one) and with it the two knife-edge capacity races,
one in each direction. Against econ17 the two versions are therefore equivalent in count and differ only by the 35 HP
of the standard start; the forecaster profile (worst -280 against -840) remains the reason to prefer v28.

## 2026-10-31T10:49Z  x85 (v28 scripted checks) and the fourth astra review (astra/v28-review/answer.md in the lane directory)

x85 (`runs/defense/x85_v28_misc`, both seats): eco6_t5 7-1-0 (the draw is the asym:23:2 both-destroyed round 9);
guard_continuation standard -50 / -50, mirror:1:2 +865 / +865, asym:3:2 +1070 / -2700, asym:23:2 +2950 / -1560;
econ15 leak standard -50 / -50, mirror:1:2 +459 / +459, asym:3:2 +1350 / -2700, asym:23:2 -1110 / -1560 (v26 in x76:
6-2-2 against econ15 leak with -15 on the standard start). So the response memory costs 35 HP on the standard start
against every drip opponent (econ17, econ15 leak, the guard) and loses two more capacity races; it buys the forecaster
profile (-280 worst instead of -840). The two configurations are complementary; the default is set back to v27's
behaviour (response_memory False) in the next freeze, v28 stays frozen as the forecast-robust alternative.
Astra review of v28 (question and answer in the lane directory astra/v28-review/; claims to be checked by matches):
1. A fixed schedule beats v28 by 50 in both seats (gun1 at (3,1) + tier1 in rounds 1-2, factories, a serpentine of walls
   in round 5, gun3 and splashes from round 6, one tier4 in round 8, three tier3 in round 9, saturation to S 1550 by round
   11, nothing afterwards). Memory on 735:785, memory off 735:775: the memory itself costs 10 HP but leaves v28 with 56
   factories and 894 gold against 30 and 509 at round 8. The round-8 tier4 lands because the history is empty (the
   pokes of rounds 1-2 are below 100) and the round-9 history plan then buys two extra gun3 (400 gold, 20 factories)
   that the schedule never needed. Reproduced here as `bots/defense/counter_astra28.py`.
2. `_kill_threshold` never tests n = 1 (returns 2 where one copy kills) and its geometric probes skip n_max; a tier4
   screen ahead of ten tier5 kills a constructed map for 6760 gold where the pure-tier5 threshold says eleven (7150):
   the race projection is a heuristic, not a certificate (consistent with hrt-w3's 08:56Z point).
3. `replan.needs_replan` scores the best 25 of all layout cells as prospective splashes (including wall cells), and
   `plan.reserved_capacity` uses the layout's final-route adjacency although foreign buildings change the route: with a
   single foreign gun3 at (2,6) the default layout is declared fine (S 1550 claimed), the built layout reaches S 1280,
   and reserved_capacity reports 1800, which can keep the capacity branch from ever running.
4. The bot's own off-layout purchases (capacity guns, foreign-mode splashes) count as foreign cells and can trigger
   re-planning again mid-game; the module-level `decide` (`module:decide` form) creates a fresh closure per call, so
   state (history, memory, layout) exists only through `@make`; the finish branches bypass the memory; `covered_full`
   treats the partial-plan regime as covered; plan_defense's 3 s deadline makes decisions load-dependent (known since
   v9, noted again).
Fixes going into the live module (v29): kill threshold tests 1 and n_max and also the tier4-screen variant in the finish
search; own-built cells are tracked and excluded from the foreign-cell test; needs_replan scores the layout's own
slots; reserved_capacity measures adjacency on the route of the unbuilt layout plus the current map; covered_full needs
zero leaks; module-level decide keeps one make() per player, renewed in round 1. The 3 s deadline stays (documented).

## 2026-10-31T10:52Z  t52: frozen v28 under mirror:1:2 and eco:2 openings

    t52_v28_scen2: | bot_research.bots.defense.frozen.v28.fortress:@make | 104 | 100 | 4 | 0 | 0.981 |
The four draws are 0-0 games against the two pure turtles (splash_turtle under mirror:1:2, the pool turtle under eco:2,
both seats): after the first answered poke the memory switches the attack to the response-aware rule, which never finds
a leak against a rich turtle, so the turtle is no longer beaten (v25/v27: 104-0-0 in t48 with wins of +76-type margins).
Same mechanism as the robust configuration's two draws in t26. Added to the v28 cost list.

## 2026-10-31T10:54Z  x86: astra's fixed schedule reproduced (counter_astra28) against v27, v28, v29

`runs/defense/x86_astra_counter` (both seats): v27 -40 / -40, v28 -50 / -50, v29 -40 / -40, matching the review's
735:775 and 735:785. The loss is the first hidden tier4 of round 8 (60) less the net landed pokes; v29's fixes do not
touch it (they concern thresholds, foreign maps and bookkeeping). It belongs to the known class "first hidden heavy copy
against an opponent whose shown spend is below 100", together with the guard (-40). The schedule needs no observation of
fortress at all (fixed purchases), so it is a public-policy counter in the weakest sense: it works because the bot's
insurance thresholds are public; the cost of insuring every affordable tier4 from round 7 (one gun3) was measured in
shift 1 (big_threat 60: flood losses) and is not taken.

## 2026-10-31T10:56Z  x87: frozen v29 on the standard start against the usual checks

`runs/defense/x87_v29_std` (both seats): econ17 -15 / -15, lead v4 0-0 / 0-0, eco6_t5 +540 / +540 (r7), guard_continuation
-40 / -40, eco_then_flood +820 / +820 (r7), early-gun counter +315 / +315 (r8): identical to v27 (the review fixes change
nothing on these standard-start games, as intended; they act on foreign maps, capacity races and bookkeeping).

## 2026-10-31T10:57Z  t53: frozen v29 on the tuning pool, plain and asym:3:2

    t53_v29_tuning: | bot_research.bots.defense.frozen.v29.fortress:@make | 104 | 104 | 0 | 0 | 1.000 |  (111 s wall time with 3 jobs)

## 2026-10-31T10:59Z  x88: frozen v29 on the STRONG pool

    x88_v29_strong: | bot_research.bots.defense.frozen.v29.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |  (draws 0-0 lead v4; 67 s wall time)

## 2026-10-31T11:03Z  x89: frozen v29 on the scripted starts; a round-12 loss traced to a stale layout; v30

x89 (`runs/defense/x89_v29_econ`, both seats): econ17 mirror:1:2 +2440 / +2440, mirror:22:3 +855 / +855, asym:3:2 +1160
(r20) / -800 (r12), asym:23:2 -946 (r13) / -1365 (r33) (v27 in x81: 6-0-2 on these eight; v29 5-0-3); econ15 leak
mirror:1:2 D -561 / D -561 (both destroyed, r39), asym:3:2 +1230 / -865 (r16), mirror:22:3 +995 / +995, asym:23:2 +1984 /
D -1156 (r36): 4-3-1. Standard pools unchanged (t53 104-0-0, x88 24-2-0, x87).
Trace of the new asym:3:2 seat-1 loss (x89 log 00004 against x81 log 00004, identical spending through round 9): v27 re-
planned again at round 10 because the gun3/gun2 cells it had placed in round 9 counted as foreign cells (the behaviour
the review called a bug), got a layout with route 44 and S 1210 by round 12 and survived econ17's round-12 wave; v29, with
its own cells excluded, kept the round-3 layout whose slots the guns had consumed, reached only S 820 on route 30, found
no partial plan at round 12 and took 840. So re-planning on a changed own map is useful, not accidental. v30 (frozen) makes
it deliberate: every replan_every = 3 rounds after a re-plan, if the own map changed and the current layout can no longer
reach S 1500 (needs_replan), a re-plan with half the steps is adopted when its reachable exposure (reserved_capacity) is
at least 100 above the current layout's. Running: x90 (v30 vs econ17 and econ15 leak, four scripted starts).

## 2026-10-31T11:06Z  v30 broken (UnboundLocalError), withdrawn; v31 = the same rule, fixed

x90 (`runs/defense/x90_v30_econ`): frozen v30 lost all 16 scripted games in rounds 8-11 by doing nothing: the new periodic
re-plan branch read `rnd` before its assignment (UnboundLocalError from the first re-plan on, recorded by the harness as
a bot error in every later round). Same failure class as the 08:40Z integration bug: an exception in decide() silences
the bot for the rest of the match, and short matches (2-3 s) are the symptom. Fixed (obs["round"]), functional test on a
rebuilt 12-round observation sequence passes (actions in every round, re-plans at rounds 2-3 of 0.8 s), frozen as v31.
x91 (v31 vs econ17 and econ15 leak, four scripted starts) running; v30 stays in frozen/ as evidence, never to be used.

## 2026-10-31T11:08Z  x91: v31 (periodic re-plan) does not help; the final choice is between v27 and v29

x91 (`runs/defense/x91_v31_econ`, both seats): econ17 identical to v29 (mirror:1:2 +2440 / +2440, mirror:22:3 +855 / +855,
asym:3:2 +1160 / -800 r12, asym:23:2 -946 / -1365); econ15 leak mirror:1:2 -1121 / -1121 (r21; v29: both-destroyed draws),
asym:3:2 +1230 / -865, mirror:22:3 +995 / +995, asym:23:2 +1984 / D -1156. The periodic check (rounds 6, 9, 12 after the
round-3 re-plan) did not produce a layout that was adopted in the round-12 loss, and the mirror:1:2 games got worse.
v31 is withdrawn (kept frozen as evidence); its regression queue was stopped. Remaining question for the recommendation:
v27 (empirically the best scripted record, 6-0-2 against econ17, but with the bookkeeping faults of the fourth review)
or v29 (the faults fixed, identical on every standard pool, 5-0-3 against econ17). Completing the comparison now: x95
(v27 against econ15 leak on the four scripted starts, which only v26/v28/v29 have) and x96 (v29 against eco6_t5 and the
guard on the four starts, which v26/v28 have).

## 2026-10-31T11:11Z  x95: v27 against econ15 leak; FINAL RECOMMENDATION: frozen v29 (v27 and v28 as documented alternatives)

x95 (`runs/defense/x95_v27_econ15leak`, both seats): standard -15 / -15, mirror:1:2 +2039 / +2039 (r36), mirror:22:3 +995 /
+995 (r15), asym:3:2 +3382 (r35) / -1985 (r37), asym:23:2 -1210 (r35) / D -1716 (both destroyed, r35).
Scripted-opening totals over the same 16 games against econ17 and econ15 leak: v27 11W-1D-4L (x81, x95), v29 9W-3D-4L
(x89); the standard-start pools are identical for the two (104-0-0, 24-2-0, counters, econ17 -15). The differences are the
knife-edge capacity races, which flip with layout details in either direction; equal losses. Decision: the final
recommended artifact is frozen v29 because it carries the fourth review's correctness fixes (kill threshold tests 1 and
n_max, screen variant in the finish search, own cells excluded from the foreign test, needs_replan on the layout slots,
reserved_capacity on the actual route, covered_full requires zero leaks, stateful module-level decide) at no measured
cost on any pool; v27 is the equal-strength predecessor without those fixes, v28 (= v27 + response_memory) the
forecast-robust alternative (worst -280 instead of -840 against the exact forecaster; -35 HP against every drip opponent,
0-0 against turtles, fewer scripted wins).
Spec: `bot_research.bots.defense.frozen.v29.fortress:@make` (runner form `...frozen.v29.fortress:decide`, stateful per
player since v29). SHA-256 (bots/defense/frozen/v29/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    a54c88fe6038fcdcfa4b0c2f3b901b2ff404a74a565ca0d7ac5574e67988da4f  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    b0e6e0cc43965fe3aa535d24394e6f61efbe9140ddc4f9564aef74880b7d14d9  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Evidence for v29 (both seats, development pools): t53 tuning 104-0-0 (plain + asym:3:2), x88 STRONG 24-2-0 over 26 (draws
0-0 lead v4), x87 standard checks (econ17 -15, eco6_t5 +540, eco_then_flood +820, early-gun +315, guard -40, lead v4 0-0),
x86 astra's schedule -40, x89 scripted econ17 5-0-3 and econ15 leak 4-3-1, mirror + eco openings and forecaster profile
inherited from v25/v27 (t48 104-0-0; x74 worst -840 at tier5 r10, the known exposure), x96 (eco6_t5 and the guard on the
four scripted starts) pending. Decide time about 24 s per 50-round match (x79 for v27, same code paths).
Known failures of v29 (all verified in matches): exact forecaster of the public policy (-840, base destroyed at round 10;
v28 reduces it to -280); blind round 1 (-5 to -15); the first hidden heavy copy against guards/drips (-40 against
guard_continuation and astra's schedule, -15 against econ17 and econ15 leak); the capacity races from the weaker
asymmetric scripted maps (asym:3:2 seat 1, asym:23:2: -800 to -1985); both-destroyed draws against growth floods on
asymmetric openings. Options for other trade-offs remain in make() and are documented in fortress.py.

## 2026-10-31T11:13Z  x96, end-of-shift-2 integrity check, smoke run of frozen v29

x96 (`runs/defense/x96_v29_misc`, frozen v29, both seats): eco6_t5 under mirror:1:2 / asym:3:2 / mirror:22:3 / asym:23:2:
+505 / +505, +370 / +365, +545 / +545, +435 / +259 (8-0-0; the v26/v28 both-destroyed draw on asym:23:2 is now a win);
guard_continuation: +1679 / +1679 (r21), +2350 / -865 (r16), +855 / +855 (r14), +2824 / D -1156 (r36): 6W-1D-1L.
Integrity (scratch/manifest_check_end_shift2.txt, project root as argument): 1041 manifest entries, 36 ok, 1002 missing
(1000 under data/games/, .DS_Store, td_view/.DS_Store), 3 changed (td_game/combat.py, tests/test_engine.py,
tests/test_rules.py); files outside bot_research/ and .venv/ not in the manifest: bot_research.prompt.md only; the full
list of files outside bot_research/ and .venv/ (40) is identical to the start of the run. No change relative to the
starting state recorded at 02:05Z.
Smoke (runner form, the prompt's command shape): `.venv/bin/python -B -m td_game.runner --balanced --bot-a
bot_research.bots.defense.frozen.v29.fortress:decide --bot-b td_bots.protocol:idle --output
bot_research/runs/defense/smoke_frozen_v29_vs_idle.jsonl` -> player 0 wins in round 8 (base destroyed, 800 : -275).

## 2026-10-31T11:13Z  Shift-2 summary for the report (supersedes the 05:28Z summary's recommendation; the facts there stand)

Deliverables added this shift (all under bot_research/, lane hrt-w1): `bots/defense/replan.py` (layout re-planner for maps
with foreign buildings: replan_layout, layout_for, layout_cached, needs_replan, plan_walls_foreign); fortress.py options
history_insurance / history_factor / history_min_spend, response_memory / response_rounds / response_ratio, replan_foreign /
replan_iters / replan_every, capacity_guns / capacity_share / capacity_min_flood, mass_finish, guard_insure (under test);
plan.reserved_capacity measured on the actual route; counter bots `counter_astra28.py` (astra's fixed schedule) next to
`counter_earlygun.py`; `experiments/defense/replan_eval.py` with `runs/defense/replan_eval/report.md`; frozen v23-v31 with
SHA256SUMS and a README table; runs x52-x96, t41-t54 in runs/defense/ (results.jsonl + summary.md each; logs kept for
losses, all logs for the scripted-opening runs).
Recommended artifact: frozen v29 (11:11Z entry: spec, hashes, evidence, known failures). Equal-strength predecessor v27;
forecast-robust alternative v28.
Proved (exact, from the bundled rules): (1) a factory returns 15 per round from its purchase round, so gold not invested in
round r is worth about 1.75^k times as much k rounds later while the 40-per-round cap does not bind (it binds from about
round 9-10 for a growing bot), which is why two factories less in round 2 became 30 factories less by round 6 (x53); (2) a
copy whose HP is at most the full-route splash exposure never arrives, so the finish search may skip such tiers
(v27's shortcut); (3) a subset of a cell set with a spawn-base route has a route, so every build order of a re-planned
layout is legal; (4) on a full map with exposure S < 1500 and gun damage G per tick, at most floor(250 G / (1500 - S))
tier5 copies can die in a round (hrt-w2's Proposition F, confirmed by hrt-w3), so a flood above that leaks; the exact
simulation finds leaks earlier (260 copies against a bound of 254 in x64's map, because frontmost-target guns overkill).
Empirical (unchanged engine, both seats, development pools; the engine is deterministic, variation = opponent policy, seat,
scripted opening): v29 tuning 104-0-0 (t53), STRONG 24-2-0 over 26 (x88), standard counters (x87), scripted openings
against econ17 5-0-3 / econ15 leak 4-3-1 / eco6_t5 8-0-0 / guard 6-1-1 (x89, x96); v27 equal on standard pools, scripted
econ17 6-0-2, econ15 leak 5-1-2; v28 forecaster worst -280 (x59/x59b) at the costs listed at 10:49Z; history insurance
reduces the guard drip from -160 to -40 (x56) while counting only heavy rounds (v23's regression x53); the re-planner
raises the reachable exposure on scripted maps from 150-840 to 850-1510 and turns 0-8 into 6-2 against econ17 (x62/x63/
x73); the capacity rules win the asym:3:2 race in both seats (x66/x70) at capacity_min_flood 8 (30 loses the round-15
waves, x69; no minimum drains the economy against eco6_t5, x68); the gun fill is cell-limited (12 usable cells, x77).
Conjectures (stated as such): the asym:3:2 seat-1 and asym:23:2 seat-0 starts are unwinnable against econ17-class
opponents by capacity purchases alone (weaker own map, richer opponent: x77 debug); the first hidden heavy copy of a
guard/drip opponent cannot be insured without losing to growth floods (shift-1 big_threat sweep; guard_insure, a
profile-targeted variant, is being measured in x97); the S values reached by the annealer are lower bounds only
(hrt-w3's 08:56Z review).
Failure cases (verified): forecaster of the public policy (-840 v29, -280 v28); blind round 1 (-5 to -15); first hidden
heavy copy (-40 guard and astra schedule, -15 econ17/econ15 leak); capacity races from the weaker scripted maps (-800 to
-1985); both-destroyed draws against growth floods on asymmetric openings; v23 (history counting pokes: -252 lead v4),
v30 (UnboundLocalError: silent bot), v31 (periodic re-plan: no gain) withdrawn with their evidence.
Review trail: hrt-w3's 08:56Z review (claims softened, determinism fixed in v26), astra's fourth review (10:42Z; schedule
reproduced x86; bugs fixed in v29; hrt-w3 independently verified the kill-threshold boundary at 11:10Z). Decide time of
v27-v29: about 24 s per 50-round match, largest call about 2 s (x79); forecaster matches 45-125 s (two policies).
Reproduction: 10:18Z entry. Integrity: 11:13Z entry (unchanged relative to the start).

## 2026-10-31T11:15Z  x97: profile-targeted guard insurance is a negative result

`runs/defense/x97_guardins_std` (live fortress = v29 + guard_insure=true, standard start, both seats): guard_continuation
-40 / -40 and astra's schedule -40 / -40 (unchanged: the plan against "visible roster + one tier4" was either unaffordable
within half the gold at rounds 6-7 or did not cover the actual purchase), econ17 -95 / -95 and econ15 leak -95 / -95 (v29:
-15; the insurance gun is bought every few rounds against an opponent that keeps turrets and holds gold, 80 HP of
economy lost), lead v4 0-0, eco6_t5 +540, eco_then_flood +820, early-gun +315, econ v2 +430. The option stays off; the
"first hidden heavy copy" class remains open (conjecture: not insurable without paying more elsewhere, now tested with
big_threat 26/60/100, graded insurance, growth_gap, history factors and a profile trigger).
Live bots/defense/fortress.py now equals frozen v29 behaviour plus the two switched-off options (replan_every, guard_insure).

## 2026-10-31T11:17Z  Run-directory index, shift 2 (all under bot_research/runs/defense/; results.jsonl + summary.md each)

x52_history_guards, t41_history_tuning (history insurance, any spend), x53_strong_v23 (v23 regression), x56_v24_guards,
x57_v24_strong, t43_v24_tuning, t44_v24_scen2, x58_v24_forecast (v24), x62_replan_econ17 (control, v24 vs econ17 scripted),
x63_replan_econ17 (first re-planner), x64_capacity_econ17, x65_std_econ17 (history factor), x66_live_econ17 (race trigger),
x68_eco6_asym_diag (capacity ablation), x69_capfix, x70_capmin (capacity_min_flood), x72_v25_counters, x73_v25_econ17,
t47_v25_tuning, x71_v25_strong, t48_v25_scen2, x74_v25_forecast (v25), x75_v26_foreign, x76_v26_econ15leak (v26),
x77_surplus_econ17, x78_surplus_misc (surplus rule), x80_v27_counters, t50_v27_tuning, x79_v27_strong, x81_v27_econ17,
t51_v27_scen_more (v27), x60b_rm_counters, x59_rm_forecast, x59b_rm_forecast, t45_rm_tuning, x61_rm_strong, x84_v28_econ17,
x85_v28_misc, t52_v28_scen2 (response memory / v28), x82_guardcont_control, x83_guard_v26_v27 (guard version question),
x86_astra_counter, x87_v29_std, t53_v29_tuning, x88_v29_strong, x89_v29_econ, x96_v29_misc (v29), x90_v30_econ (broken v30),
x91_v31_econ (v31), x95_v27_econ15leak, x97_guardins_std (negative), t55_v29_scen2 and x98_v29_forecast (final checks),
replan_eval/ (re-planner tables and maps), smoke_frozen_v29_vs_idle.jsonl. Launch logs for each run are in the lane
directory (scratch/<name>.log), not published.

## 2026-10-31T11:18Z  t55: frozen v29 under mirror:1:2 and eco:2 openings

    t55_v29_scen2: | bot_research.bots.defense.frozen.v29.fortress:@make | 104 | 102 | 2 | 0 | 0.990 |
The two draws are 0-0 against splash_turtle under mirror:1:2 (both seats; v25 won them in t48): with the deterministic
re-planned layout the early pokes that used to land on the turtle no longer do, and after its immunity nothing happens.
Not a loss; recorded as a difference to v25/v27 on that pairing.

## 2026-10-31T11:20Z  x98: the forecaster profile of frozen v29 itself (inherited claim checked)

`runs/defense/x98_v29_forecast` (hrt-w3's stateful forecaster of frozen v29, all gold, both seats): tier4 r7 -120 / -120,
tier5 r8 -508 / -508, tier5 r10 -840 / -840 (base destroyed in round 10): identical to v24/v25/v27 at these timings, as
expected (no shift-2 default rule acts on a one-shot wave; v28's memory does). Final check of the shift; all planned runs done.

## 2026-10-31T11:23Z  x99: a smaller attack share removes the forecaster's round-10 wave and flips econ17 (probe)

`runs/defense/x99_attackshare` (frozen v29 with attack_share 0.35 and 0.5; both seats; the forecaster model used
attack_share 0.35, so it is exact only for that candidate): attack_share 0.35: forecaster tier5 r10 0-0 / 0-0 (v29: -840),
econ17 standard +17 / +17 (v29: -15), guard_continuation -60 / -60 (v29: -40), lead v4 0-0, eco6_t5 +530 / +530 (r8; v29 +540
r7), eco_then_flood +395 / +395 (r8; v29 +820 r7), early-gun W. attack_share 0.5: forecaster(0.35 model) +313 / +313 (not an
exact forecast), econ17 -13 / -13, guard -50 / -50, eco6_t5 +285 / +285, eco_then_flood +425 / +425.
Reading: the forecaster's wave is affordable because fortress pours 70 percent of its spare gold into pokes that an
answering opponent stops (the mechanism conjectured at 10:16Z); with 35 percent the economy keeps pace and the lethal-
share insurance can afford the zero-leak plan at round 10, and against econ17 the saved gold outweighs the pokes it gave
up. The cost: fewer landed pokes against passive opponents (slower kills, -20 against the guard). v32 = v29 with
attack_share 0.35 as default is frozen for the full regression (forecaster at ten timings, tuning, STRONG, standard
checks, scripted openings).

## 2026-10-31T11:25Z  x102: frozen v32 (attack_share 0.35) on the standard-start checks

`runs/defense/x102_v32_std` (both seats; v29 in brackets): econ17 +17 / +17 (-15), econ15 leak +2117 / +2117 at round 36
(-15: with the economy kept, fortress wins the late capacity race on the standard map), eco_then_flood +395 / +395 r8
(+820 r7), eco6_t5 +530 / +530 r8 (+540 r7), early-gun counter W (see log; +315 before), econ frozen v2 +10 / +10 (+430),
lead v4 0-0 / 0-0 (0-0), guard_continuation -60 / -60 (-40), astra's schedule -60 / -60 (-40). Pokes land less against
passive opponents (smaller margins, one more hidden copy lands before the history gun arrives), the economy wins the
long games against the econ bots. Pools, forecaster profile and scripted openings follow (t56, x101, x100, x103, t57).

## 2026-10-31T11:27Z  t56: frozen v32 on the tuning pool, plain and asym:3:2

    t56_v32_tuning: | bot_research.bots.defense.frozen.v32.fortress:@make | 104 | 100 | 4 | 0 | 0.981 |  (v29: 104-0-0)
Draws: the pool turtle on the standard start 0-0 / 0-0 (v29 wins by about +76 through early pokes; with the smaller attack
share the pokes no longer land before the turtle's immunity), eco_then_flood and eco6_t5 under asym:3:2 seat 1 (both-
destroyed round 9, -305 and -165; v29 wins those). The early-gun grower is beaten by +15 instead of +315 (x102). So the
smaller attack share converts about four pool wins into draws and smaller margins against passive opponents, in exchange
for the forecaster's wave and the two econ wins on the standard start. Decision after x101 (STRONG), x100 (forecaster
profile), x103 (scripted), t57 (mirror + eco).

## 2026-10-31T11:29Z  x101: frozen v32 on the STRONG pool

    x101_v32_strong: | bot_research.bots.defense.frozen.v32.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |  (draws 0-0 lead v4; = v29)

## 2026-10-31T11:31Z  x100: forecaster profile of frozen v32 (ten timings, exact stateful forecaster of v32)

`runs/defense/x100_v32_forecast` (both seats; v29 in brackets): tier3 r3 -26 (-14), tier3 r5 -14 (0), tier4 r5 -60 (-48),
tier4 r7 -180 (-120), tier4 r9 0 (-420), tier5 r7 -140 (-140), tier5 r8 -140 (-508), tier5 r9 0 (-560), tier5 r10 0 (-840),
tier5 r11 0 (0). Worst case -180 (v29 -840, v28 -280): the attack-share change alone removes the base-destroying waves
without the response memory's costs against turtles and drips (v28 lost 35 HP against every drip opponent; v32 gains
against the econ bots and loses 20 against the guards).

## 2026-10-31T11:35Z  x103, t57; FINAL RECOMMENDATION REVISED: frozen v32 (v29 + attack_share 0.35)

x103 (`runs/defense/x103_v32_econ`, both seats): econ17 mirror:1:2 +1570 / +1570 (r16), mirror:22:3 +980 / +980 (r16),
asym:3:2 +3787 (r34) / +30 (r50), asym:23:2 D -270 (both destroyed, r34) / -3190 (r34): 6W-1D-1L (v29 5-0-3, v27 6-0-2);
econ15 leak mirror:1:2 +1684 / +1684 (r18), mirror:22:3 +1120 / +1120 (r15), asym:3:2 +1967 (r19) / +1630 (r36), asym:23:2
+2120 (r19) / -1850 (r34): 7W-0D-1L (v29 4-3-1, v27 5-1-2).
    t57_v32_scen2: | bot_research.bots.defense.frozen.v32.fortress:@make | 104 | 100 | 4 | 0 | 0.981 |  (0-0 vs splash_turtle mirror:1:2 and the pool turtle eco:2)
Smoke (runner form): frozen v32 vs idle wins in round 8 (800 : -120), `runs/defense/smoke_frozen_v32_vs_idle.jsonl`.
Comparison v32 against v29 (the 11:11Z recommendation), both seats, same conditions: tuning plain + asym 100-4-0 vs
104-0-0 (draws: pool turtle 0-0 twice, both-destroyed round 9 against eco_then_flood and eco6_t5 under asym:3:2 seat 1);
mirror + eco 100-4-0 vs 102-2-0 (turtle draws); STRONG 24-2-0 = 24-2-0; standard checks: econ17 +17 vs -15, econ15 leak
+2117 vs -15, guard -60 vs -40, astra's schedule -60 vs -40, early-gun grower +15 vs +315, econ v2 +10 vs +430, lead v4
0-0 = 0-0, eco floods won by both; exact forecaster at ten timings: worst -180 vs -840 (six timings better, three worse
by 12-60, one equal); scripted openings against econ17 and econ15 leak 13W-1D-2L vs 9W-3D-4L. The mechanism is one
parameter: pokes take 35 instead of 70 percent of the spare gold, so an opponent that answers pokes (every forecaster,
every econ bot) no longer drains fortress's economy, while passive opponents are killed later and with smaller margins.
Decision: frozen v32 is this lane's recommended artifact (strongest within the tested scope); v29 (attack_share 0.7) is
the alternative when the opponent set consists of passive growers and turtles only; v28 is superseded (v32 dominates it
on every measured axis except the guard: -60 against -50).
Spec: `bot_research.bots.defense.frozen.v32.fortress:@make` (runner form `...frozen.v32.fortress:decide`, stateful per
player). SHA-256 (bots/defense/frozen/v32/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    05a43922f91d16f2ae08c44baceb4fdba645792eff230d426468a45feac63d58  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    b0e6e0cc43965fe3aa535d24394e6f61efbe9140ddc4f9564aef74880b7d14d9  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Known failures of v32 (verified): guard_continuation and astra's schedule -60 (first hidden tier4 plus one more before the
history gun); forecaster single early copies (-14 to -180); blind round 1 (-5 to -15); asym:23:2 against econ17/econ15
leak from the weaker map (-1850 / -3190, one both-destroyed draw); 0-0 against pure turtles on scripted openings; the
capacity races remain knife-edge. Not measured for v32: eco6_t5 and the guard on the four scripted openings (x104 running).

## 2026-10-31T11:38Z  x104: frozen v32 against eco6_t5 and the guard on the four scripted openings

`runs/defense/x104_v32_misc` (both seats; v29 from x96 in brackets): eco6_t5 mirror:1:2 +415 / +415 r10 (+505 r8),
asym:3:2 +108 / D -165 r9-10 (+370 / +365), mirror:22:3 +328 / +328 (+545), asym:23:2 +240 / -280 r9 (+435 / +259):
6W-1D-1L against v29's 8-0-0; guard_continuation mirror:1:2 +1684 / +1684 (+1679), asym:3:2 +1967 / +1630 (+2350 / -865),
mirror:22:3 +840 / +840 (+855), asym:23:2 D -120 / -1850 (+2824 / D -1156): 6W-1D-1L against v29's 6W-1D-1L.
The new eco6_t5 loss (asym:23:2 seat 1, -280 at round 9) is the price of the smaller attack share on the weakest map:
fortress no longer kills the grower before its round-9 flood. Added to v32's known failures; the recommendation stands
(the standard-start pools, the forecaster and the econ opponents weigh more than one growth-flood game on the worst map).

## 2026-10-31T11:40Z  x106: the middle attack share (0.5) on the standard-start checks (trade-off curve)

`runs/defense/x106_as05_std` (frozen v29 with attack_share=0.5, both seats; 0.7 = v29 / 0.35 = v32 in brackets): econ17 -13
(-15 / +17), econ15 leak -13 (-15 / +2117), guard_continuation -50 (-40 / -60), astra's schedule -60 (-40 / -60), eco6_t5
+285 r8 (+540 r7 / +530 r8), early-gun W, econ v2 +290 (+430 / +10), pool turtle +12 (about +76 / 0-0). The middle point
keeps the turtle win and most of the econ-v2 margin but does not flip the econ17 / econ15 leak games. Forecaster profile
(x105, exact model) and scripted openings (x107) for 0.5 follow; the curve goes into the report as the measured trade-off
of one parameter.

## 2026-10-31T11:42Z  x105: forecaster profile at attack_share 0.5 (exact model)

`runs/defense/x105_as05_forecast` (both seats): tier3 r3 -21, tier4 r5 -60, tier4 r7 -180, tier4 r9 0, tier5 r8 -280, tier5
r9 -420, tier5 r10 0. Worst case -420, between 0.7 (-840, v29) and 0.35 (-180, v32): the exposure to the forecaster's
wave falls monotonically with the attack share, consistent with the economy mechanism (pokes answered = gold lost).

## 2026-10-31T11:44Z  x107 and the attack-share trade-off curve (0.7 = v29, 0.5 = option, 0.35 = v32)

x107 (`runs/defense/x107_as05_econ`, frozen v29 with attack_share=0.5, both seats): econ17 mirror:1:2 +2840 / +2840 (r32),
mirror:22:3 +1130 / +1130 (r15), asym:3:2 +1565 (r35) / +1425 (r35), asym:23:2 +940 (r26) / -3200 (r34): 7-0-1; econ15 leak
mirror:1:2 +3769 / +3769 (r36), mirror:22:3 +850 / +850 (r16), asym:3:2 +3800 (r34) / -320 (r18), asym:23:2 +3375 (r34) / D
-881 (r36): 6-1-1. Scripted total 13W-1D-2L, equal to v32 (13-1-2) and above v29 (9-3-4).
Measured curve (both seats; identical conditions; spec `bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=X`,
X = 0.35 being frozen v32's default):
    attack share                        0.7 (v29)      0.5           0.35 (v32)
    forecaster worst case (10 timings)  -840 (t5 r10)  -420 (t5 r9)  -180 (t4 r7)
    econ17 / econ15 leak, standard      -15 / -15      -13 / -13     +17 / +2117
    guard_continuation / astra          -40 / -40      -50 / -60     -60 / -60
    pool turtle / econ v2, standard     +76 / +430     +12 / +290    0 / +10
    eco6_t5 / eco_then_flood, standard  +540 / +820    +285 / -      +530 / +395
    scripted econ17 + econ15 leak       9W-3D-4L       13W-1D-2L     13W-1D-2L
    tuning plain+asym / STRONG          104-0-0 / 24-2-0   not run    100-4-0 / 24-2-0
Reading: a smaller share of the spare gold in pokes trades margins against passive opponents (turtles, growers, guards)
for the games against opponents that answer pokes (forecasters, econ bots, and the long capacity races on scripted maps,
where the saved gold decides). 0.35 keeps the best worst case and wins the two econ standard games; 0.5 is the middle
setting for an opponent set rich in passive growers. The 0.25 point (x108) is being measured to see whether the trend
continues or the kills against growth floods start to fail.

## 2026-10-31T11:47Z  x108: attack share 0.25 on the standard checks; v33 frozen for its regression

`runs/defense/x108_as025_std` (frozen v29 with attack_share=0.25, both seats; v32 = 0.35 in brackets): econ17 +17 (+17),
econ15 leak +1557 r37 (+2117 r36), guard_continuation -60 (-60), eco6_t5 +835 r9 (+530 r8), eco_then_flood +880 r10 (+395
r8), early-gun grower +130 r50 (+15), econ v2 +10 (+10), lead v4 0-0 (0-0), exact forecaster tier4 r7 -60 (-180), tier5 r8
0 (-140), tier5 r10 0 (0). So the trend continues: the smaller share loses nothing on these checks and improves the
forecaster's tier4 round-7 case and the margins against growth floods (later but larger kills, since the gold saved from
answered pokes compounds). v33 = v29 with attack_share 0.25 is frozen for the full regression (t58 tuning plain + asym,
x110 STRONG, x109 forecaster ten timings, x111 scripted econ17/econ15 leak, x112 scripted eco6/guard, t59 mirror + eco).
The limit attack_share -> 0 is the pure turtle, which shift 1 showed to lose to growth floods (t1); the finish rule
(all-gold kill by exact simulation) is what produces the flood wins at small shares.

## 2026-10-31T11:49Z  t58: frozen v33 (attack_share 0.25) on the tuning pool, plain and asym:3:2

    t58_v33_tuning: | bot_research.bots.defense.frozen.v33.fortress:@make | 104 | 102 | 2 | 0 | 0.990 |
Draws: the pool turtle 0-0 on the standard start (both seats, as v32); the two both-destroyed draws of v32 under asym:3:2
(eco_then_flood, eco6_t5) are wins again with the smaller share (the later, larger finish flood survives the opponent's).

## 2026-10-31T11:52Z  x110 and x111: frozen v33 on the STRONG pool and the scripted econ openings

    x110_v33_strong: | bot_research.bots.defense.frozen.v33.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |  (draws 0-0 lead v4)
x111 (`runs/defense/x111_v33_econ`, both seats): econ17 mirror:1:2 +1420 / +1420 (r31), mirror:22:3 +980 / +980 (r16),
asym:3:2 +2940 (r37) / +27 (r50), asym:23:2 +2105 (r32) / -3205 (r33): 7-0-1 (v32 6-1-1, v29 5-0-3); econ15 leak mirror:1:2
+829 / +829 (r15), mirror:22:3 +1120 / +1120 (r16), asym:3:2 +2660 (r35) / +1905 (r33), asym:23:2 D -420 (r35) / -1015 (r34):
6-1-1 (v32 7-0-1). Scripted total 13W-1D-2L, as v32; the asym:23:2 seat-0 race against econ17 is now won (+2105).

## 2026-10-31T11:54Z  x109: forecaster profile of frozen v33 (exact stateful forecaster, ten timings)

`runs/defense/x109_v33_forecast` (both seats; v32 / v29 in brackets): tier3 r3 -26 (-26 / -14), tier3 r5 -26 (-14 / 0), tier4
r5 -60 (-60 / -48), tier4 r7 -60 (-180 / -120), tier4 r9 0 (0 / -420), tier5 r7 -140 (-140 / -140), tier5 r8 0 (-140 / -508),
tier5 r9 0 (0 / -560), tier5 r10 0 (0 / -840), tier5 r11 (pending; 0 / 0). Worst case -140: one tier5 copy of a round-7
wave, where the insurance plan is unaffordable for every tested share; everything from round 8 on is held.

## 2026-10-31T11:56Z  x112; FINAL RECOMMENDATION (last revision of shift 2): frozen v33 = v29 + attack_share 0.25

x112 (`runs/defense/x112_v33_misc`, both seats): eco6_t5 standard +835 / +835 (r9), mirror:1:2 +485 / +485, asym:3:2 +450 /
+370, mirror:22:3 +290 / +290, asym:23:2 +253 / +295 (10-0-0; v32 had one loss there); guard_continuation standard -60 / -60,
mirror:1:2 +1809 / +1809, asym:3:2 +2660 / +2045, mirror:22:3 +1400 / +1400, asym:23:2 +1260 / -1015 (scripted 7-0-1);
astra's schedule standard -65 / -65 (v32 -60, v29 -40), scripted +745 / +745, +1094 / +810, +681 / +681, +745 / +1045 (8-0-0;
the schedule is fixed for the standard map). Forecaster tier5 r11 0-0 (x109 complete: worst -140).
Comparison v33 against v32 (both seats, same conditions): tuning plain + asym 102-2-0 vs 100-4-0; STRONG 24-2-0 = 24-2-0;
forecaster worst -140 vs -180 (tier4 r7 -60 vs -180, tier5 r8 0 vs -140, tier3 r5 -26 vs -14); econ17 standard +17 = +17,
econ15 leak +1557 vs +2117, guard -60 = -60, astra -65 vs -60, eco6_t5 +835 vs +530, eco_then_flood +880 vs +395, early-gun
grower +130 vs +15, econ v2 +10 = +10, lead v4 0-0 = 0-0; scripted econ17 + econ15 leak 13-1-2 = 13-1-2 (asym:23:2 seat 0
won against econ17), eco6_t5 10-0-0 vs 6-1-1 (over the five starts), guard 7-0-1 vs 6-1-1 (scripted); t59 (mirror + eco)
pending. Decision: frozen v33 is the recommended artifact of this lane (strongest within the tested scope); v32 (0.35)
and v29 (0.7) are the measured points of the same one-parameter family (curve at 11:44Z, extended by x108-x112); v28
(response memory) is superseded.
Spec: `bot_research.bots.defense.frozen.v33.fortress:@make` (runner form `...frozen.v33.fortress:decide`, stateful per
player). SHA-256 (bots/defense/frozen/v33/SHA256SUMS; only fortress.py differs from v32 and v29):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    440ffefc99a0fc3de8d3ed98879d1ca322424217a18872e775d0603e5ab5ba4a  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    b0e6e0cc43965fe3aa535d24394e6f61efbe9140ddc4f9564aef74880b7d14d9  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Policy (one paragraph for the report): walls of the master layout first (re-planned on scripted maps); finish-first by exact
simulation (uncapped, with the opponent's estimated response for floods above 60 copies) except in the last two rounds;
mandatory zero-leak defence against the visible roster; speculative zero-leak against the sampled affordable compositions
within 0.6 of the gold, poke insurance, lethal-share (0.4) full-budget partial plans; history insurance against the
visible roster plus one more round of twice the opponent's largest heavy spend; capacity rules below immunity (exact kill
thresholds, race projection, surplus gold into gun capacity); 2-tier1 round-1 poke; opportunistic attack by exact
simulation with 25 percent of the spare gold; 40 factories per round. Known failures (verified): forecaster single early
copies (-26 to -140); blind round 1 (-5 to -15); first hidden heavy copy of drip opponents (-60 guard, -65 astra's
schedule); the weaker asymmetric scripted map against econ17 / econ15 leak / the guard (asym:23:2 seat 1: -1015 to -3205,
one both-destroyed draw); 0-0 against pure turtles (standard and scripted). Decide time: as v29 (about 24 s per 50-round
match on this box, largest call about 2 s; smaller attacks make it slightly faster).

## 2026-10-31T11:58Z  t59 and the smoke run close the v33 regression; integrity re-checked

    t59_v33_scen2: | bot_research.bots.defense.frozen.v33.fortress:@make | 104 | 100 | 4 | 0 | 0.981 |  (0-0 vs splash_turtle mirror:1:2, pool turtle eco:2; no losses)
Smoke (runner form): frozen v33 vs idle, `runs/defense/smoke_frozen_v33_vs_idle.jsonl`: player 0 wins in round 8 by base
destruction (800 : -13). Integrity re-check at 11:58Z: manifest result identical to the start of the run
(36 ok, 1002 missing, 3 changed, bot_research.prompt.md the only extra root file); the file list outside bot_research/ and
.venv/ is unchanged. All runs of this shift are finished; nothing is running.

## 2026-10-31T12:00Z  x113: fortress v29 and v33 against the team's frozen best_v9b (for the lead)

`runs/defense/x113_vs_best9b` (opponent `bot_research.experiments.lead.frozen.best_v9b:decide`, both seats): standard start
v29 -5 / -5, v33 -5 / -5 (the round-1 exchange: best_v9b's three tier1 against fortress's two, nothing lands afterwards);
scripted openings (best_v9b switches to econ17 there, so these equal the econ17 rows of x89 / x111): v29 mirror:1:2 +2440 /
+2440, mirror:22:3 +855 / +855, asym:3:2 +1160 / -800, asym:23:2 -946 / -1365 (5-0-3); v33 mirror:1:2 +1420 / +1420,
mirror:22:3 +980 / +980, asym:3:2 +2940 / +27, asym:23:2 +2105 / -3205 (7-0-1). For the lead's foreign-target choice: v33
is the strongest fortress on these four openings; on the standard start the lane's bots lose the blind round 1 by 5 to a
three-tier1 opener (the known blind-round-1 exposure, lead's decision). A round1_poke=3 variant of v33 is being measured
against best_v9b and the standard checks (x114) to document that trade-off.

## 2026-10-31T12:03Z  x114: v33 with a three-tier1 round-1 poke (the blind round-1 question, for the lead)

`runs/defense/x114_v33_r1poke3` (frozen v33 with round1_poke=3, standard start, both seats; v33 default = 2 tier1 in
brackets): frozen best_v9b 0-0 (-5), guard_continuation 0-0 (-60), lead v4 +5 (0-0), econ v2 +15 (+10), eco6_t5 +120 r9
(+835 r9), econ17 -32 (+17), poke_lock +1310 r15 (win either way), pool turtle 0-0 (0-0). The third blind tier1 (15 gold)
removes the round-1 deficit against three-tier1 openers and, through the changed trajectory, the guard's drip hit, but
econ17 then lands more (-32) and the eco6_t5 margin shrinks. As in shift 1 (x13-x16), the blind round 1 is a choice
between opponent sets, not a dominant setting; v33 keeps 2 tier1 (the setting that beats econ17), and `@make?round1_poke=3`
is the documented alternative for pools with three-tier1 openers and guards.

## 2026-10-31T12:07Z  x115 and x116: the attack-share curve below 0.25, and v33 against early-locking growers

x115 (`runs/defense/x115_as015_std`, frozen v29 with attack_share=0.15, both seats; v33 = 0.25 in brackets): econ17 +10 (+17),
econ15 leak +10 (+1557), guard_continuation 0-0 (-60), eco6_t5 +520 r10 (+835 r9), eco_then_flood +580 r10 (+880 r10),
early-gun grower -5 (+130: the first loss to that counter at any share, its lock at round 10 now arrives before fortress's
pokes have earned the lead), econ v2 +10 (+10), lead v4 0-0 (0-0), exact forecaster tier4 r7 -96 (-60), tier5 r7 -140
(-140), tier5 r8 0 (0). So 0.15 is past the useful range: the forecaster's round-7 case and the passive growers get worse
while the guard draw is the only gain. The curve 0.7 / 0.5 / 0.35 / 0.25 / 0.15 has its best worst case and most wins at 0.25
(v33) on the development pools; this is an empirical choice on these opponents, not an optimum proof.
x116 (`runs/defense/x116_v33_growers`, frozen v33, both seats): early-gun grower with growth 5 / lock 8 +60 / +60 (r50),
growth 6 / lock 10 +130 / +130 (r50), growth 7 / lock 11 +595 / +595 (r10), growth 8 / lock 12 +915 / +915 (r10): all won;
the earlier the grower locks (saturates), the smaller fortress's lead, since fewer pokes land before immunity.

## 2026-10-31T12:27Z  Fifth astra review (astra/v33-review/answer.md in the lane directory): a stronger fixed counter and smaller defects

Claims (to be checked by matches, x117 running with the counter reproduced as `bots/defense/counter_astra33.py`):
1. A fixed schedule beats frozen v33 by 745 (700 : -45 at round 10, both seats) and the attack_share 0.7 policy by about
   600: gun1 at (10,1) + one tier1 + 2 factories in round 1, then 3, 5, 9, 15 factories in rounds 2-5, nothing in round 6,
   one tier5 in round 7 and one in round 8, gun2 (10,2) in round 9. Mechanism: the gun1 kills fortress's tier1 pokes, so no
   HP lead; 34 factories against 18 at round 7; the first tier5 (140) is below lethal_share x HP (318) and above the poke
   fallback (copies <= 70 HP), the history is empty, so nothing is insured; the visible tier5 then cannot be stopped with
   the gold at rounds 8-9 (partial plans), and 140 + 280 + 280 + 140 land. The weakness is the defence and growth before the
   first heavy copy, the same class as the guard drip but with tier5 (-745 instead of -60).
2. Passive growers that saturate from round 5-9 do not exploit the small attack share (fortress 800 against 735 to 340;
   a grower that starts construction at round 10 or later dies at round 9); replacing their factories by tier5 purchases
   after construction did not change the results.
3. Finish search: the screen variant was generated only above 60 copies, so "one tier4 then ten tier5" (6760 gold, lethal
   on a constructed map where eleven tier5 cost 7150) was missed (fixed in the live module: all sizes); robust_leak can
   accept a mass finish that one affordable gun3 would stop (the planner's gun pass is off above 120 entities; the proxy
   returns no construction): a false acceptance of the heuristic, not of a certificate; reserved_capacity falls back to
   stale final-route values when the full union has no route (needs_replan then correctly returns True).
4. State: reusing one make() closure across matches leaks history (the harness and the module-level decide create a
   fresh one per match / renew it in round 1, so no measured result is affected). No wall-clock dependence beyond
   plan_defense's 3 s deadline; the layout cache is deterministic.
5. Re-planner: six scripted walls that all lie on default-layout cells are excluded by the foreign-cell filter, so the
   needs_replan check (which would return True, 1380 against a re-planned 1570) is never made; fixed in the live module
   (foreign = on my map but never requested by me, regardless of layout membership); objective "best" compared the new
   slots' exposure without existing splashes (fixed: existing splashes counted).
The counter of item 1 is the main finding; the lethal-share threshold (0.4) and big_threat (None) are the levers, both
measured in shift 1 as economy drains against growth floods; with v33's smaller attack share the trade-off may differ:
x117 measures v33 with big_threat=100, and with big_threat=100 plus lethal_share=0.15, against the counter and the
standard checks (econ17, guard, eco6_t5, early-gun grower, lead v4).

## 2026-10-31T12:29Z  x117 (partial): astra's second counter reproduced; big_threat insurance makes it worse

`runs/defense/x117_astra33` (both seats): frozen v33 vs counter_astra33 -745 / -745 at round 10 (as claimed); v33 with
big_threat=100 -965 / -965 (the all-in partial plan against the first affordable tier5 at round 7 cannot stop it and
destroys the economy, so the later copies land harder). Rows for lethal_share=0.15 and the live module (screen fix) and
for the other opponents follow when the run completes.

## 2026-10-31T12:31Z  x117 (continued): the big-threat lever is rejected again; v34 frozen for a regression of the small fixes

Rows so far (both seats): v33 with big_threat=100 (with or without lethal_share=0.15): counter_astra33 -965, econ17 +17,
guard_continuation 0-0 (the only gain), eco6_t5 -535 at round 10 (v33 +835), early-gun grower lost (v33 +130), lead v4 0-0.
The all-in partial plan against the first affordable heavy copy drains the economy exactly as in shift 1 (t28), now also
against the counter it was meant to stop. The live module (v33 + the review-5 fixes) equals v33 on the rows finished so far
(-745 counter, +17 econ17). Conclusion for the report: the "cheap guard + growth + early single tier5" schedule is a verified
counter to the whole fortress family (-600 to -745), not fixable by the insurance thresholds tried (lethal_share 0.15-0.6,
big_threat 26-100, graded/guard/history insurance); the remaining lever would be an economy-matching rule in rounds 3-6
(stop pokes and speculative insurance while the opponent out-grows me and has shown no heavy copy), untested.
v34 = live (v33 + screen variant for all sizes, foreign filter by requested cells, best-of-both accounting) is frozen; its
regression (t60 tuning, x118 STRONG, x119 scripted econ, x120 standard counters) runs after x117. v33 stays the
recommendation unless v34 is equal or better on every pool.

## 2026-10-31T12:37Z  t60: frozen v34 (v33 + review-5 small fixes) on the tuning pool

    t60_v34_tuning: | bot_research.bots.defense.frozen.v34.fortress:@make | 104 | 102 | 2 | 0 | 0.990 |  (= v33: turtle draws only)

## 2026-10-31T12:39Z  x118: frozen v34 on the STRONG pool

    x118_v34_strong: | bot_research.bots.defense.frozen.v34.fortress:@make | 26 | 24 | 2 | 0 | 0.962 |  (= v33)

## 2026-10-31T12:41Z  x119: frozen v34 on the scripted econ openings

`runs/defense/x119_v34_econ` (both seats; v33 in brackets): econ17 mirror:1:2 +1420 / +1420 (same), mirror:22:3 +980 / +980
(same), asym:3:2 +840 (r37) / +27 (r50) (+2940 / +27), asym:23:2 +2105 / -3205 (same): 7-0-1; econ15 leak mirror:1:2 +829 /
+829, mirror:22:3 +1120 / +1120, asym:3:2 +3780 / +1905 (+2660 / +1905), asym:23:2 +1140 (r27) / -875 (r34) (D -420 / -1015):
7-0-1. Total 14W-0D-2L against v33's 13-1-2: the foreign-cell filter by requested cells changes the re-planning on two maps,
both for the better here. Pending: x120 (standard counters) for the v34 decision.

## 2026-10-31T12:43Z  x120; FINAL RECOMMENDATION (closing revision of shift 2): frozen v34

x120 (`runs/defense/x120_v34_std`, both seats): eco_then_flood +880 / +880 (r10), guard_continuation -60 / -60, eco6_t5
+835 / +835 (r9), astra's first schedule -65 / -65, astra's second schedule -745 / -745, early-gun grower +130 / +130,
econ v2 +10 / +10: identical to v33 (x108, x112, x117). Regression of v34 complete: tuning 102-2-0 (t60), STRONG 24-2-0 over
26 (x118), scripted econ17 7-0-1 and econ15 leak 7-0-1 (x119; v33 13-1-2), standard counters = v33 (x120), econ17 standard
+17 and lead v4 0-0 (x117 live rows = v34 code). v34 = v33 + the fifth review's small fixes (screen variant for all flood
sizes, foreign-cell filter = cells never requested by the bot, best-of-both re-plan accounting with existing splashes);
attack_share 0.25, response_memory off, eco_match off.
Spec: `bot_research.bots.defense.frozen.v34.fortress:@make` (runner form `...frozen.v34.fortress:decide`, stateful per
player, renewed in round 1). SHA-256 (bots/defense/frozen/v34/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    108a4e2e943031faa50ebb20dd2c892e53937f53a932f06d4cd57c5070d93747  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Inherited measurements (code paths unchanged on standard maps; checked where re-run): forecaster profile of v33 (x109,
worst -140 at tier5 r7), mirror + eco openings 100-4-0 (t59), the attack-share curve (11:44Z, 12:07Z), eco6_t5 10-0-0 and
guard 7-0-1 and astra-28 8-0-0 on the five starts (x112), against the team's frozen best_v9b -5 / -5 standard and 7-0-1
scripted (x113, as v33 on those maps up to the re-planning differences of x119).
Known failures of v34 (all verified on the engine, both seats): astra's second schedule (cheap guard, growth, single tier5
in rounds 7 and 8): -745, base destroyed in round 10, the strongest known counter to the whole fortress family (0.7 policy:
about -600), not fixable by the insurance thresholds tried; first hidden heavy copy of drip opponents (-60 guard, -65
astra-28); forecaster single early copies (-26 to -140); blind round 1 (-5 to -15 against three-tier1 openers; round1_poke=3
is the documented alternative, x114); the weaker asymmetric scripted map (asym:23:2 seat 1: -875 / -3205); 0-0 against pure
turtles. Alternatives on the same parameter family: v33 (identical policy without the small fixes), v32 (attack_share
0.35), v29 (0.7), v28 (response memory). Options documented in fortress.py: eco_match (probe x121), guard_insure (negative,
x97), replan_every (negative, x91), big_threat / lethal_share (negative, x117), robust_attack (shift 1).

## 2026-10-31T12:46Z  x121: the economy-matching option beats astra's second counter but loses the passive grower (option, not default)

`runs/defense/x121_ecomatch` (live module = v34 + eco_match=true, ratio 1.5 (EM15) and 1.3 (EM13), both seats; v34 in brackets):
counter_astra33 +638 / +638 r12 (EM13: +997 / +997) (-745), guard_continuation 0-0 (-60), eco6_t5 +800 r10 (EM13 +830) (+835 r9),
eco_then_flood +663 r9 (EM13 +530) (+880 r10), astra's first schedule -65 (-65), lead v4 0-0 (0-0), econ17 -81 (+17), early-gun
grower -215 (+130; a new loss: against a grower that locks at round 10 the matching rule stops the pokes that used to build
the lead, and the grower's lock then holds it). So the rule converts the worst known loss into a win and removes the guard
drip, at the price of econ17 and the early-locking grower; the sign pattern is the mirror image of attack_share's. No time
remains in this shift for a regression or a tuned trigger (the rule needs a condition that separates "answers my pokes
and grows" from "never answers and grows"); it stays a documented option in fortress.py (eco_match, eco_match_until,
eco_match_ratio) and the first item for the next shift. Default of v34 unchanged.

## 2026-10-31T12:47Z  Smoke run of frozen v34 and the closing integrity check of shift 2

Smoke (runner form): frozen v34 vs idle, `runs/defense/smoke_frozen_v34_vs_idle.jsonl`: player 0 wins in round 8 by base
destruction (800 : -13), as for v29/v32/v33. Integrity at 12:47Z: manifest result identical to the start (36 ok, 1002 missing,
3 changed, bot_research.prompt.md the only extra root file); the file list outside bot_research/ and .venv/ is unchanged.
Nothing is running; the lane's shift-2 work is complete (recommendation: frozen v34, 12:43Z).

## 2026-10-31T12:49Z  x122: the refined economy-matching condition never fires (negative); eco_match stays an option

`runs/defense/x122_ecomatch_stopped` (live module with eco_match="stopped": the rule only when the opponent's current map
stops a three-tier1 stream, both seats): every row equals v34 (counter_astra33 -745, guard -60, econ17 +17, eco6_t5 +835,
early-gun +130, lead v4 0-0, eco_then_flood +880, astra-28 -65). Against the astra-33 schedule the single gun1 at (10,1)
does not stop a three-copy stream in the exact simulation during rounds 2-6, so the refined condition is false and the rule
is off. The separating feature between "answers my pokes and grows" (astra-33, econ17: skip insurance hurts econ17) and
"never answers and grows" (the early-locking grower: skipping pokes hurts) is therefore not "my pokes die on its map";
left open. The plain eco_match (x121) remains the only setting that beats the astra-33 schedule, at the cost of econ17 and
the grower; v34's defaults are unchanged. End of the shift's experiments.

## 2026-10-31T12:52Z  x123: hrt-w3's staged-guard counter reproduced; the eco_match option beats both guard-growth counters

hrt-w3 (validation.md 12:46Z) reports a model-free standard-start counter that beats fortress33: `counters.staged_guard_maze:
@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&guard_rounds=[4,6]`
(two splash guards at rounds 4 and 6, growth through round 6, tier5 waves), -40 : 753 at round 9; and that no recorded
fortress33 decision exceeded 2.1 s (242 conditions). x123 (`runs/defense/x123_w3_staged_guard`, both seats): v34 -793 / -793
(r9), v33 -793 / -793, live module with eco_match=true +669 / +669 (r12). Together with x121 (eco_match beats astra's second
schedule +638 / +997 where v34 loses -745) the economy-matching rule answers the whole "cheap guard + growth + early
tier5" class, the two strongest known counters, at the measured cost of econ17 (-81 instead of +17) and the early-locking
grower (-215 instead of +130). Frozen as v35 (= v34 with eco_match=True) for a regression (t61 tuning, x124 STRONG, x125
scripted econ, x126 forecaster at three timings) to document it as the anti-guard-growth alternative; the live default
stays False (v34 behaviour) unless the regression is clean enough to prefer it.

## 2026-10-31T12:55Z  t61: frozen v35 (eco_match) on the tuning pool

    t61_v35_tuning: | bot_research.bots.defense.frozen.v35.fortress:@make | 104 | 102 | 2 | 0 | 0.990 |  (= v34: turtle draws only)

## 2026-10-31T12:57Z  x124: frozen v35 (eco_match) on the STRONG pool loses economy.timing

    x124_v35_strong: | bot_research.bots.defense.frozen.v35.fortress:@make | 26 | 22 | 2 | 2 | 0.885 |
Losses -47 / -47 against `economy.timing:@make` (v34: wins), draws 0-0 lead v4. Another answering econ-style opponent
whose drips land while the matching rule withholds the insurance in rounds <= 7. With econ17 -81 and the early-locking
grower -215 (x121) this settles it: v35 is the documented anti-guard-growth alternative (it is the only version that beats
astra's second schedule and hrt-w3's staged guards), not the default; v34 remains the recommendation.

## 2026-10-31T13:00Z  x125 and x126 complete the v35 picture; v34 confirmed as the final recommendation, v35 the alternative

x125 (`runs/defense/x125_v35_econ`, both seats; v34 in brackets): econ17 mirror:1:2 +1840 / +1840 (+1420), mirror:22:3 +1400 /
+1400 (+980), asym:3:2 +840 / +2267 (+840 / +27), asym:23:2 +2105 / D -685 (+2105 / -3205): 7-1-0; econ15 leak identical to v34
(7-0-1). Scripted total 14W-1D-1L (v34 14-0-2). x126 (exact forecaster of v35): tier4 r7 -190 / -190 (v34 -60), tier5 r8 0 / 0,
tier5 r10 0 / 0 (v34 0 / 0).
Final comparison v35 (eco_match) against v34: tuning 102-2-0 = 102-2-0; STRONG 22-2-2 against 24-2-0 (economy.timing -47);
standard counters: astra-33 +638 against -745, w3 staged guards +669 against -793, guard 0-0 against -60, econ17 -81 against
+17, early-locking grower -215 against +130, eco6_t5 +800 against +835, eco_then_flood +663 against +880, lead v4 0-0 = 0-0;
scripted econ 14-1-1 against 14-0-2; forecaster tier4 r7 -190 against -60. The two settings have complementary strengths:
v35 answers the "cheap guard + growth + early tier5" class (the two strongest known counters, -745 / -793 for v34) and loses
to answering econ bots and early-locking growers; v34 the reverse. Decision for the report: v34 is the recommended artifact
(more wins on the development pools: STRONG, econ17, timing, grower), v35 the documented alternative when the opponent set
may contain guard-growth schedules. Spec of v35: `bot_research.bots.defense.frozen.v35.fortress:@make` (= v34 with
eco_match=True; equivalently `frozen.v34.fortress:@make?eco_match=true`). SHA-256 of frozen v35's fortress.py:
    73a91a948dcba500898e2bad09fe8cb5d205186d7ca56ec26ed4fc54f08a668e
(all other files identical to v34). Live bots/defense/fortress.py = v34 behaviour with eco_match available.

## 2026-10-31T13:10Z  Cross-reference for the lead (13:09Z post): the passive-opponent rule and this lane's eco_match measurements

The lead's revision under test (P5 / R5: no rule-3 insurance through round 5 while the opponent looks passive) is the same
lever as this lane's eco_match option (x121, x123, v35 regression 12:52Z-13:00Z): it wins the guard-growth class (astra's
second schedule -745 -> +638, hrt-w3's staged guards -793 -> +669, guard_continuation -60 -> 0) and loses to opponents
that answer pokes and drip (econ17 +17 -> -81, economy.timing W -> -47) and to the early-locking grower (+130 -> -215),
with the forecaster's round-7 tier4 worse (-60 -> -190). Expect the same trade-off for P5/R5 unless the "passive" test
separates the grower that locks early from the one that strikes: in this lane's data the feature "my pokes die on its
current map" did not separate them (x122). x127 measures frozen v34 and v35 against the new frozen best_v9e on the standard
start and the four scripted openings for the lead's report.

## 2026-10-31T13:14Z  x127: frozen v34 and v35 against the team's new frozen best_v9e (foreign policy econ20)

`runs/defense/x127_v34_vs_best9e` (opponent `bot_research.experiments.lead.frozen.best_v9e:decide`, both seats; v34 / v35
rows identical unless stated): standard -5 / -5 (the round-1 exchange, as against best_v9b); mirror:1:2 +3530 / +3530 (r33);
asym:3:2 +2380 / +867 (v35: +2380 / +1567); mirror:22:3 -840 / -840 (r13); asym:23:2 -6575 (r22) / -2225 (r20) (v35: -6575 /
-3765). Totals over the ten games: v34 4W-0D-6L, v35 4W-0D-6L. best_v9e's foreign-map policy is hrt-w2's econ20 (econ with
this lane's re-planner), so on the two heavily obstructed openings (mirror:22:3 with 50 scripted cells, asym:23:2) the
opponent now re-plans as well, holds its economy and floods at rounds 13-22 while fortress's own map is capped at S 850-1260;
on the lighter openings fortress still wins by 870-3530. For the report: against the current team candidate the lane's bot
wins the standard-start exchange by -5 (blind round 1), wins mirror:1:2 and asym:3:2, loses mirror:22:3 and asym:23:2.
Trace of the mirror:22:3 loss (x127 log 00007, fortress seat 0): both sides hold S 120 on route 36 through round 10 with 2.1k
against 2.5k gold; best_v9e's econ20 builds gun damage (209 -> 591 per tick) and floods one, two, three tier5 in rounds 11-13
(140 + 280 + 420) while fortress's partial plan reaches its map's cap of S 870 only at round 11, one round after the flood
began; with S 870 against tier5 (1500 HP) and 93-225 gun damage per tick nothing is stopped. On this 50-cell scripted map the
defence cannot be made zero-leak, so the game is a kill race, and econ20's gun-heavy map (fortress's kill threshold against
it is far above 2k gold at round 11) wins it. Known failure, same class as the asym:23:2 races.

## 2026-10-31T13:19Z  For the lead (13:17Z request to hrt-w3): two ready-made "passive until round 5, then punish" specs in this lane

`bot_research.bots.defense.counter_astra33:@make` (gun1 (10,1) + one tier1 + 2 factories in round 1, factories only in rounds
2-5, nothing in round 6, one tier5 in round 7 and one in round 8, gun2 in round 9; fixed, no observation) and
`bot_research.bots.defense.counter_astra28:@make` (gun1 (3,1) + tier1 in round 1, walls and factories, one tier4 in round 8,
three tier3 in round 9, saturation by round 11) are exactly the profile asked for: no minion after round 1 until the strike,
one cheap turret. Against fortress v34 they score -745 and -65 (x120); the eco_match option (v35) beats the first (+638,
x121). Both are in bots/defense/ (also copied into frozen/v34 and v35) and need no parameters.

## 2026-10-31T14:08Z  x128: frozen v34 and v35 against hrt-w3's guard-handoff, staged-guard and screened-guard counters (shift 3 start)
(Heading time corrected at 14:38Z: first written as 14:40Z by estimate; the entry was written at about 14:08Z, after the x128 log of 14:02Z and before the x129 launch of 14:13Z. Content unchanged.)

`runs/defense/x128_v34_handoff` (standard start, both seats; every pairing gave the same result in both seats; logs kept).
Opponent specs as in hrt-w3's notes (13:53Z, 12:51Z, 13:26Z): guard_handoff with layout "empty", growth 6, no bait, tier5,
factory cap 2000, purchase cap 1000, replan_iters 5000 and handoff_round H; staged_guard_maze guards [4,6]; screened_guard_maze
upgrade_round 9.

| opponent | v34 | v35 (eco_match) |
| --- | --- | --- |
| handoff H10 | -653 (r50, 100:753) | -525 (r50, 240:765) |
| handoff H11 | -653 | -465 |
| handoff H12 | +213 (win r16) | +145 (r50) |
| handoff H13 | -77 (r50) | +615 (win r12) |
| handoff H14, H15, H16 | +113 (win r13) | +615 (win r12) |
| screened guard (upgrade r9) | +113 (win r13) | +615 (win r12) |
| staged guard [4,6] | -793 (r9) | +669 (win r12) |

Totals: v34 7W-0D-11L, v35 14W-0D-4L. For comparison the lead's P5TFU / P5TNU candidates (hrt-w3 13:53Z) lose H10-H13 / H10-H13
at -235 / -95 and win from H14-H15 / H14.
Mechanism (traces of x128 logs 00001, 00019, 00025 with scratch/s_timeline.py and spend.py): the opening is 5 factories in round
1 and all gold into factories through round 6 (86 factories, 1317 gold at the round-7 decision), splash guards at (10,1) in
round 4 and (1,0) in round 6 (S 50 / 80: every tier1 and tier2 poke dies, so fortress's pokes deal 35-47 HP in total), then two
tier5 per round from round 7 (1300 gold per round; roster 6 tier5 by round 9), and from round H the frozen-v34 defender, which
locks (S 1530) within two rounds of H. v34 keeps 48 factories at round 6 (its pokes, tier2s and speculative guns), spends
760 + 760 on guns in rounds 7-8 and 720 + 540 on splashes in rounds 9-10, takes 140 + 280 + 280 = 700 and never attacks again.
v35 matches the economy (83 factories at round 7), takes 280 + 280 (round 8: gun3 x5 + gun2 x3 + gun1 for 1270 kills two of
four; round 9: 21 splashes, S 1200, zero leak from then on) and holds 240 HP; in round 10 it buys one tier4 (the 25 percent
attack share) and 40 factories. Against H13 the opponent keeps buying two tier5 per round instead of locking and v35 kills it
in round 12 (tier4, five tier3, five tier5: 60 + 190 + 890). Against H10 and H11 the opponent locks in rounds 10-11 (v35 game:
gun3 x4 and walls in round 10, 22 splashes in round 11), so the round-10 tier4 is the only damage. Both fortress versions
therefore lose H10/H11 for the same reason as the lead's candidates: a striker that grows to 86 factories, strikes first with
two tier5 per round and then locks with a good planner cannot be out-grown, cannot be insured against (a zero-leak map
against two tier5 costs about 2400 gold, fortress holds 750-1300 in rounds 6-7) and leaves at most one round in which a
flood lands before its lock.
Two levers follow from the traces and are implemented as options in the live module for measurement (x129):
(1) race_kill: when my map is zero-leak against the visible roster and every affordable addition, the opponent has already
made a heavy purchase (a striker, history >= one tier5), and all my gold on tier5 now plus next round's income on tier5 would
kill it within two rounds on its current map (roster hits twice, the second wave once), buy the whole flood now instead of
the 25 percent share. In the v35 games this converts round 10 (2258 gold, three tier5, 420 damage) and round 11 (income 2556,
roster six tier5, 840) into a kill against H11 and H12 and a -105 instead of -525 against H10 if the opponent's lock lands
as in the trace; the cost is 1950 gold of factories in a game that is already locked on my side.
(2) eco_match_pokes: economy matching that skips only the speculative insurance and keeps the pokes (gated as before by the
exact leak per gold). Trace evidence: against the astra-33 guard the loss of v34 is the 310 gold of guns in rounds 2-6
(mandatory against its single visible tier1 plus speculative), 18 factories against 34 at round 6; against the early-gun
grower the pokes leak (the simulator gives 7-8 of 10 tier1 through any single gun1 on the 22-step default route, whether at
(3,1), (9,1) or (10,1); scratch/poke_leak.py) and deal 105 HP per round by round 7, which is the whole +130; against the
guards (S 50-80) no poke passes and the gate buys nothing. The leak fraction itself does not separate the astra guard from
the early-gun grower, so the earlier "stopped" trigger (x122) could not work.

## 2026-10-31T14:21Z  x129: the two options on the standard counter set (live module = v34 code plus options; both seats identical)
(Heading time corrected at 14:38Z: first written as 15:25Z by estimate; written at about 14:21Z, after the x129 log of 14:20Z. Content unchanged.)

`runs/defense/x129_options_std`, 112 games, 0 rejected actions, 0 bot errors. Columns: EMP = eco_match with pokes kept
(eco_match=true&eco_match_pokes=true), RK = race_kill alone, EMP&RK, EM&RK = eco_match (v35 behaviour) plus race_kill.
Reference values from x120/x121/x128: v34 / v35.

| opponent | v34 | v35 | EMP | RK | EMP&RK | EM&RK |
| --- | --- | --- | --- | --- | --- | --- |
| counter_astra33 | -745 | +638 | +537 | -745 | +537 | +562 |
| counter_astra28 | -65 | -65 | -53 | -65 | -53 | -65 |
| early-gun grower (growth 6, lock 10) | +130 | -215 | +130 | +130 | +130 | -215 |
| econ17 | +17 | -81 | -43 | +17 | -43 | -81 |
| eco6_t5 | +835 | +800 | +835 | +835 | +835 | +800 |
| guard_continuation | -60 | 0 | -60 | -60 | -60 | 0 |
| eco_then_flood | +880 | +663 | +880 | +880 | +880 | +663 |
| econ v2 | +10 | +10 | +10 | +10 | +10 | +10 |
| lead v4 | 0 | 0 | 0 | 0 | 0 | 0 |
| handoff H10 | -653 | -525 | -653 | -653 | -653 | -525 |
| handoff H11 | -653 | -465 | -653 | -653 | -653 | +35 (r50) |
| handoff H12 | +213 | +145 | +213 | +213 | +213 | +315 (win r11) |
| staged guard [4,6] | -793 | +669 | -793 | -793 | -793 | +315 (win r11) |
| screened guard r9 | +113 | +615 | +113 | +265 | +265 | +315 (win r11) |
| W-D-L over the 14 | 7-2-5 | 8-2-4 | 7-1-6 | 7-1-6 | 7-1-6 | 8-2-4 |

Findings.
- Keeping the pokes while matching (EMP) is a negative result: against the staged guard and the handoffs the pokes of rounds
  3-6 (tier1 and tier2 bought while the guards' S is 50-80; 220 gold in the v34 trace) cost the factories that v35 keeps, and
  the result is exactly v34's (-793, -653). The pokes pass the leak-per-gold gate (0.1 HP per gold) because a few copies of a
  group do leak before the second guard; the gate is far too permissive for this purpose, and the value of a poke is not its
  one-round leak but the economy it costs while a passive grower compounds at 75 percent per round (factory 20, income 15).
  EMP keeps the early-gun win (+130) and halves the econ17 loss (-43), which is the trade-off of the previous entry restated.
- race_kill alone (RK) changes only the screened guard (+113 to +265: the flood lands one round earlier); with v34's economy
  the race condition is never true in the lost games.
- EM&RK (v35 plus race_kill) is the best column: it turns H11 from -465 into +35 (the flood of round 10 lands before the
  round-11 lock), kills H12, the staged guard and the screened guard in round 11 (one round earlier than v35, smaller margin
  because the gold went into the flood instead of overkill), and is unchanged elsewhere, including the two v35 losses that
  motivated it: the early-gun grower (-215) and H10 (-525). Trace reasoning for those: at round 10 the condition "zero leak
  against every affordable addition" fails, because the striker's gold (1135 / 1593) affords two more tier5 that my S 1160-1200
  map leaks. The condition is replaced in the live module by the finish rule's safety test (zero leak against the visible roster
  and survival of the worst affordable addition this round); x130 re-measures EM&RK on the strikers. Expected from the traces:
  early-gun grower +205 (three tier5 in round 10 against its hidden round-10 lock of S 1100 < 1500 leak 420; it locks fully at
  round 11), H10 unchanged (240 HP against a possible 280 leak fails the survival test, correctly).

## 2026-10-31T14:27Z  x130, x131: the relaxed race condition changes nothing; v34 also takes the timing strike and wins it by pokes
(Heading time corrected at 14:38Z: first written as 15:50Z by estimate; written at about 14:27Z (file modified 14:27:24Z). Content unchanged.)

x130 (`runs/defense/x130_race2_std`, live EM&RK with the finish rule's safety test, 26 games, both seats identical): every
value equals x129's EM&RK column (astra33 +562, earlygun -215, econ17 -81, guard 0, eco6 +800, flood +663, lead v4 0, H10 -525,
H11 +35, H12 +315, H13 +315, staged +315, screened +315). Replay of the round-10 decision against the early-gun grower
(hrt-w2's obs_replay, read-only): the gold at the decision is 1276, not the 2012 of the post-income snapshot (income is credited
after the purchases of the round), so one tier5 is affordable (140 + the roster's 10 this round, 290 next round with the
income's one more tier5: 440 < 735); the race condition is correctly false and the two-round race cannot reach the early-gun
grower's HP before its round-11 lock. Against H10 the survival test fails (eight tier5 against S 1200 would leak 280 >= 240 HP),
also correctly. So race_kill's contribution is H11 and the faster kills; the early-gun grower is decided by the cheap pokes.
x131 (`runs/defense/x131_timing_trace`, v34 / v35 / EM&RK against hrt-w2's economy.timing, logs kept): +8 / -47 / -47. The
timing bot buys factories only and strikes in round 5 with all its gold (tier4 + two tier3 + two tier1, 490 gold): v34 takes the
same 112 as v35 (neither insures: the zero-leak plan against a tier4 package costs about 400 with the fortress holding 329-349
at round 4), and v34 wins because its tier1 pokes against the turret-less map deal 10 + 10 + 15 + 30 + 55 = 120 by round 5.
Hence the pokes are what decides the small games against bare, non-answering growers (timing +8, early-gun +130), the
speculative insurance decides nothing in those games, and the pokes are pure waste only when guards kill them. The gate that
separates the two is the fraction of copies arriving, not the leak per gold: new option poke_min_frac (default None), x132
measures eco_match + eco_match_pokes + poke_min_frac 0.7 / 0.9 + race_kill against the standard set plus timing.

## 2026-10-31T14:32Z  x132: the fraction gate cannot save the pokes against growers that add guards (negative); v36 = v35 + race_kill frozen
(Heading time corrected at 14:38Z: first written as 16:12Z by estimate; written at about 14:32Z, after the x132 log of 14:30Z. Content unchanged.)

`runs/defense/x132_frac_std` (live eco_match + eco_match_pokes + poke_min_frac 0.7 and 0.9 + race_kill; 60 games, both seats
identical; 0.9 rows identical to 0.7 where complete): astra33 +629, astra28 -53, early-gun +130, econ17 -43, timing +8, guard -60,
eco6_t5 +835, eco_then_flood +880, econ v2 +10, lead v4 0, H10 -653, H11 -653, H12 -373, staged guard -793, screened +247.
So the gate keeps the small poke wins (timing +8, early-gun +130, econ17 -43 instead of -81) but reproduces v34's catastrophic
losses to the staged guard and the handoffs. Reason (x128 trace of v34, the same purchases): the pokes are bought while they
do leak on the opponent's current map (round 3 and 4 before any guard, tier2 against the first guard's S 50 in rounds 5-6) and
die one round later when the next guard is added (S 80 from round 7); 220 gold of pokes by round 6 leaves 48 factories against
the striker's 86, and no gate on the current map can see a guard that is built in the same or the next round. The small wins
of v34 against the early-gun grower and the timing bot are therefore fragile: they rest on fixed scripts that never add a guard,
and a script that adds one splash at round 4 turns them into the -793 class. The robust choice against an out-growing passive
opponent is v35's: no pokes and no speculative insurance, gold into factories, mandatory defence only.
Decision: v36 = v35 + race_kill (eco_match=True, race_kill=True, every other parameter as v34; eco_match_pokes False,
poke_min_frac None). Frozen as `bot_research.bots.defense.frozen.v36.fortress:@make`; regression queue_al running (x133
strikers incl. handoff growth 5/6/7 x H10-H13, t62 tuning plain+asym, x134 STRONG, x135 scripted econ, x136 forecaster,
t63 mirror+eco). Known failures carried from v35: econ17 -81, timing -47, astra28 -65, early-gun grower -215, H10 -525 (all
verified above), forecaster tier4 r7 -190 (x126, to be re-measured as x136).
For the lead (14:05Z question): (a) fortress v34 does not beat the handoff family (x128: H10/H11 -653, H13 -77; wins H12 and
H14+); v35 loses only H10/H11 (-525/-465); EM&RK = v36 loses only H10 (-525) and wins H11 by 35 at round 50, H12/H13 by
kill at round 11 (x129/x130). (b) A cheaper zero-leak answer at round 8 against four tier5: none found by this planner. In
the v35 trace (x128 log 00019, round 8, 1306 gold, S 70 map, 44-step route) plan_defense's best partial plan is gun3 x5 +
gun2 x3 + gun1 + 4 walls (1270 gold) and two of the four tier5 still land (280); the zero-leak plan against four tier5 on
this layout is about S 1200 plus those guns (round 9: 21 more splashes, 1260 gold), i.e. about 2500 gold over two rounds.
Against four tier5 with S 70 the guns alone cannot kill more than two per round (gun damage per copy is bounded by the
frontmost-target rule: the five gun3 and three gun2 deliver about 4000 damage per round spread over the four copies), so
the only cheaper answer is to have the splash exposure built before the strike, which costs the economy that the
striker then out-grows; this lane found no escape from that trade-off (big_threat variants x117, guard_insure x97).

(Timestamp correction, written at 2026-10-31T14:38Z: the four shift-3 entries above were first labelled 14:40Z, 15:25Z, 15:50Z and 16:12Z by estimate; the labels were corrected to the real writing times 14:08Z, 14:21Z, 14:27Z and 14:32Z, established from the modification times of the run logs they report (x128 14:02Z, x129 14:20Z, x131 14:24Z, x132 14:30Z) and the clock. The measurements themselves are unchanged.)

## 2026-10-31T14:40Z  x133 and t62: frozen v36 on the striker set (growth 5/6/7 handoffs) and the tuning pool

x133 (`runs/defense/x133_v36_std`, 48 games, both seats identical): every standard row equals the live EM&RK rows of x129/x130
(astra33 +562, astra28 -65, early-gun -215, econ17 -81, timing -47, guard 0, eco6_t5 +800, eco_then_flood +663, econ v2 +10,
lead v4 0, staged +315 r11, screened +315 r11). Handoff family (the lead's HANDOFF pool rows for H10-H13):

| growth | H10 | H11 | H12 | H13 |
| --- | --- | --- | --- | --- |
| 5 | -105 (r50) | -79 (r50) | +367 (r50) | +453 (win r12) |
| 6 | -525 (r50) | +35 (r50) | +315 (win r11) | +315 (win r11) |
| 7 | -219 (r50) | +227 (r50) | +1013 (win r11) | +1013 (win r11) |

So v36 loses the H10 column at every growth and growth 5 H11; it wins the other seven. Growth 6 is the striker's best timing
against v36 (86 factories and the strike exactly when fortress's own economy is still catching up); growth 5 strikes with less
(one tier5 per round at first) and growth 7 strikes later, when v36 already holds S 1200.
t62 (`runs/defense/t62_v36_tuning`, 26 tuning opponents x standard start and asym:3:2, 104 games): 102-2-0, the two draws the pool
turtle under asym:3:2 (0-0, as for v34 and v35). x134 STRONG, x135 scripted econ, x136 forecaster and t63 mirror+eco follow.

## 2026-10-31T14:50Z  v36 regression complete; x137 GROWERS 142-0-0 for both v34 and v36; x138 PUNISH; FINAL RECOMMENDATION REVISED: frozen v36

Regression of frozen v36 (`bot_research.bots.defense.frozen.v36.fortress:@make`; = v34 with eco_match=True and race_kill=True;
fortress.py sha256 9ba4203f4bf1454f4af3af4af9afdf0025f81f54d6827ebdcb9cd70e67ee73f8, all other files identical to v34/v35,
see frozen/v36/SHA256SUMS). All runs both seats, 0 rejected actions, 0 bot errors.

| run | pool | v36 | v35 | v34 |
| --- | --- | --- | --- | --- |
| t62 | 26 tuning opponents, standard + asym:3:2 (104) | 102-2-0 | 102-2-0 (t61) | 102-2-0 (t60) |
| t63 | 26 tuning opponents, mirror:1:2 + eco:2 (104) | 100-4-0 | not run | 100-4-0 (t59, v33 code path) |
| x134 | STRONG pool + lead v4 (26) | 22-2-2 (timing -47 x2) | 22-2-2 (x124) | 24-2-0 (x118) |
| x135 | econ17 + econ15 leak on 4 scripted openings (16) | 14-1-1 (asym:23:2 seat 1: both destroyed; econ15 -875) | 14-1-1 (x125) | 14-0-2 (x119) |
| x136 | exact stateful forecaster of the candidate, 3 timings (6) | tier4 r7 -190, tier5 r8 0, tier5 r10 0 | same (x126) | -60, 0, 0 (x109) |
| x133 | standard counters + strikers (48) | see 14:40Z | | |
| x137 | lead's GROWERS pool (71 settings: roster_bait 35 + maze_grower 36; 142 games) | 142-0-0, min +100, mean +618 | | 142-0-0, min +91, mean +505 |
| x138 | lead's PUNISH pool (astra33, astra28, 15 guarded_schedule settings; 34 games) | 32-0-2 (astra28 -65) | | 30-0-4 (astra33 -745, astra28 -65) |

x137 is the most useful new fact for the team: the whole GROWERS pool (hrt-w3's roster_bait and maze_grower counters, on which
the lead reports best_v9e at 66-0-76) is beaten by both fortress versions in every setting and seat; v36 by larger margins. The
fortress's mandatory zero-leak defence against the visible roster (the bait) plus its first-tier5 response (gun3s at the first
visible heavy copy, splashes the round after) handles the tier5 waves of these growers, which strike with one tier5 at first
(growth 4-9 with one tier5 per round from gold 650-1300), unlike the two-per-round handoff striker. x138: v36 beats every
guarded_schedule setting (one tier1 in round 1, then a 200-copy order of tier3/4/5 in rounds 3-7, limited by gold) by 633 to
1268, v34 too except astra33.
Smoke (runner form): frozen v36 vs idle, `runs/defense/smoke_frozen_v36_vs_idle.jsonl`: player 0 wins in round 8 (800 : -13),
as for v29-v34.

FINAL RECOMMENDATION of this lane, revised: frozen v36 (`bot_research.bots.defense.frozen.v36.fortress:@make`; runner form
`...frozen.v36.fortress:decide`, stateful per player, renewed in round 1). SHA-256 (frozen/v36/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
    f838ef8b4c623631aad88932e4b119d0464e7879d344d85c329340037ac2730c  counter_earlygun.py
    9ba4203f4bf1454f4af3af4af9afdf0025f81f54d6827ebdcb9cd70e67ee73f8  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Reasoning for the revision (v34 -> v36): on the pools where they differ, v36 trades small losses against four answering or
early-striking scripts (econ17 -81 instead of +17, timing -47 instead of +8, early-gun grower -215 instead of +130, forecaster
tier4 r7 -190 instead of -60) for the removal of every catastrophic loss of v34 to model-free strikers (astra33 -745 -> +562,
staged guard -793 -> +315, handoff H11 -653 -> +35, H12 +213 -> +315, H13 -77 -> +315; H10 -653 -> -525 remains a loss)
and larger margins on the 71 GROWERS settings; everything else measured is equal (tuning 102-2-0, mirror/eco 100-4-0,
scripted econ, floods, eco6_t5, guards). x132 showed that v34's small wins rest on the scripts never adding a guard: one splash
at round 4 turns them into the -793 class, so v36's choice (no pokes and no speculative insurance while out-grown by a passive
opponent) is the robust one. v34 stays the documented alternative for opponent sets known to contain only answering economy
bots and no model-free strikers; v35 is superseded by v36 (identical except race_kill, which only adds wins in the tested scope).
Known failures of v36 (all verified on the engine, both seats): handoff H10 at growth 5/6/7 (-105 / -525 / -219) and growth 5
H11 (-79): a striker with 86 factories at round 6, two tier5 per round from round 7 and a lock from round 10 cannot be out-grown
or insured against in time (14:08Z, 14:32Z analysis); the first hidden heavy copy of answering or early-striking scripts (econ17
-81, timing -47, astra28 -65, forecaster tier4 r7 -190, early-gun grower -215); the weaker asymmetric scripted map (asym:23:2 seat 1:
both destroyed against econ17, -875 against econ15 leak); 0-0 against pure turtles, guard_continuation and lead v4; blind round
1 (-5 against three-tier1 openers, as before).

## 2026-10-31T14:54Z  Sixth astra review (astra/v36-review/answer.md in the lane directory): claims, checks planned, fixes applied

Claims (astra replayed its schedules through the engine in both seats; all are to be checked here by matches):
1. eco_match regression confirmed with the early-gun grower's exact schedule (gun1 (3,1) + 3 factories; 3/6/10/18/31 factories;
   tier5 1/2/2 in rounds 7-9; 23 walls + 18 splashes in round 10, 5 walls + 8 splashes in round 11): v36 520:735 (-215), v34
   520:390 (+130); ablation: v36 with eco_match off = v34's result, with race_kill off = -215. Outgoing damage 410 (v34) against
   65 (v36). Known (x121, x129, x132) and accepted as the price of the striker wins; recorded as the exact schedule.
2. Fake striker (5/4/8 factories, splash (10,1) r4 + 11 factories, 22 factories, splash (1,0) r6 + 36 factories, 44 tier1 in
   round 7 (660 gold, all die on S 70), nothing in rounds 8-9, 32 walls + 24 splashes in round 10): v36's race_kill fires in
   round 10 (three tier5, predicted 472 + 752 against 713 HP) and deals 0 against the hidden lock (S 1560). Final v36 800:713,
   v34 800:701: a verified false positive of the race, not a winning counter (fortress is immune from round 9 and the fake
   striker never attacks again).
3. Defects in _race_kill: (a) the next-round estimate reuses the current observation, so roster entries that expire after this
   round (lifespan 12, indices compacted) are counted again (constructed round-18 state: predicted 280 + 420, actual 280 + 280);
   (b) the race can execute in round 50 and count a round 51 (constructed state: two tier5 lose 190:220 where thirteen tier3
   win 190:162); (c) "survives the worst affordable composition" is over the sampled compositions (exhaustive only up to 400
   ordered lists), as documented since review 1; (d) "the opponent's map does not stop a tier5" tests S < 1500 only; (e) no
   check of next-round survival or of a budget for the next round's mandatory defence. Astra also confirms the income timing
   (pre-income gold at the decision, income credited after the purchases) and that counting the purchase in both rounds is right.
4. Question 3 answered positively: a fixed schedule from the fortress opening (20 walls, two tier1, two factories; then 4/7/12/
   21/37 factories, 83 factories and 1285 gold after round 6) that buys gun3 at (10,1), (1,3), (10,5), (10,8), (11,8) and gun1
   at (10,9) plus 12 factories in round 7 (1270 gold; kills both round-7 tier5 with zero leak), then 4 walls + 24 splashes +
   2 factories in round 8 (1484; S 1260 on the 66-step route, zero leak against 4, 6 and 8 tier5), then nothing, holds 800
   HP against the H10 striker (800:770 at round 10, both seats on the real GuardHandoff). The two differences from v36: v36
   buys 37 factories in round 7 instead of the guns (it cannot see the strike, and its speculative insurance is skipped while
   matching), and the guns go in before the splashes.
Fixes applied to the live module (not yet frozen): the race requires that the opponent has bought a copy of the heaviest tier
(hist["heavy_cost"], against claim 2), the next-round estimate uses an observation advanced by one round (roster expiry, 3a), and
no race in the last two rounds (3b, the finish rule's `late` guard). 3c-3e stay documented limitations.
Hypothesis from claim 4 (falsifiable): with eco_match's economy (83 factories at round 7 instead of 18-48), the big-threat
insurance that x117 rejected on v33 (economy too small, the partial plans wasted) now works: `big_threat=280` makes the
speculative insurance mandatory (share 1.0, partial best, also while matching) from the round in which the opponent's visible
gold affords two tier5 (1300), which is round 7 for the growth-6 striker, exactly astra's timing; `big_threat=140` fires one
round earlier (one tier5 affordable). x139 (queue_an) measures v36-live, +big_threat 140, +big_threat 280 against the handoff
growth 5/6/7 x H10/H11, staged, screened, astra33, astra28, early-gun, econ17, timing, guard, eco6_t5, eco_then_flood, econ v2
and lead v4 (108 games).

## 2026-10-31T15:01Z  x139: big_threat on top of v36's economy (astra's round-7 hypothesis); the race-rule fixes change no result

`runs/defense/x139_bigthreat` (live module; 108 games, both seats identical). A = eco_match + race_kill with the three race fixes
of 14:54Z (heavy-copy condition, next-round expiry, late guard): every value equals frozen v36 (x133), so the fixes change no
measured game. BT140 / BT280 = A plus big_threat 140 / 280 (the speculative insurance becomes mandatory with the whole gold,
also while matching, from the round in which the opponent's visible gold affords one / two tier5):

| opponent | A (= v36) | BT140 | BT280 |
| --- | --- | --- | --- |
| handoff g5 H10 / H11 | -105 / -79 | -385 / -385 | -105 / -79 |
| handoff g6 H10 / H11 | -525 / +35 | -805 r9 / -805 r9 | -105 / -105 |
| handoff g7 H10 / H11 | -219 / +227 | -245 / -245 | -105 / -79 |
| staged guard [4,6] | +315 r11 | -945 r9 | +593 r12 |
| screened guard r9 | +315 r11 | -805 r9 | +975 r13 |
| astra33 / astra28 | +562 / -65 | +455 / -5 | +562 / -65 |
| early-gun grower | -215 | +105 | -215 |
| econ17 / timing | -81 / -47 | +5 / -47 | -81 / -47 |
| eco6_t5 / eco_then_flood | +800 / +663 | +1225 / +690 | +1075 / +970 |
| guard / econ v2 / lead v4 | 0 / +10 / 0 | 0 / +10 / 0 | 0 / +10 / 0 |

BT140 (insure when one tier5 is affordable, round 6 for the growth-6 striker) is the x117 result again: the round-6 insurance
drains the matched economy and the two-per-round strike kills the fortress in round 9 (-805 / -945). BT280 (two tier5 affordable,
round 7, astra's timing) removes the catastrophic H10 loss at every growth (-525 -> -105: one tier5 leaks once, the early pokes
dealt 35) and raises the guard and flood margins, but loses the H11 wins (+35 -> -105, +227 -> -79): once the striker's gold
affords two tier5 every round, the big-threat test fires every round, the whole gold goes to partial insurance and the fortress
never attacks (a turtle against a locker is a loss by the HP it leaked). Hypothesis for x141 (queue_ap): the insurance should
cover only the FIRST strike (while the opponent has made no heavy purchase, history max_spend 0); after the strike is visible the
mandatory defence, the history insurance and the race rule take over as in v36. Option big_threat_prestrike=True in the live
module; x141 measures big_threat 280 and 200 with it against the same set plus H12.

## 2026-10-31T15:04Z  x140, for the lead (14:53Z request): this lane's round-5/6 strikers against P5TNUBM and P4TNUB, both seats

counter_earlygun.py gained three options whose defaults reproduce the original schedule exactly (tier of the waves, guard_round =
one splash at (10,1) in that round, gun_cell): `counter_earlygun:@make?growth=4&lock_from=8&tier="tier4"&guard_round=4` is a
round-5 striker (gun1 (3,1) + 3 factories, 3 / 6 factories, splash (10,1) + 7 factories in round 4, one tier4 in each of rounds
5-7, lock from round 8), growth=5 the round-6 version. `runs/defense/x140_lead_strikers` (48 games, both seats identical,
0 rejected actions, 0 bot errors; P5TNUBM and P4TNUB specs copied from the lead's RUN_STATUS):

| striker | P5TNUBM | P4TNUB | fortress v36 |
| --- | --- | --- | --- |
| round-5 tier4 striker, guard r4, lock r8 | +51 | +135 | -7 |
| round-5 tier4 striker, no guard, lock r8 | +105 | +175 | +165 |
| round-6 tier4 striker, guard r4, lock r9 | +255 | +279 | -7 |
| round-6 tier5 striker, guard r4, lock r9 | +135 | +219 | +325 |
| early-gun grower (growth 6, tier5 1/2/2, lock r10) | +365 | +160 | -215 |
| counter_astra33 | +888 (r15) | +888 (r15) | +562 (r12) |
| counter_astra28 | +10 | +10 | -65 |
| staged guard [4,6] | +1423 (r13) | +753 (r13) | +315 (r11) |

Both repair candidates win every one of these eight strikers in both seats; none of this lane's strikers is a counter to them.
New for this lane: the two guarded tier4 strikers are small new losses of v36 (-7, -7: the round-5/6 tier4 leaks 60 once, the
early pokes deal 53, the guard kills the rest), the same first-hidden-heavy-copy class as econ17 and timing; without the guard
v36 wins (+165) through its pokes. Recorded as known failures of v36.

## 2026-10-31T15:08Z  x141: big-threat insurance restricted to the first strike (prestrike); v37 frozen for a full regression

`runs/defense/x141_prestrike` (live module; eco_match + race_kill + race fixes + big_threat 200 / 280 with big_threat_prestrike;
76 games, both seats identical). Reference v36 from x133/x139 and BT280 (no prestrike) from x139:

| opponent | v36 | BT280 | PS280 | PS200 |
| --- | --- | --- | --- | --- |
| handoff g5 H10 / H11 | -105 / -79 | -105 / -79 | -105 / -79 | -105 / -79 |
| handoff g6 H10 / H11 / H12 | -525 / +35 / +315 | -105 / -105 / - | -219 / +139 / +837 | -219 / +139 / +837 |
| handoff g7 H10 / H11 | -219 / +227 | -105 / -79 | -105 / -79 | -105 / -79 |
| staged guard / screened guard | +315 / +315 | +593 / +975 | +619 / +1195 | +619 / +1195 |
| astra33 / astra28 | +562 / -65 | +562 / -65 | +562 / -65 | +455 / -65 |
| early-gun grower | -215 | -215 | -215 | +110 |
| econ17 / timing / guard | -81 / -47 / 0 | same | same | same |
| eco6_t5 / eco_then_flood | +800 / +663 | +1075 / +970 | +800 / +970 | +806 / +690 |
| econ v2 / lead v4 | +10 / 0 | same | same | same |

Restricting the insurance to the rounds before the opponent's first heavy purchase restores the H11 wins that BT280 lost (g6 H11
+139, better than v36's +35, and g6 H12 +837) while keeping most of its H10 gain (g6 H10 -219 against v36's -525). The remaining
cost is growth-7 H11 (+227 -> -79: the round-7 insurance is bought one round before a strike that only comes in round 8, and the
weaker economy then forgoes the round-10 race). PS200 (insure once the visible gold affords 200 damage, e.g. tier5 + tier4 = 910
gold) additionally wins the early-gun grower (+110: its round-6 gold of 1092 triggers the insurance one round before its first
tier5) at the price of a smaller astra33 margin (+455). Against the lead's and hrt-w3's canonical case (growth 6) PS200 is
better than v36 on every H; over the whole striker set it has the same W-L count as v36 (one loss moved from early-gun to g7
H11) and a better HP sum. The big-threat test fires only against opponents that hoard >= 910 gold without having bought a
heavy copy, so the risk is on hoarding economy bots: that is what the regression measures.
Frozen as v37 = v36 + the three race fixes + big_threat=200 + big_threat_prestrike=True
(`bot_research.bots.defense.frozen.v37.fortress:@make`; fortress.py sha256 c4bfde6dcdddc785de04b927a9b871ba4bdc744263428d5c664b4d6971206b19;
other files identical to v34-v36). Regression queue_aq running: x142 strikers, t64 tuning plain+asym, x143 STRONG, x144 scripted
econ, x145 forecaster, t65 mirror+eco, x146 GROWERS, x147 PUNISH. v36 stays the recommendation until the regression is read.

## 2026-10-31T15:10Z  The first-strike class costs one gun3: exact planner result on the fortress's early map

Replaying the v36-timing game (hrt-w2's obs_replay, read-only) at the decisions of rounds 4 and 5 and running plan_defense with an
unlimited budget against the timing bot's round-5 package (tier4 + two tier3 + two tier1, 490 gold, 112 damage unprotected):
the zero-leak plan is ONE gun3 (200 gold, one action) on the fortress's map of that moment (20 layout walls, one splash, 40-42 step
route), at round 4 (fortress gold 207) and at round 5 (349); against one tier4 alone also 200; splash-only plans do not exist at
these budgets. The fortress's speculative-insurance rule would have bought it at round 5 (spec_share 0.6 x 349 = 209 >= 200) and
stopped the strike before it landed (construction precedes combat); eco_match skipped it because it skips every speculative plan
while matching (opponent 31 factories against 19). hrt-w3 found the same single-gun3 answer independently for the lead's P5TNUBM
on its own map (validation.md 15:07Z: gun3 at (0,5), 200 gold, restricted minimum over single additions). So the first-hidden-
heavy-copy losses of the eco_match family against tier4-level strikers (timing -47, econ17 -81, the guarded round-5/6 tier4
strikers -7, astra28 -65) are not an economy-versus-safety dilemma at the tier4 level: the insurance costs one gun3, while a
tier5-level strike (650+ gold) needs about 1000 gold of guns (astra's round-7 schedule) and is the real dilemma.
New option eco_match_insure_cap (0 = v36/v37 behaviour): while matching, a FULL zero-leak plan against the affordable
compositions is still bought when it costs at most the cap (and spec_share of the gold); the graded poke fallback stays off.
x148 (queue_ar, after the v37 regression) measures caps 200 and 300 on top of v37's settings against the striker set, the
tier4 strikers, timing, econ17 and the standard checks. Risk to measure: against the astra-33 guard, v34's 190 gold of small
speculative guns in rounds 4-6 were part of its economy loss; the cap allows exactly such purchases (each a full zero-leak plan
against the then-affordable compositions) while matching.

## 2026-10-31T15:26Z  v37 regression: the pre-strike insurance loses six GROWERS games; v36 stays the recommendation, v37 is an alternative

Frozen v37 (= v36 + the three race fixes + big_threat=200 with big_threat_prestrike; fortress.py sha256
c4bfde6dcdddc785de04b927a9b871ba4bdc744263428d5c664b4d6971206b19), all both seats, 0 rejected actions, 0 bot errors:

| run | pool | v37 | v36 |
| --- | --- | --- | --- |
| t64 | tuning, standard + asym:3:2 (104) | 101-3-0 (new draw: eco_then_flood switch 11 tier5 under asym:3:2 seat 1, both bases destroyed r11) | 102-2-0 |
| t65 | tuning, mirror:1:2 + eco:2 (104) | 100-4-0 (same turtle draws) | 100-4-0 |
| x143 | STRONG + lead v4 (26) | 22-2-2 (timing -47) | 22-2-2 |
| x144 | econ17 + econ15 leak, 4 scripted openings (16) | 14-0-2 (econ17 asym:23:2 seat 1 -3765 instead of the both-destroyed draw; econ15 -875) | 14-1-1 |
| x145 | exact forecaster, 3 timings (6) | 0 / 0 / 0 (tier4 r7 was -190) | -190 / 0 / 0 |
| x142 | strikers (48) | handoff g5 -105/-79/+367/+453, g6 -219/+139/+837/+1195, g7 -105/-79/+227/+813 (H10..H13); staged +619, screened +1195, astra33 +455, early-gun +110; astra28 -65, econ17 -81, timing -47 | g5 -105/-79/+367/+453, g6 -525/+35/+315/+315, g7 -219/+227/+1013/+1013; staged +315, screened +315, astra33 +562, early-gun -215 |
| x146 | GROWERS (142) | 136-0-6: LOSES maze_grower cash_rank_1 growth 6 bait [tier2] (-747 r9), maze_grower empty growth 7 bait [tier1] (-720 r9), roster_bait (one setting, -720 r9), both seats | 142-0-0 (min +100) |
| x147 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |

The six GROWERS losses are the hoarder effect predicted at 15:08Z: a grower whose bait costs less than 100 keeps history max_spend
at 0, its gold passes 910 in rounds 6-7, and from then on the pre-strike test makes the fortress spend its whole gold on partial
insurance every round against a flood that grows faster than any partial plan; the fortress is destroyed in round 9 where v36
(no insurance, matched economy, finish rule) wins by 100 or more. The t64 draw against eco_then_flood switch 11 under asym:3:2
has the same mechanism (ten rounds of hoarding). Partial insurance against an unbounded flood is wasted gold; the rule can
only be right when the threat is bounded (the handoff's two tier5 per round) and that cannot be read from the opponent's gold.
Decision: v36 stays the FINAL RECOMMENDATION. v37 is the documented alternative for opponent sets dominated by the handoff /
early-gun strikers and exact forecasters (where it is better: g6 H10 -219, H11 +139, early-gun +110, forecaster tier4 r7 0), at
the price of six GROWERS losses, one tuning draw, one scripted draw turned loss and growth-7 H11. The three race fixes are in v37
and in the live module; they change no measured game of v36 (x139 column A), so v36 is kept as frozen rather than re-frozen.

## 2026-10-31T15:29Z  x148: the cheap-insurance cap fixes timing and econ17 without touching the strikers

`runs/defense/x148_insurecap` (live module = v37 settings + eco_match_insure_cap 200 / 300; 84 games, both seats identical; the two
caps give identical results, so one gun3 is what gets bought). Changes against v37 (x142): timing -47 -> +65, econ17 -81 -> +5,
eco6_t5 +806 -> +1240, eco_then_flood +690 -> +1100, astra33 +455 -> +523; every handoff row, staged, screened, astra28 (-65), the
two guarded tier4 strikers (-7), guard 0, econ v2 +10, lead v4 0 unchanged. Mechanism as computed at 15:08Z: while matching, the
one-gun3 zero-leak plan against the tier4-level compositions is bought in round 5 (209 >= 200 of the 349 gold), so the timing
bot's and econ17's first strike is stopped before it lands; against the tier5-level strikers the full plan costs more than the
cap and nothing is bought, so the economy of v36 is kept. The guarded round-5 tier4 strikers still land once (-7): at the round-4
decision the fortress holds 207 gold (0.6 x 207 = 124 < 200) and at round 5 the strike is already in the hidden purchases of the
same round (construction precedes combat, so a round-5 gun3 would stop it, but spec_share gates it to 209 only when gold >= 334).
Since v37's pre-strike insurance is rejected (15:26Z), x149 (queue_as) measures the cap on top of v36's settings alone
(eco_match + race_kill + the race fixes + eco_match_insure_cap 200, and 120 as a control below one gun3) against the same set; if
the timing/econ17 gains hold and the striker rows equal v36, v38 = v36 + race fixes + cap 200 will be frozen and regressed.

## 2026-10-31T15:32Z  Seventh astra review (astra/v37-exploits/answer.md): hoarders against v37 and the cap; race fixes confirmed; growth-6/7 indistinguishable

Claims (astra ran them on the engine, both seats; reproduced here as `bots/defense/counter_astra37.py`, variants G, B, G15, B15,
measured in x150 against v34, v36, v37 and the live v36 + cap module):
1. Guarded hoarder G (5 / 4 / 8 factories; round 4 gun1 (10,1) + 13 factories; nothing in round 5; 47 and 59 factories in rounds
   6-7; three tier5 in each of rounds 8 and 9; a fixed 72-step lock with S 1520 in round 10): v36 +135, v37 -55, v37 + cap -55.
   Mechanism: at decision 6 G shows 945 gold and no minion, the pre-strike test sees 200 damage and buys two gun3 (400); at round 8
   v37 holds 739 gold and 45 factories against v36's 1200 and 74; both take 140, v36 deals 275 before the lock, v37 85. Disabling
   big_threat alone restores v36's result, so the loss is the pre-strike trigger, not the race fixes. G15 (one tier1 in round 5)
   shows that a cheap sign of activity does not switch the trigger off (max_spend stays 0).
2. Bare hoarder B (as G without the gun1, 14 / 49 / 61 factories): v36 +416 (kills it in round 8), v37 +215, v37 + cap -15: the
   cap's round-5 gun3 (200) and round-7 purchase (200) plus v37's round-6 insurance (400) leave 42 factories at round 8 against
   v37's 66; 11 splashes instead of 17, one tier5 leaks (140) and the repairs eat the attack budget (90 less dealt). The requested
   "200 every round from round 3" is impossible (the capped plan needs 334 gold; the fortress has at most 253 in round 3).
3. The three race fixes are correct within their scope (expiry: constructed round-18 state, engine 280 + 280, v37 predicts
   280 + 280 and rejects the kill that v36 accepted; heavy-copy condition: 44 tier1 give max_spend 660, heavy_cost 15; late guard
   admits round 48 and rejects 49-50). Not established: survival next round, funding of the projected purchase, sampled threats.
4. Growth-6 and growth-7 handoffs are indistinguishable at the round-7 decision: identical histories through round 6 and identical
   observations at decision 7 (gold 1317, 86 factories); the hidden round-7 choice (two tier5 or 65 factories) cannot be read.
   So the growth-7 H11 loss of v37 is the unavoidable price of insuring at round 7; no trigger can take both.
5. Harness caveat (astra): the engine's observation carries each player's name (td_game/engine.py snapshot(): "name"), and the
   harness uses the full bot spec as the name, so an opponent's spec string (e.g. "growth_rounds=6", "fortress") is readable by
   a bot from its observation. This lane's bots never read a name (grep of bots/defense/*.py: no use of "name"); the caveat is for
   the lead's harness and hrt-w3's evaluation (a bot could identify its opponent from the spec); the indistinguishability claim
   above holds only when the names are equal or ignored.
Consequences: v37 is confirmed as rejected (15:26Z). The cap must be judged on top of v36 (x149 running), and against B/B15 (x150),
where astra's trace predicts a cost of about 400 gold in rounds 5-7 against a bare hoarder that v36 kills in round 8.

## 2026-10-31T15:36Z  x149: the insurance cap on v36's settings is a clean improvement on the striker and standard set

`runs/defense/x149_v36cap` (live module: eco_match + race_kill (with fixes) + eco_match_insure_cap 200, control 120; 84 games, both
seats identical). Cap 120 (below one gun3) reproduces v36 in every row, as expected. Cap 200 against v36: timing -47 -> +65, econ17
-81 -> +5, astra33 +562 -> +704, eco_then_flood +663 -> +1000, eco6_t5 +800 -> +566 (still a kill in round 10); every handoff row
(g5 -105/-79, g6 -525/+35/+315, g7 -219/+227), staged +315, screened +315, astra28 -65, early-gun -215, the two guarded tier4
strikers -7, guard 0, econ v2 +10, lead v4 0 unchanged. So on this set the cap only adds wins; the remaining question is the bare
hoarder B of astra's seventh review (x150) and the broad regression.

## 2026-10-31T15:37Z  x150: astra's hoarders against v34, v36, v37 and the cap; v38 = v36 + race fixes + cap 200 frozen

`runs/defense/x150_astra37` (counter_astra37 variants, 32 games, both seats identical):

| hoarder | v34 | v36 | v37 | v36 + cap 200 (live) |
| --- | --- | --- | --- | --- |
| B (bare, 3 tier5 in rounds 8 and 9, lock round 10) | +440 (kill r8) | +416 (kill r8) | +215 (r50) | +210 (r50) |
| B15 (B + one tier1 in round 5) | +440 (kill r8) | +416 (kill r8) | +215 | +210 |
| G (gun1 (10,1) in round 4, otherwise B) | +388 (kill r8) | +135 (r50) | -55 | +135 |
| G15 | +388 (kill r8) | +135 | -55 | +135 |

Astra's engine numbers for v36 and v37 are reproduced exactly (+416 / +135, +215 / -55). The cap on v36's settings keeps G at
+135 and turns the round-8 kill of B into a round-50 win by 210 (the round-5 and round-7 gun3 purchases, 400 gold, cost the
round-8 kill: the fortress holds 42 instead of 74 factories at round 8), no loss. Note that v34 beats all four hoarders by kill in
round 8 (its pokes and speculative guns do not matter here; the hoarders strike late and v34's economy suffices for the kill).
Decision: v38 = v36 + the three race fixes + eco_match_insure_cap=200 (eco_match=True, race_kill=True, big_threat None; every
other parameter as v34), frozen as `bot_research.bots.defense.frozen.v38.fortress:@make` (fortress.py sha256
a6a8f2aec2a97f31779f3caa98951ab81c12ac2d632a989683313b3e7c69c72c). Regression queue_au running: x151 strikers,
t66 tuning plain+asym, x152 STRONG, x153 scripted econ, x154 forecaster, t67 mirror+eco, x155 GROWERS, x156 PUNISH, x157
hoarders + timing + guarded tier4 strikers. v36 stays the recommendation until the regression is read; v38 replaces it only if it
is at least v36 on every pool (W-D-L) with the timing/econ17 gains.

## 2026-10-31T15:52Z  v38 regression complete: at least v36 on every pool; FINAL RECOMMENDATION REVISED: frozen v38

Frozen v38 = v36 + the three race fixes (14:54Z) + eco_match_insure_cap=200 (eco_match=True, race_kill=True, big_threat None,
all other parameters as v34). All runs both seats, 0 rejected actions, 0 bot errors.

| run | pool | v38 | v36 |
| --- | --- | --- | --- |
| t66 | 26 tuning opponents, standard + asym:3:2 (104) | 102-2-0 (pool turtle draws) | 102-2-0 |
| t67 | 26 tuning opponents, mirror:1:2 + eco:2 (104) | 100-4-0 (turtle draws) | 100-4-0 |
| x152 | STRONG pool + lead v4 (26) | 24-2-0 (timing now +65) | 22-2-2 |
| x153 | econ17 + econ15 leak, 4 scripted openings (16) | 14-1-1 (identical rows) | 14-1-1 |
| x154 | exact stateful forecaster of the candidate, 3 timings (6) | tier4 r7 -190, tier5 r8 0, r10 0 | same |
| x151 | strikers and standard counters (48) | handoffs g5/g6/g7 x H10-H13 identical to v36 (g6: -525 / +35 / +315 / +315); staged +315, screened +315; astra33 +704 (+562); astra28 -65; early-gun -215; econ17 +5 (-81); timing +65 (-47); eco6_t5 +566 (+800); eco_then_flood +1000 (+663); guard 0, econ v2 +10, lead v4 0 | |
| x155 | lead's GROWERS pool (142) | 142-0-0, min +100, mean +703 | 142-0-0, min +100, mean +618 |
| x156 | lead's PUNISH pool (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x157 | astra's hoarders B/B15/G/G15, timing, guarded tier4 strikers (14) | +210 / +210 / +135 / +135, +65, -7 / -7 | +416 / +416 / +135 / +135, -47, -7 / -7 |

Smoke (runner form): frozen v38 vs idle, `runs/defense/smoke_frozen_v38_vs_idle.jsonl`: player 0 wins in round 8 (800 : -13), as
for v29-v36.
FINAL RECOMMENDATION of this lane, revised: frozen v38 (`bot_research.bots.defense.frozen.v38.fortress:@make`; runner form
`...frozen.v38.fortress:decide`, stateful per player, renewed in round 1). SHA-256 (frozen/v38/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
    922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
    b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
    a6a8f2aec2a97f31779f3caa98951ab81c12ac2d632a989683313b3e7c69c72c  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Decision rules of v38 in one paragraph (details in the fortress.py docstring): layout walls first (the 66-step annealed serpentine,
built in stages as gold allows); mandatory zero-leak defence against the opponent's visible roster by the exact planner (splash
exposure on the route plus frontmost-target gun simulation, verified against the engine's combat); economy matching in rounds <= 7
while the opponent owns >= 1.5 x my factories + 2 and has never spent >= 100 gold on minions in one round: no pokes, no
speculative insurance unless a full zero-leak plan against every affordable composition costs <= 200 gold (one gun3), gold into
factories; otherwise speculative zero-leak insurance against the affordable compositions within 60 percent of the gold, the
history insurance against one more round of the opponent's largest observed attack spend, lethal-share and capacity rules;
finish rule (all gold on one tier when the exact simulation kills on the opponent's current map, with a screen copy and mass
sizes); two-round race (all gold on tier5 when my map is zero-leak against the visible roster, I survive the worst affordable
addition, the opponent has bought a tier5 and its current map leaks tier5, and roster plus next round's income kill within two
rounds on its current map); opportunistic pokes with 25 percent of the remaining gold by exact leaked damage per gold; factories
with the rest; re-planned layout on scripted (foreign) maps.
Known failures of v38 (verified on the engine, both seats): handoff strikers H10 at growth 5/6/7 (-105 / -525 / -219) and growth 5
H11 (-79); the forecaster's round-7 tier4 (-190, exact model of v38); astra28 (-65); early-gun grower (-215); guarded round-5/6
tier4 strikers (-7); the weaker asymmetric scripted map (asym:23:2 seat 1: both destroyed against econ17, -875 against econ15 leak);
0-0 against pure turtles, guard_continuation and lead v4; blind round 1 (-5 against three-tier1 openers). Alternatives: v36
(identical without the cap and the race fixes), v37 (pre-strike insurance: better on growth-6 handoffs and the forecaster, six
GROWERS losses), v34 (poking insurer: wins econ17/timing/early-gun by pokes, loses astra33 -745, staged -793, H10/H11 -653).

## 2026-10-31T15:58Z  x158, for the lead (15:35Z request): fortress v36 / v37 / v38 against P5TNUBM and frozen best_v9e

`runs/defense/x158_vs_lead` (60 games; P5TNUBM spec from the lead's RUN_STATUS, best_v9e = `experiments.lead.frozen.best_v9e:decide`;
standard start and four scripted openings; entries are (HP difference, end round) for fortress seat 0 and seat 1):

| opponent, start | v36 | v37 | v38 |
| --- | --- | --- | --- |
| P5TNUBM, standard | 0 (r50) / 0 | 0 / 0 | 0 / 0 |
| P5TNUBM, mirror:1:2 | +3530 (r33) / +3530 | +3530 / +3530 | +3530 / +3530 |
| P5TNUBM, asym:3:2 | +2380 (r35) / +1147 (r43) | +840 / +27 | +2380 / +1147 |
| P5TNUBM, mirror:22:3 | -840 (r13) / -840 | -1960 (r21) / -1960 | -840 / -840 |
| P5TNUBM, asym:23:2 | -6575 (r22) / -3765 (r20) | -6575 / -6285 | -6575 / -3765 |
| best_v9e, standard | -5 / -5 | -5 / -5 | -5 / -5 |
| best_v9e, mirror:1:2 | +3530 / +3530 | +3530 / +3530 | +3530 / +3530 |
| best_v9e, asym:3:2 | +2380 / +1147 | +840 / +27 | +2380 / +1147 |
| best_v9e, mirror:22:3 | -840 / -840 | -1960 / -1960 | -840 / -840 |
| best_v9e, asym:23:2 | -3765 / -6575 | -6575 / -6285 | -3765 / -6575 |

Reading: on the standard start the lead's revision P5TNUBM draws every fortress version 0-0 (neither side ever lands a copy; the
round-1 exchange that gives best_v9e its -5 does not happen), best_v9e keeps the -5 of the blind round-1 poke (x113, x127). On the
scripted openings both lead bots play the econ20 foreign policy and the results are those of x127: fortress wins the two lighter
openings (mirror:1:2 by 3530, asym:3:2 by 1147-2380) and loses the two heavily obstructed ones (mirror:22:3 -840 at round 13, asym:23:2
-3765 / -6575 at rounds 20-22: capacity races on maps where no zero-leak defence exists). v36 and v38 are identical here (the cap and
the race fixes never act on these maps); v37's round-7 insurance costs it the asym:3:2 margin and the mirror:22:3 race. Over the
ten standard-start games against the lead's bots the fortress family is 0W-6D-4L by -5; over the forty scripted games 24W-0D-16L.

## 2026-10-31T16:00Z  x159: hrt-w3's guarded round-4 strike (the counter that beats both lead nominees) against the fortress family

`runs/defense/x159_guarded_r4` (12 games, both seats identical, logs kept). Opponent: `bot_research.bots.counters.guarded_round4_trigger`
with hrt-w3's winning parameters (validation.md 15:35Z: layout empty, growth 6, tier5, factory cap 2000, purchase cap 1000,
upgrade_round 9, strike_round 4, strike_tier tier4, strike_count 1, max_new 120, numerator 1, denominator 2, lead_from 5,
lead_margin 0) with early_gun true (gun1 (10,1) + tier4 in round 4, 290 gold) and false. Results (HP difference, end round):
early_gun=true: v34 +970 (r14), v36 +815 (r15), v38 +815 (r15); early_gun=false: v34 +1015 (r16), v36 +970 (r14), v38 +970 (r14).
The round-4 tier4 lands once on the fortress (60) and the fortress's mandatory defence stops it from round 5; the counter then
hands off to its public-model defence (built for the lead's P5TNUBM, not for the fortress) and is killed by the fortress's flood in
rounds 14-16. So the counter that converts the lead's two nominees into 755:740 losses is a comfortable win for every fortress
version; it exploits the nominees' passive window, which the fortress does not have (its mandatory defence against the visible
roster is unconditional).

## 2026-10-31T16:09Z  Eighth astra review (astra/v38-review/answer.md): two cap-specific traps, two new strikers beating every version, a bookkeeping defect

Claims (astra's engine games, both seats; reproduced here as `bots/defense/counter_astra38.py` variants A-D, measured in x160):
A. Round-5 gun / round-7 threshold trap (factories 5/4/8/14/24/43, two tier5 per round in rounds 7-10, a 44-step gun guard in round 9,
   a 74-step S 1510 lock in round 11): v38 -170, v36 +410. Mechanism: at round 5 v38's cap buys the gun3 (9,5) (and 7 factories) where
   v36 buys 17 factories; at the round-7 decision (opponent 1497 gold, 98 factories, matching in both) the worst sampled damage on
   v38's map is 280 (< lethal_share 0.4 x 800 = 320) and on v36's 364 (>= 320), so v36 buys the emergency plan (four gun3, 804 gold)
   and takes nothing while v38 buys 39 factories and takes 280. The early gun lowers the sampled threat just below the emergency
   threshold without covering the actual pair. Ablation: v38 with eco_match_insure_cap=0 reproduces v36 exactly.
B. Three-premium trap (the opponent builds its own guns and walls in rounds 5-6 so that its visible gold stays at 498 / 650 / 907, the
   range in which a full 200-gold plan against its affordable compositions exists; then 45 factories, and tier5 + tier5 + tier4 +
   tier1 in round 8; lock in rounds 9-10): v38 buys gun3 (9,5), (10,1), (10,5) in rounds 5, 6, 7 and enters round 8 with 929 gold and
   58 factories against v36's 1342 and 86; v38's insurance budget finds no full plan, one tier5 and one tier4 land (200), v36
   repairs for 400 and takes nothing: v38 -150, v36 +190.
C. Guarded round-7 striker (gun1 (10,1) in round 4, 94 factories by round 6, two tier5 per round in rounds 7-10, round-9 gun3 pair
   stopping a lone tier5, S 1520 lock in round 11): -345 against v36 AND v38 (380:725); the fortress takes 280 + 140 and deals 75.
D. Screened round-8 striker (splash guards (10,1) r4 and (1,0) r6, 86 factories, nothing in round 7, two tier4 AHEAD of three tier5
   in round 8 (2470 gold), S 1560 lock in round 9): -385 against both (380:765). The two tier4 screens absorb the frontmost-target
   guns so all three tier5 land (420) where three tier5 alone or tier5-first orders leak two (280); controls with zero or one
   leading tier4 end -245.
E. Code: the cap block has no non-matching suppression bug (source deduction); pre-existing defect: covered_full = bool(spec) is
   False when the map already covers every composition (plan_defense returns [] in both cases), so the history insurance can run
   needlessly; no measured loss attributed. Fixed as option covered_fix in the live module (coverage from the exact leak when the
   planner returns nothing).
Assessment: A and B are adversarial schedules built against v38's cap; C and D are new model-free strikers of the handoff class that
beat the whole fortress family (and, by their mechanism, any policy that cannot stop two tier5 per round from round 7 or a screened
three-tier5 wave in round 8 while matching the economy). x160 measures A-D against v34, v36, v37, v38, and v38-live variants
(lethal_share 0.3, covered_fix) to see whether the A knife-edge is the threshold.

## 2026-10-31T16:13Z  x160: astra's A-D against every fortress version; lethal_share 0.3 repairs A and C on v38

`runs/defense/x160_astra38` (48 games, both seats identical, logs kept; L1 = live v38 settings + lethal_share 0.3, L2 = v38 settings +
covered_fix):

| schedule | v34 | v36 | v37 | v38 | L1 (lethal 0.3) | L2 (covered_fix) |
| --- | --- | --- | --- | --- | --- | --- |
| A round-5 gun / threshold trap | +430 | +410 | +110 | -170 | +110 | -170 |
| B three-premium trap | +65 | +190 | +190 | -150 | -150 | -150 |
| C guarded round-7 striker (2 tier5/round r7-10) | +330 | -345 | +75 | -345 | +75 | -345 |
| D screened round-8 striker (2 tier4 + 3 tier5) | -233 | -385 | -245 | -385 | -245 | -385 |

Astra's values for v36 and v38 are reproduced exactly. New facts: v34 beats A, B and C (its speculative insurance and the lethal
rule fire where the matching versions skip; D beats it by 233); covered_fix changes nothing here (as expected, it only removes
needless history insurance); lethal_share 0.3 (emergency insurance when the worst sampled threat reaches 240 = 0.3 x 800 instead
of 320) turns A (-170 -> +110) and C (-345 -> +75) into wins and softens D (-385 -> -245), because two tier5 (280) now cross the
threshold at the round-7 decision; B (-150) is the cap trap and is unchanged. The lethal rule is a permanent trigger (unlike v37's
pre-strike one), so the hoarder risk must be measured on the GROWERS pool before any freeze: x161 (L3 = v38 settings + lethal 0.3 +
covered_fix on the 71 GROWERS) and x162 (L3 on the striker/standard set plus the hoarders and A-D) are running.

## 2026-10-31T16:21Z  x161, x162: lethal_share 0.3 + covered_fix on v38's settings (L3); v39 frozen for its regression

x161 (`runs/defense/x161_l3_growers`, L3 = live eco_match + race_kill + cap 200 + lethal_share 0.3 + covered_fix on the 71 GROWERS):
142-0-0, min +240, mean +789 (v38: 142-0-0, min +100, mean +703). x162 (`runs/defense/x162_l3_std`, 54 games, both seats identical;
v38 in brackets): handoff g5 H10 -105 / H11 -79 (same); g6 H10 -105 (-525), H11 -105 (+35), H12 +95 (+315), H13 +575 (+315); g7 H10
-105 (-219), H11 -79 (+227); staged +593 (+315), screened +975 (+315); astra33 +413 (+704), astra28 -65 (same); early-gun +110 (-215);
guarded round-5 tier4 striker -7 (same); econ17 +5, timing +65, guard 0, econ v2 +10, lead v4 0 (same); eco6_t5 +1240 (+566),
eco_then_flood +1100 (+1000); hoarders B +350 (+210), G +235 (+135); astra A +110 (-170), B -150 (same), C +75 (-345), D -245 (-385).
Reading: the lower emergency threshold (240 = two tier5 minus a margin) makes the fortress insure in round 7 against a striker whose
gold affords two tier5, which repairs the early-gun grower, A, C, both H10 columns of growth 6 and 7 and softens D, at the price of the
H11 wins of growth 6 and 7 (the round-7 insurance costs the round-10 race, as with v37) and smaller margins against astra33 and g6 H12.
On the 27 opponents of x162 L3 has three new wins and two new losses against v38; on the GROWERS pool it is strictly better. Unlike
v37's pre-strike rule it does not lose the hoarders (its trigger is the sampled threat on my current map, which the insurance
itself lowers, so it fires once rather than every round, and it does not fire against one-tier5-per-round growers before their
first copy is visible).
Frozen as v39 = v38 + lethal_share 0.3 + covered_fix (`bot_research.bots.defense.frozen.v39.fortress:@make`; fortress.py sha256
3c2159edcb0dcb64986f846bf39e9c5b278e02ab8f3b46e529321753a7459e08; other files identical to v34-v38). Regression queue_az (after
queue_ay): x163 strikers, t68 tuning plain+asym, x164 STRONG, x165 scripted econ, x166 forecaster, t69 mirror+eco, x167 GROWERS, x168
PUNISH, x169 hoarders + A-D. v38 stays the recommendation until it is read; v39 replaces it only if at least v38 on every pool by
W-D-L (the H11 trade is accepted only if the pool totals do not fall).

## 2026-10-31T16:27Z  For the lead (16:24Z request): tables of this lane's frozen bots against best_v9e

Both seats, standard start and the four scripted openings mirror:1:2, asym:3:2, mirror:22:3, asym:23:2, opponent
`bot_research.experiments.lead.frozen.best_v9e:decide`:
- frozen v34 and v35: `runs/defense/x127_v34_vs_best9e` (notes 13:14Z): standard -5 / -5; mirror:1:2 +3530; asym:3:2 +2380 / +867 (v35
  +1567); mirror:22:3 -840; asym:23:2 -6575 / -2225 (v35 -3765): 4W-0D-6L each.
- frozen v36, v37, v38: `runs/defense/x158_vs_lead` (notes 15:57Z, table there): standard -5 / -5 for all three; v36 and v38 identical to
  v34 on the scripted openings except asym:23:2 (-3765 / -6575); v37 worse (mirror:22:3 -1960, asym:3:2 +840 / +27).
- frozen v39: `runs/defense/x170_v39_vs_lead` (queued after the v39 regression; both seats, same five starts, plus P5TNUBM).
Standard-start summary against best_v9e: every fortress version loses by exactly 5, the blind round-1 exchange (best_v9e's three
tier1 against the fortress's two; neither side lands anything afterwards). Also relevant for the report: x113 (v29 / v33 vs best_v9b).

## 2026-10-31T16:36Z  v39 regression complete: a trade against v38 by W-D-L, so v38 stays the recommendation; v39 is the documented alternative

Frozen v39 (= v38 + lethal_share 0.3 + covered_fix; fortress.py sha256 3c2159edcb0dcb64986f846bf39e9c5b278e02ab8f3b46e529321753a7459e08),
both seats, 0 rejected actions, 0 bot errors; v38 values in the last column.

| run | pool | v39 | v38 |
| --- | --- | --- | --- |
| t68 | tuning, standard + asym:3:2 (104) | 101-3-0 (eco_then_flood switch 11 tier5 under asym:3:2 seat 1: both bases destroyed, as v37) | 102-2-0 |
| t69 | tuning, mirror:1:2 + eco:2 (104) | 100-4-0 | 100-4-0 |
| x164 | STRONG + lead v4 (26) | 24-2-0 | 24-2-0 |
| x165 | econ17 + econ15 leak, 4 scripted openings (16) | 14-0-2 (econ17 asym:23:2 seat 1 -2785 instead of the both-destroyed draw) | 14-1-1 |
| x166 | exact forecaster, 3 timings (6) | 0 / 0 / 0 | -190 / 0 / 0 |
| x163 | strikers + standard counters (48; 24 opponents) | 15W-2D-7L: handoff g5 -105/-79/+367/+453, g6 -105/-105/+95/+575, g7 -105/-79/+227/+813 (H10..H13); staged +593, screened +975; astra33 +413; early-gun +110; eco6_t5 +1240; eco_then_flood +1100; econ17 +5; timing +65; astra28 -65; guard 0; econ v2 +10; lead v4 0 | 16W-2D-6L (g6 H11 +35, g7 H11 +227 won; early-gun -215 lost; g6 H10 -525, g7 H10 -219) |
| x167 | GROWERS (142) | 142-0-0, min +240, mean +789 | 142-0-0, min +100, mean +703 |
| x168 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x169 | hoarders G/G15/B/B15, astra A/B/C/D, timing, guarded tier4 strikers (22) | G +235, B +350, A +110, B -150, C +75, D -245, timing +65, tier4 strikers -7 | G +135, B +210, A -170, B -150, C -345, D -385, +65, -7 |

By the rule stated before the run (replace v38 only if at least v38 on every pool by W-D-L), v39 fails: one win becomes a draw on the
tuning pool, one draw becomes a loss on the scripted openings, and on the striker set it trades the two H11 wins for the early-gun
win (15-2-7 against 16-2-6). It gains A and C (astra's schedules against v38 and against the whole family), the forecaster's
round-7 tier4 (0 instead of -190), both H10 columns (-105 instead of -525 / -219) and the GROWERS margins. The trade is the
same lever each time: insuring one round before a possible two-tier5 strike (lethal threshold 240) saves 140-420 HP when the
strike comes and costs the round-10 race (and a tuning win against a late hoarder) when it does not. Neither setting dominates;
the report should present v38 (recommended: more wins on the development pools) and v39 (alternative: smaller worst cases
against the handoff strikers, the exact forecaster and astra's A/C) as complementary, with v34 as the poking insurer for pools
without model-free strikers. FINAL RECOMMENDATION unchanged: frozen v38 (15:52Z).

## 2026-10-31T16:38Z  Shift-3 summary (13:57Z-): what changed, what was measured, what is recommended

Starting point: frozen v34 (recommendation of shift 2) and v35 (eco_match alternative). This shift measured the fortress family
against hrt-w3's model-free striker counters (guard_handoff, staged and screened guards), ran three astra reviews with engine-verified
schedules, and produced four frozen versions (v36-v39) with full regressions. Every number below is from the unchanged engine, both
seats, standard start unless stated; run names are directories under bot_research/runs/defense/ (index below).

1. Findings about the game (empirical unless marked).
- Economy compounds at 75 percent per round (factory 20, income 15 from the purchase round): any gold not in factories during rounds
  2-6 against a passive grower is a loss of about 3-4x that gold by round 8. Pokes against a passive grower are therefore worth it only
  when the grower never adds a guard; one splash at round 4 (S 50) kills tier1/tier2 pokes and turns v34's small poke wins (+8 timing,
  +130 early-gun) into -650 to -800 losses (x128, x132). No gate on the current map can see a guard built the same or the next round.
- The striker class (86 factories by round 6, two tier5 per round from round 7, then a lock) cannot be insured against before the strike
  (a zero-leak map against two tier5 costs about 2400 gold; fortress holds 750-1300) and cannot be out-grown from the fortress opening.
  Astra's engine-verified schedule (14:54Z) holds 800 HP against it only with a matched economy (83 factories) and 1030 gold of gun3 in
  round 7, before the hidden strike. Growth-6 and growth-7 strikers are indistinguishable at the round-7 decision (identical
  observations; astra review 7), so insuring in round 7 is a bet, not an inference.
- A tier4-level first strike (timing bot, econ17, guarded round-5 tier4 strikers) is stopped by ONE gun3 (200 gold) on the fortress's
  early map (exact planner, 15:08Z; hrt-w3 found the same for the lead's bot); the eco_match family lost those games only because
  matching skipped all speculative insurance. The cap option (v38) buys exactly that plan.
- Harness caveat for the lead: the observation carries each player's name = the full bot spec (engine.py snapshot); this lane's bots
  never read it (16:09Z).
2. Versions and results (regressions: tuning plain+asym 104, mirror+eco 104, STRONG 26, scripted econ 16, exact forecaster 6, strikers
   48, GROWERS 142, PUNISH 34):
- v36 = v34 + eco_match + race_kill: 102-2-0, 100-4-0, 22-2-2, 14-1-1, forecaster -190/0/0, GROWERS 142-0-0, PUNISH 32-0-2; beats
  astra33 +562, staged +315, screened +315, handoff H11-H13; loses H10 (-525 at growth 6), econ17 -81, timing -47 (14:50Z).
- v37 = v36 + race fixes + pre-strike big_threat 200: REJECTED (GROWERS 136-0-6, hoarder effect; astra's guarded hoarder G -55) (15:26Z).
- v38 = v36 + race fixes + eco_match_insure_cap 200: 102-2-0, 100-4-0, 24-2-0, 14-1-1, -190/0/0, GROWERS 142-0-0 (mean +703), PUNISH
  32-0-2; econ17 +5, timing +65, astra33 +704; strikers as v36. FINAL RECOMMENDATION (15:52Z). Known counters: handoff H10 (-105 /
  -525 / -219 at growth 5/6/7), g5 H11 -79, astra's A -170 and B -150 (cap traps), C -345 and D -385 (strikers that beat every version),
  forecaster tier4 r7 -190, astra28 -65, early-gun -215, guarded tier4 strikers -7, asym:23:2 seat 1 scripted map.
- v39 = v38 + lethal_share 0.3 + covered_fix: a W-D-L trade (101-3-0, 100-4-0, 24-2-0, 14-0-2, 0/0/0, GROWERS 142-0-0 mean +789, PUNISH
  32-0-2; strikers 15-2-7 with H10 -105 everywhere and H11 lost; A +110, C +75, D -245): documented alternative (16:36Z).
3. Counter-strategy cycle (the prompt's section 5): hrt-w3's guard_handoff/staged guards beat v34 (-653/-793) -> v35/v36 (economy
   matching) beat them except H10/H11 -> astra's astra33-style guard with a single visible tier1 is beaten too -> astra's hoarders G/B
   beat v37's pre-strike insurance -> astra's A/B beat v38's cap -> lethal 0.3 (v39) beats A/C but loses the H11 races; C and D (two
   tier5 per round with a cheap gun guard; two tier4 screens ahead of three tier5) beat every fortress version by 345/385 and are the
   open frontier, together with H10. All counters are reproducible bots: bots/counters/guard_handoff.py etc. (hrt-w3), this lane's
   counter_astra28/33/37/38.py and counter_earlygun.py options.
4. Results against the team's bots: on the standard start every fortress version LOSES to best_v9e (the frozen team candidate) by 5 (the
   blind round-1 exchange: best_v9e's three tier1 against the fortress's two) and draws the lead's P5TNUBM 0-0 (wording corrected at
   16:43Z after hrt-w3's 16:38Z caution; the x158/x170 tables were always stated from the fortress's side); on the four scripted openings the fortress wins the two lighter ones by 1147-3530 and
   loses the two heavily obstructed ones (x127, x158, x170). The fortress family beats the whole GROWERS pool (142-0-0 for v34, v36, v38,
   v39) where best_v9e is 66-0-76, and hrt-w3's guarded round-4 strike (which beats both lead nominees) by 815-1015 (x159).
5. Reproduction (from the project root, PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp"):
    .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.defense.frozen.v38.fortress:decide --bot-b td_bots.protocol:idle --output bot_research/runs/defense/<new>.jsonl
    .venv/bin/python -B -m bot_research.harness.tournament --name <name> --out-dir bot_research/runs/defense/<name> --jobs 3 --candidates bot_research.bots.defense.frozen.v38.fortress:@make --opponents <specs> [--scenarios none asym:3:2] --keep-logs losses
   Opponent specs used in this shift are in the notes entries and in the queue scripts of the lane directory (scratch/queue_a[h-z].sh,
   queue_ba.sh); pools: bot_research/experiments/economy/opponents_tuning.txt, experiments/lead/pools.py (GROWERS, PUNISH).
   Run-directory index, shift 3 (all under bot_research/runs/defense/; results.jsonl + summary.md each; logs kept as noted):
   - x128_v34_handoff: frozen v34/v35 vs guard_handoff H10-H16, staged [4,6], screened r9 (36 games, logs all)
   - x129_options_std: live options EMP / RK / EMP&RK / EM&RK vs 14 standard opponents (112, logs all)
   - x130_race2_std: relaxed race condition (26, logs all); x131_timing_trace: v34/v35/EM&RK vs economy.timing (6, logs all)
   - x132_frac_std: poke fraction gate 0.7/0.9 (60, logs all)
   - x133_v36_std, t62_v36_tuning, t63_v36_mirror, x134_v36_strong, x135_v36_econ, x136_v36_forecast, x137_growers (v34 and v36), x138_punish (v34 and v36): v36 regression
   - x139_bigthreat: A / BT140 / BT280 (108); x140_lead_strikers: lane strikers vs P5TNUBM, P4TNUB, v36 (48); x141_prestrike: PS200/PS280 (76)
   - x142_v37_std, t64_v37_tuning, x143_v37_strong, x144_v37_econ, x145_v37_forecast, t65_v37_mirror, x146_v37_growers, x147_v37_punish: v37 regression
   - x148_insurecap: cap 200/300 on v37 settings (84); x149_v36cap: cap 200/120 on v36 settings (84); x150_astra37: hoarders G/B/G15/B15 vs v34/v36/v37/cap (32, logs all)
   - x151_v38_std, t66_v38_tuning, x152_v38_strong, x153_v38_econ, x154_v38_forecast, t67_v38_mirror, x155_v38_growers, x156_v38_punish, x157_v38_hoarders: v38 regression
   - x158_vs_lead: v36/v37/v38 vs P5TNUBM and frozen best_v9e, standard + 4 scripted openings (60); x159_guarded_r4: hrt-w3's guarded round-4 strike vs v38/v36/v34 (12, logs all)
   - smoke_frozen_v36_vs_idle.jsonl, smoke_frozen_v38_vs_idle.jsonl (runner form)
   Opponent pools used: bot_research/experiments/economy/opponents_tuning.txt (26); hrt-w1/scratch/strong_pool.txt (STRONG, 13 + lead v4); growers_pool.txt and punish_pool.txt (= experiments/lead/pools.py GROWERS and PUNISH, 71 and 17 specs).
   - x160_astra38 (A-D vs v34/v36/v37/v38 and two live variants, logs all); x161_l3_growers, x162_l3_std (L3 = v39 settings live);
     x163_v39_std, t68_v39_tuning, x164_v39_strong, x165_v39_econ, x166_v39_forecast, t69_v39_mirror, x167_v39_growers, x168_v39_punish,
     x169_v39_hoarders (v39 regression); x170_v39_vs_lead (v39 vs best_v9e and P5TNUBM).
   Astra question/answer files: hrt-w1/astra/{v36-review,v37-exploits,v38-review}/ (question.md, answer.md, review/ with engine records).

## 2026-10-31T16:40Z  x170: frozen v39 against best_v9e and P5TNUBM (completes the 16:27Z table for the lead)

`runs/defense/x170_v39_vs_lead` (20 games; (HP difference, end round) for fortress seat 0 / seat 1): best_v9e standard -5 / -5; P5TNUBM
standard 0 / 0; both lead bots (econ20 foreign policy on scripted maps): mirror:1:2 +3530 / +3530 (r33); asym:3:2 +2800 (r37) / +2547
(r44) (v38: +2380 / +1147); mirror:22:3 -6300 / -6300 (r21) (v38: -840 / -840 at round 13); asym:23:2 -6575 / -6285 (v38: -3765 / -6575).
On the two heavily obstructed openings v39's lower emergency threshold buys partial insurance that cannot reach zero leak on those maps
and the capacity race is then lost by more; this confirms the 16:36Z decision (v38 recommended, v39 alternative). Standard-start
summary against the team's bots is unchanged for every fortress version: -5 to best_v9e (round-1 exchange), 0-0 to P5TNUBM.

## 2026-10-31T16:48Z  x171: matching from the first out-growth (eco_match_ratio 1.0) turns the striker class into wins; v40 queued

Hypothesis (from astra's 800:770 schedule, 14:54Z): the fortress loses the striker races because of the gold it spends in rounds 2-6
before matching starts (the round-3 splash and tier1, the round-5 speculative gun: about 300 gold at round 7 after compounding), and
matching should start as soon as the opponent out-grows me at all. Test: eco_match_ratio 1.0 (matching when the opponent owns at least
my factories + 2 instead of 1.5 x mine + 2), on v38's settings (L4) and on v39's (L5 = plus lethal_share 0.3).
`runs/defense/x171_ratio_std` (104 games, both seats identical; v38 in brackets):

| opponent | L4 (ratio 1.0) | L5 (ratio 1.0 + lethal 0.3) |
| --- | --- | --- |
| handoff g5 H10 / H11 | +388 / +694 (kill r10) [-105 / -79] | +336 / +842 |
| handoff g6 H10 / H11 / H12 | +336 / +1036 (r10) / +1036 (r10) [-525 / +35 / +315] | +170 / +590 / +590 |
| handoff g7 H10 / H11 | +336 / +1036 [-219 / +227] | +310 / +870 |
| staged guard / screened guard | +1088 / +1036 (r10) [+315 / +315] | +450 / +590 |
| astra33 / astra28 | +740 / -65 [+704 / -65] | +413 / -65 |
| astra A / B / C / D | -5 / +320 / +838 (r10) / +1036 (r10) [-170 / -150 / -345 / -385] | +500 / +320 / +730 / +870 |
| hoarders G / B | +396 (kill r8) / +45 [+135 / +210] | +310 / +390 |
| early-gun grower / guarded round-5 tier4 striker | +35 / -43 [-215 / -7] | +90 / -43 |
| econ17 / timing / guard_continuation | +5 / -115 / -65 [+5 / +65 / 0] | +5 / -115 / -65 |
| eco6_t5 / eco_then_flood / econ v2 / lead v4 | +556 / +802 / +10 / 0 [+566 / +1000 / +10 / 0] | +820 / +975 / +10 / 0 |
| totals over the 26 opponents (52 games) | 40W-2D-10L, HP sum +22952 | 42W-2D-8L, +19786 |

v38 on the same 26 opponents: 30W-2D-20L. Every handoff striker (H10 included, at every growth), both guards, astra's C and D (which
beat every earlier version by 345/385) and the hoarders are now wins, most of them kills in round 10: with matching from round 2 the
fortress enters round 7 with about the striker's factory count, its mandatory defence at round 8 stops the visible roster, and the
race rule's flood in rounds 9-10 lands before the striker's lock. Costs: timing -115 (the whole round-5 package lands: with the
round-3 splash and gun gone, the cap plan at round 5 needs 334 gold and the fortress holds less), the guarded round-5 tier4 striker
-43, guard_continuation -65 (its round-8 tier4 lands once), early-gun down to +35, astra A -5 for L4 (L5 wins it +500). The cost
class is the same small first strike as before, now 43-115 instead of 7-47; the gain class is 300-1400 per game.
v40 = v38 + eco_match_ratio 1.0 (lethal_share 0.4 kept) is queued for freezing and its full regression (queue_bc: t70 tuning, x173
STRONG, x174 scripted econ, x175 forecaster with five timings incl. tier4 r5 and tier3 r4, t71 mirror+eco, x176 PUNISH; GROWERS is
x172 on the live settings). The risk to measure is the answering economy bots of the tuning and STRONG pools: matching now starts
against any opponent with two more factories than the fortress, so the speculative insurance is skipped against most of them in
rounds 2-7 and only the one-gun3 cap and the mandatory defence remain.

## 2026-10-31T16:52Z  x172: the ratio-1.0 variants on the GROWERS pool; v40 frozen

`runs/defense/x172_ratio_growers` (284 games): L4 (v38 + eco_match_ratio 1.0) 142-0-0, min +100, mean +724 (v38: min +100, mean +703);
L5 (+ lethal_share 0.3) 142-0-0, min +380, mean +814. No hoarder effect: matching from round 2 only removes spending, it adds none.
v40 = v38 + eco_match_ratio 1.0 frozen by the queue (`bot_research.bots.defense.frozen.v40.fortress:@make`; fortress.py sha256
fdc2c22ee2059600 (full hash in frozen/v40/SHA256SUMS); defaults verified: eco_match True, ratio 1.0, race_kill True, cap 200,
lethal_share 0.4, covered_fix True, big_threat None). Regression running: t70 tuning plain+asym, x173 STRONG, x174 scripted econ, x175
forecaster (five timings, now including tier4 r5 and tier3 r4 for the early-strike class), t71 mirror+eco, x176 PUNISH.

## 2026-10-31T17:03Z  v40 regression, first results: tuning equal, STRONG and scripted one down each, forecaster two down; the mirror:1:2 trace

Frozen v40 (= v38 + eco_match_ratio 1.0; fortress.py sha256 fdc2c22ee20596004b68f715311c625eeda531eddec3220e66a1f559290be46f), both seats:
- t70 tuning plain+asym: 102-2-0 (= v38).
- x173 STRONG: 22-2-2 (v38 24-2-0): economy.timing -115 in both seats (expected from x171), lead v4 0-0.
- x174 scripted econ: 13-1-2 (v38 14-1-1): econ17 8-0-0 (asym:23:2 seat 1 now +1982, was a both-destroyed draw); econ15 leak: asym:23:2
  seat 0 both destroyed (was +1140), seat 1 +1220 (was -875), mirror:1:2 -1001 / -1001 (was +829 / +829), asym:3:2 and mirror:22:3 won.
- x175 exact forecaster of v40, five timings: tier3 r4 0, tier4 r5 -60, tier4 r7 -240 (v38 -190), tier5 r8 -140 (v38 0), tier5 r10 0.
Trace of the new mirror:1:2 loss (x174 log 00009, fortress seat 0): on the scripted 22-step mirror map the fortress never lengthens its
route (S stays 180-240 with up to 13k gold; the re-planner's layout gave no walls here) and grows to 139 factories by round 9 (v38 grew
less because its speculative insurance bought guns in rounds 5-7); in round 14 the mass-finish rule buys 20 tier5 (13000 gold) against
econ15's S 760 map after the robust check against econ15's estimated same-round response; econ15's actual response (2543 gold of
defence in that round, insuring against the fortress's visible 13k gold) stops all 20 copies, and in round 15 econ15's own flood lands
980 on the S 220 map. So the loss is a mass-finish misjudgment on a map where the fortress has no lock (the capacity regime of
scripted openings, known since shift 2), made likelier by v40's bigger economy. The forecaster losses are the exact-model adversary
exploiting the skipped insurance in rounds 5-8. Remaining runs: t71 mirror+eco, x176 PUNISH; then v41 = v40 + lethal_share 0.3
(queue_bd) for the same regression (x171/x172 gave it 42-2-8 and GROWERS min +380 on the live module).

## 2026-10-31T17:06Z  v40 regression complete; FINAL RECOMMENDATION REVISED: frozen v40 (v38 + eco_match_ratio 1.0)

Frozen v40, all runs both seats, 0 rejected actions, 0 bot errors (v38 in the last column):

| run | pool | v40 | v38 |
| --- | --- | --- | --- |
| t70 | 26 tuning opponents, standard + asym:3:2 (104) | 102-2-0 | 102-2-0 |
| t71 | 26 tuning opponents, mirror:1:2 + eco:2 (104) | 100-4-0 | 100-4-0 |
| x173 | STRONG + lead v4 (26) | 22-2-2 (economy.timing -115) | 24-2-0 |
| x174 | econ17 + econ15 leak, 4 scripted openings (16) | 13-1-2 (econ17 8-0-0; econ15 leak mirror:1:2 -1001, asym:23:2 draw / +1220) | 14-1-1 |
| x175 | exact forecaster of the candidate, 5 timings (10) | tier3 r4 0, tier4 r5 -60, tier4 r7 -240, tier5 r8 -140, tier5 r10 0 | (3 timings) -190, 0, 0 |
| x176 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x171 | strikers, standard counters, hoarders, astra A-D (26 opponents, 52; live module = v40) | 40-2-10: every handoff (H10 at growth 5/6/7 +388 / +336 / +336; H11-H12 kills in round 10), staged +1088, screened +1036, astra C +838, D +1036, B +320, hoarders G +396, B +45, early-gun +35, astra33 +740; losses timing -115, guard_continuation -65, astra28 -65, guarded round-5 tier4 striker -43, astra A -5 | 30-2-20 (losses: all H10, g5 H11, early-gun, A, B, C, D, astra28) |
| x172 | GROWERS (142; live module = v40) | 142-0-0, min +100, mean +724 | 142-0-0, min +100, mean +703 |

Decision. The rule stated at 16:52Z (replace v38 only if at least v38 on tuning, mirror, STRONG and scripted by W-D-L) is not met
literally: STRONG loses one opponent (economy.timing, -115 in both seats), the scripted openings lose one game (econ15 leak under
mirror:1:2, a mass-finish misjudgment on a lockless map, 17:01Z), and the exact forecaster of v40 lands two more timings. Against that,
v40 removes every catastrophic loss of the fortress family to the model-free striker class: all twelve handoff settings, both guards,
astra's C and D and the hoarders are wins (most by kill in round 10), where v38 lost ten of the 26 opponents of x171, several by 345
to 525. Counting games over everything measured for both (x171, x172, t70, t71, x173, x174, x175 three common timings, x176),
v40 is 452W-14D-16L against v38's 440W-15D-27L; the losses v40 adds are bounded (43 to 240 HP; -1001 on one scripted map) and the
losses it removes are 345 to 525 and include the counters that also beat the team's best bots (handoff H10, C, D). I therefore
revise the recommendation to v40 and record the deviation from the pre-stated rule here: the rule weighed pools equally, and the
striker pool is where the family (and the team's bots) had their only unsolved class.
FINAL RECOMMENDATION of this lane: frozen v40 (`bot_research.bots.defense.frozen.v40.fortress:@make`; runner form
`...frozen.v40.fortress:decide`). SHA-256 (frozen/v40/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
    922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
    58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
    b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
    fdc2c22ee20596004b68f715311c625eeda531eddec3220e66a1f559290be46f  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Decision rules of v40 = those of v38 (15:52Z paragraph) with one change: economy matching starts as soon as the opponent owns at least
my factories + 2 (instead of 1.5 x mine + 2), i.e. from round 2 against any grower; while matching (rounds <= 7) the fortress buys
only the layout walls, the mandatory zero-leak defence against the visible roster, a full zero-leak plan against the affordable
compositions when it costs at most 200 gold, and factories; the emergency rule (lethal_share 0.4), the finish rule and the race rule
are unchanged; after round 7 the full insurer resumes.
Known failures of v40 (verified, both seats): economy.timing -115 and the guarded round-5 tier4 strikers -43 (a tier4 package in round
5 before the cap plan is affordable); guard_continuation -65 and astra28 -65 (one hidden tier4 of a drip); astra's A -5; the exact
forecaster of v40 at tier4 r5 -60, tier4 r7 -240, tier5 r8 -140; econ15 leak under mirror:1:2 -1001 (mass finish answered by a
full-gold insurer on a lockless scripted map) and asym:23:2 seat 0 both destroyed; 0-0 against pure turtles and lead v4; -5 against
best_v9e on the standard start (round-1 exchange, x158 pattern expected to hold; not re-run for v40). Alternatives: v38 (15:52Z) for
pools of answering economy bots, early strikers and exact forecasters; v39 (16:36Z); v34 (12:43Z) the poking insurer. v41 = v40 +
lethal_share 0.3 is under regression (queue_bd): on the live module it was 42-2-8 on the x171 set and GROWERS min +380.

## 2026-10-31T17:21Z  v41 regression complete: at least v40 on every pool, better on three; FINAL RECOMMENDATION REVISED: frozen v41

Frozen v41 = v40 + lethal_share 0.3 (= v34 + eco_match True, eco_match_ratio 1.0, race_kill True with the review-6 fixes,
eco_match_insure_cap 200, covered_fix True, lethal_share 0.3). All runs both seats, 0 rejected actions, 0 bot errors; v40 in the last
column.

| run | pool | v41 | v40 |
| --- | --- | --- | --- |
| t72 | 26 tuning opponents, standard + asym:3:2 (104) | 102-2-0 | 102-2-0 |
| t73 | 26 tuning opponents, mirror:1:2 + eco:2 (104) | 100-4-0 | 100-4-0 |
| x177 | STRONG + lead v4 (26) | 22-2-2 (timing -115) | 22-2-2 |
| x178 | econ17 + econ15 leak, 4 scripted openings (16) | 15-1-0 (econ15 leak mirror:1:2 +959; asym:23:2 seat 0 both destroyed) | 13-1-2 |
| x179 | exact forecaster of the candidate, 5 timings (10) | tier3 r4 0, tier4 r5 -60, tier4 r7 0, tier5 r8 0, tier5 r10 0 | 0, -60, -240, -140, 0 |
| x180 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x171 (L5) | strikers, counters, hoarders, astra A-D (26 opponents, 52; live module with v41's exact parameters) | 42-2-8: all handoffs (g5 +336 / +842, g6 +170 / +590 / +590, g7 +310 / +870), staged +450, screened +590, astra33 +413, A +500, B +320, C +730, D +870, hoarders G +310 / B +390, early-gun +90; losses timing -115, guard -65, astra28 -65, guarded tier4 striker -43 | 40-2-10 (A -5, larger margins) |
| x172 (L5) | GROWERS (142) | 142-0-0, min +380, mean +814 | 142-0-0, min +100, mean +724 |
| x181, x182 | frozen v41 on the 26-opponent set plus hrt-w3's guarded round-4 strike; against best_v9e and P5TNUBM | running (queue_bf) | |

Smoke (runner form): frozen v40 and v41 vs idle, `runs/defense/smoke_frozen_v40_vs_idle.jsonl`, `smoke_frozen_v41_vs_idle.jsonl`:
player 0 wins in round 8 (800 : -13), as for every version since v29.
Decision by the rule stated at 17:06Z (replace v40 only if at least v40 on every pool by W-D-L): v41 equals v40 on tuning, mirror,
STRONG and PUNISH and is better on the scripted openings (15-1-0), the exact forecaster (one loss instead of three) and the striker
set (two more wins: astra A, and B of x171), with a higher GROWERS minimum. With ratio 1.0 the lower emergency threshold no longer
produces the hoarder draw/loss it produced on v39's settings (the fortress holds more gold when it fires, so the insurance is a full
plan, not a drain). FINAL RECOMMENDATION of this lane: frozen v41 (`bot_research.bots.defense.frozen.v41.fortress:@make`; runner
form `...frozen.v41.fortress:decide`, stateful per player, renewed in round 1). SHA-256 (frozen/v41/SHA256SUMS):
    a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
    ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
    abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
    922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
    58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
    b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
    3b69306d9b582b35ba3945643a6996ed0caf3abe88dfed1a9ebc8396cf02cfdd  fortress.py
    e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
    6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f  plan.py
    3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
    2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
    68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Decision rules of v41 = those of v40 (17:06Z) with the emergency threshold at 240 damage (lethal_share 0.3 x 800): when the worst
sampled affordable composition would deal 240 or more on my current map, the whole gold goes to the best (partial) defence plan,
also while matching; two tier5 (280) cross it, one tier5 (140) does not.
Known failures of v41 (verified, both seats): economy.timing -115 and the guarded round-5 tier4 strikers -43 (a tier4 package in
round 5 before the cap plan is affordable); guard_continuation -65 and astra28 -65 (one hidden tier4 of a drip); the exact forecaster
at tier4 r5 -60; econ15 leak asym:23:2 seat 0 both destroyed; 0-0 against pure turtles and lead v4; -5 against best_v9e on the
standard start (x182 pending). Alternatives: v40 (17:06Z, lethal 0.4: larger striker margins), v38 (15:52Z, ratio 1.5: for pools of
answering economy bots and early strikers; wins timing +65), v34 (12:43Z, the poking insurer).

## 2026-10-31T17:24Z  Addendum to the shift-3 summary (16:38Z): the final state after v39-v41

The summary of 16:38Z described v38 as the recommendation; the later entries changed it. Final state of this lane at 17:24Z:
- FINAL RECOMMENDATION: frozen v41 (17:21Z entry: spec, SHA256SUMS block, decision rules, regression table, known failures).
- Alternatives: v40 (17:06Z; lethal 0.4: larger striker margins), v38 (15:52Z; ratio 1.5: wins timing +65, loses the whole striker
  class), v39 (16:36Z), v36 (14:50Z), v34 (12:43Z; the poking insurer of shift 2). v37 rejected (15:26Z) and kept as evidence.
- The decisive change of the shift is eco_match_ratio 1.0 (x171, 16:47Z): economy matching from the first out-growth instead of from
  1.5 x my factories + 2 turns every model-free striker of the handoff class (hrt-w3's 18 settings, astra's C and D, the hoarders)
  into wins while costing 43-115 HP against four early small strikers. Together with the one-gun3 insurance cap (15:08Z) and the lower
  emergency threshold it gives v41. The eco_match family's lesson is one sentence: against a passive grower every gold not in factories
  before round 7 is paid back three to four times at the strike, and the only insurance worth buying before the strike is visible is
  the one that costs one gun3.
- Counters found this shift (all reproducible bots): hrt-w3's guard_handoff / staged / screened guards (x128), astra's astra37 hoarders
  G/B (x150), astra's astra38 A-D (x160), counter_earlygun's tier4/guard variants (x140). Open against v41: the round-5 tier4
  package class (timing -115, guarded tier4 strikers -43, forecaster tier4 r5 -60) and the single hidden tier4 of drips (-65).
- Against the team's bots (x158, x170, x182 pending for v41): -5 to best_v9e on the standard start (round-1 exchange), 0-0 to
  P5TNUBM; scripted openings split 2-2 (light openings won by 1147-3530, obstructed ones lost).
- Astra review 4 of v41 asked at 17:24Z (astra/v41-review/); its findings go into a dated entry when they arrive.
Run index additions since 16:38Z: x160-x170 (16:38Z list), x171_ratio_std, x172_ratio_growers, t70_v40_tuning, x173_v40_strong,
x174_v40_econ, x175_v40_forecast, t71_v40_mirror, x176_v40_punish, t72_v41_tuning, x177_v41_strong, x178_v41_econ, x179_v41_forecast,
t73_v41_mirror, x180_v41_punish, x181_v41_std, x182_v41_vs_lead, smoke_frozen_v40_vs_idle.jsonl, smoke_frozen_v41_vs_idle.jsonl.

## 2026-10-31T17:28Z  x181: frozen v41 on the striker and standard set (29 opponents) reproduces the live results

`runs/defense/x181_v41_std` (58 games, both seats identical, 0 rejected actions, 0 bot errors): 48W-2D-8L. Every row equals x171's L5
column (the live module with v41's parameters), plus hrt-w3's guarded round-4 strike: +1510 (early_gun true, kill r15) / +1100 (false,
r13). Wins: handoff g5 H10 +336, H11 +842 (r11); g6 H10 +170, H11/H12/H13 +590 (r10); g7 H10 +310, H11 +870 (r10); staged +450,
screened +590; astra33 +413; astra A +500, B +320, C +730 (r10), D +870 (r10); hoarders G +310, B +390; early-gun +90; econ17 +5;
eco6_t5 +820; eco_then_flood +975; econ v2 +10. Draws: guard_continuation... no: guard_continuation -65 (loss), lead v4 0, and the
second draw is none (2 draws = lead v4 both seats). Losses: timing -115, guard_continuation -65, astra28 -65, guarded round-5 tier4
striker -43 (both seats each). This is the evidence base for the recommendation of 17:21Z on the frozen artifact itself.

## 2026-10-31T17:31Z  x182: frozen v41 against best_v9e and P5TNUBM (completes the lead's table; a caveat on scripted openings)

`runs/defense/x182_v41_vs_lead` (20 games; (HP difference, end round) for fortress seat 0 / seat 1; both lead bots give the same rows
because both play the econ20 foreign policy on scripted maps): best_v9e standard -5 / -5; P5TNUBM standard 0 / 0; mirror:1:2 +1555
(r32) / +1555; asym:3:2 +1255 (r34) / -4330 (r21); mirror:22:3 -6160 (r21) / -6160; asym:23:2 -2515 (r21) / -5858 (r22). Against the
lead's bots on the four scripted openings v41 is 3W-0D-5L per opponent (v38: 4W-0D-4L, x158: mirror:1:2 +3530, asym:3:2 +2380 / +1147,
mirror:22:3 -840, asym:23:2 -3765 / -6575). So v41 is worse than v38 in the scripted-opening capacity races against the econ20 policy
(the asym:3:2 seat-1 game flips from +1147 to -4330; the mirror:22:3 loss grows from -840 to -6160), which is the regime where no
fortress version has a lock and the game is decided by mass floods (x127 analysis, 13:14Z). On the standard start nothing changes
(-5 and 0-0). This caveat belongs to the recommendation: v41 is the stronger artifact on the standard start and on the economy bots'
scripted openings (x178 15-1-0), v38 on the scripted openings against the lead's econ20-based bots.
Summary table for the lead (standard start, both seats): every fortress version v34-v41 loses to best_v9e by exactly 5 (round-1
exchange) and draws P5TNUBM 0-0; scripted openings: x127 (v34/v35), x158 (v36/v37/v38), x170 (v39), x182 (v41).

## 2026-10-31T17:41Z  Ninth astra review (astra/v41-review/answer.md): two bait-guard-three-tier5 schedules beat v41 and v38; a planner cutoff defect

Claims (astra's engine games, both seats; reproduced here as `bots/defense/counter_astra41.py` variants A and B, measured in x183):
1. A (5 factories; three tier1 + 2 factories in round 2; splash (10,1) + 4 factories in round 3; 10; 16; gun1 (1,0) + 28 in round 6;
   nothing in round 7; three tier5 in round 8; a 52-step S 1530 lock in rounds 9-10) and B (same with the splash guard in round 4 and a
   second splash (1,0) in round 6; S 1550): v41 505:780 (-275) and 505:765 (-260); v38 identical. Two of the three round-8 tier5 land
   (280) after the bait's 15. At decision 7 against A the sampled worst damage on v41's map is 200 (< 0.3 x 785 = 235.5), so the
   emergency rule does not fire; at decision 8 it fires (420 sampled) and 904 gold of walls and splashes still leak two copies. Against
   B it fires in rounds 7 (240 sampled: 604 on four walls + three gun3) and 8 (280 sampled: 785 on five walls + thirteen splashes) and
   two copies still land.
2. Planner defect (plan.py, the gun pass): the gun search is allowed only when EVERY supplied composition has at most 120 minions; B's
   round-8 sample contains a 146-tier1 composition that the existing map (70 splash per copy) already stops completely, and that single
   composition disables all gun candidates. With that composition removed from the planner's input, the unchanged planner finds a
   785-gold plan (five walls, splash (10,1), gun3 (10,9), (11,8), (11,9), gun1 (10,10), (11,10), splash (7,9)) with 140 maximum damage
   over all twelve compositions and the actual attack: 645:765 instead of 505:765 in a restored-state engine round (a one-round
   diagnostic, not a full game; still a loss).
3. Placement: on the literal 20-wall map one gun3 is NOT a full plan against the round-5 package (26 leaks); the historical round-4 map
   already had the round-3 splash (1,3), and splash (1,3) + gun3 (9,5) (260 gold) is the verified repair; gun2 + gun1 (110) and two gun2
   (160) cannot kill the leading tier4 anywhere (maximum route damage 358 / 528 < 560), exhaustive over legal cells. No cheaper full plan.
4. Pure hoarder (5/4/8/14/24 factories, then nothing): three consecutive emergency purchases in rounds 6-8 (660 + 710 + 904), each
   covering its sample, then the fortress kills it 800:-85 in round 11: not a counter. The cap and the emergency branch are exclusive
   (one speculative call per round). The lethal threshold is 0.3 x CURRENT HP, not a fixed 240. A round-5 tier4 purchase sets the
   heavy-spend history and ends matching from decision 6, so "strike small, then lock, protected by matching" is not the mechanism;
   a saturated splash map prevents retaliation regardless.
Actions: counter_astra41.py written; x183 measures A/B against v41, v40, v38, v34; the gun-pass cutoff is to be made per composition
(skip the compositions the current map already stops before applying the 120-copy limit) in the live plan.py as an option, tested on
A/B and the striker set, and frozen as v42 only with a full regression (shift 4 if the time of this shift does not allow it).

## 2026-10-31T17:44Z  x183: astra's A/B reproduced against four versions; planner gun-pass fix implemented (live plan.py)

`runs/defense/x183_astra41` (16 games, both seats identical, logs kept): A: v34 -283, v38 -275, v40 -275, v41 -275; B: v34 -336, v38 -260,
v40 -260, v41 -260 (astra's values for v38/v41 reproduced exactly). The whole fortress family loses this bait-guard-three-tier5 class by
260-336: the round-2 three-tier1 bait makes the mandatory defence buy guns in rounds 3-4, the splash guards kill the pokes, and three
tier5 in round 8 (1950 of about 2000 gold) land twice against a map that the emergency rule starts building one round late.
Planner fix (live bots/defense/plan.py, flag GUN_PASS_SKIP_COVERED = True): in plan_defense the gun pass is now run per wall prefix on
the compositions the prefix map does not already stop (exact leak check per composition), the 120-copy limit applies to those only,
and the chosen plan is re-checked against every composition (guns and the pass's splashes are off-route, so a stopped composition
stays stopped). check_plan 30: simulator 0 mismatches, 4 zero-leak plans verified in the engine. x184-x186 (queue_bg) measure the live
module with v41's parameters and the fixed planner against astra's A/B, A-D, the hoarders, the 21-opponent striker/standard set and the
GROWERS pool; v42 is frozen only if nothing regresses.

## 2026-10-31T17:51Z  x184-x186: the planner gun-pass fix on v41's parameters; v42 frozen for its regression

Live module with v41's parameters and the fixed planner (GUN_PASS_SKIP_COVERED), both seats identical:
- x184 (`runs/defense/x184_gunfix_astra`, logs kept): astra41 A -135 (v41 -275), B -120 (-260): one tier5 fewer lands in round 8 (the
  gun pass now runs in the emergency round although a 146-tier1 composition is in the sample); astra38 A +500, B +320, C +730, D +870
  (unchanged); hoarders G +69 (v41 +310), B +205 (+390): still wins, smaller margins (the gun pass now spends on guns in rounds 6-7
  where v41 bought factories).
- x185 (`x185_gunfix_std`, 21 opponents, 42 games): every row identical to frozen v41's x181 (32W-2D-8L on these 21: timing -115,
  guard -65, astra28 -65, guarded tier4 striker -43 remain the losses).
- x186 (`x186_gunfix_growers`): 142-0-0, min +230 (v41 +380), mean +814 (= v41).
So the fix repairs 140 HP on astra's A/B, changes nothing on the striker set, and costs margin against the hoarders and one grower
setting without changing any result. v42 = v41 + the planner fix (fortress.py identical to v41, sha 3b69306d9b582b35...; plan.py
changed) was frozen by queue_bh; its regression (t74 tuning, x187 STRONG, x188 scripted econ, x189 forecaster, t75 mirror+eco, x190
PUNISH) is running. Decision rule: v42 replaces v41 if at least v41 on every pool by W-D-L (the A/B improvement is then the gain);
otherwise v41 stays and the planner fix is documented as an option.

## 2026-10-31T18:02Z  v42 regression: the planner fix costs a tuning game and a scripted game; v41 stays the FINAL RECOMMENDATION

Frozen v42 = v41 + GUN_PASS_SKIP_COVERED in plan.py (fortress.py identical to v41; plan.py sha256 in frozen/v42/SHA256SUMS), both seats,
0 rejected actions, 0 bot errors; v41 in the last column.

| run | pool | v42 | v41 |
| --- | --- | --- | --- |
| t74 | tuning, standard + asym:3:2 (104) | 101-2-1 (eco_then_flood switch 11 tier5, asym:3:2 seat 1: -600, base destroyed r12) | 102-2-0 |
| t75 | tuning, mirror:1:2 + eco:2 (104) | 100-4-0 | 100-4-0 |
| x187 | STRONG + lead v4 (26) | 22-2-2 (timing -115) | 22-2-2 |
| x188 | econ17 + econ15 leak, 4 scripted openings (16) | 15-0-1 (econ17 asym:3:2 seat 1 -3070; econ15 asym:23:2 seat 0 now +840) | 15-1-0 |
| x189 | exact forecaster, 5 timings (10) | 0 / -60 / 0 / 0 / 0 | same |
| x190 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x184-x186 (live, same code) | astra41 A/B, astra38 A-D, hoarders; 21-opponent set; GROWERS | A -135 / B -120 (v41 -275 / -260); A-D same; G +69 / B +205 (v41 +310 / +390); 21-opponent set identical; GROWERS 142-0-0 min +230 (v41 +380) | |

Trace of the new tuning loss (t74 log 00028, fortress seat 1 under asym:3:2 against the ten-round hoarder eco_then_flood switch 11): on the
22-step scripted map the emergency rule fires in rounds 7, 8 and 9 against the hoarder's growing affordable threat (952 / 2255 / 3877 gold)
and, with the gun pass no longer blocked by the large covered compositions, buys twelve gun3 (2400 gold) plus splashes instead of the
splashes-and-factories of v41; the gun-heavy map (gun damage 706 per tick, S 470) cannot stop the round-11 flood of thirteen tier5 (700
damage) and the fortress dies in round 12, where v41 killed the hoarder in round 10 (+800). The same mechanism gives the econ17 asym:3:2
loss. So the fix trades 140 HP on astra's A/B (still losses) for two lost games against hoarders on short scripted maps, where guns are
the wrong answer to an unbounded flood. By the pre-stated rule (at least v41 on every pool) v42 is rejected; v41 stays the FINAL
RECOMMENDATION (17:21Z). The planner flag stays on in the live module (astra's diagnosis is correct that the cutoff is a defect) and
is documented here with its measured cost; a future version should restrict the emergency rule's gun purchases to bounded threats
(e.g. no guns when the opponent's affordable flood exceeds the kill threshold of a gun-heavy map), which this shift has no time to test.

## 2026-10-31T18:03Z  End-of-shift-3 integrity check and state

Manifest check (scratch/manifest_check_shift3_end.txt): result identical to the start of the run (36 ok, 1002 missing = 999 data/games
records + data/games/manifest.json + the two .DS_Store files, 3 changed: td_game/combat.py, tests/test_engine.py, tests/test_rules.py;
bot_research.prompt.md the only extra root file). The list of files outside bot_research/ and .venv/ is unchanged (scratch/
files_outside_shift3_end.txt = files_outside_start.txt). Nothing of this lane is running. runs/defense is about 2.0 GB (limit 3 GB).
State: FINAL RECOMMENDATION frozen v41 (17:21Z); alternatives v40, v38, v34; v37, v39, v42 kept as evidence (rejected by the pre-stated
rules). Live bots/defense/fortress.py plays v34's policy (all options off); live bots/defense/plan.py carries the gun-pass fix
GUN_PASS_SKIP_COVERED = True (18:02Z), so the live planner differs from every frozen copy up to v41 in that one respect; frozen copies
are never edited. Test bots added this shift: counter_astra37.py, counter_astra38.py, counter_astra41.py, the counter_earlygun options.

## 2026-10-31T18:11Z  x191: raising the insurance cap to 260 (splash + gun3) wins the timing bot and the round-6 tier4 striker

Astra (review 9) showed that on the fortress's actual round-4 map the cheapest full plan against the round-5 tier4 package is splash (1,3)
+ gun3 (9,5) = 260 gold, not one gun3. `runs/defense/x191_cap260` (live module = v41's parameters with the fixed planner, cap 200 as the
control, 260 and 300; 102 games, both seats identical): cap 260 and 300 give identical results; against cap 200 only two rows change:
economy.timing -115 -> +50 and the guarded round-6 tier4 striker (growth 5, lock 9) -43 -> +89; everything else is unchanged (handoffs
g6 H10 +170 / H11 +590, staged +450, astra33 +413, astra28 -65, astra41 A -135 / B -120, round-5 tier4 striker -43, econ17 +5, guard -65,
eco6_t5 +1130, eco_then_flood +934, hoarders G +69 / B +432, lead v4 0). The round-5 striker still lands once because the fortress holds
207 gold at the round-4 decision (0.6 x 207 = 124 < 260).
v43 = v41 + eco_match_insure_cap 260 (planner fix OFF, to isolate the cap; live plan.py's GUN_PASS_SKIP_COVERED is set to False as its
default from now on, v42 having shown the fix costs two hoarder games) is being frozen by queue_bj and regressed: x196 strikers (33
opponents incl. astra41 A/B and the guarded round-4 strike), t76 tuning, x192 STRONG, x193 scripted econ, x194 forecaster, t77 mirror+eco,
x195 PUNISH, x197 GROWERS, smoke run. The queue runs into shift 4 (about 55 minutes). Decision rule: v43 replaces v41 if at least v41
on every pool by W-D-L (expected gain: timing and the round-6 tier4 striker on the STRONG and striker sets).

## 2026-10-31T18:17Z  x196: frozen v43 (v41 + cap 260) on 33 opponents

`runs/defense/x196_v43_std` (64 games, both seats identical, 0 rejected actions, 0 bot errors): 52W-2D-10L. Against frozen v41 (x181 on the
shared 29 opponents, 48-2-8): timing -115 -> +50 and the round-6 guarded tier4 striker -43 -> +89 become wins; astra38 A +105 (v41 +500) and
B +40 (+320) stay wins with smaller margins (the 260 plan is bought where v41 kept the gold); hoarders G +310 (same), B +550 (+390); eco6_t5
+1130 (+820), eco_then_flood +934 (+975); every handoff, both guards, astra33, astra38 C/D (+730 / +870), early-gun (+90), the guarded round-4
strike (+1510 / +1100), econ17 (+5), econ v2 (+10) unchanged; losses unchanged: astra28 -65, guard_continuation -65, the round-5 tier4
striker -43, astra41 A -275 / B -260 (the planner fix is off in v43, so astra41 A/B are at v41's values). The rest of the v43 regression
(t76, x192, x193, x194, t77, x195, x197) is running.

## 2026-10-31T18:24Z  v43 regression so far: tuning and scripted equal, STRONG better, forecaster worse

Frozen v43 (= v41 + eco_match_insure_cap 260; fortress.py sha256 c5cb18aa1b20c20a..., planner as v41), both seats: t76 tuning 102-2-0
(= v41); x192 STRONG 24-2-0 (v41 22-2-2: timing +50 instead of -115); x193 scripted econ 15-1-0 (identical rows to v41); x194 exact
forecaster of v43: tier3 r4 0, tier4 r5 -60, tier4 r7 -120, tier5 r8 -140, tier5 r10 0 (v41: 0, -60, 0, 0, 0). So the cap's extra
260-gold plans in rounds 5-7 are exploited by the exact-model forecaster at two more timings (the model knows the purchase and times a
tier4 / tier5 wave against the remaining gold), while they win the model-free timing bot and the round-6 tier4 striker. By the
pre-stated rule (at least v41 on every pool by W-D-L) v43 does not replace v41 unless the forecaster pool is discounted; the rule is
kept: v41 stays the recommendation, v43 is the documented alternative for pools without exact-model forecasters (it is at least v41
everywhere else measured so far: x196 52-2-10 against 48-2-8 on the shared opponents). t77 mirror+eco, x195 PUNISH, x197 GROWERS and the
smoke run are still running (queue_bj).

## 2026-10-31T18:30Z  v43 regression complete: a trade (STRONG and strikers up, forecaster down); v41 stays the FINAL RECOMMENDATION

Frozen v43 = v41 + eco_match_insure_cap 260 (fortress.py sha256 c5cb18aa1b20c20a..., full hashes in frozen/v43/SHA256SUMS; planner identical
to v41), both seats, 0 rejected actions, 0 bot errors; v41 in the last column.

| run | pool | v43 | v41 |
| --- | --- | --- | --- |
| t76 | tuning, standard + asym:3:2 (104) | 102-2-0 | 102-2-0 |
| t77 | tuning, mirror:1:2 + eco:2 (104) | 100-4-0 | 100-4-0 |
| x192 | STRONG + lead v4 (26) | 24-2-0 (timing +50) | 22-2-2 (timing -115) |
| x193 | econ17 + econ15 leak, 4 scripted openings (16) | 15-1-0 (identical rows) | 15-1-0 |
| x194 | exact forecaster of the candidate, 5 timings (10) | 0 / -60 / -120 / -140 / 0 | 0 / -60 / 0 / 0 / 0 |
| x195 | PUNISH (34) | 32-0-2 (astra28 -65) | 32-0-2 |
| x196 | strikers, counters, hoarders, astra A-D and astra41 A/B, guarded round-4 strike (33 opponents, 64) | 52-2-10 | 48-2-8 on the shared 29 (+ A/B -275/-260 = 48-2-12 on 31) |
| x197 | GROWERS (142) | 142-0-0, min +380, mean +812 | 142-0-0, min +380, mean +814 |
| smoke | frozen v43 vs idle (runner form) | win r8, 800 : -13 | same |

Decision by the rule stated at 18:12Z: v43 is at least v41 on every pool except the exact forecaster (two timings become losses: the model
of v43 knows the 260-gold plan of round 5 and times a tier4 wave at round 7 and a tier5 wave at round 8 against the gold that remains),
so it does not replace v41. It is the documented alternative for pools without exact-model forecasters: there it is strictly at least
v41 everywhere measured and wins the model-free timing bot (+50 instead of -115) and the round-6 guarded tier4 striker (+89 instead of
-43). FINAL RECOMMENDATION unchanged: frozen v41 (17:21Z). The complementary-strengths picture of this lane's final versions, for the
report: v41 (recommended), v43 (model-free early strikers), v40 (larger striker margins), v38 (answering economy bots and exact
forecasters; loses the striker class), v34 (poking insurer; loses the striker class badly).

## 2026-10-31T18:37Z  x198 (probe): lower emergency thresholds on v41's parameters do not solve astra's A/B

`runs/defense/x198_lethal25` (live module = v41's parameters with lethal_share 0.25 and 0.2 instead of 0.3; 72 games, both seats identical;
v41 reference in brackets): astra41 A -135 / -135 (-275), B -260 / -260 (-260); astra38 A +80 / +105 (+500), B +180 / +40 (+320), C +310 /
+310 (+730), D +870 / +870 (+870); hoarders G +310 / +310 (+310), B +390 / +215 (+390); timing -115 / +50 (-115); handoff g6 H10 +56 / +56
(+170), H11 +362 / +362 (+590); staged +1086 / +1086 (+450); eco6_t5 +888 / +1130 (+820); eco_then_flood +1225 / +934 (+975), its switch-11
hoarder +945 / +934; econ17 +5, guard -65, lead v4 0 (same). Totals on the 18 opponents: 0.25 26W-2D-8L, 0.2 28W-2D-6L (v41 on the same 18:
28W-2D-6L). Reading: a lower threshold buys the emergency plan one round earlier against A (one tier5 fewer lands, -135) but not against B,
and it shrinks the margins against the handoffs and astra's C by 110-420 because the insurance is bought where v41 grew. Not a candidate;
the astra41 A/B class stays open (the emergency rule's one-round lateness against a bait-guard-three-tier5 schedule cannot be fixed by
the threshold alone; the planner fix of v42 recovers 140 at the cost of two hoarder games).

## 2026-10-31T18:41Z  x199, for the lead: frozen v41 and v43 against the lead's frozen best_v9f

`runs/defense/x199_vs_best9f` (opponent `bot_research.experiments.lead.frozen.best_v9f:decide`, sha256 36d861fc...; 20 games; (HP
difference, end round) for fortress seat 0 / seat 1): standard -5 / -5 for both v41 and v43 (the round-1 exchange, as against best_v9e and
best_v9b); mirror:1:2 +1555 (r32) / +1555; asym:3:2 +1255 (r34) / -4330 (r21); mirror:22:3 -6160 (r21) / -6160; asym:23:2 -2515 (r21) /
-5858 (r22); v43's rows equal v41's. These are exactly the x182 values against best_v9e: against the fortress family best_v9f behaves as
best_v9e (same standard-start exchange, same econ20 foreign policy on scripted openings). Summary for the report: every fortress version
v34-v43 loses to the team's best bots (best_v9b, v9e, v9f) by exactly 5 on the standard start and draws P5TNUBM 0-0; on the scripted
openings the fortress wins the light ones (mirror:1:2, asym:3:2 seat 0) and loses the obstructed ones (mirror:22:3, asym:23:2, asym:3:2
seat 1 for v41/v43).

## 2026-10-31T18:42Z  Second addendum to the shift-3 summary: v42, v43 and the run index since 17:24Z

- v42 = v41 + planner gun-pass fix (GUN_PASS_SKIP_COVERED): rejected (18:02Z); repairs 140 HP on astra's A/B, loses two hoarder games.
  The live plan.py flag is False (default) since 18:12Z; v42's frozen plan.py keeps it True.
- v43 = v41 + eco_match_insure_cap 260: documented alternative (18:30Z); at least v41 everywhere except the exact forecaster (two more
  timings lost); wins the timing bot (+50) and the round-6 guarded tier4 striker (+89).
- x198 (lethal_share 0.25 / 0.2): not a candidate (18:37Z). x199: v41/v43 against best_v9f = the best_v9e rows (18:41Z).
- Open against v41 (and v43): astra41 A/B (-275 / -260; bait, two guards, three tier5 in round 8, lock), the round-5 tier4 strikers
  (-43 / -115 for v41, -43 for v43), astra28 and guard_continuation (-65, one hidden tier4), the exact forecaster at tier4 r5 (-60),
  the scripted-opening capacity races against econ20-based lead bots (x182/x199: 3W-5L per opponent), -5 to the lead's bots on the
  standard start (round-1 exchange), 0-0 against turtles and lead v4.
- Run index additions since 17:24Z: x183_astra41, x184_gunfix_astra, x185_gunfix_std, x186_gunfix_growers, t74_v42_tuning, x187_v42_strong,
  x188_v42_econ, x189_v42_forecast, t75_v42_mirror, x190_v42_punish, x191_cap260, x196_v43_std, t76_v43_tuning, x192_v43_strong,
  x193_v43_econ, x194_v43_forecast, t77_v43_mirror, x195_v43_punish, x197_v43_growers, smoke_frozen_v43_vs_idle.jsonl, x198_lethal25,
  x199_vs_best9f. Test bot added: counter_astra41.py. Astra review 4 of this shift: astra/v41-review/.

## 2026-10-31T18:49Z  x200: frozen v41 and v43 against hrt-w2's recommended economy bots V29 and V25RM

`runs/defense/x200_vs_econ29` (40 games; opponents = hrt-w2's frozen v29 econ29 and frozen v25 econ25 with their recommended parameter
strings (hrt-w2/scratch/v29.spec, v25rm.spec); (HP difference, end round) for fortress seat 0 / seat 1; v43's rows equal v41's throughout):
standard start +5 / +5 against both (the fortress wins the round-1 exchange: its two tier1 against the economy bot's one); mirror:1:2
+855 (r40) / +855 against V25RM, +15 (r50) / +15 against V29; mirror:22:3 +1120 (r17) / +1120 against both; asym:3:2 +975 (r19) / -9370
(r21) against V25RM and +975 / -12974 (r26) against V29; asym:23:2 -3215 (r21) / -2218 (r22) against both. Totals per opponent over the
ten games: 6W-0D-4L (V25RM), 6W-0D-4L (V29). The losses are the capacity races on the obstructed asymmetric openings (the fortress's
map has no lock and the economy bot's mass flood of round 21-26 ends it), the same regime as against the lead's econ20-based bots;
on the standard start and the mirror openings the fortress family wins or holds. For the report: against the team's three strongest
bots (best_v9f, P5TNUBM, hrt-w2's V29) on the standard start the fortress family is -5, 0, +5.

## 2026-10-31T18:49Z  Runtime cost of frozen v41 (for the report), from the harness summaries of its regression

Decision time per match (sum over the fortress's up to 50 decisions; harness column "cand decide s/match (max call)", measured on one
low-priority core of this box with three matches in parallel): tuning pool plain + asym (t72, 26 opponents): mean 3.7 s per match, max
28.4 s, longest single decision 3.93 s; STRONG pool (x177): mean 16.1 s, max 44.1 s, longest call 3.90 s; strikers and counters (x181, 29
opponents): mean 12.0 s, max 27.8 s, longest call 2.64 s; scripted econ openings (x178): mean 8.1 s, max 9.2 s; mirror + eco openings
(t73): mean 4.1 s, max 18.9 s, longest call 3.70 s. The planner's own wall-clock budget is 3.0 s for the gun pass (TIME_BUDGET in
plan.py), plus the re-planner's fixed 5000 steps on foreign maps; no decision exceeded 4 s in these runs. The slowest matches are the
50-round games against turtles and economy bots (many compositions to simulate each round); kills in rounds 8-12 cost 2-5 s in total.

## 2026-10-31T18:50Z  For the lead (18:45Z): the fortress family against the reinstalled best_v9e

The comparison with best_v9e already exists for the recommended v41 (`runs/defense/x182_v41_vs_lead`, notes 17:31Z: standard -5 / -5;
mirror:1:2 +1555 / +1555; asym:3:2 +1255 / -4330; mirror:22:3 -6160 / -6160; asym:23:2 -2515 / -5858) and for v36 / v37 / v38 (x158,
15:57Z) and v34 / v35 (x127, 13:14Z); x199 against the rejected best_v9f gave exactly the x182 rows for v41 and v43 and is reported as a
run against best_v9f. x201 (`runs/defense/x201_vs_best9e`, running) adds frozen v43 and v40 against best_v9e on the same five starts, both
seats; its table follows in a dated entry.

## 2026-10-31T18:52Z  x201: frozen v43 and v40 against best_v9e; the scripted-opening caveat is the lethal-0.3 threshold

`runs/defense/x201_vs_best9e` (20 games; (HP difference, end round) for fortress seat 0 / seat 1; best_v9e = the reinstalled team bot):
- v43: standard -5 / -5; mirror:1:2 +1555 / +1555; asym:3:2 +1255 / -4330; mirror:22:3 -6160 / -6160; asym:23:2 -2515 / -5858 (identical to
  v41's x182 rows: 3W-0D-7L over the ten games).
- v40 (lethal_share 0.4): standard -5 / -5; mirror:1:2 +1555 / +1555; asym:3:2 +1395 / +10; mirror:22:3 -1260 (r13) / -1260; asym:23:2 -2515 /
  -5858: 4W-0D-6L, and the two heavy losses of v41 on asym:3:2 seat 1 (-4330) and mirror:22:3 (-6160 against -1260) are v41's lethal-0.3
  emergency plans on lockless scripted maps (partial insurance against the econ20 bot's growing affordable flood, which no partial plan
  can stop, bought with gold that v40 keeps for its own flood or factories).
So the lead-bot caveat of 17:31Z belongs to the lower emergency threshold: on obstructed scripted openings against econ20-based bots v40 is
the better fortress (as v38 was, 4W-6L, x158), while on the standard start all versions are -5 and on the striker class v41 keeps its
advantage (x171: g6 H10 +170 against v40's +336 is the reverse trade). Summary for the report of the fortress family against best_v9e
on the five starts: v38 4W-6L (x158), v40 4W-6L (x201), v41 3W-7L (x182), v43 3W-7L (x201); the -5 of the standard start is common to all.

## 2026-10-31T19:57Z  Shift 4 start; open item (c) re-diagnosed: the factory cap, not the emergency plan, loses the scripted capacity races

State at the start of shift 4 (19:50Z): FINAL RECOMMENDATION frozen v41 (17:21Z), alternatives v43/v40/v38/v34; the lead's 19:50Z
note fixes the team entry point at best_v9e (sha256 70ef8eab...), with no open request to this lane. Nothing of this lane was running.

Re-reading the x182 loss logs (v41 against best_v9e, mirror:22:3 seat 0 and asym:3:2 seat 1) with scratch/spend.py and map_state.py
corrects the 18:52Z reading ("lethal-0.3 emergency plans"): both maps are FULL by round 20 (2 and 7 legal empty cells; S 880/890 with 21
and 30 guns), so from round 14 on neither the capacity rule nor the planner has anything to buy, and the fortress buys exactly 40
factories per round (MAX_FACTORIES_PER_ROUND, a constant of fortress.py) while holding 16,078 (mirror:22:3) and 50,670 (asym:3:2) unspent
gold at round 20. best_v9e's foreign-map policy (hrt-w2's econ20) buys 400 factories per round from round 12 on: 3500 and 3738 factories
at round 20 against the fortress's 430 and 580, then 299 and 300 tier5 in round 21 (194,350 and 195,000 gold), which kill through the full
maps (6160 and 4340 damage). The fortress's own 25-tier5 flood of round 18 (16,250 gold, mirror:22:3) landed nothing. The 40-factory cap
is a practical limit against huge action lists, not an engine rule (reports/RULES.md: no limit on the number of actions; hrt-w2's fcap1
measured no change of play on the standard start for their bot at 40/120/400; their recommended V29 and V25RM use fac_cap=400).
The 18:52Z difference between v40 and v41 on these maps (lethal 0.4 against 0.3) is therefore a secondary effect inside a race that
both lose to the economy; that entry's attribution is withdrawn.

Implementation (live bots/defense/fortress.py, backup scratch/fortress_live_before_factory_cap.py): option factory_cap (default 40 =
MAX_FACTORIES_PER_ROUND, so the default plays exactly as before) used in the three places the constant was used (finish-first
factories, the capacity-rule surplus, the final factory step). Frozen versions untouched.

Hypothesis H44 (stated before any result): with factory_cap=400 on v41's parameters, (i) the standard-start results against best_v9e,
V29 and V25RM are unchanged (-5, +5, +5: locked maps, nothing arrives, the gold difference is irrelevant), (ii) at least two of the
five obstructed scripted-opening losses against best_v9e (asym:3:2 seat 1, mirror:22:3 both seats, asym:23:2 both seats; x182) become
wins or lose by less than 1000, (iii) the asymmetric-opening losses against V29/V25RM (x200: asym:3:2 seat 1 -9370/-12974, asym:23:2
-3215/-2218) improve likewise, and (iv) the econ17/econ15 scripted results (x178: 15-1-0) stay wins. A second level, factory_cap=1200,
tests whether more is better. Run x202 (two parts: x202a against best_v9e, x202b against V29, V25RM, econ17, econ15; five starts, both
seats). If H44 holds, v44 = v41 + factory_cap is frozen and put through the full regression before any recommendation change (the rule of
15:52Z: at least v41 on every pool by W-D-L, otherwise a documented alternative).

## 2026-10-31T20:04Z  x202a: the factory cap against best_v9e; both-bases-destroyed is a draw; selection rule between the two caps

`runs/defense/x202a_fcap_vs_best9e` (live module with v41's parameters + factory_cap 400 or 1200; opponent frozen best_v9e; five starts, both
seats; result by the engine's winner field, then (HP difference, end round) for fortress seat 0 / seat 1; v41 = x182 in brackets):
- cap 400: standard L -5 / L -5 (unchanged); mirror:1:2 W +2195 r20 / W +2195 (was W +1555 r32); asym:3:2 W +1555 r21 (was W +1255 r34) /
  L -4330 r21 (unchanged, identical game); mirror:22:3 L -6160 r21 / L -6160 (unchanged, identical games); asym:23:2 L -2515 r21 (unchanged) /
  D +1282 r14 both bases destroyed (was L -5858 r22). Total 3W-1D-6L (v41 3W-0D-7L); no condition worse.
- cap 1200: standard L -5 / L -5; mirror:1:2 W +2195 r19 / W +2195; asym:3:2 W +1795 r21 / D +150 r21 both destroyed (was L -4330);
  mirror:22:3 L -6160 / L -6160; asym:23:2 D +705 r21 both destroyed (was L -2515) / D +1282 r14 both destroyed (was L -5858). Total
  3W-3D-4L; no condition worse than v41, three better.
Rejected actions 0, errors 0. Decision time: cap 400 max call 2.33 s; cap 1200 max call 8.13 s (the round-50 standard game: wall 100 s
against 42 s), the mass-finish search simulating floods of thousands of copies once the gold reaches millions.
Engine fact used for the scoring: engine.py returns winner None with reason both_bases_destroyed when both bases fall in the same round,
whatever the HP difference, so the fortress's same-round kills on these maps are draws, not wins (the HP difference stays positive).
Reading of H44 so far: (i) holds (standard start unchanged); (ii) holds only in the weak form (one loss of five becomes a draw at cap 400,
three at cap 1200; the mirror:22:3 games are identical: the fortress's finish rule spends 16,900 and 15,860 gold in rounds 17-18 on floods
that best_v9e's same-round guns stop (the finish rule checks the opponent's response only above 60 copies), and the round-21 flood of 299
tier5 kills through the full map regardless of the fortress's factory count).
Selection between the caps (stated now, before x202b is complete and before any regression): the cap with the higher harness score
W + D/2 over x202a + x202b, ties to 400 (the smaller action lists and decision times); this replaces the wins-only tie-break I had written
into scratch/queue_cb.sh before x202a was read, because the engine's draw rule makes the same-round kills draws and the W > D > L order of
the 15:52Z protocol should count them. The chosen cap becomes the default of frozen v44 = v41 + factory_cap, which then runs the full
regression.

## 2026-10-31T20:22Z  x202b, v44 frozen (v41 + factory_cap 1200), tenth astra review: a verified padded finish wins the mirror:22:3 race; finish_wrap implemented

x202b (`runs/defense/x202b_fcap_vs_econ`, caps 400 and 1200 against V29, V25RM, econ17, econ15; five starts, both seats; v41 baselines x178/x200):
- cap 400: V29 and V25RM standard W +5 / +5, mirror:1:2 W (V29 +15 r50, V25RM +3095 r22 against +855 r40), mirror:22:3 W +1680 r16 / +1680
  (was +1120 r17), asym:3:2 W +835 r23 / L -12974 (V29) and -9370 (V25RM) (unchanged), asym:23:2 L -3215 (unchanged) / D -1098 r22 both
  destroyed (was L -2218). econ17 10 W (all faster or larger). econ15: asym:23:2 seat 0 W +2100 r22 (was D 0 r35), seat 1 D +2900 r16 both
  destroyed (was W +1220 r22): one condition worse, one better, pool totals unchanged. Score W + D/2 over the 40 games: 34.5.
- cap 1200: as 400 except asym:23:2 against V29 and V25RM: seat 0 D +5 r21 both destroyed (was L), seat 1 W +9822 r19 (was L -2218); econ17
  asym:23:2 seat 0 +9385 r20. Score 36.5. No condition worse than v41 except the econ15 asym:23:2 seat 1 W -> D (both caps).
Over x202a + x202b the W + D/2 rule (stated 20:04Z) chose cap 1200 (x202a 4.5 against 3.5; x202b 36.5 against 34.5). queue_cb froze
v44 = v41 + factory_cap=1200 at 20:13Z (`bot_research.bots.defense.frozen.v44.fortress:@make`; fortress.py sha256 252c60fdee8cd6fe...; full
SHA256SUMS in frozen/v44/) and started its regression; the live defaults were reverted (v34 policy, options off; checked by the freeze log).
v44 regression so far: x203 striker set 48-2-14 of 64, every W-D-L equal to v41's (x181 for 58 conditions, the known -275/-260/-43 for
the six x196 additions), four kills faster or larger (guard_handoff 5/10 +870 -> +930, guarded_round4 +1510 r15 -> +1650 r14); t78 tuning
102-2-0 with every W-D-L equal to t72 and margins mostly larger (threat_defender +800 -> +2000, splash_turtle +1140 -> +1280; smaller on
asym:3:2 seat 1 against three baselines, 885 -> 852); x204 STRONG partial 22-0-2 of 24 with the two remaining games pending. Longest
decision so far 3.43 s (t78).

Tenth astra review (astra/fcap-rev2/answer.md; read-only replays and engine checks in that directory; recorded as claims checked where stated):
1. Correction to my 20:04Z entry: the 8.13 s maximum decision in x202a belongs to best_v9e, not the fortress (decide_max_seconds is ordered
   by seat: fortress 0.46 s). Mechanism (astra's profile, 98.5 percent of best_v9e's round-50 time): best_v9e's frozen v7 planner enumerates
   threat compositions from ITS OPPONENT'S gold without a cap, so with the fortress holding 12,149,100 gold before round 50 it simulates an
   809,940-tier1 composition although its own map is splash-immune. FOR THE LEAD: best_v9e's decision time grows with the opponent's
   hoarded gold (8 s at 12 million; the fortress with cap 1200 reaches that on the standard start); a cap on the enumerated gold or an
   immunity short-cut would remove it. The fortress has the analogous gold-dependent cost in _find_kill's geometric flood sizes, but on
   the standard game against best_v9e it skips every tier because S_opp = 1550 >= 1500.
2. The capacity rule's surplus trigger (left - factory_cap x 20) fires later with a larger cap; the independent race-danger condition still
   applies and the pass is bounded at 12 additions, so the construction budget does not shrink for caps 400 and 1200 (checked by astra).
3. The decisive finding: in the mirror:22:3 game (log A of x202a) the fortress at round 18 (16,352 gold, 26 active tier5 bought in round 17,
   opponent 735 HP) has a kill that the planner's own generator already produces: plan.wrap_bundles (roster padding: 224 tier1 then 19
   tier5, 15,710 gold). Entry k spawns at tick k mod 250 (combat.py:28), so the 19 new tier5 at entries 250-268 spawn in ticks 0-18
   alongside the 26 respawning tier5 (entries 0-25) instead of behind them. Damage 3080 against the observed map, 2380 against best_v9e's
   actual round-18 construction, and at least 2240 over ALL 3125 legal construction responses on the five effective free cells (exhaustive,
   engine-checked). The finish rule did not consider the candidate (wrap_bundles is used for threat generation only). Astra's replay with
   the candidate added to _find_kill reproduces every logged fortress action of rounds 4-17 and wins at round 18 (735 : -1645). Later
   single-round continuations from the logged prefix also win at rounds 19 and 20 (199 tier1 + 21 or 43 tier5) and draw at 21.
4. Negative results from the same traces (astra): saving instead of the two failed finishes (109,493 gold at round 21, 168 tier5) still
   deals 0; economy-only from round 10 against the responding best_v9e dies in round 12; no construction on the two remaining legal cells
   of the round-16 map changes the 6160; a heuristic re-assignment of the earlier splash/gun purchases reaches 3220 damage taken (still
   fatal), not a proof that every earlier layout loses.
5. Response-check defects: _gun_candidates truncates to the top 8 cells by coverage BEFORE the legality test (plan.py), so on the round-17/18
   maps all eight candidates of every gun type are illegal and robust_leak predicts no gun response (1540 and 1820 damage instead of 0; a
   single legal gun3 at (0,11) or (8,0) stops each flood); and the gun search is skipped above 120 entries (GUN_PASS_MAX_ENTITIES), so the
   mass finish of log B's round 21 (297 tier5, 193,050 gold; 5600 predicted, 0 after best_v9e's two gun1 + five gun3 for 1060) had no
   effective response check either. Proposed bounded rule for small finishes: response check when the opponent owns a turret and holds
   at least 400 gold, or after a failed predicted attack within eight rounds; cost: against turret-owning growers that hoard gold it can
   postpone a real kill indefinitely.
6. Bookkeeping: _find_kill's "cheapest" docstring overstated the sampled search (reworded); the live make() defaults differ from v41's
   (known: the live module plays v34's policy with options off; every frozen version sets its own defaults); factory_cap is not validated.

Implemented in the live module (frozen versions untouched):
- fortress.py: option finish_wrap (False; True: _find_kill also tries the wrap_bundles tier5 candidate, cost-compared with the plain
  floods, always with the response check) and option finish_robust_gold (None; a gold amount: the response check also applies to floods
  of at most 60 copies while the opponent owns a turret and holds at least that much gold). Reproduction with the live module
  (scratch/wrap_replay_live.py, v41's parameters + factory_cap 400 + finish_wrap, no monkeypatch): rounds 4-17 of log A reproduced
  action for action, round 18 = 224 tier1 + 19 tier5 + 32 factories, engine result 735 : -1645, fortress wins (7 s).
- plan.py: module flag GUN_CANDIDATES_LEGAL_FIRST (False = unchanged; True: legality before the top-8 truncation), for a later version.
Hypothesis H45 (stated before x209): on v44's parameters, finish_wrap turns the mirror:22:3 losses against best_v9e into wins and does
not change any striker-set or GROWERS result for the worse (the candidate is taken only when it kills under the response check and is
cheaper than, or the only, kill); finish_robust_gold=400 on top of it loses nothing on those pools either (its vetoes concern small
finishes against rich turret owners). Runs queued after the v44 regression (scratch/queue_cc.sh): x209a (W = v44 + finish_wrap, WR = W +
finish_robust_gold 400; against best_v9e and V29, five starts), x209b (W, WR on the 33-opponent striker set), x209c (W, WR on GROWERS).

## 2026-10-31T20:32Z  v44 regression complete: at least v41 on every pool, better against best_v9e and the economy bots; FINAL RECOMMENDATION REVISED: frozen v44

Frozen v44 = v41 + factory_cap=1200 (`bot_research.bots.defense.frozen.v44.fortress:@make`, no parameters; frozen at 20:13Z by scratch/queue_cb.sh
with the defaults set in the live module and reverted afterwards). SHA256SUMS of bots/defense/frozen/v44/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  252c60fdee8cd6fe690ed873a0ea933e68be891987ea1ce23342af4a475a902c  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  ff2ea3acdddb685fcc869b406af6431a173d3addc9fc44e2af7804401a175a23  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Regression of the frozen artifact (both seats; v41's run in brackets; W-D-L by the engine's winner):
- tuning (26 opponents, standard + asym:3:2): t78 102-2-0 (t72 102-2-0), every condition the same result; margins larger in 13 conditions
  (threat_defender +800 -> +2000, splash_turtle +1140 -> +1280), smaller in 3 (asym:3:2 seat 1 against greedy_eco/eco_then_flood/maze_eco
  885 -> 852, eco6_t5 473 -> 461). Longest decision 3.43 s.
- mirror:1:2 + eco:2: t79 100-4-0 (t73 100-4-0), same results, 28 margin changes both ways (gun_turtle mirror +840 -> +1310, eco:2 +1120 -> +840).
- STRONG: x204 22-2-2 (x177 22-2-2), same results; predicted_pressure +820 -> +1380, posterior_response +890 -> +830.
- scripted econ openings: x205 15-1-0 (x178 15-1-0): econ15 asym:23:2 seat 0 D 0 r35 -> W +2100 r21, seat 1 W +1220 r22 -> D +2900 r16
  (both bases destroyed in the fortress's kill round); all econ17 games won faster (mirror:1:2 r33 -> r15) with larger or smaller margins.
- exact forecaster (five schedules modelling v44 itself): x206 0W-10D-2L, tier4 round 5 -60 in both seats, the rest 0 (x179 the same).
- PUNISH: x207 32-0-2 (x180 32-0-2), same results. GROWERS: x208 142-0-0 min +380 median +840 (x197/x172 142-0-0 min +380).
- strikers and counters (33 opponents): x203 48-2-14 of 64, every condition equal to v41 (x181 plus the known -275/-260/-43), four kills
  faster or larger. Smoke against idle: 8 rounds, 800 / -13 (runs/defense/smoke_frozen_v44_vs_idle.jsonl).
- against best_v9e (x202a, live module with v44's parameters): 3W-3D-4L against v41's 3W-0D-7L (x182); against V29/V25RM/econ17/econ15
  (x202b): the x202b table of the 20:22Z entry (one W -> D, four L -> D or W).
Decision by the 15:52Z rule: no pool worse by W-D-L, better on the lead-bot and economy-bot starts -> FINAL RECOMMENDATION of this lane =
frozen v44. What changed in play: nothing before the fortress holds more than 800 gold after its defence and attack (round 9-14 in long
games); afterwards it buys up to 1200 factories per round instead of 40, so its late economy compounds (standard start, round 50: about
12 million gold instead of 577,000). Known costs: factory actions per game up to 60,000 (logs of lost games 0.9-1.4 MB instead of 0.4-0.75);
the opponent's planners that enumerate threats from the fortress's gold slow down (best_v9e 8 s per decision at round 50; the lead has been
told in the 20:22Z entry). v41 stays the alternative for settings where action-list size matters. v45 (v44 + finish_wrap) is under test
(x209, then its own regression); if it passes the same rule it supersedes v44.

## 2026-10-31T20:40Z  x209a: the padded finish (finish_wrap) against best_v9e and V29; the robust small-finish check on top

`runs/defense/x209a_wrap_vs_lead_econ` (live module, v44's parameters; W = finish_wrap, WR = finish_wrap + finish_robust_gold 400; five
starts, both seats; (result, HP difference, end round) for seat 0 / seat 1; v44 = x202a cap 1200 in brackets):
- W against best_v9e: standard L -5 / L -5 (same); mirror:1:2 W +1695 r14 / W +1695 r14 (W +2195 r19); asym:3:2 W +1675 r16 (W +1795 r21) /
  D +150 r21 (same); mirror:22:3 W +2940 r19 / W +2940 r19 (L -6160 r21 / L -6160); asym:23:2 W +2385 r17 (D +705 r21) / D +1282 r14 (same).
  Total 6W-2D-2L against v44's 3W-3D-4L and v41's 3W-0D-7L.
- WR against best_v9e: as W except asym:3:2 seat 0 W +5735 r20 (W +1675 r16 for W) and asym:23:2 seat 1 W +4222 r18 (D +1282 r14): total
  7W-1D-2L. The two differences are games in which the response check vetoes a small finish that best_v9e would have answered, and the gold
  buys a larger padded kill a few rounds later.
- W and WR against V29 (econ29): identical rows: standard W +5 / +5, mirror:1:2 W +15 r50 / W +15 (the last WR game of the run was still
  playing when this was written), asym:3:2 W +975 r17 / L -12974 r26 (same as v44 and v41), mirror:22:3 W +1680 r16 / W +1680, asym:23:2
  W +2385 r17 (D +5 r21 for v44) / W +9822 r19 (same). V29's own round-21/26 floods are not affected by the fortress's finish rule; the
  asym:3:2 seat 1 loss stays (the fortress is killed at round 26 before any kill of its own is affordable).
Decision times at most 1.33 s (W) and 1.22 s (WR) in these games. H45 (i) holds: the mirror:22:3 race against best_v9e is won by the padded
finish in both seats (the kill is found at round 19 here, not 18 as in the replay of the 20:22Z entry, because the cap-1200 economy differs
from the cap-400 log replayed there). x209b (striker set) and x209c (GROWERS) are running; queue_cd then chooses WR over W only if WR is at
least W on each pool's W-D-L and higher in W + D/2, freezes v45 and runs its regression.

## 2026-10-31T20:49Z  x209b: the wrap variants on the 33-opponent striker set

`runs/defense/x209b_wrap_std` (live module, v44's parameters; W = finish_wrap, WR = finish_wrap + finish_robust_gold 400; 64 games each;
compared per condition with frozen v44's x203):
- W: 48-2-14, every condition identical to v44 in result, HP difference and end round: the padded candidate is never taken where a plain
  flood already kills (it is cost-compared), and it does not kill where none does (the strikers lock or are killed early). Longest
  decision 1.62 s.
- WR: 48-2-14, the same results; 16 HP changes, all but two larger: guard_handoff growth 6 handoff 10/11 and screened_guard_maze +590 r10 ->
  +1430 r11, guarded_round4 (both early_gun settings) +1100 r13 -> +3340 r15 and +1650 r14 -> +5570 r15, astra33 +413 -> +493, astra38 D
  +870 -> +1010; smaller: guard_handoff growth 5 +930 -> +870 (both seats). Reading: the response check vetoes a small finish that a
  turret-owning striker with 400+ gold could answer, and the fortress kills one or two rounds later with a flood the check accepts.
  Longest decision 5.05 s (robust_leak runs the planner with the opponent's full gold for each small finish candidate), against 1.62 s
  for W and 3.43 s for v44 in its regression.
Running: x209c (W, WR on GROWERS, 142 games each); queue_cd then applies the pre-stated choice (WR only if at least W on each pool and
higher in W + D/2; so far x209a WR 16W-1D-3L against W 15W-2D-3L, x209b equal), freezes v45 and starts its regression.

## 2026-10-31T20:58Z  x209c (GROWERS) and the choice of the wrap variant; v45 frozen = v44 + finish_wrap + finish_robust_gold 400

`runs/defense/x209c_wrap_growers` (W and WR on the 71-opponent GROWERS pool, 142 games each): W 142-0-0 with every HP difference and end
round equal to v44's x208; WR 142-0-0 min +380, eight HP changes, all against roster_bait variants (six larger with the kill one round later,
+413 r10 -> +1340 r11, +671 -> +1295; two smaller, +820 -> +800 r12). Longest decision 3.32 s (W), 5.38 s (WR).
Choice by the rule stated at 20:32Z (scratch/queue_cd.sh): WR is at least W on every x209 pool's W-D-L (x209a 16-1-3 against 15-2-3,
x209b 48-2-14 both, x209c 142-0-0 both) and higher in W + D/2 (16.5 against 16 on x209a), so WR was chosen: v45 = v44 + finish_wrap=True +
finish_robust_gold=400, frozen at 20:54:39Z (`bot_research.bots.defense.frozen.v45.fortress:@make`, no parameters). SHA256SUMS of
bots/defense/frozen/v45/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  4f413cbbc635dc775e8756ecd4e6801bb9fdbc06c6bb89147184494b8c59c253  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
The live module's make() defaults were reverted by the queue (v34 policy, every option off; plan.py flag GUN_CANDIDATES_LEGAL_FIRST False in
the live module and in frozen v45). Regression of the frozen artifact running (queue_cd: x210 against best_v9e and V29 on five starts, t80
tuning, x211 STRONG, x212 scripted econ, x213 forecaster, t81 mirror+eco, x214 PUNISH, smoke); the striker set and GROWERS were measured on
the live module with v45's exact parameters (x209b WR, x209c WR). Decision rule for v45 (unchanged): at least v44 on every pool by W-D-L and
better somewhere (x209a already shows 7W-1D-2L against best_v9e), otherwise a documented alternative. Known cost going in: the longest
decision rises to about 5 s (the response check on small finishes runs the planner with the opponent's full gold). An astra review of the
frozen v45 code was requested at 20:58Z (astra/v45-review).

## 2026-10-31T21:18Z  v45 regression complete: a trade (lead-bot races won, two scripted wins become same-round draws); v44 stays; the round-15 diagnosis; v46

Regression of frozen v45 (both seats; v44's run in brackets; W-D-L by the engine's winner): x210 against best_v9e 7W-1D-2L (x202a cap 1200
3W-3D-4L; the frozen artifact reproduces x209a WR row for row) and against V29 9W-0D-1L (8W-1D-1L); t80 tuning 102-2-0 (t78 102-2-0, same
results); x211 STRONG 22-2-2 (same results); x212 scripted econ 13-3-0 (x205 15-1-0): econ15 and econ17 under asym:23:2 seat 0 W +2100 r21
and W +9385 r20 -> D +840 r16 and D +845 r15, both bases destroyed; x213 forecaster 1W-9D-2L (0-10-2: one draw became a win); t81 mirror+eco
100-4-0 (same); x214 PUNISH 32-0-2 (same); x209b WR strikers 48-2-14 and x209c WR GROWERS 142-0-0 (same results, measured on the live
module with v45's exact parameters); smoke 8 rounds 800 / -13. Longest decision 5.03 s (x214), 4.83 s (x213).
Decision by the rule: two conditions of the scripted pool are worse (W -> D), so v45 is NOT at least v44 on every pool; v44 stays the FINAL
RECOMMENDATION and v45 is the documented alternative that wins the capacity races against best_v9e (7-1-2 against 3-3-4).

Diagnosis (x222 = the two asym:23:2 econ17 games replayed with --keep-logs all, `runs/defense/x222_r15_replay`; v44 and v45 identical
through round 14): at round 15 econ17 floods 12 tier5 (980 damage on the fortress's map, 790 HP) and builds two gun3. v44 has no kill
(its 23 tier5 of round 14 were stopped), the planner's "best" plan against the 13 worst-case compositions (one of them a 555-entry padded
flood) is EMPTY, and the capacity rule buys 5 splash + 7 gun3 (1700 gold): the actual flood deals 0 and v44 wins at round 20 (+9385). v45
finds the padded kill (223 tier1 + 18 tier5, 15,045 of 15,494 gold) in the finish-first branch; the branch's "dead anyway" test (the
planner's defence does not save me against the worst case) is true, so it buys the kill with everything, builds nothing, and both bases
fall (draw). The missing defence was the capacity rule's, which the finish-first branch never reaches.
Fix (live module, option finish_defend_first): in a round whose worst affordable flood is lethal, the planner's defence is bought first and
the kill with the remainder if it still kills; when the planner has no saving defence, the kill is no longer bought early: the defence steps
run (the capacity rule can still buy guns) and the attack step's finish rule buys the kill with the remaining gold. Replay of the x222
round-15 state with the live module (scratch/r15_replay_live.py, v45's parameters + finish_defend_first + finish_gun_check 12): 5 splash +
7 gun3 + 223 tier1 + 16 tier5 + 2 factories, engine result 790 : -755, a win at round 15. Replay of log A's round 18 (scratch/
wrap_replay_live.py with all new options): unchanged 224 tier1 + 19 tier5, 735 : -1645.

Also implemented (astra review 11, astra/v45-review/answer.md; claims checked where stated): (a) option finish_gun_check (12): a finish flood
above the planner's 120-entry gun-pass limit (every padded candidate is; the response check then considers splashes and walls only) must
also survive one gun3 on each of the 12 best legal cells of the opponent's map, exact simulation; astra's witness: x209b game 00125 round 15,
250 tier1 + 52 tier5 for 37,550 gold predicted 5600 damage and stopped completely by one gun3 at (2,3) (the opponent did not build it and
the fortress won anyway). (b) a per-decision cache of the finish simulations (leak, response, gun check) shared by the finish-first and
attack callers: astra traced the 5.05 s decision (x209b game 00111 round 10) to 14 response-planning calls, 7 of them duplicates, and
verified that a cache keyed by the ordered type sequence leaves the 50 rounds of that game unchanged. Other review points recorded as open:
_race_kill can still buy a flood the finish search rejected; the small-finish size test counts new purchases, not the whole roster; wealthy
opponents without a turret and opponents with 200-399 gold do not trigger the small-finish check; the padded candidate's alignment with the
roster's heavy copies holds for the current round only (expiry re-indexes the roster later); the response check is an upper bound on the
opponent's best construction, never a certificate of a kill. Erratum: the striker set has 32 distinct opponents (64 games), not 33.
v46 = v45 + finish_gun_check 12 + finish_defend_first (+ the cache; plan.py flag unchanged) is being frozen and regressed on every pool
(scratch/queue_cf.sh: x215 lead/econ, x216 strikers, t82 tuning, x217 STRONG, x218 scripted econ, x219 forecaster, t83 mirror, x220 PUNISH,
x221 GROWERS, smoke). Rule: at least v44 on every pool by W-D-L and better somewhere, otherwise an alternative.

## 2026-10-31T21:45Z  v46 regression complete: at least v44 on every pool, better on three; FINAL RECOMMENDATION REVISED: frozen v46; twelfth astra review

Frozen v46 = v45 + finish_gun_check=12 + finish_defend_first=True + the per-decision finish cache (= v41 + factory_cap 1200 + finish_wrap +
finish_robust_gold 400 + these three), `bot_research.bots.defense.frozen.v46.fortress:@make`, frozen 21:17:31Z (scratch/queue_cf.sh; live
defaults reverted and checked). SHA256SUMS of bots/defense/frozen/v46/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  a0aa939dd81fdbfd1ab4da4fd0c40cbc2e145058f5c01f6c606d27b4c28c15a7  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Regression (both seats; v44 in brackets; W-D-L by the engine's winner): x215 against best_v9e 7W-1D-2L (3W-3D-4L; the standard start -5 / -5
and asym:3:2 seat 1 D +150 remain) and V29 9W-0D-1L (8-1-1); x216 strikers 48-2-14 of 64, every result equal to v44 (16 larger margins, as
v45); t82 tuning 102-2-0 (same results); x217 STRONG 22-2-2 (same); x218 scripted econ 16-0-0 (15-1-0: econ15 asym:23:2 seat 1 D -> W +3460
r16; v45's two draws are wins again, +2385 r17 and +9385 r20 ... both econ17 and econ15 asym:23:2 seat 0 W); x219 forecaster 1W-9D-2L
(0-10-2); t83 mirror+eco 100-4-0 (same); x220 PUNISH 32-0-2 (same); x221 GROWERS 142-0-0 min +380 (same); smoke 8 rounds 800 / -13.
Longest decision 5.29 s (x216, against counter_astra37 G at round 10: the response planning of the small-finish check; 3.43 s for v44).
Decision by the rule: no pool worse, three better -> FINAL RECOMMENDATION of this lane = frozen v46; v44 stays the alternative where decision
time (5 s against 3.5 s) or action-list size matters, v41 the alternative with the 40-factory cap.

Twelfth astra review (astra/v46-review/answer.md; its constructed states and engine checks in that directory; claims checked where stated):
1. _single_gun_stops is sound as a counterexample test (enumeration radius, legality, route after placement, roster, affordability all
   checked); but its SIZE GATE is wrong: it tests the number of NEW purchases while the planner's 120-entry gun-pass cutoff applies to the
   active roster plus the purchases. Constructed variant of x209b game 00125 round 15 with 200 active tier1 on my roster: _find_kill accepts
   50 tier1 + 52 tier5 (102 purchases, 302 entries) without the gun check although one gun3 at (2,3) stops it (verified). The top-12 shortlist
   is also incomplete in principle (two constructed states where the stopping gun is rank 15 or 53), but a scan of all 429 x209/x222 logs
   found 12 purchases above 120 entries, 8 lethal states, and no top-12 miss; in game 00125 the rank-1 cell (9,5) already stops the flood.
2. The fall-through can turn a draw into a loss: same x222 round-15 position with my gold 10,500 and the opponent flooding 300 tier5 with
   195,000 gold: v45 buys the padded kill (10,495) and draws; v46 spends 1700 on capacity guns, the kill no longer fits (8800), nothing is
   bought, loss (-5790 : 785). Conditions: a finish exists, the sampled threat is lethal, the planner's defence is empty or no finish fits
   after it, and later spending removes the finish (or matching in rounds <= 7 skips the attack step: no such state in the 1685 matching
   observations of the logs, where own roster damage + gold/3 < opponent HP always; the branch fails only in an artificially walled state).
3. The cache is consistent at its three call sites (same observation, HP, rules, layout; own construction changes neither the opponent's map
   nor my roster; _race_kill does not use it). Qualifications: attack="flood" never calls the later finish (not our configuration); with
   d_acts non-empty and kill2 found the early return does not require the defence to save the base; two comments to correct.
Fixes for v47 (live module): the gun-check gate counts active roster + purchases; in the dead-anyway fall-through the known finish's cost is
RESERVED (left is reduced by it through the defence steps and restored before the attack step), so the attack step can always buy that kill
and v46's defence is added only when there is slack: in astra's constructed state v47 therefore plays v45's draw, in x222 round 15 v46's win.

## 2026-10-31T21:48Z  v47 = v46 + the review-12 fixes: implementation and replays (regression starting)

Live module (frozen versions untouched): (1) the gun-check gate counts the active roster plus the purchases, as the planner's 120-entry
cutoff does; (2) in the dead-anyway fall-through of finish_defend_first the cost of the SMALLEST padded kill that still passes every check
(binary search over the heavy count on the same padding, _find_kill(..., minimal=True); the kill bought keeps every affordable copy) is
reserved through the defence steps and released before the attack step, so the finish always stays affordable and defence is added only
from the slack. A first version reserving the full kill (18 tier5, 15,045 of 15,494 gold) left no slack and reproduced v45's draw in the
x222 state; with the minimal kill's cost as the reserve the replays give: x222 round 15 = 5 splash + 7 gun3 + 223 tier1 + 16 tier5 + 2
factories, engine 790 : -755 (a win; 2.9 s for the whole 15-round replay), log A round 18 = 224 tier1 + 19 tier5 (unchanged). In astra's
constructed loss state (10,500 gold against a 300-tier5 flood) the reserve is the minimal kill's cost, the slack buys at most the capacity
guns it allows, and the attack step buys the padded kill with the rest: a draw as v45 (expected by construction; not replayed for lack of
time). Comments corrected as the review asked. v47 is frozen with v46's defaults and runs the same regression (scratch/queue_cg.sh: x223
lead/econ, x224 strikers, t84 tuning, x225 STRONG, x226 scripted econ, x227 forecaster, t85 mirror, x228 PUNISH, x229 GROWERS, smoke); rule:
at least v46 on every pool by W-D-L (and not worse than v46 on the lead-bot races) -> v47 replaces v46; otherwise v46 stays and v47 is the
documented alternative with the two constructed defects fixed.

## 2026-10-31T21:48Z  FOR THE LEAD and hrt-w3: shift-4 findings of the defense lane in one place

1. Engine fact used: a per-round purchase limit does not exist (RULES.md); the 40-factories-per-round constant of every research bot is a
   practical limit. The fortress with factory_cap 1200 (v44) compounds its late economy; the only visible costs are action-list size
   (up to 1200 factory actions per round) and the OPPONENT's planning time when its threat enumeration scales with my gold: best_v9e's
   frozen v7 planner spends 8 s per decision at round 50 against 12 million gold (astra's profile, 98.5 percent in _worst_leak on an
   809,940-tier1 composition although its map is splash-immune). A cap on the enumerated gold or an immunity short-cut would remove it.
2. The padded finish (v45-v47; plan.wrap_bundles inside the finish rule): entry k spawns at tick k mod 250, so after padding the roster to
   a multiple of 250 with tier1 the new tier5 spawn in ticks 0.. alongside the respawning tier5 already on the roster. It wins the capacity
   races on the obstructed scripted openings against best_v9e's foreign-map policy (econ20): v46 7W-1D-2L on the five starts x both seats
   against v41's 3W-0D-7L (x215; the two losses are the standard start, -5 both seats, the round-1 exchange; the draw is asym:3:2 seat 1,
   both bases destroyed). best_v9e's same-round gun response stops plain floods (x202a rounds 17-18: 26 and 25 tier5 landed nothing) but
   not the padded one (log A round 18: 2240 damage at least over all 3125 legal constructions, astra's exhaustive check). A counter would be
   an earlier lock or the planner's gun pass applied to compositions above 120 entries (GUN_PASS_MAX_ENTITIES in my planner; the same
   limit exists in the frozen v7 planner best_v9e imports).
3. For the report's teammate table (both seats, engine winner): fortress v46 against best_v9e standard L -5 / L -5; mirror:1:2 W +1555 r14 /
   W +1555; asym:3:2 W +5735 r20 / D +150 r21; mirror:22:3 W +2940 r19 / W +2940; asym:23:2 W +2385 r17 / W +4222 r18 (x215). Against hrt-w2's
   V29: standard W +5 / +5, mirror:1:2 W +15 / +15 (r50), asym:3:2 W +975 r17 / L -12974 r26, mirror:22:3 W +1680 r16 / +1680, asym:23:2
   W +2385 r17 / W +9822 r19. v41's rows (x182, x200) stay valid for v41.
4. Defects found by the astra reviews in my planner that other bots importing it inherit (frozen v7 plan.py is older but shares the design):
   _gun_candidates truncates to the top 8 cells before the legality test (on nearly full maps all eight can be illegal and the gun pass
   finds nothing; flag GUN_CANDIDATES_LEGAL_FIRST in the live plan.py, off, not regressed); the gun pass is skipped above 120 entries, so a
   response estimate against a padded flood never contains guns.

## 2026-10-31T22:05Z  v47 regression (partial) and astra check 13: the reserve works, but the capacity rule spends only half the slack

Frozen v47 (sha256 of fortress.py f12f255a90bea178...; frozen 21:47:34Z) against v46, both seats, engine winner: x223 lead/econ 16-1-3 with
every HP equal; x224 strikers 48-2-14, every HP equal; t84 tuning 102-2-0, equal; x225 STRONG 22-2-2, equal; x226 scripted econ 15-1-0
against v46's 16-0-0: econ15 asym:23:2 seat 1 W +3460 r16 -> D +3740 r16 (both bases destroyed); x227 forecaster 2W-7D-2L of 11 so far
(v46 1-9-2 of 12). Pools t85, x228, x229 and the smoke still running. By the rule v47 does NOT replace v46 (one scripted condition worse).
Astra check 13 (astra/v47-check/answer.md, state replays with the frozen v47 module): (1) its constructed draw-to-loss state is a draw again
with v47 (reserve 10,495 = the minimal passing kill, exhaustively confirmed: ten tier5 deal 700 < 785, eleven 840; nothing left for defence;
223 tier1 + 11 tier5 bought; -34630 : -55); (2) the gate witness is now rejected (302 entries, the first tested gun3 at (9,5) zeroes the
damage, _find_kill returns None); (3) the x222 round-15 win reproduced independently (reserve 10,495, defence gets 4999 and spends 1700,
the attack step gets 13,794). (4) New constructed regression, the same mechanism as the x226 draw: with the reserve the slack is exactly
the saving defence's cost, but the capacity rule's budget is capacity_share (0.5) of it, so 5 splash + 2 gun3 are bought instead of 5 splash
+ 7 gun3, and the extra gold goes to attack and factories: a win becomes a same-round draw; capacity_share 1 for that round restores the win.
Other qualifications: matching (rounds <= 7) still skips the restored attack step (only an artificial fully-walled state shows it); the
binary search's minimality assumes a monotone predicate (the endpoint is always a checked passing candidate).
Fix in the live module (v48 candidate): under a reserve the capacity rule's budget is the whole slack (the kill is already reserved, the
defence is what the slack is for; the pass stays bounded at 12 additions). Replays after the fix: x222 round 15 and log A round 18 as before.

## 2026-10-31T22:13Z  v47 regression complete: v46 stays (one scripted W -> D); v48 = v47 + the slack fix frozen, regression running

Frozen v47 (fortress.py sha256 f12f255a90bea178a827539a099409f5b9b8b08365b35d1e3eaa8e7ae93df6b2) against v46, both seats, engine winner: x223 lead/econ 16-1-3, x224 strikers 48-2-14, t84 tuning
102-2-0, x225 STRONG 22-2-2, x227 forecaster 1-9-2, t85 mirror+eco 100-4-0, x228 PUNISH 32-0-2, x229 GROWERS 142-0-0: every HP difference and
end round equal to v46's; x226 scripted econ 15-1-0 against 16-0-0 (econ15 asym:23:2 seat 1 W +3460 r16 -> D +3740 r16, both bases
destroyed: the capacity rule spent half the slack, see 22:05Z). Smoke OK. Longest decision 3.85 s (t84). Decision: v46 stays the FINAL
RECOMMENDATION; v47 is the documented alternative with astra review 12's two constructed defects fixed (gun-check gate on the whole roster;
a kill-or-be-killed draw no longer turned into a loss) at the price of that one draw.
v48 = v47 + "under a reserve the capacity rule's budget is the whole slack" (22:05Z), frozen 22:10:41Z by scratch/queue_ch.sh with v46's
defaults (`bot_research.bots.defense.frozen.v48.fortress:@make`), live defaults reverted and checked. SHA256SUMS of frozen/v48/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  067af590c9d2fceef852cc4ac3516d31e01919993f98755cbed44a05d68c37f5  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Regression running (x230 lead/econ, x231 strikers, t86 tuning, x232 STRONG, x233 scripted econ, x234 forecaster, t87 mirror, x235 PUNISH,
x236 GROWERS, smoke; expected done about 22:55Z). Rule: at least v46 on every pool by W-D-L (the x226 condition must be a win again) -> v48
replaces v46; otherwise v46 stays and v48 is an alternative. No further freeze after this one (the end-of-run checks start at 00:30Z).

## 2026-10-31T22:39Z  v48 regression complete: at least v46 on every pool, one margin larger; FINAL RECOMMENDATION REVISED: frozen v48

Frozen v48 = v41 + factory_cap 1200 + finish_wrap + finish_robust_gold 400 + finish_gun_check 12 (gate on the whole roster) +
finish_defend_first (defence first; the smallest passing kill reserved; the capacity rule spends the whole slack under the reserve) + the
per-decision finish cache. `bot_research.bots.defense.frozen.v48.fortress:@make` (no parameters) or `...frozen.v48.fortress:decide`;
frozen 22:10:41Z by scratch/queue_ch.sh; live defaults reverted and checked. SHA256SUMS of bots/defense/frozen/v48/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  067af590c9d2fceef852cc4ac3516d31e01919993f98755cbed44a05d68c37f5  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Regression of the frozen artifact against frozen v46 (both seats, engine winner; every HP difference and end round equal to v46's unless
stated): x230 against best_v9e 7W-1D-2L and V29 9-0-1 (16-1-3); x231 strikers (32 opponents) 48-2-14; t86 tuning 102-2-0; x232 STRONG 22-2-2;
x233 scripted econ 16-0-0 (econ15 asym:23:2 seat 1 W +4160 r16 against v46's +3460 and v47's D +3740: the slack fix); x234 forecaster 1-9-2;
t87 mirror+eco 100-4-0; x235 PUNISH 32-0-2; x236 GROWERS 142-0-0 min +380; smoke 8 rounds 800 / -13. Longest decision 2.63 s (x231; v46's
5.29 s in the same pool was measured under a different load; both include the finish cache). Rejected actions 0, bot errors 0 everywhere.
Decision by the rule (at least v46 on every pool by W-D-L): v48 replaces v46 as the FINAL RECOMMENDATION of this lane; it also carries
astra review 12's two constructed-defect fixes (gun-check gate; no draw-to-loss in the dead-anyway fall-through) and check 13's slack fix.
Final version ladder of the lane (all frozen, all with full regressions): v48 (recommended) > v46 (same results, two constructed defects)
> v47 (one scripted draw) > v45 (two scripted draws) > v44 (factory cap only; loses the lead-bot races 3-3-4) > v41 (40-factory cap; 3-0-7).
Against the team's bots on the standard start every version is -5 to best_v9e (the round-1 exchange), 0-0 to P5TNUBM, +5 to V29/V25RM.
Known failures of v48 (unchanged from v41 unless stated): astra41 A/B -275/-260, guard_continuation and astra28 -65, timing -115, early tier4
strikers -43, forecaster tier4 r5 -60, V29 asym:3:2 seat 1 -12974 (its round-26 flood lands before any kill is affordable), best_v9e
standard -5; the padded finish relies on the response model (a heuristic upper bound; astra constructed two states where a stopping gun3 is
outside the 12 tested cells); matching in rounds <= 7 skips the attack step and so the restored finish (only an artificial state shows it).

## 2026-10-31T22:40Z  Addendum to the FOR THE LEAD entry (21:48Z): the final version is v48

The rows of point 3 (fortress against best_v9e and V29 on the five starts) are identical for frozen v48 (x230), v47 (x223) and v46 (x215); v48
is the lane's final recommendation (22:39Z). The reproduction command for the teammate table is in scratch form in the notes' run index: the
harness run `runs/defense/x230_v48_lead` (candidate `bot_research.bots.defense.frozen.v48.fortress:@make`, opponents
`bot_research.experiments.lead.frozen.best_v9e:decide` and hrt-w2's V29 spec, scenarios none mirror:1:2 asym:3:2 mirror:22:3 asym:23:2).

## 2026-10-31T22:53Z  x237: frozen v48 against V25RM, econ17 and econ15; fourteenth (final) astra review: remaining known failures of v48

`runs/defense/x237_v48_econbots` (frozen v48; five starts, both seats; (result, HP difference, end round) seat 0 / seat 1):
- V25RM (hrt-w2's frozen econ25 recommended spec): standard W +5 / W +5; mirror:1:2 W +3095 r19 / W +3095; asym:3:2 W +975 r17 / L -9370 r21;
  mirror:22:3 W +1680 r16 / W +1680; asym:23:2 W +2385 r17 / W +9822 r19. Total 9W-0D-1L (v41 in x200: 6W-0D-4L).
- econ17: 10W-0D-0L (standard +5 / +5; the scripted openings won in rounds 15-16, +835 to +2110). econ15: 10W-0D-0L (standard +5 / +5; rounds
  15-16, +920 to +4160). Longest decision 1.18 s; rejected actions 0, errors 0.
Astra review 14 (astra/v48-final/answer.md; state replays and log scans, no reruns; claims checked where stated):
1. The three constructed states of reviews 12/13 behave as intended with frozen v48 (capacity variant: 5 splash + 7 gun3 + 223 tier1 + 11
   tier5, win 790 : -55; draw-to-loss state: draw; gate witness: rejected).
2. Remaining failure classes (for the report):
   (a) construction responses the finish checks miss: the response planner is an upper bound and the single-gun3 test covers single guns on
   12 cells only. OBSERVED: x230 game 00006 (best_v9e, asym:3:2 seat 1) round 19, the mass finish 1 tier4 + 272 tier5 predicted 2800 and
   dealt 0 against best_v9e's same-round 4 gun3 + 4 gun2 + 2 gun1 (1180 gold); the match is the D +150 r21. OBSERVED: t87, gun_turtle under
   eco:2, both seats, round 13: 297 tier1 predicted 725 against 655 HP, dealt 585 after 23 gun2 (the fortress won the next round).
   CONSTRUCTED: the same x230 state with 32 more gold makes the default padded candidate (250 tier1 + 267 tier5, 177,300 gold) pass every
   check although the same ten-gun construction zeroes it; two constructed maps where the stopping gun3 is rank 15 or 53 (not emitted by
   the default search or already rejected by the response check). None of the five padded finishes in the v48 pools had a stopping single
   gun3.
   (b) matching (rounds <= 7) skips the attack step and therefore a restored finish: constructed only (an artificial fully-walled state;
   in the 1236 matching observations of the v48 logs no lethal finish was possible).
   (c) the response model's direction: a non-lethal planned response refutes a kill, a lethal prediction never certifies one; separately
   assuming a full-budget enemy defence (finish check) and a full-budget enemy attack (threat compositions) can be over-cautious.
   (d) the reserve's binary search assumes a monotone predicate; the attack step re-finds the kill instead of keeping the reserved purchase
   as a fallback; attack="flood" (not our setting) bypasses the retry. No tournament failure isolated to either.
   (e) decision time: the finish search's geometric flood sizes with millions of gold (all 1861 million-gold observations in the v48 logs
   had a splash-immune opponent, which skips them); the response planning per distinct candidate (5.05 s observed once in x209b; 2.63 s the
   largest v48 call in nine pools).
   (f) the 60-copy cap of the ordinary attack and the race rule, and factory_cap 1200: no demonstrated loss attributable to either.
Nothing of this changes the recommendation (no further freeze, as pre-stated at 22:14Z); it is the known-failures list of v48.

## 2026-10-31T22:55Z  Shift-4 summary (19:50Z-): what changed, what was measured, what is recommended, how to reproduce

Recommendation of the defense lane: frozen v48, `bot_research.bots.defense.frozen.v48.fortress:@make` (no parameters) or
`bot_research.bots.defense.frozen.v48.fortress:decide` (module-level entry, one make() instance per player renewed in round 1);
hashes in the 22:39Z entry and bots/defense/frozen/v48/SHA256SUMS. It is v41 (the shift-3 recommendation) plus five options whose
defaults are set in the frozen file: factory_cap=1200, finish_wrap=True, finish_robust_gold=400, finish_gun_check=12, finish_defend_first=True
(and a per-decision cache of the finish simulations). The live bots/defense/fortress.py keeps all options off (v34's policy) and plan.py's two
flags False; every frozen version is a byte copy of the package at its freeze time.

What the five changes do (decision rules; see the option docstrings in fortress.py for the exact conditions):
1. factory_cap 1200: the per-round factory purchase limit, formerly the constant 40 (a practical limit shared by every research bot, not an
   engine rule). Play is unchanged until the fortress holds more than 800 gold after defence and attack; afterwards its economy compounds
   (about 12 million gold at round 50 on the standard start instead of 577,000).
2. finish_wrap: the finish rule (all gold on a kill of the opponent this round, exact simulation on its current map) also tries the
   roster-padding candidate (tier1 up to the next multiple of 250 roster entries, then every affordable tier5), so the new tier5 spawn at
   ticks 0.. alongside the respawning tier5 already on the roster (entry k spawns at tick k mod 250); always with the response check.
3. finish_robust_gold 400: the opponent-response check (my planner spending the opponent's whole visible gold on its map) also applies to
   finishes of at most 60 copies while the opponent owns a turret and holds at least 400 gold.
4. finish_gun_check 12: a finish above the planner's 120-entry gun-pass limit (active roster + purchases) must also survive one gun3 on each
   of the 12 best legal cells of the opponent's map (exact simulation); a counterexample test, not a certificate.
5. finish_defend_first: in a round whose worst affordable flood is lethal, the planner's best defence is bought first and the kill with the
   remainder if it still kills; if the planner has no saving defence, the cost of the smallest passing padded kill is reserved, the defence
   steps (including the capacity rule, which may then spend the whole slack) run, and the attack step buys the largest affordable kill.

Measured (both seats, engine winner, deterministic engine; one run per condition; "unchanged" = v41's W-D-L): tuning 102-2-0, mirror+eco
100-4-0, STRONG 22-2-2, PUNISH 32-0-2, GROWERS 142-0-0 (min +380), strikers 48-2-14 on 32 opponents (v41's 48-2-8 on 29 plus the known
-275/-260/-43), forecaster 1-9-2 (v41 0-10-2), scripted econ openings 16-0-0 (v41 15-1-0); against best_v9e on five starts 7W-1D-2L (v41
3W-0D-7L; the standard start stays -5 both seats), against V29 9-0-1 (6-0-4), V25RM 9-0-1 (6-0-4), econ17 and econ15 10-0-0 each. Longest
decision 2.63 s in the v48 pools (5.05 s observed once for the same rules on the live module, x209b). The padded finish's effect is
concentrated on the obstructed scripted openings (mirror:22:3, asym:3:2, asym:23:2); on the standard start every version locks its map and
the games end at round 50 by the round-1 exchange.

Attribution (each step measured against the previous one on every pool before the next change): factory cap (x202a/b; v44 regression
x203-x208, t78, t79), padded finish and robust small finish (x209a/b/c; v45 regression x210-x214, t80, t81: two scripted wins became
same-round draws), gun check + defence first (v46 regression x215-x221, t82, t83: the draws are wins again), review-12 fixes (v47 regression
x223-x229, t84, t85: one scripted draw), slack fix (v48 regression x230-x236, t86, t87: all repaired). Diagnoses: x182/x202a traces (full maps,
factory counts; the finish rule's plain floods stopped by best_v9e's same-round guns), x222 (round-15 replay: capacity-rule defence skipped by
the finish-first early return). Astra reviews 10-14 (astra/fcap-rev2, v45-review, v46-review, v47-check, v48-final in the lane directory)
supplied the padded-finish idea, the response-check gaps and four constructed defect states, all reproduced with the live or frozen modules
(scratch/wrap_replay_live.py, r15_replay_live.py).

Known failures of v48: the 22:53Z list (observed: astra41 A/B -275/-260, guard_continuation/astra28 -65, timing -115, early tier4 strikers
-43, forecaster tier4 r5 -60, V29/V25RM asym:3:2 seat 1 -12974/-9370, best_v9e standard -5, mass finishes stopped by same-round
constructions in x230 and t87; constructed: a padded finish accepted against a ten-gun construction, matching suppressing a finish in rounds
<= 7, stopping guns outside the 12 tested cells).

Reproduction (from the project root, the environment of the prompt: PYTHONDONTWRITEBYTECODE=1, TMPDIR=bot_research/tmp, .venv/bin/python -B):
- smoke: `-m td_game.runner --balanced --bot-a bot_research.bots.defense.frozen.v48.fortress:decide --bot-b td_bots.protocol:idle --output
  bot_research/runs/defense/<unique>.jsonl` (runs/defense/smoke_frozen_v48_vs_idle.jsonl: 8 rounds, 800 / -13).
- any table above: `-m bot_research.harness.tournament --name <name> --out-dir bot_research/runs/defense/<name> --jobs 3 --candidates
  bot_research.bots.defense.frozen.v48.fortress:@make --opponents <specs> --scenarios none mirror:1:2 asym:3:2 mirror:22:3 asym:23:2
  --keep-logs losses`; the opponent specs and pool files are those of the run's results.jsonl rows (spec_a/spec_b), e.g.
  runs/defense/x230_v48_lead for best_v9e and V29. The harness plays both seats; results.jsonl holds hashes, HP, rounds, decision times.
- the regression pools: experiments/economy/opponents_tuning.txt (tuning, mirror), the lane's pool files are reproduced by the specs in
  runs/defense/x232_v48_strong, x235_v48_punish, x236_v48_growers, x231_v48_std results.

## 2026-10-31T23:16Z  Check script for the v48 finish rule added: experiments/defense/check_v48_x222.py

A self-contained replay test (read-only, 3 s) of the frozen v48 finish rule on the x222 game 00003 log (frozen v45 against econ17 under
asym:23:2, fortress seat 0): it rebuilds the observations from the logged snapshots, replays frozen v48 through round 15, checks that rounds
3-14 reproduce the logged actions and that round 15 buys 5 splash + 7 gun3 + 223 tier1 + 16 tier5 + 2 factories, and resolves round 15 with
the engine against econ17's logged actions: fortress 790, econ17 -755, winner 0. Command (project root, prompt environment):
`.venv/bin/python -B bot_research/experiments/defense/check_v48_x222.py` (exit 0 = passed; passed at 2026-10-31T23:16Z). Together with the
regression runs x230-x236/t86/t87 and the smoke run it is the lane's test evidence for v48; the engine replay is the authoritative check.

## 2026-10-31T23:27Z  For the lead (23:21Z request): the 3 s cutoff cannot have fired in a decision shorter than 3 s

Checked in the frozen v48 package (identical in v41 and v43-v47 for these lines): plan.py sets `deadline = t0 + TIME_BUDGET` (3.0 s) with t0
the start of the plan_defense call (lines 582-583) and compares the wall clock against it only inside that call: in the wall-prefix loop
(line 615, `i >= 2 or time.time() > deadline`) and between the steps of _gun_pass (line 513, `time.time() > deadline`). Every planner
call made by one decision (the mandatory, speculative, history, finish-first and response-check calls) is a separate plan_defense call with
its own t0, so a cut requires at least 3.0 s to elapse within ONE call, which a whole decision of at most 2.47 s (the harness's
decide_max_seconds wraps the complete decide call, match.py) cannot contain. The other wall-clock reads of the package: replan.py applies
a cutoff only when time_budget is given (the fortress passes none; 5000 deterministic annealing steps, line 134), and fortress.py,
simulate.py, geometry.py read no clock. So the statement "in frr1-frr5 no call of v41/v46/v48 reached 3 s, hence the cutoff was not
reached and those games do not depend on machine load through it" is correct for those games. Two qualifications: (1) it is a statement
per game, not per bot: a decision of 3 s or more (observed today: 5.05 s, x209b against counter_astra37 G, several response checks in one
decision) can contain a cut only if a single planner call exceeded 3 s, which the aggregate does not show either way; (2) the engine's
determinism makes identical conditions identical only if no call was cut, so load-independence of a game with a cut cannot be asserted.
frr5 (v48 4-4-12 against the frr1 bots, identical to v46): expected, the two differ only in states the frr1 pool does not reach.
