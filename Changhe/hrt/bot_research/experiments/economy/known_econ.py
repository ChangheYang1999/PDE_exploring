"""Known-policy timing counter against this lane's econ bots (development only).

Wraps hrt-w3's ForecastTiming (bots/counters/forecast_timing.py, imported
unmodified) with an econ model, as the lead's experiments/lead/known_counter.py
does for its v4..v6. Every round the counter predicts the econ bot's exact
actions from a copy of the public observation (the model is the frozen econ
factory with the same parameters, rebuilt for every prediction), defends
against econ's active roster, buys factories (at most 80 per round), and in
``attack_round`` buys as many copies of ``tier`` as ``attack_share`` of its
gold allows if they leak on econ's predicted post-action map.

    bot_research.experiments.economy.known_econ:@timing?model="v10"&model_parameters={"r1_units":2}&attack_round=9&tier="tier5"&attack_share=1.0

The forecast is exact: econ v10, v13 and v14 keep one flag (whether the opponent ever owned
a turret), and since buildings are never removed the flag equals "the
opponent owns a turret now", which a fresh model recomputes from the
observation.

``python3 known_econ.py GRID 'PARAMS_JSON' [MODEL]`` prints the opponent specs
of the grid (one per line) for experiments/economy/run_tourn.sh.
"""
from __future__ import annotations

import json
import sys

GRIDS = {
    "small": [("tier3", r) for r in (3, 5)] + [("tier4", r) for r in (5, 7, 9)]
             + [("tier5", r) for r in (7, 8, 9, 10, 11)],
    "full": [("tier3", r) for r in (3, 4, 5, 6)] + [("tier4", r) for r in (5, 6, 7, 8, 9, 10)]
            + [("tier5", r) for r in (6, 7, 8, 9, 10, 11, 12)],
}


def _models():
    from bot_research.bots.economy.frozen.v10 import econ10
    from bot_research.bots.economy.frozen.v13 import econ13
    from bot_research.bots.economy.frozen.v14 import econ14
    from bot_research.bots.economy.frozen.v15 import econ15
    from bot_research.bots.economy.frozen.v16 import econ16
    return {"v10": econ10.make, "v13": econ13.make, "v14": econ14.make, "v15": econ15.make,
            "v16": econ16.make}


class _Model:
    def __init__(self, name, parameters):
        self.make = _models()[name]
        self.parameters = dict(parameters or {})
        self.make(**self.parameters)

    def __call__(self, observation):
        return self.make(**self.parameters)(observation)


def timing(model="v10", model_parameters=None, **parameters):
    from bot_research.bots.counters.forecast_timing import ForecastTiming
    counter = ForecastTiming(**parameters)
    counter.model = _Model(model, model_parameters)
    return counter.decide


def grid_specs(grid, params, model="v10"):
    mp = json.dumps(params, separators=(",", ":"))
    return [f'bot_research.experiments.economy.known_econ:@timing?model="{model}"&model_parameters={mp}'
            f'&attack_round={r}&tier="{t}"&attack_share=1.0' for t, r in GRIDS[grid]]


if __name__ == "__main__":
    for s in grid_specs(sys.argv[1], json.loads(sys.argv[2]), *(sys.argv[3:4] or ["v10"])):
        print(s)
