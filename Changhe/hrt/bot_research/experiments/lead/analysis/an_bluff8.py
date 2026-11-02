from bot_research.experiments.lead.obs_at import observation_at
from bot_research.bots import best
from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.harness import gamekit as gk
import sys
opp = 'bot_research.bots.counters.feature_bluff:@make?turret_round=3'
for rnd in (7, 8):
    obs = observation_at('bot_research.bots.best:@make', opp, rnd, 0)
    me, op = obs["players"][0], obs["players"][1]
    print("round", rnd, "my gold", me["gold"], "opp gold", op["gold"], "opp roster", [(e["type"], e["bought_round"]) for e in op["roster"]])
    comps = P.threat_compositions(obs)
    print(" n comps", len(comps), "sizes", sorted({len(c) for c in comps}))
    for c in comps[:12]:
        from collections import Counter
        print("  ", dict(Counter(c)))
    rules = gk.Rules.from_observation(obs)
    print(" worst leak", best._worst_leak(obs, rules, comps))
    b = best.make()
    acts = b(obs)
    from collections import Counter
    print(" actions", Counter(a.get("type", a["op"]) for a in acts))
    full = P.plan_defense(obs, 10**6, threat_types=comps, layout=b.layout, partial="none", allow_guns=False)
    print(" zero-leak splash-only cost (unlimited)", best._cost_of(full, rules), Counter(a.get("type", a["op"]) for a in full))
    full2 = P.plan_defense(obs, me["gold"], threat_types=comps, layout=b.layout, partial="best", allow_guns=max(len(c) for c in comps) <= 120)
    print(" best partial within gold", best._cost_of(full2, rules), Counter(a.get("type", a["op"]) for a in full2))
