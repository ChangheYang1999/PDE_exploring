"""Astra's second fixed schedule (review of frozen v33, 2026-10-31T12:07Z; answer in the lane directory): a test bot.

Round 1: gun1 (10,1), one tier1, 2 factories; 2: 3 factories; 3: 5; 4: 9; 5: 15; 6: nothing; 7: one tier5; 8: one tier5;
9: gun2 (10,2); 10-50: nothing. Fixed in advance, no observation used. Beats v33 745 : -45 at round 10 (both seats) and
the attack_share 0.7 policy by about 600 according to the review (reproduced in x117).
Spec: bot_research.bots.defense.counter_astra33:@make  (also module-level decide).
"""


def _t(kind, x, y):
    return {"op": "build_turret", "type": kind, "x": x, "y": y}


def _m(kind, n=1):
    return [{"op": "buy_minion", "type": kind}] * n


def _f(n):
    return [{"op": "buy_factory"}] * n


SCHEDULE = {
    1: [_t("gun1", 10, 1)] + _m("tier1") + _f(2),
    2: _f(3),
    3: _f(5),
    4: _f(9),
    5: _f(15),
    7: _m("tier5"),
    8: _m("tier5"),
    9: [_t("gun2", 10, 2)],
}


def decide(obs):
    return list(SCHEDULE.get(obs["round"], []))


def make():
    return decide
