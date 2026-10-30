from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path

from td_bots.protocol import collect_actions, load_bot

from .config import balanced_config, load_config
from .engine import Engine


def run_match(config, bots, names, output: str | Path, *, match_metadata: dict | None = None) -> Engine:
    engine = Engine(config, tuple(names))
    initial = engine.initial_records(tuple(names))
    if match_metadata:
        if set(match_metadata) & set(initial[0]["match"]):
            raise ValueError("extra match metadata must not replace engine metadata")
        for record in initial:
            record["match"].update(deepcopy(match_metadata))
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive create prevents accidentally replacing an earlier match.
    with output.open("x", encoding="utf-8") as stream:
        def write(records):
            for record in records:
                stream.write(json.dumps(record, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n")
            stream.flush()

        write(initial)
        while engine.result is None:
            observations = [engine.observation(p) for p in (0, 1)]
            actions, errors = collect_actions(bots, observations)
            write(engine.play_round(actions, errors))
    return engine


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Run a deterministic trusted-Python bot match")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--balanced", action="store_true", help="select the bundled game rules")
    source.add_argument("--config", help="JSON rules file (must include minions, turrets, wall_cost)")
    parser.add_argument("--bot-a", default="td_bots.protocol:idle", help="module or module:function; defaults to empty actions")
    parser.add_argument("--bot-b", default="td_bots.protocol:idle", help="module or module:function; defaults to empty actions")
    parser.add_argument("--output", required=True, help="new JSONL file; existing files are not overwritten")
    args = parser.parse_args(argv)
    try:
        config = balanced_config() if args.balanced else load_config(args.config)
        names = (args.bot_a, args.bot_b)
        bots = [load_bot(spec) for spec in names]
        engine = run_match(config, bots, names, args.output)
    except (OSError, ValueError, ImportError, AttributeError) as exc:
        parser.exit(2, f"td_match: {exc}\n")
    winner = engine.result["winner"]
    outcome = "draw" if winner is None else f"player {winner} ({names[winner]}) wins"
    print(f"{config.label}\n{engine.round} rounds: {outcome} ({engine.result['reason']})")
    print(f"HP: {engine.players[0].hp} / {engine.players[1].hp}; log: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
