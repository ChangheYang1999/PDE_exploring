"""Read and cross-check completed anisotropic evidence; no numerical solver runs."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from decimal import Decimal
import json
import hashlib


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    now = datetime.now(timezone.utc).isoformat()
    base = Path('evidence/q_exact_jets')
    summary = base / 'C3_ANISOTROPIC_SUMMARY.json'
    data = json.loads(summary.read_text())
    rows = []
    for r in data['rows']:
        tag = r['tag']
        hp = Path('evidence/q_canonical_high_jets') / tag / 'diagnostic.json'
        mp = Path('evidence/q_canonical_moment_shells') / tag / 'diagnostic.json'
        h, m = json.loads(hp.read_text()), json.loads(mp.read_text())
        exact = r['exact']
        assert h['source_sha256'] == m['source_sha256'] == r['metadata']['sha256'] == sha(r['metadata']['source'])
        assert h['input_sha256'] == m['input_sha256'] == sha(m['input'])
        assert h['poisson_exact_zero'] and h['degree'] == 7
        assert all(Fraction(h[k + '_exact']) == Fraction(exact[k]) for k in ['a', 'c', 'delta'])
        moments = m['evaluated']
        assert [v['n'] for v in moments] == [1, 2, 3]
        assert abs(Decimal(moments[0]['total']) - 2 * Decimal(str(float(Fraction(exact['c']))))) < Decimal('2e-15')
        telescoping = max(abs(Decimal(v['telescoping_error'])) / (1 + abs(Decimal(v['total']))) for v in moments)
        precision = max(Decimal(x['normalized_difference']) for x in m['precision_checks'])
        assert max(telescoping, precision) < Decimal('1e-50')
        jets = {str(k): max((abs(Decimal(x['physical_decimal'])) for x in h['rows']
                            if x['field'] == 'R' and x['degree'] == k), default=Decimal(0))
                for k in [1, 3, 5, 7]}
        rows.append(dict(tag=tag, source_sha256=r['metadata']['sha256'],
                         highjet_file=str(hp), highjet_sha256=sha(hp),
                         moment_file=str(mp), moment_sha256=sha(mp), degree=7,
                         all_exact_poisson_zero=True, source_and_center_agree=True,
                         moment_precision_max=str(precision), moment_digits=m['dps'],
                         normalized_telescoping_error=str(telescoping),
                         canonical_stream_source_moments=moments,
                         max_absolute_residual_monomial_coefficient={k: str(v) for k, v in jets.items()},
                         T1_over_signed_6e=exact['T1_relative'],
                         T1_over_abs_6e=str(-Fraction(exact['T1_relative'])),
                         gradient_witness=r['gradient_witness']))
    report = Path('../numerics/NUM_REPORT.md').read_text()
    start = report.index('    (c24)')
    end = report.index('    (c25)', start)
    frozen = base / 'C3_ANISOTROPIC_c24.frozen.md'
    frozen.write_text(report[start:end])
    scope = ('Five actual saved finite smooth densities with an independently reconstructed canonical inverse. '
             'MP selected-point values, three source-moment integrals and exact core jets are distinct finite diagnostics. '
             'No sampled maximum is a uniform bound; no nearby or limiting profile is asserted. '
             'T1 in producer c24 is divided by abs(6e), while the main own table uses signed6e. '
             'Their opposite signs are convention, not a contradiction. No gradient witness means no violation '
             'was found by that witness search, not that a global cap holds.')
    out = dict(utc=now, verdict='CONFIRMED finite numerical/center audit; primary endpoint OPEN',
               code_sha256=sha(__file__), summary_file=str(summary), summary_sha256=sha(summary),
               producer_c24=str(frozen), producer_c24_sha256=sha(frozen), rows=rows, scope=scope,
               aggregation_repair='Initial foreground aggregation expected four moments and exact zero telescoping. '
               'It failed before publishing any audit. Actual default moment job computes n=1,2,3; arithmetic '
               'telescoping differences are measured here, not assumed zero. No numerical computation changed.')
    (base / 'C3_ANISOTROPIC_HIGH_JET_AUDIT.json').write_text(json.dumps(out, indent=2) + '\n')
    lines = ['# Five anisotropic states: independent audit', '', now, '',
             'CONFIRMED as finite evaluations. Primary endpoint OPEN.', '', scope, '',
             'The exact source hashes match the saved data, dense-grid inverse, two-precision source-primitives '
             'inverse, degree7 exact core jets and three canonical source moments. All exact Poisson combinations '
             'vanish. All five center defects are nonzero. The complete residual table with raw residuals, both '
             'denominators and locations is C3_ANISOTROPIC_SUMMARY.md/json.', '',
             '| State | max selected MP R/Nf | max selected MP R/Nv | max absolute R coefficient degree3 | degree5 | degree7 |',
             '|---|---:|---:|---:|---:|---:|']
    for r, x in zip(data['rows'], rows):
        maxima = r['MP']['max_over_MP_selected_points']
        jets = x['max_absolute_residual_monomial_coefficient']
        lines.append(f"| {r['tag']} | {float(maxima['R_Nf']['R_Nf']):.10g} | {float(maxima['R_Nv']['R_Nv']):.10g} | "
                     f"{float(jets['3']):.10g} | {float(jets['5']):.10g} | {float(jets['7']):.10g} |")
    lines += ['', 'These are monomial coefficients, not derivative tensor norms. Large coefficients alone do '
              'not prove a nonsmooth limit or a global residual lower bound. The actual finite density and its '
              'exact canonical inverse are smooth.', '',
              'The largest normalized source-moment change between precision levels is ' +
              str(max(Decimal(r['moment_precision_max']) for r in rows)) +
              '; the largest normalized shell telescoping error is ' +
              str(max(Decimal(r['normalized_telescoping_error']) for r in rows)) +
              '. This is empirical arithmetic stability, not an interval enclosure.', '',
              'Four states exceed1e-6 at selected independent points. The192x32 state has selected maxima '
              '9.21279924018e-7 and4.64323353592e-7; no claim that its entire plane meets that level. Its source '
              'slope21.9573659431, canonical center defect2.55185391e-8 and cubic coefficients '
              '(-172.2534329,-343.33488) do not make this an endpoint. The neighboring discretizations and '
              'stationary-state tests remain unresolved.', '',
              'The two earlier moment jobs failed because a binary.pt checkpoint was supplied to a JSON-only '
              'audit interface. Their errors were retained; corrected exact_input.json retries completed04:00:59. '
              'No failed output is counted as numerical evidence.', '', out['aggregation_repair'], '']
    (base / 'C3_ANISOTROPIC_AUDIT.md').write_text('\n'.join(lines))
    print(json.dumps({'utc': now, 'rows': len(rows), 'maximum_moment_precision_change':
                      str(max(Decimal(r['moment_precision_max']) for r in rows)),
                      'maximum_normalized_telescoping_error':
                      str(max(Decimal(r['normalized_telescoping_error']) for r in rows))}))


if __name__ == '__main__':
    main()
