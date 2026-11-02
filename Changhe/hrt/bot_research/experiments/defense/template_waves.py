"""Wave-band templates for the lead's request (a): high S(k) for small k, S(25) >= 1500.

Band A (rows 0-2): teeth down col 0, up col 2, down col 4, up col 6, down col 8, up col 10, then column 11
down to the row-3 gap. Pillars (slots) at (1,1),(3,1),(5,1),(7,1),(9,1); blockers (walls) (1,0),(3,2),(5,0),
(7,2),(9,0). Separator row 3: walls except (11,3).
Band B (rows 4-6), right to left: pillars (10,5),(8,5),(6,5),(4,5); blockers (10,4),(8,6),(6,4),(4,6),(2,4).
Separator row 7: walls except (0,7). Bottom wave rows 8-11 as in the w1 master layout.
Variants differ in which separator/wave cells are slots versus walls.
"""
from bot_research.experiments.defense.template_eval import report, greedy_sequence
from bot_research.bots.defense.geometry import route, attackable_cells, splash_adjacency


def waves(extra_slots="auto", n_slots=26):
    pillars_a = [(1, 1), (3, 1), (5, 1), (7, 1), (9, 1)]
    block_a = [(1, 0), (3, 2), (5, 0), (7, 2), (9, 0)]
    sep3 = [(x, 3) for x in range(11)]
    pillars_b = [(10, 5), (8, 5), (6, 5), (4, 5)]
    block_b = [(10, 4), (8, 6), (6, 4), (4, 6), (2, 4)]
    sep7 = [(x, 7) for x in range(1, 12)]
    wave = []
    for c in (1, 3, 5, 7, 9):
        rows = (8, 9, 10) if (c - 1) in (0, 4, 8) else (9, 10, 11)
        wave += [(c, y) for y in rows]
    cells = pillars_a + block_a + sep3 + pillars_b + block_b + sep7 + wave
    full = set(cells)
    p = route(full)
    att = attackable_cells(p)
    adj = {c: splash_adjacency(c, att) for c in cells}
    slots = list(pillars_a + pillars_b)
    # add further slots by final adjacency among separators and wave cells
    pool = sorted((c for c in sep3 + sep7 + wave), key=lambda c: -adj[c])
    for c in pool:
        if len(slots) >= n_slots:
            break
        slots.append(c)
    walls = [c for c in cells if c not in set(slots)]
    return tuple(walls), tuple(slots), adj


if __name__ == "__main__":
    for n in (26, 30):
        walls, slots, adj = waves(n_slots=n)
        print("final adjacency of pillars:", [(c, adj[c]) for c in slots[:9]])
        report(f"wave bands, {n} slots", walls, slots, show_map=(n == 26))
