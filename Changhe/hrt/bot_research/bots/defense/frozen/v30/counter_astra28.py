"""Astra's fixed schedule against fortress v28 (review of 2026-10-31T10:42Z, answer in the lane directory): a test bot.

Round by round (coordinates (x, y)); factories last in each round: 1: gun1 (3,1), tier1, 2 factories; 2: walls (0,1),
(11,3), tier1, 2 factories; 3: 4 factories; 4: gun1 (10,9), 6 factories; 5: walls (x,5) x=0..10, walls (x,7) x=11..1,
10 factories; 6: gun3 (0,9), walls (3,8),(7,8),(1,9),(9,9),(1,10),(9,10),(1,11),(5,11),(9,11), splash (7,9), 7 factories;
7: gun1 (10,10), splashes (7,10),(5,10),(3,9),(5,9), 12 factories; 8: splashes (3,10),(10,3),(8,1),(10,1),(7,1), one tier4,
7 factories; 9: gun3 (10,11), splashes (2,1),(4,1),(6,1),(1,1),(5,1), three tier3, 1 factory; 10: splashes (9,1),(9,3),
(8,3),(7,3),(6,3),(5,3), 23 factories; 11: splashes (4,3),(3,3),(2,3),(1,3), 40 factories; 12-50: nothing.
Spec: bot_research.bots.defense.counter_astra28:@make  (also module-level decide). Needs no state.
"""


def _t(kind, x, y):
    return {"op": "build_turret", "type": kind, "x": x, "y": y}


def _w(x, y):
    return {"op": "build_wall", "x": x, "y": y}


def _m(kind, n=1):
    return [{"op": "buy_minion", "type": kind}] * n


def _f(n):
    return [{"op": "buy_factory"}] * n


SCHEDULE = {
    1: [_t("gun1", 3, 1)] + _m("tier1") + _f(2),
    2: [_w(0, 1), _w(11, 3)] + _m("tier1") + _f(2),
    3: _f(4),
    4: [_t("gun1", 10, 9)] + _f(6),
    5: [_w(x, 5) for x in range(0, 11)] + [_w(x, 7) for x in range(11, 0, -1)] + _f(10),
    6: [_t("gun3", 0, 9)] + [_w(*c) for c in ((3, 8), (7, 8), (1, 9), (9, 9), (1, 10), (9, 10), (1, 11), (5, 11), (9, 11))]
       + [_t("splash", 7, 9)] + _f(7),
    7: [_t("gun1", 10, 10)] + [_t("splash", *c) for c in ((7, 10), (5, 10), (3, 9), (5, 9))] + _f(12),
    8: [_t("splash", *c) for c in ((3, 10), (10, 3), (8, 1), (10, 1), (7, 1))] + _m("tier4") + _f(7),
    9: [_t("gun3", 10, 11)] + [_t("splash", *c) for c in ((2, 1), (4, 1), (6, 1), (1, 1), (5, 1))] + _m("tier3", 3) + _f(1),
    10: [_t("splash", *c) for c in ((9, 1), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3))] + _f(23),
    11: [_t("splash", *c) for c in ((4, 3), (3, 3), (2, 3), (1, 3))] + _f(40),
}


def decide(obs):
    return list(SCHEDULE.get(obs["round"], []))


def make():
    return decide
