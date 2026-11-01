"""Exact Cartesian checks of the highest-frequency nontermination lemma."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
from cartesian_verify import Q, qs, sin_field, poisson


def main():
    cases = []
    for p in ['3/5', '1/7', '-1', '-7/5', '-23/9']:
        for m in [1, 3, 5, 9]:
            modes = {m: Q('7/11')}
            if m > 1:
                modes[1] = Q('-2/3')
            cases.append((Q(p), modes, None))
    # Resonances both above and below the density's forced stream bandwidth.
    for p, m, k in [(-5, 1, 4), (-7, 1, 6), (-9, 3, 8), (-3, 3, 2), (-5, 5, 4)]:
        cases.append((Q(p), {m: Q('2/7')}, (k, Q('3/13'))))
    rows = []
    for p, modes, harmonic in cases:
        rho = sin_field(p, modes)
        psi = poisson(rho)
        if harmonic:
            psi = psi + sin_field(p + 1, {harmonic[0]: harmonic[1]})
            assert (psi.laplace().scale(-1) - rho.dx()).zero()
        adv = psi.dy().scale(-1) * rho.dx() + psi.dx() * rho.dy()
        m, k = max(modes), max(psi.sine())
        a, b = modes[m], psi.sine()[k]
        expected = a*b*((p+1)*m-p*k)/2
        observed = adv.sine()[m+k]
        assert expected == observed and observed != 0
        assert max(adv.sine()) == m+k
        rows.append({
            'p': qs(p), 'density_top_frequency': m, 'stream_top_frequency': k,
            'extra_harmonic': harmonic[0] if harmonic else None,
            'nonlinear_top_frequency': m+k,
            'nonlinear_top_amplitude': qs(observed), 'exact_identity': True,
        })
    output = {
        'checked_at_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'cartesian_engine_sha256': sha256(Path('code/cartesian_verify.py').read_bytes()).hexdigest(),
        'scope': 'Supplemental finite checks; the all-parameter proof is in PROOF.md.',
        'cases': rows,
    }
    Path('research/05_no_termination/verification/highest_frequency_checks.json').write_text(
        json.dumps(output, indent=2)+'\n'
    )
    print(f'{len(rows)} exact highest-frequency identities checked')


if __name__ == '__main__':
    main()
