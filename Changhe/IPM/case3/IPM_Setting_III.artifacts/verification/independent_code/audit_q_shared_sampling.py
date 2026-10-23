"""Own canonical inverse and density derivatives on exported sampling locations.

No numerics-lane module or code is imported. Only frozen numbers are read.
The finite set is shared deliberately; inverse orders and physical points are saved.
Derivation and limitations: research/shared_sampling_inverse_audit/PROOF.md.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import numpy as np


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sampling(raw):
    n, m = int(raw['N']), int(raw['M'])
    t = np.array(raw['tR'], dtype=float)
    assert len(t) == n + 1 and t[0] == -1 and np.all(np.diff(t) > 0) and t[-1] < 1
    interior = np.sort(np.r_[t[1:], (t[:-1] + t[1:]) / 2])
    sigma = (1 + interior) / 2
    log_radius = math.log(float(raw['L'])) + np.log(sigma) / 2 - float(raw['p']) * np.log1p(-interior)
    keep = log_radius < 120 * math.log(10)
    th = (np.arange(m) + .5) * math.pi / (2 * m)
    first, last = float(th[0]), float(th[-1])
    extras = [first / 4, first / 2, (last + math.pi / 2) / 2,
              math.pi / 2 - (math.pi / 2 - last) / 4, math.pi / 2]
    angles = np.sort(np.r_[th, (th[1:] + th[:-1]) / 2, extras])
    assert len(angles) == 2 * m + 4 and np.all(np.diff(angles) > 0)
    assert math.isclose(float(angles[0]), math.pi / (16 * m), rel_tol=2e-16)
    return log_radius[keep], angles, interior[keep], int(np.count_nonzero(~keep))


def canonical_grid(model, log_radius, angles, order):
    from complementary_inverse_charts import FullChart
    from angular_log_inverse import AngularLogInverse
    shape = (len(log_radius), len(angles))
    z = {k: np.empty(shape) for k in ['R_over_r', 'Nf_over_r', 'Nv_over_r', 'rho_over_r', 'ux_over_r', 'uy_over_r']}
    sn, cs = np.sin(angles)[None, :], np.cos(angles)[None, :]
    for use_defect in (True, False):
        ids = np.flatnonzero((log_radius <= model.log_core) == use_defect)
        if not len(ids):
            continue
        owner = model if use_defect else FullChart(model)
        fields = AngularLogInverse(owner, order).fields(log_radius[ids], angles)
        density = fields['H'] + owner.a * sn
        residual = fields['Fr'] + owner.a * (owner.cl + owner.c - 1) * sn
        dx = fields['grad_radial'] * cs - fields['grad_angular'] * sn
        dy = fields['grad_radial'] * sn + fields['grad_angular'] * cs
        ux = fields['ur'] * cs - fields['ut'] * sn
        uy = fields['ur'] * sn + fields['ut'] * cs
        z['R_over_r'][ids] = residual
        z['rho_over_r'][ids] = density
        z['ux_over_r'][ids], z['uy_over_r'][ids] = ux, uy
        z['Nf_over_r'][ids] = np.abs((model.cl * cs + ux) * dx) + np.abs((model.cl * sn + uy) * dy) + np.abs(density)
        z['Nv_over_r'][ids] = np.abs(density) + np.abs(cs * dx + sn * dy) + np.abs(ux * dx + uy * dy)
    assert all(np.all(np.isfinite(v)) for v in z.values())
    assert np.all(z['Nf_over_r'] > 0) and np.all(z['Nv_over_r'] > 0), 'Nonpositive denominator: requires explicit review, no filter.'
    return z


def summarize(z, log_radius, angles):
    radii = np.exp(log_radius)
    nf, nv, residual = z['Nf_over_r'], z['Nv_over_r'], z['R_over_r']
    metrics = {'abs_R': np.abs(residual) * radii[:, None], 'R_Nf': np.abs(residual) / nf, 'R_Nv': np.abs(residual) / nv}
    ranges = [('all', 0, float('inf')), ('0_to_0.1', 0, .1), ('0.1_to_1', .1, 1),
              ('1_to_100', 1, 100), ('100_to_1e4', 100, 1e4), ('1e4_to_1e8', 1e4, 1e8), ('1e8_to_1e300', 1e8, 1e300)]
    record, peaks = {}, set()
    for name, lo, hi in ranges:
        ids = np.flatnonzero((radii >= lo) & (radii < hi))
        if not len(ids):
            continue
        row = {'radii': len(ids), 'points': len(ids) * len(angles), 'maxima': {}}
        for label, values in metrics.items():
            ri, ai = np.unravel_index(np.argmax(values[ids]), (len(ids), len(angles)))
            ri = int(ids[ri]); ai = int(ai)
            r, theta = float(radii[ri]), float(angles[ai])
            x, y = r * math.cos(theta), r * math.sin(theta)
            if theta == math.pi / 2:
                x = 0.
            peaks.add((x, y))
            row['maxima'][label] = {'maximum': float(values[ri, ai]), 'r': r, 'theta': theta, 'x': x, 'y': y,
                                    'R': float(residual[ri, ai] * r), 'Nf': float(nf[ri, ai] * r), 'Nv': float(nv[ri, ai] * r),
                                    'radial_index': ri, 'angular_index': ai}
        record[name] = row
    return {'regions': record, 'minimum_Nf': float(np.min(nf * radii[:, None])),
            'minimum_Nv': float(np.min(nv * radii[:, None])), 'nonpositive_denominators': 0}, peaks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('snapshot'); ap.add_argument('export'); ap.add_argument('--tag', required=True)
    ap.add_argument('--orders', nargs='+', type=int, default=[128, 192, 256])
    ap.add_argument('--grid-only', action='store_true')
    args = ap.parse_args()
    raw = json.loads(Path(args.export).read_text()); source_sha = digest(args.snapshot)
    assert raw['sha256'] == source_sha
    log_radius, angles, nodes, omitted = sampling(raw)
    folder = Path('evidence/q_shared_sampling') / args.tag; folder.mkdir(parents=True, exist_ok=True)
    grid = {'utc': utc(), 'snapshot': args.snapshot, 'source_sha256': source_sha, 'export': args.export, 'export_sha256': digest(args.export),
            'log_radius': log_radius.tolist(), 'radius': np.exp(log_radius).tolist(), 'theta': angles.tolist(), 'map_nodes': nodes.tolist(),
            'radial_guard_removed': omitted, 'N': raw['N'], 'M': raw['M'], 'points': len(log_radius) * len(angles),
            'scope': 'Only sampling locations are reproduced. Floating-point operation order may change locations by rounding; no bit-exact coordinate claim. No producer inverse or differentiation is used.'}
    grid_path = folder / 'grid.json'; grid_path.write_text(json.dumps(grid, indent=2) + '\n')
    if args.grid_only:
        print(json.dumps({k: grid[k] for k in ['utc', 'source_sha256', 'N', 'M', 'points', 'radial_guard_removed']})); return
    from complementary_inverse_charts import ComplementaryQ
    model = ComplementaryQ(args.snapshot)
    assert model.N == int(raw['N']) and model.M == int(raw['M']) and model.L == float(raw['L'])
    assert model.kappa == float(raw['p']) and model.cl == float(raw['cl']) and model.mu == 0
    result = {'started_utc': utc(), 'status': 'RUNNING', 'source_sha256': source_sha, 'grid_sha256': digest(grid_path),
              'grid': str(grid_path), 'metadata': model.meta, 'a': model.a, 'c': model.c, 'delta': model.cl + model.c - 1,
              'code_sha256': digest(__file__), 'rows': [], 'order_comparisons': [],
              'scope': 'Finite shared-grid sampled maxima using this lane canonical full-plane inverse. Differences of maxima are not pointwise inverse errors. Near-origin neighborhoods, axis wedges, sampling gaps and the far tail remain unchecked here. No interval or existence certificate.'}
    previous = None; peaks = set()
    def save():
        result['updated_utc'] = utc(); (folder / 'diagnostic.json').write_text(json.dumps(result, indent=2) + '\n')
    save()
    for order in args.orders:
        z = canonical_grid(model, log_radius, angles, order)
        row, selected = summarize(z, log_radius, angles); peaks.update(selected)
        row['inverse_order'] = order; result['rows'].append(row)
        if previous is not None:
            result['order_comparisons'].append({'low_order': previous[0], 'high_order': order,
                'maximum_residual_difference_over_Nf': float(np.max(np.abs(z['R_over_r'] - previous[1]['R_over_r']) / z['Nf_over_r'])),
                'maximum_velocity_over_r_difference': float(max(np.max(np.abs(z[k] - previous[1][k])) for k in ['ux_over_r', 'uy_over_r']))})
        previous = (order, z); save()
        print(json.dumps({'utc': result['updated_utc'], 'tag': args.tag, 'order': order, 'whole_grid': row['regions']['all']}), flush=True)
    points = sorted(peaks, key=lambda p: (math.hypot(*p), math.atan2(p[1], p[0])))
    points_path = folder / 'peaks.json'; points_path.write_text(json.dumps(points, indent=2) + '\n')
    result['points_file'] = str(points_path); result['points_sha256'] = digest(points_path)
    result['status'] = 'COMPUTED'; result['finished_utc'] = utc(); save()


if __name__ == '__main__':
    main()
