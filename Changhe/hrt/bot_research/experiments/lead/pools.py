"""Opponent pools used by the lead's tuning tournaments (TUNING set only).

The held-out validation pools are owned by hrt-w3 (experiments/validation/holdout_manifest.json)
and are not used here.
"""
import json
from urllib.parse import quote

ROSTERS = ((), ("tier1",), ("tier1", "tier1"), ("tier2",), ("tier1", "tier1", "tier2"))


def _js(roster):
    return json.dumps(list(roster), separators=(",", ":"))


B = "bot_research.harness.baselines:"
C = "bot_research.bots.counters.pool:"

BASELINES = [
    "td_bots.protocol:idle",
    B + "@greedy_eco",
    B + '@rush?tier="tier1"',
    B + '@rush?tier="tier3"',
    B + "@eco_then_flood?switch=8",
    B + "@splash_turtle",
    B + "@gun_turtle",
    B + "@maze_eco",
    B + "@random_legal?seed=1",
    B + "@threat_defender",
]
ARCHETYPES = [C + f'@archetype?name="{n}"' for n in (
    "rush_t1", "rush_t2", "rush_t3", "heavy_t4", "eco3_t1", "eco5_t1", "eco5_t3", "eco6_t5",
    "splash_t2", "splash3_t4", "gun_t3", "mixed5")]
POOL_EXTRA = [C + '@turtle?kind="splash"', C + '@turtle?kind="gun1"', C + "@stacker", C + "@mirror",
              C + "@random_legal", C + "@rush_t5"]
TUNING = BASELINES + ARCHETYPES + POOL_EXTRA

# Development opponents from the lead's frozen versions and the worker lanes (also tuning, not validation).
F = "bot_research.experiments.lead.frozen."
K = "bot_research.bots.counters."
STRONG = [
    F + "best_v1:@make",
    F + "best_v1:@make?kappa=8",
    F + "best_v2:@make",
    "bot_research.bots.economy.econ:@make",
    "bot_research.bots.economy.frozen.v2.econ:@make",
    "bot_research.bots.economy.timing:@make",
    "bot_research.bots.defense.fortress:@make",
    K + "posterior_response:@make",
    K + "switching:@make",
    K + "maze_pressure:@make",
    K + "forecast_lock:@make?opening_units=2&reserve=180&saturate_round=20",
    K + "poke_lock:@make",
    K + "predicted_pressure:@make",
]

# Frontier set (cycle 3): the strongest frozen bots of every lane and the counters that beat lead versions.
E = "bot_research.bots.economy.frozen."
D = "bot_research.bots.defense.frozen."
FRONTIER = [
    F + "best_v3b:@make",
    F + "best_v2:@make",
    E + "v2.econ:@make",
    E + "v4.econ:@make",
    D + "v4.fortress:@make",
    D + "v4.fortress:@make?attack_from=6&attack_share=0.5",
    "bot_research.bots.economy.timing:@make",
    K + "forecast_lock_v3:@make?opening_units=2&reserve=0&saturate_round=20",
    K + "poke_lock:@make?opening_units=1&reserve=0&phi=1.0&saturate_round=20",
    C + '@archetype?name="eco6_t5"',
    B + "@eco_then_flood?switch=8",
    C + '@archetype?name="mixed5"',
]

# Frontier set 2 (cycle 4): current frozen worker bots, the lead prototype, and the newest hrt-w3 counters.
X = "bot_research.experiments.lead."
FRONTIER2 = [
    F + "best_v3b:@make",
    E + "v4.econ:@make",
    E + "v4.econ:@make?late_round=6&phi=0.0",
    D + "v7.fortress:@make",
    D + 'v7.fortress:@make?layout="annealed25"',
    D + "v7.fortress:@make?attack_from=6&attack_share=0.5",
    X + "v4proto:@fortress_poke?r1_poke=2&attack_from=6&attack_share=0.5",
    "bot_research.bots.economy.timing:@make",
    K + "poke_lock:@make?opening_units=1&reserve=0&phi=1.0&saturate_round=20",
    K + "forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0",
    K + 'known_policy:@timing?model="fortress_v4"&model_parameters={}&attack_round=1&tier="tier2"&count_cap=1&attack_share=1.0',
    C + '@archetype?name="eco6_t5"',
    C + '@archetype?name="mixed5"',
    B + "@eco_then_flood?switch=8",
    B + '@eco_then_flood?switch=12&tier="tier4"',
]

# FRONTIER2 plus the newest frozen worker bots (econ v8 of hrt-w2, fortress v11 of hrt-w1; both use
# planners with a 3 s wall-clock cutoff, so their actions can depend on machine load) and lead v4.
FRONTIER3 = FRONTIER2 + [
    E + "v8.econ8:@make",
    E + 'v8.econ8:@make?layout="lead_v3"',
    D + "v11.fortress:@make",
    D + 'v11.fortress:@make?layout="annealed25"',
    X + "v4:@make",
]

# FRONTIER3 plus the 04:30Z frozen worker bots (fortress v15, econ v9 and v10; timed planners) and hrt-w3's
# catalogue identifier with a one-way fortress13 fallback (beat the lead v4 snapshot 790:200).
FRONTIER4 = FRONTIER3 + [
    D + "v15.fortress:@make",
    E + "v9.econ9:@make",
    E + "v10.econ10:@make",
    K + 'falsification_fallback:@make?fallback="fortress13"&opening="factories"&saturate_round=12',
]

# FRONTIER4 plus the 05:30Z frozen worker bots (fortress v19 pool-strong and v20 forecast-robust, econ v13 and
# v15) and hrt-w3's newest development counters: the cheap round-1 guard with economy13, and the turret-feature
# bluff (off-route gun1 at (0,11) in round 1 or 3, then growth and tier5 waves).
FRONTIER5 = FRONTIER4 + [
    D + "v19.fortress:@make",
    D + "v20.fortress:@make",
    E + "v13.econ13:@make",
    E + "v15.econ15:@make",
    K + 'opening_response:@make?opening="guard_poke5"&fallback="economy13"',
    K + "feature_bluff:@make?turret_round=1",
    K + "feature_bluff:@make?turret_round=3",
]

# Scenario-robustness set (cycle 6, 06:20Z): ten development opponents for scripted openings
# (run with --scenarios; the lead's development seeds are those hrt-w2 used, notes/economy.md entry 5).
SCEN = [
    C + '@archetype?name="eco6_t5"',
    B + "@eco_then_flood?switch=8",
    E + 'v15.econ15:@make?free_fallback="leak"',
    E + "v13.econ13:@make",
    E + "v4.econ:@make?late_round=6&phi=0.0",
    D + "v19.fortress:@make",
    D + "v22.fortress:@make",
    D + "v7.fortress:@make?attack_from=6&attack_share=0.5",
    X + "v4:@make",
    K + 'opening_response:@make?opening="guard_poke5"&fallback="economy13"',
]

# hrt-w3's targeted counters against best_v9a (notes/validation.md, 06:24Z; specs decoded from
# experiments/validation/best-v9a-targeted-001.json). Used for the cycle-6 revision; not validation.
TARGETED = [
    K + "feature_bluff:@make?turret_round=0",
    K + "feature_bluff:@make?turret_round=1",
    K + "feature_bluff:@make?turret_round=2",
    K + "feature_bluff:@make?turret_round=3",
    K + 'opening_response:@make?opening="guard_poke5"&fallback="economy13"',
    K + 'guarded_schedule:@make?schedule=[[1,"tier1",1],[8,"tier4",200]]',
    K + 'guard_continuation:@make?continuation="economy15"&parameters={"free_fallback":"leak"}',
    K + 'guarded_schedule:@make?schedule=[[1,"tier1",1],[5,"tier4",200]]',
    E + "v13.econ13:@make",
    D + "v21.fortress:@make",
    E + 'v15.econ15:@make?free_fallback="leak"',
]

# Newest recommended worker artifacts (07:22Z): hrt-w1's fortress v22 (notes/defense.md 06:54Z) and hrt-w2's econ17
# (notes/economy.md entry 8; on a standard start it acts as econ16 free_fallback="zero").
LATEST = [
    D + "v22.fortress:@make",
    E + 'v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11',
]

# hrt-w3's newest development counters (notes/validation.md 09:01Z-09:21Z; specs decoded from
# experiments/validation/budget-timing-V4-001.json, guard-roster-transfer-002.json and
# guard-geometry-transfer-001.json) and hrt-w1's frozen fortress v24 and v25 (notes/defense.md 08:38Z, 09:18Z).
# Development use only (cycle 9, 2026-10-31T09:25Z); not validation.
TARGETED2 = (
    [K + f'budget_timing:@make?tier="{t}"&attack_round={r}&budget_fraction={f}'
     for t, r in (("tier3", 3), ("tier3", 5), ("tier4", 5), ("tier4", 6)) for f in (0.25, 0.5, 1.0)]
    + [K + f"guard_roster:@make?roster={_js(r)}" for r in ROSTERS]
    + [K + f"guard_geometry:@make?roster={_js(r)}" for r in ROSTERS]
    + [D + "v24.fortress:@make", D + "v25.fortress:@make"]
)

# Foreign-map opponents (cycle 9, 2026-10-31T09:39Z): the opponents that beat or drew v16 in sc1 (econ15 leak,
# fortress v19 and v22, eco6_t5, econ17), the guard opening, and the newest frozen teammate bots for scripted
# maps: fortress v25 and v26 (notes/defense.md 09:24Z) and econ19 (notes/economy.md entry 12). Run with --scenarios.
FOREIGN_OPP = [
    E + 'v15.econ15:@make?free_fallback="leak"',
    D + "v19.fortress:@make",
    D + "v22.fortress:@make",
    D + "v25.fortress:@make",
    D + "v26.fortress:@make",
    C + '@archetype?name="eco6_t5"',
    K + 'opening_response:@make?opening="guard_poke5"&fallback="economy13"',
    E + 'v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11',
    E + 'v19.econ19:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true',
]
NEW_FOREIGN = FOREIGN_OPP[3:5] + FOREIGN_OPP[8:]
OLD_FOREIGN = [s for s in FOREIGN_OPP if s not in NEW_FOREIGN]

# Newest opponents (cycle 9, 2026-10-31T11:23Z), standard start: hrt-w1's frozen fortress v27, v28 (v27 + response_memory)
# and v29 (the final recommendation, notes/defense.md 11:11Z); hrt-w2's econ21 (on the standard start it plays as
# econ19, notes/economy.md entry 14); hrt-w3's development counters (notes/validation.md 11:17Z): the adaptive
# catalogue with economy20 continuation (beats best_v9b 800:765), its guarded openings, the corner guard of their
# outside set, and GuardedForecast with an exact model of the frozen candidate best_v9c (one to four tier1 or a
# tier2 behind a corner gun1, then exact-forecast defence and no offence; 800:795 to 800:778 against best_v9b).
GF = K + "guarded_forecast:@make?attack_share=0&x=10&y=1&model_spec=" + json.dumps(F + "best_v9c:@make") + "&roster="
TARGETED3 = (
    [D + "v27.fortress:@make", D + "v28.fortress:@make", D + "v29.fortress:@make",
     E + 'v21.econ21:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true'
         '&replan=true&foreign_sat_from=11&replan_gain=400',
     K + "adaptive_continuation:@make?attack_weight=4",
     K + 'guarded_adaptive_continuation:@make?roster=["tier1"]',
     K + 'guarded_adaptive_continuation:@make?roster=["tier1","tier1"]',
     K + 'guard_geometry:@make?roster=["tier1"]&x=9&y=1&parameters={"foreign_attack_from":null}']
    + [GF + _js(r) for r in ((), ("tier1",), ("tier1", "tier1"), ("tier2",), ("tier1",) * 4,
                             ("tier1", "tier1", "tier2"))]
)
TEAMMATES3 = TARGETED3[:8]

# TARGETED3 with GuardedForecast modelling the development candidate V22G (v22 with r1_gun=[4,1]) itself (2026-10-31T11:29Z).
# The model is named by module:@factory with its parameters as a percent-encoded JSON object.
V22G_PARAMS = dict(big_threat=100, gun_cap=120, poke_until=3, big_partial=True, r1_poke=3, attack_mode="adaptive",
                  poke_reactive="turret", fortress_n=4, immune_attack=True, foreign_policy="econ17", mid_until=5,
                  fortress_guns=True, catch_up=True, mid_joint=0.75, mid_level=True, foreign_target="econ20",
                  r1_gun=[4, 1])
GF22 = (K + "guarded_forecast:@make?attack_share=0&x=10&y=1&model_spec="
        + json.dumps("bot_research.experiments.lead.v22:@make") + "&model_parameters="
        + quote(json.dumps(V22G_PARAMS, separators=(",", ":")), safe="") + "&roster=")
TARGETED3_V22G = TARGETED3[:8] + [GF22 + _js(r) for r in ((), ("tier1",), ("tier1", "tier1"), ("tier2",),
                                                           ("tier1",) * 4, ("tier1", "tier1", "tier2"))]

# hrt-w1's frozen fortress v32 (notes/defense.md 11:35Z, the lane's revised recommendation: v29 with attack_share 0.35),
# appended to the targeted3 pools from 2026-10-31T11:35Z (t9a, t9e; t9b had started without it).
V32 = [D + "v32.fortress:@make"]

# Opponents on which the joint early plan (mid_joint) decided a result in cycle 9 (2026-10-31T11:35Z): hrt-w3's four
# feature bluffs (c9h: turret_round=1 -980 for V20T, +595 for V17), budget_timing tier3 r3 0.5 (the reason for
# mid_joint) and the guard openings [tier1], [tier1, tier1] (the reason for mid_level). Development use only.
MIDJOINT = ([K + f"feature_bluff:@make?turret_round={r}" for r in range(4)]
            + [K + 'budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5']
            + [K + f"guard_geometry:@make?roster={_js(r)}" for r in (("tier1",), ("tier1", "tier1"))])

# TARGETED3 with GuardedForecast modelling the frozen candidate best_v9d (V23R) and fortress v32 (2026-10-31T11:47Z).
GF9D = K + "guarded_forecast:@make?attack_share=0&x=10&y=1&model_spec=" + json.dumps(F + "best_v9d:@make") + "&roster="
TARGETED3_V9D = (TARGETED3[:8] + [GF9D + _js(r) for r in ((), ("tier1",), ("tier1", "tier1"), ("tier2",), ("tier1",) * 4,
                                                          ("tier1", "tier1", "tier2"))] + V32)

# hrt-w3's bypass of the relevance filter (notes/validation.md 11:45Z: gun1 at (0,2) or (9,11) covers the route but
# kills no copy; V23R loses -980 there) and variations of the bluff's growth and tier (2026-10-31T11:52Z). Development use only.
BLUFFCOV = [K + "feature_bluff:@make?turret_round=" + s for s in
            ("1", "1&turret_x=0&turret_y=2", "1&turret_x=9&turret_y=11", "2&turret_x=0&turret_y=2",
             "1&growth_rounds=5", "1&growth_rounds=7", '1&tier="tier4"', "0&growth_rounds=5")]

# TEAMMATES3 + GuardedForecast modelling the candidates without the joint plan: V18FT (v19, no mid_joint) and V24G
# (V18FT with r1_gun=[4,1], played by v22) (2026-10-31T11:52Z).
V18FT_PARAMS = {k: v for k, v in V22G_PARAMS.items() if k not in ("mid_joint", "mid_level", "r1_gun")}
V24G_PARAMS = dict(V18FT_PARAMS, r1_gun=[4, 1])


def _gf(module, params):
    return (K + "guarded_forecast:@make?attack_share=0&x=10&y=1&model_spec=" + json.dumps(module + ":@make")
            + "&model_parameters=" + quote(json.dumps(params, separators=(",", ":")), safe="") + "&roster=")


GF_ROSTERS = ((), ("tier1",), ("tier1", "tier1"), ("tier2",), ("tier1",) * 4, ("tier1", "tier1", "tier2"))
TARGETED3_V18FT = (TEAMMATES3 + [_gf("bot_research.experiments.lead.v19", V18FT_PARAMS) + _js(r) for r in GF_ROSTERS]
                   + V32)
TARGETED3_V24G = (TEAMMATES3 + [_gf("bot_research.experiments.lead.v22", V24G_PARAMS) + _js(r) for r in GF_ROSTERS]
                  + V32)

# hrt-w3's grower counters (notes/validation.md 12:00Z-12:22Z), standard start: roster_bait (feature_bluff growth
# with a round-2 bait; no turret, or a gun1 at (0,2) in round 1) and maze_grower (growth behind a wall layout:
# empty, the lead's 20-wall opening, or their searched 46-wall cash_rank_1), then tier5 with all gold
# (written by 2026-10-31T12:44Z).
_BAITS = ([], ["tier1"], ["tier1", "tier1"], ["tier1", "tier1", "tier1"], ["tier2"])
_RB = K + 'roster_bait:@make?turret_x=0&turret_y=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&bait_round=2'
ROSTER_BAIT = [_RB + f"&turret_round={t}&growth_rounds={g}&bait={_js(b)}"
               for t, gs in ((0, (4, 5, 6, 7, 8, 9)), (1, (6,))) for g in gs for b in _BAITS]
MAZE_GROWER = [K + f'maze_grower:@make?layout="{lay}"&growth_rounds={g}&bait={_js(b)}&bait_round=2&tier="tier5"'
               '&factory_cap=2000&purchase_cap=1000'
               for lay in ("empty", "lead_opening", "cash_rank_1") for g in (5, 6, 7) for b in _BAITS if len(b) != 3]
GROWERS = ROSTER_BAIT + MAZE_GROWER

# TEAMMATES3 + GuardedForecast modelling the development candidate P5 (v24 with passive_until=5) (2026-10-31T12:44Z).
TARGETED3_P5 = (TEAMMATES3 + [_gf("bot_research.experiments.lead.v24", {"passive_until": 5}) + _js(r) for r in GF_ROSTERS]
                + V32)

# hrt-w3's delayed-guard grower (notes/validation.md 12:32Z): maze_grower plus one splash in guard_round, which
# ends our passive condition from the next round (written 2026-10-31T12:47Z).
GUARDED_MAZE = [K + f'guarded_maze:@make?layout="{lay}"&growth_rounds={g}&guard_round={r}&bait={_js(b)}&bait_round=2'
                '&tier="tier5"&factory_cap=2000&purchase_cap=1000'
                for lay in ("empty", "lead_opening", "cash_rank_1") for g in (4, 5, 6) for r in (3, 4, 5) if r <= g
                for b in ([], ["tier1"], ["tier2"])]

# hrt-w3's staged-guard growers (notes/validation.md 12:5xZ-13:14Z): maze_grower with splash guards in guard_rounds,
# the guard ladder (cumulative splash counts by round, empty layout) and the fixed heavy-drip schedule; P5 loses the
# empty grower with guards in rounds 4 and 6 after one failed round-6 attack (written 2026-10-31T13:16Z).
STAGED = ([K + f'staged_guard_maze:@make?layout="{lay}"&growth_rounds={g}&bait=[]&bait_round=2&tier="tier5"'
           f'&factory_cap=2000&purchase_cap=1000&guard_rounds={_js(gr)}'
           for lay in ("empty", "lead_opening", "cash_rank_1") for g in (4, 5, 6, 7, 8)
           for gr in ([3, 5], [4, 6], [5, 7], [4, 6, 8])]
          + [K + f'guard_ladder:@make?growth_rounds={g}&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000'
             f'&purchase_cap=1000&upgrades={_js(u)}'
             for g in (5, 6, 7) for u in ([[4, 1], [6, 2], [8, 5]], [[4, 1], [6, 2], [9, 5]], [[4, 1], [6, 2], [10, 5]])]
          + [K + "heavy_drip:@make"])

# TEAMMATES3 + GuardedForecast modelling P5TF (v24 passive_until=5, poke_reactive turret_only, fail_limit=2).
TARGETED3_P5TF = (TEAMMATES3 + [_gf("bot_research.experiments.lead.v24", {"passive_until": 5, "poke_reactive": "turret_only",
                                                                          "fail_limit": 2}) + _js(r) for r in GF_ROSTERS]
                  + V32)
# hrt-w3's screen-aware guard (notes/validation.md 13:26Z): staged_guard_maze empty with splashes in rounds 4 and 6
# and two gun1 at (10,3), (10,4) in upgrade_round; growth 4-8, upgrade rounds 7-12 (written 13:36Z).
SCREENED = [K + f'screened_guard_maze:@make?layout="empty"&growth_rounds={g}&bait=[]&bait_round=2&tier="tier5"'
            f'&factory_cap=2000&purchase_cap=1000&upgrade_round={u}' for g in (4, 5, 6, 7, 8) for u in (7, 8, 9, 10, 11, 12)]
# Turret-then-strike opponents for passive_turret=false (written 13:40Z): hrt-w1's fixed counters (notes/defense.md
# 13:19Z; one cheap turret and one tier1 in round 1, factories, then tier5 in rounds 7-8 or tier4/tier3 in rounds 8-9)
# and guarded_schedule (round-1 defence against two tier1, then 200 copies of one tier from round r).
PUNISH = (["bot_research.bots.defense.counter_astra33:@make", "bot_research.bots.defense.counter_astra28:@make"]
          + [K + f'guarded_schedule:@make?schedule=[[1,"tier1",1],[{r},"{t}",200]]'
             for r in (3, 4, 5, 6, 7) for t in ("tier3", "tier4", "tier5")])

# hrt-w3's guard_handoff (notes/validation.md 13:39Z-13:53Z): the screened guard opening (empty layout, splashes in
# rounds 4 and 6, two gun1 in round 9), then hrt-w1's frozen v34 defender (attack "none") from round H; growth 5-7,
# H in 10-14 and 16 (written 2026-10-31T14:04Z).
HANDOFF = [K + f'guard_handoff:@make?layout="empty"&growth_rounds={g}&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000'
           f'&purchase_cap=1000&handoff_round={h}&replan_iters=5000' for g in (5, 6, 7) for h in (10, 11, 12, 13, 14, 16)]

# Round-5 strikers (written 2026-10-31T14:43Z): the opponents of f5t and TARGETED2 that buy only factories before their strike
# (hrt-w2's economy.timing: 33 tier1 in round 5; hrt-w3's budget_timing) and the economy bots whose round-5 tier3 was
# the reason for rule 3d; for passive_until and passive_mid_from.
TIMING = ([s for s in TARGETED2 if "budget_timing" in s] + ["bot_research.bots.economy.timing:@make"]
          + [E + "v13.econ13:@make", E + 'v15.econ15:@make?free_fallback="leak"',
             E + 'v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11'])

# 2026-10-31T14:56Z: timing strikers from round 2 to 6 with tier1 to tier4 (budget_timing, half-budget defence envelope): the
# passive window skips insurance through round 4 or 5, so any strike inside it is a candidate counter.
TIMING2 = [K + f'budget_timing:@make?tier="{t}"&attack_round={r}&budget_fraction=0.5'
           for t in ("tier1", "tier2", "tier3", "tier4") for r in (2, 3, 4, 5, 6)]

# hrt-w2's strike1 set (experiments/economy/opp_strike1.txt, copied 2026-10-31T16:42Z): economy.timing with attack_round
# 4-7, attack_frac 1.0/0.5, repeat, pre_defend and fac_cap variants.
STRIKE1 = [
    'bot_research.bots.economy.timing:@make?attack_round=4&attack_frac=1.0&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=4&attack_frac=1.0&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=4&attack_frac=0.5&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=4&attack_frac=0.5&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=5&attack_frac=1.0&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=5&attack_frac=1.0&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=5&attack_frac=0.5&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=5&attack_frac=0.5&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=6&attack_frac=1.0&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=6&attack_frac=1.0&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=6&attack_frac=0.5&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=6&attack_frac=0.5&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=7&attack_frac=1.0&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=7&attack_frac=1.0&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=7&attack_frac=0.5&repeat=false',
    'bot_research.bots.economy.timing:@make?attack_round=7&attack_frac=0.5&repeat=true',
    'bot_research.bots.economy.timing:@make?attack_round=5&pre_defend=true&pre_gold=60',
    'bot_research.bots.economy.timing:@make?attack_round=5&fac_cap=10',
    'bot_research.bots.economy.timing:@make?attack_round=6&pre_defend=true&pre_gold=60',
    'bot_research.bots.economy.timing:@make?attack_round=6&fac_cap=10',
]

if __name__ == "__main__":
    import sys
    pool = {"tuning": TUNING, "strong": STRONG, "all": TUNING + STRONG, "frontier": FRONTIER, "frontier2": FRONTIER2,
            "frontier3": FRONTIER3, "frontier4": FRONTIER4, "frontier5": FRONTIER5, "scen": SCEN, "targeted": TARGETED, "latest": LATEST, "targeted2": TARGETED2, "targeted3": TARGETED3 + V32, "teammates3": TEAMMATES3, "targeted3_v22g": TARGETED3_V22G + V32, "midjoint": MIDJOINT, "targeted3_v9d": TARGETED3_V9D, "bluffcov": BLUFFCOV, "targeted3_v18ft": TARGETED3_V18FT, "targeted3_v24g": TARGETED3_V24G, "growers": GROWERS, "targeted3_p5": TARGETED3_P5, "roster_bait": ROSTER_BAIT, "maze_grower": MAZE_GROWER, "guarded_maze": GUARDED_MAZE, "staged": STAGED, "targeted3_p5tf": TARGETED3_P5TF, "screened": SCREENED, "punish": PUNISH, "handoff": HANDOFF, "timing": TIMING, "timing2": TIMING2, "strike1": STRIKE1,
            "foreign": FOREIGN_OPP, "new_foreign": NEW_FOREIGN, "old_foreign": OLD_FOREIGN,
            "scenx": SCEN + [s for s in LATEST if s not in SCEN],
            "f5t": FRONTIER5 + [s for s in TARGETED if s not in FRONTIER5],
            "everything": TUNING + STRONG + [s for s in FRONTIER if s not in STRONG and s not in TUNING]}[sys.argv[1] if len(sys.argv) > 1 else "tuning"]
    print(" ".join(f"'{s}'" for s in pool))
