"""Map geometry for the defender: paths, serpentine templates, splash/gun coverage.

Coordinates are (x, y); x is the column, y the row. Spawn (0, 0), base (11, 11).
The route is the engine's own BFS (td_game.pathfinding.shortest_path), so every
length or coverage computed here is exactly what the engine will use.
"""
from __future__ import annotations

from td_game.pathfinding import shortest_path

W = H = 12
SPAWN = (0, 0)
BASE = (11, 11)
N8 = tuple((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))


def route(blocked) -> list[tuple[int, int]] | None:
    """Engine route for a set of blocked cells (None if disconnected)."""
    return shortest_path(W, H, blocked, SPAWN, BASE)


def path_len(blocked) -> int | None:
    p = route(blocked)
    return None if p is None else len(p) - 1


def in_grid(x: int, y: int) -> bool:
    return 0 <= x < W and 0 <= y < H


def attackable_cells(path) -> set[tuple[int, int]]:
    """Path cells on which a copy can be attacked: all except the base (arrival removes it)."""
    return set(path[:-1])


def splash_adjacency(cell, attackable) -> int:
    """Number of attackable path cells among the eight neighbours of `cell`."""
    x, y = cell
    return sum((x + dx, y + dy) in attackable for dx, dy in N8)


def gun_cells(cell, rng: float, attackable) -> int:
    """Number of attackable path cells within Euclidean range (boundary included)."""
    x, y = cell
    r2 = rng * rng
    return sum((px - x) ** 2 + (py - y) ** 2 <= r2 for (px, py) in attackable)


def render(blocked, path=None, marks: dict | None = None) -> str:
    grid = [['.' for _ in range(W)] for _ in range(H)]
    for (x, y) in blocked:
        grid[y][x] = '#'
    if marks:
        for (x, y), ch in marks.items():
            grid[y][x] = ch
    if path:
        for (x, y) in path:
            if grid[y][x] == '.':
                grid[y][x] = '+'
    grid[0][0] = 'S'
    grid[H - 1][W - 1] = 'B'
    return '\n'.join(''.join(row) for row in grid)


def serpentine(orientation: str, lines: tuple[int, ...], first_gap: str) -> list[list[tuple[int, int]]]:
    """Wall lines of a serpentine maze, each as an ordered list of cells.

    orientation 'v': wall columns at x in `lines`, gaps alternate bottom/top starting
    with first_gap in {'far', 'near'} ('far' = gap at the end away from the spawn, i.e.
    y = 11 for the first vertical line). orientation 'h': wall rows, gaps alternate
    right/left ('far' = x = 11 for the first row).
    """
    result = []
    gap_far = first_gap == 'far'
    for line in lines:
        cells = []
        for t in range(12):
            gap_t = 11 if gap_far else 0
            if t == gap_t:
                continue
            cells.append((line, t) if orientation == 'v' else (t, line))
        result.append(cells)
        gap_far = not gap_far
    return result


def flatten(lines) -> list[tuple[int, int]]:
    return [c for line in lines for c in line]
