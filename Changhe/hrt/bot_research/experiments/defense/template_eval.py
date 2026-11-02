"""Evaluate WALLS/SLOTS templates: greedy per-copy splash sequence S(k) and gun cells.

Template = (WALLS, SLOTS): WALLS are built first (all of them), SLOTS are open cells filled one at a time
with a splash, each time choosing the open slot that maximises per-copy splash damage S on the resulting
route (ties: longer route). Reports S(k) for k = 1..len(SLOTS), route lengths, and the k needed for 1500.
Also lists free cells (not wall, not slot, not on the final route) ranked by gun3/gun2 coverage of the
final route. Run: .venv/bin/python -B -m bot_research.experiments.defense.template_eval
"""
from bot_research.bots.defense.geometry import attackable_cells, gun_cells, render, route, splash_adjacency


def splash_total(blocked, splashes):
    p = route(blocked)
    if p is None:
        return -1, None
    att = attackable_cells(p)
    return 10 * sum(splash_adjacency(s, att) for s in splashes), p


def greedy_sequence(walls, slots):
    blocked = set(walls)
    splashes = []
    seq = []
    open_slots = list(slots)
    while open_slots:
        best = None
        for c in open_slots:
            if c in blocked:
                continue
            S, p = splash_total(blocked | {c}, splashes + [c])
            if p is None:
                continue
            key = (S, len(p))
            if best is None or key > best[0]:
                best = (key, c)
        if best is None:
            break
        (S, L), c = best
        blocked.add(c)
        splashes.append(c)
        open_slots.remove(c)
        seq.append((c, S, L - 1))
    return seq


def lead_template():
    barriers = [[(x, y) for x in range(12) if x != gap] for y, gap in ((1, 11), (3, 0), (5, 11), (7, 0))]
    snake = []
    for i, x in enumerate(range(1, 11, 2)):
        snake += [(x, y) for y in ((9, 10, 11) if i % 2 == 0 else (8, 9, 10))]
    slots = tuple([(x, 1) for x in range(1, 11)] + [(x, 3) for x in range(1, 11)]
                  + [(5, 9), (3, 10), (7, 10), (3, 9), (7, 9), (5, 10)])
    sset = set(slots)
    walls = tuple(c for c in [c for b in barriers for c in b] + snake if c not in sset)
    return walls, slots


def my_template():
    from bot_research.bots.defense.plan import LAYOUT
    return tuple(LAYOUT.wall_order), tuple(LAYOUT.splash_cells)


def report(name, walls, slots, show_map=True):
    seq = greedy_sequence(walls, slots)
    S = [s for _, s, _ in seq]
    k1500 = next((i + 1 for i, s in enumerate(S) if s >= 1500), None)
    L0 = len(route(set(walls))) - 1
    print(f"=== {name}: walls={len(walls)} slots={len(slots)} route(walls only)={L0} route(full)={seq[-1][2] if seq else None} "
          f"S(1..10)={S[:10]} S(15)={S[14] if len(S)>14 else None} S(20)={S[19] if len(S)>19 else None} S(25)={S[24] if len(S)>24 else None} k_for_1500={k1500} sum S(1..10)={sum(S[:10])}")
    print("   order:", [c for c, _, _ in seq[:12]])
    if show_map:
        full = set(walls) | set(slots)
        p = route(full)
        marks = {c: 'o' for c in slots}
        print(render(full, p, marks))
        att = attackable_cells(p)
        free = [(x, y) for x in range(12) for y in range(12) if (x, y) not in full and (x, y) not in set(p) and (x, y) not in ((0, 0), (11, 11))]
        g3 = sorted(((gun_cells(c, 3.5, att), c) for c in free), reverse=True)[:6]
        g2 = sorted(((gun_cells(c, 3.0, att), c) for c in free), reverse=True)[:6]
        print("   free cells (not slot/wall/route): gun3 coverage", g3)
        print("                                     gun2 coverage", g2)
    return seq


if __name__ == "__main__":
    report("lead best.py template", *lead_template())
    report("w1 master layout (reserved >=5)", *my_template())
