"""Reproduction of astra's ninth-review schedules (lane hrt-w1 test bots, not candidates).

Fixed, observation-free purchase lists (astra/v41-review/answer.md): 5 factories; round 2 three tier1 + 2 factories; a splash guard at
(10,1) in round 3 (A) or 4 (B); factories; a second guard in round 6 (A: gun1 (1,0); B: splash (1,0)); nothing in round 7; three tier5
in round 8; a 52-step lock in rounds 9-10 (S 1530 / 1550). Astra's engine results: v41 and v38 both 505:780 (A, -275) and 505:765
(B, -260): two of the three tier5 land in round 8 (280) after the bait's 15.
Specs: bot_research.bots.defense.counter_astra41:@make?variant="A" (also "B").
"""

W9 = [(x, 1) for x in range(1, 10)] + [(x, 3) for x in range(11, 1, -1)] + [(0, 5), (9, 7), (10, 7), (11, 7)]
S9 = [(1, 3), (7, 5), (10, 9), (8, 7), (5, 5), (6, 7), (2, 5), (4, 5), (6, 5), (1, 5), (3, 5), (7, 7), (5, 7), (4, 7), (3, 7), (2, 7), (8, 5)]
W10 = [(3, 11), (5, 8), (7, 11), (9, 8), (9, 9)]
S10 = [(1, 7), (9, 5), (10, 5), (5, 9), (7, 10), (7, 9), (5, 10), (3, 9), (3, 10), (1, 8)]


def _w(cells):
    return [{"op": "build_wall", "x": x, "y": y} for x, y in cells]


def _t(kind, cells):
    return [{"op": "build_turret", "type": kind, "x": x, "y": y} for x, y in cells]


def _f(n):
    return [{"op": "buy_factory"}] * n


def _m(types):
    return [{"op": "buy_minion", "type": t} for t in types]


SCHEDULES = {
    "A": {1: _f(5), 2: _m(["tier1"] * 3) + _f(2), 3: _t("splash", [(10, 1)]) + _f(4), 4: _f(10), 5: _f(16),
          6: _t("gun1", [(1, 0)]) + _f(28), 8: _m(["tier5"] * 3),
          9: _w(W9) + _t("splash", S9), 10: _w(W10) + _t("splash", S10)},
    "B": {1: _f(5), 2: _m(["tier1"] * 3) + _f(2), 3: _f(7), 4: _t("splash", [(10, 1)]) + _f(9), 5: _f(18),
          6: _t("splash", [(1, 0)]) + _f(29), 8: _m(["tier5"] * 3),
          9: _w(W9) + _t("splash", S9), 10: _w(W10) + _t("splash", S10)},
}


def make(variant="A"):
    sched = SCHEDULES[variant]

    def decide(obs):
        return [dict(a) for a in sched.get(obs["round"], [])]

    return decide
