# Game records and replay

The supplied records live in `data/games/`: `game_000001.jsonl` through
`game_001000.jsonl`, plus `manifest.json`. Identities are anonymous IDs
`bot1` through `bot30`. The manifest lists each game's ID, filename, player
identities. It contains no bot source or
strategy descriptions.

These supplied games were recorded with the earlier scout/brute/titan and
gun/mortar/laser catalogs and wall cost 5. Their embedded rules and results
remain historical records. New matches use the current tier1–tier5 and
gun1/gun2/gun3/splash catalogs in [the game rules](game.md). Each replay
uses its own recorded metadata, including its building symbols.

## JSONL format

Each UTF-8 line is one complete player record with:

- `schema_version`: currently 1.
- `round`: 0 for initial state, then consecutive completed rounds.
- `player`: 0 or 1, identifying the record explicitly.
- `event`: structured round events.
- `snapshot`: the fully settled player state.

There are exactly two records per frame, one for each player. Round 0 grants
no income and performs no combat. A full 50-round game has 102 player records.
The final round is recorded normally and includes a `result` object with
`winner` (player index or null) and `reason`.

Both round-0 records contain matching `match` metadata: complete rule/type
catalogs, both bot identities, and the neutral `game_id`. The
viewer and feature extractor need no external configuration or bot source.

## Snapshots and events

A snapshot contains `name`, `hp`, `gold`, `n_factories`, `n_turrets`,
`n_walls`, `length_path`, `buildings`, and `roster`.

`buildings` is sparse, for example `{"x": 3, "y": 4, "type": "wall"}`.
No character matrix or path coordinates are persisted. `n_turrets` counts
only attacking buildings, excluding walls. `length_path` counts movement
steps on the player's own map.

Roster entries include stable IDs, type, purchase round, expiration round,
and remaining lifetime. Null expiration denotes permanence. The settled
roster contains only unexpired entries; combat deaths do not remove them.

Events include accepted/rejected actions and reasons, combat hit/damage
counts, income components, roster expiration, and bot errors. Combat totals
refer to each player's attacking copies; base damage received is separate.
Income events provide explicit path, factory, hit, and total components.
There are no tick-level records, movement traces, or firing animations.

`td_game.logs.load_log` pairs records by `(round, player)`. Malformed JSON,
duplicate identities, missing partners/fields, invalid snapshots, unsupported
schema versions, or mismatched round-0 metadata produce located errors.

## Viewer

```bash
td_view data/games/game_000001.jsonl --check
td_view data/games/game_000001.jsonl
```

`--check` validates and constructs scenes without a terminal. Interactive
use requires a UTF-8 terminal, Linux/macOS curses, and at least 92 × 24 cells.

The fixed columns are `player0`, `player1`, and EVENT. Each player panel shows
its player label, HP, gold, a bordered 12 × 12 map, T/F counts, and roster entries.
The roster displays each minion as its tier digit `1`–`5` without separators,
for example `Roster(5):12345`. It wraps at the player panel's width and uses
the available rows above the outcome and playback controls; if it still
does not fit, the last visible line ends in `...`.
Historical scout/brute/titan entries display as `1`/`2`/`3`; unrecognized
types display as `?`.
Cells occupy two terminal columns and one row. Symbols are `.` for empty
terrain, `S` for spawn, `B` for base, and `#` for walls. Current turret
symbols are `1`/`2`/`3` for gun1/gun2/gun3 and `X` for splash; the supplied
historical logs retain their recorded `G`/`M`/`L` symbols.
Overflow uses `...`; narrow terminals show an enlargement prompt.

| Key | Effect |
| --- | --- |
| Space | Pause/resume |
| Left / k | Previous frame |
| Right / j | Next frame |
| Home / 0 | First frame |
| End / G | Last frame |
| + / = | Speed up |
| - | Slow down |
| v | Toggle detailed events |
| q | Quit |

Speeds are 0.25×, 0.5×, 1×, 2×, and 4×; 1× advances one round per second.
Manual frame changes pause playback, and playback stops at the last frame.
The event panel contains events through the current frame: going backward
removes future events, and revisiting a frame does not append duplicates.

The entry point supplies a small redraw callback containing
`draw(screen, {"vs": vs})`. `control.py` owns curses startup and playback,
`scene.py` builds display data from snapshots, and `draw.py` renders panels.
Replay never reruns the engine, imports bots, or computes a path. Path
length stays stored but is not drawn or displayed.

## Summaries

```bash
td_stats data/games/game_000001.jsonl
td_stats data/games/game_000001.jsonl --json
```

Summaries report players, outcome, rounds, final HP/gold, and recorded event
totals. They read snapshots/events rather than inferring purchases or income
from changes in final counts or balances.
