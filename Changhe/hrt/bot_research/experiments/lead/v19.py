"""Lead v19 development bot: v18 with two more foreign-map targets.

v18 is imported unmodified. ``foreign_target`` may also be a key of FOREIGN19; for such a key the instance is
built with v18's foreign_target=None, and in the first round in which v16's foreign-map test holds (and no
policy has taken over yet) a fresh instance of the frozen target is created and plays the rest of the match
(v16 plays self.alt whenever it is set). For the keys of v18.FOREIGN, or without foreign_target, it plays as v18.
Targets added (2026-10-31T10:27Z):
  econ20     hrt-w2's frozen econ20 (notes/economy.md entry 13) with replan=true and foreign_sat_from=11:
             econ19 plus hrt-w1's deterministic layout re-planner on foreign maps; 14-0-2 against fortress v25
             and v26 under the four scripted starts in hrt-w2's smoke20b. No wall-clock cutoff.
  fortress27 hrt-w1's frozen fortress v27 (notes/defense.md 10:13Z, recommended artifact). Its planner keeps a
             3 s wall-clock cutoff (hrt-w3, notes/validation.md 10:23Z), so its actions may depend on the load.
"""
from __future__ import annotations

from bot_research.experiments.lead import v18
from bot_research.harness.match import resolve_spec

FOREIGN19 = {
    "econ20": 'bot_research.bots.economy.frozen.v20.econ20:@make?free_fallback="zero"&foreign_attack_from=11'
              '&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11',
    "fortress27": "bot_research.bots.defense.frozen.v27.fortress:@make",
}


class Lead19(v18.Lead18):
    def __init__(self, foreign_target=None, **params):
        new = foreign_target in FOREIGN19
        super().__init__(foreign_target=None if new else foreign_target, **params)
        if new and self.foreign_policy is None:
            raise ValueError(f"foreign_target {foreign_target!r} needs foreign_policy")
        self.target19 = foreign_target if new else None

    def __call__(self, obs):
        if self.target19 is not None and self.alt is None and self._foreign(obs):
            self.alt = resolve_spec(FOREIGN19[self.target19])
            self.switch_round = obs["round"]
        return super().__call__(obs)


def make(**params):
    return Lead19(**params)
