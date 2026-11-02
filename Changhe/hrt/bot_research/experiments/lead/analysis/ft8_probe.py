"""Loss review of c8m log 00019 (V17 vs forecast_timing r8 tier5): plans available in round 8 (development only)."""
import pickle, time
from bot_research.experiments.lead.obs_at import observation_at
from bot_research.experiments.lead import v15
from bot_research.harness import gamekit as gk
from bot_research.harness.match import resolve_spec

A = ('bot_research.experiments.lead.v17:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3'
     '&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5')
B = 'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0'
for rnd in (7, 8):
    obs = observation_at(A, B, rnd, 0)
    pickle.dump(obs, open(f"bot_research/tmp/ft8_obs_r{rnd}.pkl", "wb"))
    bot = resolve_spec(A).base
    rules = gk.Rules.from_observation(obs)
    me = obs["players"][0]
    walls = bot.P.plan_walls(obs, me["gold"], layout=bot.layout, stage=0)
    left = me["gold"] - v15._cost_of(walls, rules)
    o2 = v15._with_buildings(obs, walls, left)
    comps = bot.P.threat_compositions(obs)
    print("round", rnd, "gold", me["gold"], "walls", len(walls), "left", left, "opp gold", obs["players"][1]["gold"],
          "ncomps", len(comps), "max copies", max(len(c) for c in comps), "worst", v15._worst_leak(o2, rules, comps))
    for name, kw in (("splash partial", dict(partial="best", allow_guns=False)),
                     ("guns zero", dict(partial="none")), ("guns partial", dict(partial="best"))):
        t = time.time()
        plan = bot.P.plan_defense(o2, left, threat_types=comps, layout=bot.layout, **kw)
        o3 = v15._with_buildings(o2, plan, left - v15._cost_of(plan, rules))
        print(f"  {name:15s} cost {v15._cost_of(plan, rules):4d} n {len(plan):2d} worst after {v15._worst_leak(o3, rules, comps):4d}"
              f" {sorted(set((a['op'], a.get('type')) for a in plan))} {time.time()-t:.1f}s")
