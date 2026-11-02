"""Seven-dimensional checks for exact finite-game certificates."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.publish_extended_counter_game import exact_certificate


def main():
    labels = [0, 0, 0, 1, 1, 2, 2]
    cycle = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    matrices = {
        'zero': [[0] * 7 for _ in range(7)],
        'pure_first': [[0 if i == j else 1 if i == 0 else -1 if j == 0 else 0
                        for j in range(7)] for i in range(7)],
        'replicated_cycle': [[cycle[labels[i]][labels[j]] for j in range(7)] for i in range(7)],
    }
    cases = []
    for name, matrix in matrices.items():
        certificate = exact_certificate(matrix)
        assert certificate is not None
        weights = list(map(Fraction, certificate['weights']))
        assert len(weights) == 7 and sum(weights) == 1 and min(weights) >= 0
        assert certificate['checked_active_sets'] == 3003
        assert all(sum(weights[i] * matrix[i][j] for i in range(7)) >= 0 for j in range(7))
        if name == 'pure_first':
            assert weights == [1, 0, 0, 0, 0, 0, 0]
        if name == 'replicated_cycle':
            assert [sum(weights[i] for i in range(7) if labels[i] == k) for k in range(3)] == [Fraction(1, 3)] * 3
        cases.append(dict(name=name, matrix=matrix, certificate=certificate))
    root = Path('bot_research/experiments/validation')
    sources = [root / 'publish_extended_counter_game.py', Path(__file__).relative_to(Path.cwd())]
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), all_passed=True, cases=cases,
                  input_sha256={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources})
    atomic_json(root / 'analysis/seven_policy_game/verification/arithmetic_components.json', result, exclusive=True)
    print(json.dumps(dict(all_passed=True, cases=len(cases), active_sets_per_case=3003)), flush=True)


if __name__ == '__main__':
    main()
