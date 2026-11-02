"""Propose small rational supports; verify certificates independently and exactly."""
from fractions import Fraction
from itertools import combinations
from bot_research.experiments.validation.publish_extended_counter_game import linear_solve


def verify(matrix, weights):
    n = len(matrix)
    if not n or len(weights) != n or any(len(row) != n for row in matrix):
        return False
    if any(type(v) is not int or v not in (-1, 0, 1) for row in matrix for v in row):
        return False
    if any(matrix[i][j] != -matrix[j][i] for i in range(n) for j in range(n)):
        return False
    p = [Fraction(x) for x in weights]
    if min(p) < 0 or sum(p) != 1:
        return False
    lower = [sum(p[i] * matrix[i][j] for i in range(n)) for j in range(n)]
    upper = [sum(matrix[i][j] * p[j] for j in range(n)) for i in range(n)]
    return min(lower) >= 0 and max(upper) <= 0


def propose(matrix):
    n = len(matrix)
    attempted = 0
    for size in range(1, n + 1):
        for support in combinations(range(n), size):
            for omitted in range(size):
                rows = [[1] * size]
                rows += [[matrix[i][j] for i in support]
                         for k, j in enumerate(support) if k != omitted]
                attempted += 1
                values = linear_solve(rows, [1] + [0] * (size - 1))
                if values is None:
                    continue
                weights = [Fraction(0)] * n
                for i, v in zip(support, values):
                    weights[i] = v
                if verify(matrix, weights):
                    payoffs = [sum(weights[i] * matrix[i][j] for i in range(n))
                               for j in range(n)]
                    return dict(weights=list(map(str, weights)),
                                column_payoffs=list(map(str, payoffs)),
                                exact_value='0', attempted_systems=attempted,
                                search_complete=False)
    return None
