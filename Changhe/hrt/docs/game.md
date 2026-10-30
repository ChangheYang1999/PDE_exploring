# Game rules and engine

Two players build on separate 12 × 12 maps. Purchased minions enter the
opponent's map. Coordinates are `(x, y)`, with x as column and y as row;
grids use `[y][x]`. Spawn is `(0, 0)` and base is `(11, 11)`.

## Parameters

The JSON configuration is available in `configs/balanced.json` and bundled
with `td_game` for installed use.

| Parameter | Value |
| --- | ---: |
| Initial HP | 800 |
| Initial gold | 100 |
| Maximum rounds | 50 |
| Ticks per round | 250, numbered 0–249 |
| Roster lifetime | 12 rounds, including purchase round |
| Factory cost | 20 |
| Income per factory per round | 15 |
| Income per path movement step | 1 |
| Bounty per successful enemy-base hit | 5 |
| Wall cost | 1 |
| Wall damage / range / cooldown | 0 / 0.0 / 1 |

| Minion type | Cost | HP | Speed (cells per tick) | Base damage |
| --- | ---: | ---: | ---: | ---: |
| tier1 | 15 | 20 | 1.0 | 5 |
| tier2 | 40 | 70 | 1.0 | 12 |
| tier3 | 100 | 180 | 1.0 | 26 |
| tier4 | 260 | 560 | 1.0 | 60 |
| tier5 | 650 | 1500 | 1.0 | 140 |

| Turret type | Symbol | Cost | Damage per tick per target | Range | Cooldown | AOE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| gun1 | 1 | 30 | 8 | 2.5 | 1 | 0 |
| gun2 | 2 | 80 | 22 | 3.0 | 1 | 0 |
| gun3 | 3 | 200 | 55 | 3.5 | 1 | 0 |
| splash | X | 60 | 10 | 0.0 | 1 | 8 |

The reference's `ticks_per_turn` is stored as `globals.ticks_per_round`;
`base_hit_gold` is stored as `globals.base_hit_bounty`. The values are 250
and 5 respectively. Minion speed is explicitly 1.0 and building cooldown
is explicitly 1. The runtime supports one-cell-per-tick movement and
attacks every tick; configurations requesting other speeds or cooldowns
are rejected. Walls have explicit `wall_damage=0`, `wall_range=0.0`, and
`wall_cooldown=1` metadata and never attack.

## Rounds and observations

Each bot sees the same fully settled public state from the preceding round,
including both maps, HP, gold, factories, rosters, and rule parameters.
Current decisions remain hidden until both submissions are collected.
Observations are independent copies of engine state.

The round then proceeds through actions, both-map combat, income, roster
expiration, and outcome determination. Actions preserve each player's
submission order and interleave as A[0], B[0], A[1], B[1], continuing with
one player when the other list ends. Players cannot act during combat.

## Actions and construction

`decide(observation)` returns a list of JSON actions:

```json
[
  {"op": "buy_minion", "type": "tier1"},
  {"op": "buy_factory"},
  {"op": "build_turret", "type": "gun1", "x": 2, "y": 1},
  {"op": "build_wall", "x": 5, "y": 5}
]
```

This is an illustration of the action format, not a dataset bot policy.
There is no action-count or wall-count limit. Gold and legal placement limit
what can be purchased. Each action is validated separately; rejection does
not charge gold or cancel later valid actions. Unknown operations/types,
missing fields, invalid coordinates, or insufficient gold have explicit
rejection reasons.

Walls and turrets occupy one cell and block movement. They cannot overlap,
occupy spawn/base, or eliminate every route between endpoints. Buildings are
permanent; selling, replacement, removal, and upgrades are unsupported.
Factories are permanent, occupy no map cells, and provide income in their purchase round.
Walls never attack.

## Paths and combat

Movement is orthogonal, one cell per tick, along one deterministically
selected shortest route per map per round. Minions do not block each other
or affect route selection. Path length counts moves: an empty map has length
22. Paths may be computed internally but coordinates are never saved to the
replay. The viewer does not compute or draw paths or display their lengths.

A minion purchase charges its cost once and adds one roster entry. Fresh full-HP
copies spawn each round. Combat deaths do not remove entries. An entry
bought in round r participates through round r+11 and is removed after that
round settles. `roster_lifespan=0` supports permanent entries, represented
with a null expiration round.

Active entries retain purchase order and are densely indexed after expired
entries are skipped. The kth active entry spawns at tick
`k % ticks_per_round` (`k % 250` with the bundled rules); multiple copies
can spawn or occupy a cell together.
A newly spawned copy stays at spawn during its spawn tick and first moves
on the next tick. On a route of length L, a copy spawned at s reaches the
base at s+L. Arrival at tick 249 counts; arrival at 250 does not.

Each tick processes:

1. Spawn scheduled copies.
2. Move copies that existed before this tick.
3. Resolve base arrivals immediately and remove those copies.
4. Attack remaining copies with turrets.
5. Remove copies whose HP is at most zero.

Every gun attacks every target in range each tick (cooldown 1). Gun range
uses Euclidean distance, including its boundary. Splash has range 0.0 and
AOE 8: provisionally, it damages every copy in the eight neighboring cells
of the 3 × 3 neighborhood centered on the splash building, including
diagonals and excluding the center. It needs no target on its own cell.
Turret damage accumulates per copy before removal. Newly spawned copies can
be attacked; copies that already reached the base cannot. There are no
projectiles, armor, slowing, line-of-sight restrictions, or kill rewards.

Remaining combat copies are cleared at round end without base damage.
Their positions and HP do not carry into the next round.

## Income and outcomes

```text
income = own_length_path * 1 + own_factory_count * 15 + own_successful_hits * 5
```

Path income belongs to the owner of the defensive map. Hit bounties belong
to the attacking player and are counted once. Combat completes on both maps
before outcome determination, even if a base reaches zero HP earlier.
Recorded HP can be negative.

If one base has HP at most zero, its player loses; if both do, the match is
a draw. Otherwise, at round 50, higher HP wins and equal HP draws. Final
round records include the winner and end reason.

## Running the engine

After installation:

```bash
td_match --balanced --output local-runs/my-match.jsonl
td_stats local-runs/my-match.jsonl
td_view local-runs/my-match.jsonl --check
```

The default adapter returns empty actions. Supply your own `module` or
`module:function` through `--bot-a` and `--bot-b` to exercise other inputs.
A module selector uses its `decide` function. The adapter collects both
returns before applying actions and validates JSON-compatible output.
Bot exceptions or invalid whole returns produce empty submissions and a
recorded `bot_error`; individually invalid actions receive rejections.
Execution is trusted Python in process, without sandboxing or hard timeouts.

`--config FILE` replaces `--balanced` for an explicit configuration. Custom
configurations must include the minion/turret catalogs and wall cost;
missing numerical type definitions are errors. Global defaults remain
centralized in `GlobalRules`. The engine supports the fixed game map layout.

The runner creates the requested output directory and exclusively creates
a new log, preventing accidental replacement. The equivalent command is
`python -m td_game.runner` with the same options.
