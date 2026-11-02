"""Self-checks for bot_research/bots/defense (exactness and legality), against the unchanged engine.

1. simulate_leak (planning sim) == td_game.combat.simulate_map on random buildings/rosters (hits, damage).
2. plan_defense zero-leak plans really give zero hits in the engine for every threat composition,
   all actions are accepted by td_game.actions.apply_action, and total cost <= budget.
Run: .venv/bin/python -B -m bot_research.experiments.defense.check_plan [n_cases]
"""
import random
import sys
import time

from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import Building, PlayerState, RosterEntry

from bot_research.bots.defense import plan as P
from bot_research.bots.defense.simulate import simulate_leak
from bot_research.harness import gamekit as gk

TYPES = ["tier1", "tier2", "tier3", "tier4", "tier5"]
TURRETS = ["wall", "wall", "wall", "splash", "gun1", "gun2", "gun3"]


def random_buildings(rnd, n):
    blocked, out = set(), []
    for _ in range(n):
        c = (rnd.randrange(12), rnd.randrange(12))
        if gk.legal_build(blocked, c):
            kind = rnd.choice(TURRETS)
            blocked.add(c)
            out.append({"x": c[0], "y": c[1], "type": kind})
    return out


def engine_sim(types, buildings, cfg):
    att = PlayerState("A", 800, 0, roster=[RosterEntry(i, t, 1, None) for i, t in enumerate(types)])
    dfn = PlayerState("D", 10 ** 9, 0, buildings=[Building(b["x"], b["y"], b["type"]) for b in buildings])
    path = gk.route({(b["x"], b["y"]) for b in buildings})
    tot = simulate_map(att, dfn, path, 1, cfg)
    return tot.hits, tot.damage


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    cfg = balanced_config()
    eng = Engine(cfg, ("A", "B"))
    obs0 = eng.observation(0)
    rules = gk.Rules.from_observation(obs0)
    rnd = random.Random(12345)
    t = time.time()
    mism = 0
    for i in range(n):
        b = random_buildings(rnd, rnd.randrange(0, 40))
        types = [rnd.choice(TYPES) for _ in range(rnd.randrange(1, 40))]
        if rnd.random() < 0.1:
            types += ["tier1"] * rnd.randrange(200, 300)
        path = gk.route({(x["x"], x["y"]) for x in b})
        h, d, lhp = simulate_leak(types, path, b, rules)
        eh, ed = engine_sim(types, b, cfg)
        if (h, d) != (eh, ed):
            mism += 1
            print("MISMATCH", i, (h, d), (eh, ed))
    print(f"[1] simulate_leak vs engine: {n} cases, {mism} mismatches, {time.time()-t:.1f}s")
    # 2. planner guarantees
    t = time.time()
    fails = 0
    checked = 0
    for i in range(n // 4):
        obs = eng.observation(0)
        me = obs["players"][0]
        me["buildings"] = random_buildings(rnd, rnd.randrange(0, 25))
        me["gold"] = rnd.choice([100, 300, 1000, 3000, 10000])
        opp = obs["players"][1]
        opp["gold"] = rnd.choice([0, 100, 300, 700, 1500, 3000])
        opp["roster"] = [{"id": k, "type": rnd.choice(TYPES), "bought_round": 1, "expires_after_round": 12, "remaining_rounds": 11}
                         for k in range(rnd.randrange(0, 8))]
        obs["round"] = 1
        comps = P.threat_compositions(obs)
        if not comps:
            continue
        acts = P.plan_defense(obs, me["gold"], threat_types=comps, partial="none")
        if not acts:
            # either already zero-leak or unaffordable: verify the former claim when planner says []
            continue
        checked += 1
        # legality and cost via the engine's own action validation on a fresh state
        ps = PlayerState("D", 800, me["gold"], buildings=[Building(x["x"], x["y"], x["type"]) for x in me["buildings"]])
        cost = 0
        for a in acts:
            ev = apply_action(ps, a, 1, cfg)
            if not ev["accepted"]:
                fails += 1
                print("REJECTED", a, ev["reason"])
            else:
                cost += ev["cost"]
        if cost > me["gold"]:
            fails += 1
            print("OVER BUDGET", cost, me["gold"])
        bl = [{"x": x.x, "y": x.y, "type": x.type} for x in ps.buildings]
        for types in comps:
            eh, ed = engine_sim(types, bl, cfg)
            if eh != 0:
                fails += 1
                print("LEAK after plan", types[:5], len(types), eh, ed)
    print(f"[2] planner zero-leak plans checked in engine: {checked} plans, {fails} failures, {time.time()-t:.1f}s")
    return 1 if (mism or fails) else 0


if __name__ == "__main__":
    raise SystemExit(main())
