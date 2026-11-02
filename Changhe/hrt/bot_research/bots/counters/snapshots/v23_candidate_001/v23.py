"""Lead v23 development bot: v22 with the joint early plan (v18's mid_joint) only against a covering turret.

v22, v21, v20, v19 and v18 are imported unmodified. mid_relevant (default False = v22): before each decision the
configured mid_joint is kept only if the opponent owns a turret that covers its own route (v15's _covering_turret:
a splash next to a route cell or a gun in range of one) or its visible roster holds a tier1/tier2 entry bought in
round 2 or later (the roster part of poke_reactive); otherwise mid_joint is None for that round and Base18 skips
the joint plan. v20's mid_level test still applies on top. The poke fallback and the other rules keep
poke_reactive="turret" (any turret).
Reason (2026-10-31T11:34Z, runs/lead/c9h log 00059, tmp/replay_obs.py): against hrt-w3's feature_bluff turret_round=1
(one gun1 at (0,11), off its route, then factories and tier5 from round 7) V17 wins +595 and V20T loses -980 at
round 9 in both seats. The off-route gun1 satisfies poke_reactive="turret", so the joint plan bought a splash in
round 2 and two gun1 in round 3; our economy stayed behind the opponent's and its tier5 floods won. The opponent
that the joint plan was added for, budget_timing (tier3, attack_round 3, budget_fraction 0.5), covers its own
route with its round-1 turret.
"""
from __future__ import annotations

from bot_research.bots.counters.snapshots.v23_candidate_001 import v22
from bot_research.bots.counters.snapshots.v23_candidate_001.v15 import _covering_turret
from bot_research.harness import gamekit as gk


class Lead23(v22.Lead22):
    def __init__(self, mid_relevant=False, **params):
        super().__init__(**params)
        self.mid_relevant = mid_relevant
        self.mid_joint0 = self.mid_joint
        self.relevant_skips = []

    def __call__(self, obs):
        if self.mid_relevant and self.mid_joint0 is not None and obs["round"] >= 2:
            rules = gk.Rules.from_observation(obs)
            opp = obs["players"][1 - obs["player"]]
            ok = _covering_turret(opp["buildings"], rules) or any(
                e["bought_round"] >= 2 and rules.minions[e["type"]]["hp"] <= 70 for e in opp["roster"])
            self.mid_joint = self.mid_joint0 if ok else None
            self.base.mid_joint = self.mid_joint
            if not ok:
                self.relevant_skips.append(obs["round"])
        return super().__call__(obs)


def make(**params):
    return Lead23(**params)
