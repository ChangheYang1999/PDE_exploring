"""Candidate interfaces for square character grids; default map size is 12."""

from __future__ import annotations


def shortest_path_length(grid: list[list[str]]) -> int | None:
    """Return the fewest cardinal moves between a square grid's corners.

    Accept the map's character grid, indexed grid[y][x]. '.', 'S', and 'B'
    are walkable; all other single-character strings are blocked, including
    '#' walls and turret symbols. Start is (0, 0); goal is (n - 1, n - 1).
    Return None if either endpoint is blocked or the goal is unreachable.
    Raise ValueError unless the grid is a nonempty square list of lists of
    single-character strings. Do not modify the input.
    """
    raise NotImplementedError("TODO: implement shortest_path_length")


def best_wall_placement(size: int = 12) -> tuple[set[tuple[int, int]], int]:
    """Return (wall coordinates, shortest length) for an initially empty grid.

    Use a size × size grid with no wall-count limit. Leave (0, 0) and
    (size - 1, size - 1) open and connected; wall coordinates are (x, y).
    Maximize the shortest cardinal path length; any optimal placement is valid.
    Raise TypeError for a non-integer size (including bool), or ValueError
    for a size less than 1. The default size is 12.
    """
    raise NotImplementedError("TODO: implement best_wall_placement")
