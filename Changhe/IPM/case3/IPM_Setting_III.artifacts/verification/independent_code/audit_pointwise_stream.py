#!/usr/bin/env python3
"""Independent polynomial reconstruction of exported stream; producer code unused."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import hashlib
import json
import math
import time
import mpmath as mp
from q_high_precision_density import MPQDensity

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'research/shared_pointwise_inverse_audit/PROOF.md'
VERIFY = PROOF.parent / 'verification'
OUT = ROOT / 'evidence/pointwise_stream_audit'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def pack(x, digits=75):
    if isinstance(x, dict):
        return {k: pack(v, digits) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [pack(v, digits) for v in x]
    if isinstance(x, (str, int, bool)) or x is None:
        return x
    return mp.nstr(x, digits)


class Interpolant:
    def __init__(self, nodes, values):
        self.nodes = list(nodes)
        self.values = list(values)
        assert len(nodes) == len(values) and len(set(nodes)) == len(nodes)
        self.weights = [1/mp.fprod(x-y for j, y in enumerate(nodes) if i != j)
                        for i, x in enumerate(nodes)]

    def at(self, t):
        assert all(t != x for x in self.nodes), 'selected point is a node'
        distance = [t-x for x in self.nodes]
        d0 = [b/h for b, h in zip(self.weights, distance)]
        d1 = [-b/h for b, h in zip(d0, distance)]
        d2 = [-2*b/h for b, h in zip(d1, distance)]
        den = [mp.fsum(d) for d in (d0, d1, d2)]
        assert den[0]
        answer = []
        for col in zip(*self.values):
            num = [mp.fsum(x*y for x, y in zip(d, col)) for d in (d0, d1, d2)]
            p0 = num[0]/den[0]
            p1 = (num[1]-den[1]*p0)/den[0]
            p2 = (num[2]-den[2]*p0-2*den[1]*p1)/den[0]
            answer.append((p0, p1, p2))
        return answer


def fields(r, theta, s, w, kappa, jets):
    h = 2*s*w/(w+2*kappa*s)
    h2 = h*h*(1/s-1/w-(2*kappa-1)/(w+2*kappa*s))
    sn, cs = mp.sin(theta), mp.cos(theta)
    mode_sines = [mp.sin(2*(j+1)*theta) for j in range(len(jets))]
    ss = [mp.fsum(row[k]*si for row, si in zip(jets, mode_sines)) for k in range(3)]
    stheta = mp.fsum(2*(j+1)*row[0]*mp.cos(2*(j+1)*theta) for j, row in enumerate(jets))
    stheta2 = -mp.fsum((2*(j+1))**2*row[0]*si for j, (row, si) in enumerate(zip(jets, mode_sines)))
    ur = -r*w*stheta
    ut = r*((2*w-h)*ss[0]+2*w*h*ss[1])
    lap = (4*w-4*h-h2)*ss[0]+(8*w*h-4*h*h+2*w*h2)*ss[1]+4*w*h*h*ss[2]+w*stheta2
    return dict(psi=r*r*w*ss[0], U=[ur*cs-ut*sn, ur*sn+ut*cs], laplacian=lap)


def measure(x, y, rho, grad, velocity, ell):
    gx, gy = grad
    ux, uy = velocity
    tx, ty = (ell*x+ux)*gx, (ell*y+uy)*gy
    residual = tx+ty-rho
    nf = abs(tx)+abs(ty)+abs(rho)
    nv = abs(rho)+abs(x*gx+y*gy)+abs(ux*gx+uy*gy)
    assert nf > 0 and nv > 0
    return dict(R=residual, Nf=nf, Nv=nv, R_Nf=abs(residual)/nf, R_Nv=abs(residual)/nv)


def gate():
    started = time.monotonic()
    rows = []
    for digits in (70, 110):
        with mp.workdps(digits):
            errors = []
            for n in (7, 13, 23):
                nodes = [-1+2*(mp.mpf(i)/(n-1))**2 for i in range(n)]
                vals = [[x**k for k in range(n)] for x in nodes]
                model = Interpolant(nodes, vals)
                for target in ('-.877', '-.341', '.193', '.731'):
                    t = mp.mpf(target)
                    jets = model.at(t)
                    for k, jj in enumerate(jets):
                        expected = [t**k, k*t**(k-1) if k else mp.mpf(0),
                                    k*(k-1)*t**(k-2) if k >= 2 else mp.mpf(0)]
                        for a, b in zip(jj, expected):
                            error = abs(a-b)/(1+abs(b))
                            assert error < mp.power(10, -digits+22), (n, k, target, error)
                            errors.append(error)
            for m in (2, 4, 6, 8):
                degree = m//2-1
                # Explicit rational Cartesian stream, with no use of polar derivatives.
                def psi(x, y):
                    rr = x*x+y*y
                    return rr/(1+rr)*(2*rr/(1+rr))**degree*mp.im((x+1j*y)**m)/rr**(m//2)
                for xx, yy in (('.2', '.3'), ('.7', '.4'), ('2', '1')):
                    x, y = mp.mpf(xx), mp.mpf(yy)
                    r = mp.sqrt(x*x+y*y)
                    s, w = r*r/(1+r*r), 1/(1+r*r)
                    t = 2*s-1
                    jet = [(t+1)**degree, degree*(t+1)**(degree-1) if degree else mp.mpf(0),
                           degree*(degree-1)*(t+1)**(degree-2) if degree >= 2 else mp.mpf(0)]
                    jets = [[mp.mpf(0)]*3 for _ in range(m//2)]
                    jets[-1] = jet
                    got = fields(r, mp.atan2(y, x), s, w, mp.mpf('.5'), jets)
                    expected = [psi(x, y), -mp.diff(lambda v: psi(x, v), y),
                                mp.diff(lambda v: psi(v, y), x),
                                mp.diff(lambda v: psi(v, y), x, 2)+mp.diff(lambda v: psi(x, v), y, 2)]
                    for a, b in zip([got['psi'], *got['U'], got['laplacian']], expected):
                        error = abs(a-b)/(1+abs(b))
                        assert error < mp.power(10, -digits+10), (m, xx, yy, error)
                        errors.append(error)
            rows.append(dict(digits=digits, checks=len(errors), maximum_scaled_error=mp.nstr(max(errors), 30)))
    result = dict(utc=datetime.now(timezone.utc).isoformat(), status='PASS', rows=rows,
                  elapsed_seconds=time.monotonic()-started, code_sha256=sha(__file__), proof_sha256=sha(PROOF),
                  scope='Full-degree irregular-node interpolation and direct Cartesian differentiation of rational manufactured streams. Finite numerical gates, not interval bounds.')
    (VERIFY/'GATES.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)


def run():
    gates = json.loads((VERIFY/'GATES.json').read_text())
    assert gates['status'] == 'PASS' and gates['code_sha256'] == sha(__file__)
    OUT.mkdir(parents=True, exist_ok=True)
    summary_path = ROOT/'evidence/q_shared_sampling/SUMMARY.json'
    summary = json.loads(summary_path.read_text())
    printed_r = {128: ['1.260e-8', '2.305e-8'], 160: ['-8.008e-9', '-1.506e-8'], 192: ['2.854e-9', '9.233e-9']}
    result = dict(started_utc=datetime.now(timezone.utc).isoformat(), status='RUNNING',
                  code_sha256=sha(__file__), proof_sha256=sha(PROOF), gates_sha256=sha(VERIFY/'GATES.json'),
                  canonical_summary_sha256=sha(summary_path), rows=[],
                  scope='Reconstruction of exact binary exported nodal stream at six fixed Cartesian points. Canonical values reused from the independently checked 75/110-digit source-primitives audit. Polynomial interpolation arithmetic is independent. Precision comparison is empirical, not an enclosure. No causation by endpoint defects or global maximum is inferred.')
    def save():
        result['updated_utc'] = datetime.now(timezone.utc).isoformat()
        (OUT/'diagnostic.json').write_text(json.dumps(result, indent=2)+'\n')
    save()
    for original in summary['rows']:
        n = original['N']
        if n not in printed_r:
            continue
        tag = original['tag']
        export_path = ROOT/f'evidence/interpolated_stream_exports/r1C_cl3.0_N{n}.json'
        snapshot = export_path.with_suffix('.pt')
        export = json.loads(export_path.read_text())
        assert export['sha256'] == original['source_sha256'] == sha(snapshot)
        assert sha(ROOT/original['MP']) == original['MP_sha256']
        canonical_file = json.loads((ROOT/original['MP']).read_text())
        inp_path = ROOT/canonical_file['exact_input']
        assert sha(inp_path) == canonical_file['exact_input_sha256']
        inp = json.loads(inp_path.read_text())
        assert inp['source_sha256'] == export['sha256']
        selected = next(row for row in original['regions'] if row['region'] == 'all')['maxima']
        state = dict(tag=tag, N=n, M=original['M'], source_sha256=sha(snapshot),
                     export_sha256=sha(export_path), canonical_diagnostic_sha256=sha(ROOT/original['MP']), precision_rows=[])
        result['rows'].append(state)
        for digits in (80, 120):
            with mp.workdps(digits):
                binary = lambda v: mp.mpf(float(v))
                interpolant = Interpolant([binary(v) for v in export['tL']], [[binary(v) for v in row] for row in export['PsiC']])
                density = MPQDensity([[float(Fraction(v)) for v in row] for row in inp['coefficients']],
                                     float(Fraction(inp['L'])), float(Fraction(inp['kappa'])), float(Fraction(inp['ell'])))
                assert density.L == binary(export['L']) and density.kappa == binary(export['p']) and density.ell == binary(export['cl'])
                runrow = dict(digits=digits, points=[])
                state['precision_rows'].append(runrow)
                for i, key in enumerate(('R_Nf', 'R_Nv')):
                    cc = selected[key]['multiprecision_at_double_peak']
                    x, y = mp.mpf(cc['x']), mp.mpf(cc['y'])
                    r, theta = mp.sqrt(x*x+y*y), mp.atan2(y, x)
                    s, w = density.coords(r)
                    t = 2*s-1 if s < mp.mpf('.5') else 1-2*w
                    si = fields(r, theta, s, w, density.kappa, interpolant.at(t))
                    hrho, gx, gy = density.at(r, theta)
                    rho = r*hrho
                    canonical_velocity = [mp.mpf(v) for v in cc['U']]
                    ci = measure(x, y, rho, [gx, gy], canonical_velocity, density.ell)
                    ii = measure(x, y, rho, [gx, gy], si['U'], density.ell)
                    dc = [si['U'][i]-canonical_velocity[i] for i in (0, 1)]
                    contributions = [dc[0]*gx, dc[1]*gy]
                    delta_r = ii['R']-ci['R']
                    identity_error = abs(delta_r-mp.fsum(contributions))
                    density_errors = [abs(rho-mp.mpf(cc['rho']))/(1+abs(rho)),
                                      abs(gx-mp.mpf(cc['gradient'][0]))/(1+abs(gx)),
                                      abs(gy-mp.mpf(cc['gradient'][1]))/(1+abs(gy))]
                    canonical_errors = {k: abs(ci[k]-mp.mpf(cc[k]))/(1+abs(ci[k])) for k in ci}
                    assert max(density_errors+list(canonical_errors.values())) < mp.power(10, -min(digits, 110)+12)
                    assert identity_error < mp.power(10, -digits+15)
                    slack = mp.power(10, -digits+15)
                    assert abs(ii['Nf']-ci['Nf']) <= sum(abs(v) for v in contributions)+slack
                    assert abs(ii['Nv']-ci['Nv']) <= abs(delta_r)+slack
                    pp = dict(maximizer=key, x=x, y=y, r=r, theta=theta, rho=rho, gradient=[gx, gy],
                              stream_interpolant=si, interpolant=ii, canonical=ci, canonical_U=canonical_velocity,
                              delta_U=dc, delta_R=delta_r, delta_R_contributions=contributions,
                              residual_identity_error=identity_error, poisson_defect=-si['laplacian']-gx,
                              relative_Nf_difference=(ii['Nf']-ci['Nf'])/ci['Nf'],
                              relative_Nv_difference=(ii['Nv']-ci['Nv'])/ci['Nv'],
                              density_scaled_differences=density_errors, canonical_recomputed_scaled_differences=canonical_errors,
                              producer_printed_R=printed_r[n][i],
                              interpolant_minus_producer_printed_R=ii['R']-mp.mpf(printed_r[n][i]),
                              canonical_over_interpolant_R_Nf=ci['R_Nf']/ii['R_Nf'])
                    runrow['points'].append(pack(pp, min(digits-10, 110)))
                    save()
                    print(json.dumps(dict(tag=tag, digits=digits, point=key, R=mp.nstr(ii['R'], 16),
                                          delta_U=[mp.nstr(v, 16) for v in dc], poisson_defect=mp.nstr(pp['poisson_defect'], 16))), flush=True)
        with mp.workdps(135):
            differences=[]
            for low, high in zip(state['precision_rows'][0]['points'], state['precision_rows'][1]['points']):
                vals={}
                for key in ('psi', 'laplacian'):
                    a,b=mp.mpf(low['stream_interpolant'][key]),mp.mpf(high['stream_interpolant'][key]);vals[key]=abs(a-b)/(1+abs(b))
                for key in ('R','Nf','Nv','R_Nf','R_Nv'):
                    a,b=mp.mpf(low['interpolant'][key]),mp.mpf(high['interpolant'][key]);vals[key]=abs(a-b)/(1+abs(b))
                for key in ('delta_R', 'poisson_defect'):
                    a,b=mp.mpf(low[key]),mp.mpf(high[key]);vals[key]=abs(a-b)/(1+abs(b))
                vals['U']=max(abs(mp.mpf(a)-mp.mpf(b))/(1+abs(mp.mpf(b))) for a,b in zip(low['stream_interpolant']['U'],high['stream_interpolant']['U']))
                differences.append(dict(maximizer=high['maximizer'], scaled_differences=pack(vals, 30)))
            state['precision_comparison']=differences
        save()
    result['status']='COMPUTED'
    result['finished_utc']=datetime.now(timezone.utc).isoformat()
    save()


if __name__ == '__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--gate',action='store_true');ap.add_argument('--run',action='store_true');args=ap.parse_args()
    assert args.gate or args.run
    if args.gate:gate()
    if args.run:run()
