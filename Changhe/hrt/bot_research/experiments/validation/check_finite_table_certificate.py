"""Positive and negative exact arithmetic fixtures for the ten-policy study."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.finite_table_certificate import propose, verify
from bot_research.experiments.validation.source_closure import static_closure


def main():
    zero = [[0] * 10 for _ in range(10)]
    pure = [[0] * 10 for _ in range(10)]
    for i in range(1, 10):
        pure[0][i] = 1
        pure[i][0] = -1
    rps = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    embedded = [[0] * 10 for _ in range(10)]
    for i in range(3):
        for j in range(3):
            embedded[i][j] = rps[i][j]
    for i in range(3):
        for j in range(3, 10):
            embedded[i][j] = 1
            embedded[j][i] = -1
    cases = []
    for name, matrix in [('zero10', zero), ('pure10', pure), ('rps3', rps), ('rps10', embedded)]:
        certificate = propose(matrix)
        assert certificate and verify(matrix, certificate['weights'])
        cases.append(dict(name=name, matrix=matrix, certificate=certificate))
    p = [Fraction(1, 3)] * 3 + [Fraction(0)] * 7
    assert verify(embedded, p)
    malformed = [row[:] for row in embedded]
    malformed[0][0] = 1
    negatives = dict(wrong_dimension=not verify(embedded, [1]),
                     wrong_sum=not verify(embedded, [0] * 10),
                     negative_weight=not verify(zero, [-1, 2] + [0] * 8),
                     losing_policy=not verify(embedded, [1] + [0] * 9),
                     nonskew_matrix=not verify(malformed, p))
    assert all(negatives.values())
    inputs = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in static_closure({
        'bot_research.experiments.validation.check_finite_table_certificate'})}
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), all_passed=True,
                  cases=cases, rejected_invalid_cases=negatives, input_sha256=inputs)
    atomic_json('bot_research/experiments/validation/analysis/ten_policy_game/verification/arithmetic_components.json', output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'all_passed', 'rejected_invalid_cases')}))


if __name__ == '__main__':
    main()
