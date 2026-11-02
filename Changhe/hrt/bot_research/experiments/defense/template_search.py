"""Anneal the slot assignment of the 59-cell structure (rows 1,3,5,7 + bottom snake) to maximise the
greedy S(k) sequence for small k subject to S(25) >= 1500.

Objective: sum_{k<=10} S(k) + 0.5 * sum_{11<=k<=20} S(k) - 2000 * max(0, 1500 - S(25))/10 + 3 * route(walls only).
State: set of 25 (or --slots N) slot cells among the 59; moves swap one slot with one wall cell.
Writes bot_research/runs/defense/template_search.jsonl (one line per seed) and prints the best.
Run: .venv/bin/python -B -m bot_research.experiments.defense.template_search --iters 1500 --seeds 2
"""
import argparse
import json
import math
import random
import time

from bot_research.experiments.defense.template_eval import greedy_sequence, report
from bot_research.experiments.defense.template_pillars import pillars_template, snake
from bot_research.bots.defense.geometry import route

STRUCT = [(x, y) for y, gap in ((1, 11), (3, 0), (5, 11), (7, 0)) for x in range(12) if x != gap] + snake()


ROUTE_WEIGHT = 3.0
GUN_WEIGHT = 0.0


def free_gun_coverage(walls, slots):
    """Sum of the two best gun3 coverages (route cells within 3.5) over cells that are neither wall, slot
    nor on the final route, measured with every wall and slot built."""
    from bot_research.bots.defense.geometry import attackable_cells, gun_cells
    full = set(walls) | set(slots)
    p = route(full)
    att = attackable_cells(p)
    free = [(x, y) for x in range(12) for y in range(12) if (x, y) not in full and (x, y) not in set(p) and (x, y) not in ((0, 0), (11, 11))]
    cov = sorted((gun_cells(c, 3.5, att) for c in free), reverse=True)
    return sum(cov[:2])


def objective(slots):
    walls = [c for c in STRUCT if c not in slots]
    seq = greedy_sequence(walls, list(slots))
    S = [s for _, s, _ in seq]
    if len(S) < 25:
        return -1e9, S, 0
    L0 = len(route(set(walls))) - 1
    val = sum(S[:10]) + 0.5 * sum(S[10:20]) - 2000 * max(0, 1500 - S[24]) / 10 + ROUTE_WEIGHT * L0
    if GUN_WEIGHT:
        val += GUN_WEIGHT * free_gun_coverage(walls, slots)
    return val, S, L0


def anneal(n_slots, iters, seed):
    rnd = random.Random(seed)
    walls0, slots0 = pillars_template(n_bulk_per_row=7, extra_snake=((1, 9), (3, 10), (5, 9), (7, 10)))
    slots = set(slots0)
    while len(slots) > n_slots:
        slots.remove(rnd.choice(sorted(slots)))
    while len(slots) < n_slots:
        slots.add(rnd.choice([c for c in STRUCT if c not in slots]))
    cur, S, L0 = objective(slots)
    best = (cur, set(slots), S, L0)
    T0, T1 = 60.0, 2.0
    for i in range(iters):
        T = T0 * (T1 / T0) ** (i / iters)
        trial = set(slots)
        trial.remove(rnd.choice(sorted(trial)))
        trial.add(rnd.choice([c for c in STRUCT if c not in trial]))
        val, S2, L2 = objective(trial)
        if val >= cur or rnd.random() < math.exp((val - cur) / T):
            slots, cur = trial, val
            if val > best[0]:
                best = (val, set(trial), S2, L2)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iters", type=int, default=1500)
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--slots", type=int, default=25)
    ap.add_argument("--route-weight", type=float, default=3.0)
    ap.add_argument("--gun-weight", type=float, default=0.0)
    a = ap.parse_args()
    global ROUTE_WEIGHT, GUN_WEIGHT
    ROUTE_WEIGHT = a.route_weight
    GUN_WEIGHT = a.gun_weight
    overall = None
    with open("bot_research/runs/defense/template_search.jsonl", "a") as f:
        for seed in range(a.seeds):
            t = time.time()
            val, slots, S, L0 = anneal(a.slots, a.iters, seed)
            rec = {"seed": seed, "iters": a.iters, "n_slots": a.slots, "route_weight": a.route_weight, "gun_weight": a.gun_weight,
                   "free_gun_cov2": free_gun_coverage([c for c in STRUCT if c not in slots], slots), "objective": val, "S": S, "route_walls_only": L0,
                   "slots": sorted(slots), "walls": sorted(c for c in STRUCT if c not in slots), "seconds": round(time.time() - t, 1)}
            f.write(json.dumps(rec) + "\n"); f.flush()
            print(json.dumps({k: v for k, v in rec.items() if k not in ("slots", "walls")}))
            if overall is None or val > overall[0]:
                overall = (val, slots)
    walls = [c for c in STRUCT if c not in overall[1]]
    report("best annealed template", tuple(walls), tuple(sorted(overall[1])))


if __name__ == "__main__":
    main()
