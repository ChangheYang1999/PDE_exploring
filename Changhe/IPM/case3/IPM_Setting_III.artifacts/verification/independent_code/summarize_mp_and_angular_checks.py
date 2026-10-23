"""Aggregate completed independent checks without rerunning numerical jobs.

Only local files; no JS/TS, servers/listeners or RLScience cluster access.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib, json

D = Decimal
now = datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def fmt(value, digits=12):
    if value is None:
        return 'undefined'
    return format(D(str(value)), f'.{digits}g')

smooth = []
for path in sorted(Path('evidence/smooth_mp_inverse').glob('*/diagnostic.json')):
    data = json.loads(path.read_text())
    if 'finished_utc' not in data or len(data['rows']) < 2:
        continue
    assert sha(data['source']) == data['source_sha256']
    low, high = data['rows'][0], data['rows'][-1]
    assert len(low['points']) == len(high['points'])
    comparisons = []
    with localcontext() as context:
        context.prec = 150
        for a, b in zip(low['points'], high['points']):
            assert all(abs(D(a[key])-D(b[key])) <= D('1e-70')*(1+abs(D(b[key]))) for key in ('x','y')), 'coordinate displays disagree beyond their output precision'
            diffs = {}
            for key in ('rho', 'psi', 'U1', 'U2', 'rho_x', 'rho_y', 'R', 'Nf', 'Nv', 'R_Nf', 'R_Nv'):
                if a.get(key) is not None and b.get(key) is not None:
                    diffs[key] = str(abs(D(a[key]) - D(b[key])) / (1 + abs(D(b[key]))))
            comparisons.append({'x': b['x'], 'y': b['y'], 'scaled_absolute_difference': diffs})
    points = [{key: point.get(key) for key in ('x', 'y', 'radius', 'rho', 'U1', 'U2', 'rho_x', 'rho_y', 'R', 'Nf', 'Nv', 'R_Nf', 'R_Nv')} for point in high['points']]
    best = {key: max((point for point in points if point[key] is not None), key=lambda point: D(point[key])) for key in ('R_Nf', 'R_Nv')}
    row = {'tag': path.parent.name, 'diagnostic': str(path), 'diagnostic_sha256': sha(path), 'source': data['source'], 'source_sha256': data['source_sha256'], 'started_utc': data['started_utc'], 'finished_utc': data['finished_utc'], 'a_exact': high['a_exact'], 'delta_exact': high['delta_exact'], 'a_float': float(Fraction(high['a_exact'])), 'delta_float': float(Fraction(high['delta_exact'])), 'far_leading_defect_exact': high['far_leading_defect_exact'], 'target_digits': [low['digits'], high['digits']], 'selected_point_maxima': best, 'points': points, 'precision_comparisons': comparisons, 'max_scaled_difference': str(max(D(v) for comparison in comparisons for v in comparison['scaled_absolute_difference'].values()))}
    smooth.append(row)

angular = []
for path in sorted(Path('evidence/finite_angular_projection').glob('*/diagnostic.json')):
    data = json.loads(path.read_text())
    if 'finished_utc' not in data or data['status'] != 'COMPUTED':
        continue
    assert sha(data['source']) == data['source_sha256']
    points = []
    with localcontext() as context:
        context.prec = 140
        for point in data['rows'][-1]['points']:
            coeff = [D(x) for x in point['R_over_r_sine_coefficients']]
            energy = sum(x*x for x in coeff)
            low_energy = sum(x*x for x in coeff[:2])
            order = sorted(range(len(coeff)), key=lambda k: abs(coeff[k]), reverse=True)
            output = {key: point[key] for key in ('radius', 'R1_projection', 'R3_projection', 'angular_R_L2', 'angular_rho_L2', 'R_to_rho_angular_L2', 'estimated_angular_abs_envelope')}
            output.update({'first_third_fraction_of_squared_L2': str(low_energy/energy) if energy else None, 'dominant_residual_sine_mode': 2*order[0]+1, 'dominant_mode_fraction_of_squared_L2': str(coeff[order[0]]**2/energy) if energy else None, 'highest_available_residual_mode': 2*len(coeff)-1, 'highest_mode_R_over_r_coefficient': str(coeff[-1]), 'highest_mode_fraction_of_squared_L2': str(coeff[-1]**2/energy) if energy else None})
            points.append(output)
    angular.append({'tag': path.parent.name, 'diagnostic': str(path), 'diagnostic_sha256': sha(path), 'source': data['source'], 'source_sha256': data['source_sha256'], 'finished_utc': data['finished_utc'], 'kind': data['kind'], 'points': points, 'precision_comparisons': data['precision_comparisons'], 'max_scaled_difference': str(max(D(v) for comparison in data['precision_comparisons'] for v in comparison['scaled_absolute_differences'].values()))})

record = {'utc': now, 'scope': 'Aggregation of completed finite numerical checks. Multiprecision point maxima are only among their explicitly listed selected points, not new optimizations. Angular L2 ratios use a different denominator from Nf and Nv. No interval enclosures, whole-plane suprema or smooth-profile convergence claimed.', 'smooth': smooth, 'angular': angular, 'summarizer_sha256': sha(__file__)}
out = Path('evidence/MP_AND_ANGULAR_CHECKS.json')
out.write_text(json.dumps(record, indent=2) + '\n')
lines = ['# Multiprecision inverse and angular residual checks', '', now, '', record['scope'], '', '## Smooth saved states', '', 'The density and canonical velocity are both evaluated by the separate multiprecision finite-primitive inverse. Cartesian differentiation uses relative physical coordinates. The 75/110 target-digit comparison below compares rounded outputs; it does not certify their accuracy.', '', '| State | a | exact-source Delta, decimal | selected max R/Nf | selected max R/Nv | largest scaled precision difference |', '|---|---:|---:|---:|---:|---:|']
for row in smooth:
    lines.append('| ' + ' | '.join([row['tag'], fmt(row['a_float']), fmt(row['delta_float']), fmt(row['selected_point_maxima']['R_Nf']['R_Nf']), fmt(row['selected_point_maxima']['R_Nv']['R_Nv']), fmt(row['max_scaled_difference'], 5)]) + ' |')
lines += ['', 'The expanded coarse-peak refinement for N24/M20 was completed after the original MP sample. Its independent double-precision union max R/Nv is 2.19199141408e-6 (see REFINEMENT_FOLLOWUPS.md). The separately labeled coarse_refined_peaks row now gives the completed MP audit at those new coordinates, with R/Nv = 2.19199141562e-6. The original MP row refers to the earlier selected coordinates.', '', 'Every smooth input has stored exponent defect ell*p-1 = 1/18014398509481984. At enormous radii this produces a growing absolute residual with a small asymptotic relative residual. The finite-primitive formulas and source-exact exponents explain this; it is not evidence for an exact profile.', '', '## Complete angular convolution at selected radii', '', 'Here R1 and R3 are integrals against sin(theta) and sin(3theta), not Fourier coefficients. Parseval gives ||R||_L2(theta)^2 = pi*r^2*sum C_l^2 when R=r*sum C_l sin(l theta). The fraction column is (C_1^2+C_3^2)/sum C_l^2. The triangle envelope is a computed estimate of r*sum|C_l|, with no interval enclosure. It does not have the same units as an L2 norm, and can be smaller than that norm.', '']
for row in angular:
    lines += [f"### {row['tag']}", '', f"Source SHA256: {row['source_sha256']}. Completed {row['finished_utc']}. Largest scaled 75/110 difference: {fmt(row['max_scaled_difference'], 5)}.", '', '| r | R1 | R3 | ||R||2/||rho||2 | first+third energy fraction | largest residual mode | highest-mode energy fraction |', '|---:|---:|---:|---:|---:|---:|---:|']
    for point in row['points']:
        lines.append('| ' + ' | '.join([fmt(point['radius'], 6), fmt(point['R1_projection'], 8), fmt(point['R3_projection'], 8), fmt(point['R_to_rho_angular_L2'], 8), fmt(point['first_third_fraction_of_squared_L2'], 6), str(point['dominant_residual_sine_mode']), fmt(point['highest_mode_fraction_of_squared_L2'], 4)]) + ' |')
lines += ['', 'For example, the smooth N28/M24 state at r=0.7 has a small first-plus-third residual energy fraction while its full angular norm is appreciable. Testing only those two projections would miss most of that residual. Conversely, the highest available harmonic can be extremely small; the finite-angular rigidity theorem gives no resolution-independent positive residual bound. These numerical diagnostics neither prove nor disprove convergence as the number of angular modes grows.', '', 'CONFIRMED: the source hashes, finite computations and displayed arithmetic aggregation. OPEN: uniform global bounds, smooth convergence, and a primary endpoint.', '']
Path('evidence/MP_AND_ANGULAR_CHECKS.md').write_text('\n'.join(lines))
print(json.dumps({'utc': now, 'smooth_states': len(smooth), 'angular_states': len(angular), 'output': str(out)}))
