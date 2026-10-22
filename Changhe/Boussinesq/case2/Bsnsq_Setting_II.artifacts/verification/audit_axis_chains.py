"""Independent axis roots and trace residuals using the adaptive full-plane inverse.

No fitting-code imports. This is an exploratory sampled audit, not a root-count
certificate. Analytic modal radial derivatives and finite-difference thermal
traces are deliberately separate. Run one substantial audit process at a time.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import brentq

from modal_quad import CoefficientModes, radial_integrals
from profile_data import CoefficientProfile, snapshot
from residuals import differentiate


def axes_from_vorticity(modes, radius, tail_power, tolerance):
    n = np.asarray(modes.frequencies)
    inside, outside, info = radial_integrals(modes, radius, tail_power, tolerance)
    modal_sigma = radius * (inside + outside) / 2
    modal_derivative = (-(n + 1) * inside + (n - 1) * outside) / 2
    if np.any(n % 2):
        raise ValueError('Fourfold parity requires even sine frequencies')
    weights = np.stack([np.ones_like(n), (-1.0) ** (n // 2)])
    return weights @ modal_sigma, weights @ modal_derivative, info


def manufactured_test():
    # Stream modes A r^n/(1+r^2)^s with s=n/2; decay fixes the canonical inverse.
    class Modes:
        frequencies = np.array([2, 4])
        amplitudes = np.array([1.2, -0.7])
        def __call__(self, radius):
            n, amplitude = self.frequencies, self.amplitudes
            s = n / 2
            return (4*s*amplitude*radius**n*((n+1)+(n-s)*radius**2)
                    /(1+radius**2)**(s+2))
    modes = Modes()
    rows = []
    for radius in [0.02, 0.7, 3.0, 90.0]:
        n, amplitude = modes.frequencies, modes.amplitudes
        s = n / 2
        psi = amplitude*radius**n/(1+radius**2)**s
        derivative = psi*(n/radius-2*s*radius/(1+radius**2))
        weights = np.array([[1., 1.], [-1., 1.]])
        sigma_exact = weights @ (n*psi/radius)
        prime_exact = weights @ (n*(derivative/radius-psi/radius**2))
        sigma, prime, info = axes_from_vorticity(modes, radius, 2.0, 1e-12)
        rows.append(dict(radius=radius, sigma=sigma.tolist(), prime=prime.tolist(),
                         max_sigma_error=float(np.max(abs(sigma-sigma_exact))),
                         max_prime_error=float(np.max(abs(prime-prime_exact))), info=info))
    assert all(row['info']['success'] for row in rows)
    assert max(row['max_sigma_error'] for row in rows) < 2e-10
    assert max(row['max_prime_error'] for row in rows) < 2e-10
    return rows


def quotient(residual, denominator):
    if denominator > 0:
        return dict(value=float(abs(residual)/denominator), zero_denominator=False)
    return dict(value=None if residual else 0., zero_denominator=True,
                inconsistent=bool(residual))


def trace_residuals(profile, axis, root, speed, derivative):
    direction = np.array([1., 0.]) if axis == 0 else np.array([0., 1.])
    point = (root*direction)[None, :]
    if axis == 0:
        thermal = lambda pts: pts[:, 0]**2*profile.a(pts)
        vorticity = lambda pts: pts[:, 0]*profile.G(pts)
        multiplier, lam = 1, profile.beta+2
    else:
        thermal = lambda pts: pts[:, 1]*profile.a(pts)
        vorticity = lambda pts: pts[:, 1]*profile.G(pts)
        multiplier, lam = 2, 3*profile.beta+2
    thermal_value, vort_value = float(thermal(point)[0]), float(vorticity(point)[0])
    rows = []
    for step in [8e-4, 4e-4, 2e-4]:
        thermal_prime = float(differentiate(thermal, point, axis, relative_step=step)[0])
        vort_prime = float(differentiate(vorticity, point, axis, relative_step=step)[0])
        terms_t = [speed*thermal_prime, -multiplier*derivative*thermal_value, lam*thermal_value]
        forcing = thermal_prime if axis == 0 else 2*thermal_value
        terms_v = [speed*vort_prime, (2*profile.beta+1)*vort_value, -derivative*vort_value, -forcing]
        rt, rv = sum(terms_t), sum(terms_v)
        nt, nv = sum(map(abs, terms_t)), sum(map(abs, terms_v))
        rows.append(dict(relative_fd_step=step, thermal_prime=thermal_prime, vorticity_prime=vort_prime,
                         thermal_residual=rt, vorticity_residual=rv, thermal_denominator=nt,
                         vorticity_denominator=nv, thermal_ratio=quotient(rt,nt), vorticity_ratio=quotient(rv,nv)))
    return dict(thermal_trace=thermal_value, vorticity_trace=vort_value,
                thermal_name='Theta_y' if axis == 0 else 'Theta_xx/2',
                vorticity_name='Omega_y' if axis == 0 else 'Omega_x', rows=rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', nargs='?')
    parser.add_argument('tag', nargs='?')
    parser.add_argument('--scan-count', type=int, default=96)
    parser.add_argument('--max-radius', type=float, default=2000.)
    parser.add_argument('--manufactured-only', action='store_true')
    args = parser.parse_args()
    start = time.monotonic()
    stamp = lambda: datetime.now(timezone.utc).isoformat()
    if args.manufactured_only:
        report = dict(timestamp=stamp(), method='Two exact rational stream modes, both axes', rows=manufactured_test())
        report['elapsed_seconds'] = time.monotonic()-start
        Path('runs/axis_chain_manufactured.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report)); return
    if not args.source or not args.tag or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in args.tag):
        parser.error('source and simple tag are required')
    target = Path('data/control_snapshots')/(args.tag+'.npz')
    if not target.exists(): snapshot(args.source,target)
    profile = CoefficientProfile(target)
    modes = CoefficientModes(profile)
    report = dict(timestamp_start=stamp(), source=str(target), source_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), metadata=profile.metadata(),
                  method='Adaptive radial full-plane Green integrals, exact even sine weights at both axes, eighth-order trace finite differences',
                  limitations=['Logarithmic scan does not certify root count or first-root status',
                               'Axis quantization requires a nonzero adjacent thermal trace or an all-prior-simple chain',
                               'No interval bounds; adaptive flags retained; no denominator floor',
                               'Local trace equations alone do not verify the coupled full-plane profile'], scans=[], roots=[])
    dest = Path('runs')/(args.tag+'_axes.json')
    def save():
        report['last_update']=stamp(); report['elapsed_seconds']=time.monotonic()-start
        dest.write_text(json.dumps(report,indent=2)+'\n')
    cache = {}
    def field(radius, tolerance):
        key=(float(radius),tolerance)
        if key not in cache:
            sigma,prime,info=axes_from_vorticity(modes,radius,profile.tail_power,tolerance)
            cache[key]=(profile.beta*radius-sigma, profile.beta-prime, info)
        return cache[key]
    radii=np.geomspace(1e-3*min(1.,profile.length),args.max_radius, args.scan_count)
    for radius in radii:
        values, derivatives, info=field(float(radius),1e-9)
        report['scans'].append(dict(radius=float(radius),W=values.tolist(),derivative=derivatives.tolist(),info=info))
        save()
    for axis in [0,1]:
        values=np.array([row['W'][axis] for row in report['scans']])
        intervals=np.flatnonzero(values[:-1]*values[1:]<0)
        for idx in intervals:
            bracket=[float(radii[idx]),float(radii[idx+1])]
            result=dict(axis='x' if axis==0 else 'y',bracket=bracket,rows=[])
            report['roots'].append(result)
            for tolerance in [1e-7,1e-10,1e-12]:
                calls=[]
                def function(radius):
                    velocity,derivative,info=field(radius,tolerance)
                    calls.append(dict(radius=radius,value=float(velocity[axis]),info=info))
                    return float(velocity[axis])
                root,solver=brentq(function,*bracket,xtol=1e-10,rtol=1e-13,full_output=True)
                velocity,derivative,info=field(root,tolerance)
                nu=float(derivative[axis]); lam=(profile.beta+2) if axis==0 else (3*profile.beta+2)
                exponent=None if nu == 0 else (1 if axis==0 else 2)-lam/nu
                quant=dict(thermal_exponent=exponent,degenerate_computed_derivative=bool(nu == 0))
                if exponent is not None:
                    quant.update(nearest_integer=int(round(exponent)),integer_distance=abs(exponent-round(exponent)))
                if nu<0:
                    index=-lam/nu
                    quant.update(negative_index=index,nearest_positive_index=max(1,int(round(index))),
                                 slope_defect=nu+lam/max(1,int(round(index))))
                elif nu>0:
                    allowed=[lam] if axis==0 else [lam/2,lam]
                    quant.update(positive_allowed=allowed,nearest_slope_defect=min(allowed,key=lambda value:abs(value-nu))-nu)
                result['rows'].append(dict(tolerance=tolerance,root=root,derivative=nu,speed=float(velocity[axis]),
                    quadrature=info,root_calls=calls,root_converged=bool(solver.converged),quantization=quant,
                    traces=trace_residuals(profile,axis,root,float(velocity[axis]),nu)))
                save()
                print(json.dumps(dict(axis=result['axis'],tolerance=tolerance,root=root,derivative=nu,thermal_exponent=exponent)),flush=True)
    report['timestamp_end']=stamp();save()


if __name__=='__main__':main()
