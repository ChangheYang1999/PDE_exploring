"""Reproduction of astra's eighth-review schedules (lane hrt-w1 test bots, not candidates).

Fixed, observation-free purchase lists (astra/v38-review/answer.md). Astra's engine results, both seats:
A (round-5 gun / round-7 threshold trap): v38 -170, v36 +410.  B (three-premium trap): v38 -150, v36 +190.
C (guarded round-7 striker, two tier5 per round in rounds 7-10, cheap gun guard, lock in round 11): -345 against both.
D (screened round-8 striker: two tier4 ahead of three tier5, lock in round 9): -385 against both.
Specs: bot_research.bots.defense.counter_astra38:@make?variant="A" (also "B", "C", "D").
"""

W = [(x, 1) for x in range(0, 10)] + [(x, 3) for x in range(11, 1, -1)]
E = [(0, 5), (9, 7), (10, 7), (11, 7), (3, 11), (5, 8), (7, 11), (9, 8), (9, 9)]
T = [(7, 5), (9, 10), (7, 9), (8, 7), (5, 5), (6, 7), (2, 5), (7, 10), (4, 5), (6, 5), (1, 5), (3, 5), (7, 7), (4, 7), (3, 7),
     (5, 9), (2, 7), (5, 10), (1, 7), (8, 5), (9, 5), (10, 5), (3, 9)]
B_WALLS9 = [(1, 7), (1, 11), (2, 6), (5, 11), (6, 7), (7, 3), (7, 7), (7, 8), (8, 0), (8, 2), (8, 3), (8, 5), (8, 6), (9, 4), (9, 6),
            (9, 11), (10, 2), (11, 4), (11, 10)]
B_SPLASH9 = [(5, 7), (3, 1), (9, 10), (7, 9), (7, 10), (9, 9), (9, 8), (5, 9), (3, 3), (4, 1), (1, 1), (5, 10), (5, 3), (5, 5), (2, 1),
             (4, 7), (3, 8), (3, 9), (3, 10), (3, 5), (6, 1), (1, 8), (11, 9), (1, 10), (11, 8), (1, 9)]
D_WALLS9 = [(1, 6), (1, 7), (1, 8), (1, 9), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (5, 0), (5, 6), (5, 7), (5, 8), (5, 9),
            (7, 2), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 1), (8, 5), (8, 9), (9, 9), (10, 7), (10, 9),
            (11, 3), (11, 7)]
D_SPLASH9 = [(9, 7), (9, 5), (9, 3), (10, 5), (5, 2), (3, 1), (5, 3), (3, 3), (1, 2), (5, 5), (10, 3), (3, 4), (10, 10), (5, 1), (7, 3),
             (9, 1), (5, 4), (5, 10), (7, 1), (3, 5), (3, 2), (1, 1), (1, 3), (1, 4)]


def _w(cells):
    return [{"op": "build_wall", "x": x, "y": y} for x, y in cells]


def _t(kind, cells):
    return [{"op": "build_turret", "type": kind, "x": x, "y": y} for x, y in cells]


def _f(n):
    return [{"op": "buy_factory"}] * n


def _m(types):
    return [{"op": "buy_minion", "type": t} for t in types]


SCHEDULES = {
    "A": {1: _f(5), 2: _f(4), 3: _f(8), 4: _f(14), 5: _f(24), 6: _f(43),
          7: _m(["tier5"] * 2), 8: _m(["tier5"] * 2),
          9: _m(["tier5"] * 2) + _w(W) + _t("gun3", [(10, 1)]) + _t("gun3", [(1, 3)]),
          10: _m(["tier5"] * 2),
          11: _w(E) + _t("splash", T + [(5, 7), (3, 10), (1, 8)])},
    "B": {1: _f(5), 2: _f(4), 3: _f(8), 4: _f(14),
          5: _t("gun3", [(9, 2)]) + _t("gun2", [(8, 1)]) + _w([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]) + _f(10),
          6: _t("gun3", [(10, 5)]) + _t("gun2", [(9, 5)]) + _w([(0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]) + _f(18),
          7: _f(45),
          8: _m(["tier5", "tier5", "tier4", "tier1"]),
          9: _w(B_WALLS9) + _t("splash", B_SPLASH9),
          10: _t("splash", [(5, 1), (6, 3), (4, 3)])},
    "C": {1: _f(5), 2: _f(4), 3: _f(8), 4: _t("gun1", [(10, 1)]) + _f(13), 5: _f(23), 6: _f(41),
          7: _m(["tier5"] * 2), 8: _m(["tier5"] * 2),
          9: _m(["tier5"] * 2) + _w(W) + _t("gun3", [(1, 3)]) + _t("gun3", [(10, 5)]),
          10: _m(["tier5"] * 2),
          11: _w(E) + _t("splash", T[:20] + [(3, 9), (9, 5), (5, 7), (3, 10), (1, 8), (1, 9)])},
    "D": {1: _f(5), 2: _f(4), 3: _f(8), 4: _t("splash", [(10, 1)]) + _f(11), 5: _f(22), 6: _t("splash", [(1, 0)]) + _f(36),
          8: _m(["tier4", "tier4", "tier5", "tier5", "tier5"]),
          9: _w(D_WALLS9) + _t("splash", D_SPLASH9)},
}


def make(variant="A"):
    sched = SCHEDULES[variant]

    def decide(obs):
        return [dict(a) for a in sched.get(obs["round"], [])]

    return decide
