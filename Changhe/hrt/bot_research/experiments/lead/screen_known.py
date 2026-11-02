"""Known-policy exploitability screen of one lead setting (development only).

    taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.experiments.lead.screen_known \\
        NAME '{"spec_share":1.0}' [--grid small|full|early|rounds|waves] [--model v5]
        [--counter known|public|stateful|mixed|schedule]

Plays the lead setting (module experiments/lead/MODEL.py; default v5) against a counter that forecasts
that same setting exactly, for every attack round and tier in the grid, attack_share=1.0, both seats,
through the ordinary tournament driver (results in runs/lead/NAME/). Counters: "known" is
experiments/lead/known_counter.py (models v4, v4b, v5, v6); "public" is hrt-w3's
bots/counters/public_factory.py timing counter with the model named as module:@make (any model; it
builds a fresh model for every prediction, so it is not exact against stateful settings such as
attack_mode "adaptive", hrt-w3 07:06Z); "stateful" is hrt-w3's bots/counters/stateful_public.py, the
same timing counter with one persistent private model per game;
"mixed" is the same file's mixed-package counter (bounded search over ordered mixed purchases at the
attack round; the grid's tier is ignored, use --grid rounds); "schedule" is hrt-w3's
bots/counters/public_schedule.py with one tier1 in round 1 followed by the grid's wave (all gold;
use --grid waves; it is the two-wave form that beat hrt-w3's lead7 snapshot 800:735). The lowest candidate HP difference over
the grid is the setting's measured exploitability on this grid.
"""
from __future__ import annotations

import json
import os
import sys

from bot_research.harness import tournament

# With this file present the screen uses one worker (as run_pool.sh does), leaving a slot for development games.
JOBS1 = "bot_research/experiments/lead/JOBS1"

GRIDS = {
    "small": [("tier3", r) for r in (3, 5)] + [("tier4", r) for r in (5, 7, 9)]
             + [("tier5", r) for r in (7, 8, 9, 10, 11)],
    "full": [("tier1", r) for r in (2, 3, 4)] + [("tier2", r) for r in (2, 3, 4, 5)]
            + [("tier3", r) for r in (3, 4, 5, 6)] + [("tier4", r) for r in (5, 6, 7, 8, 9, 10)]
            + [("tier5", r) for r in (6, 7, 8, 9, 10, 11, 12, 14, 16, 20)],
    "early": [("tier1", r) for r in (2, 3, 4)] + [("tier2", r) for r in (2, 3, 4, 5)],
    "rounds": [(None, r) for r in (3, 4, 5, 6, 7, 8, 9, 10, 11)],
    "waves": [("tier3", r) for r in (3, 4, 5, 6)] + [("tier4", r) for r in (4, 5, 6, 7, 8)]
             + [("tier5", r) for r in (7, 8, 9, 10)],
}


def specs(params: dict, grid: str = "small", model: str = "v5", counter: str = "known"):
    q = "&".join(f"{k}={json.dumps(v, separators=(',', ':'))}" for k, v in params.items())
    cand = f"bot_research.experiments.lead.{model}:@make" + (f"?{q}" if q else "")
    mp = json.dumps(params, separators=(",", ":"))
    pf = "bot_research.bots.counters.public_factory:"
    ms = f'model_spec="bot_research.experiments.lead.{model}:@make"&model_parameters={mp}'
    if counter == "known":
        opps = [f'bot_research.experiments.lead.known_counter:@timing?model="{model}"&model_parameters={mp}'
                f'&attack_round={r}&tier="{t}"&attack_share=1.0' for t, r in GRIDS[grid]]
    elif counter == "public":
        opps = [f'{pf}@timing?{ms}&attack_round={r}&tier="{t}"&attack_share=1.0' for t, r in GRIDS[grid]]
    elif counter == "stateful":
        opps = [f'bot_research.bots.counters.stateful_public:@timing?{ms}&attack_round={r}&tier="{t}"&attack_share=1.0'
                for t, r in GRIDS[grid]]
    elif counter == "mixed":
        opps = list(dict.fromkeys(f'{pf}@mixed?{ms}&attack_round={r}&attack_share=1.0' for _, r in GRIDS[grid]))
    elif counter == "schedule":
        opps = [f'bot_research.bots.counters.public_schedule:@make?{ms}'
                f'&schedule=[[1,"tier1",1],[{r},"{t}",200]]&defense_first=false' for t, r in GRIDS[grid]]
    else:
        raise ValueError(f"unknown counter {counter}")
    return cand, opps


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    opts = {"--grid": "small", "--model": "v5", "--counter": "known"}
    for key in opts:
        if key in argv:
            i = argv.index(key)
            opts[key] = argv[i + 1]
            del argv[i:i + 2]
    name, params = argv[0], json.loads(argv[1])
    cand, opps = specs(params, opts["--grid"], opts["--model"], opts["--counter"])
    return tournament.main(["--name", name, "--candidates", cand, "--opponents", *opps,
                            "--jobs", "1" if os.path.exists(JOBS1) else "2", "--keep-logs", "losses"])


if __name__ == "__main__":
    sys.exit(main())
