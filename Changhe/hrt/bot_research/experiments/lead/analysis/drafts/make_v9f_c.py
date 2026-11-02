"""Build the best_v9f candidate V33C = P5TNUBM plus the capped passive plan: best_v9f_P5TNUBM.py (make_v9f_m.py) with
the three code edits that turn experiments/lead/v30.py into v33.py, the default passive_cheap_from=3 and the rule
text. Usage: python3 make_v9f_c.py"""
from pathlib import Path

D = Path(__file__).parent


def rep(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)


s = (D / "best_v9f_P5TNUBM.py").read_text()
old_par = '    passive_mid_from=5,     # rule 3a against tier1-tier3 rosters only, in passive rounds from this round (None: off)\n'
s = rep(s, old_par, old_par +
        '    passive_cheap_from=3,  # rule 3a against tier1-tier2 rosters, capped, in passive rounds from this round (None: off)\n'
        '    passive_cheap_hp=70,   # ... largest minion HP in those rosters\n'
        '    passive_cheap_cap=60,  # ... gold cap of that plan\n')
s = rep(s, '''            passive_mid = passive and p["passive_mid_from"] is not None and rnd >= p["passive_mid_from"]
            if passive_mid:
                comps = [c for c in P.threat_compositions(obs) if all(rules.minions[t]["hp"] <= p["mid_hp"] for t in c)]
''', '''            passive_mid = passive and p["passive_mid_from"] is not None and rnd >= p["passive_mid_from"]
            passive_cheap = passive and not passive_mid and p["passive_cheap_from"] is not None \\
                and rnd >= p["passive_cheap_from"]
            budget = int(left * p["spec_share"])
            if passive_mid:
                comps = [c for c in P.threat_compositions(obs) if all(rules.minions[t]["hp"] <= p["mid_hp"] for t in c)]
            elif passive_cheap:
                comps = [c for c in P.threat_compositions(obs)
                         if all(rules.minions[t]["hp"] <= p["passive_cheap_hp"] for t in c)]
                budget = min(budget, p["passive_cheap_cap"])
                passive_mid = True  # rules 3b to 3d stay off, as in passive_mid rounds
''')
s = rep(s, '''                spec = self._plan(o2, int(left * p["spec_share"]), threat_types=comps, layout=layout,
                                  partial="none", **ins)
                if not spec and not passive_mid and p["big_threat"]''', '''                spec = self._plan(o2, budget, threat_types=comps, layout=layout,
                                  partial="none", **ins)
                if not spec and not passive_mid and p["big_threat"]''')
s = rep(s, "   the tier5 part of the insurance is the expensive part the passive rule skips.)\n",
        """   the tier5 part of the insurance is the expensive part the passive rule skips.)
   In the rounds of that window from ``passive_cheap_from`` (3) up to round ``passive_mid_from``,
   rule a alone runs against the listed rosters made only of types with at most ``passive_cheap_hp``
   (70) HP, i.e. tier1 and tier2, and buys their zero-leak plan only if it costs at most
   ``passive_cheap_cap`` (60) gold and at most ``spec_share`` of the remaining gold; b to d stay off.
   (Development reason: without it, budget strikes with tier1 or tier2 in rounds 3 and 4 and hrt-w1's
   fortress v32, which buys one tier2 in round 4, beat the bot by 7 to 50 where best_v9e draws or wins;
   the full rule a against tier1 to tier3 from round 3 or 4 lost grower counters by up to 1075. The
   cap of 60 is one splash; with 30 the planner found no plan in those games.)
""")
s = rep(s, '&passive_mid_from=5``', '&passive_mid_from=5&passive_cheap_from=3``')
s = s.replace("bot_research.experiments.lead.v30:@make?passive_until=5", "bot_research.experiments.lead.v33:@make?passive_until=5")
(D / "best_v9f_V33C.py").write_text(s)
print("V33C written")
