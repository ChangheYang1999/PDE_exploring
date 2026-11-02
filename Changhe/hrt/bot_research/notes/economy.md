# Economy and offense notes (lane hrt-w2)

Newest entry last. Times are UTC. Paths are relative to the project root.
All matches were played on the unchanged engine through the lead's harness
(`bot_research/harness/tournament.py`), both seats, fresh process per match.

## 2026-10-31T02:35Z Entry 1: tools, rule facts used, economy model, first bot measurements

### Tools written (owned files)

- `bot_research/bots/economy/fastsim.py`: exact replica of one map's combat
  (`td_game/combat.py` semantics) that groups copies by spawn tick. Copies born
  at the same tick move in lockstep and share a cell for the whole round, so a
  group is one object; guns hit the first live member of the frontmost
  in-range group, splash hits every member. Verified equal (hits and damage,
  and the defender's HP change) to `td_game.combat.simulate_map` on 300 random
  maps and rosters with seed 1 and 150 with seed 2, rosters up to 700 entries
  with mixed purchase rounds: 0 mismatches.
  Command: `.venv/bin/python -B -m bot_research.experiments.economy.check_fastsim 300 1`.
- `bots/economy/threat.py`: attack families used as the defender's threat
  model (pure tiers, greedy mixes, tier1 screens in front of heavier tiers,
  heavy-first with a cheap tail). They are a heuristic cover of the
  attacker's options, not an exhaustive one.
- `bots/economy/defense_plan.py`: slot-serpentine template (wall rows
  y=1,3,5,7,9, crossing gaps alternating x=0 and x=11, final route length 66,
  28 turret slots each adjacent to six route cells, 10 extra cells in row 11)
  and a greedy builder `defend(...)` that adds the bundle with the largest
  reduction of a surrogate threat per gold until the worst simulated leak over
  the families is at most a tolerance. `saturate(...)` adds splash until the
  per-copy splash on the route reaches a target.
- `bots/economy/offense.py`: attack-package search on the opponent's observed
  map (optimistic estimate: the opponent builds nothing; responded estimates).
- `bots/economy/econ.py`: the full bot, `bot_research.bots.economy.econ:@make`,
  parameters documented in its docstring.
- `experiments/economy/eco_model.py`, `summarize.py`, `run_tourn.sh`,
  `freeze.sh` (copies the bot to `bots/economy/frozen/<tag>/` so that a
  running tournament never sees edited code), `opponents_tuning.txt`
  (baselines plus hrt-w3's TUNING pool only; the held-out manifest was not read).

### Rule facts this lane relies on (read from the code)

1. Income is paid after combat each round: 15 per factory owned (including
   factories bought this round) plus the own route length. Gold received after
   combat of round 50 is never usable.
2. Every copy on a route of length L is attacked once at each index 0..L-1;
   arrival at index L is resolved before turrets fire. Per-copy splash damage
   is `S = 10 * sum_{i<L} a_i`, where `a_i` is the number of splash turrets at
   Chebyshev distance exactly 1 from route cell i. It does not depend on how
   many copies there are.
3. Only the owner builds on its map and buildings are never removed, so a
   player's route changes only when that player builds.

### Q1. Economy model

Proposition 1 (factory return). Hypotheses: bundled rules (cost 20, income 15
from the purchase round, 50 rounds, income after combat). A factory bought in
round r yields usable gold 15(50 - r), net 15(50 - r) - 20. It is positive for
r <= 48 and negative for r >= 49. Values: r=1: 715, r=10: 580, r=20: 430,
r=40: 130, r=47: 25, r=48: 10, r=49: -5. Proof: income is received after
combat of rounds r..50, of which rounds r..49 precede a decision.

Proposition 2 (compounding). Same hypotheses, route length 22, all gold to
factories every round, no cap: gold at decision time is 100, 97, 174, 291,
498, 865, 1497, 2619, 4571, 7983 in rounds 1..10. The ratio of consecutive
values tends to 1.75 (each 20 gold returns 15 per round). With the baselines'
cap of 40 factories per round the growth becomes linear from round 8 on (+600
income per round per round). With route length 66 from round 1 the sequence is
100, 141, 247, 433, 754, 1310, 2281, 3982 (not reachable in practice: the
walls cost gold in round 1). Spending only a fraction f of gold on factories:
round-9 gold 4571 (f=1), 3051 (0.75), 1791 (0.5), 876 (0.25).
Command: `python3 bot_research/experiments/economy/eco_model.py`.

Proposition 3 (path income). A wall that lengthens the own route by d steps
returns d gold per round from its purchase round, so it repays its cost of 1
in the same round when d >= 1. Walls are the cheapest income when they
lengthen the route, but walls on the template's turret slots destroy splash
capacity (each slot holds 60 of per-copy splash in the final serpentine).

Proposition 4 (saturation is permanent immunity). Hypotheses: player P's route
R (length L) has per-copy splash S >= h, and P builds nothing afterwards.
Then in every later round no copy with HP <= h reaches P's base, whatever the
opponent buys. Proof: by fact 3 the route stays R; by fact 2 every copy that
would reach index L first receives splash S >= h at indices 0..L-1 (it may
also receive gun damage), so it dies before arrival. With h = 1500 (tier5)
this covers every minion type. The template's 28 slots give S = 1720 when all
are splash (measured with MapModel: L=66), and 2020 with the 10 extra cells.
`saturate` reaches S >= 1600 from an empty map for 1587 gold (route L=62).

Consequence for the horizon. Gold only matters through damage dealt or
prevented. Once both players are saturated no further damage is possible in
the bundled rules, so factories pay in HP terms only until mutual saturation
(about 1600 gold of splash plus walls each), and the game is decided by the
HP difference accumulated before that. A player that is saturated while the
opponent is not keeps converting gold into damage until the opponent
saturates. This is a consequence of Proposition 4, not an empirical claim.

### First measurements: worst-case safety against the visible gold is a trap

Empirical finding (exact conditions below). The first bot version defended,
from round 1, against every attack family that the opponent's full visible
gold could buy (phi=1). Against opponents that only build factories for 6 to
10 rounds and then flood, it spent nearly all its income on defense against a
threat that had not yet been bought, never grew, and lost when the flood
came. Example, `runs/economy/econ_smoke1` (log of the match against
`baselines:@eco_then_flood`): our gold stayed at 110 to 160 per round in
rounds 2..8 while the opponent's gold went 174, 291, 498, 865, 1512, 2759; the
tier5 flood in rounds 8 and 9 took our HP from 800 to 380 to -460.

Parameter `phi` is the fraction of the opponent's visible gold assumed
spendable on attack before round `late_round` (after it, the full gold);
`phi=0` defends only against the opponent's already-visible active roster.

Sweep 1: `runs/economy/sweep1` (results.jsonl, summary.md). Candidates
`bots/economy/econ.py:@make` with the listed parameters, opponents the 26
specs in `experiments/economy/opponents_tuning.txt` (lead baselines and
hrt-w3's tuning pool), both seats, no scripted scenario, 52 matches per
candidate. W-D-L over the 52:

| parameters | W-D-L | losses against |
| --- | --- | --- |
| default (r1_factories=5, phi=1 from round 1) | 46-0-6 | eco_then_flood (switch 8 tier5; switch 11 tier5), eco6_t5 |
| late_round=4, tolerate=60 | 46-0-6 | same three |
| late_round=5, phi=0.5 | 46-0-6 | same three |
| late_round=6, phi=0.0 | 52-0-0 | none |
| r1_factories=0 (round-1 gold to defense) | 36-2-14 | rush tier3 eco 0.5, eco_then_flood x3, eco5_t3, eco6_t5, mixed5; draws vs pool turtle |

No rejected actions and no bot errors in any of the 260 matches; the largest
single decision took 0.755 s.

Interpretation (empirical, for this opponent pool only): growing first and
defending only against the visible roster for rounds 1..5 beat every tuning
opponent, while defending in round 1 with the starting gold lost 14 of 52.
This pool is weak; the claim says nothing yet about adaptive opponents.

### Failure found in self-play: template exhausted by guns, endgame floods

In self-play between these versions (first matches of a round robin that was
later discarded because a module was edited while it ran, see
`runs/economy/rr1_INVALID/README.txt`), both players reached rounds 46..47
with 150k to 430k gold and all 38 template cells filled, mostly with guns
(per-copy splash 580 and 720). At round 48 (`factory_stop=47`, end of the
growth phase) both spent everything on tier5 copies and both bases were
destroyed in the same round (draw). Cause: the greedy builder preferred guns
in the slots because they were cheaper against the small threats of the
early rounds, which removed the saturation option. Fix (version v2):
`reserve` (guns only where the completed template can still reach per-copy
splash 1600) and `saturate` (spend `sat_frac` of the gold left after defense
on splash slots from round `sat_from` on).

## 2026-10-31T02:53Z Entry 2: route lemma, Theorem B (Q2), the lock, self-play stalemate, timing probe

### Route lemma

Lemma 1. Hypotheses: the route is the one returned by
`td_game.pathfinding.shortest_path` (BFS from spawn to base; this is the
route used by `td_game.combat.simulate_map`). Then two route cells that are
4-neighbours are consecutive on the route. Proof: BFS returns a shortest
path; if cells at positions i and j > i + 1 were 4-neighbours, the path
through that edge would be shorter. So the route cells inside any set of
cells induce a linear forest (disjoint union of paths) of the 4-neighbour
grid graph.

Corollaries (same hypotheses).
(a) A 2x2 block contains at most 3 route cells (4 would form a cycle).
    Partitioning the 12x12 grid into 36 blocks: the route has at most
    sum over blocks of min(3, unbuilt cells of the block) cells, so its
    length is at most 107 on the empty map, and building more only lowers
    this bound.
(b) The 8 neighbours of a cell form an 8-cycle of the 4-neighbour graph, so
    at most 7 of them are route cells. A splash turret therefore deals at
    most 70 to a copy over its whole trip (10 per adjacent route cell).
(c) The cells within Euclidean range 2.5, 3.0, 3.5 of a gun (centre
    excluded; 20, 28, 36 cells) contain at most 15, 20, 27 route cells.
    Exact maximum induced linear forest by exhaustive search:
    `python3 bot_research/experiments/economy/induced_forest.py`.

### Q2. Theorem B: damage guaranteed against every same-round response

Setting. The attacker sees the defender's buildings B and gold G at decision
time and appends a package P = (t_1..t_n) after its e active entries, so the
j-th copy spawns at tick s_j = (e + j) mod 250. The defender then adds any
buildings of total cost at most G (it cannot see P and cannot remove
buildings). Engine facts used (td_game/combat.py): every turret acts once
per tick; a gun deals its damage to one copy within range; a splash deals
its damage to every copy at Chebyshev distance 1; a copy born at tick s is
at route index i at tick s + i, is attacked at indices 0..L'-1 and arrives
at tick s + L' if alive, which must be at most 249.

Definitions. L_max: the bound of Corollary (a) on the post-response route
length (or the current length if G is below the cheapest building cost).
Eligible copies E: those with s_j <= 249 - L_max. m: number of distinct
spawn ticks in E; span = min(250, s_max - s_min + L_max) over E. For k new
splash turrets and g = G - 60k gold on new guns:
S_k = 10 * sum over existing splash of min(7, unbuilt in-grid neighbours) + 70k;
Gamma_k = sum over existing guns of damage * min(span, m * c) (c from
Corollary (c), capped by the gun's unbuilt in-range cells) plus the largest
sum of damage * min(span, m * c) over integer gun combinations costing at
most g.

Theorem B. Under these hypotheses the copies of P deal at least
min over 0 <= k <= G/60 of [ sum of d_j over j in E with h_j > S_k  -  F_k ]
damage to the defender's base this round, where F_k is the optimum of the
fractional knapsack max sum d_j x_j subject to
sum (h_j - S_k) x_j <= Gamma_k, 0 <= x_j <= 1, over those j.

Proof. Fix a response with k new splash turrets; its new guns cost at most
G - 60k. By Corollaries (b) and (c) and the once-per-tick rule, every
eligible copy receives at most S_k splash damage over its trip, and the guns
deal at most Gamma_k damage to eligible copies in total (a gun can hit only
in ticks when some eligible copy is on an in-range route cell; copies with
the same spawn tick share the cell; there are at most min(span, m * c) such
ticks). An eligible copy with h_j > S_k that dies received at least
h_j - S_k gun damage, so the set K of such dead copies satisfies
sum_K (h_j - S_k) <= Gamma_k and sum_K d_j <= F_k. Every eligible copy that
does not die arrives, because s_j + L' <= s_j + L_max <= 249. Taking the
minimum over k covers every response. QED.

Implementation: `bots/economy/guarantee.py:bound(def_buildings, def_gold,
n_existing, pkg_types, rules)`.

Soundness and tightness check. `experiments/economy/guarantee_check.py`
computes the bound and the exact package damage (fastsim) after nine concrete
responses that spend the defender's gold: none, an omniscient greedy
(`defend` told the exact package), all splash, greedy guns on any free cell by
exact damage reduction per gold, 30 gold of serpentine walls then greedy guns,
serpentine walls then splash, and three random legal spends. The minimum over
the responses is an upper bound on the true guaranteed damage. Quick run
(`... guarantee_check runs/economy/guarantee/quick2.jsonl quick`; defender
maps empty, defend300, splash800, template_mid; G in {0, 100, 400}; 23
packages each; e = 0): 276 cases, 0 violations (bound never above the best
response found). The bound is conservative. Sums of bound / best-response
damage over the 23 packages per state:

| defender map | G=0 | G=100 | G=400 |
| --- | --- | --- | --- |
| empty | 4045 / 4045 | 668 / 2888 | 0 / 1280 |
| defend300 | 2576 / 2576 | 551 / 2368 | 0 / 1220 |
| splash800 | 980 / 980 | 265 / 980 | 0 / 560 |
| template_mid | 620 / 1340 | 0 / 1220 | 0 / 560 |

In this run the G=0 bound used the gun term for existing guns, hence the
gap on template_mid; `bound` now returns the exact simulated damage when the
defender cannot afford any building (no response exists). The gap at G>0
comes mainly from
Corollary (c): the bound lets each new gun see 15 to 27 route cells, which a
defender reaches only by also building a maze, while the tested responses
place guns next to the existing route (5 to 10 cells). Whether a defender
with G gold can realise coverage near 27 and still afford the gun is open;
the true guaranteed damage lies between the two columns.

Consequences (from the theorem; exact conditions as stated there):
1. Splash is the binding term for heavy copies: a copy is safe from splash
   alone only if h > S_exist + 70 floor(G/60). With no existing splash, tier5
   (HP 1500) passes this test for G < 1320 and tier4 (560) for G < 480.
2. Gun capacity depends on the number m of distinct spawn ticks, not on the
   number of copies. Several copies per spawn tick (only possible beyond 250
   active entries, since entry k spawns at k mod 250) raise the total HP the
   guns must remove without raising Gamma.
3. The clock: only copies with spawn tick at most 249 - L_max are counted
   (at most the first 143 ticks on any map). New entries come after the e
   active entries, which stay active for 12 rounds; a large roster of old
   cheap entries pushes new heavy entries towards the cutoff. With route
   length L' the engine itself discards every copy with spawn tick
   above 249 - L' (for the 66-cell serpentine: ticks 184..249).
4. Screens (cheap copies in front) cannot raise the bound, because the
   knapsack lets the defender choose which copies die; in the engine the
   gun must shoot the frontmost copy, so screens can only help the attacker
   in practice. Not yet measured.

### The lock (Proposition 5)

Proposition 5. Hypotheses: bundled rules; at some decision time player P's
route has per-copy splash S >= 1500 (the largest minion HP) and P never
again adds a wall or turret (factories and minions allowed). Then P's HP
never decreases again. If moreover HP_P > HP_Q at that time, P wins.
Proof: P's route never changes (only P builds on its map), so by
Proposition 4 no copy reaches P's base. HP changes only through arrivals
(`defender.hp -= damage` in td_game/combat.py), so HP_Q never increases. The
match ends by Q's base being destroyed or at the round limit, where
HP_P > HP_Q. QED. Consequence: once both players are saturated the result is
fixed; all that matters is the HP difference accumulated before the later
of the two saturates. Version v3 of the bot (`lock=True`) stops building
turrets and walls once its own per-copy splash is at least 1500.

### Self-play is a stalemate (empirical)

Round robin `runs/economy/rr2` (command: `experiments/economy/run_rr.sh rr2
""` with six frozen-v2 variants and `bots/economy/frozen/lead_best_a/best.py`,
a snapshot of the lead's `bots/best.py` taken 2026-10-31T02:41Z, sha256
e6b81009...; no scenario; both seats). Every v2-v2 match ended in a draw at
round 50 with HP 755-755 and 400k to 550k unspent gold on each side. In
each case the 45 damage came from round-2 and round-3 tier1 purchases
(6 then 4 copies) against a map with no turrets yet; afterwards both
players defended against the visible roster and saturated. v2
(late_round=6, phi=0) beat the lead snapshot in all 14 of its matches
(HP difference at round 50, or base destroyed in round 11 or 15).

### Timing probe (empirical)

`bots/economy/timing.py` (frozen p1): factories only before round r, one
all-in attack in round r (largest no-response damage on the opponent's
map), then defence and saturation (`repeat=True`: attack again every round
in which the opponent's per-copy splash is below 1500). Tournament
`runs/economy/probe1` against v2 (late_round 6 and 7) and the lead
snapshot, both seats. Against v2 late_round=6 it drew for r=2 and lost for
r=3..8 (HP difference -45 to -845): v2 attacks an undefended economy with
tier1 every round (its roster grew 6, 14, 26, 41 in rounds 2..5 of the r=5
match). With repeat=True and r=5 it beat v2 late_round=7 in both seats
(+702) but lost to v2 late_round=6 (-130). So late_round=7 has an
exploitable window; late_round=6 survived this probe.

## 2026-10-31T03:10Z Note for the lead: specs to use in pools

- Use frozen copies only. Recommended now:
  `bot_research.bots.economy.frozen.v2.econ:@make?late_round=6&phi=0.0` (v2, used in rr2 and
  probe1) and `bot_research.bots.economy.frozen.v3.econ:@make?late_round=6&phi=0.0` (v3: v2 plus
  the lock, Proposition 5). Each frozen directory has a SHA256SUMS file.
- `bots/economy/econ.py` is now v4 (frozen/v4) and will not change again: new versions go to new
  files (`econ5.py`, ...) so that pools that import the live `economy.econ` keep one version.
  `bots/economy/timing.py` gained two options with defaults that keep its behaviour.
- `defense_plan.py`, `fastsim.py` and `threat.py` will not change (hrt-w3's forecast_lock imports
  them live).

## 2026-10-31T03:27Z Entry 3: Q2 order effects, sweeps 3 and 4 (v3, v4), the round-1 poke question, the lead Planner

### Q2 consequences 2-4: screens, stacking, cutoff (exact one-round simulations)

Command (project root): `PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp .venv/bin/python -B -m
bot_research.experiments.economy.order_effects`, output `runs/economy/order_effects.txt`. The simulator
is `bots/economy/fastsim.py` (checked equal to `td_game.combat.simulate_map`, entry 1). One round, no
response. Maps: empty (L=22); the walls-only template (L=66); that template plus 2 gun3 (400 gold, L=66);
6 splash (per-copy splash S=300, L=28).

- Damage per gold when every copy arrives: tier1 0.333, tier2 0.300, tier3 0.260, tier4 0.231,
  tier5 0.215 HP per gold (damage/cost). Heavy copies are worth buying only for surviving.
- Screens (cheap tier1 copies in front of, between, or behind 4 tier4). On the maps where everything
  arrives they add exactly their own damage. On the 2-gun3 map 2 of the 4 tier4 arrive with 0, 2, 4, 8
  or 16 screens in front, interleaved or behind (no extra arrival; 5 tier4 give 3 arrivals). On the
  splash map the screens die and all tier4 arrive. 10 tier3 (1000 gold) arrive 0 times on both defended
  maps. Empirical, these four maps only: screens did not buy an extra heavy arrival against
  frontmost-first guns; extra heavy copies did.
- Stacking beyond 250 roster entries (two copies per spawn tick). Empty map: 250 copies give 228
  arrivals (spawn ticks 0..227 = 249-L reach the base), 300 give 278. 2-gun3 map: tier1 0 arrivals up
  to 500 copies and 178 at 750; tier2 0 up to 250, 40 at 300, 358 at 750; tier3 40 at 50, 174 at 250,
  546 at 750. Two copies on one tick share the guns' shots (one target per gun per tick), so stacks
  overwhelm guns. Splash hits every adjacent copy, so stacking does not help against S >= HP
  (Proposition 4).
- Cutoff. Entry e of the active roster spawns at tick e mod 250 and arrives only if that tick is at most
  249-L. Walls-only template (L=66, last arriving spawn tick 183), e old tier1 entries active ahead of 2
  new tier5: e = 0..182 both arrive, 183 one, 184..248 none, 249 one (the second tier5 wraps to tick 0),
  250..432 both, 433 one, 434 none. So an attacker with a large stale roster cannot land new heavy copies
  until old entries expire (lifetime 12) or the count passes 250. offense.search simulates the own active
  roster followed by the package, so it accounts for this.
- Lifetime: a copy bought in round r hits in every round r..r+11 in which it arrives. Econ v2..v4 valued
  only the purchase round; v6 (entry 4) counts later rounds.

### sweep3: v3 early guard (tuning pool of 26 plus v2, both seats)

`runs/economy/sweep3`, candidates `frozen.v3.econ:@make?late_round=6&phi=0.0` plus guard_gold in
{60, 100, 150, 250} and guard_gold=100&guard_tol=26. W-D-L: base 52-2-0, guard 60 50-4-0, guard 100
50-0-4, guard 150 50-0-4, guard 100 with tolerance 26 50-4-0, guard 250 48-2-4. Every early guard cost
factories and lost or drew against eco_then_flood and eco6_t5 (for example guard 60: -315 and -455).
The base setting stays.

### sweep4: v4 options (tuning 26 plus strong 11, both seats, 666 matches)

Command: `JOBS=3 experiments/economy/run_tourn.sh sweep4 bot_research/experiments/economy/opp_tuning_strong.txt ""`
with 9 candidates `frozen.v4.econ:@make?late_round=6&phi=0.0&...`. Opponents: `opp_tuning_strong.txt`
(the 26 tuning specs of `opponents_tuning.txt`, frozen lead_best_a and lead_best_b, frozen econ v2 and v3,
poke_lock with opening 1 and 2, forecast_lock, posterior_response, switching, maze_pressure,
predicted_pressure). Results `runs/economy/sweep4/summary.md`.

| variant (added to base) | W-D-L | non-wins (mean HP difference) |
| --- | --- | --- |
| base | 64-4-6 | lead_best_b -120, v2 and v3 0, poke_lock o1 -5, o2 -10 |
| r1_guard=30 | 62-4-8 | eco_then_flood -500, eco6_t5 -95, lead_best_b -96, v2/v3 -71 |
| r1_guard=30, guard_gold=60 | 54-4-16 | eco_then_flood -1005, eco6_t5 -380, lead_best_b -811 |
| r1_guard=30, early_attack_frac=0.3 | 66-2-6 | lead_best_b -49, v2/v3 -74, poke_lock o1 0 |
| r1_guard=30, guard_gold=60, early_attack_frac=0.3 | 56-6-12 | |
| r1_guard=30, early_min_cap=6 | 60-4-10 | |
| r1_units=1 | 64-2-8 | lead_best_b -73, v2/v3 -10, poke_lock o2 -5 |
| r1_units=1, r1_guard=30 | 60-4-10 | |
| early_attack_frac=0.3 | 64-0-10 | lead_best_b -23, v2/v3 -50, poke_lock o1 -5, forecast_lock -5 |

Failure mechanism of r1_guard alone (timeline of the eco_then_flood match): the round-1 defence leaves
3 factories instead of 5, and the attack then spends everything on tier1 in each early round with no
factories; the tier5 flood of rounds 8-9 ended in mutual destruction. Capping the early attack at 30%
of the gold (early_attack_frac=0.3) repairs it: against eco6_t5 r1_guard alone gives -95 and with the
cap +575. Variant [3] (r1_guard=30, early_attack_frac=0.3) is the best v4 setting on this pool and is
the default of econ6 (entry 4). Against v2 it loses -74: v2 pokes with 2 tier2 + 1 tier1 (round 2),
2 tier2 (round 3) and a tier3 (round 4) through the round-1 gun1s.

### Answer to the lead: is a round-1 tier1 attack worth its lost compounding?

Command: `KEEP=all JOBS=3 experiments/economy/run_tourn.sh r1poke bot_research/experiments/economy/opp_reactive.txt ""`
with candidates `frozen.v4.econ:@make?late_round=6&phi=0.0&r1_units=n`, n in {0, 1, 2, 4, 6} (n tier1
bought first in round 1, then (100-15n)//20 factories). Opponents (`opp_reactive.txt`): frozen econ v2
and v3 (late_round=6, phi=0), frozen lead_best_b, poke_lock opening 1, forecast_lock, predicted_pressure.
Both seats; every pairing gave the same result in both seats (deterministic bots), so each cell is one
distinct game. Per-match HP after rounds 1, 2, 5, 10 and factories/gold at round 10:
`python3 experiments/economy/econ_effects.py runs/economy/r1poke/results.jsonl 10`.

Mean final HP difference (factories own/opponent at round 10):

| opponent | n=0 | n=1 | n=2 | n=4 | n=6 |
| --- | --- | --- | --- | --- | --- |
| econ v2, v3 | 0 (76/76) | -10 (82/84) | -5 (54/103) | -5 (24/111) | -135 (12/20) |
| lead_best_b | -120 (41/39) | -73 (76/44) | -68 (53/37) | -84 (21/23) | -794 (2/14) |
| poke_lock o1 | -5 (85/144) | 0 (138/129) | +5 (83/238) | +15 (41/265) | +25 (7/303) |
| forecast_lock | +35 (86/221) | +26 (73/120) | +10 (91/268) | +10 (49/268) | +20 (6/268) |
| predicted_pressure | +23 (40/31) | +63 (20/61) | +5 (24/10) | +46 (12/11) | 0 (17/36) |

HP effect: every round-1 copy lands against these defenders (opponent HP after round 1 is 800-5n in all
games), because none of them builds a turret in round 1. After that the defenders answer the visible
roster and the HP exchange is decided by later rounds. Economy effect: n copies cost 15n gold, so
floor(15n/20) fewer round-1 factories, and the gap grows: at round 10, n=2 has 54 factories against
v2's 103, n=4 24 against 111, n=6 12 against 20 (v2 attacks the weaker economy and loses growth
itself). Against the lock-type defenders (poke_lock, forecast_lock) the 5n HP lead holds to round 50
because both sides stop everything afterwards, so n=4..6 wins by 15..25 there; against attackers that
exploit a smaller economy (v2/v3, lead_best_b) n=6 loses 135 and 794. Empirical answer, these
opponents and seats only: a round-1 poke of 1-2 tier1 is roughly neutral (from -10 to +63 across this
pool), 4 is neutral to slightly positive against locks and slightly negative against v2, and 6 is
dangerous. It wins only against bots that stop everything afterwards; its value is the 5n HP that a
lock keeps, not damage that compounds.

### Why the lead Planner (frozen lead_best_b) beat econ v4 (-120 in both seats)

lead_best_b pokes in rounds 2..9 with single heavy copies (tier2, tier3, 2 tier3, tier4) that econ's
phi=0 defence does not anticipate (it defends only the visible roster before round 6), and its 33-wall
opening gives about +24 gold per round of path income. Econ's own attack valued only the purchase round:
surplus = a*opt + (1-a)*resp - theta*net with theta=0.2 HP per gold and a=alpha=0.3 after the opponent
owned a turret. Against the Planner's splash-only map a tier5 lands 140 HP per round until the
Planner's per-copy splash reaches 1500, but the crude response model blocks it, the value is
0.3*140 = 42 against theta*net of about 130, and econ never bought it. This motivated v6 (entry 4).

### Note on hrt-w1's observation (defense.md 03:16Z) and the lead's c2rr1

Both used the default spec `econ:@make` (late_round=1, phi=1.0: defend against the opponent's full
visible gold from round 1). That setting buys turrets in rounds 2..3 against 93-100 visible gold and
falls behind in factories; it is the "worst-case safety is a trap" result of entry 1. In c2rr1 the
default spec lost -645 to eco6_t5, whereas `frozen.v4.econ:@make?late_round=6&phi=0.0` beat eco6_t5
by +705 in sweep4 (and +575 with r1_guard=30&early_attack_frac=0.3). Please use the parametrised specs
of the 03:10Z note (or econ6, entry 4) in pools; the bare `econ:@make` is not a recommended bot.

## 2026-10-31T04:04Z Entry 4: v6 persistence (no effect), alpha, v7 on hrt-w1's planner, the round-1 guard, v8

All runs in this entry: the lead's tournament through `experiments/economy/run_tourn.sh NAME
bot_research/experiments/economy/opp_key2.txt "" CANDIDATES...` (3 jobs, both seats, standard start, logs
kept for losses), results in `runs/economy/NAME/`. Opponent list `experiments/economy/opp_key2.txt` (27
specs): baselines rush tier1, rush tier2, eco_then_flood, eco_then_flood(switch 11, tier5), gun_turtle;
counters.pool archetypes heavy_t4, eco5_t3, eco6_t5, turtle, stacker, rush_t5; frozen lead_best_b and
lead_best_a (my snapshots of the lead Planner at 02:4x), frozen econ v2 and v3 (late_round=6, phi=0),
poke_lock (opening 1 and 2, reserve 0, saturate_round 20, phi 1), forecast_lock (opening 2, reserve 180),
posterior_response, switching, maze_pressure, predicted_pressure; hrt-w1 fortress frozen v9 (default,
annealed25, attack_from=6&attack_share=0.5); the lead's frozen best_v3b; frozen econ v4 with the sweep4
setting. hrt-w3's held-out pools and scenarios were not used. W-D-L counts matches (two per opponent).
"clip" is the mean over matches of the HP difference clipped to [-800, 800]
(`experiments/economy/compact.py RESULTS`, which also counts matches with bot errors; none unless stated).

### v6 = v4 sweep4 setting + persistence-aware attack value (sweep5): no effect

econ6.py (frozen v6) values a package for the later rounds k = 1..min(11, rounds left) in which the
opponent's visible gold plus k rounds of its income stays below block_k * (HP - lone-copy damage of its
current map). sweep5, candidates `frozen.v6.econ6:@make` with persist_w in {1 (default), 0.5, 0},
block_k in {0.5 (default), 1}, and theta=0.3: every persistence setting gave the same 36-6-12 with the
same HP difference in every pairing; theta=0.3 gave 30-10-14. Reason (checked on logs): in this pool the
opponent's visible gold almost always exceeds the cost of stopping a copy, so the counted later rounds are
0 for every type the search proposes. The term is kept (it costs nothing) but it is not a lever.
Non-wins of the default: lead_best_b -49, v2/v3 -74, fortress v9 -32, fortress v9 annealed25 -12,
best_v3b -49, draws with poke_lock o1, fortress attack variant and v4[3].

### alpha (sweep6)

Candidates `frozen.v6.econ6:@make?alpha=...`. alpha=1.0 (value = no-response damage even after the
opponent owned a turret): 40-4-10, beats fortress v9 (+28) and annealed25 (+74), loses lead_best_b -23,
lead_best_a -17, v2/v3 -62, best_v3b -23. alpha=1.0&theta=0.1 38-4-12 (fortress -6); alpha=0.6 38-4-12;
alpha=1.0&persist_w=0 identical to alpha=1.0. The crude response model (the defender spends all its
visible gold on splash and guns next to its current route) is too pessimistic against defenders that
pre-defend only a small speculative share; with alpha=0.3 econ never bought the heavy pokes that land.

### v7: this lane's economy and attack on hrt-w1's planner (econ7.py, frozen v7)

Defence from `bots/defense/frozen/v9/plan.py` (imported, not modified): layout walls of stage 0, the
lock check (own per-copy splash >= 1500 skips all defence), plan_defense against the visible roster, from
round 6 plan_defense against `threat_compositions` (full visible gold, spec_share 1.0, partial plans
allowed), saturation from round 6 with half the gold. Economy and attack of v6 with alpha=1.0. Round 1:
r1_guard=30 (zero-leak plan against 30 gold of purchases, partial plans not allowed).

smoke7 (live econ7, 3 opponents, both seats): fortress v9 +452 in both seats (econ7 landed a tier4 in
round 6, two tier3 in round 7 and a tier5 in round 10 while fortress pre-defended only its speculative
share), lead_best_b -23, v2 -13.

sweep7 (candidates `frozen.v7.econ7:@make` plus the options shown):

| variant | W-D-L | clip | non-wins (mean HP difference) |
| --- | --- | --- | --- |
| default (r1_guard=30) | 40-4-10 | +439 | eco6_t5 -450, lead_best_b -23, v2/v3 -13, best_v3b -23, poke_lock o1 0, fortress attack variant 0 |
| guard_gold=40 | 34-4-16 | +337 | eco_then_flood -750, eco6_t5 -870, lead_best_a -33, lead_best_b -20, v2/v3 -45, annealed25 -7, best_v3b -20 |
| guard_gold=60 | 34-4-16 | +337 | as guard_gold=40 |
| guard_gold=100 | 38-6-10 | +364 | eco_then_flood -510, eco6_t5 -915, lead_best_a -7, v2/v3 -50 |
| r1_guard=0 | 48-0-6 | +496 | v2/v3 -10, poke_lock o1 -5 |
| layout="lead_v3" | 44-4-6 | +479 | v2/v3 -2, annealed25 -2, poke_lock o1 0, fortress attack variant 0 |

Failure of the v7 default against eco6_t5 (log `runs/economy/sweep7/logs/*00015*`): eco6_t5 buys only
factories for six rounds (98 factories, 1497 gold at the end of round 6), then two tier5 per round and
never a turret. econ7 had built the round-1 gun1 (30 gold) and 20 layout walls, so it had 2 factories
after round 1 instead of 4 and 27 after round 5; from round 6 its unseen-purchase defence spent all gold
on gun3/gun2 partial plans against the affordable tier5 copies (they cannot be stopped with that gold),
bought no factory, and died in round 9 (-450). With r1_guard=0 the same bot has 4 factories after round 1
and beats eco6_t5 by +775.

Finding (empirical, this pool): every early insurance purchase made blind (round-1 guard, guard_gold in
rounds 2-5) lowers the result: the losses it prevents are 10-30 HP against early pokers, the losses it
causes are hundreds of HP against economy-then-flood bots, because the gold is missing from compounding
at the time the flood must be stopped. sweep3/sweep4 (entry 3) and hrt-w1's t9 (pure turtle with a
round-1 gun2, defense.md 03:51Z) show the same direction.

### v8 = v7 + the open case (econ8.py, frozen v8)

From round none_from=4, while the opponent has never owned a turret, the attack runs before the
unseen-purchase defence with none_frac=1.0 of the gold, copies are valued for their whole remaining
lifetime (no answer expected), and the value of a package is capped at the opponent's HP. Default
r1_guard=0 (from sweep7).

sweep8 (candidates `frozen.v8.econ8:@make` plus options):

| variant | W-D-L | clip | non-wins |
| --- | --- | --- | --- |
| default | 48-0-6 | +471 | v2/v3 -10, poke_lock o1 -5 |
| layout="lead_v3" | 52-0-2 | +450 | poke_lock o1 -5 |
| spec_splash=True | 48-0-6 | +459 | v2/v3 -10, poke_lock o1 -5 |
| none_from=6 | 48-0-6 | +481 | v2/v3 -10, poke_lock o1 -5 |
| none_frac=None, and layout="lead_v3"&none_frac=None | invalid | | bot errors in 20 and 22 matches |

The two none_frac=None rows are invalid: the harness parses spec values with json.loads, so `None` arrives
as the string "None" and decide raised in every open-case round. Use `null` (JSON) in specs. The valid
control (none_frac=null) is in sweep9.

Margins of the lead_v3 setting against the strongest opponents (both seats identical): fortress v9 +1,
annealed25 +78, fortress attack variant +140, lead_best_b +32, lead_best_a +29, best_v3b +32, v2/v3 +15,
eco6_t5 +209. The default layout has larger margins against most of these (fortress v9 +72, lead_best_a
+167, eco6_t5 +524) but loses -10 to v2/v3. The fortress v9 margin of +1 is fragile; this choice is not
settled by one pool.

Note on lead_v3 in this bot: the template's stage-0 walls (rows 1 and 3) are only 2 cells, so with
`layout="lead_v3"` the route stays 22 until plan_defense builds the next wall stages (round 6 in the
lead_v5 smoke log). The early path income therefore comes only from the default layout's 20 walls (route
40); that it does not help here is an empirical fact for this pool, not a claim about walls in general.

The remaining loss of every v7/v8 setting is poke_lock o1 (-5): one tier1 bought blind in round 1 lands
because v8 builds no round-1 turret, and afterwards both sides stop everything. Against v2/v3 the default
layout loses -10 to v2's round-2 poke of 6 tier1 against our turret-free route of 40 (log
`runs/economy/smoke8/logs/*00005*`): 30 HP in round 2 against our 20 HP of pokes in rounds 2-4.

### For the lead (specs to put in your pool; all frozen, files never edited)

- `bot_research.bots.economy.frozen.v8.econ8:@make?layout="lead_v3"` (52-0-2 on opp_key2) and
  `bot_research.bots.economy.frozen.v8.econ8:@make` (48-0-6, larger margins). Files: `frozen/v8/econ8.py`
  sha256 29b92591146ca44a2ac0488538ef38183cee24a58b9514a5b3d50f3eebc72baa; it imports
  `bots/defense/frozen/v9/plan.py` and the frozen/v8 copies of fastsim, offense, threat.
- v9 (`frozen/v9/econ9.py`, hrt-w1's frozen v11 planner, finishing attack, default layout lead_v3) is
  being measured in sweep9 against opp_key3 (opp_key2 + fortress v11 default and annealed25 + snapshots of
  your development bots v4 (03:22Z, sha d7870f3b...) and v5 (03:51Z, sha 6049108b...) in
  `bots/economy/frozen/lead_v4`, `lead_v5`). Smoke: v9 beats eco6_t5 +525 (round 7) and loses -5 to your
  v5 (your two blind round-1 tier1 land for 10 HP, our round-2 tier1 for 5; nothing lands afterwards).

## 2026-10-31T05:56Z Entry 5: v9 to v15, the scenario weakness, known-policy exposure, the finalist

Summary (details below; all results are empirical and hold only for the named pools, seeds and scenarios):
- Finalist: recommended spec for the lead's pool now: `bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak"`
  (frozen v15; specs, hashes and pending checks under "For the lead" below).
- Standard start, development pool opp_key4 (34 specs, both seats, 68 matches per setting): v13, v15 and v15 with
  `free_fallback="leak"` are all 66-2-0. The two draws are against poke_lock opening_units=1. Mean clipped HP difference:
  v13 +404, v15 +404 (identical to v13 in every pairing), v15 leak +411.
- Scripted openings (opp_scen9, 9 specs, 6 development scenarios, 108 matches per setting): v13 wins 46, mean clip -96;
  v15 wins 81, +349; v15 leak wins 88, +473. The gain comes from a layout-free fallback planner (freeplan.py) for maps
  on which hrt-w1's template planner finds no legal cell.
- Known-policy exposure (exact-forecast timing counters, 17 timings, both seats): v13 worst -60. Every early-insurance
  variant tried (econ14) is worse (-280 to -800), and so is late_round=4 (-560). The screen of v15 leak (known15l) is running: worst -26 after 4 of 34 matches.
- Defect report for hrt-w1 (frozen v15 plan.py): item 1 of the v15 section below.

### v9 (sweep9): the finish rule and hrt-w1's frozen v11 planner

econ9 = econ8 on hrt-w1's frozen v11 planner, with the finishing attack (`finish`: if some package kills the
opponent this round under the stated model, buy the cheapest such package before anything else) and default layout
lead_v3. Command: `experiments/economy/run_tourn.sh sweep9 bot_research/experiments/economy/opp_key3.txt "" CANDS`
(opp_key3.txt, 31 specs; both seats; 372 matches; 1026 s). Result rows (W-D-L, mean clip, non-wins with mean HP
difference):

| setting | W-D-L | clip | non-wins |
| --- | --- | --- | --- |
| default | 56-0-6 | +413 | poke_lock o1 -5, lead v4 -5, lead v5 -5 |
| finish=null | 56-0-6 | +395 | same three, -5 each |
| none_frac=null | 56-0-6 | +415 | same three, -5 each |
| finish="resp" | 56-0-6 | +395 | same three, -5 each |
| layout="default" | 56-0-6 | +435 | v2 -10, v3 -10, poke_lock o1 -5 |
| layout="pillars774" | 54-0-8 | +417 | lead_best_a -19, poke_lock o1 -5, lead v4 -5, lead v5 -5 |

finish="opt" matters only for the margin against eco6_t5 (+525 against +209 with finish off). All losses are -5:
one blind round-1 tier1 lands because v9 builds no round-1 turret.

### guarantee.py: exact arithmetic (after hrt-w3's audit)

hrt-w3's audit (validation.md, 04:00Z) found floating-point comparisons in the Theorem B bound. Since 04:12Z
guarantee.py uses Fraction arithmetic with explicit ceilings, and the detail field is JSON-safe. Regression with
experiments/economy/guarantee_check.py (the same 276 cases as entry 2): 0 violations
(runs/economy/guarantee/quick_exact.jsonl). This is a check on 276 cases, not a new proof; the soundness argument
is the one of entry 2.

### v10: deterministic planning time

hrt-w1's planner stops its search at a wall-clock deadline (`time_budget`). A wall-clock cutoff makes a decision
depend on machine load, so the same match can play differently on a busy machine. econ10 = econ9 with
`plan_time=1e6` (the deadline never binds; decisions are deterministic given the observation). Cost: decision time
is unbounded. Measured maxima of one decision (results.jsonl `decide_max_seconds`): v13 default 1.26 s (sweep13),
2.10 s (scen15); v15 default 2.24 s (sweep15), 2.33 s (scen15); v15 leak 3.48 s (sweep15, against pool:turtle;
that match took 65 s of decision time in total), 1.52 s (scen15). One outlier: v13 with `layout="default"` took
30.5 s for one decision against lead v5 (sweep13; 91.8 s in that match). Any time limit per decision in the final
evaluation would have to be checked against these numbers.

### v11 and v12: scripted openings

The standard start hides a weakness that the harness scenarios expose (scen10, 04:3xZ): under scripted openings v10
lost -488 (lead_best_b, mirror:1:2), -886 and -267 (lead_best_b, asym:3:2 seeds), -655 and -243 (v2/v3, asym:3:2).
econ11 = econ10 on hrt-w1's frozen v15 planner, which drops the layout's exclusions on a "foreign" map (more than 8
own buildings outside the layout). scen11s (opp_scen_small.txt, 6 specs; mirror:1:2, asym:3:2, eco:3; both seats;
72 matches) fixed v2/v3 (+800, +626) but not lead_best_b under mirror:1:2 (-488). Replay of that match (round 6,
experiments/economy/obs_replay.py): the lead_v3 template plan spent 498 of 519 gold and still leaked, while the
default layout had a zero-leak plan for 353 gold; from round 9 on no template cell was left.

econ12 = econ11 + `alt_layouts` (if the plan on the primary layout leaks, plan again on layout "default" and keep the
better plan). scen12s (same pool and scenarios): lead_best_b mirror -594, lead_best_a -146, fortress v14 -920
(v11: -20). Rejected.

### sweep10: the round-1 poke size (econ10 r1_units)

Command: `run_tourn.sh sweep10 bot_research/experiments/economy/opp_key4.txt "" CANDS` (opp_key4.txt = opp_key3 +
fortress v14 default and annealed25 + lead v6 snapshot, 34 specs; both seats; 408 matches).

| setting | W-D-L | clip | non-wins |
| --- | --- | --- | --- |
| r1_units=0 (v10 default) | 60-0-8 | +384 | poke_lock o1, lead v4, v5, v6: -5 each |
| r1_units=1 | 66-2-0 | +404 | poke_lock o1 0 (two draws) |
| r1_units=2 | 52-8-8 | +340 | lead_best_b -18, fortress v9/v11 -45, best_v3b -18; draws vs poke_lock o2, lead v4/v5/v6 |
| r1_units=3 | 62-2-4 | +352 | lead_best_b -15, best_v3b -15; draw vs econ v4 |
| r1_units=2&layout="default" | 56-6-6 | +381 | lead_best_a -2, v2/v3 -35; draws vs lead v4/v5/v6 |
| r1_units=4 | 52-0-16 | +327 | v2/v3 -56, lead_best_b -20, best_v3b -20, fortress v9/v11 -19, v14 -30, econ v4 -3 |

One blind tier1 in round 1 (15 gold) answers the opponents that poke once in round 1: both pokes land, nothing
lands afterwards, and the match is drawn instead of lost by 5. Larger pokes cost compounding: each tier1 bought in
round 1 is 15 gold that is not a factory (a factory bought in round 1 returns 15 per round for 49 rounds).

econ13 = econ11 with `r1_units=1` (frozen v13, econ13.py sha256
b6dba11ba22cf9804215d7d9f9d8710e9814948792da8e1c61660409db5a44b7).

### v13: sweep13, scen13, known13

- sweep13 (opp_key4, 136 matches): v13 66-2-0, clip +404 (draws: poke_lock o1); v13 `layout="default"` 62-2-4, +424
  (v2/v3 -3).
- scen13 (opp_key4 under mirror:1:2, asym:3:2, eco:3; 204 matches): mirror:1:2 44-0-24 (+273), asym:3:2 52-0-16
  (+365), eco:3 38-14-16 (+330). Worst rows (mean of both seats, unclipped): mirror:1:2 fortress v9 attack variant,
  lead v4, v5, v6 -1380 each.
- known13: `python3 known_econ.py full '{}' v13 > opp_known13.txt` gives 17 counters (hrt-w3's ForecastTiming,
  bots/counters/forecast_timing.py, wrapped in experiments/economy/known_econ.py with frozen econ13 as the model of
  our bot: tier3 at rounds 3-6, tier4 at 5-10, tier5 at 6-12, all gold, once). Each counter runs our frozen code
  on a copy of our observation, so it knows our purchases of the round, hidden ones included, before it decides; it
  defends against them (hrt-w3's use of frozen v2 defense_plan.defend) and buys its attack only if it gains on our
  predicted map. In all 204 matches of the known-policy screens of this entry we never finished ahead of a counter
  (our largest base damage dealt in one match: 12), so a draw is the practical best result. Worst -60. Four
  counters land, all before late_round=6: tier3 at 3 (-14), at 4 (-26), at 5 (-52), tier4 at 5 (-60). From round 6 on v13 insures against the opponent's full visible gold and nothing lands.

### v14: threat-triggered early insurance (rejected)

econ14 = econ13 + `early_threat`: before late_round, from round `early_from`, insure with `early_share` of the gold
when the worst roster the opponent can afford would deal at least `early_threat` damage on our map this round (exact
simulation with hrt-w1's frozen v15 simulate_leak). Each variant was screened against its own exact-forecast
counters (`known_econ.py full PARAMS v14`), 34 matches each:

| variant | worst | counters that land |
| --- | --- | --- |
| v13 (reference) | -60 | 4 of 17 |
| early_threat=20 | -800 | 9 of 17 (tier5 at rounds 9-11: -800 each) |
| early_threat=20&early_partial="best" | -800 | 9 of 17 |
| early_threat=50&early_partial="best" | -280 | 3 of 17 |
| early_threat=20&early_partial="best"&early_share=0.5 | -420 | 7 of 17 |
| v13 late_round=4 (k13lr4) | -560 | 4 of 17 (tier3 at 3, tier5 at 8-10) |

Early insurance closes the round 3-5 window but slows the economy, and a counter that waits until round 8-11 then
buys a tier5 our splash cannot stop. This agrees with the lead's finding (NOTES_FOR_TEAM 03:38Z and 04:57Z) that
graded early insurance is worse. Rejected; the v13 setting (no insurance before round 6) is kept.

### v15: layout-free fallback planner (freeplan.py)

Cause of the scripted-opening losses (replays of scen13 losses with obs_replay.py, 05:0xZ): on a map built by a
scripted opening, hrt-w1's planner often returns a leaking plan or no plan although gold suffices for a zero-leak
plan. Two mechanisms:
1. Planner defect (hrt-w1, frozen v15 plan.py): `_gun_candidates` (line 426) ranks cells by route coverage and
   returns the top 8 (line 452); the legality test `gk.legal_build` is applied only afterwards, in `_gun_pass`
   (line 491). Cells with the largest coverage lie in the middle of the route, where building cuts the route and is
   illegal, so all 8 candidates can be illegal while legal cells with smaller coverage exist. The splash pool has
   the same order (top 6 by template adjacency, lines 487-488, then the legality test; not measured). Suggested
   fix: apply legal_build before the cut. This lane does not edit w1's files.
2. Template exhaustion: when the map is not "foreign" (at most 8 own buildings outside the layout; the boundary is
   `> FOREIGN_LIMIT` with FOREIGN_LIMIT = 8, line 320-326), the planner keeps the template's exclusions; once the
   template's cells are taken or illegal, no candidate remains.

Measurement (experiments/economy/planner_cells.py; run at 2026-10-31T05:49Z from a scratch copy with the same code;
observations replayed with obs_replay.py from v13 against lead_best_b, seat 0, layout lead_v3; "legal in range"
counts empty cells other than spawn and base that pass gk.legal_build and have a route cell in range):

| scenario, round | foreign | own buildings outside layout | gun pool (each of gun1/2/3) | legal in pool | legal in range |
| --- | --- | --- | --- | --- | --- |
| mirror:1:2, 6 | no | 7 | 1 | 1 | 62 / 76 / 81 |
| mirror:1:2, 9 | no | 8 | 0 | 0 | 17 / 23 / 23 |
| mirror:22:3, 8 | yes | 38 | 8 (6 on the route) | 3 | 25 / 28 / 28 |
| mirror:22:3, 12 | yes | 40 | 8 (8 on the route) | 0 | 19 / 21 / 21 |

So in mirror:1:2 round 9 (exactly 8 buildings outside, not foreign) and in mirror:22:3 round 12 (foreign) the planner
has no legal gun cell although 17 to 23 legal cells in range exist.

freeplan.py (`free_plan(observation, budget, comps, partial, max_steps=15)`): greedy turret purchases on every legal
empty cell that is off the current route and is not the spawn or the base; a splash is offered only next to an
attack cell, a gun only where an attack cell is in range. Each step scores every (cell, kind) pair on the roster with
the largest current leak score (w1's score: 10 x leaked base damage + leaked HP, exact frozen v15 simulate_leak) after
recomputing the route with the engine's BFS, and buys the largest score reduction per gold.

econ15 = econ14 (early_threat off by default, so v13 behaviour) + `free_fallback`. Every plan_defense call goes
through one function: the w1 plan on the layout first; if it reaches zero leaks (or the HP target) it is kept.
Otherwise the fallback candidates are (a) free_plan alone and (b) the w1 plan followed by free_plan with the gold
left; for required-HP calls, plan_defense on an empty layout. The candidate with the best key (zero leak first, then
lower leak score, then lower cost) replaces the w1 plan only if it is strictly better. `free_fallback="empty"`
(default) runs the fallback only when the w1 plan is empty; `"leak"` also when it leaks; `null` is v14.

Frozen v15: econ15.py sha256 9833a1e5... (full hashes in bots/economy/frozen/v15/SHA256SUMS). Note: the frozen
docstring says "Reason (scen13, 2026-10-31T05:20Z)"; I wrote that time before 05:20Z, and scen13 had finished at
about 05:07Z. The live econ15.py docstring is corrected ("finished 2026-10-31T05:07Z"); the frozen copy is not
edited, so its hash stays as recorded.

### scen15 and sweep15

scen15: `run_tourn.sh scen15 bot_research/experiments/economy/opp_scen9.txt "mirror:1:2 asym:3:2 mirror:21:2
mirror:22:3 asym:23:2 asym:24:3" v13 v15 v15leak` (opp_scen9.txt: eco6_t5, lead_best_b, lead_best_a, econ v2
late_round=6&phi=0.0, fortress v9 attack_from=6&attack_share=0.5, lead v4, fortress v14 default and annealed25, lead
v6; both seats; 324 matches; 1350 s). W-D-L and mean clip per scenario (18 matches each):

| scenario | v13 | v15 | v15 leak |
| --- | --- | --- | --- |
| mirror:1:2 | 4-0-14, -264 | 18-0-0, +735 | 18-0-0, +759 |
| asym:3:2 | 10-0-8, -62 | 17-0-1, +622 | 17-0-1, +667 |
| mirror:21:2 | 14-0-4, +381 | 18-0-0, +776 | 18-0-0, +781 |
| mirror:22:3 | 2-0-16, -473 | 2-0-16, -580 | 6-0-12, -214 |
| asym:23:2 | 11-0-7, +77 | 15-0-3, +462 | 17-0-1, +648 |
| asym:24:3 | 5-0-13, -234 | 11-0-7, +81 | 12-0-6, +200 |
| total | 46-0-62, -96 | 81-0-27, +349 | 88-0-20, +473 |

Pool caveat: in every scen15 match, fortress v9 attack variant, lead v4 and lead v6 spent gold identically to the
unit (results.jsonl `spent`), so opp_scen9 has 7 behaviourally distinct opponents here, not 9. In opp_key4 the same
holds for lead v4/v5/v6, for lead_best_b/best_v3b and for fortress v9/v11 (identical margins in sweep13).

sweep15: `run_tourn.sh sweep15 bot_research/experiments/economy/opp_key4.txt "" v15 v15leak` (136 matches, 1996 s):
v15 66-2-0, +404 (equal to v13 in every pairing); v15 leak 66-2-0, +411. Pairings where v15 leak differs from v13
(mean of both seats): eco5_t3 +488 (v13 +462), lead_best_a +800 (+539), switching +709 (+493), forecast_lock
opening_units=2&reserve=180 +534 (+794). All are wins.

### mirror:22:3: a growth race, not a planner failure

v13 and v15 play the same actions to round 12 against lead_best_b under mirror:22:3 (timeline.py on the kept logs
runs/economy/scen15/logs/*00019* and *00127*). After the scripted rounds 1-3 we answer visible tier1-tier4 rosters
with turrets (rounds 4-10: gun1 x3, gun2, gun3 x2, splash x4) and attacks, so we hold 11-18 factories. lead_best_b
loses 24 to 72 HP per round to our attacks in rounds 6-13 but buys 8, 11 and 21 factories in rounds 6, 10 and 11 (61
factories at round 13, 87 at round 15) and one tier5 per round from round 12. Our per-copy splash is far below 1500
and our income (about 310 per round) does not buy enough turrets: we lose 140, 280, 280 and 420 HP in rounds 12-15
(v15). The scripted map (route 42) has no cheap lock.

growth1 (opp_growth.txt: lead_best_b, lead_best_a, v2; mirror:22:3 and asym:24:3; 48 matches): v15 leak variants,
mean clip over the 6 cells: base +81, spec_partial="none" +168, sat_frac=0.25 +372, spec_share=0.5 +106. No variant
improves every cell (sat_frac=0.25: lead_best_b mirror -674 against -620; spec_share=0.5: lead_best_a mirror -502
against +578). These variants were chosen on the cells they are measured on, so this screen is biased in their
favour. 

scen15s (`run_tourn.sh scen15s bot_research/experiments/economy/opp_scen9.txt "<the 6 scenarios>" v15leak&sat_frac=0.25`;
the pool and scenarios of scen15; 108 matches; 794 s): v15 leak with sat_frac=0.25 wins 95 of 108, mean clip +566
(mirror:1:2 18-0-0 +729, asym:3:2 17-0-1 +688, mirror:21:2 16-0-2 +695, mirror:22:3 14-0-4 +411, asym:23:2 18-0-0
+682, asym:24:3 12-0-6 +192), against 88 and +473 for v15 leak. Without the 12 matches of the growth1 cells (the cells
on which 0.25 was chosen): v15 leak 81-0-15, +523; sat_frac=0.25 86-0-10, +591 (v15 77-0-19, +430; v13 42-0-54,
-73). Pairings that sat_frac=0.25 makes worse (mean of both seats, clipped): fortress v14 under mirror:21:2 (-92
against +800) and mirror:22:3 (-800 against +800), lead_best_b under mirror:22:3 (-674 against -620). Its standard-start
result is not yet measured (sweep15s, opp_key4, running since 05:55Z); sat_frac lowers the gold per round spent on
splash saturation from round 6 on, so a later lock on the standard start is the risk to check.

### Running at the time of this entry (results in the next entry)

- known15l: `python3 known_econ.py full '{"free_fallback":"leak"}' v15 > opp_known15l.txt` (17 counters with frozen
  v15 leak as the model), then `JOBS=2 run_tourn.sh known15l bot_research/experiments/economy/opp_known15l.txt ""
  v15leak` (34 matches). First 4: tier3 at round 3 -14, at round 4 -26 (v13: the same values). These matches are slower
  than v13's: 128 to 133 s of wall time for the round-3 counter (v13 in known13: 9 to 10 s), of which 63 to 65 s are our decisions
  (largest single decision 4.0 s; 9.6 s in an aborted first launch that shared a core). The first launch was stopped
  after one match and restarted with 2 workers; its log runs/economy/known15l.log contains a traceback of the stopped
  worker, and results.jsonl contains only the restarted run.
- sweep15s: v15 leak&sat_frac=0.25 on opp_key4 (68 matches).

### For the lead: specs (all frozen; files never edited after freezing)

1. `bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak"`: recommended now. Standard start
   66-2-0 on opp_key4 (as v13), best measured on the scenario pool of the settings with standard-start results.
2. `bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak"&sat_frac=0.25`: better on the scenario
   pool, standard start and known-policy screen pending; use it only after the next entry confirms it.
3. `bot_research.bots.economy.frozen.v13.econ13:@make`: previous finalist (known-policy worst -60; weak on scripted
   openings).

Files: frozen/v15/econ15.py sha256 9833a1e5cbab7c23bbe4cebb02f56c701061418096acc5f4d9d7db9257b6a831, frozen/v15/
freeplan.py fe8f5d43e824ad39b9c0fd56cbcf84dabc79d074208d46b79cf4365778420d2e, frozen/v13/econ13.py
b6dba11ba22cf9804215d7d9f9d8710e9814948792da8e1c61660409db5a44b7. econ15 imports hrt-w1's bots/defense/frozen/v15
(plan.py, simulate.py), harness/gamekit.py and the frozen/v15 copies of fastsim, freeplan, offense and threat. All
hashes are in frozen/v15/SHA256SUMS and frozen/v13/SHA256SUMS; `sha256sum -c` in bots/economy at 05:56Z: all OK.
Decision time of spec 1 is larger than v13's (v10 section above and known15l above).

### Failure cases and uncertainty

- Every scenario is one seed and every pairing is deterministic; a scenario row is one map, not a distribution. The
  development seeds used by this lane are mirror:1:2, asym:3:2, eco:3, mirror:21:2, mirror:22:3, asym:23:2,
  asym:24:3. hrt-w3's held-out manifest was not read by this lane.
- The known-policy screen uses hrt-w3's ForecastTiming with our frozen code as its model. It covers single all-gold
  purchases of one tier at one round; mixed packages, repeated waves and counters that model our gold income
  differently are not covered. Against such a counter a draw is the best result, so "worst -60" is an exposure
  bound for these 17 timings only.
- Remaining losses: under mirror:22:3 and asym:24:3 the growth race against greedy opponents (above); fortress v14
  annealed25 under asym:24:3 (-128 for v15 leak). On the standard start no setting of v13/v15 loses a match in
  opp_key4, but the margins against lead_best_b (+17), fortress v9 attack variant (+5) and fortress v9 (+61) are
  small.
- Decision time is unbounded (plan_time=1e6); see v10 above.

## 2026-10-31T06:11Z Entry 6 (short, interim): recommendation 1 of entry 5 withdrawn; v13 stays the safe spec

For the lead: do not put `frozen.v15.econ15:@make?free_fallback="leak"` (entry 5, spec 1) into the pool as this lane's
finalist. Until the next entry, the recommended spec is again `bot_research.bots.economy.frozen.v13.econ13:@make`.

Measurements (empirical, standard start, both seats; harness tournament via experiments/economy/run_tourn.sh):
- known15l (v15 leak against its 17 exact-forecast counters, `experiments/economy/opp_known15l.txt`): worst -60,
  4 of 17 counters land (tier3 at rounds 3/4/5: -14/-26/-52, tier4 at round 5: -60), the same profile as v13 in
  known13. Candidate decision time: largest single decision 4.01 s, largest per match 65.4 s (v13: 0.33 s, 7.9 s).
- w3dev1 (`runs/economy/w3dev1`, opponents `experiments/economy/opp_w3dev.txt`: hrt-w3's development counters
  opening_response guard_poke5 + economy13, feature_bluff with the off-route gun1 in round 3 / round 1 / never,
  guarded_schedule tier1 r1 + tier4 r8 / r5, and hrt-w1's frozen fortress v21):

  | candidate | W-D-L | clip | non-wins |
  | --- | --- | --- | --- |
  | frozen v15 leak | 8-0-6 | +347 | guard -15, feature_bluff r3 -260, fortress v21 -5 |
  | frozen v15 leak&sat_frac=0.25 | 8-0-6 | +372 | same three |
  | frozen v13 | 10-0-4 | +485 | guard -15, fortress v21 -5 |
  | frozen v15 leak&r1_guard=15 | 10-0-4 | +53 | guard -835, feature_bluff r3 -435 |
  | frozen v15 leak&r1_guard=15&r1_units=0 | 14-0-0 | +468 | none |

  Every loss above is identical in both seats. v13 beats feature_bluff r3 by +705 (base destroyed in round 10); v15
  leak loses by -260 (own base destroyed in round 10).
- Cause (replay, `experiments/economy/diag_bluff.py`, v15 leak vs feature_bluff r3, player 0, round 6, own gold 613,
  opponent 805 gold and 52 factories, own route 22): hrt-w1's template plan against the unseen purchases costs 592
  (22 walls, 2 gun3, 3 gun1, 1 gun2), the free plan 600 (1 splash, 1 gun2, 2 gun3, 2 gun1, no walls). Both leak
  against 5 of the 8 sampled rosters (worst damage 140 each). The free plan has the lower leak score (6623 against
  7194), so "leak" buys it, and the route stays 22 long. The same choice repeats in round 7, and two tier5 per round
  hit from round 7 on. The leak score values only the current round; it gives the walls no value.
- Change: econ16 (frozen `bots/economy/frozen/v16`, econ16.py sha256
  6b495e876e1642ae9e31842d34df16243f94d49df8ed88da60602529d71ba363) adds `free_fallback="zero"`: a non-empty template
  plan is replaced only by a fallback plan with zero simulated leaks (or, in the saturation step, one that reaches the
  target). Defaults are those of v15. sweep16 (opp_key4 + opp_w3dev, 41 opponents, 328 matches) is running with
  v16 zero, zero&r1_guard=15&r1_units=0, leak&r1_guard=15&r1_units=0 and r1_guard=15&r1_units=0.

## 2026-10-31T06:51Z Entry 7: econ16 free_fallback="zero" is this lane's recommended spec; scripted maps and the final flood

For the lead (replaces entry 5's spec 1 and entry 6's interim advice). Recommended spec:
`bot_research.bots.economy.frozen.v16.econ16:@make?free_fallback="zero"`. Files: bots/economy/frozen/v16/econ16.py
sha256 6b495e876e1642ae9e31842d34df16243f94d49df8ed88da60602529d71ba363, freeplan.py 337be65f..., econ15.py 559a9d43...
(the v16 copies of econ15.py and freeplan.py differ from the frozen/v15 files in docstrings only); all 22 files in
frozen/v16/SHA256SUMS, `sha256sum -c` run from bots/economy at 2026-10-31T06:51Z: 22 OK. Imports: hrt-w1's bots/defense/frozen/v15
(plan.py, simulate.py, unmodified), harness/gamekit.py, and the frozen/v16 copies of fastsim, freeplan, offense and
threat. Fallback if the lead prefers the smaller decision time: `bot_research.bots.economy.frozen.v13.econ13:@make`
(sha256 b6dba11ba22cf9804215d7d9f9d8710e9814948792da8e1c61660409db5a44b7). Both are deterministic, read only their
observation and keep one flag per player (whether the opponent ever owned a turret).

What v16 changes (entry 6): the template plan of hrt-w1's planner is replaced by a layout-free plan only if the
layout-free plan has zero simulated leaks against the threat set (or reaches the splash target in the saturation step).
The leak mode of v15 also replaced a leaking template plan by a leaking free plan with a lower leak score, which lost
the walls (entry 6, bluff r3).

### Measurements since entry 6 (empirical; harness tournament via experiments/economy/run_tourn.sh, both seats)

All runs below use cores 25-27 with nice 19; opponent files are in experiments/economy; results in runs/economy/NAME.
"clip" is the mean HP difference with each match clipped to [-800, 800].

1. sweep15s (opp_key4, 34 opponents, standard start, 68 matches): `frozen.v15.econ15:@make?free_fallback="leak"&sat_frac=0.25`
   64-2-2, clip +421. Both losses are -5548 in round 48 against
   `bot_research.bots.economy.frozen.v4.econ:@make?late_round=6&phi=0.0&r1_guard=30&early_attack_frac=0.3`: that
   opponent stops buying factories after round 47 (factory_stop=47) and, with theta_end=0, spends all its gold on tier5;
   our map was full (0 empty cells) at per-copy splash S=940 < 1500, so nothing could be added. Rejected.
2. sweep16 (opp_key4w = opp_key4 + opp_w3dev, 41 opponents, standard start). I stopped it at 194 of 328 matches
   (by PID) after the third candidate's failures were clear; the fourth candidate (default fallback + G0) was not
   played. G0 = `r1_guard=15&r1_units=0`.

   | candidate (frozen v16 econ16) | matches | W-D-L | clip | non-wins |
   | --- | --- | --- | --- | --- |
   | free_fallback="zero" | 82 | 76-2-4 | +420 | guard_poke5+economy13 -15, fortress v21 -5, poke_lock (opening 1, reserve 0, phi 1.0) draw |
   | zero + G0 | 82 | 68-4-10 | +318 | frozen econ v2 and v3 late_round=6&phi=0.0: -6582 (round 48); lead_best_a -31; fortress v14 annealed25 -2 |
   | leak + G0 | 30 | 24-0-6 | +359 | -6582 vs econ v2 and v3 as above; lead_best_a -31 |

   Every non-win is identical in both seats. v16 zero gives the same HP difference as frozen v13 and frozen v15
   default (sweep15) in each of the 34 opp_key4 pairings, and beats feature_bluff r3 by +800 (v15 leak: -260). The
   -6582 losses are the same mechanism as item 1: G0 at round 48 had S=940 with 5 empty cells and no gold left to
   reach 1500 against all-gold tier5 bought after factory_stop. G0 rejected.
3. scen16 (opp_scen9, 9 opponents x mirror:1:2, asym:3:2, mirror:21:2, mirror:22:3, asym:23:2, asym:24:3, 108 matches):
   v16 zero 89-0-19, clip +474 (scen15: v15 leak 88-0-20 +474, v15 default 81 wins, v13 46 wins). Per scenario:
   mirror:1:2 18-0-0, asym:3:2 18-0-0, mirror:21:2 18-0-0, mirror:22:3 6-0-12, asym:23:2 17-0-1, asym:24:3 12-0-6.
4. Final-flood test. New wrapper `bot_research.experiments.economy.endflood:@make?base=SPEC` (URL-encoded base spec):
   from round 48 it keeps only the base bot's wall and turret actions and spends the rest of its gold on tier5, at most
   1000 per round. New script experiments/economy/lock_check.py: for each kept log, the first round in which the
   candidate's per-copy splash S is at least 1500, the final S and the number of empty cells.
   endflood1 (opp_endflood.txt: endflood around lead_v4, lead_v6, fortress v21, fortress v14,
   forecast_lock opening_units=2&reserve=180&saturate_round=20, frozen v13; standard start; 36 matches, all logs kept):

   | candidate | W-D-L | clip | non-wins |
   | --- | --- | --- | --- |
   | frozen v16 zero | 8-2-2 | +209 | endflood(v21) -5, endflood(v13) draw |
   | frozen v13 | 8-2-2 | +209 | the same |
   | frozen v15 leak | 6-2-4 | -57 clipped | endflood(forecast_lock) -80386 (round 48), endflood(v21) -5 |

   lock_check: v16 zero and v13 reach S >= 1500 in rounds 9 to 11 of every endflood1 match (final S 1550-1560). v15 leak
   against endflood(forecast_lock) ended with S=910 and 0 empty cells. lock_check on the standard-start runs sweep15, sweep16 and
   w3dev1 finds final maps with 0 empty cells and S < 1500 only for leak-mode settings (sweep15 v15 leak: 12 of 68
   logs; w3dev1 leak&r1_guard=15: 4 of 14) and for none of the v16 zero logs (0 of 82 in sweep16) or v15 default
   logs (0 of 68 in sweep15). sweep15s was not checked.
5. known16z (17 exact-forecast counters with model v16 zero, experiments/economy/opp_known16z.txt, 34 matches): worst -60,
   4 of 17 counters land (tier3 at rounds 3/4/5: -14/-26/-52, tier4 at round 5: -60), the same profile as v13 (known13)
   and v15 leak (known15l). Decision time of the candidate: largest single decision 4.51 s, largest total per match
   47.3 s (v13 in known13: 0.33 s and 7.9 s). In sweep16 the largest single decision of v16 zero was 5.37 s and the
   largest total 65.3 s; there were no bot errors or rejected-action errors in any run of this entry.
6. scenflood1 (endflood around lead_v6, fortress v21 and forecast_lock x mirror:1:2, mirror:22:3, asym:24:3; v16 zero
   and v13; 36 matches, all logs kept): every match ended by round 23 with a destroyed base, so the round-48 flood never
   fired; v16 zero 13-0-5, v13 6-0-12. On these scripted maps neither candidate reached S >= 1500 in any match (final S
   330 to 1080). The scripted openings place walls and turrets off the template, so the template cannot be completed.

### Proposition F: a full map below the lock cannot stop a large tier5 purchase (proof, bundled engine code)

Hypotheses, for one round r and one defender: (H1) at the start of round r every cell of the defender's 12x12 map is
either built or on its current route (lock_check reports 0 empty cells); (H2) the per-copy splash S of that map (10 times
the sum over route cells of adjacent splash turrets, gamekit.splash_total) satisfies S < 1500, the tier5 HP; (H3) the
attacker's active roster in round r contains n tier5 entries whose spawn ticks (roster index modulo 250) are at most
249 - L, where L + 1 is the number of route cells; (H4) n (1500 - S) > 250 D, where D is the sum of the per-tick damage
of the defender's non-splash turrets.
Conclusion: at least n - floor(250 D / (1500 - S)) tier5 copies reach the base in round r, each dealing 140.
Proof. The only actions are build_wall, build_turret, buy_factory and buy_minion; nothing removes a building. By (H1)
any new wall or turret would occupy a route cell. The route is a shortest path, so no two non-consecutive route cells
are adjacent; the free cells after the build would be the route minus one cell, which does not connect spawn and base,
and td_game/actions.py rejects such a build ("building would block every path"). Hence the defender's buildings
in round r are those at its start. In td_game/combat.py each non-splash turret adds its damage to at most one copy per
tick, so all guns together deal at most 250 D in the round. A copy that dies has received at most S splash (splash per
copy over the full route is S, and a copy that dies early receives less), so it received at least 1500 - S gun damage.
Hence at most floor(250 D / (1500 - S)) tier5 copies die. A copy that does not die and spawned at tick t <= 249 - L
reaches route index L at tick t + L <= 249 and hits the base. QED.
Remarks. (H1) and (H2) are properties of the defender's map that the attacker observes. The attacker's gold decides n;
in round 48 of item 1 the opponent had tens of thousands of gold. The proposition explains items 1, 2 and 4 (lead to a
destroyed base in round 48) but those matches were not checked against (H3) and (H4) individually. A bot that cannot
reach S >= 1500 must therefore keep empty legal cells for late splash; filling the map with guns or walls below the lock
is a terminal exposure against any opponent that grows and floods at the end.

### Finding: the growth race on scripted maps (empirical, mirror:22:3, v16 zero vs fortress v21)

Timeline (experiments/economy/timeline.py on the scenflood1 log; snapshot gold is the gold after the next round's
income): rounds 1-3 are scripted and identical. From round 4 to 7 v16 buys 5 tier1 (round 4), one tier3 in round 6 and
one in round 7, two gun1 and two gun2, and factories only in round 5 (4). After round 8 it has 12 factories against
v21's 40, after round 14 17 against 196; v21 buys tier4 and tier5 from round 11 and destroys our base in round 14. The
attack step (theta=0.2, attack_frac=1.0 from round 6) values the 26 HP of a tier3 above 100 gold of factories at a time
when the factories would compound for 40 more rounds.

Probe growth16 (tuning on the failure cases; opp_growth2.txt: lead_v6, fortress v21, fortress v14 annealed25,
lead_best_b; scenarios mirror:22:3, asym:24:3, mirror:1:2; both seats; 24 matches per candidate):

| frozen v16 econ16 free_fallback="zero" + | W-D-L | clip | mirror:22:3 losses |
| --- | --- | --- | --- |
| (nothing) | 13-0-11 | +84 | lead_best_b -620, lead_v6 -1514, v14 annealed25 -219, v21 -1239 |
| theta=1.0 | 16-0-8 | +247 | lead_v6 -428, v14 annealed25 -1265, v21 -985 |
| attack_from=11 | 22-0-2 | +581 | v21 -845 (both seats); every other cell is a win |
| early_attack_frac=0.0&attack_frac=0.3 | 16-0-8 | +206 | lead_v6 -434, v14 annealed25 -1179, v21 -985 |

attack_from=11 means no attack purchases in rounds 2 to 10 (the round-1 poke r1_units=1 is a separate step and stays).
These four settings were chosen after seeing the failure, and the probe's cells are the failure cells, so this is a
tuning result. Validation running at the time of writing: sweep17 (attack_from=11 and attack_from=8 on opp_key4w,
standard start, 164 matches) and scen17 (attack_from=11 on opp_scen9 x the 6 development scenarios, 108 matches). Do not
use attack_from=11 before the next entry reports them and a known-policy screen.

### Failure cases and uncertainty (v16 zero)

- Standard start: loses -15 to hrt-w3's opening_response guard_poke5+economy13 and -5 to hrt-w1's fortress v21; draws
  poke_lock opening 1. hrt-w3's three-policy cycle (cheap guard > econ13 > bluff r3 > cheap guard) applies to v16 zero
  too, since v16 zero equals v13 on the guard and beats bluff r3.
- Scripted openings mirror:22:3 and asym:24:3: growth-race losses of -219 to -1514 against greedy-economy opponents.
- Exact forecasters: worst -60 among 17 single-tier all-gold timings; mixed packages and repeated waves were not screened.
- Decision time up to 5.4 s per call and 65 s per match on one shared core; the engine imposes no limit that I know of,
  but a time-limited evaluation would hurt v16 more than v13.
- Every pairing is deterministic and every scenario is one seed; the 19 scenario losses come from 4 scenario-opponent
  families, so the counts overstate independence. hrt-w3's held-out pool and scenarios were not used by this lane.

## 2026-10-31T07:22Z Entry 8: econ17 (frozen v17) holds attacks on scripted maps; recommended spec for the lead

For the lead (replaces the recommendation of entry 7). Recommended spec:
`bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11`. File:
bots/economy/frozen/v17/econ17.py, sha256 ea98c5e7c2fe2ad00816c4f6f8a47ad617f98098014ec9343a8ca3065b40465d; the other 22
files in frozen/v17 are unchanged copies of the frozen/v16 files. `sha256sum -c frozen/v17/SHA256SUMS` run from bots/economy
at 2026-10-31T07:11Z: 23 OK. Imports: as v16 (hrt-w1's bots/defense/frozen/v15 plan.py and simulate.py, unmodified;
harness/gamekit.py; the frozen/v17 copies of fastsim, freeplan, offense, threat). The planner deadline is plan_time = 1e6
seconds after each call, so no wall-clock cutoff binds in a match and the bot is deterministic. State kept per player: the
opponent-turret flag, the set of cells at which it asked to build, and the foreign flag. Fallback 1:
`bot_research.bots.economy.frozen.v16.econ16:@make?free_fallback="zero"` (entry 7). Fallback 2:
`bot_research.bots.economy.frozen.v13.econ13:@make`.

### What v17 changes

econ17 = econ16 plus one parameter, foreign_attack_from (default None, off). The bot records every cell at which it requested
a wall or a turret. When its observed map has a building at a cell it never requested, the map is marked foreign for the rest
of the match; on a foreign map the attack step and the open-case attack buy nothing before round foreign_attack_from. The
finishing attack (a package that destroys the opponent's base this round) and the round-1 poke are not affected.

Observation (code-level argument, not a theorem about the engine in general): without a scripted opening, every own building
results from an own request, because the engine builds only requested cells and a rejected request leaves no building. Then
the foreign flag never becomes true and v17 returns the same actions as v16 in every round. The eco:K scenario places only
factories, so the same holds there. Consequently the gate acts only under the harness's scripted openings with buildings
(mirror:S:K, asym:S:K). In a game without such an opening v17 is v16, and the standard-start results of entry 7 (sweep16,
known16z worst -60, endflood1) carry over. A scripted building at a cell the bot also requested in a discarded scripted round
is not detected; the gate fires on the first building that does not match.

Why a gate and not a global attack hold: the growth race of entry 7 is a scripted-map effect. On the standard start the
round 2-10 pokes decide the close matches, and a global hold loses them (item 1).

### Measurements (empirical; experiments/economy/run_tourn.sh; both seats; cores 25-27, nice 19; clip as in entry 7)

1. sweep17 (opp_key4w, 41 opponents, standard start, 82 matches per candidate), econ16 with a global attack_from (no gate):

   | frozen v16 econ16 free_fallback="zero" + | W-D-L | clip | non-wins |
   | --- | --- | --- | --- |
   | nothing (sweep16, entry 7) | 76-2-4 | +420 | guard_poke5+economy13 -15, fortress v21 -5, poke_lock opening 1 draw |
   | attack_from=11 | 44-4-34 | +391 | 17 opponents lost in both seats, -5 to -85 (fortress v9, v11, v14 default and annealed25, lead_best_a -59, lead_best_b -21, best_v3b -21, lead v4/v5/v6 -5, econ v2/v3 late6 phi0 -15, econ v4 -5, guard_poke5+economy13 -37, fortress v21 -5); draws turtle and poke_lock opening 1 |
   | attack_from=8 | 72-2-8 | +483 | econ frozen v2 and v3 late_round=6&phi=0.0 -15, econ frozen v4 late6 phi0 r1_guard30 eaf0.3 -5, guard_poke5+economy13 -37; draw poke_lock opening 1; beats fortress v21 |

   Every non-win is the same in both seats. attack_from=11 as a global setting is rejected. attack_from=8 has the larger clip
   but twice the losses; not adopted (a lead for shift 2, see below).
2. scen17 (opp_scen9: pool eco6_t5, frozen lead_best_b, lead_best_a, econ v2 late6 phi0, fortress v9 attack_from=6&
   attack_share=0.5, lead_v4, fortress v14 default and annealed25, lead_v6; scenarios mirror:1:2, asym:3:2, mirror:21:2,
   mirror:22:3, asym:23:2, asym:24:3; 108 matches): econ16 zero + global attack_from=11 107-0-1, clip +736. Same conditions
   for v16 zero (scen16, entry 7): 89-0-19, +474. The single loss: eco6_t5 under asym:23:2, candidate in seat 1, -719 in
   round 11.
3. Frozen v17 at 06:57Z (econ17.py as above). scen18 (frozen v17 foreign_attack_from=11, the 108 scen17 conditions):
   107-0-1, clip +734, the same single loss. It differs from scen17 in one match only: frozen lead_best_b under asym:3:2,
   candidate in seat 0, +595 in round 10 against +890 in round 11. I did not examine why (logs of won matches are not kept).
4. std18 (frozen v17 foreign_attack_from=11 on opp_key4w, standard start, 82 matches): 76-2-4, clip +420; HP difference equal
   to v16 zero (sweep16) in all 82 (opponent, seat) pairs (experiments/economy/pair_diff.py: no differing key). This is the
   empirical check of the observation above.
5. scenw3 (opp_w3dev: hrt-w3's development counters guard_poke5+economy13, feature_bluff default, turret_round=0 and 3,
   guarded_schedule tier4 at rounds 5 and 8, and hrt-w1's fortress v21; scenarios mirror:1:2, asym:3:2, mirror:22:3,
   asym:24:3; 56 matches per candidate). These opponents were not used to choose the gate or the round.

   | candidate | mirror:1:2 | asym:3:2 | mirror:22:3 | asym:24:3 | total | clip |
   | --- | --- | --- | --- | --- | --- | --- |
   | frozen v17 foreign_attack_from=11 | 14-0-0 | 14-0-0 | 12-0-2 | 14-0-0 | 54-0-2 | +695 |
   | frozen v16 zero | 14-0-0 | 14-0-0 | 10-0-4 | 13-0-1 | 51-0-5 | +533 |

   v17's two losses: fortress v21 under mirror:22:3, both seats, -845 in round 14 (the growth16 case). v16 zero's five:
   guard_poke5+economy13 mirror:22:3 -840 (both seats), fortress v21 mirror:22:3 -1239 (both seats) and asym:24:3 seat 0 -997.
6. The eco6_t5 loss (timeline.py on the scen18 log). Rounds 1-2 are scripted and unequal: the opponent gets 3+3 factories, our
   seat 2+2 factories and one tier1. eco6_t5 buys only factories (71 after round 6) and never a turret; from round 7 it buys
   one or two tier5 per round. v17 holds its attacks (rounds 3-10), buys factories (31 after round 5, 47 after round 11) and
   from round 6 guns and splash, and is destroyed in round 11 with the opponent at 679 HP. v16 zero, which attacks the
   undefended opponent, wins the same match in scen16 (+445, round 8).
7. scen19 (frozen v17b, `...frozen.v17b.econ17:@make?free_fallback="zero"&foreign_attack_from=11&foreign_open=false`: the hold
   applies only once the opponent has owned a turret; econ17.py sha256 4760b017e49920ab97f58e9c3791c53be8a337df899f64d0538a72b3faf6dbb5,
   23 OK; the 108 scen17 conditions): 92-0-16, clip +554. It wins the eco6_t5 match (+445) but loses 16 matches that v17 wins,
   all under mirror:22:3 and asym:24:3 (lead_best_b -330 in both seats; lead_v4, lead_v6 and fortress v9 attack_from=6 each -134
   in both seats under mirror:22:3 and -1097 in seat 0 under asym:24:3; fortress v14 -699 and v14 annealed25 -879 in both seats;
   econ v2 late6 phi0 -929 in seat 0 under asym:24:3). By the code, v17b differs from v17 only in rounds before 11 in which the
   opponent has not yet owned a turret, so these losses come from attacks on opponents that had no turret yet: the growth race
   is lost whether or not the opponent defends. foreign_open=false is rejected; v17 keeps the default (True).

Running at the time of writing: v9a19 (v17 and v16 zero against the lead's frozen best_v9a,
experiments/lead/frozen/best_v9a.py sha256 88a8e42f..., standard start and the 7 development scenarios, 32 matches) and scen20
(foreign_attack_from=9 and 13 on the scen17 conditions, a sensitivity check of the round). Both go into the next entry.

### Failure cases and uncertainty (v17 foreign_attack_from=11)

- Standard start: identical to v16 zero (losses -15 to guard_poke5+economy13 and -5 to fortress v21, draw with poke_lock
  opening 1); hrt-w3's three-policy cycle applies unchanged.
- Scripted openings: fortress v21 mirror:22:3 -845 (growth race not removed); eco6_t5 asym:23:2 seat 1 -719 (an undefended
  greedy opponent with a better scripted start is allowed to reach tier5 unopposed).
- Selection: the round 11 was chosen on growth16, whose cells are failure cells of scen16, and all scenario evidence uses
  this lane's development seeds (mirror:1:2, asym:3:2, mirror:21:2, mirror:22:3, asym:23:2, asym:24:3). scenw3 adds new
  opponents, not new scenarios. hrt-w3's held-out pool and scenarios were not used; an independent check on them is needed.
- The gate is a detector of the harness's scripted openings. Its measured gain applies to evaluations that use such openings;
  it says nothing about which state variable should decide the attack timing. A state-based rule (for example: hold attacks
  while the opponent's factory count or income exceeds ours) would be more general; this is a conjecture to test.
- Every pairing is deterministic and every scenario is one seed; counts overstate independence.

### Independent checks by hrt-w3 (notes/validation.md)

- 07:02Z: Proposition F (entry 7) checked by an independent proof and component checks on four legally reached full maps;
  CONFIRMED for the capacity bound and the construction obstruction, with affordability and attacker survival as extra
  hypotheses.
- 07:04Z: certificate for the endflood1 round-48 loss of v15 leak (route 56, S=910, per-tick gun damage 717, 1000 tier5 of which
  776 can arrive; at most 303 can die). CONFIRMED.

## 2026-10-31T07:35Z Entry 9: v17 against the lead's frozen best_v9a; sensitivity of the hold round

### v9a19: frozen v17 and frozen v16 zero against frozen best_v9a (empirical)

Command (from experiments/economy): `JOBS=1 ./run_tourn.sh v9a19 opp_v9a.txt "none mirror:1:2 asym:3:2 eco:3 mirror:21:2
mirror:22:3 asym:23:2 asym:24:3" <v17 spec of entry 8> 'bot_research.bots.economy.frozen.v16.econ16:@make?free_fallback="zero"'`.
Opponent: `bot_research.experiments.lead.frozen.best_v9a:@make` (experiments/lead/frozen/best_v9a.py, sha256 88a8e42f954c...,
the lead's 06:11Z freeze). Both seats, 16 matches per candidate. HP difference in the candidate's view (seat 0 / seat 1):

| scenario | frozen v17 foreign_attack_from=11 | frozen v16 zero |
| --- | --- | --- |
| standard start | -5 / -5 (round 50) | -5 / -5 |
| mirror:1:2 | +812 / +812 | +900 / +900 |
| asym:3:2 | +850 / +826 | +1085 / +1045 |
| eco:3 | +80 / +80 (round 50) | +80 / +80 |
| mirror:21:2 | +812 / +812 | +997 / +997 |
| mirror:22:3 | +1054 / +1054 | -956 / -956 |
| asym:23:2 | +970 / +1075 | -1215 / -1225 |
| asym:24:3 | +997 / +847 | -1097 / -861 |
| total | 14-0-2, clip +609 | 8-0-8, clip +9 |

Standard start: best_v9a's round-1 poke (two tier1) lands for 10 and ours (one tier1) for 5; afterwards neither side's
attacks land; at round 50 both have about 1500 to 1650 factories (timeline.py on the kept log). This is the round-1 exchange
of entry 5 (sweep10: r1_units=2 or 3 cost more elsewhere).

Scripted openings, one traced case (match replayed with logs: runs/economy/v9a19_trace/v17_vs_v9a_mirror-1-2.jsonl, same
result +812 in round 13, so the replay is deterministic): best_v9a in seat 1 owns 3 turrets from round 4 to round 11 and buys
only factories (40 per round from round 8). In round 11 it has 5883 gold, route length 26, per-copy splash 70 and 85 empty
legal cells off the route; v17 has 2932 gold and buys 24 tier3, which deal 572. On that observation (replayed with
experiments/economy/obs_replay.py), this lane's layout-free greedy planner (frozen/v17/freeplan.py) finds a plan with zero
simulated leaks against all 11 threat compositions of the opponent's 2932 gold for 1970 gold (12 turrets); best_v9a bought
no turret in that round. So a zero-leak defence was affordable on that map and best_v9a did not buy it. The cause inside
best_v9a was not examined; conjecture: its template planner (hrt-w1 frozen v7) returns no plan once the scripted buildings
occupy the template, the failure this lane found in its own v11 to v14 (entry 5) and fixed with the layout-free fallback.
The lead may want to check best_v9a's insurance on this observation (seat 1, mirror:1:2, round 11).

### scen20: sensitivity of foreign_attack_from (empirical, the 108 scen17 conditions, frozen v17)

| foreign_attack_from | W-D-L | clip | losses |
| --- | --- | --- | --- |
| 9 | 102-0-6 | +696 | eco6_t5 asym:23:2 seat 1 -497; fortress v14 and v14 annealed25 mirror:22:3 -281 (both seats each); v14 asym:24:3 seat 1 -89 |
| 11 (scen18) | 107-0-1 | +734 | eco6_t5 asym:23:2 seat 1 -719 |
| 13 | 107-0-1 | +737 | eco6_t5 asym:23:2 seat 1 -785 |

Rounds 11 and 13 give the same W-D-L; 9 is too early against fortress v14 on mirror:22:3. The choice of 11 is not on a knife
edge at the upper side. All three use this lane's development scenarios.

Recommendation unchanged from entry 8: `bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11`.

## 2026-10-31T07:43Z Entry 10 (short): scenw3b, the asym:23:2 seat-1 weakness of v17

scenw3b (empirical; opp_w3dev, the 7 opponents of entry 8 item 5, under the two development scenarios scenw3 lacked,
mirror:21:2 and asym:23:2; both seats; 28 matches per candidate; from experiments/economy:
`JOBS=3 ./run_tourn.sh scenw3b opp_w3dev.txt "mirror:21:2 asym:23:2" <v17 spec> <v16 zero spec>`):

| candidate | W-D-L | clip | losses |
| --- | --- | --- | --- |
| frozen v17 foreign_attack_from=11 | 26-0-2 | +655 | feature_bluff default and turret_round=0, asym:23:2 seat 1, -719 each (round 11) |
| frozen v16 zero | 27-0-1 | +683 | feature_bluff turret_round=3, asym:23:2 seat 1, -470 (round 11) |

With scenw3 (entry 8), opp_w3dev over all six development scenarios: v17 80-0-4, v16 zero 78-0-6. The three v17 losses
under asym:23:2 in seat 1 (eco6_t5 in scen18, two feature_bluff settings here) all end -719 in round 11. This is one failure
mode, not three: in that seat the scripted rounds leave v17 behind in factories (entry 8 item 6), and holding attacks lets
a greedy opponent reach tier5 first. I conjecture that a hold conditioned on relative income (hold only while our income
is at least the opponent's) would remove it without losing the mirror:22:3 and asym:24:3 gains; not tested. The
recommendation of entry 8 stands, with this failure case added.

## 2026-10-31T09:05Z Entry 11: shift 2 of hrt-w2; fac_cap, a round-1 tier2, the late-flood loss to fortress v21, econ18 (frozen v18)

All runs on cores 25-27 at nice 19 with the unchanged engine and bundled rules; both seats; "clip" as in entry 7. Another
user's processes shared these cores during every run, so wall times are not comparable between runs.

### New opponent file opp_key5 (45 opponents)

experiments/economy/opp_key5.txt = opp_key4w (41) + the lead's frozen best_v9a, hrt-w1's frozen fortress v22, and two
settings of the lead's v15 (development file experiments/lead/v15.py, copied unchanged at 07:48Z to
bots/economy/frozen/lead_v15/v15.py, sha256 1b7485ef..., SHA256SUMS there, so that a later edit by the lead cannot change
this lane's opponents): V4 = `big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&
poke_reactive="turret"&fortress_n=4&immune_attack=true` and a C2-like setting with `attack_mode="robust"` and no fortress_n
or immune_attack. experiments/economy/opp_scen_new.txt holds these four lines for scenario runs.

### fcap1: the factory cap per round (empirical, standard start)

Hypothesis: the default `fac_cap=40` (at most 40 factories per round, a practical limit against huge action lists, not a
rule; RULES.md) slows growth. Command: `JOBS=3 run_tourn.sh fcap1 bot_research/experiments/economy/opp_key5.txt ""`
with frozen v17 `free_fallback="zero"&foreign_attack_from=11` and the same with `&fac_cap=120` and `&fac_cap=400`; 270
matches, 3262 s.

| fac_cap | W-D-L | clip | non-wins |
| --- | --- | --- | --- |
| 40 (v17 default) | 82-2-6 | +388 | guard_poke5+economy13 -15, fortress v21 -5, best_v9a -5 (each both seats); poke_lock o1 0 (both seats) |
| 120 | 82-2-6 | +388 | the same |
| 400 | 82-2-6 | +388 | the same |

89 of the 90 pairings per candidate have identical HP differences. The exception, frozen fortress v9 default with v17 in
seat 1, is +121 for fac_cap=40 and +61 for 120 and 400; std18 (entry 8) had +61 for the same fac_cap=40 condition. This is
not an effect of fac_cap: hrt-w1's planners cut their search after a wall-clock budget (TIME_BUDGET 3.0 s), so their
moves depend on machine load (hrt-w3 noted the mechanism earlier). It is one measured instance of irreproducibility in
this lane's tables: identical specs, identical engine, different HP difference. On the standard start the cap does not
change play. Other results of v17 here: best_v9a -5 in both seats (the round-1 exchange of entry 9), fortress v22 +195,
V4 +16 and C2-like +16 (each both seats).

### r1t2: a round-1 tier2 instead of a tier1 (empirical, standard start; REJECTED)

Hypothesis: the -5 losses against best_v9a and v21 and the -15 against guard_poke5 come from the blind round-1
exchange (best_v9a buys two tier1, 10 HP; v17 buys one tier1, 5 HP; guard_poke5 builds a gun1 at (3,1) that kills a
20 HP tier1 but not a 70 HP tier2), so one tier2 (40 gold, 12 damage) should turn them into wins.
Command: `JOBS=2 run_tourn.sh r1t2 bot_research/experiments/economy/opp_key5.txt ""` with frozen v17
`free_fallback="zero"&foreign_attack_from=11&r1_tier="tier2"`; 90 matches, 1242 s.

| round-1 purchase | W-D-L | clip |
| --- | --- | --- |
| one tier1 (v17, fcap1) | 82-2-6 | +388 |
| one tier2 | 76-0-14 | +285 |

The targeted pairings turned as predicted: best_v9a -5 to +2, v21 -5 to +2, guard_poke5 -15 to +15 (each both seats).
New losses, each in both seats: fortress v14 and v22 +195 to -38, feature_bluff turret_round=3 +810 to -270, econ v2 and
v3 late6 phi0 +32 to -23, lead v15 V4 and C2-like +16 to -3; lead_best_a/b fell from +539 to +22. The round-1 purchase is
chosen blind (both players see the same initial observation), so no observation-based rule can pick tier2 only against
the openings it beats. Kept: one tier1.

### Loss review: fortress v21 under mirror:22:3, seat 0 (frozen v17, -845 in round 14)

Tools: experiments/economy/capacity.py (route, splash, empty cells per log snapshot, and a greedy lower bound on the
splash-only capacity), timeline.py, and the new diag_flood.py (replays the match to a round and prints, for the
observation of one player, both players' state, the worst damage of hrt-w1's threat_compositions and the result of
four defence planners with the full own gold). Commands (from the project root, PYTHONPATH=.):
`python -B -m bot_research.experiments.economy.diag_flood '<v17 spec>' 'bot_research.bots.defense.frozen.v21.fortress:@make' 0 R mirror:22:3`
for R = 13, 14 (output runs/economy/diag_flood_v21.txt).

| decision of round | own HP | own gold | opp gold | own / opp factories | own S | empty cells off route | worst damage | best planner result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | 730 | 2411 | 4062 | 154 / 184 | 460 | 2 | 280 | no construction found (all four planners) |
| 14 | 730 | 4563 | 6660 | 194 / 224 | 460 | 2 | 840 | no construction found (all four planners) |

Our map was full from round 12 (L=42, 33 turrets, 66 walls), below the lock (S=460 < 1500). By Proposition F (entry 7) no
construction stops a large enough tier5 purchase; here no construction was even possible. v17 spent its gold on
factories, and v21 bought 10 tier5 in round 14 (840 damage). Hoarding on a full map is useless: gold can only buy
factories (whose return arrives later) or minions.

### econ18 (frozen v18): doom attack and income-conditioned hold

bots/economy/econ18.py = econ17 + two parameters, both off by default (so `econ18:@make` plays as `econ17:@make`):

- `hold_income` (float or null): the foreign hold of v17 applies only while own income >= hold_income x opponent income,
  income = factory_income x factories + path_income_per_step x route length from the observation. Target: the
  asym:23:2 seat-1 losses of entry 10 (v17 behind in factories, holding, the opponent reaches tier5 first).
- `doom` (false, true or "next"): after the defence steps, if the worst damage of threat_compositions on the own map
  with this round's construction is at least the own HP, spend all remaining gold on the offense.search package with the
  largest damage on the opponent's current map (no response model; ties to the cheaper), before factories. "next" also
  fires when the same test with the opponent's gold plus its visible income reaches the own HP and free_plan, with our
  remaining gold plus our income, finds no construction that brings that damage below the own HP. Reason for firing a
  round early: a roster entry attacks in every round of its 12-round life, so a package bought now attacks again next
  round together with next round's purchase. Both bases destroyed in the same round is a draw (engine.py:111-119).

Smoke tests against v21 under mirror:22:3 (live econ18 before the freeze, which is identical in code; both seats; runs
smoke18 and smoke18b, all logs kept):

| spec (econ18, all with free_fallback="zero"&foreign_attack_from=11) | result (both seats) | what happened |
| --- | --- | --- |
| doom=true | L -145, round 14 | fires in round 14 only: 7 tier5 (4550 of 4563 gold), 5 hit, 700 of v21's 735 HP |
| doom="next" | D (both destroyed, -5), round 14 | round 13: 3 tier5 (1 hit, 140); round 14: 4 more tier5, 5 of the 7 hit (700 vs 595 HP left) |
| doom="next"&fac_cap=400 | D -5, round 14 | the same |
| fac_cap=400 only | L -845, round 14 | as v17 |

Frozen at 2026-10-31T08:51Z as bots/economy/frozen/v18 (econ18.py sha256 7d1cc29a..., SHA256SUMS 25 files) with
experiments/economy/freeze.sh. Spec prefix: `bot_research.bots.economy.frozen.v18.econ18:@make?`.
Scenario evaluation (scen21a/b/c) follows in the next entry.

## 2026-10-31T09:33Z Entry 12: erratum on W-D-L counts; scen21a/b/c and scenw3d (v18); lock reachability; econ19 (frozen v19)

### Erratum: draws counted by the sign of the HP difference (entries 1 to 11)

Until 2026-10-31T09:21Z this lane's experiments/economy/compact.py, nonwins.py and pair_diff.py classified a match as
win, draw or loss by the sign of the candidate's HP difference. The engine declares a draw when both bases are at
HP <= 0 after the same round (reason `both_bases_destroyed`, td_game/engine.py:111-119), and such a match usually has
a nonzero HP difference. The three tools now use the results field `winner` (the candidate's seat, the other seat,
or null for a draw); the clip column (mean HP difference clipped to [-800, 800]) is unchanged. Corrected counts of
every earlier table of this file that contained a both_bases_destroyed match (run name under runs/economy):

| run (spec) | W-D-L as printed | W-D-L by the engine |
| --- | --- | --- |
| scen18 (v17 fa11) | 107-0-1 | 103-4-1 |
| scen17 | 107-0-1 | 103-4-1 |
| scen16 | 89-0-19 | 89-2-17 |
| scen19 | 92-0-16 | 92-6-10 |
| scen20 (foreign_attack_from=9) | 102-0-6 | 102-1-5 |
| scen20 (foreign_attack_from=13) | 107-0-1 | 103-4-1 |
| scen15 (v15) | 81-0-27 | 81-4-23 |
| scen15 (leak) | 88-0-20 | 88-2-18 |
| scen15 (v13) | 46-0-62 | 42-18-48 |
| scen15s | 95-0-13 | 95-3-10 |
| scen13 | 134-14-56 | 125-38-41 |
| scen10 | 120-9-49 | 117-19-42 |
| scen11s/12s | 17-0-19 | 16-6-14 |
| scen11s/12s (default layout) | 18-0-18 | 18-3-15 |
| sweep2 | 48-0-4 | 48-4-0 |
| sweep3 (gg60) | 50-0-4 | 50-4-0 |
| sweep3 (gg100) | 50-0-4 | 50-4-0 |
| sweep3 (gg250) | 48-0-6 | 48-2-4 |
| sweep4 (r1_guard=30) | 62-2-10 | 62-4-8 |
| sweep4 (early_min_cap) | 60-2-12 | 60-4-10 |
| sweep4 (r1_units=1) | 60-0-14 | 60-4-10 |
| w3dev1 | 10-0-4 | 8-2-4 |
| growth16 (zero) | 13-0-11 | 13-2-9 |
| growth16 (theta) | 16-0-8 | 16-2-6 |
| growth16 (af11) | 22-0-2 | 20-2-2 |
| growth1 | 7-0-5 | 7-1-4 |

Unaffected (no such match): std18, fcap1, r1t2, scenw3, scenw3b, v9a19, sweep17. Within each table the order of the
candidates by wins and by losses is the same under both counts except for one new tie (sweep4: early_min_cap and
r1_units=1 both 60-4-10, before 60-2-12 and 60-0-14; neither was adopted), so no decision of entries 1 to 11 changes; the recommendation of entries 8
and 9 (v17 with `free_fallback="zero"&foreign_attack_from=11`) stands. The scripted-scenario draws are mostly
mutual destructions in the same round (for example the four v14 fortress matches under mirror:22:3 in scen18).

### scen21a/b/c: hold_income and doom on the development scenarios

Conditions: opponents experiments/economy/opp_scen9.txt (9), scenarios mirror:1:2 asym:3:2 mirror:21:2 mirror:22:3
asym:23:2 asym:24:3, both seats, 108 matches per spec, frozen v18, all specs with
`free_fallback="zero"&foreign_attack_from=11`. Engine counts.

| spec | run | W-D-L | clip | where it differs from v17 |
| --- | --- | --- | --- | --- |
| v17 (baseline) | scen18 | 103-4-1 | +734 | |
| v18 hold_income=1.0 | scen21a | 96-6-6 | +632 | asym:24:3 12-0-6 (v17 18-0-0); asym:23:2 eco6_t5 loss to draw; asym:3:2 one new draw |
| v18 doom="next" | scen21b | 103-4-1 | +736 | mirror:22:3 v14 fortress pairs mean +37 to +97 (still draws) |
| v18 hold_income=1.0&doom="next" | scen21c | 96-6-6 | +637 | as scen21a |

hold_income is rejected: it removes the one asym:23:2 loss it targeted (to a draw) but loses six asym:24:3 matches
(fortress v9 attack_from=6, lead_v4, lead_v6, fortress v14 annealed25 and others; under asym:24:3 the hold is useful
while v17 is behind in income). doom="next" changes no outcome here.

On the w3 development opponents (experiments/economy/opp_w3dev.txt, 7 opponents, the same 6 scenarios, both seats,
84 matches; baseline = runs scenw3 + scenw3b): v17 80-0-4 +682; v18 doom="next" (scenw3d) 80-2-2 +701. The two
changed matches are the fortress v21 mirror:22:3 losses (-845, entry 11), now draws (-5). The two remaining losses
(feature_bluff under asym:23:2) are unchanged. std21 (doom="next" on opp_key5, standard start) is running.

### Lock reachability: experiments/economy/reach_check.py

`python -B -m bot_research.experiments.economy.reach_check SPEC_A SPEC_B PLAYER ROUNDS [SCENARIO]` (PYTHONPATH=.)
replays a match and at each listed round gives the observation of PLAYER, with own gold set to 10**7, to hrt-w1's
frozen v15 plan_defense with partial="none" and required_hp 1600 (econ17's sat_target) and 1500 (the tier5 HP), once
with the lead_v3 layout and once with the empty layout. "none" from a planner means it found no plan; it is not a
proof that no construction exists.

| match (v17 fa11 as player 0) | round | own S | empty cells | 1500 with lead_v3 | 1500 with empty layout |
| --- | --- | --- | --- | --- | --- |
| fortress v21, mirror:22:3 (reach_v21.txt) | 4, 6, 8, 10, 12 | 0, 0, 170, 380, 460 | 69, 44, 28, 19, 8 | none at every round | none |
| best_v9a, standard (reach_std_v9a.txt) | 2, 4, 6, 8 | 0, 0, 0, 490 | 119, 118, 118, 43 | cost 1531, 1651, 1651, 1020 | none |
| best_v9a, standard | 10 | 1580 | 2 | reached | reached |

Under mirror:22:3 the scripted rounds leave a map on which this planner finds no lock from round 4 on, yet v17 kept
buying splash (step 5, about 1020 gold in rounds 6 to 10) and guns (steps 3 and 4, about 1970 gold in rounds 4 to 12).
On the standard start lead_v3 keeps the lock reachable until it is built.

### econ19 (frozen v19): saturation only while the lock is reachable

bots/economy/econ19.py = econ18 + `sat_reach` (default false). With sat_reach=true step 5 (saturation) runs only if
the own map already has per-copy splash >= the largest minion HP (1500) or plan_defense with gold 10**7 and
partial="none" returns a plan reaching 1500 with `layout` or the empty layout. Steps 3 and 4 (visible and unseen
threats) are unchanged. Hypothesis (falsifiable on the scenario sets): when the lock is out of reach, saturation gold is
better spent on factories, which wins the tier5 race on scripted maps without changing standard-start play. Used with
fac_cap=400 (fac_cap does not change standard-start play, fcap1 in entry 11) and doom="next".

Smoke tests, spec `econ19:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true`,
live econ19, all logs kept:

| run | conditions | result | notes |
| --- | --- | --- | --- |
| smoke19 | fortress v21, mirror:22:3, both seats | W +1255 in both seats, round 12 | factories at round 10: 178 against 107; v21 bought 21 splash in round 10; v19 bought 4 tier5 in round 11 (v21 735 to 175 HP) and 1 in round 12 (v21 at -525). v17: L -845 in round 14; v18 doom next: D -5 |
| smoke19s | fortress v21 and best_v9a, standard start, both seats | 4 losses, each 790 against 795 at round 50 | identical to v17 in fcap1 against both and to v18 doom next in std21 against v21; largest decide time 9.1 s (v17 fac_cap=400 in fcap1: 16.1 s) |

smoke19 ran before the already-locked clause was added to the reachability test (it matters only when 1500 <= S <
1600; S stayed at or below 460 in that match); smoke19s ran with the final code. Frozen at 2026-10-31T09:31:38Z as
bots/economy/frozen/v19 (econ19.py sha256 755ac742..., SHA256SUMS 26 files). Spec prefix:
`bot_research.bots.economy.frozen.v19.econ19:@make?`. scen22 (v19 on opp_scen9 x 6 scenarios, 108 matches) started at
09:31:46Z; results follow in the next entry.

## 2026-10-31T10:05Z Entry 13: v19 results; fortress v25/v26 (hrt-w1); econ20 (frozen v20) with hrt-w1's re-planner

All counts are the engine's. Spec suffix of v19 below: `free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true`.

### v19 on the development sets

| run | conditions | v19 | baseline |
| --- | --- | --- | --- |
| scen22 | opp_scen9 x 6 scenarios, both seats, 108 matches | 107-0-1 +757 | v17 (scen18) 103-4-1 +734 |
| scenw3e | opp_w3dev x 6 scenarios, both seats, 84 matches | 82-0-2 +735 | v18 doom next (scenw3d) 80-2-2 +701; v17 80-0-4 +682 |

scen22 against scen18 (pair_diff.py): the four mirror:22:3 draws against fortress v14 (both layouts) are wins
(+1124 and +1065 in place of -5 or +37); the one loss (pool eco6_t5, asym:23:2) remains. scenw3e against scenw3d: the
two fortress v21 mirror:22:3 draws are wins (+1255 both seats); the two feature_bluff asym:23:2 seat-1 losses remain.
No pairing turned from a win into a non-win in either set.

### Fortress v25 and v26 (hrt-w1, frozen 09:17Z)

hrt-w1's x73 (runs/defense/x73_v25_econ17) showed fortress v25 beating v17 under mirror:1:2, mirror:22:3 and asym:3:2
and on the standard start (-15). Run w1new: opponents experiments/economy/opp_w1new.txt (fortress v25 and v26,
`@make`), starts none (standard), mirror:1:2, asym:3:2, mirror:22:3, asym:23:2, both seats, candidates frozen v19 and
frozen v17 fa11, 40 matches, all logs kept.

| candidate | all 20 | standard | mirror:1:2 | asym:3:2 | mirror:22:3 | asym:23:2 |
| --- | --- | --- | --- | --- | --- | --- |
| v17 fa11 | 8-0-12 -317 | 4-0-0 (+15) | 0-0-4 | 1-0-3 | 0-0-4 | 3-0-1 |
| v19 | 16-0-4 +323 | 4-0-0 (+15) | 0-0-4 (v25 -1020 r17, v26 -1600 r35) | 4-0-0 | 4-0-0 | 4-0-0 |

On the standard start v17 lost to v25 by -15 in both seats in hrt-w1's x73 (09:20Z) and won by +15 in both seats here
(09:34Z) with the same frozen code on both sides; v25's play depends on the machine load (hrt-w1's planners use a
wall-clock budget), so these four standard matches are not reproducible evidence either way.

Failure case of v19, mirror:1:2 against v25 (seat 0; experiments/economy/timeline.py on the w1new log): v25 pokes
with tier1 in rounds 3 and 4 (our HP 795 to 755), then builds 25 splashes in rounds 9 and 10 on its re-planned layout
(route 22 to 70) and takes no damage afterwards. v19 buys 12 splashes in rounds 5 to 7 and guns from round 9 (39
turrets, route 48, at round 16) without reaching the lock on the scripted map, grows far faster (339 against 57
factories at round 10, 138238 gold at round 17) and has nothing that can hurt an immune map; in round 17 v25 buys 21
tier5 and v19 ends at -225.

### econ20 (frozen v20): hrt-w1's re-planned layout on scripted maps, saturation after the hold

bots/economy/econ20.py = econ19 + three parameters, all off by default:

- `replan` (bool) and `replan_iters` (5000): at every decision, if the own map has buildings at cells this bot never
  requested, the set of those cells changed since the last re-plan, and hrt-w1's frozen v26 replan.needs_replan says
  that the current layout cannot reach S 1500, then replan.replan_layout(own buildings, iters=replan_iters,
  seed=round) designs a new MasterLayout, used from then on for the layout walls, plan_defense and the reachability test
  of sat_reach. No wall-clock cutoff, so the layout is a function of the observation. On a standard start every own
  building was requested by the bot, so the rule never fires and play equals v19.
- `foreign_sat_from` (int or null): on a foreign map (the flag of foreign_attack_from) step 5 is skipped before this
  round.

Smoke tests (live econ20, identical to frozen v20 in code; v25 and v26, the four scripted starts, both seats, 16
matches each, all logs kept):

| run | spec suffix after the v19 suffix | W-D-L | clip | mirror:1:2 | asym:3:2 |
| --- | --- | --- | --- | --- | --- |
| (w1new, v19) | | 12-0-4 | +400 | 0-0-4 (-1020, -1600) | 4-0-0 |
| smoke20 | `&replan=true` | 10-0-6 | +485 | 0-0-4 (v25 -35, v26 -55) | 2-0-2 (seat 0 -30 against both) |
| smoke20b | `&replan=true&foreign_sat_from=11` | 14-0-2 | +659 | v25 2-0-0 (+525), v26 0-0-2 (-55) | 4-0-0 |

mirror:22:3 and asym:23:2 were won in all three. smoke20, asym:3:2 seat 0 against v25: with the re-planned layout
reachable, step 5 bought 32 splashes in rounds 6 to 10; the bot had 214 factories and 3289 gold at round 10 against
v19's 329 and 4990 (v19 bought 6 tier5 in round 10 and won in round 11), found no kill before v25's lock and ended
770 to 800. With foreign_sat_from=11 the growth of v19 is kept until the hold ends, then the lock is built in one
round: smoke20b mirror:1:2 seat 0 against v25: 253 factories at round 9, round 10 3825 gold on 5 tier5, 2 tier4,
a tier2 and a tier1 (v25 795 to 235 HP), round 11 27 splashes (route 62) and from then on neither side takes damage;
final 760 to 235. Against v26 the round-10 package was not bought (v26 had 10 splashes at round 9 against v25's 7), the
round-11 tier5 met v26's lock, and the -55 of the round 3 and 4 pokes decided the match (740 to 795).

Frozen at 2026-10-31T10:04:32Z as bots/economy/frozen/v20 (econ20.py sha256 450fdbcfca541091..., SHA256SUMS 27
files). Spec: `bot_research.bots.economy.frozen.v20.econ20:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11`.
Running at the time of writing: std22 (v19 on opp_key5, standard, 90 matches; to be compared with fcap1 82-2-6 +388)
and scen23 (v20 on opp_scen9 x 6 scenarios, 108 matches).

## Entry 14 (2026-10-31T10:56:10Z): the re-planner costs eco6_t5 games; econ21 adopts a re-plan only for a large gain

### Standard start and v20 on the development scenarios

- std22, frozen v19 on opp_key5, standard start, 90 matches: 82-2-6, clip +388. Equal to fcap1 in every winner. One
  pairing differs in the HP difference: frozen fortress v9 `@make`, candidate in seat 1, 121 in fcap1 against 61
  here. This is the known nondeterministic v9 pairing from entry 12.
- scen23, frozen v20 on opp_scen9 x 6 development scenarios, 108 matches: 106-0-2, clip +747. v19 in scen22 went
  107-0-1, +757. v20 loses two matches that v19 wins, both against eco6_t5:
  - asym:3:2 seat 1: -790, round 10 (v19 +543).
  - asym:24:3 seat 0: -878, round 12 (v19 +831).

### Diagnosis: the re-planned layout, not foreign_sat_from (diag24)

Runs/economy/diag24: the frozen v19, frozen v20, and v20 with replan only (no foreign_sat_from; "v20R") against
eco6_t5 on asym:3:2 and asym:24:3, both seats, all logs kept.

| candidate | asym:3:2 s0 | asym:3:2 s1 | asym:24:3 s0 | asym:24:3 s1 |
| --- | --- | --- | --- | --- |
| v19 | W +710 | W +543 | W +831 | W +1325 |
| v20 | W +660 | L -790 | L -878 | W +657 |
| v20R (replan only) | W +790 | L -790 | L -878 | W +657 |

The hypothesis that foreign_sat_from caused the losses is falsified: v20R loses the same two matches with the same
HP. Mechanism, from experiments/economy/timeline.py and capacity.py on the asym:24:3 seat-0 logs:
- v19 builds 15 lead_v3 walls in round 6, and the route grows from 22 to 32.
- v20R builds the re-planned layout's walls instead. The route stays at 22.
- eco6_t5 attacks with tier5 from round 7, and the shorter route lets it through.

The re-planned layout is chosen for its splash score on the route it reaches once its splash cells are built. Its
walls alone rarely lengthen the route. This was measured with scratch scripts on the start states of the 18
scripted maps used here (the 6 development and 6 held-out scenarios, both seats where they differ). With only the
re-planned walls, the route is 22 on 16 of the 18 maps. With lead_v3's walls it is 22 to 48, for at most 33 gold.
A wall-first defence on a cheap long route is what holds eco6_t5's early tier5 under these starts.

### Score gain of the re-planned layout

Below: the per-copy splash S_final of a layout on its final route, built as far as the existing buildings allow,
for the re-planned layout ("new") and lead_v3 ("base"). This is hrt-w1's frozen v26 _score with 25 slots plus
the existing splashes (econ21._s_final). It is taken on the observation at round 3 (K+1 for K=2) or 4 (K=3),
replayed with idle bots, so it depends only on the scenario and seat. needs_replan is True everywhere except
asym:35:2 seat 1.

| map | new | base | gain |
| --- | ---: | ---: | ---: |
| mirror:1:2 | 1490 | 1080 | 410 |
| mirror:21:2 | 1310 | 830 | 480 |
| mirror:22:3 | 840 | 710 | 130 |
| asym:3:2 s0 | 1380 | 530 | 850 |
| asym:3:2 s1 | 1150 | 840 | 310 |
| asym:23:2 s0 | 1240 | 440 | 800 |
| asym:23:2 s1 | 920 | 470 | 450 |
| asym:24:3 s0 | 990 | 780 | 210 |
| asym:24:3 s1 | 1130 | 750 | 380 |
| held-out: mirror:31:2 / asym:32:2 s0, s1 / mirror:33:3 | | | 480 / 240, 190 / 310 |
| held-out: asym:34:3 s0, s1 / asym:35:2 s0, s1 / mirror:36:3 | | | 500, 550 / 130, 50 (no re-plan) / 140 |

The two eco6_t5 losses have gains of 310 and 210. The v25 win on mirror:1:2 (smoke20b, +525) has a gain of 410.

### econ21 (frozen v21): replan_gain

bots/economy/econ21.py = econ20 + `replan_gain` (int or null, default null = econ20). When the re-plan rule of econ20
fires, the new layout is adopted only if its S_final exceeds that of the current layout by at least replan_gain. Either
way the alien-cell set is recorded, so the rule does not run again until the set changes. replan_gain=400 was chosen
from the table above. That is tuning on the development maps: the threshold lies between the loss gains (210, 310)
and the mirror:1:2 gain (410). The held-out maps were not used for the choice. Their gains were computed after the choice,
only to see which side of 400 they fall on: only mirror:31:2 and asym:34:3 (both seats) are above it.

replan_layout runs with time_budget=None (a fixed 5000 steps from seed=round), and every plan_defense call passes
plan_time=1e6. So v21 has no wall-clock cutoff, and its actions are a function of the observation and its own state.
On a standard start the re-plan rule never fires, so v21 plays as v19.

Frozen at 2026-10-31T10:30:29Z as bots/economy/frozen/v21 (econ21.py sha256 35cbb8a43216a8ff..., SHA256SUMS 28 files).
Spec:
`bot_research.bots.economy.frozen.v21.econ21:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400`

### Measurements

- smoke21: live econ21 with replan_gain=400 (same code as frozen v21). Opponents eco6_t5 and hrt-w1's fortress v25
  and v26, on mirror:1:2, asym:3:2, asym:24:3 and asym:23:2, both seats, 24 matches, all logs: 20-0-4.
  - eco6_t5: 8-0-0, including asym:3:2 s1 +543 and asym:24:3 s0 +831, the two v20 losses.
  - v25: 7-0-1. The loss is asym:24:3 s0, -2993, round 35.
  - v26: 5-0-3. Losses on mirror:1:2, -55 in both seats, and asym:24:3 s0, -833 in round 28.
- scen24: frozen v21 on opp_scen9 x 6 development scenarios, 108 matches: **108-0-0, clip +777**. For comparison,
  v19 went 107-0-1 +757 (scen22) and v20 106-0-2 +747 (scen23). Per scenario every cell is 18-0-0. The clip is
  +736 to +798 per scenario. Mean candidate decide time per match is 4.4 s; the largest single decision took 6.6 s.
- diag25: frozen v19, v20 and v21 against v25 and v26 on asym:24:3, mirror:21:2 and mirror:22:3, both seats, all logs.
  v25 and v26 have a wall-clock budget, so every cell is one sample of a load-dependent opponent, not a reproducible
  result.

| candidate | opponent | asym:24:3 s1 / s0 | mirror:21:2 (both seats) | mirror:22:3 (both seats) |
| --- | --- | --- | --- | --- |
| v19 | v25 | W +812 / L -2993 | L -2014, L -2014 | W +1250 x2 |
| v19 | v26 | W +952 / L -833 | W +948 x2 | W +1245 x2 |
| v20 | v25 | W +962 / L -1453 | W +790 x2 | W +840 x2 |
| v20 | v26 | W +962 / L -2153 | L -2272 x2 | W +2088 x2 |
| v21 | v25 | W +812 / L -2993 | W +790 x2 | W +840 x2 |
| v21 | v26 | W +952 / L -833 | L -1022 x2 | W +2088 x2 |

### Rejected: econ22 (race)

econ22 = econ21 + `race`. With race=true, the foreign hold of attacks before round 11 is lifted while the own lock is
out of reach (the sat_reach test fails). Hypothesis: on a map where we cannot lock, holding only gives a locking
opponent time. smoke22 used the smoke21 conditions plus mirror:21:2. It was killed at 25 of 36 matches because it was
already clearly worse than v21:
- mirror:21:2 against v25: L -901 and L -2441 (v21: W +790 x2).
- eco6_t5 mirror:1:2: D -27 x2 (v21: W +293 x2).
- v25 asym:3:2 seat 1: L -1790 (v21: W +805).
- v26 asym:24:3 seat 0: L -905, round 13.

The only improvement was asym:24:3 seat 0 against v25, from -2993 to -693, still a loss. The hold, plus the strike
it saves for round 11, is what wins these scripted lock races. econ22 is not frozen.

### Failure cases of v21

1. asym:24:3 seat 0 against a locking fortress (v25, v26): lost by v19, v20, v21 and econ22. From smoke21 log 00013
   (against v25): the lock is out of reach on the kept lead_v3 map, since the gain is 210 < 400. The bot holds to
   round 11 while v25 locks in rounds 10 and 11. It then grows to 10051 factories against 1021, and v25 buys 275 tier5
   in round 35. This is Proposition F (entry 7): the map is full with S < 1500, and a large enough tier5 purchase
   gets through whatever the economy. I have no fix. The only counter visible is to kill before the opponent's lock
   (rounds 10 and 11 here), which the hold forbids, and econ22 shows that lifting it costs more elsewhere.
2. mirror:21:2 against v26: L -1022 in both seats; v19 won +948. In this game v26 built 26 splashes in rounds 9 and
   10 and was immune before our round-11 strike. In v19's game it had only 12 splashes by round 10, and v19's 8 tier5
   in round 11 won. I cannot tell whether v26 reacted to our play or this is its load-dependent variance. On our side,
   at round 13 v21 built 20 splashes reaching only S 820 at route 44. The capacity greedy maximum was also 820, while
   the re-planned S_final was 1310 at route 56: guns placed earlier by the defence steps and the free fallback took
   cells of the re-planned layout. Idea, not implemented: on a re-planned map, keep defensive purchases inside the
   layout's cells.
3. mirror:1:2 against v26: -55, from the round-3 and round-4 tier1 pokes in a match that ends lock against lock (as v20).

### For the lead (09:33Z request, 10:28Z note)

Your 10:28Z note prefers econ20 as the foreign target because it has no wall-clock cutoff. econ20 (frozen v20)
carries the two eco6_t5 losses above. v21 removes them, keeps econ20's v25 wins on mirror:1:2 and mirror:21:2, and
is equally free of wall-clock cutoffs. My candidate for a foreign_target / switch target is the frozen v21 spec above.
Caveats:
- It was tuned on the 6 development scenarios.
- It loses asym:24:3 seat 0 against v25 and v26, and mirror:21:2 in one v26 sample.
- Decisions take up to about 6.6 s.

Held-out validation is running: v21, v19 and v17 fa11 on experiments/economy/opp_heldout1.txt (opp_scen9 + fortress v25
+ v26 + bots.best) x mirror:31:2, asym:32:2, mirror:33:3, asym:34:3, asym:35:2, mirror:36:3, both seats, 144 matches
each. These scenario seeds were not used for any tuning in this lane. Results will follow in entry 15.

## Entry 15 (2026-10-31T12:10:42Z): held-out set 1; erratum on entry 14; econ23 (v23), econ24 (v24), econ25 (v25); the attack caps; fortress v28/v29

All matches: the lead's harness (bot_research.harness.tournament) on the unchanged engine, both seats, W-D-L from the
results field "winner", clip = mean HP difference clipped to [-800, 800]. Fortress v25, v26, v28 and v29 (hrt-w1) keep
a wall-clock budget in their gun planner, so every match against them is one sample of a load-dependent opponent.
Every other opponent and every candidate below is deterministic (time_budget None, plan_time 1e6).

### Held-out set 1 (ho21, ho19, ho17)

Conditions: experiments/economy/opp_heldout1.txt (opp_scen9's 9 opponents plus fortress v25, v26 and bots.best as of
10:50Z) x mirror:31:2, asym:32:2, mirror:33:3, asym:34:3, asym:35:2, mirror:36:3, 144 matches per candidate. These
six scenario seeds were not used to choose anything before this run; since the mirror:36:3 diagnosis below they are
no longer clean for v23 and later.

| scenario | v21 | v19 | v17 fa11 |
| --- | --- | --- | --- |
| mirror:31:2 | 24-0-0 | 22-2-0 | 18-2-4 |
| asym:32:2 | 24-0-0 | 24-0-0 | 20-0-4 |
| mirror:33:3 | 24-0-0 | 24-0-0 | 12-12-0 |
| asym:34:3 | 24-0-0 | 24-0-0 | 21-0-3 |
| asym:35:2 | 16-0-8 | 16-0-8 | 15-0-9 |
| mirror:36:3 | 22-0-2 | 24-0-0 | 16-6-2 |
| total | **134-0-10, clip +688** | **134-2-8, clip +694** | 102-20-22, clip +391 |

- v19's two draws: bots.best on mirror:31:2, both seats.
- asym:35:2 seat 0 is lost by v19 and v21 to the same 8 opponents: v2 econ (-6501), v14 (-1294), v25 and v26 (-1714),
  bots.best (-1405), and v4, v6 and fortress v9 (-5 at round 50). This seat starts 5 HP down (a scripted tier1 hit),
  and its greedy splash capacity (experiments/economy/capacity.py) is 650, far below the lock. Against lead_v4 at
  round 11, v21 bought 35 tier3 into lead_v4's lock, built in the same round (26 splashes). I have no fix for this seat.
- v21's two mirror:36:3 losses (eco6_t5, -710 in both seats; v19 +108) are explained under econ23.

### Erratum on entry 14 (the gain table)

Entry 14's gain table compared one re-plan per map, at obs round K+1, with lead_v3. v21 does not do that. The harness
calls decide during the K scripted rounds and replaces the actions, so cells the bot never requested appear one round at
a time. The re-plan rule fires at obs rounds 2 to K+1, and each time v21 compares the new plan with the layout in use,
possibly an earlier re-plan. A trace (hrt-w2 scratch/replan_trace.py, all 18 maps, one deterministic opponent) shows that
v21's final layout differs from the table on five maps:
- mirror:21:2: v21 uses the round-2 plan (S_final 1130), not the round-3 plan (1310) in entry 14's analysis.
- mirror:22:3: v21 uses the round-4 plan, not lead_v3.
- asym:23:2 seat 1: v21 uses the round-2 plan.
- mirror:33:3: v21 uses the round-2 plan (S_final 260).
- mirror:36:3: v21 uses the round-3 plan (S_final 170).

So entry 14's sentence that v21 "re-planned S_final 1310 at route 56" on mirror:21:2 describes a plan v21 did not use.

### econ23 (frozen v23): the re-plan gain is measured against the base layout

- diag26 (mirror:36:3 against eco6_t5, all logs): v19 +108 in both seats; v21 -710 in both; v21 with
  foreign_sat_from=null also -710. The trace shows the cause:
  - v21 adopted the round-2 plan (1320 against lead_v3's 870) and then the round-3 plan (950 against 520, the round-2
    plan scored on the round-3 map).
  - It rejected the round-4 plan (390 against 170) and so kept the round-3 plan, which scores 170 on the final map,
    below both the round-4 plan (390) and lead_v3 (250).
- econ23 = econ21 + replan_base. With replan_base=true, whenever the rule fires, the layout becomes the new plan if it
  beats the base layout (lead_v3) by at least replan_gain on the current buildings, and lead_v3 otherwise. An earlier
  re-plan is never kept. needs_replan is asked about lead_v3. After the scripted rounds the own never-requested cells
  no longer change, so the layout choice is fixed by obs round K+1 and does not depend on the opponent.
- Frozen at 2026-10-31T11:15:35Z as bots/economy/frozen/v23 (30 files; econ23.py sha256 477240ae05b3...). Spec:
  bot_research.bots.economy.frozen.v23.econ23:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true
- By the trace, v23's layout differs from v21's only on the five maps above. On every other start the two play
  identically against a deterministic opponent; on the standard start both equal v19.
- d23: v23 and v21 on opp_heldout1 x those five scenarios, 120 matches each.
  - v21: 115-0-5, clip +723. Its losses: v26 mirror:21:2 -1022 x2, eco6_t5 mirror:36:3 -710 x2, bots.best
    asym:23:2 seat 1 -1260.
  - v23: **117-0-3, clip +727**. Its losses: v26 mirror:21:2 -2272 x2, bots.best asym:23:2 seat 1 -70.

### hrt-w1's fortress v28 and v29 (w1v29, w1v29b)

Conditions: opponents frozen fortress v28 and v29 (experiments/economy/opp_w1v29.txt) x the standard start, the six
development scenarios and held-out set 1, 52 matches per candidate, all logs kept.

| candidate | W-D-L | clip |
| --- | --- | --- |
| v19 | 33-0-19 | +160 |
| v21 | 34-0-18 | +278 |
| v23 | 34-0-18 | +278 |

- The common pattern: the fortress locks (per-copy splash S >= 1500) in rounds 9 to 11 while our map stays below the
  lock, and it floods in rounds 35 to 39.
- On mirror:21:2 against v28, v23 lost -2692 in both seats. By the per-round log, v23 built 11 layout walls at round 3
  (route 22), 13 guns in rounds 4 to 11, then 19 splashes at round 12, reaching S 580 at route 24. That is far below
  its adopted re-plan (25 reserved splash cells, final route 56, S_final 1310).
- A replay with hrt-w1's frozen v15 is_foreign (more than 8 own buildings outside the layout's final_adj) shows why:
  - The guns of rounds 4 to 8 sit next to the current route (length 22), which is not the layout's final route, so they
    lie outside final_adj.
  - At round 9 the tenth such building made the map foreign for v15, and v15 then drops the layout's exclusions.
  - So the round-9 and round-11 guns went onto a reserved cell and two final-route cells, and four of the round-12
    splashes onto final-route cells.

### econ24 (frozen v24): own buildings never make the map foreign

- econ24 = econ23 + own_in_layout. With own_in_layout=true, the layout passed to v15's plan_defense (in defend and
  lock_reachable) has its final_adj extended with value 0 by the cells of the own buildings this bot requested. So
  is_foreign counts only never-requested cells. The added cells are occupied, so they are never candidates, and value
  0 adds nothing to reserved_capacity; nothing else in v15 changes.
- Frozen at 2026-10-31T11:34:59Z (bots/economy/frozen/v24, 31 files; econ24.py sha256 44c8d7d5d4d0...). Spec = the v23
  spec + &own_in_layout=true.
- w1v29c (the w1v29 conditions): 34-0-18, clip +337. The mirror:21:2 losses became -32 in all four matches. Against v28
  the bot now locks at round 11 (33 splashes, S 1500 at route 56) and loses only its round-3 and round-4 HP. Other cells
  are within the fortress's variance.
- std24 (opp_key5, standard start, 90 matches): 82-2-6, clip +388. Every HP difference is identical to v19 (std22).
- ho24 (opp_heldout1 x the 6 development scenarios and held-out set 1, 288 matches): **269-0-19, clip +686**. Paired on
  common matches:
  - v21 (ho21 + d23), 216 matches: v21 203-0-13 +701, v24 202-0-14 +687.
  - v23 (d23), 120 matches: v23 117-0-3 +727, v24 116-0-4 +727.
  - v19 (ho19), 144 matches: v19 134-2-8 +694, v24 134-0-10 +673.
- New failure cases of v24:
  - asym:32:2 seat 0 against v25 (-1995) and v26 (-3815), where v21 won +935 against both.
    - Here the base layout lead_v3 is in use (re-plan gain 240 < 400), and exactly 8 never-requested cells lie outside
      it. So for v21 and v23 the first own building outside lead_v3 (round 3) makes the map foreign, while for v24 it
      never becomes foreign.
    - v24's planner kept lead_v3's exclusions on a map lead_v3 was not designed for, and reached S 690 at route 46 by
      round 19.
  - asym:23:2 seat 1 against eco6_t5: -719 (v23 +858).
    - The adopted re-plan scores 920 (lead_v3 470). v23's map became foreign at round 8 (9 own buildings outside the
      re-plan), and v23 held. v24 kept the re-plan's exclusions and lost.
- Conclusion: protecting the layout helps when the layout can reach the lock (mirror:21:2, S_final 1310) and hurts when
  it cannot (S_final 920) or was not built for the map (lead_v3 on a scripted map). v24 is not a candidate.

### The attack caps (min_cap=300, active_cap=500) and Proposition G

Every econ version since v4 caps a purchase at min_cap=300 new entries and the own active roster at active_cap=500.
The engine has neither cap: td_game/config.py, actions.py and protocol.py have no roster or action-count limit.
td_game/combat.py (read, not modified) gives the facts used below:
- spawn_schedule puts active entry k at tick k mod 250 (ticks_per_round 250).
- A copy born at tick t moves one cell per later tick, so it arrives at tick t + L on a route of L steps, and it is
  removed before turrets fire.
- Each gun (aoe 0) adds its damage to at most one copy per tick: the frontmost in range.
- A splash adds 10 to every copy in its eight neighbours.
- Copies not arrived at tick 249 are cleared.

**Proposition G.**
- Hypotheses:
  - A defender map has route length L, per-copy splash S (10 x the number of (route cell before the base, splash)
    pairs at Chebyshev distance 1) and total gun damage G (the sum of the damage of its guns).
  - The attacker's active roster in a round consists of N entries of one tier with HP h > S and damage d.
  - Nothing is built between the purchase and the round's combat.
- Then the number of copies that reach the base in that round is at least A(N) - floor(250 G / (h - S)), where A(N) is
  the number of k < N with (k mod 250) <= 249 - L.
- Proof:
  - A copy receives splash only on route cells before the base, at most once per tick per cell, so at most S in total.
  - A copy that dies therefore received at least h - S gun damage.
  - The guns deal at most G per tick and 250 G per round in total, so at most floor(250 G / (h - S)) copies die.
  - Every copy born at a tick <= 249 - L that does not die arrives within the round.
- So for S < h, the arrivals grow without bound in N: no number of guns makes a map immune. Only S >= h does
  (Proposition 4). This is the quantitative form of Proposition F.

Example (fastsim, exact replica of combat.py): fortress v28's map at round 20 of w1v29c asym:24:3 seat 0 has 27 splashes
(S 960), 26 gun3, 2 gun2 and 1 gun1 (G = 1482), and route 42.
- Tier5 x 500 does 0 damage, x 750 does 201 hits (28140 damage), x 1000 does 409 hits, x 3000 does 2074 hits.
- The bound gives at most 686 kills, so x 1000 gives at least 832 - 686 = 146 arrivals.
- In that match v24 held 251,936 gold at round 20 and 1,746,476 at round 35, never attacked, and lost -2957 to a
  275-entry tier5 flood at round 35.
- Cause: within the caps the best package does no damage. offense.search with cap 3000 on the round-24 map and 500,000
  gold returns 769 tier5 (499,850 gold, 30800 simulated damage) in 0.26 s.
- The finish rule (kill this round at least cost, no theta test) then buys it. The theta-weighted attack rule never
  would: its value is capped at the opponent's HP.

v24m = frozen v24 with &min_cap=3000&active_cap=4000 (parameters only; no new code):
- w1v29d (the w1v29 conditions): **41-0-11, clip +493** (v24 34-0-18 +337).
  - Won now: asym:24:3 seat 0 against both, asym:34:3 seat 1 (v28), mirror:21:2 (v28) x2, mirror:31:2 (v29) x2.
  - Of the 11 losses, ten are against an opponent locked (S >= 1500) by round 11 or round 20, with our map below the
    lock. The eleventh is asym:32:2 seat 1 against v28: S 1480 at route 60, where h - S = 20 and v28's guns cover the
    gap.
  - Mean decide time per match 8.1 s (v24 8.0 s); the largest single decision took 2.7 s.
- std24m (v24m, opp_key5 standard start): running.

### econ25 (frozen v25)

- econ25 = econ24 + own_in_layout="replan" and own_min_s. "replan" applies v24's rule only while a re-planned layout
  is in use, never to lead_v3. own_min_s additionally requires the adopted re-plan's score (at adoption) to be at
  least own_min_s.
- With own_min_s=1200 the rule acts on mirror:21:2 seat 0 (re-plan 1310, lead_v3 830). It does not act on asym:23:2
  seat 1 (920) or asym:32:2 seat 0 (lead_v3 kept: re-plan 1370, lead_v3 1130, gain 240).
- The threshold was set from these two examples, so it needs validation on scenarios not used to choose it.
- Frozen at 2026-10-31T12:08:01Z (bots/economy/frozen/v25; econ25.py sha256 095872ce8990...). Candidate V25RM:
  bot_research.bots.economy.frozen.v25.econ25:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true&own_in_layout="replan"&own_min_s=1200&min_cap=3000&active_cap=4000
- ho25rm (V25RM on the ho24 conditions, 288) is running; results in entry 16.

### For the lead (current recommendation)

- As a foreign target, v23 is at least as good as v21 on every match I have:
  - It is identical to v21 except on five maps.
  - On those five maps it is better: 117-0-3 against 115-0-5 over 120 matches.
  - Spec above.
- econ20 (frozen v20) carries the eco6_t5 losses of entry 14 (asym:3:2 seat 1, asym:24:3 seat 0) that v21 and v23 do
  not have.
- The attack caps are a separate gain. Appending &min_cap=3000&active_cap=4000 to any frozen econ spec from v9 on lets
  the finish rule break a sub-lock fortress once the gold suffices. So far this is measured only on v24 against
  v28/v29 (+7 wins of 52).
- Entry 16 will say whether V25RM (both changes) holds on the 12 scenarios and the standard start.

## Entry 16 (2026-10-31T13:10:27Z): V25RM on ho25rm, std24m and held-out set 2; two open failure cases

Conditions as in entry 15. V25RM = frozen v25 with the spec of entry 15 (v23 + own_in_layout="replan", own_min_s=1200,
min_cap=3000, active_cap=4000). v24m = frozen v24 + &min_cap=3000&active_cap=4000.

### ho25rm (opp_heldout1 x the 6 development scenarios and held-out set 1, 288)

- V25RM: **275-0-13, clip +719** (v24 ho24 269-0-19 +686).
- Paired with earlier runs on their common matches:

  | baseline | matches | baseline result | V25RM result |
  | --- | --- | --- | --- |
  | v24 (ho24) | 288 | 269-0-19 +686 | 275-0-13 +719 |
  | v21 (ho21 + d23) | 216 | 203-0-13 +701 | 206-0-10 +717 |
  | v23 (d23) | 120 | 117-0-3 +727 | 118-0-2 +752 |
  | v19 (ho19) | 144 | 134-2-8 +694 | 136-0-8 +697 |

- The 13 losses:
  - Eight on asym:35:2 seat 0, the same eight opponents as v19 and v21 (entry 15). The caps did not change these.
  - Fortress v26: -55 on mirror:1:2 and -32 on mirror:21:2, both seats each.
  - bots.best (frozen best_v9b, same sha256) on asym:24:3 seat 1: -1243 at round 17. v24 has the same result; there is
    no v23 run of this pairing.
- v24's new failure cases are gone: asym:32:2 seat 0 against v25 and v26 is +935 against both, and asym:23:2 seat 1
  against eco6_t5 is +560. In both, the rule of v25 does not act (entry 15).
- The caps converted asym:24:3 seat 0 against fortress v25 (+11427, v24 -2993) and v26 (+12407, v24 -833).

### std24m (v24m, opp_key5, standard start, 90)

- 82-2-6, clip +388, with every HP difference identical to std24 (v24) and so to std22 (v19).
- On these 90 matches the caps never change play: no purchase there needs more than 300 new entries or 500 active ones.

### Held-out set 2 (hs2)

Conditions:
- Opponents: experiments/economy/opp_heldout2.txt, 14 opponents.
  - opp_heldout1, with bots.best replaced by the frozen file experiments/lead/frozen/best_v9b.py, so a later change of
    bots/best.py cannot change the opponent.
  - Plus hrt-w1's frozen fortress v29 and v33 (v33 is hrt-w1's final recommendation).
- Scenarios: mirror:41:2, asym:42:2, mirror:43:3, asym:44:3, asym:45:2, mirror:46:3, both seats. These seeds were
  chosen at 10:50Z and never run before 12:38Z.
- Candidates V25RM and V23, 168 matches each.

Results:
- V25RM complete: **157-1-10, clip +688**. Its non-wins:
  - eco6_t5: mirror:41:2 -980 x2, mirror:43:3 -721 x2, asym:45:2 seat 1 -695.
  - Fortress v25 on asym:44:3 seat 0: -1165.
  - Fortress v26: mirror:43:3 -2826 x2; draw on asym:44:3 seat 0.
  - Fortress v33: mirror:43:3 -2100 x2.
- V23, partial at 13:10Z (146 of 168, paired with V25RM on the same 146): V23 135-1-10 +679, V25RM 137-1-8 +701.
  - Every non-win of V25RM on these 146 is also a non-win of V23.
  - V23 additionally loses mirror:43:3 against fortress v25 (-2800 x2), which V25RM wins by +14700 x2.
  - V23 has the same eco6_t5 losses, with slightly smaller margins (-840, -642, -695).
  - The final V23 numbers will be in the next entry.

### Open failure case 1: eco6_t5 on mirror:41:2 (both versions)

Per-round log of hs2 match 00001 (V25RM seat 0):
- eco6_t5 builds no defence beyond the scripted gun1 (S 0). It has 50 factories by round 6 and buys one tier5 per round
  from round 7 (roster 2, 3, 4, 5 at rounds 7 to 10).
- V25RM stops buying factories at 24 (round 7) and spends its whole income (about 380 per round) on guns and splashes.
  It reaches S 260 at route 22 by round 10. It loses 140, 140, 280 and 420 HP in rounds 7 to 10 (-980).
- The foreign gate (foreign_attack_from=11) forbids attack purchases before round 11, so the bot never answers on a map
  with S 0 and one gun1.
- Conjecture, not simulated: an early counter-attack (tier2 or tier3 from round 6) wins this race. The rule that would
  allow it is opponent-state based, for example lifting the foreign gate while the opponent's map is S 0 and its gun
  damage is below some bound. econ22's race rule (entry 14), which lifted the gate whenever the own lock was
  unreachable, was rejected, so the condition must be about the opponent's map, not ours.

### Open failure case 2: fortress v26 and v33 on mirror:43:3 (both versions)

Per-round log of hs2 match 00161 (V25RM seat 0 against v33):
- Our map:
  - It stays at route 22 for the whole match. V25RM adds 6 walls in round 4 and none after.
  - From round 4 it buys only guns, plus 4 splashes in round 13 (42 guns, S 140 by round 30).
  - It buys nothing in rounds 16 to 27 or after round 28.
  - Gold grows to 1,264,131 by round 32.
- v33, from the same (mirror) start:
  - It has 17 splashes at round 10 and 35 at round 11, with S 1510 at route 56.
  - So it is immune from round 11 on by Proposition 4, and the caps cannot help.
  - At round 32 it attacks with 268 entries and wins by 2100.
- So a lock was reachable from the common start, and our planners (v15 with lead_v3 or the re-plan) did not find it.
- The greedy splash-only lower bound (capacity.py, no walls) on our map is 850 at round 3 and 170 at round 14, after
  the gun purchases.
- Candidate fix for the next shift: on a foreign map, plan the lock with a wall-aware planner (hrt-w1's fortress
  planner has one, but it has a wall-clock cutoff, so it would need a fixed iteration budget to keep this bot
  deterministic).

### w1v29e (V25RM against fortress v28 and v29, 13 starts, 52), partial

At 13:10Z, 27 of 52 done: 22-0-5 clip +474, against v24m (w1v29d) on the same 27 also 22-0-5 +474. The only
differences are asym:32:2 seat 0 against v28 (-2695 and -2985) and asym:34:3 seat 1 (+6025 and +6165), within the
fortress's variance.

### Recommendation (unchanged from entry 15, now with held-out set 2)

- For the lead: V25RM is my best artifact.
  - Spec in entry 15; in hrt-w2/scratch/v25rm.spec of this lane's directory.
  - Frozen v25: bots/economy/frozen/v25, econ25.py sha256 095872ce8990...
- It is at least as good as V23 on every paired set measured so far: ho25rm, hs2 partial and w1v29e partial.
- It equals v19 on the standard start against opp_key5, by std24m together with the identity of v24 and v19 there.
- If a smaller change is preferred, V23 plus &min_cap=3000&active_cap=4000 is the parameter-only part. That
  combination itself is not measured.
- Known exposures:
  - eco6_t5-style early tier5 economies on some mirror starts (failure case 1).
  - Fortresses that lock on maps where our planners find no lock (failure case 2).
  - asym:35:2 seat 0.

Addendum to entry 16 (2026-10-31T13:14:28Z): hs2 complete.

- V23: **152-1-15, clip +650** (V25RM 157-1-10, +688, on the same 168 matches).
- Every non-win of V25RM is also a non-win of V23.
- V23's five additional losses:
  - fortress v25, mirror:43:3: -2800 x2 (V25RM +14700 x2);
  - fortress v33, asym:44:3 seat 0: -1050;
  - fortress v33, asym:45:2: -10 in seat 0 and -2370 in seat 1.
- Both lose to v33 on mirror:43:3: V23 by -780 x2, V25RM by -2100 x2.
- Matches against fortress v25 to v33 are single samples of a wall-clock-dependent opponent.

| scenario | V25RM | V23 |
| --- | --- | --- |
| mirror:41:2 | 26-0-2 | 26-0-2 |
| asym:42:2 | 28-0-0 | 28-0-0 |
| mirror:43:3 | 22-0-6 | 20-0-8 |
| asym:44:3 | 26-1-1 | 25-1-2 |
| asym:45:2 | 27-0-1 | 25-0-3 |
| mirror:46:3 | 28-0-0 | 28-0-0 |

Second addendum to entry 16 (2026-10-31T13:19:52Z):

- **w1v29e complete:** V25RM 41-0-11, clip +493, the same totals as v24m (w1v29d).
  - The 11 losses are the same 11 matches as v24m's (entry 15).
  - The only differences in HP are three asym:32:2 and asym:34:3 cells against v28, within that fortress's variance.
- **Failure case 2, lock reachability:** experiments/economy/reach_check.py on V25RM against v33, mirror:43:3, player 0.
  - Rounds 4, 6 and 10: own gold set to 10**7, hrt-w1's frozen v15 plan_defense with partial="none".
  - It finds no plan reaching S 1500 or 1600, with either the lead_v3 layout or the empty layout.
  - v33 reached S 1510 at route 56 from the same mirror start at round 11.
  - Correction to my first reading: reach_check tests only those two layouts, not a re-planned one. So it does not
    show that the econ planners as a whole cannot lock here.
  - econ25 re-plans with hrt-w1's frozen v26 replan_layout and plans with frozen v15. v33 uses its own (newer)
    replan.py and plan.py with its default layout as the base.
  - Which layout V25RM used in hs2 match 00161 is not yet traced (scratch/replan_trace.py does that). Whatever it
    was, the bot built no wall after round 4.
  - (v33 plays the replayed match with its wall-clock cutoff, but the own map at round 4 depends only on the scripted
    opening, and at rounds 6 and 10 only on our own purchases.)
- **Next step:**
  1. Trace V25RM's layout choice on mirror:43:3 (replan_trace.py), and run reach_check with that layout.
  2. If no econ layout reaches the lock, try v33's replan_layout (fixed iters and seed, so deterministic) as the
     re-planner on foreign maps.
  3. Measure on the development scenarios first; both held-out sets are now used.

Third addendum to entry 16 (2026-10-31T13:21:03Z): layout choice on mirror:43:3 seat 0.

Trace: scratch/replan_trace.py of this lane, frozen v23 against v33, replayed to obs round 5. v23 and V25RM choose the
same layout, because own_in_layout changes only the planner's input.
- Obs round 2: the re-plan scores S_final 1460 against lead_v3's 970. The gain is 490, so it is adopted.
- Obs round 4 (the first own decision after the three scripted rounds): the re-plan scores 1310 against lead_v3's 830.
  The gain is 480, so it is adopted, and V25RM protects it (1310 >= own_min_s 1200).
- So the layout in use from round 4 cannot reach the lock even when fully built: S_final 1310 < 1500.
- v33's own re-planner reached S 1510 at route 56 from the same start, so hrt-w1's newer replan.py finds a better
  layout here than the frozen v26 one econ20 to econ25 use.
- In the hs2 match (00161) V25RM also never built that layout. Its route stayed at 22 and S at 140, against the
  layout's 1310. Why defend() and sat_reach do not build toward a non-locking layout with 1.2M gold is not yet traced.


## Entry 17 (2026-10-31T13:56:33Z): the lead's foreign target; re-planner reach; a lock fill (econ26, v26) and its reserve (econ27, v27)

Shift 3 of hrt-w2 started 2026-10-31T13:21:48Z. All matches below are on the unchanged engine with the balanced rules,
run with the lead's tournament harness (experiments/economy/run_tourn.sh, cores 25-27).

### 17.1 The lead's foreign-map bot

The lead's best.py is frozen best_v9e. Its Insurer hands the rest of a match to a fresh frozen econ20 (v20) from the
first round in which its own map holds a building it never requested, which happens only after a scripted opening.
The lead's parameters for that bot (E20_PARAMS) are free_fallback "zero", foreign_attack_from 11, doom "next",
fac_cap 400, sat_reach true, replan true, foreign_sat_from 11.

- experiments/economy/lead_alt.py subclasses the lead's Insurer unmodified and only changes which bot is created at
  the switch. With alt="econ20" it is the lead's bot.
- Identity check (runs/economy/idcheck, 24 matches: frozen best_v9e, lead_alt econ20 and lead_alt v25rm against
  eco6_t5 and fortress v26 on mirror:41:2 and asym:44:3, both seats): lead_alt econ20 gives the same HP difference
  and end round as best_v9e in all 8 conditions. In a scripted opening the bot is called but its output is replaced,
  so the switch happens at the first free round and the lead's bot then plays as the foreign bot standalone.
- hs2e20 (frozen v20 with E20_PARAMS, held-out set 2 conditions: opp_heldout2.txt, 14 opponents, mirror:41:2 asym:42:2
  mirror:43:3 asym:44:3 asym:45:2 mirror:46:3, both seats, 168 matches): **151-0-17, clip +628**. V25RM on the same
  168 conditions (runs/economy/hs2): 157-1-10, clip +688.
- Outcome differences on the 168 paired conditions (full opponent specs):
  - V25RM wins, econ20 loses (7): eco6_t5 asym:44:3 seat 0 (+688 / -829); fortress v25 mirror:43:3 both seats
    (+14700 / -2800); fortress v33 asym:42:2 seat 0 (+6575 / -1540), asym:45:2 seat 0 (+17770 / -10) and seat 1
    (+10 / -2370); frozen best_v9b asym:42:2 seat 0 (+4200 / -980).
  - econ20 wins, V25RM draws (1): fortress v26 asym:44:3 seat 0 (both bases destroyed in round 21, HP difference
    +795; econ20 +948 in round 12).
- Held-out set 2 was already used to select V25RM (entry 16), so this comparison favours V25RM somewhat. It is still
  the only like-for-like measurement of the lead's current foreign target that I have. Recommendation to the lead:
  use V25RM (or a successor validated on fresh seeds, see 17.5) as the foreign target. lead_alt.py shows the
  change: ALTS["v25rm"] = frozen v25 econ25 with the V25RM parameters.

### 17.2 Re-planner reach on the scripted maps

experiments/economy/replan_reach.py plays the scripted rounds with idle bots (the own map at the first free round
then depends only on the scripted opening) and scores, for every scenario and seat used so far (27 seat-maps on 18
scenarios; mirror scenarios seat 0 only), the base layout lead_v3 and the re-plans of hrt-w1's frozen v26 and v34
replan_layout (iters 5000, seed = round). Output: runs/economy/replan_reach1.out.

- v26 and v34 give the same S_final and final route length on all 27 seat-maps. So switching econ to v34's
  re-planner changes nothing at the first free round on these maps.
- The re-plan S_final is below 1500 on 25 of the 27 seat-maps. The exceptions are mirror:41:2 (1510) and asym:35:2
  seat 1 (1550); the closest below is mirror:1:2 (1490).

experiments/economy/replan_fill.py builds the v26 re-plan in full (walls, then its 25 slots as splashes, each where
legal) and then adds splashes greedily on any legal cell (capacity.greedy). Output: runs/economy/replan_fill1.out.

- mirror:43:3: S_full 1310 at route 56; the greedy adds 20 splashes and reaches 1730. hrt-w1's frozen v15
  plan_defense (econ's lock_reachable test) finds no S 1500 with 10**7 gold with either the re-plan or the empty
  layout. Fortress v33 locks at S 1510 from the same start.
- On every other seat-map where v15 finds no lock with 10**7 gold, the full re-plan plus greedy stays below 1500
  (largest: asym:24:3 seat 1, 1490; asym:23:2 seat 0, 1390). The smallest are the 22-26-step maps mirror:33:3 (540),
  mirror:36:3 (340), asym:44:3 seat 0 (520) and mirror:46:3 (410), where the greedy adds 0 or 1 splash.
- Uncertainty: the greedy is one heuristic, so "stays below 1500" is a finding about that greedy, not a bound.

### 17.3 econ26 (frozen v26): a lock fill on foreign maps

- bot_research/bots/economy/fillplan.py: fill_plan(buildings, layout, budget, target, rules) builds the layout's walls
  (wall_order, each if legal), then its splash slots as splashes, then greedy extra splashes (largest per-copy splash
  S on the recomputed engine route) until S reaches the target, no cell raises S, or the gold runs out. Every
  returned action is legal in the returned order. 0.02 to 0.12 s per call. On mirror:43:3 at round 4 it reaches 1520
  with 38 actions costing 1926 gold.
- econ26.py: parameter fill (default false). With fill=true, on a foreign map, lock_reachable also returns "fill"
  when only fill_plan with 10**7 gold reaches max_hp, and the saturation step then buys fill_plan's actions within
  its budget. Frozen as frozen/v26 (econ26.py sha256 9e1b40e7..., fillplan.py b8050bae...). V26F = V25RM parameters
  plus fill=true (spec in this lane's scratch/v26f.spec).
- smoke26 (V26F against fortress v26 and v33 on mirror:43:3 and mirror:1:2, both seats, KEEP=all):
  - fortress v26, mirror:43:3: -26 in round 50 in both seats (V25RM -2826 in round 35). Our map locks in round 11
    (lock_check: first round with S >= 1500, final S 1600). The 26 HP were lost in round 5 (the damage of one tier3).
  - fortress v26, mirror:1:2: -55 in round 50 (unchanged; a known narrow loss).
  - fortress v33, mirror:43:3: -2100 in round 32 in both seats, unchanged: our final S 140, route 22, 47 empty
    cells, 1.26M gold unspent; v33 sent 268 tier5 in round 32.
  - fortress v33, mirror:1:2: -30 in round 50.

### 17.4 Why the fill failed against v33, and econ27 (frozen v27)

Trace (this lane's scratch/fill_v33.py and fill_v33b.py; V26F against v33 on mirror:43:3, player 0, replayed with
obs_replay): fill_plan with 10**7 gold on the own buildings reaches 1520 at rounds 4 to 8 and 1500 at round 9, then
460 at round 10. The four buildings added in round 9 were gun3 (9,4), gun2 (6,2), gun3 (9,5) and gun3 (5,1). The
first three are on the final route of the fill (and of the re-plan); each alone drops the fill to 520-540, while the
gun3 on slot (5,1) alone gives 1510. The re-plan's final_adj covers all but 7 own buildings at round 9, so the map is
not foreign for v15 and v15's layout plan excludes the final route; the three guns came from defend's layout-free
fallback (free_fallback "zero" takes the empty-layout plan when it clears the visible threat and the layout plan
does not).

econ27.py: parameter fill_reserve (default false; needs fill=true). On a foreign map whose per-copy splash is below
max_hp, each decision first runs fill_plan with 10**7 gold. If that reaches max_hp, its cells are reserved for the
decision: a fill cell may only receive the building the fill puts there, and the cells of the filled route (spawn and
base excluded) may receive nothing. Build actions of the decision (other than the saturation fill) that break the
reservation are dropped, and defend returns its layout plan without the layout-free fallback. Dropping a build never
makes a later build illegal, because removing a blocked cell cannot disconnect the spawn from the base. Frozen as
frozen/v27 (econ27.py sha256 3e678f80..., SHA256SUMS 34 OK). V27 = V25RM parameters plus fill=true and
fill_reserve=true (scratch/v27.spec). On the standard start the map is never foreign, so V27 plays as V25RM there.

smoke27a (live econ27, same 8 conditions as smoke26):
- fortress v33, mirror:43:3: **+980 in round 12, both seats** (V26F -2100).
- fortress v26, mirror:1:2: +720 in round 10, both seats (V26F -55). This win is not a designed effect: without the
  free fallback V27 leaked more in rounds 4-5 (HP 675 against V26F's 740), so the doom rule fired in round 10 with
  6 tier5 while v26 was half-way through its lock (route 30) and killed it. V26F's doom attack came in round 11,
  after v26's lock.
- fortress v26, mirror:43:3: -26 in round 50 (unchanged). fortress v33, mirror:1:2: -30 in round 50 (unchanged).

The regression of V27 against V25RM on the hs2 and ho1 conditions (both already used, so regression only) is
running (runs/economy/hs2v27, ho1v27). Results follow in an addendum.

### 17.5 Other

- hrt-w3's standard-start counter (guarded_maze and staged_guard growers beat economy21/23/25RM 2-22 with identical
  trajectories) is noted and not addressed here. On the standard start the lead's best.py plays its own policy, not
  the economy bot.
- A fresh validation set was fixed before looking at it: mirror:51:2 asym:52:2 mirror:53:3 asym:54:3 asym:55:2
  mirror:56:3 (held-out set 3). It has not been run.

### 17.6 Addendum (2026-10-31T14:38:37Z): V27 regression runs, econ29 (frozen v29), best_v9e, HANDOFF, Astra

**Regression of V27 on used conditions.** Clipped means below are pair_diff.py means of the HP difference clipped to
[-800, 800] over the paired conditions.
- hs2v27 (held-out set 2 conditions, 168): V27 159-1-8 clip +678; V25RM 157-1-10 +688. The only outcome changes are
  fortress v33 on mirror:43:3, both seats, from losses to wins (17.4).
- ho1v27 (opp_heldout1 x 12 scenarios, 288): V27 270-1-17 clip +653; V25RM (ho25rm) 275-0-13 +719. The opponent
  bots.best:@make changed between the two runs (it is now frozen best_v9e), so its 24 rows are not paired like for
  like. Without them (264): V27 255-0-9 +691, V25RM 253-0-11 +724. V27 wins more but by smaller margins, mostly
  against the lead's older frozen bests and eco6_t5; one new loss: eco6_t5 on mirror:21:2, both seats (-200 in round
  10; V25RM +1155 in round 13).

**Cause of the mirror:21:2 loss** (trace of frozen v27 against eco6_t5, seat 0, rounds 7-10:
runs/economy/trace27_e6_m21.out). At round 9 the bot had 1232 gold, per-copy splash 1040 and three active opponent
tier5. fill_plan with 10**7 gold reached 1520 with 12 splashes costing 720 gold. The visible-threat plan_defense
proposed one gun1 on a cell of the reserved route; the reservation dropped it; saturation is gated until round 11 on
foreign maps (foreign_sat_from 11); the bot bought 61 factories. It lost 280 HP in each of rounds 9 and 10.

**econ29.py** (frozen v29, econ29.py sha256 0c71ec9b..., SHA256SUMS 36 OK): v28 plus the parameter fill_threat
(default false). While a reservation exists, defend called with threat types (the visible defence and the
unseen-purchase defence) compares two plans with the key of the layout-free fallback (no hit first, then lower leak
score, then lower cost): the layout plan of plan_defense without its actions that break the reservation, and
fill_plan with the same budget (target max_hp). It returns the better one. V29 = V27 parameters plus
fill_threat=true (lane scratch v29.spec); lift_idle is not set. On the standard start V29 plays as V25RM.

**smoke29** (V29 against eco6_t5, fortress v26 and fortress v33 on mirror:1:2, mirror:21:2, mirror:41:2, mirror:43:3
and asym:45:2, both seats, 30 matches; development, all conditions already used): 21-0-9.
- eco6_t5: mirror:21:2 +675 in round 11, both seats (V27 -200); mirror:43:3 +493 in round 12, both seats (V27 -1281,
  V25RM -721); mirror:1:2 +305; asym:45:2 seat 0 +1300. Still lost: mirror:41:2 -980 in round 10, both seats (as V27
  and V25RM), and asym:45:2 seat 1 -1030 in round 10 (V27 -1030, V25RM -695).
- fortress v26: mirror:21:2 +9648 (V27 +916, V25RM -32); asym:45:2 seat 1 +13566 (V27 +126); mirror:41:2 +975.
  mirror:1:2 -55 in round 50, both seats (V25RM -55; V27 +720 there came from the doom attack described in 17.4,
  which V29 does not repeat because it leaks less in rounds 4-5). mirror:43:3 -26 in round 50 (unchanged).
- fortress v33: mirror:43:3 +980 (as V27); mirror:21:2 +1528; mirror:41:2 +18620; asym:45:2 +17770 and +10;
  mirror:1:2 -30 in round 50 (unchanged).

**Frozen best_v9e** (bv9e: V25RM and V26F against the lead's frozen best_v9e on the 12 ho1 scenarios, both seats; V27
rows taken from ho1v27, where bots.best is best_v9e): V25RM 13-1-10, V26F 13-1-10 (identical), V27 15-1-8. V27
converts mirror:1:2 in both seats (-980 to +1820 in round 20). All three lose mirror:22:3 in both seats (-980 in
round 16) and asym:24:3 in both seats; on the other asym scenarios the result depends on the seat for all three
(map effect, not policy).

**HANDOFF** (lead's request of 14:05Z; hand1: V27 against the 18 HANDOFF specs of experiments/lead/pools.py, copied
to experiments/economy/opp_handoff.txt, standard start, both seats, 36 matches): **2-0-34**. Growth 5: handoff 10-14
lose -274 to -378 in round 50 (both maps hold, the opponent ahead), handoff 16 wins +360 in round 21. Growth 6: lose
-658 or -1078 in round 10. Growth 7: lose -658 in round 9. In a trace of growth 6 handoff 12, seat 0, our tier1/tier3
attacks of rounds 1-5 dealt 182 damage while we had 21 factories against the opponent's 86 at round 6; from round 7
the opponent sent 2 tier5 per round and our per-copy splash stayed between 40 and 370. On the standard start V27 is
the economy policy itself (no scripted opening). Lock rounds (scratch lock2.py over the 36 kept logs,
runs/economy/hand1_lock.out, checked 15:17Z): V27 reaches S >= 1500 in none of the 36 matches; against growth 6
and 7 it has lost by round 10 with S at most 680 at round 9; the growth-5 opponents lock at rounds 16-19 and the
growth-6/7 opponents had not locked when the match ended. So for V27 the answer is: no lock before round 12 against
growth 6 or 7 (only V27 was tested here). Growth-first variants of V29 are queued (hand2, below).

**Astra** (question bfs_reserve, answered; this lane's astra/bfs_reserve). Lemma (proved): on the 12x12 grid, the
engine's route BFS (FIFO queue, neighbour order right, down, left, up, parent fixed at first discovery, stop when the
base is popped) returns the lexicographically least shortest path by move order. Consequently, if P is the returned
route and a set of additional blocked cells is disjoint from P (added at once or one at a time, each avoiding the
current route), the route stays P; and a new splash on an empty cell c not on P raises the per-copy splash S by
exactly 10 times the number of cells of P other than the base at Chebyshev distance 1 from c. Omitting builds from
a legal build sequence keeps every retained build legal, but not the route or the damage. Code review of v27/v28
(no definite bug; scope remarks): the reservation is skipped when the map is already locked (intentional); its
activation depends on one greedy fill_plan result, not on the existence of a locking fill; filtering a plan can
remove its defensive value (v29 now evaluates the filtered plan); the free fallback is off while a reservation exists
(intentional); the saturation fill (target sat_target, its own budget) need not equal the reserved fill and bypasses
the filter; lift_idle is an absolute round threshold.

### 17.7 Addendum (2026-10-31T15:50:33Z): held-out set 3 (hs3, hs3v30), econ30 rejected, ho1v29, recommendation for the lead's foreign target

**Conditions.** Held-out set 3 = experiments/economy/opp_heldout3.txt (17 opponents, fixed 13:58:53Z) x scenarios
mirror:51:2 asym:52:2 mirror:53:3 asym:54:3 asym:55:2 mirror:56:3, both seats, 204 matches per candidate. The
candidates were fixed before any set-3 match was played: E20 (frozen v20 with the lead's parameters, the foreign
target inside best_v9e), V25RM, V27, V29 (hs3, 816 matches, JOBS=2, 14:40Z-15:45:54Z) and V30 (hs3v30, frozen 14:44Z,
before any hs3 result was viewed; 15:12Z-15:39Z). Clip = HP difference clipped to [-800, 800]; outcomes from the
engine's winner field. CI = 95% percentile interval of a bootstrap over the 102 (opponent, scenario) clusters (both
seats resampled together; 4000 resamples, seed 1; scratch pboot.py in the lane directory).

| candidate | W-D-L | clip mean | vs E20: clip diff [CI] | score diff [CI] |
|---|---|---|---|---|
| E20 | 171-7-26 | +572 | - | - |
| V25RM | 177-1-26 | +599 | +26.8 [-63.5, +117.9] | +0.015 [-0.042, +0.071] |
| V27 | 179-1-24 | +600 | +27.7 [-62.0, +118.6] | +0.025 [-0.032, +0.078] |
| V29 | 178-1-25 | +600 | +28.1 [-62.1, +120.5] | +0.020 [-0.037, +0.076] |
| V30 | 167-0-37 | +511 | -60.6 [-179.0, +49.2] | -0.037 [-0.113, +0.034] |

V29 - V25RM: +1.3 [-13.1, +15.9]. V30 - V29: -88.7 [-173.7, -15.3], score -0.056 [-0.108, -0.010].

Per scenario (W-D-L, clip mean), the difference between E20 and the V25 family depends on the map:
mirror:51:2 E20 26-2-6 +452, V25RM and V29 34-0-0 +781; asym:54:3 E20 25-1-8 +422, V25RM/V29 27-1-6 +536;
mirror:53:3 E20 32-2-0 +744, V25RM/V29 28-0-6 +510; mirror:56:3 E20 32-2-0 +750, V25RM/V29 32-0-2 +677; asym:52:2
and asym:55:2 within 1 win. Against frozen best_v9e (whose foreign target is econ20): E20 3-6-3, V25RM/V27/V29
8-0-4, V30 6-0-6. V29 against E20 changes 29 of 204 outcomes: 16 in V29's favour, 13 in E20's (most of them
fortress v33/v34/v35 on mirror:51:2, mirror:53:3 and asym:52:2, in both directions).

Pooled with held-out set 2 (hs2, opp_heldout2 x 6 other scenarios, 168 per candidate; E20 rows from hs2e20):
V25RM - E20 +41.6 [-16.1, +99.3], score +0.026 [-0.011, +0.062] (set 2 alone +59.6 [+14.0, +115.8]); V27 - E20
+37.4 [-26.0, +97.5], score +0.036 [-0.001, +0.073]. Both sets are now USED.

**econ30 (V30) is rejected.** fill_any (greedy splash fill below the lock on foreign maps, 17.6) was meant to repair
the best_v9e losses on mirror:22:3 and asym:24:3 (ho1 conditions). On set 3 it is significantly worse than V29
(above). Of 204 outcomes, 2 change in V30's favour (fortress v33 and v34, asym:52:2 seat 0) and 14 against it
(mirror:56:3 against fortress v33/v34/v35 and best_v9b, mirror:53:3 against best_v9b and best_v9e, both seats;
best_v9b asym:52:2 and asym:54:3 seat 0). Each of the 14 ends in rounds 15-18 with our HP gone, where V29 wins
(13) or draws (1) in round 20.
Trace (V30 seat 0 against best_v9e, mirror:53:3, kept log): in round 11 V30 built 14 walls and 21 splashes (route
length stayed 28); in round 15, with 12 tier5 copies in the opponent's roster and 29274 gold, it bought 400
factories and nothing else and lost 840 HP. At that point our map held 41 turrets and 68 walls, so 144 - 109 = 35
cells were empty, 29 of them on the route; at most 6 off-route cells could take a new turret. Conjecture (not
tested): the fill used the cells that the later defence needed. The development run ho1v30 was stopped at 54/288
(its rows: V30 equals V29 except eco6_t5 mirror:36:3, both seats, D -165 in round 13 where V29 won +108). A
4-match check of V30 against bots.best on mirror:22:3 and asym:24:3 is queued (v30best) only to test the original
mechanism claim.

**ho1v29 (development set ho1, 288; bots.best = best_v9e copy since 13:07:59Z).** V29 268-1-19 +675; V27 (ho1v27)
270-1-17 +653; V25RM (ho25rm, played when bots.best was best_v9b) 275-0-13 +719. Without the bots.best rows: V29
253-0-11 +715, V25RM 253-0-11 +724. Outcome changes of V29 against V27: V29 wins eco6_t5 mirror:21:2 in both seats
(+675; V27 -200, the 17.6 cause); V29 loses fortress v25 mirror:1:2 (-35 in round 50; V27 +500) and fortress v26
mirror:1:2 (-55; V27 +720) in both seats. Trace of the v25 case (seat 0): fortress v25 had 4 turrets and route
length 22 until round 10 and built 25 splashes in round 11; our attack is held until round 11 by
foreign_attack_from=11, our 17 tier3 of round 11 met the new splashes and did no damage, and the 40 HP we lost
in rounds 2-4 to tier1 pokes decided the match. lift_idle (v28) does not cover this case, because the opponent
built turrets in rounds 3-5, after the foreign snapshot.

**Recommendation to the lead (foreign target, for best_v9f).** Measured on two held-out sets, replacing econ20 by
V25RM, V27 or V29 raises the mean clipped margin by about +28 (set 3) and +42 (sets 2 and 3 pooled). Neither
interval excludes 0, and the per-map sign changes (mirror:51:2 and asym:54:3 in favour, mirror:53:3 and
mirror:56:3 against). So this is a small expected gain with real map-dependent risk, not a demonstrated
improvement. Against best_v9e itself the V25 family scores 8-0-4 where econ20 scores 3-6-3 on set 3. If the lead
swaps, V25RM is the smaller change (V29 - V25RM = +1.3 [-13, +16]; V29 adds fill code); spec:
bot_research.experiments.economy.lead_alt:@make?base="v9e"&alt="v25rm"&<Insurer parameters> (ALTS also has "v29"
and, for completeness, "v30", which should not be used). The swap only changes play after the Insurer's foreign
handoff (a building on our map that the Insurer never requested), which does not occur on the standard start, so
it does not change the standard-start pools. A third held-out set of scenarios (hs4: E20, V25RM, V29,
fixed before any set-4 match; opp_heldout3 x mirror:61:2 asym:62:2 mirror:63:3 asym:64:3 asym:65:2 mirror:66:3,
612 matches) started 15:48Z and should finish about 16:40Z; it uses the set-3 opponents, so it is held out in
scenarios only.

### 17.8 Addendum (2026-10-31T16:01:10Z): timing strikers against P4TNUB, P5TNUBM and best_v9e (the lead's 14:53Z request)

**Conditions.** strike1: the lead's P4TNUB and P5TNUBM (specs copied 15:18Z from the lead's RUN_STATUS, lane scratch
p4tnub.spec and p5tnubm.spec; experiments/lead/v28.py and v30.py as of 15:39Z, hashes in the result rows) against
the 20 variants of bots/economy/timing.py in experiments/economy/opp_strike1.txt (attack_round 4/5/6/7 x
attack_frac 1.0/0.5 x repeat false/true; attack_round 5 and 6 with pre_defend=true&pre_gold=60; attack_round 5 and 6
with fac_cap=10), standard start, both seats, 80 matches, all logs kept (runs/economy/strike1). strike1b: frozen
best_v9e against the same 20 (40 matches, runs/economy/strike1b). Every result below is identical in both seats.

| striker (economy.timing) | P4TNUB | P5TNUBM | best_v9e |
|---|---|---|---|
| attack_round=4, attack_frac=1.0 (repeat either) | L -35 r50 | L -35 r50 | L -35 r50 |
| attack_round=4, attack_frac=0.5 | W +15 r50 | W +15 r50 | W +15 r50 |
| attack_round=5 (frac 1.0 or 0.5, repeat either, or fac_cap=10) | W +75 r50 | W +75 r50 | W +75 r50 |
| attack_round=5, pre_defend, pre_gold=60 | W +880 r12 | W +880 r12 | W +560 r50 |
| attack_round=6 (frac, repeat or fac_cap=10) | W +105 r50 | W +100 r50 | W +105 r50 |
| attack_round=6, pre_defend, pre_gold=60 | W +26 r50 | W +26 r50 | D 0 r50 |
| attack_round=7 (any) | W +155 r50 | W +155 r50 | W +155 r50 |

Answer to the request: none of our round-5 or round-6 timing strikers beats P5TNUBM or P4TNUB; the closest is
attack_round=6 with pre_defend (they win by 26; best_v9e draws). The one loss is the round-4 all-in striker,
and best_v9e loses it by the same -35, so it is not a new loss of the repair candidates. Mechanism (logs of
P5TNUBM, P4TNUB and best_v9e in seat 0; rounds 1-5 are identical for the three): the Insurer builds 20 walls and
sends 3 tier1 in round 1, which hit the striker's empty map for 15 per round in rounds 1-4 (60); the striker
buys only factories in rounds 1-3 and 19 tier1 in round 4, which hit the Insurer's map (20 walls, no turret,
route 40) for 95 in round 4; from round 5 both maps stop everything and the match ends 705:740 in round 50. With
attack_frac 0.5 the round-4 wave is smaller and the Insurer wins by 15. Conjecture (not tested): one cheap turret
on the Insurer's route by round 4 would remove most of the 95; whether that costs elsewhere is the lead's
trade-off and is not measured here.

### 17.9 Addendum (2026-10-31T16:26:31Z): held-out set 4 (hs4) and the pooled foreign-target comparison

**Conditions.** hs4: E20, V25RM and V29 (specs as in 17.7, all frozen before any set-4 match) against the 17
opponents of experiments/economy/opp_heldout3.txt on mirror:61:2 asym:62:2 mirror:63:3 asym:64:3 asym:65:2
mirror:66:3, both seats, 204 paired conditions per candidate (612 matches, runs/economy/hs4, finished 16:23:49Z).
Set 4 is held out in scenarios only: the opponents are the set-3 list. Held-out set 4 is now USED. Statistics as
in 17.7 (clipped HP difference, cluster bootstrap over (opponent, scenario), scratch pboot.py, 4000 resamples, seed 1).

| candidate | W-D-L | clipped mean | paired difference |
|---|---|---|---|
| E20 | 166-6-32 | +531 | |
| V25RM | 174-2-28 | +577 | V25RM - E20 = +46.6 [-13.9, +104.6] |
| V29 | 174-2-28 | +577 | V29 - V25RM = 0 on every one of the 204 conditions (identical HP differences) |

Per scenario (E20 / V25RM W-D-L): asym:62:2 32-0-2 / 32-0-2; asym:64:3 21-0-13 / 25-0-9; asym:65:2 27-0-7 / 31-0-3;
mirror:61:2 30-2-2 / 32-0-2; mirror:63:3 30-2-2 / 30-2-2; mirror:66:3 26-2-6 / 24-0-10. The outcome changes
between E20 and V25RM: 12 in V25RM's favour (asym:64:3 seat 1 against fortress v9, v14, lead_v4 and lead_v6;
asym:65:2 seat 1 against fortress v29, v33, v34 and v35; eco6_t5 asym:62:2 seat 1; best_v9e asym:62:2 seat 0 and
mirror:61:2 both seats) and 6 against, all six against the lead's own bots (best_v9b asym:62:2 seat 0 and
mirror:66:3 both seats; best_v9e asym:62:2 seat 1 and mirror:66:3 both seats, draws for E20 that become losses
at round 16). Against the two lead bots together, hs3 + hs4: E20 27-12-9, V25RM 31-3-14.

**Pooled.** V25RM - E20: hs2 +59.6 [+14.0, +115.8] (168 conditions); hs3 + hs4 +36.7 [-19.0, +91.4] (408); hs2 + hs3
+ hs4 +43.4 [+1.3, +85.6] (576 conditions, 288 clusters; score difference +0.027 [0.000, +0.054]). V25RM was
frozen before all three sets were run, so all three are held out for this comparison. They are not held out for
V29, whose fill code was written from an hs2 failure case; on hs3 + hs4, V29 - V25RM = +0.6 [-6.5, +8.2] and V29 -
E20 = +37.3 [-16.7, +90.5].

**Recommendation (17.7 stands; set 4 adds the numbers and the failure class below).** The swap econ20 -> V25RM is a small positive on average
over the 576 held-out conditions; the 95% interval only just excludes zero, and the hs3 + hs4 interval alone does
not. It has a reproducible failure class: on the mirror three-site starts mirror:53:3, mirror:56:3 (hs3) and
mirror:66:3 (hs4), V25RM loses by round 16 to the strongest opponents (fortress v33-v35 on 53:3, the lead's
best_v9b and best_v9e on 66:3) where E20 wins or draws; the mechanism is under investigation (17.10, pending).
Six of V25RM's 18 changed outcomes on set 4 go against it, and all six of them are against the lead's own bots, so
in a field of lead-like opponents the swap could be neutral or worse. My recommendation: keep econ20 as the foreign target
in the freeze unless the lead values the pooled average over this failure class; if swapped, use V25RM (not V29,
which adds code and measured nothing on sets 3-4), spec
bot_research.experiments.economy.lead_alt:@make?base="v9e"&alt="v25rm"&<Insurer parameters>.

### 17.10 Addendum (2026-10-31T16:31:13Z): why the V25 family loses mirror:53:3; HANDOFF with growth-first openings (hand2); V30 on its own motivating cases (v30best)

**mirror:53:3 against fortress v33** (seat 0; the mirror start gives the same result in seat 1).
- Ablation dbg53b (runs/economy/dbg53b, both seats, logs kept): V23 (frozen econ23: econ20 plus replan_gain=400
  and replan_base=true), V25R (V25RM without the caps; scratch v25r.spec) and V25C (V25RM without own_in_layout;
  scratch v25c.spec) all lose -985 at round 16, as V25RM, V27 and V29 do in hs3. E20 wins +4895 at round 21
  (dbg53, runs/economy/dbg53). So the loss comes from what V23 adds to E20, the re-plan gain rule
  (replan_gain=400 with replan_base), not from own_in_layout or the caps.
- Re-plan gains at the first free decision round (scratch gain53.py: _s_final of lead_v3 and of hrt-w1's frozen
  v26 re-plan, iters 5000, seed = round, as econ23 computes them): mirror:53:3 550 -> 760 (gain 210), mirror:56:3
  490 -> 760 (270), mirror:66:3 360 -> 730 (370). All three are below 400, so V23 and its descendants keep lead_v3
  on these maps, while E20 adopts the re-plan. The other maps checked: mirror:51:2 +530 and mirror:63:3 +520 are
  above 400; mirror:61:2 +380 and asym:64:3 +370 (seat 0) / +110 (seat 1) are below.
- Trace (scratch trace53.py, V25RM, rounds 8-12; it patches only our own frozen module's planner reference and
  reproduces the hs3 log's actions):
  - Rounds 8-11: V25RM buys guns only (S 0, route 26, 16-20 free cells adjacent to the route).
  - Round 11: lock_reachable is False. hrt-w1's v15 plan_defense finds no S 1500 plan with 10**7 gold, either
    with lead_v3 or with the empty layout, so the saturation step is skipped.
  - Round 12: the unseen-purchase defence (11 threat compositions of the opponent's gold, lead_v3, partial
    "best") buys 16 walls and 9 splashes. That gives route 28 and S 260, and leaves no free cell adjacent to
    the route, so no later step can add splash.
  - Rounds 13-15: only guns are bought, and v33's tier5 wave kills us in round 16 (S 260, 30 guns, 82940 gold
    unspent).
  - E20 on the same map (dbg53 log) has 23 splashes on the re-planned layout by round 10, S 740 at route 36. It
    keeps HP 785 to the end.
- So this failure class is the layout choice. The 400 threshold was chosen in shift 2 (econ21 section) from two
  eco6_t5 losses where adopting the re-plan lost (gains 210 and 310). Here it rejects re-plans that would have
  won. The gain does not separate the two cases: those eco6_t5 re-plans had S_final 990 and 1150, higher than the
  760 here, so a threshold on the re-plan's own S does not separate them either. The difference is the opponent
  (eco6_t5 attacks early; v33 and best_v9e attack with tier5 later). I propose no rule. Any change would need a
  fresh held-out set, because sets 2-4 are used.

**HANDOFF with growth-first openings (hand2; the lead's 14:30Z question whether an opening economy reaches a lock
before round 12 against that counter).**
- Conditions: the 18 guard_handoff specs of experiments/economy/opp_handoff.txt (growth 5/6/7 x handoff round
  10-14, 16), standard start, both seats, 36 matches per candidate, logs kept (runs/economy/hand2; lock and
  factory table runs/economy/hand2_lock.out from scratch lock2.py).
- Candidates (fixed before the run): g0 = V29 + r1_units=0&attack_from=7; g5 = V29 +
  r1_units=0&attack_from=8&late_round=5&sat_from=5&sat_frac=1.0&sat_target=1500; g6 = the same with late_round=6
  and sat_from=6 (lane scratch g0/g5/g6.spec).
- For comparison, hand1 (17.6): V27, which has V29's defaults r1_units=1 and attack_from=2, went 2-0-34 -632.

| candidate | vs growth 5 | growth 6 | growth 7 | own first round with S >= 1500 |
|---|---|---|---|---|
| g0 | 12-0-0 +637 | 12-0-0 +711 | 12-0-0 +702 | none |
| g5 | 12-0-0 +779 | 10-2-0 +486 | 10-2-0 +486 | round 10 (growth 5), round 9 (growth 6, 7), in all 36 |
| g6 | 12-0-0 +702 | 12-0-0 +681 | 12-0-0 +676 | none |

- Answer: yes. g5, which saturates with all its gold from round 5 (target 1500), reaches S >= 1500 by round 9
  against growth 6 and 7 in every match. Its four draws are the handoff-round-10 opponents (0 at round 50).
- The larger effect is the opening itself. Without the round-1 poke and with no attack before round 7, g0 has
  16/55/62 factories at rounds 3/6/9 (V27 in hand1: 12/21/22), against the counter's 50 (growth 5) or 86
  (growth 6, 7) at round 6. g0 wins all 36 without ever locking: 26 by killing the counter in round 10 or 11,
  before or at its handoff to fortress v34, and 10 on HP at round 50.
- Uncertainty: g0, g5 and g6 change the standard-start opening. In sweep10 (shift 1), r1_units=0 lost by 5 to the
  round-1 pokers (poke_lock and the lead's v4-v6); that was with attack_from=2. So these are not candidates until
  the standard pool is measured. stdg (g0, g5, g6 and V29 on opp_key5, standard start, both seats) is queued
  after lift3. vbest (V29, V25RM, E20, g0, g5 and g6 against best_v9e, standard start, both seats) is running.

**v30best** (V30 against bots.best = best_v9e, sha256 70ef8eab..., on mirror:22:3 and asym:24:3, both seats,
logs kept): 0-0-4 (-2520 and -2520 on mirror:22:3, rounds 16; -917 and -2363 on asym:24:3, rounds 19 and 15).
These are the four bv9e losses that motivated fill_any (17.7). So V30 does not fix its own motivating cases
either, which agrees with its rejection on held-out set 3.

### 17.11 (2026-10-31T16:52:05Z) Tables against best_v9e for the report (lead request 16:24Z); lift_idle rejected

**Strongest frozen economy bots against best_v9e, both seats.** Opponent: bot_research.bots.best:decide with
best.py sha256 70ef8eab... or bot_research.experiments.lead.frozen.best_v9e:@make (byte-identical). All rows have 0
rejected actions and 0 bot errors. Rows are computed by lane scratch vtab.py from runs/economy/RUN/results.jsonl.
"HP diff" is our HP minus theirs at the end; "clipped mean" clips each match to [-800, 800]. Mirror scenarios give
the same result in both seats.

| candidate | run | conditions | seat 0 W-D-L | seat 1 W-D-L | worst HP diff | clipped mean | end rounds | max decide s |
|---|---|---|---|---|---|---|---|---|
| E20 | vbest | standard start | 0-0-1 | 0-0-1 | -10 | -10 | 50 | 0.9 |
| V25RM | vbest | standard start | 0-0-1 | 0-0-1 | -10 | -10 | 50 | 0.6 |
| V29 | vbest | standard start | 0-0-1 | 0-0-1 | -10 | -10 | 50 | 0.7 |
| g0 | vbest | standard start | 0-0-1 | 0-0-1 | -15 | -15 | 50 | 0.7 |
| g5 | vbest | standard start | 0-0-1 | 0-0-1 | -15 | -15 | 50 | 0.6 |
| g6 | vbest | standard start | 0-0-1 | 0-0-1 | -15 | -15 | 50 | 0.8 |
| V29 + r1_guard=30 | vbest2 | standard start | 0-0-1 | 0-0-1 | -7 | -7 | 50 | 3.3 |
| V29 + r1_guard=60 | vbest2 | standard start | 1-0-0 | 1-0-0 | +5 | +5 | 50 | 1.6 |
| g0 + r1_guard=30 | vbest2 | standard start | 0-1-0 | 0-1-0 | 0 | 0 | 50 | 0.8 |
| V25RM | bv9e | 12 development scenarios (ho1) | 8-0-4 | 5-1-6 | -5185 | +98 | 11-22 | 5.8 |
| V27 | ho1v27 | the same 12 | 9-0-3 | 6-1-5 | -5185 | +231 | 11-22 | 5.0 |
| V29 | ho1v29 | the same 12 | 9-0-3 | 6-1-5 | -5185 | +231 | 11-26 | 5.2 |
| E20 | hs3 | held-out set 3 (6 scenarios) | 0-3-3 | 3-3-0 | -1285 | 0 | 14-50 | 9.6 |
| V25RM | hs3 | held-out set 3 | 3-0-3 | 5-0-1 | -3790 | +267 | 12-28 | 6.5 |
| V27 | hs3 | held-out set 3 | 3-0-3 | 5-0-1 | -3790 | +267 | 12-27 | 4.2 |
| V29 | hs3 | held-out set 3 | 3-0-3 | 5-0-1 | -3790 | +267 | 12-27 | 4.1 |
| V30 (rejected) | hs3v30 | held-out set 3 | 2-0-4 | 4-0-2 | -4645 | 0 | 12-27 | 4.3 |
| E20 | hs4 | held-out set 4 (6 scenarios) | 2-3-1 | 1-3-2 | -3770 | 0 | 11-23 | 2.3 |
| V25RM | hs4 | held-out set 4 | 4-1-1 | 1-1-4 | -3780 | 0 | 11-23 | 2.3 |
| V29 | hs4 | held-out set 4 | 4-1-1 | 1-1-4 | -3780 | 0 | 11-23 | 3.5 |

- Scenario lists: ho1 = mirror:1:2 asym:3:2 mirror:21:2 mirror:22:3 asym:23:2 asym:24:3 mirror:31:2 asym:32:2
  mirror:33:3 asym:34:3 asym:35:2 mirror:36:3; set 3 = mirror:51:2 asym:52:2 mirror:53:3 asym:54:3 asym:55:2
  mirror:56:3; set 4 = mirror:61:2 asym:62:2 mirror:63:3 asym:64:3 asym:65:2 mirror:66:3. Specs: lane scratch
  e20/v25rm/v27/v29/v30/g0/g5/g6/v29rg30/v29rg60/g0rg30.spec; V25RM and V29 are also lead_alt ALTS entries.
- The scenario starts are decided by who locks first (11-28 rounds) and by the start itself: each asym scenario's
  seats differ. They measure behaviour from foreign starts, not the standard game.
- **Standard start.** Every frozen economy bot loses to best_v9e by 10 (E20, V25RM, V29: 785:795) or by 15 (g0, g5,
  g6: 785:800) at round 50, in both seats. Both sides lock (V29 S 1560 at round 10; best_v9e S 640-1230 in rounds
  10-14 and S 1510 at round 15), so the match is decided by the round-1 exchange: best_v9e's three tier1 deal 15,
  our one tier1 deals 5 (the g bots send none).
- **The kill attempt is blocked by the same-round defence (lane scratch killshot.py on the vbest V29 seat-0 log,
  runs/economy/vbest/logs/...-00001-...).** With fastsim against best_v9e's end-of-round maps, with no response:
  on its maps after rounds 10-13 no affordable all-tier5, all-tier4 or all-tier3 package reaches its HP 795 (the
  most is 4 tier5 for 280 damage on the round-10 map; at the round-14 decision, 15203 gold, 23 tier5 deal 0). Its round-14 map (identical to round 13: it bought only factories in rounds 13
  and 14) stops up to 28 tier5 but not 29 (18850 gold). At the round-15 decision V29 had 27801 gold and bought 32
  tier5 (20800 gold; the finish step: finish="opt", the default, buys before the other purchases the cheapest
  package that with the active roster removes the opponent's whole HP on its current map with no response). In
  the same round best_v9e built 5 walls and 3 splashes (S 1510) and all 32 were stopped. I did not trace
  best_v9e's reason; the timing (its first turret purchase since round 12, when our visible gold first sufficed)
  is consistent with its defence planning against our gold. Skipping V29's factory purchases (about 400, 8000 gold,
  per round in rounds 12-14) would not have made a kill affordable at round 14, since a factory returns its 20 gold
  within two rounds (+15 per round).
- The later attack() step cannot buy such a package before round 48: it values a package at its damage capped at
  the opponent's HP and buys only if that exceeds theta (0.2 through round factory_stop = 47) times the net cost
  (cost minus expected bounties), so the net cost must be below 5 x the opponent's HP, at most 4000 gold.
  Expensive kills are bought only by the finish step, as exact kills against the current map.
- **r1_guard (vbest2).** r1_guard=G lets the unseen-purchase defence spend up to G gold in round 1 with share 1.0
  against the opponent's possible round-1 purchases. With G=60 (one splash) V29 stops best_v9e's three tier1 and
  wins 800:795 in both seats. G=30 (one gun1) is not enough (771:778). g0 + r1_guard=30 draws 800:800. This is one
  opponent and one start. In sweep7 (shift 2) r1_guard was rejected on the standard pool, so the margin here is a
  development result until stdrg (V29 + r1_guard=60 and g0 + r1_guard=30 on opp_key5, standard start, both seats)
  is compared with V29 on the same conditions.

**lift_idle (econ28 gate lift, carried into econ29) is rejected.** lift3: V29 + lift_idle=3 and V29 + lift_idle=6 on
experiments/economy/opp_lift1.txt (10 opponents) x mirror:41:2 mirror:43:3 asym:45:2 mirror:1:2 asym:3:2 asym:23:2,
both seats, 120 matches each. Baseline: V29 in runs/economy/lift2_partial (84 conditions, the first 7 opponents;
lift2 was stopped at 14:40Z). Paired clipped difference, cluster bootstrap over (opponent, scenario), lane scratch
pboot.py:
- lift_idle=3 minus V29: -64.0 [-134.9, +7.7] (84 conditions, 42 clusters); score +0.012 [-0.036, +0.077].
  Changes: eco6_t5 asym:45:2 seat 1 L -1030 to D +117; v26 mirror:43:3 L -26 (round 50) to W +7534 in both seats;
  mixed5 asym:3:2 seat 0 W +626 to D +45; v34 asym:3:2 seat 0 W +9066 to L -1249.
- lift_idle=6 minus V29: -56.0 [-108.9, -14.9]; score -0.030 [-0.083, 0.000]. Changes: eco6_t5 asym:23:2 seat 1 W
  +560 to D -40, eco6_t5 mirror:43:3 W +493 to L -294 in both seats.
- Against best_v9e on the three lift3 scenarios that ho1v29 also has (asym:23:2, asym:3:2, mirror:1:2, both seats):
  lift_idle=3 is worse in 5 of 6 conditions (asym:23:2 seat 0 +1250 to -940, asym:3:2 seat 0 +2370 to -805, seat 1
  -830 to -4050, mirror:1:2 +2660 to +1265 in both seats) and better in one (asym:23:2 seat 1 -4470 to -2650);
  lift_idle=6 is worse in one (asym:23:2 seat 0 +1250 to -3510) and equal in the others.
- So lifting the foreign attack hold early, on the test "the opponent built no turret since the map became
  foreign", loses more than it gains on these conditions. econ29 keeps lift_idle unset (its default).

### 17.12 (2026-10-31T17:54:49Z) Growth-first openings and the round-1 guard on the standard pool (stdg, stdrg)

Conditions for both runs: experiments/economy/opp_key5.txt (45 opponents), standard start, both seats, 90 matches per
candidate, candidates fixed before the runs (lane scratch specs). stdg (runs/economy/stdg, JOBS=2): g0, g5, g6 (17.10)
and V29. stdrg (runs/economy/stdrg, JOBS=1): V29 + r1_guard=60 and g0 + r1_guard=30, the two variants of 17.11 that
did not lose to best_v9e on the standard start. Differences: cluster bootstrap over the 45 opponents (pairs of seats),
4000 resamples; score counts a win 1 and a draw 0.5.

| candidate | W-D-L | clipped mean | minus V29, clipped [95%] | minus V29, score [95%] |
|---|---|---|---|---|
| V29 | 82-2-6 | +388 | | |
| g0 (no round-1 poke, attack from round 7) | 70-2-18 | +416 | +28.7 [-11.0, +67.3] | -0.133 [-0.233, -0.044] |
| g5 (g0 + saturation from round 5) | 42-2-46 | +335 | -53.1 [-110.5, -5.3] | -0.444 [-0.589, -0.311] |
| g6 (the same from round 6) | 58-2-30 | +397 | +9.7 [-39.3, +56.6] | -0.267 [-0.400, -0.144] |
| V29 + r1_guard=60 | 40-4-46 | -137 | -524.9 [-661.1, -393.4] | -0.456 [-0.611, -0.300] |
| g0 + r1_guard=30 | 66-18-6 | +376 | -12.1 [-54.9, +27.8] | -0.089 [-0.178, -0.011] |

- V29 equals V25RM (std24m) in all 90 matches, as expected: the fill acts only on foreign maps (17.6). The last two
  rows were bootstrapped against std24m for that reason.
- g0, g5 and g6 lose by 5 to 37 at round 50, both seats, against opponents that land something early and then lock:
  econ v2 and v3 late6 phi0 (-30; V29 +32), best_v9a (-10; V29 -5), fortress v21 (-10; V29 -5), the lead's two
  r1_poke=3 / fortress_n=4 specs (-15; V29 +16), econ v4 r1_guard=30 early_attack_frac=0.3 (-5; V29 +52), the
  opening_units=1 phi=1.0 saturate_round=20 counter (-5; V29 0), guard_poke5 (-37 for g0 and g6, -17 for g5; V29
  -15). Two logs show the mechanism: g0 and g5 against econ v2 (seat 0) buy four factories and no turret in round 1,
  econ v2 lands six round-2 tier1 (30), and nothing lands afterwards in either direction; g5 against lead v4 loses
  the 10 of two round-1 tier1. g5 also loses (-20 to -52) to opponents that g0 beats: fortress v9, v11, v14 and v22
  and the lead's best_a, best_b and best_v3b. In the lead v4 log (seat 0) g5 buys only splashes in rounds 5-8, its
  first tier5 in round 10, and none of its purchases in rounds 10-13 lands. Conjecture (g0's winning logs were not
  kept): g0 wins these games with attacks bought in rounds 7-9 from the gold that g5 puts into saturation.
- The round-1 guard: V29 + r1_guard=60 bought a gun2, two walls, its round-1 tier1 and no factory in round 1 in all
  90 matches. Against fortress v14 (seat 0) it had 10 factories at round 5 where V25RM had 35, and it lost
  -1165 at round 12; 36 of its 46 losses end in rounds 8-12, the other 10 at round 50. g0 + r1_guard=30 bought a
  gun1, three factories and two walls in round 1 in all 90. Against g0 it turned 12 of g0's 18 losses into draws and 6 wins (lead v4, v5, v6) into
  draws, and it won fortress v9 attack_from=6 (g0 0); minus g0: clipped -40.8 [-77.1, -11.2], score +0.044 [-0.022,
  +0.111]. Its remaining losses are guard_poke5 (-37) and econ v2 and v3 late6 phi0 (-79), both seats.
- Conclusion (empirical, these 45 opponents, standard start): none of the five variants is better than V29 on score;
  g0 has the higher clipped mean but not significantly. Together with 17.10 (hand2) and 17.11 (vbest) this gives a
  trade: the growth-first openings beat the HANDOFF growers (g0 36-0-0, V27 2-0-34) and lose small lock-versus-lock
  margins to the early pokers. Since the round-1 choice is blind (entry 11), the trade cannot be removed in round 1;
  whether a round-2 observation can separate the two families is untested.
- Running: grow1 (g0, g5, V29 against a copy of the lead's GROWERS pool, experiments/economy/opp_growers.txt,
  standard start, both seats, JOBS=1), then hand3; gmaze1 (the same three against GUARDED_MAZE, opp_gmaze.txt,
  JOBS=2), then stdg2. hand3 and stdg2 split g0 into its two changes: g1 = V29 + attack_from=7 (keeps the round-1
  tier1) and g2 = V29 + r1_units=0 (attacks from round 2), on the HANDOFF specs (logs kept) and on opp_key5; both
  were fixed at 17:53Z before any of their matches.

### 17.13 (2026-10-31T18:09:35Z) The lead's grower pools GROWERS and GUARDED_MAZE against g0, g5 and V29 (grow1, gmaze1)

Conditions: standard start, both seats, candidates g0, g5 and V29 (lane scratch specs, unchanged since 17.10).
grow1: experiments/economy/opp_growers.txt, a copy of the lead's pools.GROWERS (35 roster_bait and 36 maze_grower
settings), 142 matches per candidate, JOBS=1. gmaze1: experiments/economy/opp_gmaze.txt, a copy of pools.GUARDED_MAZE
(72 guarded_maze settings), 144 per candidate, JOBS=2. Logs of non-wins kept. Comparison column: the lead's numbers on
the same pools for best_v9e (= V18FT) and P5TNUBM (reports/REPORT.md, runs g9a-g9d and gm2-gm3), not rerun here.

| pool | g0 | g5 | V29 | best_v9e (lead) | P5TNUBM (lead) |
|---|---|---|---|---|---|
| GROWERS (142) | 142-0-0, worst +240, clip +728 | 128-4-10, worst -1312, clip +463 | 140-2-0, worst +117, clip +571 | 66-0-76 (worst -1955) | 142-0-0 (+368) |
| GUARDED_MAZE (144) | 144-0-0, worst +512, clip +757 | 144-0-0, worst +536, clip +793 | 72-0-72, worst -1310, clip -85 | 66-0-78 (worst -1340) | 144-0-0 (+268) |

- Each seat has the same W-D-L (half of each total). No bot errors, no rejected actions; the largest single decision
  took 2.4 s (g0, grow1).
- Matches end early: g0 in rounds 9-12, g5 in rounds 10-14, V29 in rounds 7-10 on GROWERS and 8-16 on GUARDED_MAZE.
- V29 on GROWERS: 132 of its 140 wins end in round 7 or 8. Its two non-wins are one maze_grower setting
  (lead_opening, growth 5, tier2 bait) in both seats, a draw at round 9 with HP difference +125, so both bases fell
  in the same round.
- V29 on GUARDED_MAZE loses 72 matches, all against settings with guard_round 4 or 5 (70 with growth_rounds 5 or 6,
  2 with growth 4). It wins all 54 with guard_round 3 and the other 18 with guard_round 4.
- Example loss: guard_round=5, growth 5, empty layout, no bait, seat 0, -579 at round 9.
  - V29 buys 25 tier1 and one tier3 in rounds 1-5 and has 17 factories at round 5 against the grower's 52.
  - The grower builds its single splash in round 5. Its HP then falls by only 26 per round.
  - From round 6 it adds one tier5 per round. V29's HP over rounds 5-9 is 800, 660, 520, 240, -40, while it
    buys one to three guns per round and five splashes in round 9.
  - The losing pattern resembles the eco6_t5 case of entry 16: one tier5 per round against a map below the lock.
    There the foreign gate held the attacks. Here the map is the standard one, and the 18 factories after the
    early pokes are too few to build an answer in time.
- g5's 14 non-wins on GROWERS are seven settings, each in both seats, all ending in round 10 or 11.
  - Losses (-715 to -882): roster_bait with growth 7 and a tier2 bait, roster_bait with growth 8 and three tier1, and
    maze_grower with growth 7 and a tier2 bait on each of its three layouts.
  - Draws: roster_bait with growth 9 and a tier2 bait (HP difference -1312, both bases fell) and maze_grower
    lead_opening with growth 7 and no bait (-28).
  - The logs are kept; the mechanism is not traced.
- Reading together with 17.12 (empirical, these pools, standard start):
  - g0 wins every match on the three grower pools tested (HANDOFF 36-0-0, GROWERS 142-0-0, GUARDED_MAZE 144-0-0).
  - g0 loses 18 of 90 on opp_key5 (small lock-versus-lock margins, -5 to -37), where V29 loses 6.
  - V29 beats the GROWERS family that best_v9e loses, but not GUARDED_MAZE.
  - Neither economy bot beats best_v9e on the standard start (17.11).

### 17.14 (2026-10-31T18:28:45Z) Which half of g0 wins the growers: g1 (attack hold only) and g2 (no round-1 tier1 only) (hand3, stdg2)

g0 (17.10) differs from V29 in two parameters: r1_units=0 (no round-1 tier1) and attack_from=7 (no attack purchase
before round 7). g1 = V29 + attack_from=7 and g2 = V29 + r1_units=0 (lane scratch g1.spec, g2.spec, fixed at 17:53Z
before any of their matches) separate the two. Standard start, both seats.

hand3 (the 18 HANDOFF specs of experiments/economy/opp_handoff.txt, 36 matches per candidate, JOBS=1, logs kept):

| candidate | W-D-L | worst | clipped mean |
|---|---|---|---|
| g1 (keeps the round-1 tier1, attacks from round 7) | 36-0-0 | +301 | +703 |
| g2 (no round-1 tier1, attacks from round 2) | 6-0-30 | -1368 | -469 |
| g0 (hand2, 17.10) | 36-0-0 | | |
| V27 (hand1, 17.6; V27 and V29 differ only on foreign maps) | 2-0-34 | | -632 |

- g1 bought one tier1 and four factories in round 1 in all 36 matches. It won 26 by killing the counter in rounds
  10-11 and 10 on HP at round 50, the same split as g0.
- g2 won only against growth 5 with handoff rounds 12, 14 and 16. It lost all 12 against growth 6 (-668, round 9)
  and all 12 against growth 7 (-808 and -1368, round 10).
- So on HANDOFF the attack hold until round 7 decides the result, not the round-1 tier1 (empirical, these 18 specs).
  The held gold goes into factories.

stdg2 (opp_key5, 90 matches per candidate, JOBS=2). g1 is complete; g2 was still running when this was written.

| candidate | W-D-L | clipped mean | minus V29, clipped [95%] | minus V29, score [95%] |
|---|---|---|---|---|
| V29 (stdg) | 82-2-6 | +388 | | |
| g1 | 76-2-12 | +441 | +53.4 [+8.5, +96.2] | -0.067 [-0.178, +0.022] |
| g0 (stdg) | 70-2-18 | +416 | +28.7 [-11.0, +67.3] | -0.133 [-0.233, -0.044] |

- g1 minus g0: clipped +24.7 [+3.5, +48.5], score +0.067 [+0.011, +0.133].
- Outcome changes from V29 to g1, each in both seats:
  - fortress v21: from L -5 to W +107.
  - econ v2 and v3 late6 phi0: from W +32 to L -15.
  - econ v4 r1_guard=30 early_attack_frac=0.3: from W +52 to L -5.
  - the lead's r1_poke=3 robust spec: from W +16 to L -10.
- g1's other non-wins are the same as V29's: guard_poke5 -37 (V29 -15), best_v9a -5, and a draw against the
  opening_units=1 phi=1.0 counter.
- Against g0, the round-1 tier1 is worth 5 HP against best_v9a and the r1_poke=3 robust spec (-10 to -5 and -15 to
  -10) and 15 against econ v2 and v3 (-30 to -15). Against fortress v21 g1 wins +107 where g0 loses -10.
- Running (fixed before any of its matches): g1chk = g1 against best_v9e, GROWERS and GUARDED_MAZE (288, JOBS=1).
  After stdg2: fam2b = V29, g0 and g1 against copies of the lead's TIMING2, STAGED, SCREENED and PUNISH pools (822,
  JOBS=2).
- A first fam2 run (V29 and g0 only) was stopped after 23 matches to free its core for g1chk. It is kept as
  runs/economy/fam2_stopped and is not used.

### 17.15 (2026-10-31T18:48:15Z) g1 on the lead's grower pools and against best_v9e; g2 on opp_key5 (g1chk, stdg2)

Conditions: standard start, both seats, the lead's harness on the unchanged engine. Runs: runs/economy/g1chk (g1
against experiments/economy/opp_g1check.txt, which holds best_v9e and copies of the lead's GROWERS (71 specs) and
GUARDED_MAZE (72 specs) pools, 288 matches, done 18:45Z) and runs/economy/stdg2 (g1 and g2 on opp_key5, 180 matches,
done 18:46Z). g1 = V29 + attack_from=7, g2 = V29 + r1_units=0 (17.14). The V29 and g0 numbers are from vbest (17.11),
grow1 and gmaze1 (17.13) and stdg (17.12).

| candidate | best_v9e | GROWERS | GUARDED_MAZE | opp_key5 |
|---|---|---|---|---|
| V29 | 0-0-2 (-10 in both seats) | 140-2-0 | 72-0-72 | 82-2-6 |
| g0 | 0-0-2 (-15 in both seats) | 142-0-0 | 144-0-0 | 70-2-18 |
| g1 | 0-0-2 (-10 in both seats) | 142-0-0 | 144-0-0 | 76-2-12 |
| g2 | not run | not run | not run | 74-0-16 |

- g1 on the grower pools: every game ends in rounds 9-12; the smallest margin is +118 (GROWERS) and +534
  (GUARDED_MAZE). Paired over the 143 grower specs (286 games): g1 - V29 = +480.4 [+375.0, +585.1] clipped HP, score
  +0.255 [+0.182, +0.329]; g1 - g0 = -21.4 [-45.3, +0.6], with identical outcomes in all 286.
- g1 against best_v9e loses by 10 at round 50 in both seats, the same result as V29; g0, which also drops the round-1
  tier1, loses by 15 (17.11).
- On opp_key5 all 12 g1 losses end at round 50 with margins 5 to 37 HP (-5 four times, -10 twice, -15 four times, -37
  twice).
- g2 on opp_key5: 74-0-16, clipped mean +360. The 16 losses are both seats against 8 opponents (poke_lock with
  opening_units=1 and saturate_round=20, lead_v4, lead_v5, lead_v6, fortress v21, best_v9a, two lead_v15 variants), all
  at round 50 by 5 or 10 HP. g2 - V29 = -27.7 [-60.4, +4.4], score -0.100 [-0.211, 0.000]; g2 - g0 = -56.4 [-87.0,
  -27.7], score +0.033 [-0.089, +0.156]. Removing only the round-1 tier1 is worse than V29 on opp_key5 and loses
  HANDOFF (6-0-30, 17.14), so it is rejected.

Conclusion for these conditions: on the standard-start pools where g1 was run, its record equals V29's against
best_v9e, is higher on GROWERS, GUARDED_MAZE and HANDOFF (36-0-0 against V27's 2-0-34, 17.14; V27 and V29 differ only
in the foreign-map fill, which does not act on the standard start), and is lower on opp_key5, where it has 6 more
losses (all at round 50, at most 37 HP) and a higher clipped mean (17.14). Of the variants run both against best_v9e
and on the grower pools (V29, g0, g5, g1), only g1 matches V29 on the first and g0 on the second. g1 has not been run
on any scenario start. In econ29 the foreign hold (foreign_attack_from=11) blocks only the ordinary attack, not the
finish and doom attacks, so on a map with buildings g1 never requested, attack_from=7 changes only finish and doom
purchases before round 7 (and the rounds before the map became foreign). Conjecture, not measured: g1's results on
such scenario starts stay close to V29's. Scenario starts without foreign buildings are untested.

Running at the time of writing: vbf (V29, g0 and g1 against the lead's best_v9f, installed 18:29Z, standard start, both
seats), then fam2b (V29, g0 and g1 on copies of the lead's TIMING2, STAGED, SCREENED and PUNISH pools).

## Entry 18 (2026-10-31T18:48:15Z): summary of this lane's results for the report

This entry only collects results stated in entries 1-17; each item names the entry with the exact conditions. All
matches were played with the lead's harness on the unchanged engine (balanced rules), both seats.

### Artifacts

- Tools (owned files, entry 1 and later): bots/economy/fastsim.py (exact replica of one map's combat, equal to
  td_game.combat.simulate_map on 450 random maps and rosters, 0 mismatches), guarantee.py (Theorem B), offense.py
  (package search), threat.py, defense_plan.py, fillplan.py (lock fill, 17.3), experiments/economy/run_tourn.sh,
  freeze.sh, capacity.py, reach_check.py, replan_reach.py, replan_fill.py, lead_alt.py (the lead's Insurer with a
  different foreign target, 17.1).
- Frozen bots: bots/economy/frozen/<tag>/ with SHA256SUMS (v2 to v30; files never edited after freezing).
- Specs of the three bots compared on the held-out sets (lane scratch e20.spec, v25rm.spec, v29.spec; the
  standard-start variants g0, g1, g2, g5, g6 add parameters to the V29 spec, entries 17.10, 17.12, 17.14):
  - E20 = frozen v20 econ20 with the lead's parameters (the foreign target inside best_v9e):
    bot_research.bots.economy.frozen.v20.econ20:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11
  - V25RM = frozen v25 econ25:
    bot_research.bots.economy.frozen.v25.econ25:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true&own_in_layout="replan"&own_min_s=1200&min_cap=3000&active_cap=4000
  - V29 = frozen v29 econ29 with the V25RM parameters plus &fill=true&fill_reserve=true&fill_threat=true.
  - On the standard start V29 plays exactly as V25RM (the fill only acts on foreign maps, 17.6).

### Proved statements (hypotheses as stated in the entries)

- Proposition 1 (entry 1): a factory bought in round r returns 15(50 - r) usable gold, net 15(50 - r) - 20,
  positive for r <= 48.
- Proposition 4 and Proposition 5, the lock (entries 1 and 2): if a player's route has per-copy splash S >= h, no copy
  with HP <= h reaches its base while it builds nothing more; with S >= 1500 its HP never decreases again.
- Lemma 1 and corollaries (entry 2): route cells induce a linear forest; a splash deals at most 70 to one copy; the
  route has at most 107 cells.
- Theorem B (entry 2): a lower bound on the damage of a package against every same-round response that the
  defender's visible gold can buy (guarantee.py; 276 checked cases, 0 violations).
- Proposition F (entry 7) and Proposition G (entry 15): on a map below the lock (S < h) the number of arrivals of
  N copies of HP h is at least A(N) - floor(250 G / (h - S)), so it grows without bound in N; no number of guns
  makes a map immune, only S >= h does. Consequence (entry 15): the purchase caps min_cap=300 and active_cap=500
  kept the finish rule from buying the kill it would otherwise find on a sub-lock fortress (fortress v28, round 24:
  769 tier5 for 30800 simulated damage); v24m raised the caps to 3000 and 4000 with no new code.
- Route lemma (Astra bfs_reserve, 17.6): the engine's BFS returns the lexicographically least shortest path, so
  blocking cells off the route leaves the route unchanged and a new off-route splash adds exactly 10 per adjacent
  route cell.

### Main empirical findings

1. Growth before defence (entry 1, sweep1, 26 tuning opponents): defending only against the visible roster until
   round 6 (late_round=6, phi=0) went 52-0-0; defending against everything the opponent's visible gold could buy went
   46-0-6.
2. Lock-versus-lock is decided early (entries 2, 5 and 17.11): self-play of growth bots ends 755:755 from round-2 and
   round-3 pokes (rr2). On the standard start against best_v9e every frozen economy bot loses by 10 (E20, V25RM, V29)
   or 15 (g0, g5, g6) at round 50, both seats, from the round-1 exchange. The best round-1 poke size depends on the
   opponent pool (sweep10). The round-1 purchase is chosen blind (both players see the same initial observation), so
   no observation rule can pick a round-1 counter only against the openings it beats (entry 11, r1t2: one tier2
   instead of one tier1 turned the three targeted pairings into wins and lost others: 76-0-14 against 82-2-6).
3. Scripted starts (entries 7-17): holding attack purchases until round 11 on a map with buildings the bot never
   requested (v17) raised the 108 scen17 conditions from 89-0-19 to 107-0-1 without changing any standard-start
   result (std18 identical to v16 in all 82). Then: hrt-w1's re-planned layouts with a gain rule (v21, v23), attack
   caps raised so the finish rule can break a sub-lock fortress (v24m: 41-0-11 against 34-0-18 on 52 fortress
   conditions), and a lock fill with a reservation (V27, V29: fortress v33 on mirror:43:3 from -2100 to +980).
4. Held-out sets 2, 3 and 4 (576 conditions, 288 clusters; 17.9): V25RM - E20 = +43.4 [+1.3, +85.6] clipped HP,
   score +0.027 [0.000, +0.054]. Sets 3 + 4 alone: +36.7 [-19.0, +91.4]. V29 - V25RM on sets 3 + 4: +0.6
   [-6.5, +8.2]. Failure class: mirror three-site starts (mirror:53:3, mirror:56:3, mirror:66:3) against the strongest
   opponents, caused by the re-plan gain threshold (17.10).
5. Against best_v9e (17.11 table): on the scenario starts V25RM/V27/V29 win more often than E20 (hs3: 8-0-4 against
   3-6-3); their worst single results are -5185 (12 ho1 scenarios, bv9e) and -3790 (hs3).
6. Growth-first openings (17.10): against hrt-w3's guard_handoff growers, V27 went 2-0-34, while g0 (V29 without the
   round-1 poke and no attack before round 7) went 36-0-0 and g5 (saturating from round 5) locked by round 9-10 in all
   36. On opp_key5 (standard start, 17.12) the same openings lose small lock-versus-lock margins to the early pokers:
   g0 70-2-18, g5 42-2-46, g6 58-2-30 against V29's 82-2-6 (score -0.133 [-0.233, -0.044] for g0).
7. The lead's grower pools (17.13, standard start, both seats): g0 142-0-0 on GROWERS and 144-0-0 on GUARDED_MAZE;
   V29 140-2-0 on GROWERS and 72-0-72 on GUARDED_MAZE (all 72 losses against settings with guard_round 4 or
   5). The lead's best_v9e numbers on the same pools are 66-0-76 and 66-0-78. So the grower
   family is not a counter to an economy bot as such: V29's attacks from round 2 win GROWERS, and g0's growth-first
   opening wins both pools, at the cost of finding 6.
8. The attack hold, not the missing round-1 tier1, wins HANDOFF (17.14): g1 = V29 + attack_from=7 went 36-0-0 and
   g2 = V29 + r1_units=0 went 6-0-30. On opp_key5 g1 went 76-2-12 (V29 82-2-6, g0 70-2-18): clipped +53.4 [+8.5,
   +96.2] and score -0.067 [-0.178, +0.022] against V29, score +0.067 [+0.011, +0.133] against g0. On the lead's
   pools (17.15) g1 went 142-0-0 on GROWERS and 144-0-0 on GUARDED_MAZE (g1 - V29 over the 143 specs: +480.4
   [+375.0, +585.1] clipped, score +0.255 [+0.182, +0.329]) and lost to best_v9e by 10 in both seats, as V29 does.
   g2 went 74-0-16 on opp_key5 (score -0.100 [-0.211, 0.000] against V29) and is rejected. g1 has not been run on
   any scenario start.

### Rejected ideas (each measured; entry)

- Global attack hold on the standard start (entry 8, sweep17: attack_from=11 44-4-34 against 76-2-4).
- A round-1 tier2 instead of a tier1 (entry 11, r1t2).
- Persistence-aware attack value (entry 4, sweep5: no effect); alpha below 1 (sweep6).
- Threat-triggered early insurance v14 (entry 5).
- econ22 race (lift the foreign hold while the own lock is unreachable; entry 14).
- econ30 fill_any (17.7: -88.7 [-173.7, -15.3] against V29 on held-out set 3).
- lift_idle 3 and 6 (17.11).
- r1_guard (sweep7, entry 4; 17.12): V29 + r1_guard=60 beats best_v9e +5 on the standard start but goes 40-4-46 on
  opp_key5 against V29's 82-2-6 (a round-1 gun2 instead of four factories); g0 + r1_guard=30 turns 18 of g0's 90
  results into draws, score -0.089 [-0.178, -0.011] against V29.

### Open failure cases

- eco6_t5 on mirror:41:2 (-980, both seats; entry 16): no early answer to one tier5 per round while the foreign gate
  holds attacks.
- asym:35:2 seat 0 against 8 opponents (entry 15): the seat starts 5 HP down and its greedy splash capacity is 650.
- Re-plan gain threshold on mirror three-site starts (17.10).
- The round-1 exchange against best_v9e on the standard start (17.11).
- V29 against GUARDED_MAZE with guard_round 4 or 5 (17.13): in the traced loss its early tier1 pokes leave 17
  factories at round 5 against 52, and one tier5 per round from round 6 ends the game in round 9 (all 72 losses end
  in rounds 8-12).

### Recommendation (17.9, with one addition from 17.15)

Keep econ20 as best_v9e's foreign target unless the pooled held-out average is valued over the mirror three-site
failure class; if swapped, use V25RM through lead_alt:
bot_research.experiments.economy.lead_alt:@make?base="v9e"&alt="v25rm"&<Insurer parameters>.
None of this lane's standalone bots should replace best_v9e: each loses to it on the standard start (17.11).
Where the report needs one standalone economy bot for standard-start tables, g1 (V29 + attack_from=7) is the best
trade measured here (finding 8): V29's result against best_v9e, g0's results on the grower pools, and 76-2-12 on
opp_key5 between V29 (82-2-6) and g0 (70-2-18). Its spec is the V29 spec followed by &attack_from=7 (lane scratch
g1.spec).

### Running at the time of writing

- vbf (V29, g0 and g1 against the lead's best_v9f, standard start, both seats), then fam2b (V29, g0 and g1 against
  copies of the lead's TIMING2, STAGED, SCREENED and PUNISH pools). Results will be added as addenda.

### Uncertainty

- Matches against hrt-w1's fortresses v25-v35 are single samples of an opponent with a wall-clock budget.
- The held-out sets are scenario starts; the standard start was measured on opp_key4w/opp_key5 (41/45 opponents) and
  on the lead's pools only where stated.
- Bootstrap intervals are over (opponent, scenario) clusters of one opponent list; they do not cover opponents outside
  it.

### 18.1 (2026-10-31T18:49:02Z) Addendum: V29, g0 and g1 against best_v9f (vbf)

Conditions: the lead's best_v9f (experiments/lead/frozen/best_v9f.py, sha256 prefix 36d861fc, installed 18:29Z),
standard start, both seats, runs/economy/vbf (6 matches, all logs kept, done 18:46:27Z). V29 0-0-2 (-10 at round 50 in
both seats), g0 0-0-2 (-15 at round 50 in both seats), g1 0-0-2 (-10 at round 50 in both seats). These are the same
results as against best_v9e (17.11, 17.15). In all 6 logs the only HP changes are in the round-1 snapshot (V29 and
g1 785 against best_v9f's 795; g0 785 against 800) and neither base loses HP afterwards, so finding 2 of entry 18 (the
round-1 exchange decides the game) also holds against best_v9f on the standard start for these three bots.

Storage note (2026-10-31T18:51:15Z): to keep runs/economy under 3 GB, the match logs (logs/*.jsonl) of stdg, stdg2, stdrg, hs3,
std24m, std24, std22, w1v29, w1v29b, w1v29c, w1v29e, hand2, sweep2, sweep13, sweep15, sweep16, sweep17, hs4, lift3,
hs2e20, strike1, grow1, gmaze1 and r1t2 were compressed with gzip (names end in .jsonl.gz; contents unchanged).
results.jsonl and summary.md files are not compressed.

### 18.2 (2026-10-31T18:53:03Z) Addendum: a reactive attack hold would not separate the growers from the early pokers (log diagnosis, no new matches)

Question: can an observation rule keep g1's attack hold against the growers and V29's early attacks against the
opponents of 17.14 where g1 loses? The rule considered: attack before round 7 only after the opponent has bought a
minion in some round from 2 on (its roster entries carry bought_round). Data: the opponents' roster snapshots up to
round 6 in the kept logs of grow1, gmaze1 (all candidates) and stdg (V29 rows), scratch scripts oppfirst.py and two
inline variants.

- The growers buy minions in round 2 in most settings. First purchase after round 1: maze_grower round 2 in 162 of
  216 games, round 6 in 18, none before round 7 in 36; roster_bait 168, 12 and 30 of 210; guarded_maze 288, 90 and
  54 of 432. The most frequent round-2 purchases are one tier1, two tier1 or one tier2 (maze_grower), one, two or
  three tier1 (roster_bait) and one tier1 or one tier2 (guarded_maze, which also buys one tier5 in round 6 in many
  settings).
- In V29's 144 GUARDED_MAZE games the opponent bought a minion in round 2 in 96, and 50 of V29's 72 losses are among
  them (10 losses with the first purchase in round 6, 12 with none before round 7).
- Of the opponents that beat g1 but not V29 on opp_key5 (17.14), the three econ specs (v2 and v3 late6 phi0, v4
  r1_guard=30) buy 1 to 4 tier1 in round 2 and 2 to 8 in round 3, while the lead's r1_poke=3 robust spec
  (bots.economy.frozen.lead_v15) buys nothing in rounds 2 to 6.

So the rule would release the early attacks in two thirds of the GUARDED_MAZE games, including 50 of V29's 72 lost
games, and would keep the hold against the lead_v15 spec, which V29 beats (+16) and g1, differing from V29 only in the
hold, loses to (-10). Conjecture, not measured: the rule would lose most of those 50 games as V29 does. I did not
implement it. These data do not support a rule keyed on purchase size or type either: one to three tier1 in round 2
appear in both families.

### 18.3 (2026-10-31T19:15:54Z) Pre-statement: fresh standard-start opponents for V29, g1 and g0 (fresh5a, fresh5b; no result seen)

Opponent list experiments/economy/opp_fresh5.txt, fixed 2026-10-31T19:15:21Z before any match of these candidates
against these opponents: the lead's af2g (best_v9f with passive_until=null) and V33M (best_v9f with
passive_mid_from=null), P4TNUB and P5TNUBM (the lead's v28 and v30 specs of 14:53Z), hrt-w1's frozen fortress v36 to
v43, and fifteen hrt-w3 counters written in shift 3 with default parameters (hp_handoff, forecast_handoff,
early_guard_handoff, early_heavy_handoff, budget_handoff, triggered_budget_handoff, guarded_round4_trigger,
walled_handoff, template_handoff, early_wall_guard, early_wall_followup, delegated_defense, mixed_guard_maze,
guard_geometry, guard_roster); 27 opponents. None of them was used to choose g1 (opp_key5, HANDOFF, GROWERS,
GUARDED_MAZE). best_v9e and best_v9f are left out because their results against these three bots are known (17.11,
18.1). Standard start, both seats, so 54 conditions per candidate; the engine is deterministic, so only the opponent
and the seat vary. Runs: fresh5a (V29, g1; JOBS=1, after ho1g1) and fresh5b (g0; JOBS=2, after fam2b).
Hypothesis H18.3: g1's mean score (W 1, D 0.5, L 0) on these 54 conditions is at least V29's. It is falsified if the
paired g1 - V29 score difference has a 95% cluster-bootstrap interval (over opponents) entirely below 0. Secondary,
descriptive: g0 scores below g1 on the lead's bots and hrt-w1's fortresses (the early-poke and lock families of
17.12).

### 18.4 (2026-10-31T19:17:45Z) Pre-statement: V29, g1 and g0 on six of the lead's gate pools (gate1; no result seen)

Opponents experiments/economy/opp_gate1.txt (written 19:18Z from experiments/lead/pools.py): f5t (38), TARGETED2
(24), TARGETED3_P5TF (15), BLUFFCOV (8), TIMING (16) and STRIKE1 (20), 105 distinct specs (pool membership in
opp_gate1_pools.json); standard start, both seats, 630 matches; run gate1 (scratch/chain26.sh, after fresh5b, JOBS=2).
Purpose: one table of this lane's three standard-start bots on the pools the lead uses for best_v9e and af2g, so the
complementary-strength statement can be made per pool. Some f5t opponents are in opp_key5, which was used to choose
g1, so f5t is not held-out evidence for g1. Prediction (H18.4, descriptive, no decision depends on it): g1 wins at
most as many conditions as V29 on f5t, TIMING and STRIKE1 and at least as many on TARGETED2, TARGETED3_P5TF and
BLUFFCOV.

### 18.5 (2026-10-31T19:24:50Z) Observation on TIMING2 and pre-statement of a final-flood test on best_v9e (fl1; no fl1 result seen)

Observation (fam2b, done 19:19:08Z; details in 18.7): V29, g1 and g0 each win all 40 TIMING2 games (hrt-w3's
budget_timing, tier1 to tier4, attack rounds 2 to 6, half budget; standard start, both seats). The lead's runs on the
same 40 conditions: best_v9e's twin V18FT (runs/lead/tm2) 0-34-6, af2g (g13tm2) 0-34-6, V33C (x33tm2) 0-32-8. The
result rows show the economic difference: in runs/lead/tm2 the V18FT side ends with 1450-1541 factories and
spends 0 or 6500-7150 gold on tier5 (at most 11 copies), while budget_timing ends with 3146-3258 factories; in the
first fam2b row V29 ends with 13717 factories, spends 27300 on tier5 (42 copies) and wins 780:120 at round 50
against budget_timing with 3087 factories and 28 splashes. Conjecture: budget_timing's map stays below the lock
(per-copy splash < 1500) against both bots, and the draws come from best_v9e's small late attacks, not from a locked
opponent map.
Test fl1 (stated before any fl1 game): experiments/economy/endflood.py (shift 1; sha256 6165fb58...) wraps a base bot
and, from round flood_round on, keeps the base's wall and turret purchases, drops its other purchases and spends the
remaining gold on tier5 (at most 1000 per round). Candidates: frozen best_v9e (experiments/lead/frozen/best_v9e.py,
sha256 70ef8eab..., control) and endflood(best_v9e) with flood_round 40, 45 and 48, on TIMING2
(experiments/economy/opp_timing2.txt), standard start, both seats, KEEP=all, 160 games.
Hypothesis H18.5: for at least one flood_round, endflood(best_v9e) wins at least 17 of the 34 conditions best_v9e
draws and loses no condition that best_v9e wins or draws. If it holds, the same wrapper goes to a regression on the
other gate pools (f5t first; a flood that drops factory purchases from round 40 could cost games against late
attackers), and the result goes to the lead as evidence, not as an installation request (the lead's R13 is fixed).

### 18.6 (2026-10-31T19:29:45Z) Log diagnosis of TIMING2: the decisive window closes at round 20 (refutes the 18.5 conjecture; revised fl1 prediction stated before any endflood game)

Method: for every kept log, the per-copy splash S of budget_timing's route in each per-round snapshot (route from
gamekit.route with the snapshot's buildings as blocked cells, S from gamekit.splash_total with the engine's balanced
rules), and the rounds in which budget_timing lost HP. Scripts are lane scratch, not part of the published tree.

- runs/lead/tm2 (the lead's kept logs, the best_v9e twin V18FT against budget_timing, 40 games): budget_timing never
  loses HP. Its S first reaches 1500 in round 20 in all 40 games and is 1510 in every snapshot from round 20 to
  round 50. Before that it is below the lock; in one log (tier1, attack_round 3, seat 0) S is 280 in round 10, 1240 in
  round 12, 1390 in round 14 and 1450 in rounds 16 and 18. The twin's own losses (12, 20 and 26 HP, six games) all
  happen in rounds 2 and 3, from budget_timing's first attack.
- runs/economy/fam2b (V29, g1 and g0 against budget_timing, 120 games, all won): every HP loss of budget_timing
  happens in rounds 6 to 19. In 52 games budget_timing's base is destroyed in rounds 14 to 19; in the other 68 its S
  reaches 1500 in round 20 and it loses no HP afterwards (the games end at round 50 with the margin from rounds 6 to
  19). The largest S of the previous round's snapshot at which a hit landed is 1420. Example (first row, V29, seat 0):
  hits of 120 in round 9 (S 0) and 560 in round 13 (S 760); 42 tier5 copies bought in rounds 13 to 18 deal nothing
  after round 13.

The 18.5 conjecture (budget_timing stays below the lock) is false: its final map is locked (S = 1510 >= 1500) in all
40 tm2 games, so by Propositions 4 and 5 no tier1 to tier5 copy reaches its base from round 20 on, whatever the
opponent buys. The TIMING2 draws are decided before round 20: the twin lands no hit in rounds 6 to 19, while V29, g1
and g0 land every hit in that window. Revised conjecture: on TIMING2 only damage dealt before round 20 counts, and a
late flood cannot convert any draw.
Revised test (replaces fl1, stated before any endflood game): fl1b = endflood(best_v9e) with flood_round 40 on the 40
TIMING2 conditions, KEEP=all, run after fresh5a with JOBS=1 (lane scratch chain27; gate1 runs after fresh5b in
chain26d, not in chain26 as 18.4 says). Prediction: it wins none of the 40 conditions and its HP margins equal the twin's in tm2
(the wrapper keeps every wall and turret purchase of the base, so its defense is the same until round 40 and at least
as strong after). H18.5 is therefore predicted false. The control and flood rounds 45 and 48 are dropped: the engine is
deterministic, the lead's tm2 holds the twin's 40 games, and a later flood meets the same S = 1510 map.
Consequence for the lead (evidence only, no request): a best_v9e variant can only gain on TIMING2 by damage in rounds 6
to 19, against a map whose S rises from below 300 to 1450 in that window.

### 18.7 (2026-10-31T19:30:33Z) Result: V29, g1 and g0 on the lead's TIMING2, STAGED, SCREENED and PUNISH pools (fam2b)

Run fam2b (done 19:19:08Z): experiments/economy/opp_fam2.txt, 137 specs (pool membership in opp_fam2_pools.json:
TIMING2 20, STAGED 70, SCREENED 30, PUNISH 17), standard start, both seats, 274 games per bot. None of these
opponents was used to choose g1 or g0. Outcomes from the engine's winner field; clip = mean HP margin clipped to
[-800, 800]; worst = smallest raw margin.

| pool | V29 | g1 | g0 |
| --- | --- | --- | --- |
| PUNISH | 34-0-0 (34), clip +734, worst 47 | 32-0-2 (34), clip +744, worst -5 | 32-0-2 (34), clip +745, worst -5 |
| SCREENED | 24-0-36 (60), clip -236, worst -1690 | 54-4-2 (60), clip +696, worst -45 | 58-2-0 (60), clip +575, worst -8 |
| STAGED | 64-0-76 (140), clip -115, worst -1586 | 136-4-0 (140), clip +761, worst -19 | 138-2-0 (140), clip +743, worst -174 |
| TIMING2 | 40-0-0 (40), clip +677, worst 320 | 40-0-0 (40), clip +604, worst 394 | 40-0-0 (40), clip +690, worst 365 |
| ALL | 162-0-112 (274), clip +79, worst -1690 | 262-8-4 (274), clip +722, worst -45 | 268-4-2 (274), clip +699, worst -174 |

- All three bots: 0 bot errors, 0 rejected actions, largest decide call 3.69 s (V29), 2.27 s (g1), 1.64 s (g0);
  games last 9 to 50 rounds. Every condition has the same outcome in both seats for all three bots.
- PUNISH: the only non-wins of g1 and g0 are against counter_astra28, lost by 5 HP at round 50 in both seats; V29
  beats it by 47 in both seats.
- The lead's results on the same pools (runs/lead, read only; same pool sizes, standard start, both seats): TIMING2
  V18FT (best_v9e twin, tm2) 0-34-6, af2g (g13tm2) 0-34-6, V33C (x33tm2) 0-32-8, v28 and v30 0-24-16; STAGED V18FT
  114-0-26 (st1), V33C 140-0-0; SCREENED best_v9e 50-0-10 (bse_sg), V33C 60-0-0; PUNISH 34-0-0 for every lead version.
- Reading (descriptive): on these held-out pools g1 is far above V29 (262-8-4 against 162-0-112), so the attack hold
  of g1 (attack_from=7) is not specific to the families it was chosen on. Against the lead's bots, g1 and g0 are
  ahead on TIMING2 (40 wins against at most 0; mechanism in 18.6) and behind V33C on PUNISH, SCREENED and STAGED
  by 2 to 6 non-wins per pool. Against the installed best_v9e (or its twin) they are also ahead on STAGED
  (136 and 138 wins against 114) and SCREENED (54 and 58 against 50). No paired interval is given because the
  lead's runs are separate files; the counts are exact for these deterministic conditions.

### 18.8 (2026-10-31T19:31:21Z) Result: g1 on the development set ho1 (ho1g1)

Run ho1g1: g1 on the 288 ho1 conditions of ho1v29 (17.7; the 12 ho1 scenarios, both seats). Its 24 bots.best games
played the file with sha256 70ef8eab... (best_v9e), the same file as in ho1v29. Paired by (opponent, scenario, seat)
with experiments/economy/pair_diff.py: g1 and V29 have the same HP margin and the same number of rounds in all 288
games, so the same record, 268-1-19, clip +675. g1: 0 bot errors, 0 rejected actions, largest decide call 5.20 s.
Reading: on the 12 ho1 scenarios (all non-standard starts) the attack hold attack_from=7 never changes the margin or the
length of a game of V29, so ho1 gives no evidence for or against g1 beyond V29's own record. Conjectured reason (not checked in the
code or logs): V29 already buys no attack before round 11 on a foreign map (foreign_attack_from=11), which contains
the hold of attack_from=7 whenever the scenario map counts as foreign.

### 18.9 (2026-10-31T19:33:06Z) Corrections to Entry 18 from an external audit (Astra, tag e18audit), each checked against the cited lines

Astra was asked to check every claim of Entry 18 against entries 1 to 17.15. It reports 119 claim occurrences as
supported and 12 problems. I checked each problem against the cited text (and, for items 11 and 12, against the
results file and the opponent source). All 12 are accepted; the corrected statements replace those of Entry 18.

1. Lemma 1 corollary: the route has at most 108 cells, so its length (steps) is at most 107 (entry 2; entry 7 counts
   L + 1 route cells). Entry 18 wrote "at most 107 cells".
2. Proposition G needs all of its hypotheses: a fixed defender map (nothing built between the purchase and the
   round's combat) with route length L, per-copy splash S and total gun damage G (sum of gun damage per tick); an
   active roster of N entries of one tier with HP h > S. Then arrivals in that round are at least
   A(N) - floor(250 G / (h - S)), with A(N) the number of k < N with (k mod 250) <= 249 - L. Entry 18 left out the
   fixed-map and one-tier conditions and did not define A(N) and G.
3. The "769 tier5 for 30800 simulated damage" example (fortress v28, round-24 map of w1v29c asym:24:3 seat 0,
   offense.search with cap 3000 and 500,000 gold) is a simulation result (fastsim), not a proved consequence. It
   belongs under empirical findings.
4. Route lemma: a new splash on an empty cell c not on the route raises S by exactly 10 times the number of route
   cells other than the base at Chebyshev distance 1 from c (17.6). Entry 18 dropped "other than the base".
5. Finding 1: the phi=1 defence defended against every attack family of bots/economy/threat.py that the opponent's
   visible gold could buy, a heuristic cover, not every possible purchase (entry 1). 46-0-6 stands.
6. Finding 2 and the recommendation: on the standard start E20, V25RM and V29 lose to best_v9e by 10 and g0, g5 and
   g6 by 15, both seats; the round-1 guard variants do not lose: V29 + r1_guard=60 wins by 5 and g0 + r1_guard=30
   draws (17.11, both seats). "Every frozen economy bot loses" is true only for the bots without r1_guard. The
   recommendation is unchanged: the two guard variants lose on opp_key5 (40-4-46 and score -0.089 against V29, 17.12).
7. Finding 3: the foreign hold of v17 holds the ordinary attack and the open-case attack until round 11; the
   finishing attack (a kill this round) and the round-1 poke are not held (entry 8).
8. Finding 3: by the engine's winner field (erratum of entry 12) scen16 is 89-2-17 and scen17 103-4-1, so the hold
   took the 108 conditions from 89-2-17 to 103-4-1, not from 89-0-19 to 107-0-1.
9. Finding 5: the -5185 results are V25RM in run bv9e, V27 in ho1v27 and V29 in ho1v29 (17.11 table), all on the 12
   ho1 scenarios.
10. Rejected ideas, r1_guard: the +5 against best_v9e is in 17.11 (vbest2), not 17.12.
11. Open failure cases: "all 72 losses end in rounds 8-12" was not stated before Entry 18. Checked now in
    runs/economy/gmaze1/results.jsonl (V29 rows, engine winner): the 72 losses end in round 8 (8), 9 (52), 10 (8),
    11 (2) and 12 (2), so the statement is true.
12. Uncertainty: before Entry 18 the wall-clock qualification was stated for fortress v25 to v33. Checked now in the
    frozen sources: v34 and v35 (and v36 to v43, which are opponents in opp_fresh5, 18.3) have the same gun-pass
    deadline (plan.py, TIME_BUDGET = 3.0 s, checked with time.time()), so every match against them is one sample of
    a load-dependent opponent. A static scan of import closures (lane scratch clockdeps.py: imports, literal
    import_module names and literal module strings inside bot_research; dynamic names not followed) finds a clock
    read in the closure of 21 of the 27 opp_fresh5 opponents (the four lead bots through fortress v15/v26 planners,
    the eight fortresses, 9 of the 15 counters; none in budget_handoff, triggered_budget_handoff,
    guarded_round4_trigger, walled_handoff, template_handoff, mixed_guard_maze), 12 of the 17 opp_heldout3
    opponents (none in eco6_t5, lead_best_a, lead_best_b, econ v2 late6 phi0, lead v4), 44 of the 105 opp_gate1
    opponents and none of the 137 opp_fam2 opponents. A clock read in the closure only means the play may depend
    on load; whether each bot disables the cutoff was not checked. V29's closure also contains the v15 and v26
    planners, but every plan_defense call of econ29 passes time_budget=plan_time (default 1e6 s) and replan_layout
    is called without time_budget (default None, no cutoff), so V29's cutoffs are off.

### 18.10 (2026-10-31T19:35:12Z) Addendum to 18.6: attack spending in the TIMING2 window (logs, no new matches)

Minion gold spent per game in rounds 2 to 12 and 2 to 19 against budget_timing (accepted buy_minion actions in the
kept logs; min / median / max over the 40 games of each bot):

| bot (run) | rounds 2-12 | rounds 2-19 |
| --- | --- | --- |
| best_v9e twin V18FT (runs/lead/tm2) | 30 / 520 / 1520 | 100 / 7540 / 7540 |
| V29 (fam2b) | 1945 / 3770 / 6240 | 9620 / 15230 / 29380 |
| g1 (fam2b) | 2470 / 5850 / 7800 | 11050 / 16900 / 42640 |
| g0 (fam2b) | 1430 / 4590 / 6600 | 10400 / 21320 / 35490 |

In the traced tm2 log (tier1, attack_round 3, seat 0) the twin buys one tier3 in round 6 and then 1, 1, 2, 3 and 4
tier5 in rounds 11 to 15, buys 40 factories in every round from 11 on and holds 35,369 gold at round 20; none of its
copies reaches the base. Reading (descriptive, this pool only): in rounds 2 to 12, while budget_timing's map is still
far from the lock (S 280 in round 10 and 1240 in round 12 in the traced tm2 log), the twin spends about a seventh of
what V29 spends on attacks (medians 520 and 3770), and its tier5 in rounds 11 to 15 meet a map of S 1240 to 1450 plus
guns in groups of at most 4. Whether a larger early attack would cost best_v9e elsewhere is not measured here.

### 18.11 (2026-10-31T19:57:00Z) Pre-statement: g1 on held-out sets 3 and 4 (hs34g1; no result seen)

Run hs34g1 (lane scratch chain28, after fl1b, JOBS=1): g1 against experiments/economy/opp_heldout3.txt (17 opponents,
no bots.best) on the 12 scenarios of held-out sets 3 and 4 (mirror:51:2 asym:52:2 mirror:53:3 asym:54:3 asym:55:2
mirror:56:3 mirror:61:2 asym:62:2 mirror:63:3 asym:64:3 asym:65:2 mirror:66:3), both seats, 408 games, paired with
V29's games in runs hs3 and hs4 by (opponent, scenario, seat). Purpose: test the conjecture of 18.8 outside ho1.
Prediction: g1 has the same HP margin and number of rounds as V29 in every game, except possibly games against
opponents with a clock read in their import closure (18.9 item 12), where load can change the opponent's play.
The conjecture is refuted if any game against one of the five opponents without one (eco6_t5, lead_best_a,
lead_best_b, econ v2 late6 phi0, lead v4; 120 games) differs. (Edited at 19:58:09Z before any hs34g1 game, to name
these five.)

### 18.12 (2026-10-31T20:24:30Z) Result: V29, g1 and g0 on 27 fresh standard-start opponents (fresh5a, fresh5b; H18.3)

Runs fresh5a (V29, g1; done 20:22:24Z) and fresh5b (g0; done 19:35:02Z): experiments/economy/opp_fresh5.txt (18.3),
standard start, both seats, 54 games per bot; families in opp_fresh5_pools.json (LEAD = af2g, V33M, P4TNUB, P5TNUBM;
W1_FORTRESS = fortress v36 to v43; W3_COUNTERS = the 15 hrt-w3 counters). Every condition has the same outcome in
both seats for all three bots. 0 bot errors and 0 rejected actions; largest decide call 3.67 s (V29), 4.57 s (g1),
5.59 s (g0).

| family | V29 | g1 | g0 |
| --- | --- | --- | --- |
| LEAD | 2-0-6 (8), clip -2, worst -10 | 2-0-6 (8), clip +5, worst -10 | 0-0-8 (8), clip -15, worst -15 |
| W1_FORTRESS | 4-0-12 (16), clip +16, worst -5 | 14-0-2 (16), clip +60, worst -17 | 0-0-16 (16), clip -10, worst -10 |
| W3_COUNTERS | 14-0-16 (30), clip -12, worst -886 | 26-0-4 (30), clip +512, worst -5 | 24-0-6 (30), clip +494, worst -8 |
| ALL | 20-0-34 (54), clip -2, worst -886 | 42-0-12 (54), clip +303, worst -17 | 24-0-30 (54), clip +269, worst -15 |

Paired differences (lane scratch pboot.py, cluster bootstrap over the 27 opponents; score W 1, D 0.5, L 0):
- g1 - V29: score +0.407 [+0.148, +0.630], clip +305.2 [+113.2, +528.4]. H18.3 (g1's mean score at least V29's,
  falsified only by an interval entirely below 0) is not falsified; the interval is entirely above 0.
- g0 - g1: score -0.333 [-0.519, -0.148], clip -33.7 [-53.0, -15.2].
- g0 - V29: score +0.074 [-0.185, +0.333], clip +271.5 [+83.7, +489.9].
Secondary prediction of 18.3 (g0 below g1 on the lead's bots and hrt-w1's fortresses): holds, 0 against 2 wins on
LEAD and 0 against 14 on W1_FORTRESS. g0 loses every one of these 24 games by 10 or 15 at round 50.

Per opponent (margin in both seats, all games of 50 rounds unless stated):
- af2g beats all three (-10, -10, -15). V33M loses to V29 (+16) and g1 (+50) and beats g0 (-15). v28 and v30 beat
  all three (-8, -10, -15).
- Fortresses: V29 beats v36 and v37 (+81) and loses to v38 to v43 (-5); g1 beats v36 (+61), v38 and v39 (+107) and
  v40 to v43 (+55) and loses to v37 (-17).
- Counters: V29 loses to hp_handoff, forecast_handoff and delegated_defense (-658, round 10), early_heavy_handoff
  (-718, round 9), mixed_guard_maze (-886, round 10), early_guard_handoff (-596) and early_wall_guard and
  early_wall_followup (-45); g1 wins all eight. g1 and g0 lose to guard_geometry and guard_roster (-5), which V29
  beats (+42, +12). g0 also loses to early_wall_followup (-8).
Caveat: 21 of the 27 opponents have a clock read in their import closure (18.9 item 12), so each of these results is
one sample; the six counters without one (budget_handoff, triggered_budget_handoff, guarded_round4_trigger,
walled_handoff, template_handoff, mixed_guard_maze) are beaten by all three bots.
Reading: this is the second held-out standard-start set (after fam2b, 18.7) on which g1 is clearly above V29; the
cost of attack_from=7 here is two guard counters lost by 5 and one fortress lost by 17. Against af2g, the lead's
remaining candidate, g1 loses by 10 in both seats, the same margin as against best_v9e (17.15).

### 18.13 (2026-10-31T20:38:30Z) Result: final flood on best_v9e against TIMING2 (fl1b; H18.5 false as predicted in 18.6)

Run: runs/economy/fl1b, endflood(best_v9e) with flood_round 40, the 40 TIMING2 conditions (budget_timing, tier1 to
tier4, attack_round 2 to 6, both seats), JOBS=1, KEEP=all. No bot errors, no rejected actions, largest decide call
1.17 s.
- Outcome: 0-34-6. The six losses are tier1 with attack_round 2 (-20), tier2 with attack_round 2 (-12) and tier3 with
  attack_round 3 (-26), each in both seats; every game lasts 50 rounds.
- Pairing with the twin V18FT in runs/lead/tm2 (suffix foreign_target="econ20"), keyed by opponent spec and seat: all
  40 pairs have the same winner, the same HP margin and the same number of rounds.
- The flood happens: 643 to 720 tier5 copies per game (median 643) are bought in rounds 40 to 50, of which 370 to 428
  in round 40. In rounds 1 to 39 the candidate's accepted actions (op, type and cell, per round) are identical to the
  twin's in all 40 pairs; these include 0 to 11 tier5 copies in rounds 11 to 17. The candidate lands 0 hits and deals 0
  damage in all 40 games.
- budget_timing's final map has S = 1510 and route length 67 in all 40 games (lane scratch bothS.py on the kept logs).
Both parts of the 18.6 prediction hold: no condition is won, and the margins equal the twin's. H18.5 (a final flood
converts TIMING2 draws) is false on these 40 conditions. This agrees with the 18.6 reading that only damage before
round 20 counts against budget_timing; the result does not show that a flood fails against opponents whose S stays
below 1500.

### 18.14 (2026-10-31T20:41:51Z) Pre-statement: V29, g1 and g0 against the lead's AS1C (as1c; no result seen)

The lead's AS1C (NOTES_FOR_TEAM 20:19:29Z) is best_v9e with attack_share=1.0 and catch_up_share=0.5, built on the
18.6 and 18.10 diagnosis; it wins all 40 TIMING2 conditions where best_v9e draws 34. Run as1c (lane scratch chain29,
after gate1 and after compressing the logs of fam2b, ho1g1, fresh5a, fresh5b and fl1b): V29, g1 and g0 against
experiments/economy/opp_as1c.txt (AS1C, and best_v9e as the control in the same run) on the standard start and the 12
scenarios of held-out sets 3 and 4, both seats, 156 games, JOBS=2. Both opponents have wall-clock reads in their
import closure (the fortress planners of defense v15 and v26), so each game is one sample.
Known: on the standard start V29 and g1 lose to best_v9e by 10 and g0 by 15 in both seats (runs vbest and g1chk); in
the traced g1 against af2g log (fresh5a, seat 0) the 10 come from the round-1 exchange (three tier1 against one) and
nothing lands afterwards in either direction.
Conjecture (weak; stated so that the run can refute it): on the standard start each of the three has the same
outcome and margin against AS1C as against best_v9e in both seats (reason, from the one traced af2g game only: the
margin is set in round 1 and both maps reach S >= 1500 by round 12, g1's in round 9). No prediction for the 12 scenarios. The run is evidence for the lead only; it selects
nothing in this lane.

### 18.15 (2026-10-31T20:52:33Z) Failure case of g1 in gate1 (lock out of reach on its own map), econ31 fill_own, pre-statement of its test (no econ31 game played)

as1c (18.14) is not run: chain29 was stopped at 20:49Z before it started anything (it was still waiting for gate1);
the cores go to the test below, and 18.14 stays a pre-statement without a result.

Observation (runs/economy/gate1, g1 rows complete, g0 rows still running): g1 loses to my own old
bots.economy.timing with attack_round=7 and repeat=true by -2139 (attack_frac 1.0, round 36) and -1859 (attack_frac
0.5, round 40) in both seats, where V29 wins in round 7 (+468, +634). Log 00407 (g1 seat 0, frac 1.0; lane scratch
traj.py, buys.py, fillcheck.py):
- Neither side loses HP from round 8 to 35 (g1 800; timing 699, from g1's tier1 and tier3 hits in rounds 1 to 7).
  timing's map has S 1600 from round 9.
- g1's S is 40 after round 6, 380 after round 8, 840 from round 12 to the end; it buys 400 factories per round from
  round 14 and holds 1,759,566 gold in round 36. timing buys only factories in rounds 18 to 35 and 275 tier5 in round 36, which end
  the game.
- fill_plan with 10**7 gold (layout lead_v3) reaches S 1550 on g1's map after round 6, 870 after round 7 (the round-7
  gun2 and two gun3) and 840 from round 8 on, so from round 7 neither the saturation step (lock_reachable is not
  "fill" on a map that is not foreign) nor any later step can lock.
- V29 has the same failure class in the same run against econ8 (-5618, round 48) and econ9 and econ10 (-2678, round
  34): in the econ10 log (00045, seat 0) S is 1370 from round 12, V29 holds 1,526,301 gold in round 34 and econ10
  buys 279 tier5 in that round. There fill_plan never reaches 1500 from round 6 on (1400 after round 6, 1370 after
  round 8), so the change below cannot help there. g1 loses these three by 45 at round 50.

Change: bots/economy/econ31.py (frozen as bots/economy/frozen/v31 with SHA256SUMS) = econ29 + fill_own (default
false, then v29). With fill_own=true, v26's lock fill test in lock_reachable and v27's fill reservation (and so
v29's fill_threat) also apply when the own map is not foreign. g1f = g1 + fill_own=true (lane scratch g1f.spec).
g1_31 = the same econ31 spec without fill_own, a check that econ31 with the default plays as econ29.

Runs (lane scratch chain30, after gate1; all standard start, both seats, KEEP=losses):
1. smoke31: g1f and g1_31 against experiments/economy/opp_smoke31.txt (6 gate1 opponents: the two timing
   attack_round=7 repeat=true losses, timing default, timing attack_round=4 frac 1.0 repeat, econ10 and
   guard_geometry roster ["tier1"]), 24 games, JOBS=2. Development cases: they were chosen from g1's gate1 results.
2. g1fg: g1f on opp_gate1.txt (210). 3. g1ff: g1f on opp_fresh5.txt (54). 4. g1fm: g1f on opp_fam2.txt (274).
5. g1fc: g1f on opp_g1check.txt (best_v9e, GROWERS and GUARDED_MAZE, 288). JOBS=2; later runs may not finish
   before the end of the shift, and any run not finished is reported as partial.
Predictions (stated before any econ31 game):
- g1_31 has the same winner, margin and length as g1 in gate1 in all 12 smoke31 games.
- g1f wins both timing attack_round=7 repeat=true conditions in both seats. It loses to econ10 (V29's failure class
  is not addressed) or draws or wins it; no prediction on the margin.
Decision rule: g1f replaces g1 as this lane's standard-start recommendation only if, over all conditions of runs 2
to 5 that finish, its paired score difference to g1 (cluster bootstrap over opponents, 4000 resamples) has a mean
above 0 and a 95% interval not entirely below 0, and on no pool table (gate1 pools, fresh5 families, fam2 pools,
GROWERS, GUARDED_MAZE) it has more than 2 fewer wins than g1. Otherwise g1 stays and g1f is reported as evidence.
Runs 2, 4 and 5 hold opponents whose g1 results were seen (gate1 chose the change), so only run 3 is held out for
the change; 21 of its 27 opponents read the clock.

### 18.16 (2026-10-31T20:55:25Z) Pre-statement: the two gate pools this lane has not covered (pcs1, hand4; no result seen)

Of the lead's 14 R13 gate pools (846 conditions), the lane runs so far cover 838 for g1 and 802 for V29
(experiments/economy/gate_vs_base.py, which now also reads the g1f runs of 18.15). Missing: PCS (the four pool C spec
opponents C-08 to C-11, standard start, both seats; experiments/economy/opp_pcs.txt, copied from runs/lead/g13pc) for
every bot, and HANDOFF (experiments/economy/opp_handoff.txt, the same 18 specs as runs/lead/bse_hd) for V29 and g1f.
Runs (lane scratch chain31, after hs34g1, JOBS=1): pcs1 = V29, g1, g0 and g1f on PCS (32 games); hand4 = V29 and g1f on
HANDOFF (72 games). Both are descriptive table completions; neither changes the 18.15 decision rule.
Predictions: V29 on HANDOFF has V27's hand1 result in every condition (2-0-34; conjecture: on the standard start V27
and V29 play as V25RM, 17.6); g1f has g1's outcome on all 36 HANDOFF conditions (36-0-0, hand3). No prediction for PCS.

### 18.17 (2026-10-31T21:13:03Z) Pre-statement: V29, g1 and g1f on 16 fresh standard-start opponents (fresh6; no result seen)

experiments/economy/opp_fresh6.txt (fixed 2026-10-31T21:12:47Z, every spec checked to load, no game played): hrt-w1's final
fortress v44 and v45, the lead's AS1C (best_v9e with attack_share=1.0 and catch_up_share=0.5), and 13 hrt-w3 counters
written after opp_fresh5 was fixed (wall_signal_timing with 20 and 0 walls, wall_signal_delayed tier4 in round 4 and
5, wall_signal_repair, shared_prefix_selector, screened_roster_continuation screen/original and front/economy20,
screened_roster_guarded, screened_continuation_repair with fortress41 and with v29_g1 (g1 as its delegate from round
7), wall_prefix_selector, delayed_wall_guard). Most of these counters were built against best_v9e; none was used to
build or tune V29, g1 or g1f. Run fresh6 (lane scratch chain32, after chain31): V29, g1 and g1f, standard start, both
seats, 96 games, JOBS=1, KEEP=losses.
Predictions:
- H18.17a: g1's mean score is at least V29's (falsified only if the cluster-bootstrap interval over the 16
  opponents of g1 - V29 is entirely below 0).
- 18.14 conjecture, restated for this run: against AS1C, V29 and g1 lose by 10 in both seats, as against best_v9e.
- Addition to the 18.15 decision rule (stated before any econ31 game against these opponents): g1f is recommended
  over g1 only if the 18.15 rule holds and, on fresh6, the interval of its paired score difference to g1 is not
  entirely below 0.

### 18.18 (2026-10-31T21:28:09Z) Result: V29, g1 and g0 on six of the lead's gate pools (gate1; H18.4 false on two pools)

Run gate1 (done 21:25Z, 630 games, 6596 s with JOBS=2): experiments/economy/opp_gate1.txt (105 specs), standard
start, both seats. 0 bot errors and 0 rejected actions for all three; largest decide call V29 4.57 s, g1 2.78 s, g0
6.52 s. Every condition has the same outcome in both seats for all three bots. Table (lane scratch pooltab.py with
experiments/economy/opp_gate1_pools.json; a spec in two pools counts in both, ALL counts each game once):

| pool | games | V29 | g1 | g0 |
| --- | ---: | --- | --- | --- |
| f5t | 76 | 52-8-16 | 54-2-20 | 48-2-26 |
| TARGETED2 | 48 | 48-0-0 | 34-4-10 | 32-4-12 |
| TARGETED3_P5TF | 30 | 22-2-6 | 26-0-4 | 24-0-6 |
| BLUFFCOV | 16 | 16-0-0 | 16-0-0 | 16-0-0 |
| TIMING | 32 | 26-6-0 | 26-0-6 | 24-0-8 |
| STRIKE1 | 40 | 36-0-4 | 16-2-22 | 6-12-22 |
| ALL | 210 | 172-12-26 | 144-8-58 | 124-18-68 |

Paired score differences (W 1, D 0.5, L 0; cluster bootstrap over the 105 opponent specs, 4000 resamples):
g1 - V29 -0.143 [-0.238, -0.048] overall; per pool STRIKE1 -0.475 [-0.750, -0.175], TARGETED2 -0.250 [-0.417,
-0.104], TIMING -0.094 [-0.250, +0.031], f5t -0.013 [-0.118, +0.105], TARGETED3_P5TF +0.100 [-0.167, +0.400].
g1 - g0 +0.071 [+0.024, +0.124] overall.
H18.4 (g1 wins at most as many conditions as V29 on f5t, TIMING and STRIKE1, at least as many on TARGETED2,
TARGETED3_P5TF and BLUFFCOV) is false on f5t (54 against 52 wins) and on TARGETED2 (34 against 48); it holds on the
other four pools.
Where g1 loses and V29 wins: STRIKE1, economy.timing with attack_round 4 or 5 (-25 to -145 at round 50) and the two
attack_round=7 repeat=true floods (-2139 at round 36, -1859 at round 40; 18.15); TARGETED2, guard_geometry and
guard_roster with one tier1 or tier2 (-5, -12 at round 50). These are lock-versus-lock games decided by the early
exchange: with attack_from=7, g1 makes no attack in rounds 2 to 6, so the margin V29 takes from those rounds is not
taken (conjecture from the margins; the logs of these games were not traced, except the round-7 flood in 18.15).

Against best_v9e condition by condition (experiments/economy/gate_vs_base.py; best_v9e's rows are the lead's base
files of the R13 gate; gate1 plus the earlier lane runs fam2b, g1chk, grow1, gmaze1, hand3; PCS is not covered yet,
HANDOFF not for V29):

| bot | conditions | bot W-D-L | best_v9e W-D-L | bot worse | bot better |
| --- | ---: | --- | --- | ---: | ---: |
| g1 | 838 | 756-16-66 | 522-76-240 | 72 | 298 |
| V29 | 802 | 574-18-210 | 510-76-216 | 140 | 202 |
| g0 | 838 | 740-22-76 | 522-76-240 | 84 | 292 |

Per pool for g1 (worse/better than best_v9e): TIMING 6/14, TIMING2 0/40, STRIKE1 18/0, TARGETED2 10/16, f5t 22/2,
PUNISH 2/0, BLUFFCOV 0/0, TARGETED3_P5TF 4/12, HANDOFF 0/24, SCREENED 6/10, GROWERS 0/76, GUARDED_MAZE 0/78, STAGED 4/26.
g1's 72 worse conditions are the early-exchange games above, the two round-7 floods, small margins against older
economy bots (econ8, econ9, econ10 -45; econ13, econ15, econ21 -17), guard_geometry at (9,1) with
foreign_attack_from null (-37), fortress v20 and counter_astra28 (-5), all at round 50, and five growth_rounds=8
screened or staged guard mazes (10 conditions) that end in round 10 with both bases destroyed (draws, -19) or g1
behind by 45, where best_v9e wins by 1033 to 1163 in round 13. Reading: no bot of the
four dominates on this gate; best_v9e and V29 keep the early exchange, g1 and g0 keep the growers. GROWERS,
GUARDED_MAZE and HANDOFF informed the choice of g1 (17.14), and f5t shares opponents with opp_key5, so the g1 rows
of those pools are not held-out evidence.

### 18.19 (2026-10-31T21:33:24Z) Results: hs34g1 (18.11 prediction holds) and smoke31 (18.15 predictions: one holds, one fails in part)

hs34g1 (runs/economy/hs34g1, 408 games, g1 against held-out sets 3 and 4, standard start, both seats): paired by
(opponent, scenario, seat) with V29's rows in runs/economy/hs3 and hs4, all 408 games have the same winner, HP margin
and number of rounds. The 18.11 prediction (g1 = V29 in every game) holds, including the 120 games against eco6_t5,
lead_best_a, lead_best_b, econ v2 late6 phi0 and lead v4. On these 17 opponents attack_from=7 changes nothing; the
held-out evidence for g1 against V29 therefore comes from fresh5 (18.12) and the coming fresh6, not from hs3/hs4.

smoke31 (runs/economy/smoke31, 24 games, development cases, standard start, both seats):
- g1_31 (econ31 with fill_own at its default false) has the same winner, margin and length as g1 in gate1 in all 12
  games. The prediction holds; econ31 with the default plays as econ29 on these 12 conditions.
- g1f (fill_own=true), per condition (both seats give the same result in every pair):

| opponent (gate1 condition) | V29 | g1 | g1f |
| --- | --- | --- | --- |
| timing attack_round=7 frac 1.0 repeat | W +468 r7 | L -2139 r36 | L -39 r50 |
| timing attack_round=7 frac 0.5 repeat | W +634 r7 | L -1859 r40 | W +101 r50 |
| timing default | W +117 r50 | L -140 r50 | L -140 r50 |
| timing attack_round=4 frac 1.0 repeat | W +36 r50 | L -75 r50 | L -75 r50 |
| econ10 | L -2678 r34 | L -45 r50 | L -24 r50 |
| guard_geometry roster ["tier1"] | W +42 r50 | L -5 r50 | L -10 r50 |

- The prediction "g1f wins both timing attack_round=7 repeat=true conditions in both seats" fails for frac 1.0: g1f
  loses by 39 instead of 2139. Log 00001 (g1f seat 0; lane scratch traj.py): g1f has S 430 after round 7 and 1610
  from round 8 to the end, so the lock now holds; but timing's two tier5 in round 7 take 140 HP (800 to 660) before
  it, and timing has S 1600 from round 9 with 699 HP. Both maps are immune from round 9 and the game ends 660 to 699.
  The fill turns a -2139 loss into a -39 loss, not a win. With frac 0.5 timing sends one tier5 in round 7, which deals
  no damage (log 00003: g1f keeps 800 HP, the same S trajectory), and g1f wins 800 to 699, by
  101. The econ10 prediction (lose, draw or win) holds: it loses by 24. guard_geometry tier1 is 5 HP worse (-10 vs -5).
- 0 errors and 0 rejected actions. Max decide call: g1f 0.61 s, g1_31 1.84 s.
These are development cases chosen from g1's gate1 losses; they show that fill_own acts where intended, not that g1f
is better. The 18.15 decision rule on runs 2 to 5 and the 18.17 condition on fresh6 decide.

### 18.20 (2026-10-31T21:35:43Z) Pre-statement: best_v9e on the fresh5 and fresh6 opponents (bvf; no result seen)

The lead will not gate another candidate before the end (NOTES_FOR_TEAM 21:28:53Z), so the report compares this
lane's bots with best_v9e, the entry point, only through tables. On the R13 gate pools g1 has more wins than best_v9e
(18.18), but g1 was chosen after seeing several of those pools. The fresh5 and fresh6 opponents are the held-out sets
of this lane; best_v9e has not been run against them by this lane. Run bvf (lane scratch chain34, after chain33):
best_v9e (bot_research.experiments.lead.frozen.best_v9e:@make) against experiments/economy/opp_fresh56.txt (opp_fresh5
followed by opp_fresh6, 43 opponents), standard start, both seats, 86 games, JOBS=1, KEEP=losses. g1's rows come from
fresh5a (seen) and fresh6 (not yet seen when this is written).
Prediction: H18.20: g1's mean score on the 43 opponents is at least best_v9e's (falsified only if the
cluster-bootstrap interval of g1 - best_v9e over the opponents is entirely below 0).
Bias stated before the games: most hrt-w3 counters in both sets were built against best_v9e, so the W3 family favors
g1 by construction. The table therefore also reports the 15 opponents that were not built against either bot (the
lead's af2g, V33M, P4TNUB, P5TNUBM and AS1C; hrt-w1's fortress v36 to v45), with no prediction for that subset.
Head to head, best_v9e beats g1 by 10 in both seats (17.15).

### 18.21 (2026-10-31T21:45:50Z) g1f fails the 18.15 rule on f5t; no purchase or turret signal in rounds 1 to 6 separates the strikers from the growers (logs, no new matches)

g1f (partial g1fg, 79 of 210 gate1 conditions paired with g1's gate1 rows when this was written): 35 W for both, 20
L for both, 22 W to L and 2 D to L, none better in outcome. The W to L conditions include fortress v7, v11, v15, v19 and
v21 (g1 +107 to +495 at round 50, g1f -15 to -51), best_v3b (+159 to -107), lead v4 and v4proto (+107 and +145 to
-15), and the economy15 leak continuations (+1103 and +2903 to -27 and -34). On f5t g1f has at most 34 wins of 76
against g1's 54 (gate_vs_base.py), so the 18.15 condition "no pool table with more than 2 fewer wins than g1" already
fails and g1f is not recommended, whatever the remaining runs show. The traced gain (18.19) is real but much smaller
than the cost; the cost was not traced.

Question: could an observation rule give g1's attack hold against the growers and V29's early attacks against the
opponents where V29 beats g1 (STRIKE1, TARGETED2)? 18.2 rejected "attack early only after the opponent buys a minion".
Two more signals were read from the kept logs (gate1, all 630 logs; fam2b; gmaze1 and grow1 for V29 and g1chk for g1;
lane scratch quietq.py and oppturret.py; the loser's log of each condition where V29 and g1 differ):
- First minion bought by the opponent from round 2 on (q). Where V29 wins and g1 loses: STRIKE1 q = 4 (8 conditions),
  5 (10), none by round 6 (4); TARGETED2 none (14). Where V29 loses and g1 wins: SCREENED none (30), STAGED none (56)
  or 6 (16), GUARDED_MAZE 2 (50), 6 (10) or none (12). A rule "attack early while the opponent buys no minion" would
  therefore play V29 against about 120 grower conditions that V29 loses, to win at most about 40 strike conditions.
- First round with an opponent turret. Where V29 loses and g1 wins: GUARDED_MAZE round 4 (36) or 5 (36), SCREENED 4
  (30), STAGED 3 (2), 4 (44) or 5 (26). Where V29 wins and g1 loses: STRIKE1 round 5 (8), 6 (10) or none (4), TARGETED2
  round 1 (10). The growers and the strikers both show their first turret in rounds 4 to 6.
Conclusion (empirical, these pools): neither signal separates the two families before round 4, so I implement no
reactive hold. The remaining knob is the length of the hold itself (18.22).

### 18.22 (2026-10-31T21:45:50Z) Pre-statement: attack-hold sweep attack_from 6 and 5 on the conditions where V29 and g1 differ (afs6, afs5; no result seen)

af6 = V29 + attack_from=6 and af5 = V29 + attack_from=5 (lane scratch af6.spec, af5.spec; g1 is attack_from=7, V29
attack_from=2). attack_from=7 came from g0 (17.10) and was never varied. Opponents experiments/economy/opp_afsweep.txt
(fixed before any game of af5 or af6): the 127 gate-pool specs on which V29 and g1 have different outcomes in some
seat (STAGED 38, GUARDED_MAZE 36, SCREENED 17, STRIKE1 14, f5t 7, TARGETED2 7, TARGETED3_P5TF 5, TIMING 1, PUNISH 1,
GROWERS 1) and the 18 HANDOFF specs; standard start, both seats, 290 games per candidate. Runs afs6 then afs5 (lane
scratch chain35, JOBS=2, after g1fg; g1fm and g1fc are dropped, g1ff runs last if time allows). These conditions were
seen for V29 and g1 (development evidence); the conditions where V29 and g1 agree are not run.
Predictions:
- H18.22 (monotone trade): per pool, wins are monotone in attack_from over 5, 6, 7: on STRIKE1, TARGETED2 and f5t
  af5 >= af6 >= g1; on GUARDED_MAZE, SCREENED, STAGED and HANDOFF af5 <= af6 <= g1. Falsified on a pool if one of
  these inequalities fails by more than 2 conditions.
- Decision rule: a value is named as a possible replacement of g1 only if it has more wins than g1 on the 290
  conditions and on no pool more than 2 fewer wins than g1. Such a value then runs on opp_fresh56 (86 games, held
  out) if it can finish before 00:30Z, and is recommended over g1 only if its paired score difference to g1 there has
  a cluster-bootstrap interval not entirely below 0. Because the agreeing conditions are not run, even then the
  evidence is partial and is reported as such.

### 18.23 (2026-10-31T21:51:39Z) Results: pcs1 and hand4 (18.16: the V29 prediction holds, the g1f prediction fails on one spec)

pcs1 (runs/economy/pcs1, 32 games, the four PCS specs, standard start, both seats; 0 errors, 0 rejected actions,
largest call 1.95 s). Both seats give the same margin and length in every pair. Margin and end round:

| PCS opponent | V29 | g1 | g0 | g1f |
| --- | --- | --- | --- | --- |
| budget_timing tier3, attack round 4, fraction 0.65 | +814 r15 | +814 r15 | +1234 r16 | +114 r50 |
| budget_timing tier4, attack round 6, fraction 0.65 | +280 r50 | +280 r50 | +420 r50 | +280 r50 |
| guard_geometry roster ["tier1"] at (9, 2) | +3397 r22 | +975 r15 | +5455 r21 | +4610 r21 |
| guard_geometry roster ["tier2"] at (10, 2) | +9250 r25 | +26028 r26 | +34988 r26 | +1084 r23 |

All four bots win all 8 PCS conditions; best_v9e has 2-6-0 there (runs/lead/g13pc: draws against both budget_timing
specs and guard_geometry tier1, and wins by 5 against guard_geometry tier2, whose row in the lead's summary table is
0-0-4, -5 from the counter's side; gate_vs_base.py counts 2-6-0 on the 8 conditions).

hand4 (runs/economy/hand4, 72 games, the 18 HANDOFF specs, standard start, both seats; 0 errors, 0 rejected actions,
largest call 2.18 s):
- V29 has V27's hand1 winner, margin and length in all 36 conditions (2-0-34). The prediction holds; it is consistent
  with the conjecture that V27 and V29 play as V25RM on the standard start (17.6).
- g1f 34-0-2. The prediction (g1's outcome on all 36) fails on guard_handoff growth_rounds=5 handoff_round=10 (g1f
  -57 at round 50 in both seats; g1 +301). The other 34 conditions are wins with other margins (g1f +83 to +1263, g1
  +301 to +1133).

With pcs1 and hand4 every bot of the 18.18 table now has all 846 conditions of the 14 R13 pools
(experiments/economy/gate_vs_base.py, exact spec match, best_v9e from the lead's base files):

| bot | W-D-L of 846 | best_v9e on the same 846 | worse than best_v9e | better |
| --- | --- | --- | ---: | ---: |
| V29 | 584-18-244 | 524-82-240 | 150 | 208 |
| g1 | 764-16-66 | 524-82-240 | 72 | 304 |
| g0 | 748-22-76 | 524-82-240 | 84 | 298 |

Four of the 14 pools were seen when g1 and g0 were chosen (GROWERS, GUARDED_MAZE and HANDOFF directly, f5t through its
overlap with opp_key5), so on those 398 conditions the table is selection evidence. On the other ten pools (PCS,
TIMING, TIMING2, STRIKE1, TARGETED2, PUNISH, BLUFFCOV, TARGETED3_P5TF, SCREENED, STAGED; 448 conditions, all run
after g1 was fixed at 17:53Z) the counts from the per-pool tables are: g1 388-14-46, V29 318-8-122, best_v9e 310-76-62.
For comparison, the lead's AS1C on the whole gate: 604-26-216 (NOTES_FOR_TEAM 21:28:53Z, the lead's count).

### 18.24 (2026-10-31T22:04:31Z) Result: g1fg complete (g1f on the 210 gate1 conditions; descriptive, g1f already rejected in 18.21)

g1fg (runs/economy/g1fg, 210 games, the 105 opp_gate1 specs, standard start, both seats; 0 errors, 0 rejected
actions, largest call 2.84 s). Paired with g1 and V29 from gate1 on the same 210 conditions (scratch pooltab.py,
cluster bootstrap over opponent specs, 4000 resamples, seed 1; score W 1, D 0.5, L 0):

| pool (lowercase as in opp_gate1_pools.json) | conditions | g1f | g1 | V29 | g1f - g1 [95% interval] |
| --- | ---: | --- | --- | --- | --- |
| bluffcov | 16 | 16-0-0 | 16-0-0 | 16-0-0 | +0.000 [+0.000, +0.000] |
| f5t | 76 | 32-0-44 | 54-2-20 | 52-8-16 | -0.303 [-0.447, -0.158] |
| strike1 | 40 | 14-2-24 | 16-2-22 | 36-0-4 | -0.050 [-0.200, +0.100] |
| targeted2 | 48 | 24-4-20 | 34-4-10 | 48-0-0 | -0.208 [-0.375, -0.042] |
| targeted3_p5tf | 30 | 14-0-16 | 26-0-4 | 22-2-6 | -0.400 [-0.667, -0.133] |
| timing | 32 | 24-0-8 | 26-0-6 | 26-6-0 | -0.062 [-0.188, +0.000] |
| all | 210 | 98-6-106 | 144-8-58 | 172-12-26 | -0.224 [-0.310, -0.143] |

The complete run confirms the 18.21 rejection. g1f is worse than g1 on 50 of the 210 conditions and better on 2 (both
seats of timing attack_round=7 attack_frac=0.5 repeat=true, +101 r50 against -1859 r40, the smoke31 case). Three
pools have intervals entirely below 0 (f5t, targeted2, targeted3_p5tf). I have not traced why fill_own loses these
conditions; no mechanism is claimed. g1ff (g1f on opp_fresh5) stays last in chain35 and is descriptive only.

### 18.25 (2026-10-31T22:29:26Z) Result: afs6 (af6 = V29 + attack_from=6); H18.22 false on SCREENED and STAGED; af6 qualifies under the 18.22 rule; g1ff dropped

afs6 (runs/economy/afs6, done 22:25:00Z, 290 games, the 145 opp_afsweep specs, standard start, both seats; 0 errors,
0 rejected actions, largest call 5.21 s). Paired with g1 and V29 on the same conditions (pooltab.py; g1 and V29 rows
from gate1, fam2b, grow1, gmaze1, g1chk, hand3 and hand4; pools of opp_afsweep_pools.json):

| pool | conditions | af6 | g1 | V29 | af6 - g1 [95% interval] |
| --- | ---: | --- | --- | --- | --- |
| GROWERS | 2 | 2-0-0 | 2-0-0 | 0-2-0 | |
| GUARDED_MAZE | 72 | 72-0-0 | 72-0-0 | 0-0-72 | +0.000 [+0.000, +0.000] |
| HANDOFF | 36 | 36-0-0 | 36-0-0 | 2-0-34 | +0.000 [+0.000, +0.000] |
| PUNISH | 2 | 0-0-2 | 0-0-2 | 2-0-0 | |
| SCREENED | 34 | 34-0-0 | 30-4-0 | 0-0-34 | +0.059 [+0.000, +0.147] |
| STAGED | 76 | 76-0-0 | 72-4-0 | 0-0-76 | +0.026 [+0.000, +0.066] |
| f5t | 14 | 4-0-10 | 6-0-8 | 4-6-4 | -0.143 [-0.429, +0.000] |
| strike1 | 28 | 8-0-20 | 4-2-22 | 24-0-4 | +0.107 [-0.143, +0.357] |
| targeted2 | 14 | 0-4-10 | 0-4-10 | 14-0-0 | +0.000 [+0.000, +0.000] |
| targeted3_p5tf | 10 | 6-0-4 | 6-0-4 | 2-2-6 | +0.000 [+0.000, +0.000] |
| timing | 2 | 0-0-2 | 0-0-2 | 0-2-0 | |
| all | 290 | 238-4-48 | 228-14-48 | 48-12-230 | +0.017 [-0.014, +0.048] |

af6 has g1's winner, margin and length in 158 of the 290 games and V29's in none. Its outcome differs from g1's on 18
conditions (9 opponents, both seats each):
- better: screened_guard_maze and staged_guard_maze with growth_rounds=8 (four specs; W +1055 or +1081 at round 11
  against g1's draws at -19 in round 10); economy.timing attack_round=6 pre_defend (W +72 against D 0); the two
  economy.timing attack_round=7 repeat=true floods (W +227 at round 50 against -1859 and -2139; V29 wins them in round 7).
- worse: guard_continuation economy15 (L -37 against W +2903 in round 21) and economy.timing attack_round=5
  pre_defend (L -70 against W +350).
H18.22 for af6 against g1: holds on STRIKE1 (8 against 4 wins), TARGETED2 (0 and 0), GUARDED_MAZE and HANDOFF
(equal); on f5t af6 has 2 fewer wins (4 against 6), which is within the stated tolerance of 2; false on SCREENED and
STAGED, where af6 has 4 more wins than g1 instead of at most as many. So wins are not monotone in attack_from on the
grower pools: one round less of hold wins the four growth_rounds=8 mazes that g1 draws. The af5 half of H18.22
follows when afs5 is done.
Decision rule of 18.22: af6 has more wins than g1 on the 290 conditions (238 against 228) and no pool with more than
2 fewer wins (worst f5t, 2 fewer), so af6 qualifies to run on opp_fresh56. Two additions, stated before afs5 is done:
- If af5 also qualifies, the value with more wins on the 290 goes to opp_fresh56; on a tie, af6. This is implemented
  in experiments/economy/dec22.py, written before its first run. Its first run (22:28Z, a test) printed af5's first
  50 of 290 games, so the af5 partial counts were seen before afs5 finished; the rule did not change.
- To fit the fresh56 run before 00:30Z, g1ff (g1f on opp_fresh5, descriptive) is dropped. Lane scratch chain36
  replaces the rest of chain35: after afs5 it runs dec22.py and then the chosen value on opp_fresh56 (run afq56, 86
  games, JOBS=2). Recommended over g1 only if the paired score difference to g1 on those 43 opponents (g1 rows from
  fresh5a and fresh6) has a cluster-bootstrap interval not entirely below 0; the evidence stays partial because the
  gate conditions on which V29 and g1 have the same outcome in both seats were not run for af6 or af5.

### 18.26 (2026-10-31T22:47:11Z) Result: afs5 (af5 = V29 + attack_from=5); the 18.22 rule selects af5; pre-statement of afg5 (af5 on the rest of the gate; no afg5 result seen)

afs5 (runs/economy/afs5, done about 22:43Z, 290 games, the same 145 specs; 0 errors, 0 rejected actions, largest call
3.77 s). Wins per pool, af5 / af6 / g1 / V29 (pooltab.py, same sources as 18.25):

| pool | conditions | af5 | af6 | g1 | V29 |
| --- | ---: | --- | --- | --- | --- |
| GROWERS | 2 | 2-0-0 | 2-0-0 | 2-0-0 | 0-2-0 |
| GUARDED_MAZE | 72 | 70-0-2 | 72-0-0 | 72-0-0 | 0-0-72 |
| HANDOFF | 36 | 36-0-0 | 36-0-0 | 36-0-0 | 2-0-34 |
| PUNISH | 2 | 2-0-0 | 0-0-2 | 0-0-2 | 2-0-0 |
| SCREENED | 34 | 34-0-0 | 34-0-0 | 30-4-0 | 0-0-34 |
| STAGED | 76 | 74-0-2 | 76-0-0 | 72-4-0 | 0-0-76 |
| f5t | 14 | 12-0-2 | 4-0-10 | 6-0-8 | 4-6-4 |
| strike1 | 28 | 12-0-16 | 8-0-20 | 4-2-22 | 24-0-4 |
| targeted2 | 14 | 14-0-0 | 0-4-10 | 0-4-10 | 14-0-0 |
| targeted3_p5tf | 10 | 6-0-4 | 6-0-4 | 6-0-4 | 2-2-6 |
| timing | 2 | 2-0-0 | 0-0-2 | 0-0-2 | 0-2-0 |
| all | 290 | 264-0-26 | 238-4-48 | 228-14-48 | 48-12-230 |

Paired score differences (cluster bootstrap over the 145 specs): af5 - g1 +0.100 [+0.038, +0.159]; af5 - af6 +0.083
[+0.028, +0.138]; af5 - V29 +0.724 [+0.628, +0.810]. Per pool, af5 - g1: targeted2 +0.857 [+0.714, +1.000], f5t +0.429
[+0.143, +0.857], strike1 +0.250 [-0.036, +0.536], GUARDED_MAZE -0.028 [-0.083, +0.000], the others within
[-0.066, +0.147]. af5 has g1's winner, margin and length in 14 games and V29's in 6; its outcome equals g1's in 238 of
the 290 conditions and V29's in 38.
af5's 26 non-wins (all losses, both seats of each spec): eight economy.timing specs of STRIKE1 with attack_round 4 or
5 (-25 to -79 at round 50; V29 wins seven of them and g1 one) and timing default in f5t (-74; V29 +117); in
TARGETED3_P5TF guard_geometry tier1 at (9, 1) with foreign_attack_from null (-13; V29 +2105 in round 21) and
guarded_adaptive_continuation with two tier1 (-39; g1 +801 in round 13); guarded_maze cash_rank_1 growth 6 guard 5
with a tier2 bait (-676 in round 10; g1 +788) and staged_guard_maze lead_opening growth 7 (-570 in round 10; g1
+1164). The last two are grower losses of V29's kind (V29 -723 and -1279 in rounds 8 and 9), smaller and later.

H18.22 (monotone trade over attack_from 5, 6, 7), full verdict: the af5 >= af6 >= g1 chains hold on STRIKE1 (12, 8, 4)
and TARGETED2 (14, 0, 0) and hold within the tolerance of 2 on f5t (12, 4, 6); the af5 <= af6 <= g1 chains hold on
GUARDED_MAZE (70, 72, 72) and HANDOFF (36, 36, 36) and fail on SCREENED (34, 34, 30) and STAGED (74, 76, 72), both
through af6 > g1 (18.25). H18.22 is false on two of seven pools. On TARGETED2 the change is a step, not a slope: af6
wins none of the 14, af5 all 14.
Decision rule (18.22 with the 18.25 tie-break): both qualify (af5 264 and af6 238 wins against g1's 228; af5's worst
pool is GUARDED_MAZE with 2 fewer wins than g1, within the tolerance); af5 has more wins, so dec22.py chose af5
(runs/economy/dec22.out, 22:43:35Z) and chain36 started afq56 = af5 on opp_fresh56 (86 games, JOBS=2). The 18.22
condition for recommending af5 over g1 (the afq56 interval of af5 - g1 not entirely below 0) is still open.

Pre-statement of afg5 (stated before any afg5 game): the 290 sweep conditions were chosen because V29 and g1 differ
on them, so af5 has not been seen on the rest of the R13 gate. experiments/economy/opp_afagree.txt (fixed 22:46Z):
the 257 gate specs not in opp_afsweep.txt (V29 and g1 have the same outcome in both seats on each), ordered TIMING2,
PCS, BLUFFCOV, TIMING, STRIKE1, TARGETED2, TARGETED3_P5TF, PUNISH, SCREENED, STAGED, GUARDED_MAZE, GROWERS, f5t; run
afg5 = af5 on it, standard start, both seats, 514 games, JOBS=2 (lane scratch chain37, after afq56). If it is not
done by 00:30Z it is stopped and reported as partial.
- Prediction: af5 has the outcome that V29 and g1 share on at least 95% of the 514 conditions (at most 25 differ).
- Added condition for the recommendation, stated now: af5 is recommended over g1 only if, in addition to the 18.22
  afq56 condition, on the gate conditions that afs5 and afg5 cover, af5 has on no R13 pool more than 2 fewer wins than
  g1 (gate_vs_base.py per-pool counts, with afs5 and afg5 added to RUNS). If afg5 is partial, the recommendation is
  stated as conditional on the covered part.

### 18.27 (2026-10-31T22:53:29Z) Result: fresh6 (V29, g1 and g1f on 16 fresh standard-start opponents; H18.17a not falsified)

fresh6 (runs/economy/fresh6, 96 games, standard start, both seats, done about 22:52Z; 0 errors, 0 rejected actions).
Each of the three bots has the same outcome, margin and length in both seats against every one of the 16 opponents.
Per family (experiments/economy/opp_fresh6_pools.json; pooltab.py):

| family | conditions | g1 | V29 | g1f |
| --- | ---: | --- | --- | --- |
| LEAD (AS1C) | 2 | 0-0-2 | 0-0-2 | 0-0-2 |
| W1_FORTRESS (v44, v45) | 4 | 4-0-0 | 0-0-4 | 0-0-4 |
| W3_COUNTERS | 26 | 24-0-2 | 22-2-2 | 22-0-4 |
| all | 32 | 28-0-4 | 22-2-8 | 22-0-10 |

- H18.17a: g1 - V29 +0.156 [-0.031, +0.375] (cluster bootstrap over the 16 opponents); the interval is not entirely
  below 0, so H18.17a is not falsified. W3_COUNTERS alone: +0.038 [-0.115, +0.231].
- 18.14 conjecture: against AS1C, V29 and g1 both lose by 10 at round 50 in both seats, as against best_v9e. It holds
  on this run. g1f loses by 25.
- Where g1 and V29 differ: g1 beats hrt-w1's fortress v44 and v45 (+55 at round 50; V29 -5) and wall_prefix_selector
  (+28; V29 -45), and loses to delayed_wall_guard (-5; V29 draws). All three are round-50 margins under 200.
- g1f: g1f - g1 -0.188 [-0.375, +0.000]. The 18.17 addition for g1f is moot because g1f had already failed the 18.15
  rule (18.21). Descriptively, g1f loses to v44 and v45 (-15), wall_prefix_selector (-170), delayed_wall_guard (-5)
  and AS1C (-25).
- Largest single decide call: g1 18.73 s (against v44); V29 12.38 s; g1f 12.73 s.
Conditions: 16 opponents, one list, so the intervals describe this list only. Most of the 13 W3 counters were built
against best_v9e (hrt-w3, lead 22:14Z note). v44 and v45 give the same outcome, margin and length against each of
the three bots.

### 18.28 (2026-10-31T22:54:24Z) Pre-statement: af5 against the ten bots of the lead's round robin frr1 (afrr; no result seen)

The lead's frr1 (runs/lead/frr1, standard start, both seats; NOTES_FOR_TEAM 22:14Z, report 5.16) plays ten bots
against each other; g1 went 6-0-12 and V29 4-0-14 in it. In frr1, g1 and V29 lose by 8 to 10 at round 50 to
best_v9e, best_v9f, best_v9f passive_until=null, the lead's v30 and AS1C; g1 beats v41 (+55), guard00 (+28) and
threat_defender, V29 loses to v41 (-5) and guard00 (-45); V29 beats g1 by 17. experiments/economy/opp_frr1.txt (fixed
22:54Z) lists the ten frr1 specs, including V29 and g1. Run afrr = af5 against them, standard start, both seats, 20
games, JOBS=1 (lane scratch chain38, after bvf). af5 itself is not a frr1 bot, so this adds one row and one column to
frr1 and does not change the lead's matrix.
Predictions:
- H18.28a: af5 loses to best_v9e, best_v9f, best_v9f passive_until=null, v30 and AS1C by 5 to 20 at round 50 in both
  seats (the round-1 exchange of finding 2; af5 differs from g1 only in attack_from, which allows attacks from round
  5 instead of round 7).
- H18.28b: af5 beats threat_defender in both seats.
- No prediction against v41, guard00, V29 and g1.

### 18.29 (2026-10-31T23:07:48Z) Result: afq56 (af5 on the 43 fresh5 and fresh6 opponents); the 18.22 condition holds

afq56 (runs/economy/afq56, 86 games, standard start, both seats, 22:43:35Z to 23:03:28Z; 0 errors, 0 rejected
actions, largest decide call 11.15 s). g1 and V29 rows from fresh5a and fresh6. No af5 game against these opponents
was seen before af5 was chosen (18.26). Per family (opp_fresh56_pools.json, pooltab.py):

| family | conditions | af5 | g1 | V29 |
| --- | ---: | --- | --- | --- |
| LEAD | 10 | 4-0-6 | 2-0-8 | 2-0-8 |
| W1_FORTRESS | 20 | 20-0-0 | 18-0-2 | 4-0-16 |
| W3_COUNTERS | 56 | 54-0-2 | 50-0-6 | 36-2-18 |
| all | 86 | 78-0-8 | 70-0-16 | 42-2-42 |
| NOT_BUILT_AGAINST (LEAD + W1_FORTRESS) | 30 | 24-0-6 | 20-0-10 | 6-0-24 |

af5 - g1 +0.093 [+0.023, +0.186] over the 43 opponents (NOT_BUILT_AGAINST +0.133 [+0.000, +0.333]); af5 - V29
+0.407 [+0.256, +0.558]. af5 has one outcome per opponent in both seats. It has g1's outcome on 78 of the 86
conditions and is better on the other 8, in both seats each: guard_geometry and guard_roster with default parameters
(W +1705 and +2825 in round 21; g1 -5 at round 50, V29 +42 and +12), hrt-w1's fortress v37 (+69; g1 -17) and the
lead's af2g = best_v9f passive_until=null (+410 at round 50; g1 and V29 -10). af5 loses to AS1C, v28 (P4TNUB) and v30
(P5TNUBM) by 10 at round 50, like g1, and to delayed_wall_guard by 5 (V29 draws).
The 18.22 condition for recommending af5 over g1 (the interval of af5 - g1 on fresh56 not entirely below 0) holds.
The 18.26 gate condition (afg5, running since 23:03:37Z) is still open.

Correction to the protocol of 18.28 (written before afq56 finished): opp_frr1 contains af2g, v30, AS1C and hrt-w1's
v41, which are also in opp_fresh56, so afq56 has already played those four afrr opponents on the same start (af5
beats v41 by 55 at round 50). H18.28a is therefore refuted for af2g before afrr runs (af5 wins by 410), and its parts
for v30 and AS1C are already observed (af5 loses by 10). Only best_v9e and best_v9f with default parameters are new tests of H18.28a. If afrr gives another
result on a repeated condition, that is reported as a load-dependent difference.

### 18.30 (2026-10-31T23:22:27Z) Result: bvf (best_v9e on the 43 fresh5 and fresh6 opponents; H18.20 not falsified)

bvf (runs/economy/bvf, 86 games, standard start, both seats, done about 23:20Z; 0 errors, 0 rejected actions,
largest decide call 6.46 s). best_v9e has one outcome per opponent in both seats. g1 and V29 rows from fresh5a and
fresh6, af5 rows from afq56 (18.29). Per family (opp_fresh56_pools.json, pooltab.py):

| family | conditions | g1 | best_v9e | af5 | V29 |
| --- | ---: | --- | --- | --- | --- |
| LEAD | 10 | 2-0-8 | 0-8-2 | 4-0-6 | 2-0-8 |
| W1_FORTRESS | 20 | 18-0-2 | 20-0-0 | 20-0-0 | 4-0-16 |
| W3_COUNTERS | 56 | 50-0-6 | 36-4-16 | 54-0-2 | 36-2-18 |
| all | 86 | 70-0-16 | 56-12-18 | 78-0-8 | 42-2-42 |
| NOT_BUILT_AGAINST (LEAD + W1_FORTRESS) | 30 | 20-0-10 | 20-8-2 | 24-0-6 | 6-0-24 |

- H18.20: g1 - best_v9e +0.093 [-0.070, +0.256] over the 43 opponents; the interval is not entirely below 0, so H18.20
  is not falsified. The interval also contains 0, so this run does not show that g1 is better either.
- The bias stated in 18.20 shows in the split: on W3_COUNTERS g1 - best_v9e +0.214 [+0.000, +0.429]; on the 15
  opponents built against neither bot -0.133 [-0.300, +0.033]. There best_v9e draws the lead's af2g, V33M, P4TNUB and
  P5TNUBM (0 at round 50) and loses only to AS1C (-60), while g1 loses to AS1C, af2g, P4TNUB and P5TNUBM by 10 and
  beats V33M by 50; best_v9e beats all ten fortresses, g1 loses to v37 (-17).
- af5 (no prediction was stated for it on bvf, descriptive): af5 - best_v9e +0.186 [+0.058, +0.326] over the 43
  opponents, +0.000 [-0.133, +0.133] on the 15 built against neither. af5 beats af2g (+410), V33M (+16) and v37 (+69)
  and loses to AS1C, P4TNUB and P5TNUBM by 10.
- best_v9e's 18 losses: AS1C (-60) and eight W3 counters (early_wall_followup, early_wall_guard and wall_prefix_selector
  -30; screened_continuation_repair fortress41 and screened_roster_guarded -26; forecast_handoff, hp_handoff and
  mixed_guard_maze -235), each in both seats. g1 and af5 win against all eight of those W3 counters.
- Head to head on the standard start best_v9e beats g1 by 10 in both seats (17.15, frr1); af5 against best_v9e is in
  afrr (18.28).

### 18.31 (2026-10-31T23:24:04Z) Pre-statement: af5 on scenario starts (scnaf5) and the hold values 4 and 3 (afs4, afs3); no result seen

1. scnaf5. On every scenario start tested, g1 played V29's game (18.8, 18.19), so attack_from=7 acted only on the
   standard start there. Whether attack_from=5 does the same has not been measured. Run scnaf5 (lane scratch
   chain40, after afrr, JOBS=1): af5 against experiments/economy/opp_clockfree5.txt (the five opponents of
   opp_heldout3 without a clock read in their import closure: eco6_t5, lead_best_b, lead_best_a, econ v2 late6 phi0,
   lead v4) on the 12 scenarios of held-out sets 3 and 4, both seats, 120 games, paired by (opponent, scenario, seat)
   with V29's games in hs3 and hs4.
   Prediction H18.31a: af5 has V29's winner, HP margin and number of rounds in all 120 games; refuted by one
   difference. If it is refuted, the recommendation of af5 (if any) is restricted to the standard start.
2. afs4 and afs3 (lane scratch chain39, after afg5, JOBS=2, afs4 first): V29 + attack_from=4 (af4) and =3 (af3) on
   opp_afsweep.txt, standard start, both seats, 290 games each. Purpose: sensitivity of the sweep result to the hold
   round (V29's default is attack_from=2). Prediction H18.31b: af4 and af3 each have fewer wins than af5 (264) on the
   290 conditions. No recommendation depends on afs4 or afs3: there is no time left for a held-out check of another
   value, so a value that beats af5 here is reported as development evidence only.
Stop rule: a run not finished at 00:30Z is stopped and reported as partial.

### 18.32 (2026-10-31T23:34:38Z) Result: afg5 (af5 on the rest of the R13 gate); the 18.26 prediction and safeguard hold

afg5 (runs/economy/afg5, 514 games, 257 specs of experiments/economy/opp_afagree.txt, standard start, both seats,
23:03:37Z to 23:33:35Z; 0 errors, 0 rejected actions). af5 has one outcome per spec in both seats.
- 18.26 prediction (at most 25 of the 514 differ from the outcome V29 and g1 share): 2 differ, so it holds. Both are
  the two seats of screened_guard_maze with layout empty and growth_rounds 8 (SCREENED), which af5 wins by 1169 in
  round 11 where g1 loses by 45 and V29 by 1612, both in round 10.
- With afs5 this covers all 846 gate conditions. gate_vs_base.py (afq56 and afg5 added to RUNS), wins per pool,
  af5 / g1 / V29 / best_v9e: PCS 8/8/8/2, TIMING 30/26/26/18, TIMING2 40/40/40/0, STRIKE1 24/16/36/34, TARGETED2
  48/34/48/24, f5t 60/54/52/70, PUNISH 34/32/34/34, BLUFFCOV 16/16/16/16, TARGETED3_P5TF 26/26/22/18, HANDOFF
  36/36/2/12, SCREENED 60/54/24/50, GROWERS 142/142/140/66, GUARDED_MAZE 142/144/72/66, STAGED 138/136/64/114.

| bot | W-D-L on the 846 | worse than best_v9e | better |
| --- | --- | ---: | ---: |
| best_v9e | 524-82-240 | | |
| af5 | 804-2-40 | 32 | 310 |
| g1 | 764-16-66 | 72 | 304 |
| V29 | 584-18-244 | 150 | 208 |

- Safeguard of 18.26 (af5 has on no pool more than 2 fewer wins than g1): the only pool with fewer is GUARDED_MAZE (142
  against 144), so it holds. With the 18.22 rule (18.26) and the afq56 condition (18.29) this makes af5 the
  recommended standard-start bot of this lane in place of g1, subject only to H18.31a for scenario starts.
- Where af5 is worse than best_v9e (32 conditions: 15 specs in both seats, the default economy.timing counted in
  TIMING and in f5t): the economy.timing strikers with attack
  round 4 or 5 (STRIKE1 six specs, TIMING and f5t the default; -25 to -79 at round 50 where best_v9e wins by 15 to
  560), the old economy bots econ8 (two specs), econ9 and econ10 (-21 at round 50; best_v9e +5 or +10), fortress v20
  (-5), opening_response guard_poke5 with economy13 (-12; best_v9e draws), poke_lock (draw; best_v9e +10) and
  guard_geometry tier1 at (9, 1) (-13; best_v9e +7).
- af5's other non-wins, where best_v9e also loses: economy.timing attack round 4 with frac 1.0 (two specs, -75; best_v9e
  -35), guarded_adaptive_continuation with two tier1 (-39; -10), guarded_maze cash_rank_1 growth 6 guard 5 with a tier2
  bait (-676 in round 10; -1212 in round 9) and staged_guard_maze lead_opening growth 7 (-570 in round 10; -1200 in
  round 9).
Evidence status: the 290 sweep conditions chose af5 (development evidence); the 514 afg5 games and the 86 afq56
games were played after the choice and are held out for af5. Counted by pool, 296 of the 846 gate conditions use a
sweep spec; on the other 550 af5 went 536-2-12, g1 and V29 534-2-14 (equal by the construction of opp_afagree) and
best_v9e 358-70-122. On the afg5 specs alone af5 differs from g1 on one
spec (better). On every gate pool the specs are parameter variants of a few bots, so the per-pool counts are not
independent draws.

### 18.33 (2026-10-31T23:36:30Z) Pre-statement: afrep, a replay of af5 against best_v9e with every log kept (afrr partly seen)

Seen before this entry: 15 of the 20 afrr games (18.28), among them af5 against best_v9e in both seats, which af5 wins
by 410 at round 50, and against best_v9f in both seats (also +410). This refutes H18.28a for best_v9e and best_v9f.
afrr keeps only the logs of losses, so the mechanism is not visible, and best_v9e's import closure reads the wall
clock (scratch clockdeps.py: defense v15 plan, v26 plan and replan; the same modules appear in V29's closure), so
the result may depend on load. Run afrep (lane scratch chain41, after afrr, before scnaf5): af5 against best_v9e
alone (experiments/economy/opp_bv9e.txt), standard start, both seats, 2 games, JOBS=1, KEEP=all.
Prediction H18.33: both games repeat afrr's result (af5 wins by 410 at round 50). If either differs, the af5 result
against best_v9e is reported as load-dependent. The log is used to name the rounds in which the HP difference arises.

### 18.34 (2026-10-31T23:41:09Z) Result: afrr and afrep; af5 beats best_v9e and best_v9f by 410 in both seats (H18.28a false, H18.33 holds)

afrr (runs/economy/afrr, 20 games, standard start, both seats, 23:20:24Z to about 23:37Z; 0 errors, 0 rejected
actions, largest decide call of af5 0.8 s) and afrep (runs/economy/afrep, 2 games, every log kept, 23:37:34Z to
23:39:18Z). af5 has one outcome per opponent in both seats:

| opponent (frr1 name) | af5 | g1 in frr1 | V29 in frr1 |
| --- | --- | --- | --- |
| best_v9e | W +410 | L -10 | L -10 |
| best_v9f | W +410 | L -10 | L -10 |
| af2g (best_v9f passive_until=null) | W +410 | L -10 | L -10 |
| P5TNUBM (v30) | L -10 | L -10 | L -8 |
| AS1C | L -10 | L -10 | L -10 |
| v41 | W +55 | W +55 | L -5 |
| guard00 | W +2 | W +28 | L -45 |
| V29 | W +7 | L -17 | |
| g1 | W +31 | | W +17 |
| threat_defender | W +800 (round 11) | W (round 9) | W (round 11) |

All margins are at round 50 except threat_defender. af5 goes 16-0-4 against the ten frr1 bots; in frr1 the best
record is guard00's 16-0-2 against nine. af5 is not part of the lead's frr1 matrix, so no statement about its
max-min mixtures is made here.
- H18.28a (af5 loses to best_v9e, best_v9f, af2g, v30 and AS1C by 5 to 20) is false for best_v9e, best_v9f and af2g
  and holds for v30 and AS1C. H18.28b (af5 beats threat_defender) holds.
- H18.33: afrep repeats afrr's result in both seats; the seat-0 log of afrep equals the seat-0 log of afrr in every
  event, HP and gold value of all 102 lines, so the result did not change between the two runs (started 23:20:24Z and 23:37:34Z).
- What the logs show (seat 0, afrr game 9; compared with the lead's frr1 log of g1 against best_v9e, game 12): both
  bots play the same first four rounds and lose round 1 by 10 (785 against 795). In round 5 af5 buys a tier3
  (attack_from=5 allows it), where g1 buys only factories. best_v9e's own round-5 purchases are the same in both games;
  from round 6 on they differ (against af5: a gun3, a gun1 and two tier1 in round 6; against g1: four splash and one
  tier1). af5 then buys a tier5 in round 9 and two in round 10; three reach best_v9e's base (140 in round 9, 280 in
  round 10), and no HP changes after round 10 (785 against 375). g1 buys a tier4 in rounds 7 and 8, and none reaches.
  Why best_v9e's map lets the tier5s through in rounds 9 and 10 is not measured here (no splash count per route
  cell was computed); that the round-5 tier3 is what changes best_v9e's play is a conjecture from the two logs.
Conditions: one start (standard), one engine, deterministic up to the clock reads in both bots' import closures
(scratch clockdeps.py lists defense v15 plan and v26 plan and replan for best_v9e and for V29's family). Ten
opponents only; the gate and fresh tables (18.32, 18.29) are the broader evidence.

### 18.35 (2026-10-31T23:50:32Z) Result: scnaf5 (af5 on scenario starts); H18.31a holds

Run: runs/economy/scnaf5 (lane scratch chain41, after afrep, JOBS=1; chain40, which was to run it, was stopped
before it started any game; same command), 23:39:18Z to 23:47:49Z, 120 games, 0 errors, 0 rejected actions, largest
decide call 1.70 s. Paired with V29's rows of hs3 and hs4 by (opponent, scenario, seat): 120 of 120 paired, 0 differ
in winner, HP difference or number of rounds (scratch scnchk.py). H18.31a holds, so the 18.31 restriction does not
apply.
- af5 113-0-7, equal to V29 game by game. All 7 losses are against eco6_t5: asym:54:3 seat 1 (-560, round 12),
  mirror:61:2 both seats (-710, round 12), mirror:63:3 both seats (-143, round 15), asym:64:3 seat 1 (-1176, round 10)
  and asym:65:2 seat 1 (-588, round 12). The other four opponents lose all 24 of their games.
- With 18.8 and 18.19 (g1 equal to V29 on ho1 and on held-out sets 3 and 4), attack_from=5 and attack_from=7 changed
  no game on the scenario starts tested. A possible reason, not checked game by game, is the separate hold of econ18+
  on maps with buildings the bot did not request (no attack, finish or doom purchase before foreign_attack_from=11).
Conditions: five opponents of opp_heldout3 (those without a clock read in their import closure), the 12 scenarios of
held-out sets 3 and 4, both seats. The clock-reading opponents of those sets and the other scenario sets were not
run with af5.

### 18.36 (2026-10-31T23:53:43Z) Result: afs4 (af4 = V29 + attack_from=4 on the 290 sweep conditions); H18.31b holds for af4

Run: runs/economy/afs4 (lane scratch chain39, JOBS=2), 23:33:49Z to about 23:52:23Z (1114.1 s), 290 games, 0 errors,
0 rejected actions, largest decide call 2.31 s; each opponent spec has the same winner and margin in both seats.
chain39 was stopped after it started afs4, and afs3 runs in chain42 with JOBS=3 (started 23:52:24Z), so that it can
finish before the 00:30Z stop; the job count changes the load on the box, which can matter only for opponents whose
import closure reads the clock (18.9 item 12).
Wins per pool on the 290 conditions (g1 rows from gate1, fam2b, g1chk and hand3; V29 from 18.26; scratch afs43.py):

| bot | W-D-L | GROWERS | GUARDED_MAZE | HANDOFF | PUNISH | SCREENED | STAGED | f5t | strike1 | targeted2 | targeted3_p5tf | timing |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| V29 (attack_from=2) | 48-12-230 | 0 | 0 | 2 | 2 | 0 | 0 | 4 | 24 | 14 | 2 | 0 |
| af4 | 162-2-126 | 2 | 20 | 12 | 2 | 20 | 50 | 12 | 22 | 14 | 6 | 2 |
| af5 | 264-0-26 | 2 | 70 | 36 | 2 | 34 | 74 | 12 | 12 | 14 | 6 | 2 |
| af6 | 238-4-48 | 2 | 72 | 36 | 0 | 34 | 76 | 4 | 8 | 0 | 6 | 0 |
| g1 (attack_from=7) | 228-14-48 | 2 | 72 | 36 | 0 | 30 | 72 | 6 | 4 | 0 | 6 | 0 |

- H18.31b holds for af4: 162 wins against af5's 264. af4 - af5 = -0.348 [-0.441, -0.252] (pooltab.py, cluster
  bootstrap over the 145 opponent specs); af4 is better than af5 on 16 conditions and worse on 118.
- af4 wins more strike1 conditions than af5 (22 against 12; af4 - af5 +0.357 [+0.143, +0.643] over 14 specs, V29
  24) and loses most of af5's growth-first wins (GUARDED_MAZE 20 against 70, HANDOFF 12 against 36, SCREENED 20
  against 34, STAGED 50 against 74).
- Over attack_from = 2, 4, 5, 6, 7 the strike1 wins are 24, 22, 12, 8, 4 and the GUARDED_MAZE wins 0, 20, 70, 72,
  72; the total peaks at 5 among the five values (48, 162, 264, 238, 228).
Conditions: development evidence only (the 290 conditions were chosen because V29 and g1 differ on them; standard
start, both seats); no held-out check of af4, and no recommendation depends on it (18.31).

### 18.37 (2026-11-01T00:05:45Z) Result: afs3 (af3 = V29 + attack_from=3 on the 290 sweep conditions); H18.31b holds

Run: runs/economy/afs3 (lane scratch chain42, JOBS=3), 23:52:24Z to 00:04:36Z (732.0 s), 290 games, 0 errors, 0
rejected actions, largest decide call 1.92 s; each opponent spec has the same winner and margin in both seats.
Wins per pool on the 290 conditions (rows of 18.36 for the other values; scratch afs43.py):

| bot | W-D-L | GROWERS | GUARDED_MAZE | HANDOFF | PUNISH | SCREENED | STAGED | f5t | strike1 | targeted2 | targeted3_p5tf | timing |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| af3 | 146-0-144 | 2 | 14 | 18 | 2 | 22 | 30 | 12 | 24 | 14 | 6 | 2 |
| af4 | 162-2-126 | 2 | 20 | 12 | 2 | 20 | 50 | 12 | 22 | 14 | 6 | 2 |
| af5 | 264-0-26 | 2 | 70 | 36 | 2 | 34 | 74 | 12 | 12 | 14 | 6 | 2 |

- H18.31b holds for both values: af3 146 and af4 162 wins against af5's 264. af3 - af5 = -0.407 [-0.503, -0.303]
  and af3 - af4 = -0.059 [-0.134, +0.017] (pooltab.py, cluster bootstrap over the 145 specs); af3 is better than af5
  on 18 conditions and worse on 136.
- On strike1 af3 has V29's 24 wins (af3 - af5 +0.429 [+0.071, +0.714]). Over attack_from = 2 (V29), 3, 4, 5, 6, 7
  (g1) the strike1 wins are 24, 24, 22, 12, 8, 4 and the GUARDED_MAZE wins 0, 14, 20, 70, 72, 72; HANDOFF (2, 18, 12,
  36, 36, 36) and SCREENED (0, 22, 20, 34, 34, 30) are not monotone. The total is largest at attack_from=5 (48, 146,
  162, 264, 238, 228).
Conditions: development evidence only, as in 18.36; no held-out check of af3, and no recommendation depends on it.
Storage: the match logs of afs3, afs4, afs5, afs6 and afg5 were compressed with gzip at 23:55Z and 00:05Z (names end in
.jsonl.gz; contents unchanged); runs/economy is now about 2.2 GB.

## Entry 19 (2026-11-01T00:06:35Z): final summary of this lane's results for the report; af5 for the standard start

This entry supersedes Entry 18 as the summary of this lane for the report. It only collects results stated in
entries 1 to 18.37; each item names the entry with the exact conditions. All matches were played with the lead's
harness (bot_research.harness.tournament) on the unchanged engine with the balanced rules, both seats, on cores 25
to 27 at low priority. Selection evidence and held-out evidence are named separately in each item.

### Artifacts (paths relative to bot_research/)

- Bots: bots/economy/econ*.py (development copies) and bots/economy/frozen/<tag>/ for v2 to v31, each with
  SHA256SUMS; frozen files were never edited after freezing. Tools: bots/economy/fastsim.py (one map's combat, equal
  to td_game.combat.simulate_map on 450 random maps and rosters), guarantee.py (Theorem B), offense.py, threat.py,
  defense_plan.py, fillplan.py (lock fill, 17.3), econ31.py (fill_own, 18.15).
- Candidate specs: experiments/economy/specs/*.spec with a README naming each (E20, V25RM, V29, g1, g0, g1f, af6, af5;
  af4 and af3 for sensitivity only). best_v9e is bot_research.experiments.lead.frozen.best_v9e:@make (sha256
  70ef8eab..., the file bots/best.py installs; no job of this lane imports bots/best.py).
- Opponent lists (experiments/economy/, one spec per line, fixed before the candidate games named in the entry):
  opp_key5 (17.12, tuning), opp_heldout3 (17.9), opp_fam2 (18.7, the lead's TIMING2, STAGED, SCREENED, PUNISH),
  opp_gate1 (18.4, the lead's f5t, TARGETED2, TARGETED3_P5TF, BLUFFCOV, TIMING, STRIKE1), opp_pcs and opp_handoff
  (18.16), opp_fresh5 (18.3), opp_fresh6 (18.17), opp_fresh56 (18.20), opp_afsweep (18.22), opp_frr1 (18.28, the ten
  bots of the lead's round robin frr1), opp_clockfree5 (18.31), opp_bv9e (18.33); pool or family membership in the
  matching *_pools.json.
- Evaluation scripts: experiments/economy/run_tourn.sh (the lead's harness, both seats, cores 25-27, nice 19),
  pooltab.py (per-pool W-D-L and paired cluster bootstrap), gate_vs_base.py (condition-by-condition comparison with
  best_v9e on the lead's 14 R13 gate pools), pair_diff.py, endflood.py (18.5).
- Runs: runs/economy/<name>/results.jsonl and summary.md for every run named here; match logs of losses (or all games
  where stated), several runs compressed with gzip (18.1 storage note, 18.37).

### Proved statements (exact hypotheses in the cited entries, with the 18.9 corrections)

- Proposition 1 (entry 1): a factory bought in round r returns 15(50 - r) gold over the remaining rounds, net
  15(50 - r) - 20, positive for r <= 48.
- Propositions 4 and 5, the lock (entries 1 and 2): if a player's route has per-copy splash S >= h, no copy with
  HP <= h reaches its base while it builds nothing more; with S >= 1500 (tier5 HP) its HP never decreases again.
- Lemma 1 and corollaries (entry 2, 18.9 item 1): route cells induce a linear forest; a splash deals at most 70 to one
  copy; a route has at most 108 cells (at most 107 steps).
- Theorem B (entry 2): a lower bound on a package's damage against every same-round response that the defender's
  visible gold can buy (guarantee.py, exact Fraction arithmetic; 276 checked cases, 0 violations).
- Propositions F and G (entries 7 and 15, hypotheses as restated in 18.9 item 2): on a fixed map below the lock
  (S < h) the arrivals of N copies of one tier with HP h are at least A(N) - floor(250 G / (h - S)), unbounded in N;
  no number of guns makes a map immune, only S >= h.
- Route lemma (17.6, 18.9 item 4): the engine's BFS returns the lexicographically least shortest path, so blocking
  cells off the route leaves the route unchanged, and a new splash on an empty off-route cell c raises S by exactly 10
  times the number of route cells other than the base at Chebyshev distance 1 from c.

### Main empirical findings (unchanged engine, balanced rules, both seats; exact conditions in the cited entries)

1. Growth before defence (entry 1, sweep1, 26 tuning opponents): defending only against the visible roster until
   round 6 went 52-0-0; defending against every attack family of threat.py that the opponent's visible gold could buy
   went 46-0-6.
2. The round-1 exchange decides most standard-start games against the lead's bots (17.11, 17.15, 18.1, 18.12): V29 and
   g1 lose to best_v9e and best_v9f by 10 and g0 by 15 at round 50 in both seats, and in the traced logs no HP changes
   after round 1. The round-1 purchase is chosen from the initial observation, which is the same for both players, so
   no observation rule picks a round-1 counter only against the openings it beats (entry 11, r1t2). The two round-1
   guard variants are the exception against best_v9e (V29 + r1_guard=60 wins by 5, g0 + r1_guard=30 draws) and lose on
   opp_key5 (18.9 item 6). af5 (finding 6) loses the round-1 exchange by the same 10 (785 against 795) but beats
   best_v9e, best_v9f and af2g by +410 at round 50 in both seats (18.34, afrr; afrep repeats the seat-0 game line for
   line) and V33M by +16 (afq56). In the traced game af5 buys a tier3 in round 5 where g1 buys only factories, and
   three of the tier5s it buys in rounds 9 and 10 reach best_v9e's base (140 HP in round 9, 280 in round 10); g1's
   tier4s of rounds 7 and 8 never reach it. That the earlier attack gate causes the win is a conjecture from this one
   log. af5 still loses to P4TNUB, P5TNUBM and AS1C by 10 at round 50 in both seats (afq56, afrr).
3. Scripted starts (entries 7 to 17): holding attacks until round 11 on a map with buildings the bot never requested
   took the 108 scen17 conditions from 89-2-17 to 103-4-1 (engine winner field, 18.9 item 8) with no standard-start
   change; then hrt-w1's re-planned layouts with a gain rule, raised attack caps (v24m: 41-0-11 against 34-0-18 on 52
   fortress conditions) and a lock fill with a reservation (V27, V29).
4. Held-out scenario sets 2, 3 and 4 (576 conditions, 17.9): V25RM - E20 = +43.4 [+1.3, +85.6] clipped HP, score
   +0.027 [0.000, +0.054]; V29 - V25RM on sets 3 + 4: +0.6 [-6.5, +8.2]. On every scenario start tested (ho1, 288
   games; held-out sets 3 and 4, 408 games) g1 has V29's winner, margin and length in every game (18.8, 18.19), and so
   has af5 on 120 games of held-out sets 3 and 4 (18.35), so the attack holds attack_from=7 and 5 act only on the
   standard start in these runs.
5. The attack hold attack_from=7 (g1) wins the growth-first families: HANDOFF 36-0-0 (V29 2-0-34), GROWERS 142-0-0,
   GUARDED_MAZE 144-0-0 (V29 72-0-72) (17.14, 17.15; these pools informed the choice of g1). Held out for g1: fam2b
   (18.7, the lead's TIMING2, STAGED, SCREENED, PUNISH; 274 conditions) g1 262-8-4 against V29 162-0-112; fresh5
   (18.12, 27 opponents, 54 conditions) g1 42-0-12 against V29 20-0-34, g1 - V29 score +0.407 [+0.148, +0.630];
   fresh6 (18.27, 16 opponents, 32 conditions) g1 28-0-4 against V29 22-2-8, g1 - V29 +0.156 [-0.031, +0.375].
6. The same hold loses the early-strike families (18.18, gate1, 210 conditions): V29 172-12-26, g1 144-8-58, g1 - V29
   -0.143 [-0.238, -0.048]; STRIKE1 -0.475 [-0.750, -0.175] and TARGETED2 -0.250 [-0.417, -0.104]. Where g1 loses and
   V29 wins the games are lock-versus-lock margins from rounds 2 to 6 (conjecture from the margins) and two round-7
   tier5 floods that reach a map whose lock is out of reach (18.15, log traced). Neither the opponent's first minion
   purchase nor its first turret in rounds 1 to 6 separates the strikers from the growers on these pools (18.2,
   18.21), so no reactive hold was built.
   Attack-hold sweep (18.22, 18.25, 18.26, 18.29): on the 290 gate conditions where V29 and g1 differ (development
   evidence) the earlier hold af5 = V29 + attack_from=5 went 264-0-26, af6 (attack_from=6) 238-4-48, g1 228-14-48 and
   V29 48-12-230; af5 - g1 +0.100 [+0.038, +0.159]. af5 keeps V29's TARGETED2 wins (14 of 14) and all but 4 of g1's
   grower wins (GUARDED_MAZE 70 of 72, STAGED 74 of 76, HANDOFF and SCREENED all), but still loses 16 of the 28
   STRIKE1 conditions. The trade over attack_from is not monotone on SCREENED and STAGED (H18.22 false there).
   Held out for af5 (fresh5 + fresh6, 43 opponents, 86 conditions): af5 78-0-8, g1 70-0-16, V29 42-2-42; af5 - g1
   +0.093 [+0.023, +0.186], better than g1 on 8 conditions and worse on none. On the 514 gate conditions outside
   the sweep (afg5, 18.32, also held out for af5) af5 has the outcome V29 and g1 share on 512 and wins the other 2.
7. The lead's 14 R13 gate pools (846 conditions, 18.23; gate_vs_base.py, exact spec match against the lead's base
   files for best_v9e):

   | bot | W-D-L | worse than best_v9e | better |
   | --- | --- | ---: | ---: |
   | best_v9e | 524-82-240 | | |
   | V29 | 584-18-244 | 150 | 208 |
   | g1 | 764-16-66 | 72 | 304 |
   | g0 | 748-22-76 | 84 | 298 |
   | af5 | 804-2-40 | 32 | 310 |

   On the ten pools not used to choose g1 (448 conditions, run after g1 was fixed): g1 388-14-46, V29 318-8-122,
   best_v9e 310-76-62. The lead's AS1C on the whole gate: 604-26-216. af5 (18.32) has the most wins, ties included, on
   11 of the 14 pools; it has fewer than V29 (36) and best_v9e (34) on STRIKE1 (24), fewer than best_v9e on f5t (60
   against 70) and 2 fewer than g1 on GUARDED_MAZE. No bot dominates: best_v9e wins more of f5t and STRIKE1 than af5
   and g1, V29 more of STRIKE1, and V29 loses most of the grower pools. For af5, 296 of the 846 pool conditions use
   the 145 sweep specs that chose it; on the other 550 (the 257 afg5 specs, played after the choice, all specs on
   which V29 and g1 agree) af5 went 536-2-12, g1 and V29 534-2-14 and best_v9e 358-70-122.
8. TIMING2 (hrt-w3's budget_timing, 40 conditions; 18.6, 18.10, 18.13): budget_timing's map reaches S = 1510 in round
   20 in all 40 of the lead's logs, so only damage before round 20 counts. V29, g1 and g0 win all 40 (they spend a
   median 3770 to 5850 on attacks in rounds 2 to 12, best_v9e's twin 520); a final tier5 flood on best_v9e from
   round 40 (fl1b) lands 0 hits and changes no result (0-34-6, as predicted).
9. best_v9e on the fresh5 and fresh6 opponents (18.30, 43 opponents, 86 conditions, held out for every bot here):
   g1 70-0-16, best_v9e 56-12-18, af5 78-0-8, V29 42-2-42; g1 - best_v9e +0.093 [-0.070, +0.256] (H18.20 not
   falsified, and no difference shown), af5 - best_v9e +0.186 [+0.058, +0.326]. Most W3 counters in these sets were
   built against best_v9e; on the 15 opponents built against neither bot, g1 - best_v9e is -0.133 [-0.300, +0.033]
   and af5 - best_v9e +0.000 [-0.133, +0.133]. best_v9e draws the lead's af2g, V33M, P4TNUB and P5TNUBM, where g1
   loses three of the four by 10 and af5 beats af2g (+410) and V33M (+16) and loses to P4TNUB and P5TNUBM (-10).

### Recommendation for the standard start (for the lead's decision; this lane does not touch bots/best.py)

- This lane's standard-start bot is af5 = V29 + attack_from=5 (experiments/economy/specs/af5.spec). It was chosen by
  the rule stated in 18.22 before the af5 and af6 games (dec22.py, on 290 development conditions) and then met both
  conditions stated before its held-out games: on fresh5 + fresh6 (afq56, 86 conditions) af5 - g1 is +0.093 [+0.023,
  +0.186], with no condition worse than g1; on the 514 other gate conditions (afg5) it differs from the outcome V29
  and g1 share on 2 conditions, both wins (prediction: at most 25), and no gate pool has more than 2 fewer wins than
  g1 (18.32).
- Against best_v9e: on the 846 gate conditions af5 goes 804-2-40 against best_v9e's 524-82-240, better on 310
  conditions and worse on 32 (pool memberships; on the 804 distinct conditions the lead counts af5 764-2-38, worse on
  30 and better on 288, report section 5.15); on fresh5 + fresh6 af5 - best_v9e is +0.186 [+0.058, +0.326], and +0.000
  [-0.133, +0.133] on the 15 opponents built against neither bot; head to head af5 wins by 410 at round 50 in both
  seats, and a second run repeats the seat-0 game line for line (finding 2). Against the ten bots of the lead's round
  robin frr1 af5 is 16-0-4 (afrr), and in the lead's eleven-bot matrix (frr1 plus afrr) the max-min mixtures put 1/3
  on af5, 1/3 on guard00 and 1/3 on P5TNUBM and AS1C (report section 5.16; linear programming, checked in exact
  fractions).
- Under H14's reading rule (outcome at least best_v9e's on every one of the 846 conditions, 0 rejected actions, 0
  bot errors, no call of 3 s or more) af5 is evidence, not a recommended revision. It has 0 rejected actions and 0
  bot errors, but it is worse than best_v9e on 32 conditions (15 opponent specs in both seats, listed below), and 3 of
  its gate games contain a call of 3 s or more (the slowest is 3.77 s, against a staged_guard_maze in afs5; call
  times are wall-clock and were taken on a shared box).
- Where af5 is weaker than best_v9e (gate, both seats, round 50 unless stated): six economy.timing strikers with
  attack_round 4 or 5 and the default economy.timing (-25 to -79, where best_v9e wins by 15 to 560); the old economy
  bots econ8 (two specs), econ9 and econ10 (-21 against +5 to +10); fortress v20 (-5 against +5); opening_response
  guard_poke5 (-12 against a draw); poke_lock (a draw against +10); guard_geometry with one tier1 at (9,1) (-13
  against +7). It also loses to the lead's P4TNUB, P5TNUBM and AS1C by 10 (afq56, afrr), where best_v9e draws P4TNUB
  and P5TNUBM (finding 9).
- Against g1 on the gate, af5 is worse on 6 conditions (3 specs in both seats: guarded_adaptive_continuation with two
  tier1, -39 against +801; guarded_maze cash_rank_1 growth 6 guard 5 with a tier2 bait, -676 at round 10 against
  +788; staged_guard_maze lead_opening growth 7, -570 at round 10 against +1164), all among the 290 sweep conditions.
- Scenario starts: against the five opponents of opp_heldout3 without a clock read, on the 12 scenarios of held-out
  sets 3 and 4 (both seats, 120 games), af5 has V29's winner, HP margin and length in every game (18.35, H18.31a
  holds), as g1 does on every scenario start tested (finding 4). So that test does not restrict the recommendation to
  the standard start, but af5 was not run on the other scenario sets or against the clock-reading opponents of sets 3
  and 4; there V29 is the measured bot. In the lead's frr7 (report section 5.16: af5 against seven bots on mirror:1:2
  and asym:23:2, 28 games) attack_from=5 also changes no game relative to V29 and g1 (the lead's comparison).
- Sensitivity of the hold round: on the 290 sweep conditions (development evidence) the wins over attack_from = 2
  (V29), 3, 4, 5, 6 and 7 (g1) are 48, 146, 162, 264, 238 and 228 (18.26, 18.36, 18.37; H18.31b holds), so 5 is the
  best of the tested values there. Smaller values win at least as many strike1 conditions (24, 24, 22, 12, 8, 4) and
  at most as many GUARDED_MAZE conditions (0, 14, 20, 70, 72, 72); HANDOFF and SCREENED are not monotone in
  attack_from. None of af3, af4 and af6 had a held-out check.

### Rejected ideas (each measured; entry)

- Global attack hold to round 11 on the standard start (entry 8, sweep17: 44-4-34 against 76-2-4).
- A round-1 tier2 instead of a tier1 (entry 11, r1t2); persistence-aware attack value and alpha below 1 (entry 4);
  threat-triggered early insurance v14 (entry 5); econ22 race (entry 14); econ30 fill_any (17.7: -88.7 [-173.7, -15.3]
  clipped against V29 on held-out set 3); lift_idle 3 and 6 (17.11); r1_guard (17.12, 18.9 item 6); g2 = V29 +
  r1_units=0 (17.14: 6-0-30 on HANDOFF).
- A final tier5 flood on best_v9e against TIMING2 (18.13: 0 hits in 40 games).
- Reactive attack holds keyed on the opponent's first minion purchase or first turret (18.2, 18.21: log analysis
  only; neither signal separates the families before round 4).
- g1f = g1 + fill_own (econ31, 18.15): fails its pre-stated rule (18.21) and on the 210 gate1 conditions goes
  98-6-106 against g1's 144-8-58, g1f - g1 -0.224 [-0.310, -0.143] (18.24).
- af6 = V29 + attack_from=6 (18.25): qualifies under the 18.22 rule but has 26 fewer wins than af5 on the 290 sweep
  conditions (18.26), so it was not run further.
- af4 and af3 = V29 + attack_from=4 and 3 (18.36, 18.37, sensitivity only): 162-2-126 and 146-0-144 on the 290 sweep
  conditions against af5's 264-0-26; they win more strike1 conditions than af5 (22 and 24 against 12) and fewer than
  half of its 214 wins on GUARDED_MAZE, HANDOFF, SCREENED and STAGED (102 and 84).

### Open failure cases (all reproducible from the named runs)

- The round-1 exchange on the standard start: V29, g1 and g0 against best_v9e, best_v9f, af2g, the lead's v28 and v30
  (-8 to -15 at round 50); af5 against v28 (P4TNUB), v30 (P5TNUBM) and AS1C (-10 at round 50; finding 2).
- af5 on the gate (40 losses and 2 draws in 846 conditions, both seats each): economy.timing with attack_round 4 or 5
  (all 16 STRIKE1 losses, -25 to -79 at round 50) and the default economy.timing (-74, counted in TIMING and f5t); the
  late floods of econ8, econ9 and econ10 (-21); fortress v20 (-5); opening_response guard_poke5 (-12); guard_geometry
  with one tier1 at (9,1) (-13); guarded_adaptive_continuation with two tier1 (-39); and two growth-first mazes that
  g1 wins (guarded_maze cash_rank_1 growth 6 guard 5, -676 at round 10; staged_guard_maze lead_opening growth 7, -570
  at round 10). The 2 draws are poke_lock.
- g1 against early strikers: economy.timing with attack_round 4 or 5 (-25 to -145 at round 50) and with attack_round
  7 and repeat=true (-2139 at round 36, -1859 at round 40; own lock out of reach after the round-7 purchase, 18.15);
  guard_geometry and guard_roster with one tier1 or tier2 (-5 to -12).
- V29 against growth-first openings: GUARDED_MAZE with guard_round 4 or 5 (72 losses, rounds 8 to 12), SCREENED and
  STAGED (36 and 76 losses, 18.7), HANDOFF (34 losses), six fresh5 counters (-596 to -886, 18.12).
- Both V29 and g1: the own lock out of reach against late tier5 floods of old economy bots (econ8, econ9, econ10:
  V29 -5618 and -2678; g1 -45 at round 50, 18.15).
- Scenario starts: eco6_t5 on mirror:41:2 (-980, entry 16), asym:35:2 seat 0 (entry 15), and the re-plan gain
  threshold on mirror three-site starts (17.10).

### Uncertainty and limits

- The engine is deterministic, so repeated games of one condition add nothing; what varies is the opponent spec, the
  seat and, on scenario starts, the scripted opening. In every standard-start run where this was checked (gate1,
  fam2b, fresh5, fresh6, pcs1, g1fg, afs6, afs5, afq56, afg5, afrr, afs4, afs3) each opponent spec gives the same
  outcome in both seats (in afs5, afq56, afg5, afrr, afs4 and afs3 also the same margin), so the effective sample is
  the number of opponent specs, not of games.
- Bootstrap intervals resample opponent specs of one list (cluster bootstrap, 4000 resamples); they describe that list
  and do not cover opponents outside it. Many specs of one pool are parameter variants of one hrt-w3 or lead bot, so
  the opponents within a pool are not independent draws.
- Selection: GROWERS, GUARDED_MAZE, HANDOFF and opp_key5 (which overlaps f5t) were seen when g1 was chosen, and the
  290 sweep conditions were chosen because V29 and g1 differ on them; results on those sets are development evidence.
  Held-out for g1: fam2b, fresh5, fresh6 and the ten gate pools run after 17:53Z. Held out for af5 (all fixed before
  its games): afq56 (fresh5 + fresh6), afg5 (the 514 gate conditions outside the sweep), afrr (the ten bots of the
  lead's round robin frr1) and afrep. The 296 gate conditions that use sweep specs are development evidence for af5.
- Most hrt-w3 counters in fresh5 and fresh6 were built against best_v9e, which favors the economy bots in any
  comparison with best_v9e on those sets; the 15 opponents built against neither are reported separately.
- Load: the box ran at load averages of about 11 to 155 during these runs. Opponents whose import closure reads the
  clock (18.9 item 12: 21 of 27 in opp_fresh5, 44 of 105 in opp_gate1) may play differently under other load, so each
  of those games is one sample. V29, g1, g0, af6 and af5 run their planners without a wall-clock cutoff.
- Runtime: the largest single decide call of the economy bots was 18.73 s (g1 against fortress v44 in fresh6, late in
  a game with 4.2 million gold and 14,190 factories at the end); in gate1, fam2b and afs6 it is at most 6.52 s. af5's
  largest call is 11.15 s (against v44 in afq56); on the 846 gate conditions it is at most 3.77 s, with 3 games with a
  call of 3 s or more, and in afrr at most 3.07 s. Total decide time per game reaches about 150 s against hrt-w1's
  fortresses v44 and v45. No time limit appears in bot_research/harness or td_game/runner.py (searched for timeout,
  time_limit and deadline), so this cost changed no result here; a per-call limit could.

### Reproduction (from the project root, with the .venv for games and any Python 3.12 for the tables)

- A tournament: `JOBS=2 bot_research/experiments/economy/run_tourn.sh NAME bot_research/experiments/economy/opp_gate1.txt "" "$(cat bot_research/experiments/economy/specs/g1.spec)"`
  writes runs/economy/NAME (both seats; a non-empty third argument adds scenario names; KEEP=all keeps every log).
  Use a new NAME for every run.
- Pool tables and paired intervals: `python3 -B bot_research/experiments/economy/pooltab.py bot_research/runs/economy/gate1/results.jsonl bot_research/experiments/economy/opp_gate1_pools.json g1='fill_threat=true&attack_from=7' V29='fill_threat=true'`
  (a tag matches the rows whose candidate spec ends with its suffix; the first tag is the minuend of each paired
  difference).
- The 846-condition comparison with best_v9e: `python3 -B bot_research/experiments/economy/gate_vs_base.py bot_research/experiments/economy/specs/g1.spec bot_research/experiments/economy/specs/v29.spec`
  (add `--show` to list the worse and better conditions). It reads best_v9e's rows from the base files of the lead's
  gate script, four of which (base_t8f_v18f, base_b9a_v18f, base_gm2_v18f, base_st1_v18f) are under bot_research/tmp
  and are not owned by this lane.
- The sweep rule: `python3 -B bot_research/experiments/economy/dec22.py`.
- af5 on the gate: `python3 -B bot_research/experiments/economy/gate_vs_base.py bot_research/experiments/economy/specs/af5.spec --show`;
  af5 against best_v9e with every log kept: `KEEP=all JOBS=1 bot_research/experiments/economy/run_tourn.sh NAME bot_research/experiments/economy/opp_bv9e.txt "" "$(cat bot_research/experiments/economy/specs/af5.spec)"`.

## Entry 20 (2026-11-01T00:09:35Z): corrections to 18.33, 18.34, 18.35 and Entry 19 after hrt-w3's checks (validation.md, 23:46Z to 00:05Z)

Each item was rechecked here from the records or the frozen source; no game was run.
1. 18.34, largest af5 call in afrr: "0.8 s" is wrong. From decide_max_seconds in runs/economy/afrr/results.jsonl
   (indexed by physical seat), af5's largest call is 3.0694 s (result line 8, af5 in seat 1 against g1). af5 also has
   3.0148 s against g1 (line 7) and 2.95 s and 2.90 s against V29 (lines 5 and 6); against the other eight opponents
   its largest call is 0.78 s, which matches the wrong figure. Entry 19 (Uncertainty, Runtime) already
   gives "in afrr at most 3.07 s". afrr is not a gate run, so the H14 status of af5 in Entry 19 is unchanged.
2. 18.33, log retention: "afrr keeps only the logs of losses, so the mechanism is not visible" is wrong. All 20 afrr
   logs exist (runs/economy/afrr/logs). Under KEEP=losses, harness/tournament.py (line 61) drops a won game's log only
   if the game is not first_of_pair, and line 223 marks every game on the first scenario of the list as first_of_pair.
   A run with only the standard start therefore keeps every log. 18.34 itself read afrr game 9. The afrep prediction
   H18.33 and its result do not depend on this premise. Entry 19 (Artifacts, Runs) says "match logs of losses (or all
   games where stated)". It should read: logs of all losses and of every game on the first scenario of the run's list,
   so every game of a standard-start-only run.
3. 18.35, foreign hold: the parenthesis "no attack, finish or doom purchase before foreign_attack_from=11" is wrong.
   In bots/economy/frozen/v29/econ29.py only the ordinary attack (the nested attack function, which also serves the
   open-case attack) returns while hold is true. The finishing attack and the doom attack test rnd >= attack_from
   and their own conditions, not hold. The open-case branch sets attacked = True even when attack returns under hold,
   and that suppresses doom in that round. Corrected sentence: a possible reason is the ordinary attack's separate hold
   on maps with buildings the bot did not request, before round 11; finishing and doom keep their attack_from checks
   and bypass that hold, subject to their other conditions. This mechanism was not checked game by game. hrt-w3 found
   no accepted minion purchase in 356 candidate rounds (after the scripted prefix, before round 11) of 45 retained
   histories; 103 of the 120 scnaf5 histories were not kept, so a reachable game in which finish or doom fires under
   the hold is neither shown nor excluded. The 120 equal outcomes in 18.35 are unchanged.
4. Entry 19, finding 3, "holding attacks until round 11 on a map with buildings the bot never requested": the hold is
   the ordinary attack's hold of item 3, not a hold of finishing or doom purchases.
No other statement of 18.33 to 18.37 or Entry 19 was found to be contradicted by validation.md up to its 00:06:20Z
entry. The frr8 HP erratum there (790:735, not 795:740) concerns hrt-w3's own review; these notes give no frr8 HP pair.
The af5 terminal HP in 18.34 (785 against 375, round-1 785 against 795, -140 in round 9 and -280 in round 10) agrees
with hrt-w3's recount.

## Entry 21 (2026-11-01T00:13:01Z): corrections to Entry 19 after hrt-w3's review of it (validation.md 00:10:17Z; reviews/economy_final_gate_001/final_summary_019_001)

Each item was rechecked here from the result files (lane scratch scripts af5_vs_g1.py and scope_chk.py, which reuse
the loaders of experiments/economy/gate_vs_base.py); no game was run. All items are accepted.
1. af5 worse than g1 on the gate: 8 conditions, not 6 (4 opponent specs in both seats, 8 pool memberships, all among
   the 290 sweep conditions). The omitted spec is bot_research.bots.economy.timing:@make?attack_round=5&pre_defend=true&pre_gold=60
   (STRIKE1): af5 -34 at round 50 (V29 also -34), g1 +350 at round 50, in each seat (afs5 and gate1 rows). The other
   three specs of Entry 19 are confirmed. The 18.26 safeguard (no gate pool with more than 2 fewer wins than g1) is
   unchanged. The same correction applies to "Open failure cases", where this spec is among the STRIKE1 losses but
   was not named as a g1 win.
2. Memberships and distinct conditions: the 14 gate pools have 846 memberships over 804 distinct (opponent,
   scenario, seat) conditions from 402 specs; the ten pools other than GROWERS, GUARDED_MAZE, HANDOFF and f5t have 448
   memberships over 416 distinct conditions (208 specs); the sweep part has 296 memberships over 290 distinct
   conditions and the rest 550 over 514. Wherever Entry 19 (findings 7 and 9, recommendation, uncertainty) and 18.23,
   18.32 say "846 conditions", "448 conditions", "550" or "296", read memberships; the W-D-L tables are counts of
   memberships, as in the recommendation paragraph. The 32 adverse memberships against best_v9e are 30 distinct
   conditions from 15 specs.
3. Held-out labels for afrr and afrep (Entry 19, Uncertainty, Selection): afrr is not a wholly fresh sample. 8 of its
   20 games are exact repeats of afq56 games (v41, best_v9e?attack_share=1.0&catch_up_share=0.5, best_v9f?passive_until=null
   and the lead's v30 spec, both seats, same outcome, margin and length in both runs), and 2 more use early_wall_guard
   with witness="guard00", which is that bot's default, so they are the afq56 games against early_wall_guard:@make
   under another spec text (same outcome, af5 +2 at round 50 in both seats). afrep was stated after afrr outcomes were seen and is a reproduction control, not
   held-out strength evidence. The held-out evidence for af5 is afq56 and afg5, plus the 10 afrr games against the
   five bots not in afq56 (best_v9e, best_v9f, V29, g1, threat_defender).
4. The 15-opponent subset of fresh5 and fresh6 (18.29, 18.30, Entry 19 finding 9, recommendation, uncertainty): read
   "the 15 opponents not written by hrt-w3 (the lead's and hrt-w1's bots)" for "the 15 opponents built against
   neither bot"; that none of them was developed against best_v9e or an economy bot is not established. The sentence
   "which favors the economy bots in any comparison with best_v9e on those sets" is a conjecture: many hrt-w3
   opponents there were built against best_v9e, which is a possible source of selection bias that these runs do not
   measure. The intervals are unchanged.
5. Scenario starts (18.35 and Entry 19 finding 4): the 120 scnaf5 games, like ho1g1 and hs34g1 for g1, show equal
   winner, HP difference and number of rounds to V29's games; actions were not compared. "equal to V29 game by game"
   and "changed no game" mean these three recorded outputs, and the clause "so the attack holds attack_from=7 and 5
   act only on the standard start in these runs" is withdrawn: they changed no recorded outcome on the scenario starts
   tested, which does not show that they are inactive there.
6. frr7 (Entry 19, recommendation, scenario starts): af5 played seven bots on mirror:1:2 and asym:23:2 in both seats
   (28 games, runs/lead/frr7). V29's and g1's games against the same opponent, scenario and seat exist for 24 of the
   28 each (neither has a game against itself), 20 conditions have both, and the union covers all 28. hrt-w3 reports
   equal full histories on each set of 24; this lane checked only the counts from the frr7 result file.
7. Runtime (Entry 19, Uncertainty): "so this cost changed no result here" is withdrawn. Supported: no time limit is
   applied by bot_research/harness or td_game/runner.py, so no game here was cut off or forfeited by one, and the
   reported outcomes occurred with the recorded call times. Whether other load or a per-call limit would change an
   outcome is not known; the clock-reading opponents (Uncertainty, Load) are the likely place.
8. The best_v9e column of finding 7: the base rows are the frozen best_v9e (bot_research.experiments.lead.frozen.best_v9e:@make)
   on PCS, TIMING, STRIKE1, f5t, HANDOFF and SCREENED, and explicit parameterized configurations of
   bot_research.experiments.lead.v18 (TARGETED2) or lead.v19 (the other seven pools), which the lead's gate script
   uses for best_v9e. This lane did not check that those configurations play as the frozen best_v9e.
9. The mixture of the lead's eleven-bot matrix (Entry 19, recommendation): each max-min mixture puts 1/3 on af5, 1/3
   on guard00, and the remaining 1/3 split in any proportion between P5TNUBM and AS1C; it is a statement about that
   finite W-D-L table with zero diagonal (report section 5.16), not a general optimum.
None of these changes a W-D-L count, a margin, an interval or the recommendation of Entry 19; items 1 and 3 change
counts and labels in its text.
