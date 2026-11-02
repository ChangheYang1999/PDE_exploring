"""Independent exact checker: no optimizer or floating-point calculations."""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def read_fraction(value):
    assert type(value['numerator']) is int and type(value['denominator']) is int
    assert value['denominator'] > 0
    return Fraction(value['numerator'], value['denominator'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cert_path = Path(args.certificate)
    cert = json.loads(cert_path.read_text())
    matrix_path = Path(cert['matrix_path'])
    assert hashlib.sha256(matrix_path.read_bytes()).hexdigest() == cert['matrix_sha256']
    data = json.loads(matrix_path.read_text())
    assert data['all_replays_passed'] and cert['policies'] == data['policies']
    a = [[read_fraction(v) for v in row] for row in data['matrix']]
    p = [read_fraction(v) for v in cert['probabilities']]
    n = len(p)
    assert n > 0 and len(a) == n and all(len(row) == n for row in a)
    assert all(a[i][j] == -a[j][i] for i in range(n) for j in range(n))
    assert all(v >= 0 for v in p) and sum(p) == 1
    margins = [sum((p[i] * a[i][j] for i in range(n)), Fraction(0)) for j in range(n)]
    assert margins == [read_fraction(v) for v in cert['column_payoffs']]
    assert min(margins) >= 0 and read_fraction(cert['exact_value']) == 0
    assert sum(p[i] * margins[i] for i in range(n)) == 0
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'passed': True, 'policies': n,
              'support_size': sum(v > 0 for v in p),
              'certificate_sha256': hashlib.sha256(cert_path.read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Exact algebraic validation conditional on the separately audited empirical payoff matrix.'}
    with Path(args.output).open('x') as stream:
        json.dump(output, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps(output))


if __name__ == '__main__':
    main()
