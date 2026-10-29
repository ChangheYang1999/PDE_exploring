"""Independent manufactured checks of callable-source axis inversion."""
from pathlib import Path
import datetime, hashlib, json, time
import numpy as np
from t1_axis_green import axis_green
ROOT = Path(__file__).resolve().parents[1]


def main():
    start = time.perf_counter(); rows = []
    for kind in ['gaussian', 'power']:
        for alpha in [.35135135135135137, .8]:
            beta = (alpha+1.)/2.
            def source(r, z):
                u = r*r+z*z
                if kind == 'gaussian':
                    return z*(14.-4.*u)*np.exp(-u)
                return z*beta*(14.+(10.-4.*beta)*u)/(1.+u)**(beta+2.)
            for z0 in [0., .3, 1., 3.]:
                if kind == 'gaussian':
                    exact = (z0*np.exp(-z0*z0), (1.-2.*z0*z0)*np.exp(-z0*z0))
                else:
                    b = (1.+z0*z0)**(-beta)
                    exact = (z0*b, b*(1.-2.*beta*z0*z0/(1.+z0*z0)))
                measured = axis_green(source, z0, alpha, nradial=128, nangle=160)
                error = max(abs(measured['phi']-exact[0]), abs(measured['phi_z']-exact[1]))
                rows.append({'kind': kind, 'alpha': alpha, 'z0': z0,
                             'error': float(error), 'tolerance': 5e-9, 'passed': bool(error < 5e-9),
                             'measured': measured, 'exact': exact})
    paths = [Path(__file__), ROOT/'src/t1_axis_green.py']
    result = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'all_passed': all(row['passed'] for row in rows), 'rows': rows,
              'wall_seconds': time.perf_counter()-start,
              'source_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/t1_axis_green_tests.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'all_passed': result['all_passed'], 'cases': len(rows),
                      'max_error': max(r['error'] for r in rows), 'wall_seconds': result['wall_seconds']}))
    raise SystemExit(0 if result['all_passed'] else 1)


if __name__ == '__main__':
    main()
