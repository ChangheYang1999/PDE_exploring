"""Exploratory: default path, serpentine mazes, path length per wall under the engine BFS.
Run from the project root with the project venv (python -B)."""
from td_game.pathfinding import shortest_path

W = H = 12
SPAWN, BASE = (0, 0), (11, 11)


def path(blocked):
    return shortest_path(W, H, blocked, SPAWN, BASE)


def render(blocked, p=None, marks=None):
    grid = [['.' for _ in range(W)] for _ in range(H)]
    for (x, y) in blocked:
        grid[y][x] = '#'
    if marks:
        for (x, y), ch in marks.items():
            grid[y][x] = ch
    if p:
        for i, (x, y) in enumerate(p):
            if grid[y][x] == '.':
                grid[y][x] = '+'
    grid[0][0] = 'S'
    grid[11][11] = 'B'
    return '\n'.join(''.join(row) for row in grid)


def serpentine_rows(wall_rows, gap_side):
    """Walls on full rows except one gap cell; gap_side alternates 'right'/'left'."""
    blocked = set()
    for i, r in enumerate(wall_rows):
        side = gap_side[i % len(gap_side)]
        gap_x = 11 if side == 'R' else 0
        for x in range(W):
            if x != gap_x:
                blocked.add((x, r))
    return blocked


p0 = path(set())
print("default path", len(p0) - 1, p0)
print(render(set(), p0))

for rows, sides in [((1, 3, 5, 7, 9), 'RL'), ((1, 3, 5, 7, 9), 'LR'), ((2, 4, 6, 8, 10), 'RL'), ((2, 4, 6, 8, 10), 'LR'), ((1, 3, 5, 7, 9, 10), 'RL')]:
    b = serpentine_rows(rows, sides)
    p = path(b)
    print(f"\nrows={rows} sides={sides} walls={len(b)} len={None if p is None else len(p)-1}")
    if p:
        print(render(b, p))
