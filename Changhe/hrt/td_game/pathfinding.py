"""Grid routing for the game runtime. Coordinates are (x, y)."""
from collections import deque
from collections.abc import Iterable

NEIGHBORS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def shortest_path(
    width: int, height: int, blocked: Iterable[tuple[int, int]],
    spawn: tuple[int, int], base: tuple[int, int],
) -> list[tuple[int, int]] | None:
    obstacles = set(blocked)
    if spawn in obstacles or base in obstacles:
        return None
    parents = {spawn: None}
    queue = deque([spawn])
    while queue:
        x, y = queue.popleft()
        if (x, y) == base:
            path = []
            cell = base
            while cell is not None:
                path.append(cell)
                cell = parents[cell]
            return path[::-1]
        for dx, dy in NEIGHBORS:
            cell = (x + dx, y + dy)
            if 0 <= cell[0] < width and 0 <= cell[1] < height and cell not in obstacles and cell not in parents:
                parents[cell] = (x, y)
                queue.append(cell)
    return None
