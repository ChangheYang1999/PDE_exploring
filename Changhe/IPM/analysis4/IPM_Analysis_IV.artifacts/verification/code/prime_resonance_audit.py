"""Independent finite diagnostics for the all-prime modular obstruction proof."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import time
from flint import fmpq as Q, fmpq_poly as Poly
from rational_scan_audit import compute


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** .5) + 1))


def residue(q, p):
    q = Fraction(str(q))
    assert q.denominator % p
    return q.numerator * pow(q.denominator, -1, p) % p


def main():
    start = time.monotonic()
    target = Path('research/31_prime_denominator_obstruction')
    scan = []
    for path in sorted(Path('research/24_rational_scan/verification').glob('sin1_*.json')):
        if 'summary' in path.name:
            continue
        row = json.loads(path.read_text())
        a, p = map(int, row['delta'].split('/'))
        if prime(p) and a % 2 == 0 and a >= 4:
            actual = residue(row['kappa_exact'], p)
            expected = pow(-1, (a - 4) // 2, p)
            assert actual == expected
            scan.append(dict(delta=row['delta'], residue=actual, expected=expected,
                             exact_kappa=row['kappa_exact'], source=str(path),
                             source_sha256=sha256(path.read_bytes()).hexdigest()))
    X, one = Poly([0, 1]), Poly([1])
    F = {1: one}
    universal = []
    for n in range(2, 44):
        S = Poly([])
        for i in range(1, n):
            j = n - i
            u, v = F[i], F[j]
            S += -(one - X) * u * (v + 2 * X * v.derivative()) + Q(j, i) * ((one - 2 * X) * u + 2 * X * (one - X) * u.derivative()) * v
        F[n] = -S / (n - 1)
        if prime(n) and n > 2:
            modes = []
            for ell in range(n):
                q = sum((F[n][k] * Q((-1) ** ell * comb(2 * k + 1, k - ell), 4 ** k) for k in range(ell, n)), Q(0))
                actual = residue(q, n)
                expected = 0 if 2 * ell + 1 == n else pow(-1, ell, n)
                assert actual == expected, (n, ell, actual, expected)
                modes.append(actual)
            universal.append(dict(prime=n, all_sine_residues=modes, all_predicted_residues_match=True))
    direct = []
    for p in [5, 7, 11, 13, 17, 19]:
        for a in range(4, p, 2):
            row = compute(Fraction(a, p), {1: '1'}, p)
            actual = residue(row['kappa_exact'], p)
            expected = pow(-1, (a - 4) // 2, p)
            assert actual == expected
            row.update(residue=actual, predicted_residue=expected)
            direct.append(row)
            print('Direct Cartesian check', row['delta'], 'residue', actual, flush=True)
    result = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=sha256((target / 'PROOF.md').read_bytes()).hexdigest(),
                  existing_scan_cases=scan, universal_checks=universal,
                  direct_cartesian_checks=direct,
                  actual_elapsed_s=time.monotonic() - start,
                  scope='Finite exact checks corroborate the separate all-prime proof; they do not replace it.')
    (target / 'verification/modular_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print('All checks passed', len(scan), len(universal), len(direct), result['actual_elapsed_s'], flush=True)


if __name__ == '__main__':
    main()
