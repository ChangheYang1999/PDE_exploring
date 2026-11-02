"""Lead v21 development bot: v20 with hrt-w2's econ21 as a further foreign-map target.

v20, v19 and v18 are imported unmodified. ``foreign_target`` may also be a key of FOREIGN21; for such a key the
instance is built with foreign_target=None, and in the first round in which v16's foreign-map test holds (and no
policy has taken over yet) a fresh instance of the frozen target is created and plays the rest of the match.
For other keys, or without foreign_target, it plays as v20.
Target added (2026-10-31T11:24Z):
  econ21  hrt-w2's frozen econ21 (notes/economy.md entry 14): econ20 that adopts a re-planned layout only if its
          final splash exposure exceeds the current layout's by at least replan_gain=400. hrt-w2 recommends it
          as the switch target because it removes econ20's two eco6_t5 losses on the development scenarios;
          the fx1c losses of econ20 as our target include eco6_t5 asym:3:2 seat 1 (-790). No wall-clock cutoff.
"""
from __future__ import annotations

from bot_research.bots.counters.snapshots.v23_candidate_001 import v20
from bot_research.harness.match import resolve_spec

FOREIGN21 = {
    "econ21": 'bot_research.bots.economy.frozen.v21.econ21:@make?free_fallback="zero"&foreign_attack_from=11'
              '&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400',
}


class Lead21(v20.Lead20):
    def __init__(self, foreign_target=None, **params):
        new = foreign_target in FOREIGN21
        super().__init__(foreign_target=None if new else foreign_target, **params)
        if new and self.foreign_policy is None:
            raise ValueError(f"foreign_target {foreign_target!r} needs foreign_policy")
        self.target21 = foreign_target if new else None

    def __call__(self, obs):
        if self.target21 is not None and self.alt is None and self._foreign(obs):
            self.alt = resolve_spec(FOREIGN21[self.target21])
            self.switch_round = obs["round"]
        return super().__call__(obs)


def make(**params):
    return Lead21(**params)
