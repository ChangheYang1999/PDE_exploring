"""Drop-in WALLS/SLOTS templates for splash-slot defenders (lane hrt-w1, for the lead's best.py).

A template is a pair (WALLS, SLOTS) of cells. WALLS are built as walls as soon as affordable; SLOTS stay
open and receive splashes one by one (greedy on the per-copy splash damage S). Evaluated with
bot_research/experiments/defense/template_eval.py (greedy S(k) with the other slots open).

PILLARS_7_7_4: early slots are U-turn cells of complete lines (4 serpentine pillars + 5 bottom-snake
U-turn cells), 7 bulk slots in each of rows 1 and 3 next to the pillar end, 4 snake extras.
  walls 32, slots 27, route 40 with walls only, 78 full,
  S(1..10) = 70 140 190 240 310 370 440 500 560 610, S(15) = 820, S(20) = 1160, S(25) = 1500, S(27) = 1620.
LEAD_V3 (reference): the template in best.py at 02:49Z (33 walls, 26 slots, route 46/78,
  S(1..10) = 60 120 170 220 290 370 440 480 530 570, S(25) = 1540).
Free non-slot gun cells on PILLARS_7_7_4 / LEAD_V3 with 12-16 route cells in gun3 range while the
rows are open: (4,8), (5,8), (6,8), (8,8), (9,8), (8,4), (10,9) (see runs/defense/gun_value.txt).
"""
from __future__ import annotations

ROW_GAPS = {1: 11, 3: 0, 5: 11, 7: 0}


def _snake():
    out = []
    for i, x in enumerate(range(1, 11, 2)):
        out += [(x, y) for y in ((9, 10, 11) if i % 2 == 0 else (8, 9, 10))]
    return out


def _structure():
    return [(x, y) for y, gap in ROW_GAPS.items() for x in range(12) if x != gap] + _snake()


def pillars_template(n_bulk_per_row: int = 7, extra_snake=((1, 9), (3, 10), (5, 9), (7, 10))):
    pillars = [(10, 1), (1, 3), (10, 5), (1, 7)]
    snake_u = [(1, 10), (3, 9), (5, 10), (7, 9), (9, 10)]
    slots = pillars + snake_u
    for y in (1, 3):
        gap = ROW_GAPS[y]
        xs = list(range(10 - n_bulk_per_row, 10)) if gap == 11 else list(range(2, 2 + n_bulk_per_row))
        slots += [(x, y) for x in xs if (x, y) not in slots]
    slots += [c for c in extra_snake if c not in slots]
    sset = set(slots)
    walls = tuple(c for c in _structure() if c not in sset)
    return walls, tuple(slots)


PILLARS_7_7_4_WALLS, PILLARS_7_7_4_SLOTS = pillars_template()

_lead_slots = tuple([(x, 1) for x in range(1, 11)] + [(x, 3) for x in range(1, 11)]
                    + [(5, 9), (3, 10), (7, 10), (3, 9), (7, 9), (5, 10)])
LEAD_V3_SLOTS = _lead_slots
LEAD_V3_WALLS = tuple(c for c in _structure() if c not in set(_lead_slots))


# Annealed slot assignment on the same 59-cell structure (experiments/defense/template_search.py,
# objective sum S(1..10) + 0.5 sum S(11..20) with S(25) >= 1500, two seeds agree): slots are contiguous
# blocks at the pillar end of each row, filled by the greedy from the inner end outward, so every new
# splash extends the forced corridor by one cell and gains 6-7 adjacency.
#   walls 34, slots 25, route 34 with walls only, 78 full,
#   S(1..10) = 70 140 210 280 350 410 470 530 590 650, S(15) = 950, S(20) = 1240, S(25) = 1510.
ANNEALED_25_SLOTS = tuple(tuple(c) for c in [[1, 3], [1, 7], [1, 9], [2, 3], [2, 7], [3, 3], [3, 7], [3, 8], [3, 9], [3, 10], [5, 1], [5, 5], [5, 9], [6, 1], [6, 5], [7, 1], [7, 5], [7, 7], [7, 10], [8, 1], [8, 5], [9, 1], [9, 5], [10, 1], [10, 5]])
ANNEALED_25_WALLS = tuple(tuple(c) for c in [[0, 1], [0, 5], [1, 1], [1, 5], [1, 10], [1, 11], [2, 1], [2, 5], [3, 1], [3, 5], [4, 1], [4, 3], [4, 5], [4, 7], [5, 3], [5, 7], [5, 10], [5, 11], [6, 3], [6, 7], [7, 3], [7, 8], [7, 9], [8, 3], [8, 7], [9, 3], [9, 7], [9, 9], [9, 10], [9, 11], [10, 3], [10, 7], [11, 3], [11, 7]])


# 26-slot variant from the same search (seed 0, objective 8898): walls 33, slots 26, route 36 walls-only / 78 full,
#   S(1..10) = 70 140 210 280 350 420 490 550 610 670, S(15) = 970, S(20) = 1270, S(25) = 1500, S(26) = 1560.
ANNEALED_26_SLOTS = tuple(tuple(c) for c in [[1, 3], [1, 7], [1, 9], [1, 10], [1, 11], [3, 5], [3, 7], [3, 10], [4, 1], [4, 5], [5, 1], [5, 5], [5, 9], [6, 1], [6, 5], [7, 1], [7, 5], [7, 7], [7, 10], [8, 1], [8, 5], [9, 1], [9, 5], [9, 9], [10, 1], [10, 5]])
ANNEALED_26_WALLS = tuple(tuple(c) for c in [[0, 1], [0, 5], [1, 1], [1, 5], [2, 1], [2, 3], [2, 5], [2, 7], [3, 1], [3, 3], [3, 8], [3, 9], [4, 3], [4, 7], [5, 3], [5, 7], [5, 10], [5, 11], [6, 3], [6, 7], [7, 3], [7, 8], [7, 9], [8, 3], [8, 7], [9, 3], [9, 7], [9, 10], [9, 11], [10, 3], [10, 7], [11, 3], [11, 7]])
