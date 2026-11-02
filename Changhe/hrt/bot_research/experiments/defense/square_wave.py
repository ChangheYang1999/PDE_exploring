"""Square-wave band layouts: U-turns around single pillars (7 splash adjacency each)."""
from bot_research.bots.defense.geometry import attackable_cells, render, route, splash_adjacency, gun_cells


def band(y0, direction_down_first=True, blockers_top=(1, 5, 9), pillars=(1, 3, 5, 7, 9, 11)):
    """Rows y0..y0+2. Pillars at (odd x, y0+1). Blockers at top row for x in blockers_top, bottom row otherwise."""
    walls = set()
    for x in pillars:
        walls.add((x, y0 + 1))
        if x in blockers_top:
            walls.add((x, y0))
        else:
            walls.add((x, y0 + 2))
    return walls


def separator(y, gap_x):
    return {(x, y) for x in range(12) if x != gap_x}


def report(name, blocked):
    path = route(blocked)
    if path is None:
        print(name, "DISCONNECTED"); print(render(blocked)); return
    att = attackable_cells(path)
    marks = {c: str(splash_adjacency(c, att)) for c in blocked}
    adj = sorted((splash_adjacency(c, att) for c in blocked), reverse=True)
    print(f"=== {name}: walls={len(blocked)} path_len={len(path)-1} top25={sum(adj[:25])} top19={sum(adj[:19])} hist={ {k: adj.count(k) for k in range(9) if adj.count(k)} }")
    print(render(blocked, path, marks))
    g3 = sorted(((gun_cells(c, 3.5, att), c) for c in blocked), reverse=True)[:3]
    print("gun3 best:", g3)


# Layout A: band rows 0-2, separator row 3 (gap at x=11? path exits band at right end (11,0)->(11,1)->(11,2)?)
# path in band: starts (0,0) down col0 -> (0,2),(1,2),(2,2) up col2 -> (2,0),(3,0),(4,0) down col4 ... ends at col 10 going?
# cols 0,4,8 go down; cols 2,6,10 go up -> ends at (10,0) -> (11,0) -> then needs to go down: pillar at (11,1) blocks.
# so use pillars at 1,3,5,7,9 only and let the path go (10,0)->(11,0)->(11,1)->(11,2)->(11,3) gap at x=11 in separator.
A = band(0, pillars=(1, 3, 5, 7, 9)) | separator(3, 11)
report("A band0-2 + sep3(gap 11)", A)
# Add band rows 4-6 traversed right-to-left: entering at (11,4). Mirror: pillars at odd x, blockers so that col 11 goes down first.
# From (11,3) down to (11,4),(11,5),(11,6) then left (10,6) up col 10 ... pillars at x=10,8,6,4,2 (even) with blockers.
def band_rl(y0, pillars=(10, 8, 6, 4, 2), blockers_top=(8, 4)):
    walls = set()
    for x in pillars:
        walls.add((x, y0 + 1))
        walls.add((x, y0) if x in blockers_top else (x, y0 + 2))
    return walls
B = A | band_rl(4) | separator(7, 0)
report("B two bands + sep7(gap 0)", B)
C = B | band(8, pillars=(1, 3, 5, 7, 9)) 
report("C three bands", C)
D = C | separator(11, 11)  # can't: row 11 contains base; skip
