"""Q2: cheapest defences from the empty map (initial position, round 1) found by the planner.

(a) splash-only plans reaching per-copy splash damage >= 20, 70, 180, 560, 1500 (stream-independent);
(b) threat plans (guns allowed, exact simulation) for n copies of each tier, n in 1, 2, 4, 8, 16, 32;
(c) the same from the stage-A position (20 walls + nothing else) to show the effect of the maze.
Writes bot_research/runs/defense/q2_cheapest.txt. Run from the project root:
  .venv/bin/python -B -m bot_research.experiments.defense.q2_cheapest
"""
import time

from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.bots.defense import plan as P
from bot_research.bots.defense.geometry import render
from bot_research.harness import gamekit as gk

COST = {"wall": 1, "splash": 60, "gun1": 30, "gun2": 80, "gun3": 200}


def cost_of(acts):
    return sum(1 if a["op"] == "build_wall" else COST[a["type"]] for a in acts)


def summary(acts):
    from collections import Counter
    c = Counter("wall" if a["op"] == "build_wall" else a["type"] for a in acts)
    return dict(c)


def main():
    import sys
    layout_name = sys.argv[1] if len(sys.argv) > 1 else "default"
    layout = P.layout_by_name(layout_name)
    out = [f"layout: {layout_name}"]
    eng = Engine(balanced_config(), ("A", "B"))
    base = eng.observation(0)
    rules = gk.Rules.from_observation(base)
    for label, pre in (("empty map", []), ("stage-A walls built", P.plan_walls(dict(base, players=[dict(base["players"][0], gold=10**6), base["players"][1]]), 10**6, layout=layout, stage=0))):
        obs = dict(base)
        me = dict(base["players"][0])
        me["buildings"] = [{"x": a["x"], "y": a["y"], "type": "wall"} for a in pre]
        me["gold"] = 10 ** 6
        obs["players"] = [me, base["players"][1]]
        out.append(f"===== start: {label} ({len(pre)} walls already placed, not counted below)")
        out.append("(a) splash-only, per-copy splash damage >= HP")
        for hp in (20, 70, 180, 560, 1500):
            t = time.time()
            acts = P.plan_defense(obs, 10 ** 6, required_hp=hp, allow_guns=False, layout=layout)
            me2, _, b, blocked = P.observe(obs)
            for a in acts:
                b.append({"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]}); blocked.add((a["x"], a["y"]))
            dmg = P.splash_damage(b, rules, blocked)
            L = len(gk.route_cached(blocked)) - 1
            out.append(f"  HP>={hp:5d}: cost={cost_of(acts):5d} {summary(acts)} -> splash dmg/copy={dmg} route={L} ({time.time()-t:.1f}s)")
        out.append("(b) threat plans with guns (zero simulated leaks), n copies of one tier")
        for tier in ("tier1", "tier2", "tier3", "tier4", "tier5"):
            row = []
            for n in (1, 2, 4, 8, 16, 32):
                t = time.time()
                acts = P.plan_defense(obs, 10 ** 6, threat_types=[[tier] * n], partial="none", layout=layout)
                row.append(f"n={n}:{cost_of(acts)}" if acts else f"n={n}:0")
            out.append(f"  {tier}: " + "  ".join(row))
        out.append("(b') detail for tier5 n=1,4,16: buildings")
        for n in (1, 4, 16):
            acts = P.plan_defense(obs, 10 ** 6, threat_types=[["tier5"] * n], partial="none", layout=layout)
            out.append(f"  tier5 x{n}: cost={cost_of(acts)} {summary(acts)} turrets={[a['type']+str((a['x'],a['y'])) for a in acts if a['op']=='build_turret']}")
        out.append("")
    text = "\n".join(out)
    print(text)
    open(f"bot_research/runs/defense/q2_cheapest_{layout_name}.txt", "w").write(text)


if __name__ == "__main__":
    main()
