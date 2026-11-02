"""Sampling gap at medium gold: local search over purchase ORDERS against the planner's zero-leak plans.

For opponent gold G in (400, 700, 1000, 1500) and several own positions, plan a zero-leak defence against the
sampled compositions (threat_compositions), then try to find an ordered purchase list of cost <= G that leaks:
(a) every multiset reachable greedily is not enumerable, so we take the multisets of the sampled bundles plus
random multisets, and for each run a hill climb over orders (adjacent swaps, random moves) maximising leaked
base damage (exact simulation). Reports the worst leak found per position. Writes
bot_research/runs/defense/order_search.txt.
"""
import copy
import random
import time

from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.bots.defense import plan as P
from bot_research.bots.defense.simulate import simulate_leak
from bot_research.harness import gamekit as gk

TIERS = ["tier1", "tier2", "tier3", "tier4", "tier5"]


def random_multiset(rnd, gold, costs):
    out, g = [], gold
    while True:
        aff = [t for t in TIERS if costs[t] <= g]
        if not aff or rnd.random() < 0.08:
            break
        t = rnd.choice(aff)
        out.append(t)
        g -= costs[t]
    return out


def leak_of(order, path, buildings, rules, profile, guns):
    h, d, lhp = simulate_leak(order, path, buildings, rules, profile=profile, guns=guns)
    return d


def hill_climb(order, rnd, evalf, iters=150):
    cur = list(order)
    best_v = evalf(cur)
    for _ in range(iters):
        trial = list(cur)
        if len(trial) >= 2:
            if rnd.random() < 0.5:
                i = rnd.randrange(len(trial) - 1)
                trial[i], trial[i + 1] = trial[i + 1], trial[i]
            else:
                i, j = rnd.randrange(len(trial)), rnd.randrange(len(trial))
                trial.insert(j, trial.pop(i))
        v = evalf(trial)
        if v >= best_v:
            cur, best_v = trial, v
    return best_v, cur


def main():
    base = Engine(balanced_config(), ("A", "B")).observation(0)
    rules = gk.Rules.from_observation(base)
    costs = {t: rules.minions[t]["cost"] for t in TIERS}
    rnd = random.Random(7)
    out = []
    stage_a = [{"x": a["x"], "y": a["y"], "type": "wall"} for a in P.plan_walls(base, 100, stage=0)]
    positions = {"stage A, own gold 1000": (stage_a, 1000), "stage A + splash(10,1) + gun3(1,3), own gold 1500":
                 (stage_a + [{"x": 10, "y": 1, "type": "splash"}, {"x": 1, "y": 3, "type": "gun3"}], 1500)}
    for G in (400, 700, 1000, 1500):
        for name, (buildings, own) in positions.items():
            o = copy.deepcopy(base)
            o["players"][0]["buildings"] = list(buildings)
            o["players"][0]["gold"] = own
            o["players"][1]["gold"] = G
            comps = P.threat_compositions(o)
            t = time.time()
            acts = P.plan_defense(o, own, threat_types=comps, partial="none")
            if not acts:
                out.append(f"G={G} {name}: no zero-leak plan within budget ({time.time()-t:.1f}s)")
                print(out[-1])
                continue
            b = list(buildings) + [{"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]} for a in acts]
            cost = sum(1 if a["op"] == "build_wall" else rules.turrets[a["type"]]["cost"] for a in acts)
            path = gk.route_cached({(x["x"], x["y"]) for x in b})
            profile = gk.splash_profile(path, b, rules)
            guns = gk.gun_coverage(path, b, rules)
            evalf = lambda order: leak_of(order, path, b, rules, profile, guns)
            multisets = [list(c) for c in comps] + [random_multiset(rnd, G, costs) for _ in range(12)]
            worst, worst_order, n_eval = 0, None, 0
            for ms in multisets:
                if not ms:
                    continue
                v, order = hill_climb(ms, rnd, evalf, iters=120)
                n_eval += 121
                if v > worst:
                    worst, worst_order = v, order
            out.append(f"G={G} {name}: plan cost {cost} ({len(comps)} comps, {time.time()-t:.1f}s); order search over {len(multisets)} multisets x 121 evals -> worst leaked damage {worst} {('order ' + ''.join(x[-1] for x in worst_order)) if worst_order else ''}")
            print(out[-1])
    open("bot_research/runs/defense/order_search.txt", "w").write("\n".join(out))


if __name__ == "__main__":
    main()
