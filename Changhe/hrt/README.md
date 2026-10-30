# Tower Defense Interview

This repository contains a two-player tower defense game, a replay viewer,
a pathfinding exercise, and a data-analysis exercise. The supplied dataset
contains 1,000 games played by 30 unknown bots, identified as `bot1`–`bot30`.

## Setup

Use Python 3.11 or later. From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[analysis]'
```

The game and viewer use the Python standard library. The analysis extra
installs pandas and Jupyter Notebook. The viewer requires Linux/macOS curses
and a UTF-8 terminal of at least 92 × 24 cells.

## Replay a game

```bash
td_view data/games/game_000001.jsonl
```

The viewer shows `player0 | player1 | EVENT` using round-level snapshots.
Use Space to pause/resume, arrow keys to move between rounds, and `q` to quit.
Validate a replay without opening the terminal viewer:

```bash
td_view data/games/game_000001.jsonl --check
```

See [replay documentation](docs/replay.md) for the record format, viewer
controls, and `td_stats` summaries.

## Interview exercises

Implement the two function stubs in
[interview_pathfinding/problems.py](interview_pathfinding/problems.py).
Their contracts are described in the docstrings and
[exercise README](interview_pathfinding/README.md).

Open the executed starter notebook:

```bash
jupyter notebook data_analysis/analysis.ipynb
```

It loads the initial feature table from `data/games/`. See the
[data-analysis README](data_analysis/README.md) for its columns.
[AGENTS.md](AGENTS.md) defines the assistant's permitted role during the interview.

## Game runtime

See [game rules](docs/game.md) for observations, actions, and parameters.
The runner accepts trusted Python callables through `--bot-a` and `--bot-b`.
Without them, it submits empty actions:

```bash
td_match --balanced --output local-runs/my-match.jsonl
```

The supplied games replay independently of the engine and bot source.

## Infrastructure checks

```bash
python -m unittest discover -s tests -v
```
