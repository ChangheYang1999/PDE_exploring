"""Exact maximum induced linear forest in a set of grid cells (4-neighbour graph).

A route is a BFS shortest path, so two route cells that are 4-neighbours are
consecutive on the route (otherwise the route could be shortened). Hence the
route cells inside any region induce a linear forest (a disjoint union of
paths) in the 4-neighbour grid graph, and the number of route cells within a
gun's range is at most the maximum induced linear forest of the in-range cells.

Usage: python3 induced_forest.py   (prints the values for ranges 2.5, 3.0, 3.5
and for the full 12x12 grid's 2x2-block bound)
"""
from __future__ import annotations

import sys
import time


def disc(radius):
    r2 = radius * radius
    k = int(radius) + 1
    return [(dx, dy) for dx in range(-k, k + 1) for dy in range(-k, k + 1)
            if (dx, dy) != (0, 0) and dx * dx + dy * dy <= r2]


def max_induced_linear_forest(cells):
    cells = sorted(cells, key=lambda c: (c[1], c[0]))
    idx = {c: i for i, c in enumerate(cells)}
    n = len(cells)
    nbrs = [[idx[(c[0] + dx, c[1] + dy)] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
             if (c[0] + dx, c[1] + dy) in idx] for c in cells]
    best = [0, None]
    chosen = [False] * n
    deg = [0] * n

    def find(parent, a):
        while parent[a] != a:
            a = parent[a]
        return a

    def rec(i, count, parent):
        if count + (n - i) <= best[0]:
            return
        if i == n:
            best[0] = count
            best[1] = [cells[j] for j in range(n) if chosen[j]]
            return
        # try include
        cn = [j for j in nbrs[i] if chosen[j]]
        ok = len(cn) <= 2 and all(deg[j] < 2 for j in cn)
        if ok:
            roots = [find(parent, j) for j in cn]
            if len(set(roots)) == len(roots):
                p2 = parent[:]
                for r in roots:
                    p2[r] = i
                chosen[i] = True
                for j in cn:
                    deg[j] += 1
                deg[i] = len(cn)
                rec(i + 1, count + 1, p2)
                chosen[i] = False
                for j in cn:
                    deg[j] -= 1
                deg[i] = 0
        rec(i + 1, count, parent)

    rec(0, 0, list(range(n)))
    return best[0], best[1]


def main():
    for r in (2.5, 3.0, 3.5):
        t = time.time()
        cells = disc(r)
        v, sol = max_induced_linear_forest(cells)
        print(f"range {r}: {len(cells)} cells in range, max induced linear forest {v} "
              f"({time.time() - t:.1f}s)", flush=True)
    print("12x12 grid, 36 disjoint 2x2 blocks with at most 3 route cells each: route cells <= 108")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
