"""A bounded deterministic search over legal ordered minion purchases.

The model is the already validated local combat simulator. Search scores are
predictions; authoritative matches and forecast checks are recorded elsewhere.
"""
from __future__ import annotations
import random
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate


def search_package(buildings, rules, prefix, budget, *, evaluations=192, seed=0, count_cap=200):
    if budget < 0 or evaluations < 1 or count_cap < 1:
        raise ValueError('Nonnegative budget and positive search limits are required.')
    costs = {kind: stats['cost'] for kind, stats in rules['minions'].items()}
    kinds = sorted(costs, key=lambda kind: (costs[kind], kind))
    model = MapModel(buildings, rules)
    base = simulate(model, list(prefix), rules)[1]
    cache = {}
    best = ()
    best_rank = (0, 0, 0, ())
    rng = random.Random(seed)

    def examine(package):
        nonlocal best, best_rank
        package = tuple(package)
        cost = sum(costs[kind] for kind in package)
        if cost > budget or len(package) > count_cap:
            raise ValueError('Search proposed an infeasible package.')
        if package in cache or len(cache) >= evaluations:
            return
        damage = simulate(model, list(prefix) + list(package), rules)[1]
        rank = (damage - base, -cost, -len(package), package)
        cache[package] = (damage, cost)
        if rank > best_rank:
            best, best_rank = package, rank

    examine(())
    # Pure-tiers are mandatory controls. Intermediate sizes can arrive before
    # the combat cutoff even when a longer stream would be partly wasted.
    for kind in reversed(kinds):
        maximum = min(count_cap, budget // costs[kind])
        for count in sorted({1, maximum // 2, maximum}):
            if 0 < count <= maximum:
                examine([kind] * count)
    # Two-tier mixtures in opposite orders.
    for first in kinds:
        for second in kinds:
            if first == second:
                continue
            for numerator in (1, 2, 3):
                n_first = min(count_cap, (budget * numerator // 4) // costs[first])
                left = budget - n_first * costs[first]
                n_second = min(count_cap - n_first, left // costs[second])
                a, b = [first] * n_first, [second] * n_second
                examine(a + b)
                examine(b + a)
                if len(cache) >= evaluations // 2:
                    break
            if len(cache) >= evaluations // 2:
                break
        if len(cache) >= evaluations // 2:
            break
    # Random mutations are seeded and constrained by a fixed evaluation count,
    # never by wall-clock time. Restarting avoids a purely local order search.
    tries = 0
    while len(cache) < evaluations and tries < evaluations * 20:
        tries += 1
        if best and rng.random() < 0.75:
            proposal = list(best)
            mode = rng.randrange(5)
            if mode == 0 and len(proposal) >= 2:
                i, j = rng.sample(range(len(proposal)), 2)
                proposal[i], proposal[j] = proposal[j], proposal[i]
            elif mode == 1 and len(proposal) >= 2:
                i, j = sorted(rng.sample(range(len(proposal) + 1), 2))
                proposal[i:j] = reversed(proposal[i:j])
            elif mode == 2:
                for _ in range(min(len(proposal), rng.randint(1, 4))):
                    proposal.pop(rng.randrange(len(proposal)))
            elif mode == 3 and proposal:
                proposal.pop(rng.randrange(len(proposal)))
            else:
                rng.shuffle(proposal)
        else:
            proposal = []
        left = budget - sum(costs[kind] for kind in proposal)
        target = min(count_cap, len(proposal) + rng.randint(1, max(1, count_cap - len(proposal))))
        while len(proposal) < target:
            affordable = [kind for kind in kinds if costs[kind] <= left]
            if not affordable:
                break
            kind = rng.choice(affordable)
            proposal.insert(rng.randrange(len(proposal) + 1), kind)
            left -= costs[kind]
            if rng.random() < 0.05:
                break
        examine(proposal)
    return list(best), {'evaluations': len(cache), 'evaluation_limit': evaluations,
                        'seed': seed, 'baseline_damage': base,
                        'predicted_damage': base + best_rank[0],
                        'predicted_gain': best_rank[0], 'cost': -best_rank[1],
                        'package': list(best), 'attempts': tries}
