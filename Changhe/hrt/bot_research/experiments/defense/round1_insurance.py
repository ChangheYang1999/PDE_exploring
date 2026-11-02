"""Round-1 insurance: what blind round-1 defences cost and what they save against each round-1 rush.

Round-1 actions are simultaneous and blind. For each defence option D (nothing; splash at (10,1); 20 walls +
gun2 at (9,5) = the planner's zero-leak plan; 20 walls + splash at the pillar) and each rush R affordable
with 100 gold (tier1 x6, tier2 x2, tier3, tier2 + tier1 x4, tier1 x3 + tier2), simulate round 1 exactly
(engine replica) and report HP lost and bounty gold given to the attacker; plus the eco cost of the option
(gold not put into factories in round 1 = 0.75 x cost income per round).
Writes bot_research/runs/defense/round1_insurance.txt.
"""
from bot_research.bots.defense import plan as P
from bot_research.bots.defense.simulate import simulate_leak
from bot_research.harness import gamekit as gk
from td_game.config import balanced_config
from td_game.engine import Engine


def main():
    obs = Engine(balanced_config(), ("A", "B")).observation(0)
    rules = gk.Rules.from_observation(obs)
    walls20 = [(a["x"], a["y"]) for a in P.plan_walls(obs, 100, stage=0)]
    options = {
        "nothing": [],
        "splash (10,1) [60]": [{"x": 10, "y": 1, "type": "splash"}],
        "gun2 (10,1) [80]": [{"x": 10, "y": 1, "type": "gun2"}],
        "20 walls + splash (10,1) [80]": [{"x": x, "y": y, "type": "wall"} for x, y in walls20] + [{"x": 10, "y": 1, "type": "splash"}],
        "20 walls + gun2 (9,5) [100]": [{"x": x, "y": y, "type": "wall"} for x, y in walls20] + [{"x": 9, "y": 5, "type": "gun2"}],
    }
    rushes = {"tier1 x6 [90]": ["tier1"] * 6, "tier2 x2 [80]": ["tier2"] * 2, "tier3 [100]": ["tier3"],
              "tier2 + tier1 x4 [100]": ["tier2"] + ["tier1"] * 4, "tier1 x3 + tier2 [85]": ["tier1"] * 3 + ["tier2"],
              "tier1 x2 + tier2 + tier1 [85]": ["tier1", "tier1", "tier2", "tier1"]}
    out = ["option | " + " | ".join(rushes) + "   (HP lost / bounty gold to attacker)"]
    for name, b in options.items():
        path = gk.route_cached({(x["x"], x["y"]) for x in b})
        row = []
        for rname, types in rushes.items():
            h, d, lhp = simulate_leak(types, path, b, rules)
            row.append(f"{d}/{5*h}")
        out.append(f"{name} | " + " | ".join(row) + f"  route {len(path)-1}")
    text = "\n".join(out)
    print(text)
    open("bot_research/runs/defense/round1_insurance.txt", "w").write(text)


if __name__ == "__main__":
    main()
