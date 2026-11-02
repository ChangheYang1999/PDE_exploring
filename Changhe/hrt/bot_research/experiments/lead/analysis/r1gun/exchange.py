"""Exact round-1 exchange (unchanged engine): our walls with a gun1 replacing one stage-A wall, against rushes."""
import itertools, sys
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.defense.frozen.v7 import plan as P

LAY = P.layout_by_name("default")
RUSHES = {f"t1x{k}": ["tier1"] * k for k in range(1, 7)}
RUSHES.update({"t2": ["tier2"], "t2x2": ["tier2"] * 2, "t2+t1x2": ["tier2"] + ["tier1"] * 2,
               "t2+t1x4": ["tier2"] + ["tier1"] * 4, "t3": ["tier3"]})


def walls():
    e = Engine(balanced_config(), ("a", "b"))
    return P.plan_walls(e.observation(0), 100, layout=LAY, stage=0)


def damage(ours, rush):
    e = Engine(balanced_config(), ("a", "b"))
    opp = [{"op": "buy_minion", "type": t} for t in rush]
    e.play_round([ours, opp])
    return 800 - e.players[0].hp


W = walls()
cells = [(a["x"], a["y"]) for a in W]
res = []
base = {n: damage(W, r) for n, r in RUSHES.items()}
print("walls only", base)
for c in cells + [(10, 1), (1, 3)]:
    ours = [a for a in W if (a["x"], a["y"]) != c] + [{"op": "build_turret", "type": "gun1", "x": c[0], "y": c[1]}]
    d = {n: damage(ours, r) for n, r in RUSHES.items()}
    res.append((sum(d.values()), c, d))
res.sort()
for s, c, d in res[:8]:
    print(c, s, d)
