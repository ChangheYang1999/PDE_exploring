"""Measure the threat-sampling gap: for opponent gold G where the exhaustive set of ordered purchase lists is
too large for the planner (G > ~175), plan a zero-leak defence against the SAMPLED compositions, then check it
by exact simulation against EVERY ordered list (enumerated here, up to a cap) from several positions.
Reports how many lists leak and the worst leaked damage. Writes bot_research/runs/defense/sampling_gap.txt."""
import copy
import time

from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.bots.defense import plan as P
from bot_research.bots.defense.simulate import simulate_leak
from bot_research.harness import gamekit as gk


def main():
    base = Engine(balanced_config(), ("A", "B")).observation(0)
    rules = gk.Rules.from_observation(base)
    out = []
    positions = {
        "empty map, own gold 400": ([], 400),
        "stage-A walls, own gold 600": ([{"x": a["x"], "y": a["y"], "type": "wall"} for a in P.plan_walls(base, 100, stage=0)], 600),
        "stage-A + splash(10,1)+gun3(1,3), own gold 800": ([{"x": a["x"], "y": a["y"], "type": "wall"} for a in P.plan_walls(base, 100, stage=0)]
                                                           + [{"x": 10, "y": 1, "type": "splash"}, {"x": 1, "y": 3, "type": "gun3"}], 800),
    }
    for G in (200, 250, 300):
        lists = P.exhaustive_bundles(G, rules, 100000)
        for name, (buildings, own_gold) in positions.items():
            o = copy.deepcopy(base)
            o["players"][0]["buildings"] = list(buildings)
            o["players"][0]["gold"] = own_gold
            o["players"][1]["gold"] = G
            P.EXHAUSTIVE_MAX = 400
            comps = P.threat_compositions(o)
            t = time.time()
            acts = P.plan_defense(o, own_gold, threat_types=comps, partial="none")
            dt = time.time() - t
            if not acts:
                out.append(f"G={G} {name}: no zero-leak plan within budget ({len(comps)} sampled comps, {dt:.1f}s)")
                continue
            b = list(buildings) + [{"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]} for a in acts]
            cost = sum(1 if a["op"] == "build_wall" else rules.turrets[a["type"]]["cost"] for a in acts)
            path = gk.route_cached({(x["x"], x["y"]) for x in b})
            profile = gk.splash_profile(path, b, rules)
            guns = gk.gun_coverage(path, b, rules)
            leaks, worst = 0, 0
            for lst in lists:
                h, d, lhp = simulate_leak(lst, path, b, rules, profile=profile, guns=guns)
                if h:
                    leaks += 1
                    worst = max(worst, d)
            out.append(f"G={G} {name}: plan cost {cost} ({len(comps)} sampled comps, {dt:.1f}s); exhaustive {len(lists)} lists -> {leaks} leak, worst dmg {worst}")
            print(out[-1])
    open("bot_research/runs/defense/sampling_gap.txt", "w").write("\n".join(out))


if __name__ == "__main__":
    main()
