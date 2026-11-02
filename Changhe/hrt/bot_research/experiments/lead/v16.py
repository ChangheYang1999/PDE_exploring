"""Lead v16 development bot: v15 plus a policy switch for maps the bot did not build.

With the defaults (``foreign_policy=None``) it plays exactly as v15 with the same parameters
(v15 is imported unmodified; every other parameter is passed to it).

foreign_policy ("econ17" or None): the bot records every cell at which it asked to build. From the
first round in which its own map holds a building at a cell it never asked for (on the standard start
this cannot happen: a building appears only if the bot asked for it and the engine accepted it; after
a scripted opening or a legal-prefix start it does), the rest of the match is played by hrt-w2's
frozen econ17 (``bots/economy/frozen/v17/econ17.py``, imported unmodified) with
``free_fallback="zero", foreign_attack_from=11``, a fresh instance created in that round.
foreign_trigger: "any" (any such building) or "route" (only once such a building lies on the final
route of the master layout, i.e. once the layout's route cannot be completed as planned).
Reason (development games, 2026-10-31T08:05Z): on scripted openings the master layout cannot be
completed, splash-only insurance stalls below S = 1500 (S 1140 on mirror:1:2), and econ17, which
holds its attacks and grows, destroys v15 and hrt-w1's fortress v22 in rounds 11-13; hrt-w2 reports
econ17 107-0-1 on 108 scripted-opening conditions (notes/economy.md entry 8).
"""
from __future__ import annotations

from bot_research.bots.economy.frozen.v17 import econ17 as E17
from bot_research.experiments.lead import v15

E17_PARAMS = dict(free_fallback="zero", foreign_attack_from=11)


class Lead16:
    def __init__(self, foreign_policy=None, foreign_trigger="any", **params):
        if foreign_policy not in (None, "econ17"):
            raise ValueError(f"unknown foreign_policy {foreign_policy!r}")
        if foreign_trigger not in ("any", "route"):
            raise ValueError(f"unknown foreign_trigger {foreign_trigger!r}")
        self.base = v15.Lead15(**params)
        self.foreign_policy = foreign_policy
        self.foreign_trigger = foreign_trigger
        self.requested = set()
        self.alt = None
        self.switch_round = None

    def _foreign(self, obs):
        me = obs["players"][obs["player"]]
        cells = {(b["x"], b["y"]) for b in me["buildings"]} - self.requested
        if not cells:
            return False
        if self.foreign_trigger == "any":
            return True
        lay = self.base.layout
        return any(c in lay.final_route for c in cells)

    def __call__(self, obs):
        if self.alt is None and self.foreign_policy is not None and self._foreign(obs):
            self.alt = E17.make(**E17_PARAMS)
            self.switch_round = obs["round"]
        if self.alt is not None:
            return self.alt(obs)
        actions = self.base(obs)
        for a in actions:
            if a["op"] in ("build_wall", "build_turret"):
                self.requested.add((a["x"], a["y"]))
        return actions


def make(**params):
    return Lead16(**params)
