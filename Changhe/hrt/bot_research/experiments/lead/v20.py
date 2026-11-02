"""Lead v20 development bot: v19 with the joint early plan (v18's mid_joint) only while not behind.

v19 and v18 are imported unmodified. mid_level (default False): before each decision, v18's Base18 instance gets
mid_joint = the configured value if our HP is at least the opponent's, and None otherwise (Base18 skips the joint
plan when mid_joint is None). With mid_level=false it plays as v19.
Reason (2026-10-31T10:44Z, runs/lead/t8e log 00037): with mid_joint=0.75 and catch_up, against guard_geometry [tier1] (we are
5 HP behind after round 1) the joint plan bought two gun1 in round 2 and a gun1 in round 3 and the catch-up attack
a tier2 in round 4; with 9 factories at rounds 5-9 against the opponent's 24-89 the big-threat insurance took all
our gold, and the opponent locked at round 10 and flooded from round 11 (-973, round 13). Without mid_joint V17 lost
that game by 5. By P2 a mutual lock freezes the HP difference, so while behind the early gold is worth more as
economy and catch-up attacks than as insurance against mid-tier rosters; while level or ahead, a lock keeps the
result, which is the case of hrt-w3's budget_timing tier3 r3 0.5 (repaired by mid_joint, -26 to 0).
"""
from __future__ import annotations

from bot_research.experiments.lead import v18, v19


class Lead20(v19.Lead19):
    def __init__(self, mid_level=False, **params):
        super().__init__(**params)
        self.mid_level = mid_level
        if mid_level and not isinstance(self.base, v18.Base18):
            raise ValueError("mid_level needs mid_joint")
        self.level_skips = []

    def __call__(self, obs):
        if self.mid_level:
            me, opp = obs["players"][obs["player"]], obs["players"][1 - obs["player"]]
            ok = me["hp"] >= opp["hp"]
            self.base.mid_joint = self.mid_joint if ok else None
            if not ok:
                self.level_skips.append(obs["round"])
        return super().__call__(obs)


def make(**params):
    return Lead20(**params)
