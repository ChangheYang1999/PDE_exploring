# Pathfinding interview

Implement the two functions in `problems.py`. Both currently raise
`NotImplementedError`. Coordinates are `(x, y)`; grids are indexed `[y][x]`.

## `shortest_path_length(grid) -> int | None`

Return the fewest cardinal moves from `(0, 0)` to `(n - 1, n - 1)` on a
nonempty square character grid. `.`, `S`, and `B` are walkable; other
characters are blocked. Return `None` when an endpoint is blocked or the
goal is unreachable. Raise `ValueError` for an invalid grid. Do not modify
the input.

## `best_wall_placement(size=12)`

On an initially empty square grid, return wall coordinates and the resulting
shortest cardinal path length. There is no wall-count limit. Keep both
corners open and connected, and maximize the shortest path length. Any
optimal placement is valid. Raise `TypeError` for a non-integer size,
including `bool`, and `ValueError` for a size below 1.

See the function docstrings for the complete input and return contracts.
