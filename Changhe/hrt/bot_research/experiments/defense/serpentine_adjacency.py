"""Splash adjacency (attackable path cells among 8 neighbours) of every wall cell in serpentine templates,
and gun3 covered-cell counts. Writes bot_research/runs/defense/serpentine_adjacency.txt."""
from bot_research.bots.defense.geometry import (attackable_cells, flatten, gun_cells, render, route,
                                                 serpentine, splash_adjacency)

out = []
for orientation, lines, gap in [('v', (1, 3, 5, 7), 'far'), ('h', (1, 3, 5, 7), 'far'),
                                ('v', (1, 3, 5, 7, 9), 'far'), ('v', (2, 4, 6, 8), 'far'), ('v', (1, 3, 5, 7), 'near')]:
    walls = serpentine(orientation, lines, gap)
    blocked = set(flatten(walls))
    path = route(blocked)
    att = attackable_cells(path)
    out.append(f"=== serpentine {orientation} lines={lines} first_gap={gap}: walls={len(blocked)} path_len={len(path)-1}")
    marks = {}
    tot = 0
    for c in blocked:
        a = splash_adjacency(c, att)
        marks[c] = str(a)
        tot += a
    out.append(render(blocked, path, marks))
    adj_sorted = sorted((splash_adjacency(c, att), c) for c in blocked)[::-1]
    out.append("total adjacency over all wall cells: %d; top 25 sum: %d; top 19 sum: %d" % (tot, sum(a for a, _ in adj_sorted[:25]), sum(a for a, _ in adj_sorted[:19])))
    out.append("histogram: " + str({k: sum(1 for a, _ in adj_sorted if a == k) for k in range(9)}))
    # gun3/gun2/gun1 coverage at wall cells
    for name, rng in (("gun1", 2.5), ("gun2", 3.0), ("gun3", 3.5)):
        cov = sorted(((gun_cells(c, rng, att), c) for c in blocked), reverse=True)
        out.append(f"{name} best covered cells: {cov[:5]}")
    # non-wall free cells too (could host towers without changing path? only if off-path)
    free = [(x, y) for x in range(12) for y in range(12) if (x, y) not in blocked and (x, y) not in set(path)]
    out.append(f"free off-path cells: {len(free)}; best splash adjacency among them: {sorted(((splash_adjacency(c, att), c) for c in free), reverse=True)[:6]}")
    out.append('')
text = '\n'.join(out)
print(text)
open('bot_research/runs/defense/serpentine_adjacency.txt', 'w').write(text)
