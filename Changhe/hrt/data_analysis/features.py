"""Extract game features and a bot target from each replay player."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from td_game.logs import load_log


FEATURE_COLUMNS = ["n_factories", "n_turrets", "length_path", "n_minions", "result"]
COLUMNS = [*FEATURE_COLUMNS, "target"]


def _game_id(match: dict, path: Path) -> str:
    tournament = match.get("tournament", {})
    if not isinstance(tournament, dict):
        raise ValueError(f"{path}: match.tournament must be an object")
    for metadata in (tournament, match):
        if "game_id" in metadata:
            value = metadata["game_id"]
            if (isinstance(value, str) and value.strip()) or type(value) is int:
                return str(value)
            raise ValueError(f"{path}: game_id must be a nonempty string or integer")
    if "game_index" in tournament:
        index = tournament["game_index"]
        if type(index) is not int or index < 0:
            raise ValueError(f"{path}: tournament.game_index must be a nonnegative integer")
        return f"game_{index:06d}"
    return path.stem


def build_feature_df(log_dir: str | Path) -> pd.DataFrame:
    """Read every top-level *.jsonl file; return two rows per completed game.

    The MultiIndex is (game_id, player), sorted by game ID then player. IDs use
    explicit game_id metadata first, then tournament.game_index formatted as
    game_000000, then the filename stem. Targets use match.bots, checked against
    snapshot.name; snapshot.name is the fallback for logs without match.bots.
    No filenames are used to identify bots. Core fields and both players are
    validated by the existing replay loader. Invalid or unfinished logs raise
    an error with their path; no games are silently skipped or values imputed.
    n_minions counts successful minion purchases across the entire game,
    including entries that expired before the final snapshot.
    """
    directory = Path(log_dir)
    if not directory.is_dir():
        raise ValueError(f"{directory}: expected a game-log directory")
    paths = sorted(directory.glob("*.jsonl"))
    if not paths:
        raise ValueError(f"{directory}: no game JSONL files found")

    rows, index = [], []
    seen = {}
    for path in paths:
        log = load_log(path)
        if log.result is None:
            raise ValueError(f"{path}: unfinished game; final result metadata is missing")
        game_id = _game_id(log.match, path)
        if game_id in seen:
            raise ValueError(f"{path}: duplicate game_id {game_id!r}; also used by {seen[game_id]}")
        seen[game_id] = path
        final = log.frames[-1]
        names = log.match.get("bots")
        if names is not None and (not isinstance(names, list) or len(names) != 2):
            raise ValueError(f"{path}: match.bots must contain exactly two bot identities")
        winner = log.result["winner"]
        for player in (0, 1):
            snap = final.records[player]["snapshot"]
            target = names[player] if names is not None else snap["name"]
            if not isinstance(target, str) or not target.strip():
                raise ValueError(f"{path}: player {player} has no identifiable bot target")
            if target != snap["name"]:
                raise ValueError(f"{path}: player {player} match.bots disagrees with snapshot.name")
            n_minions = sum(
                1
                for frame in log.frames
                for event in frame.records[player]["event"]
                if event["kind"] == "action"
                and event["accepted"] is True
                and isinstance(event["action"], dict)
                and event["action"].get("op") == "buy_minion"
            )
            rows.append({
                "n_factories": snap["n_factories"],
                "n_turrets": snap["n_turrets"],
                "length_path": snap["length_path"],
                "n_minions": n_minions,
                "result": 0 if winner is None else (1 if winner == player else -1),
                "target": target,
            })
            index.append((game_id, player))

    return pd.DataFrame(
        rows, columns=COLUMNS,
        index=pd.MultiIndex.from_tuples(index, names=["game_id", "player"]),
    ).sort_index()
