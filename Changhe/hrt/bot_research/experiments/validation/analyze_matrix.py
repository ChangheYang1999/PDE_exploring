"""Offline analysis of a completed deterministic payoff matrix; runs no game."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linprog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rows = [json.loads(line) for line in Path(args.input).read_text().splitlines()]
    by_pair = {tuple(row['bot_specs']): row for row in rows}
    names = sorted({a for a, b in by_pair})
    assert len(by_pair) == len(names) ** 2, 'A full matrix is required.'
    matrix = np.array([[0.5 if by_pair[a, b]['result']['winner'] is None else float(by_pair[a, b]['result']['winner'] == 0)
                        for b in names] for a in names])
    assert np.array_equal(matrix + matrix.T, np.ones_like(matrix)), 'Assignment invariance failed.'
    symmetry = []
    for a, b in itertools.combinations(names, 2):
        first, second = by_pair[a, b], by_pair[b, a]
        same = first['rounds'] == second['rounds'] and first['hp'] == second['hp'][::-1]
        same = same and first['accepted_actions'] == second['accepted_actions'][::-1]
        same = same and first['rejected_actions'] == second['rejected_actions'][::-1]
        same = same and first['history'] == [{'round': h['round'], 'players': h['players'][::-1]} for h in second['history']]
        symmetry.append({'pair': [a, b], 'agrees': same})
    assert all(item['agrees'] for item in symmetry)
    cycles = []
    for a, b, c in itertools.combinations(range(len(names)), 3):
        for x, y, z in ((a, b, c), (a, c, b)):
            if matrix[x, y] == matrix[y, z] == matrix[z, x] == 1:
                cycles.append([names[x], names[y], names[z]])
    n = len(names)
    solution = linprog(np.r_[np.zeros(n), -1], A_ub=np.column_stack((-matrix.T, np.ones(n))),
                      b_ub=np.zeros(n), A_eq=np.array([np.r_[np.ones(n), 0]]), b_eq=[1],
                      bounds=[(0, 1)] * (n + 1), method='highs')
    assert solution.success, solution.message
    weights = [Fraction(float(x)).limit_denominator(10000) for x in solution.x[:n]]
    exact_payoffs = [sum(weights[i] * Fraction(float(matrix[i, j])) for i in range(n)) for j in range(n)]
    exact_valid = sum(weights) == 1 and all(x >= 0 for x in weights) and min(exact_payoffs) >= Fraction(1, 2)
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'source_input': args.input,
              'input_sha256': hashlib.sha256(Path(args.input).read_bytes()).hexdigest(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'numpy_version': np.__version__, 'scipy_version': scipy.__version__,
              'names': names, 'payoffs': matrix.tolist(), 'assignment_symmetry': symmetry,
              'strict_three_cycles': cycles,
              'numerical_maximin_value': float(solution.x[-1]),
              'portfolio': {name: str(weight) for name, weight in zip(names, weights) if weight},
              'exact_fraction_certificate_valid': exact_valid,
              'exact_payoff_against_each_column': {name: str(value) for name, value in zip(names, exact_payoffs)},
              'scope': 'Finite empirical strategy matrix only. No uncertainty estimate or whole-game optimality claim.'}
    with Path(args.output).open('x') as stream:
        json.dump(output, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: output[k] for k in ('portfolio', 'numerical_maximin_value', 'exact_fraction_certificate_valid')}))


if __name__ == '__main__':
    main()
