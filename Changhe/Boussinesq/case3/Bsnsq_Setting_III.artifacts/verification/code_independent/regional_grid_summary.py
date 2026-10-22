"""Reduce saved independent raw arrays to regional errors without a new solve."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import numpy as np
from finite_difference import safe_ratio

for arg in sys.argv[1:]:
    root = Path(arg)
    data = json.loads((root / 'results.json').read_text())
    out = {'created_utc': datetime.now(timezone.utc).isoformat(),
           'source_results_sha256': hashlib.sha256((root / 'results.json').read_bytes()).hexdigest(),
           'method': 'Reduction of saved raw arrays, h=1e-5 max(1,r); no new PDE evaluations.',
           'states': []}
    text = ['# Regional residuals from saved independent arrays', '',
            'Both original Cartesian and parity-divided residuals are included. Each maximum is sampled, not certified over a region. The two exact axis angles are omitted only for Cartesian ratios. All divided residuals include those axis points. The center has its separate analytic limit check in results.json. No denominator floor is used. The last interval ends at the largest evaluated radius, normally 1e8.', '',
            '| State | Source | Field | Radius | max absolute | max normalized |',
            '|---|---|---|---|---:|---:|']
    for s in data['states']:
        row = {'label': s['label'], 'source_sha256': s['sha256'],
               'forcing_description': s.get('forcing_description'), 'runs': []}
        for k in ['transport', 'self']:
            p = root / (s['label'] + '_' + k + '.npz')
            with np.load(p, allow_pickle=False) as a:
                points = a['points']
                radius = np.linalg.norm(points, axis=1)
                axis = points[:, 0] == 0
                run = {'kind': k, 'raw_arrays_sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'regions': []}
                for f in ['F', 'G', 'Theta', 'Omega']:
                    residual = a[f + '_R_h1e-05']
                    normalizer = a[f + '_N_h1e-05']
                    ratio = safe_ratio(residual, normalizer)
                    mask = np.ones(len(points), bool) if f in ['F', 'G'] else ~axis
                    for lo, hi in [(0, .03), (.03, .3), (.3, 3), (3, 30), (30, 300), (300, np.inf)]:
                        ix = np.flatnonzero(mask & (radius >= lo) & (radius < hi))
                        if not len(ix):
                            continue
                        ir = ix[np.argmax(ratio[ix])]
                        ia = ix[np.argmax(abs(residual[ix]))]
                        entry = {'field': f, 'r_min': lo, 'r_max': None if np.isinf(hi) else hi,
                                 'points': len(ix), 'max_abs': float(abs(residual[ia])),
                                 'max_abs_point': points[ia].tolist(), 'max_ratio': float(ratio[ir]),
                                 'max_ratio_point': points[ir].tolist(),
                                 'zero_normalizers': int((normalizer[ix] == 0).sum()),
                                 'infinite_ratios': int(np.isinf(ratio[ix]).sum())}
                        run['regions'].append(entry)
                        text.append(f"| {s['label']} | {k} | {f} | {lo:g} to {hi:g} | {entry['max_abs']:.12g} | {entry['max_ratio']:.12g} |")
                row['runs'].append(run)
        out['states'].append(row)
    (root / 'REGIONAL_RESIDUALS.json').write_text(json.dumps(out, indent=2) + '\n')
    (root / 'REGIONAL_RESIDUALS.md').write_text('\n'.join(text) + '\n')
    print(root, len(out['states']), 'states summarized')
