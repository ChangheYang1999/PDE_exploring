"""Propose a finite-game policy mixture, then require an exact certificate."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog


def frac(value):
    return Fraction(value['numerator'], value['denominator'])


def rat(value):
    return {'numerator': value.numerator, 'denominator': value.denominator}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--matrix', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    source = Path(args.matrix)
    data = json.loads(source.read_text())
    exact = [[frac(v) for v in row] for row in data['matrix']]
    n = len(exact)
    assert data['all_replays_passed'] and len(data['policies']) == n
    assert all(len(row) == n for row in exact)
    assert all(exact[i][j] == -exact[j][i] for i in range(n) for j in range(n))
    matrix = np.array([[float(v) for v in row] for row in exact])
    result = linprog(np.r_[np.zeros(n), -1.0],
                     A_ub=np.column_stack([-matrix.T, np.ones(n)]), b_ub=np.zeros(n),
                     A_eq=np.array([np.r_[np.ones(n), 0.0]]), b_eq=np.ones(1),
                     bounds=[(0, None)] * n + [(None, None)], method='highs')
    assert result.success, result.message
    probabilities = [Fraction(float(v)).limit_denominator(1000000) for v in result.x[:n]]
    total = sum(probabilities)
    assert total > 0
    probabilities = [p / total for p in probabilities]
    margins = [sum((probabilities[i] * exact[i][j] for i in range(n)), Fraction(0)) for j in range(n)]
    assert all(p >= 0 for p in probabilities) and sum(probabilities) == 1
    assert all(m >= 0 for m in margins), 'Floating-point proposal did not yield an exact feasible vector.'
    pure_worst = [min(row) for row in exact]
    output = {'time_utc': datetime.now(timezone.utc).isoformat(),
              'matrix_path': str(source), 'matrix_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'solver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'policies': data['policies'], 'probabilities': [rat(p) for p in probabilities],
              'column_payoffs': [rat(m) for m in margins], 'exact_value': rat(Fraction(0)),
              'pure_worst_payoffs': [rat(v) for v in pure_worst],
              'support': [{'policy': name, 'probability': rat(p)} for name, p in zip(data['policies'], probabilities) if p],
              'all_exact_constraints_passed': True,
              'scope': 'Finite empirical table only. The opponent must select its policy without observing the sampled component. The table does not cover new opponents, scenarios or future nondeterministic outcomes.'}
    with Path(args.output).open('x') as stream:
        json.dump(output, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'support': output['support'], 'exact_value': output['exact_value'],
                      'best_pure_worst_payoff': rat(max(pure_worst))}))


if __name__ == '__main__':
    main()
