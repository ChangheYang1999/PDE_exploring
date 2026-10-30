from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time, sys
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 768
B = Path(__file__).resolve().parents[1]
start = time.monotonic()
sha = lambda p: sha256(p.read_bytes()).hexdigest()
ar = lambda x: arb(x.p) / x.q
show = lambda x: x.str(100)
manifest = json.loads((B / 'data/manifest.json').read_text())
for name, item in manifest['inputs'].items():
    p = B / ('data' if name.endswith('.json') else 'source') / name
    assert sha(p) == item['sha256'], name
c = Q(manifest['c'])
gamma = 1/c
q = gamma - 4
delta = 1-gamma
D = 1-c*(q-delta)
E = (arb(1)/2 + arb(2)**ar(-q) + arb(2)**ar(3-q)
     + arb(2)**ar(q+2)/ar(-q) + arb(2)**ar(-q-2)/ar(-q-3)
     + arb(2)**ar(2-q)/ar(q+5))
assert c > 1 and -4 < q < -3 and D > 0 and E > 133
rows = []
for name in ('007', '013', '014'):
    j = json.loads((B/f'data/{name}_endpoint.json').read_text())
    assert Q(j['c']) == c
    A = {int(n): Q(a) for n,a in j['F12'].items()}
    P = {int(n): Q(a) for n,a in j['P'].items()}
    T = {int(n): Q(a) for n,a in j['Theta0'].items()}
    modes = sorted(A.keys() | P.keys())
    assert all(n > 0 and n % 2 for n in modes)
    a = {n: A.get(n, Q(0)) for n in modes}
    p = {n: P.get(n, Q(0)) for n in modes}
    quadratic = []
    for order in (0, 1):
        w = {n: Q(1) if order == 0 else q*q+n*n for n in modes}
        aa = sum((w[n]*a[n]*a[n] for n in modes), Q(0))
        ap = sum((w[n]*a[n]*p[n] for n in modes), Q(0))
        pp = sum((w[n]*p[n]*p[n] for n in modes), Q(0))
        lam = ap/pp
        r = {n: a[n]-lam*p[n] for n in modes}
        assert sum((w[n]*r[n]*p[n] for n in modes), Q(0)) == 0
        ss = sum((w[n]*r[n]*r[n] for n in modes), Q(0))
        assert ss == aa-ap*ap/pp and ss > 0
        if order == 0:
            assert lam == Q(j['lambda'])
            saved = {int(n):Q(v) for n,v in j['projection_residual'].items()}
            assert all(r[n] == saved.get(n,Q(0)) for n in modes)
        quadratic.append((ss, lam))
    s0, l0 = quadratic[0]
    s1, l1 = quadratic[1]
    assert s1 >= (q*q+1)*s0
    b0 = (arb.pi()*ar(s0)).sqrt()/ar(4*c)
    b1 = (arb.pi()*ar(s1)).sqrt()/ar(4*c)
    Hmin = b1/(2*arb.pi()).sqrt()
    g0 = sum((n*v for n,v in T.items()),Q(0))
    assert g0 > Q(285227, 10000)
    ratio = b1/b0
    rgrad = (E*ar(g0)*ratio/ar(D))**(1/ar(delta))
    r_amplitude = (E*ar(g0)/ar(D))**(1/ar(delta))
    cap = b0*rgrad**ar(q+1)/(-2*ar(q)-2).sqrt()
    cap0 = b0*r_amplitude**ar(q+1)/(-2*ar(q)-2).sqrt()
    gain = ratio**ar((q+1)/delta)
    assert (cap-cap0*gain).contains(0)
    ecrit = {}
    for label, value in manifest['beta_reference_values'].items():
        beta = Q(value)
        ecrit[label] = show(ar(D)*b0/(ar(g0)*b1)
             *(b0/(ar(beta)*(-2*ar(q)-2).sqrt()))**ar(delta/(-q-1)))
    hfloor = int(float(Hmin))
    assert Hmin > hfloor
    rfloor = int(float(rgrad))
    assert rgrad > rfloor
    rows.append({'candidate': name, 'modes': modes,
        'unweighted_projection_squared_without_pi_exact': str(s0),
        'gradient_projection_squared_without_pi_exact': str(s1),
        'gradient_minimizing_moment': show(-arb.pi()*ar(l1)),
        'B0': show(b0), 'B1': show(b1), 'B1_over_B0': show(ratio),
        'H_lower_bound': show(Hmin), 'strict_H_floor': str(hfloor),
        'G_lower_point_exact': str(g0), 'r_grad_lower_bound': show(rgrad),
        'strict_r_grad_floor': str(rfloor), 'CI_cap_upper_bound': show(cap),
        'cap_improvement_factor': show(gain),
        'hypothetical_E_equal_1_cap': show(cap*E**ar(-(q+1)/delta)),
        'necessary_Ecrit': ecrit})
inputs = [Path(__file__), B/'PROOF.md', B/'data/manifest.json']
inputs += list((B/'data').glob('*_endpoint.json')) + list((B/'source').glob('*.md'))
result = {'utc': datetime.now(timezone.utc).isoformat(),
    'precision_bits': ctx.prec, 'inputs': {str(p):sha(p) for p in inputs},
    'c': str(c), 'q': str(q), 'delta': str(delta), 'D_delta': str(D),
    'valid_E': show(E), 'rows': rows, 'all_assertions_passed': True,
    'elapsed_seconds': time.monotonic()-start,
    'verdict': 'OPEN independent review of the analytic theorem; exact and directed specialization checks pass'}
with (B/'verification/result.json').open('x') as f:
    json.dump(result, f, indent=2); f.write('\n')
for row in rows:
    print(row['candidate'], 'H >', row['strict_H_floor'],
          'B1/B0', row['B1_over_B0'][:28], 'cap', row['CI_cap_upper_bound'][:40],
          'E=1 diagnostic', row['hypothetical_E_equal_1_cap'][:35])
print(result['utc'], result['elapsed_seconds'])
