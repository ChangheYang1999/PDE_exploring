from __future__ import annotations

import argparse
import sys

from td_game.logs import load_log

from .control import run_replay
from .draw import draw
from .scene import buildscene


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Replay settled rounds from JSONL snapshots")
    parser.add_argument("log")
    parser.add_argument("--check", action="store_true", help="validate log and build scenes without a terminal")
    args = parser.parse_args(argv)
    try:
        log = load_log(args.log)
        if args.check:
            for frame in log.frames:
                buildscene(frame, log.match)
            print(f"Loaded {len(log.frames)} frames, rounds 0-{log.frames[-1].round}; replay data valid")
        else:
            if not sys.stdin.isatty() or not sys.stdout.isatty():
                parser.exit(2, "td_view: interactive replay requires a terminal; use --check for data validation\n")
            run_replay(log, lambda screen, vs: draw(screen, {"vs": vs}))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"td_view: {exc}\n")
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
