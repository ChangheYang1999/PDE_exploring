"""Search for the longest engine route for a given wall budget (simulated annealing).

Writes results to bot_research/runs/defense/path_length_search.txt. Run from the project root:
  .venv/bin/python -B -m bot_research.experiments.defense.path_length_search [budget ...]
"""
import math
import random
import sys
import time

from bot_research.bots.defense.geometry import W, H, SPAWN, BASE, path_len, render, route

CELLS = [(x, y) for x in range(W) for y in range(H) if (x, y) not in (SPAWN, BASE)]


def anneal(budget: int, iters: int, seed: int, init=None):
    rnd = random.Random(seed)
    blocked = set(init or [])
    best_len = cur = path_len(blocked) or 0
    best = set(blocked)
    T0, T1 = 2.0, 0.05
    for i in range(iters):
        T = T0 * (T1 / T0) ** (i / iters)
        trial = set(blocked)
        move = rnd.random()
        if move < 0.45 and len(trial) < budget:
            trial.add(rnd.choice(CELLS))
        elif move < 0.7 and trial:
            trial.remove(rnd.choice(sorted(trial)))
        elif trial:
            trial.remove(rnd.choice(sorted(trial)))
            trial.add(rnd.choice(CELLS))
        else:
            trial.add(rnd.choice(CELLS))
        if len(trial) > budget:
            continue
        L = path_len(trial)
        if L is None:
            continue
        if L >= cur or rnd.random() < math.exp((L - cur) / T):
            blocked, cur = trial, L
            if L > best_len or (L == best_len and len(trial) < len(best)):
                best_len, best = L, set(trial)
    return best_len, best


def main():
    budgets = [int(a) for a in sys.argv[1:]] or [10, 22, 30, 44, 55, 70, 90]
    out = []
    for b in budgets:
        t = time.time()
        results = []
        for seed in range(3):
            results.append(anneal(b, 40000, seed))
        L, cells = max(results, key=lambda r: (r[0], -len(r[1])))
        out.append(f"budget={b} best_len={L} walls_used={len(cells)} seeds=3 iters=40000 time={time.time()-t:.1f}s")
        out.append(render(cells, route(cells)))
        out.append('')
        print(out[-3])
    with open('bot_research/runs/defense/path_length_search.txt', 'w') as f:
        f.write('\n'.join(out))


if __name__ == '__main__':
    main()
