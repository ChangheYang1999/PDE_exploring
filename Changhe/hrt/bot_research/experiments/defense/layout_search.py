"""Simulated annealing over blocked-cell sets for defensive master layouts.

Objectives (per run, chosen by --objective):
  length   : maximise route length L (walls <= budget)
  combo    : maximise L + beta * top-k splash adjacency sum (k = --k)
Outputs JSON lines to bot_research/runs/defense/layout_search_<objective>.jsonl with the
layout (sorted cell list), L, adjacency histogram, top-k sums, gun3 best coverage.
Run from the project root:
  .venv/bin/python -B -m bot_research.experiments.defense.layout_search --objective length --budgets 30 45 60 --iters 200000 --seeds 4
"""
import argparse
import json
import math
import random
import time

from bot_research.bots.defense.geometry import (W, H, SPAWN, BASE, attackable_cells, gun_cells, render, route,
                                                 splash_adjacency)

CELLS = [(x, y) for x in range(W) for y in range(H) if (x, y) not in (SPAWN, BASE)]


def metrics(blocked, k=25):
    path = route(blocked)
    if path is None:
        return None
    att = attackable_cells(path)
    adj = sorted((splash_adjacency(c, att) for c in blocked), reverse=True)
    topk = sum(adj[:k])
    return {"L": len(path) - 1, "walls": len(blocked), "topk": topk, "k": k,
            "hist": {str(a): adj.count(a) for a in range(9) if adj.count(a)},
            "top19": sum(adj[:19]), "top25": sum(adj[:25]), "top30": sum(adj[:30]),
            "gun3_best": max((gun_cells(c, 3.5, att) for c in blocked), default=0)}


def score(blocked, objective, beta, k):
    m = metrics(blocked, k)
    if m is None:
        return None, None
    if objective == "length":
        return m["L"], m
    return m["L"] + beta * m["topk"], m


def anneal(budget, iters, seed, objective, beta, k, init=None):
    rnd = random.Random(seed)
    blocked = set(init or [])
    cur, m = score(blocked, objective, beta, k)
    best, best_set, best_m = cur, set(blocked), m
    T0, T1 = 3.0, 0.05
    for i in range(iters):
        T = T0 * (T1 / T0) ** (i / iters)
        trial = set(blocked)
        r = rnd.random()
        if r < 0.4 and len(trial) < budget:
            trial.add(rnd.choice(CELLS))
        elif r < 0.6 and trial:
            trial.remove(rnd.choice(tuple(trial)))
        elif trial:
            trial.remove(rnd.choice(tuple(trial)))
            trial.add(rnd.choice(CELLS))
        else:
            trial.add(rnd.choice(CELLS))
        if len(trial) > budget:
            continue
        s, tm = score(trial, objective, beta, k)
        if s is None:
            continue
        if s >= cur or rnd.random() < math.exp((s - cur) / T):
            blocked, cur, m = trial, s, tm
            if s > best or (s == best and len(trial) < len(best_set)):
                best, best_set, best_m = s, set(trial), tm
    return best, best_set, best_m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--objective", default="length", choices=["length", "combo"])
    ap.add_argument("--budgets", type=int, nargs="+", default=[45])
    ap.add_argument("--iters", type=int, default=100000)
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--beta", type=float, default=1.0)
    ap.add_argument("--k", type=int, default=25)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    out = f"bot_research/runs/defense/layout_search_{a.objective}{a.tag}.jsonl"
    with open(out, "a") as f:
        for b in a.budgets:
            t = time.time()
            best = None
            for seed in range(a.seeds):
                s, cells, m = anneal(b, a.iters, seed, a.objective, a.beta, a.k)
                if best is None or s > best[0]:
                    best = (s, cells, m)
            s, cells, m = best
            rec = {"objective": a.objective, "beta": a.beta, "budget": b, "iters": a.iters, "seeds": a.seeds,
                   "score": s, "metrics": m, "cells": sorted(cells), "seconds": round(time.time() - t, 1)}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            print(json.dumps({kk: vv for kk, vv in rec.items() if kk != "cells"}))
            print(render(cells, route(cells)))


if __name__ == "__main__":
    main()
