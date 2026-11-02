"""Evaluate bots/defense/replan.py on scripted-opening maps (lead request 2026-10-31T08:10Z).

For each scenario the opening is generated exactly as the harness does (play_match with idle bots and the
scenario; the snapshot of the last scripted round gives both players' maps), then for each player's map:
the broken master layout (plan_walls on the default layout, all walls, slots filled greedily) and the re-planned
layout are compared: final route length, number of new walls, S_final (all slots splashes), the greedy S(k) sequence
(template_eval.greedy_sequence: walls built, then slots one by one in the order that maximises S on the route as it
is), the cost (walls + 60 per splash) to reach S >= 560 and S >= 1500, and the re-planning time.
Also: the lead's development log runs/lead/dev/scen/V4f_vs_econ17_mirror-1-2_seat0.jsonl, seat 0, rounds 3-12.
Writes runs/defense/replan_eval/report.md and maps.json.
Run: PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp .venv/bin/python -B -m bot_research.experiments.defense.replan_eval
"""
import json
import os
import time

from bot_research.harness.match import play_match
from bot_research.bots.defense import replan as R
from bot_research.bots.defense import plan as P
from bot_research.bots.defense.geometry import route, attackable_cells, splash_adjacency
from bot_research.experiments.defense.template_eval import greedy_sequence

OUT = "bot_research/runs/defense/replan_eval"
SCENARIOS = ["mirror:1:2", "asym:3:2", "mirror:22:3", "asym:23:2"]
LEAD_LOG = "bot_research/runs/lead/dev/scen/V4f_vs_econ17_mirror-1-2_seat0.jsonl"


def scenario_maps(name):
    k = int(name.split(":")[-1])
    out = f"{OUT}/opening_{name.replace(':', '-')}.jsonl"
    if not os.path.exists(out):
        play_match("td_bots.protocol:idle", "td_bots.protocol:idle", out, scenario=name)
    maps = {}
    for line in open(out):
        r = json.loads(line)
        if r["round"] == k:
            maps[r["player"]] = r["snapshot"]["buildings"]
    return maps


def seq_costs(fixed_walls, slots, fixed_splash=()):
    """Greedy S(k) with the walls built; returns list of S and the number of splashes to reach 560 / 1500."""
    seq = greedy_sequence(list(fixed_walls), list(slots))
    S = [s for _, s, _ in seq]
    base = 0
    if fixed_splash:
        p = route(set(fixed_walls))
        att = attackable_cells(p)
        base = 10 * sum(splash_adjacency(c, att) for c in fixed_splash)
    S = [s + base for s in S]
    def n_for(th):
        for i, s in enumerate(S):
            if s >= th:
                return i + 1
        return None
    return S, n_for(560), n_for(1500)


def analyse(buildings, label, iters=4000):
    fixed = {(b["x"], b["y"]) for b in buildings}
    fixed_splash = [(b["x"], b["y"]) for b in buildings if b["type"] == "splash"]
    rows = []
    # broken master layout: legal walls of the default order, then its reserved slots that are still legal
    lay0 = P.LAYOUT
    cur = set(fixed)
    walls0 = []
    for c in lay0.wall_order:
        if c not in cur and route(cur | {c}) is not None:
            walls0.append(c); cur.add(c)
    slots0 = []
    for c in lay0.splash_cells:
        if c not in cur and route(cur | {c}) is not None:
            slots0.append(c); cur.add(c)
    S0, n560_0, n1500_0 = seq_costs(fixed | set(walls0), slots0, fixed_splash)
    rows.append(dict(layout="default(broken)", route=len(route(fixed | set(walls0) | set(slots0))) - 1, route_walls_only=len(route(fixed | set(walls0))) - 1, walls=len(walls0),
                     slots=len(slots0), S_final=S0[-1] if S0 else 0, S=S0, n560=n560_0, n1500=n1500_0, secs=0.0))
    for objective, n_slots in (("exposure", 25), ("route", 25), ("route", 0)):
        t = time.time()
        lay = R.replan_layout(buildings, iters=iters, seed=0, objective=objective, n_slots=n_slots)
        dt = time.time() - t
        S1, n560_1, n1500_1 = seq_costs(fixed | set(lay.wall_order), lay.splash_cells, fixed_splash)
        p_walls = route(fixed | set(lay.wall_order))
        rows.append(dict(layout="replan:" + objective + (",walls only" if n_slots == 0 else ""), route=lay.final_len, route_walls_only=len(p_walls) - 1,
                         walls=len(lay.wall_order), slots=len(lay.splash_cells),
                         S_final=S1[-1] if S1 else 0, S=S1, n560=n560_1, n1500=n1500_1, secs=round(dt, 1),
                         walls_list=lay.wall_order, slots_list=lay.splash_cells))
    return dict(label=label, fixed=sorted(fixed), n_fixed=len(fixed), rows=rows)


def main():
    os.makedirs(OUT, exist_ok=True)
    results = []
    for name in SCENARIOS:
        maps = scenario_maps(name)
        for p in sorted(maps):
            results.append(analyse(maps[p], f"{name} seat {p}"))
            print(results[-1]["label"], [(r["layout"], r.get("route_walls_only"), r["route"], r["walls"], r["slots"], r["S_final"], r["n560"], r["n1500"], r["secs"]) for r in results[-1]["rows"]], flush=True)
    if os.path.exists(LEAD_LOG):
        for line in open(LEAD_LOG):
            r = json.loads(line)
            if r["player"] == 0 and 3 <= r["round"] <= 12:
                results.append(analyse(r["snapshot"]["buildings"], f"lead log seat 0 round {r['round']}"))
                print(results[-1]["label"], [(x["layout"], x.get("route_walls_only"), x["route"], x["walls"], x["slots"], x["S_final"], x["n560"], x["n1500"], x["secs"]) for x in results[-1]["rows"]], flush=True)
    json.dump(results, open(f"{OUT}/maps.json", "w"), indent=1)
    with open(f"{OUT}/report.md", "w") as f:
        f.write("# replan_eval: broken master layout vs re-planned layout on scripted-opening maps\n\n")
        f.write("Columns: final route length (all walls and slots built), new walls, slots, S_final (10 x adjacency sum of all slots on the final route),\n")
        f.write("splashes needed for S >= 560 and S >= 1500 in the greedy order (None = unreachable), re-planning seconds. Cost = walls x 1 + splashes x 60.\n\n")
        f.write("| map | fixed cells | layout | route (walls only) | route (all) | walls | slots | S_final | n(560) | n(1500) | secs | S(k) k=1..10 |\n|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|\n")
        for res in results:
            for r in res["rows"]:
                f.write(f"| {res['label']} | {res['n_fixed']} | {r['layout']} | {r.get('route_walls_only')} | {r['route']} | {r['walls']} | {r['slots']} | {r['S_final']} | {r['n560']} | {r['n1500']} | {r['secs']} | {r['S'][:10]} |\n")
    print("written", OUT)


if __name__ == "__main__":
    main()
