#!/usr/bin/env python3
"""Jacobi value recurrence, export values, and independent projected derivatives."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import numpy as np
import sympy as sp
from scipy.special import eval_jacobi
from piecewise_projection import PiecewiseValues, jacobi_value_table
ROOT = Path(__file__).resolve().parents[1]
EXPORTS = [ROOT/'external_exports/S1_pilot2_L0_20261028T2100Z',
           ROOT/'external_exports/T1_ladder_L1_20261028T232238Z']
ROWS = []
def check(name, error, tolerance, detail=None):
    error = float(error)
    row = dict(name=name, error=error, tolerance=tolerance,
               passed=bool(np.isfinite(error) and error <= tolerance))
    if detail is not None: row['detail'] = detail
    ROWS.append(row)
    print(json.dumps(row), flush=True)

def main():
    start = time.perf_counter(); exception = None
    try:
        x = np.r_[-1., -.999, -.87, -.2, 0., .37, .93, .999, 1.]
        for n in [0, 1, 3, 12, 24, 40]:
            table = jacobi_value_table(x, 24, n+.5)
            for k in [0, 1, 2, 5, 12, 24]:
                ref = eval_jacobi(k, 0, n+.5, x)
                error = np.max(abs(table[:, k]-ref)/(1+abs(ref)))
                check(f'recurrence_n{n}_k{k}', error, 8e-13)
        for export in EXPORTS:
            values = PiecewiseValues.load(export/'coeffs.npz')
            with np.load(export/'samples.npz', allow_pickle=False) as data:
                s, z = data['r']**2, data['z']
                for key in ['phi', 'q']:
                    got = values.evaluate(key, s, z)
                    check(f'{export.name}_saved_{key}',
                          np.max(abs(got-data[key]))/(1+np.max(abs(data[key]))), 2e-12)
            # Test dilation away from imperfectly matched interfaces. At the
            # interfaces, test each one-sided trace with explicit ownership.
            radius = np.sqrt(s+z*z)
            smooth = np.ones(radius.shape,dtype=bool)
            for e in values.elements[:-1]:
                smooth &= abs(radius-float(e['Rhi'])) > 1e-10
            s, z = s[smooth], z[smooth]
            scaled = PiecewiseValues.load(export/'coeffs.npz', dilation=.137)
            for key in ['phi', 'q']:
                got = scaled.evaluate(key, .137**2*s, .137*z)
                ref = values.evaluate(key, s, z) * (.137 if key=='phi' else 1.)
                check(f'{export.name}_dilation_{key}',
                      np.max(abs(got-ref))/(1+np.max(abs(ref))), 2e-12)
            for element, e in enumerate(values.elements[:-1]):
                rr = float(e['Rhi'])
                mu = np.array([-1., -.75, 0., .25, 1.])
                ss, zz = rr*rr*(1-mu*mu), rr*mu
                for side in [element,element+1]:
                    for key in ['phi','q']:
                        got = scaled.evaluate(key,.137**2*ss,.137*zz,element=side)
                        ref = values.evaluate(key,ss,zz,element=side)*(.137 if key=='phi' else 1.)
                        check(f'{export.name}_dilation_interface{element}_side{side}_{key}',
                              np.max(abs(got-ref))/(1+np.max(abs(ref))),2e-12)
        # A known polynomial supplies the derivative reference. No Taylor adapter
        # or numerical-lane differentiation routine is called in this test.
        values = PiecewiseValues.load(EXPORTS[1]/'coeffs.npz')
        coeff = {key:np.zeros_like(value) for key,value in values.coefficients.items()}
        n, k = 3, 2
        for key in ['phi', 'q']:
            labels = values.elements[0].get('labels_'+key, values.elements[0]['labels'])
            index = labels.index([n, k])
            coeff[key+'_el0'][index] = 1.
        isolated = PiecewiseValues(values.metadata, coeff)
        project = isolated.project(.5, 1., element=0, radial_degree=32, angular_degree=24)
        s, z, t = sp.symbols('s z t', real=True)
        Rb = sp.Rational(str(values.elements[0]['Rhi']))
        solid = (5*z**3-3*z*(s+z*z))/(2*Rb**3)
        expr = sp.expand(solid*sp.jacobi(k,0,sp.Rational(2*n+1,2),2*(s+z*z)/Rb**2-1))
        radius = np.array([.5,.63,.84,1.])[:,None]
        mu = np.array([-1.,-.999,-.47,0.,.31,.999,1.])[None,:]
        ss, zz = radius**2*(1-mu*mu), radius*mu
        for key,scalar in [('phi',project.phi),('q',project.q)]:
            errors = {}
            for a in range(4):
                for b in range(4-a):
                    ref = sp.lambdify((s,z),sp.diff(expr,s,a,z,b),'numpy')(ss,zz)
                    got = scalar.evaluate(ss,zz,a,b)
                    errors[f'{a},{b}'] = float(np.max(abs(got-ref))/(1+np.max(abs(ref))))
            check(f'polynomial_projected_{key}_jets_through3',max(errors.values()),1e-7,errors)
        bad = dict(values.metadata)
        bad['elements'] = [dict(e) for e in values.elements]
        bad['elements'][0]['radial'] = 'unknown'
        try:
            PiecewiseValues(bad,coeff)
        except ValueError:
            check('unknown_basis_rejected',0.,0.)
        else:
            check('unknown_basis_rejected',1.,0.)
    except Exception as exc:
        import traceback
        traceback.print_exc(); exception = repr(exc)
    paths = [Path(__file__),ROOT/'src/piecewise_projection.py',ROOT/'src/independent_projection.py']
    paths += [export/'coeffs.npz' for export in EXPORTS]
    result = dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
        elapsed_seconds=time.perf_counter()-start, checks=ROWS, exception=exception,
        all_passed=exception is None and bool(ROWS) and all(row['passed'] for row in ROWS),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        scope='Value recurrence and a polynomial projected derivative reference; no candidate acceptance claim.')
    (ROOT/'results/jacobi_projection_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_passed','elapsed_seconds','exception']}),flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__': main()
