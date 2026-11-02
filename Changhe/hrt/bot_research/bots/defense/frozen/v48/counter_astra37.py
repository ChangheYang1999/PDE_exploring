"""Reproduction of astra's hoarder schedules from the seventh review (lane hrt-w1 test bots, not candidates).

Fixed, observation-free purchase lists (astra/v37-exploits/answer.md): factories 5 / 4 / 8 in rounds 1-3; round 4: the guarded
variant builds gun1 at (10,1) and buys 13 factories, the bare variant 14; round 5: nothing (the "15" variants buy one tier1);
round 6: 47 (bare 49; the 15-variants one less); round 7: 59 (bare 61; 15-variants one less); rounds 8 and 9: three tier5 each;
round 10: a fixed 72-step lock (walls, then splashes); nothing afterwards. Astra's engine results: G beats v37 (-55) and loses
to v36 (+135); B loses to v36 (+416, killed in round 8) and to v37 (+215), and beats the v37 + insurance-cap module (-15).
Specs: bot_research.bots.defense.counter_astra37:@make?variant="G" (also "B", "G15", "B15").
"""

WALLS = [(x, 1) for x in range(0, 10)] + [(x, 3) for x in range(11, 1, -1)] + \
        [(0, 5), (9, 7), (10, 7), (11, 7), (3, 11), (5, 8), (7, 11), (9, 8), (9, 9)]
SPLASH_B = [(1, 3), (10, 1), (7, 5), (9, 10), (7, 9), (8, 7), (5, 5), (6, 7), (2, 5), (7, 10), (4, 5), (6, 5), (1, 5), (3, 5),
            (7, 7), (4, 7), (3, 7), (5, 9), (2, 7), (5, 10), (1, 7), (8, 5), (9, 5), (10, 5), (3, 9)]
SPLASH_G = [c for c in SPLASH_B if c != (10, 1)] + [(5, 7), (3, 10)]


def make(variant="G"):
    guarded = variant.startswith("G")
    poke = variant.endswith("15")
    fac = {1: 5, 2: 4, 3: 8, 4: 13 if guarded else 14, 6: 47 if guarded else 49, 7: 59 if guarded else 61}
    if poke:
        fac[6] -= 1
        fac[7] -= 1

    def decide(obs):
        rnd = obs["round"]
        acts = []
        if rnd == 4 and guarded:
            acts.append({"op": "build_turret", "type": "gun1", "x": 10, "y": 1})
        if rnd == 5 and poke:
            acts.append({"op": "buy_minion", "type": "tier1"})
        if rnd in fac:
            acts += [{"op": "buy_factory"}] * fac[rnd]
        if rnd in (8, 9):
            acts += [{"op": "buy_minion", "type": "tier5"}] * 3
        if rnd == 10:
            acts += [{"op": "build_wall", "x": x, "y": y} for x, y in WALLS]
            acts += [{"op": "build_turret", "type": "splash", "x": x, "y": y} for x, y in (SPLASH_G if guarded else SPLASH_B)]
        return acts

    return decide
