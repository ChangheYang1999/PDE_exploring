"""Hand-designed master layouts: horizontal serpentine (rows 1,3,5,7) plus a square wave in rows 8-11.
Prints route length, adjacency histogram, top-k sums, and the number of cells with adjacency >= 6."""
from bot_research.bots.defense.geometry import attackable_cells, gun_cells, render, route, splash_adjacency


def serp_rows():
    cells = set()
    for y, gap in ((1, 11), (3, 0), (5, 11), (7, 0)):
        cells |= {(x, y) for x in range(12) if x != gap}
    return cells


def bottom_wave(cols_down=(0, 4, 8), pillar_cols=(1, 3, 5, 7, 9)):
    """Pillars: 3 cells each. Column c in pillar_cols: rows 8-10 if the path goes down on its left (c-1 in cols_down), else rows 9-11."""
    cells = set()
    for c in pillar_cols:
        if (c - 1) in cols_down:
            cells |= {(c, 8), (c, 9), (c, 10)}
        else:
            cells |= {(c, 9), (c, 10), (c, 11)}
    return cells


def report(name, blocked):
    path = route(blocked)
    if path is None:
        print(name, "DISCONNECTED"); print(render(blocked)); return None
    att = attackable_cells(path)
    adj = {c: splash_adjacency(c, att) for c in blocked}
    vals = sorted(adj.values(), reverse=True)
    print(f"=== {name}: cells={len(blocked)} L={len(path)-1} top19={sum(vals[:19])} top25={sum(vals[:25])} top26={sum(vals[:26])} top30={sum(vals[:30])} n>=6={sum(v>=6 for v in vals)} hist={ {k: vals.count(k) for k in range(9) if vals.count(k)} }")
    print(render(blocked, path, {c: str(v) for c, v in adj.items()}))
    print("gun3 best:", sorted(((gun_cells(c, 3.5, att), c) for c in blocked), reverse=True)[:4])
    return adj


A = serp_rows()
report("serpentine 1357", A)
B = A | bottom_wave()
report("serpentine + bottom wave", B)
# variant: wave with the last pillar at x=11? path must end at (11,11): try pillar cols (1,3,5,7,9) and extra (11,8),(11,9),(11,10)? no: that blocks the approach; try 10 going up then (11,8)->down.
C = A | bottom_wave(pillar_cols=(1, 3, 5, 7, 9)) | {(11, 8), (11, 9)}
report("serpentine + wave + (11,8),(11,9)", C)
