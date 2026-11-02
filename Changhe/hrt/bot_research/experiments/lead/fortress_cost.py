"""Cheapest zero-leak plan the frozen v7 planner finds on the empty default-layout map against
1 tier5, 1 tier4 and 4 tier5, with and without guns (defense_cost; exact simulation)."""
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.harness import gamekit as gk
e = Engine(balanced_config(), ("A", "B"))
obs = e.observation(0)
rules = gk.Rules.from_observation(obs)
print("wall cost", rules.wall_cost, "splash", rules.turrets["splash"]["cost"])
lay = P.layout_by_name("default")
for t in (["tier5"], ["tier4"], ["tier5"] * 4):
    print(t[:1], len(t), "splash-only", P.defense_cost(obs, [t], allow_guns=False, layout=lay),
          "with guns", P.defense_cost(obs, [t], allow_guns=True, layout=lay))
