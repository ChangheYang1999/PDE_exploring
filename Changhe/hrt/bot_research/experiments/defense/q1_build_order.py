"""Q1: long routes and their incremental build order.

For each layout (serpentine 1,3,5,7; serpentine + bottom wave; best annealed layouts from
runs/defense/layout_search_*.jsonl) print route length, cell count, splash adjacency summary, and an
incremental build order (greedy: at each step add the unbuilt cell that maximises the current route
length, ties by final adjacency) with the route length after every 5 cells. Every prefix of a legal
layout is legal (subset property), so the order is only about intermediate income.
Writes bot_research/runs/defense/q1_build_order.txt.
"""
import json

from bot_research.bots.defense.geometry import attackable_cells, render, route, splash_adjacency
from bot_research.bots.defense.plan import LAYOUT


def build_order(cells, lookahead=True):
    """Line-aware greedy: at each step add the unbuilt cell that maximises the route length obtainable
    after it plus one more best cell (2-step lookahead); single cells rarely lengthen a route because a
    line only deflects the route once it is closed. Ties: higher final adjacency."""
    cells = list(cells)
    final = route(set(cells))
    att = attackable_cells(final)
    fadj = {c: splash_adjacency(c, att) for c in cells}
    built, order, lens = set(), [], []
    while len(built) < len(cells):
        best = None
        rest = [c for c in cells if c not in built]
        for c in rest:
            base = built | {c}
            L1 = len(route(base)) - 1
            L2 = L1
            if lookahead and len(rest) > 1:
                L2 = max(len(route(base | {d})) - 1 for d in rest if d != c)
            key = (L1, L2, fadj[c])
            if best is None or key > best[0]:
                best = (key, c)
        built.add(best[1])
        order.append(best[1])
        lens.append(best[0][0])
    return order, lens, fadj


def report(name, cells, out):
    p = route(set(cells))
    att = attackable_cells(p)
    adj = sorted((splash_adjacency(c, att) for c in cells), reverse=True)
    out.append(f"=== {name}: cells={len(cells)} route={len(p)-1} top25adj={sum(adj[:25])} n>=6={sum(a >= 6 for a in adj)} hist={ {k: adj.count(k) for k in range(9) if adj.count(k)} }")
    out.append(render(set(cells), p))
    order, lens, fadj = build_order(cells)
    out.append("line-aware build order (cell: route after it):")
    out.append("  " + " ".join(f"{c}:{L}" for c, L in zip(order, lens)))
    out.append("route after every 5 cells: " + str(lens[4::5]) + f" final {lens[-1]}")
    gains = [(i + 1, L) for i, L in enumerate(lens) if i == 0 or L > lens[i - 1]]
    out.append("cells built -> route when it grows: " + str(gains))
    out.append("")


def main():
    out = []
    serp = [(x, y) for y, gap in ((1, 11), (3, 0), (5, 11), (7, 0)) for x in range(12) if x != gap]
    report("serpentine rows 1,3,5,7", serp, out)
    report("master layout (serpentine + bottom wave)", LAYOUT.cells, out)
    for fn in ("layout_search_length.jsonl", "layout_search_combo.jsonl"):
        try:
            recs = [json.loads(l) for l in open("bot_research/runs/defense/" + fn)]
        except FileNotFoundError:
            continue
        best = max(recs, key=lambda r: (r["metrics"]["L"], r["metrics"]["top25"]))
        report(f"annealed {fn} budget {best['budget']}", [tuple(c) for c in best["cells"]], out)
    text = "\n".join(out)
    print(text)
    open("bot_research/runs/defense/q1_build_order.txt", "w").write(text)


if __name__ == "__main__":
    main()
