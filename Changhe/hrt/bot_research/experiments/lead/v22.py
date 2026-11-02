"""Lead v22 development bot: v21 with an optional round-1 gun1 in place of one stage-A wall.

v21, v20, v19 and v18 are imported unmodified. r1_gun (a cell [x, y] or None, default None = v21): in round 1, if
the actions of v21 contain a wall at that cell, the wall is replaced by a gun1 at the same cell, the tier1 poke is
cut to r1_gun_poke copies (default 2) and the gold left buys factories as before (at most max_factories). A turret
blocks movement like a wall, so the route and the later layout walls are unchanged (plan_walls skips occupied
cells), and the cell stays in the set of cells we asked to build (v16's foreign-map test).
Reason (2026-10-31T11:29Z, tmp/r1gun/exchange.py, exact round 1 on the unchanged engine): v21 spends 20 + 45 + 20 = 85 of the
100 starting gold in round 1 (20 walls, three tier1, one factory) and has no turret, so a blind round-1 poke
deals 5 per tier1 and 12 per tier2 (guard_geometry [t1,t1] -10, hrt-w3's GuardedForecast 800:795 to 800:778,
hrt-w1's "blind round 1" -5 to -15). One gun1 at any middle cell of row 1 or row 3 (for example (4,1)) covers
the route twice and stops one to six tier1 and one tier2 completely; with two tier1 the round-1 spend is
19 + 30 + 30 + 20 = 99, the same one factory. Against the round-1 actions of the f5t, TARGETED2 and TARGETED3
opponents (both seats, tmp/r1gun/pool_exchange.txt) the round-1 exchange changes from 1270 dealt / 748 taken to
800 dealt / 72 taken; the dealt loss is 5 per opponent without a round-1 turret.
"""
from __future__ import annotations

from bot_research.experiments.lead import v21
from bot_research.harness import gamekit as gk


class Lead22(v21.Lead21):
    def __init__(self, r1_gun=None, r1_gun_poke=2, **params):
        super().__init__(**params)
        self.r1_gun = None if r1_gun is None else tuple(r1_gun)
        self.r1_gun_poke = r1_gun_poke
        self.r1_gun_used = False

    def __call__(self, obs):
        actions = super().__call__(obs)
        if obs["round"] != 1 or self.r1_gun is None or self.alt is not None:
            return actions
        x, y = self.r1_gun
        walls = [a for a in actions if a["op"] == "build_wall"]
        if not any((a["x"], a["y"]) == (x, y) for a in walls):
            return actions
        rules = gk.Rules.from_observation(obs)
        p = self.base.p
        out = [a for a in walls if (a["x"], a["y"]) != (x, y)]
        out.append({"op": "build_turret", "type": "gun1", "x": x, "y": y})
        left = obs["players"][obs["player"]]["gold"] - rules.wall_cost * len(out[:-1]) - rules.turrets["gun1"]["cost"]
        if left < 0:
            return actions
        c = rules.minions["tier1"]["cost"]
        n = max(0, min(self.r1_gun_poke, left // c))
        out += [{"op": "buy_minion", "type": "tier1"}] * n
        left -= n * c
        if obs["round"] <= p["last_factory_round"]:
            out += [{"op": "buy_factory"}] * max(0, min(p["max_factories"], left // rules.factory_cost))
        self.r1_gun_used = True
        return out


def make(**params):
    return Lead22(**params)
