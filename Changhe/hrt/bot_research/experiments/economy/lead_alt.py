"""The lead's bot with a different foreign-map policy (hrt-w2 experiment wrapper, not a candidate file).

The lead's Insurer (frozen best_v9e, or development v24) hands the rest of a match to a fresh instance of
the frozen economy bot econ20 from the first round in which its own map holds a building at a cell it never
asked for (after a scripted opening). This wrapper subclasses that Insurer unmodified and only changes which
bot is created at that moment. The switch test is the same expression as in the lead's __call__.

Spec: bot_research.experiments.economy.lead_alt:@make?base="v9e"&alt="v25rm"&<Insurer parameters>
- base: "v9e" (experiments/lead/frozen/best_v9e.py, the installed best.py) or "v24" (experiments/lead/v24.py).
- alt: a key of ALTS; "econ20" keeps the lead's own target (identity check).
"""
from __future__ import annotations

import importlib

BASES = {
    "v9e": "bot_research.experiments.lead.frozen.best_v9e",
    "v24": "bot_research.experiments.lead.v24",
}

V25RM = dict(free_fallback="zero", foreign_attack_from=11, doom="next", fac_cap=400, sat_reach=True, replan=True,
             foreign_sat_from=11, replan_gain=400, replan_base=True, own_in_layout="replan", own_min_s=1200,
             min_cap=3000, active_cap=4000)
V27 = dict(V25RM, fill=True, fill_reserve=True)
V29 = dict(V27, fill_threat=True)
V30 = dict(V29, fill_any=True)
V23 = dict(free_fallback="zero", foreign_attack_from=11, doom="next", fac_cap=400, sat_reach=True, replan=True,
           foreign_sat_from=11, replan_gain=400, replan_base=True)

ALTS = {
    "econ20": None,
    "v25rm": ("bot_research.bots.economy.frozen.v25.econ25", V25RM),
    "v23": ("bot_research.bots.economy.frozen.v23.econ23", V23),
    "v27": ("bot_research.bots.economy.frozen.v27.econ27", V27),
    "v29": ("bot_research.bots.economy.frozen.v29.econ29", V29),
    "v30": ("bot_research.bots.economy.frozen.v30.econ30", V30),
}


def make(base="v9e", alt="v25rm", **params):
    cls = importlib.import_module(BASES[base]).Insurer
    target = ALTS[alt]
    if target is None:
        return cls(**params)
    alt_mod = importlib.import_module(target[0])
    alt_params = dict(target[1])

    class Swapped(cls):
        def __call__(self, obs):
            me = obs["players"][obs["player"]]
            if self.alt is None and self.p["foreign_policy"] is not None and \
                    {(b["x"], b["y"]) for b in me["buildings"]} - self.requested:
                self.alt = alt_mod.make(**alt_params)
                self.switch_round = obs["round"]
            return super().__call__(obs)

    return Swapped(**params)
