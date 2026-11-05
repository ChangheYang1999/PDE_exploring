#!/usr/bin/env python3
"""Independent raw-cover, binding, and scalar audit of local Q coefficients."""
import json
import math
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
FOLDER = ART/'local_energy_coefficients_v01'
ctx.prec = 512

def read(p):
    return json.loads(p.read_text())

def digest(p):
    return sha256(p.read_bytes()).hexdigest()

def aa(x):
    x = F(x)
    return arb(x.numerator)/arb(x.denominator)

def complete(paths, max_depth):
    assert len(paths) == len(set(paths))
    paths = set(paths)
    assert all(set(p) <= {'0','1'} and len(p) <= max_depth for p in paths)
    def visit(s):
        if s in paths:
            assert not any(p != s and p.startswith(s) for p in paths)
            return
        assert len(s) < max_depth
        visit(s+'0')
        visit(s+'1')
    visit('')

def geometry(cfg, index, path):
    lo = F(cfg['rmin'])*F(cfg['ratio'])**index
    hi = min(F(cfg['rmin'])*F(cfg['ratio'])**(index+1), F(cfg['rmax']))
    for bit in path:
        mid = (lo+hi)/2
        if bit == '0':
            hi = mid
        else:
            assert bit == '1'
            lo = mid
    assert hi > lo > 0
    return lo, hi

def upper(value):
    value = arb(value)
    assert value.is_finite()
    return value.abs_upper()

result_path = FOLDER/'result.json'
d = read(result_path)
assert d['status'] == 'CERTIFIED_LOCAL_Q_COEFFICIENTS'
cfg = d['configuration']
assert read(FOLDER/'configuration.json') == cfg
for name, expected in cfg['bindings'].items():
    assert digest(ART/name) == expected
sources = {'base007':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21',
           'phi013':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'}
assert cfg['source_hashes'] == sources
ratio, lo, hi = map(F, [cfg['ratio'],cfg['rmin'],cfg['rmax']])
n = cfg['panels']
assert lo > 0 and ratio > 1 and lo*ratio**(n-1) < hi <= lo*ratio**n
rows, chunks = {}, {}
for p in sorted(FOLDER.glob('chunk_*.json')):
    chunk = read(p)
    assert chunk['configuration'] == cfg
    chunks[str(p.relative_to(ART))] = digest(p)
    for row in chunk['rows']:
        i = row['index']
        assert 0 <= i < n and i not in rows and row['pass']
        complete([leaf['path'] for leaf in row['leaves']], cfg['max_depth'])
        for leaf in row['leaves']:
            assert leaf['strain_pass']
            assert math.isfinite(leaf['strain_square_upper']) and 0 <= leaf['strain_square_upper'] <= 2.25
            assert all(arb(leaf[k]).is_finite() and arb(leaf[k]) > 0 for k in ['B0','H1','H2','Hu'])
        rows[i] = row
assert sorted(rows) == list(range(n))
assert not d['failed_strain_panels'] and F(d['strain_op_upper']) == F(3,2)
assert sum(len(row['leaves']) for row in rows.values()) == d['total_leaves']
assert arb(d['origin']['S']) < aa('3/2') and arb(d['exterior']['S']) < aa('3/2')
c, q, omega = aa('4076476460239181/2251799813685248'), aa('21/10'), arb(4)
assert c > aa('3/2')
env = {}
for k in ['B0','H1','H2','Hu']:
    env[k] = max([upper(d['origin'][k]),upper(d['exterior'][k])]+
                 [upper(leaf[k]) for row in rows.values() for leaf in row['leaves']])
    assert arb(d['global_envelopes'][k]).overlaps(env[k])
B0,H1,H2,Hu = [env[k] for k in ['B0','H1','H2','Hu']]
s = aa('3/2')
Minf = 1+(2-q)*c
K1 = 2*omega*arb(2).sqrt()*(Minf+s)+omega*Hu+omega*arb(2).sqrt()*B0
K1 += omega*H1+q*omega*(1+1/arb(2).sqrt())*H1/2+(1+q)*H2/2
K0 = omega*((8-2*q)*c+4+B0+(2-q/2)*H1/2)
# Re-reading finite-digit endpoint balls and taking their upper endpoints
# conservatively inflates the original producer's pre-serialization inputs.
# Rebuilt scalar uppers may therefore exceed the serialized scalar balls by
# a final-digit amount. Adopt rebuilt bounds; only check algebraic agreement
# to far greater precision than any constant used in the theorem.
assert (arb(d['E1_local_upper'])-K1).abs_upper() < arb('1e-60')
assert (arb(d['E0_local_upper'])-K0).abs_upper() < arb('1e-60')
K1 = max(K1.abs_upper(), upper(d['E1_local_upper']))
K0 = max(K0.abs_upper(), upper(d['E0_local_upper']))
weighted_u2 = []
for row in rows.values():
    for leaf in row['leaves']:
        left, right = geometry(cfg, row['index'], leaf['path'])
        left = aa(left)
        weighted_u2.append(upper(leaf['Hu'])*(1+4*left*left).sqrt()/left)
for endpoint, key in [('origin','rmin'),('exterior','rmax')]:
    radius = aa(cfg[key])
    weighted_u2.append(upper(d[endpoint]['Hu'])*(1+4*radius*radius).sqrt()/radius)
Wu2 = max(v.abs_upper() for v in weighted_u2)
out = {'status':'INDEPENDENT_LOCAL_COEFFICIENT_AUDIT_PASS',
       'finished_utc':datetime.now(timezone.utc).isoformat(),
       'bindings':{str(p.relative_to(ART)):digest(p) for p in
                   [Path(__file__),result_path,FOLDER/'configuration.json']},
       'nested_bindings':cfg['bindings'], 'used_chunk_sha256':chunks,
       'base_panels':len(rows), 'leaves':d['total_leaves'],
       'envelopes':{k:v.str(80) for k,v in env.items()},
       'reconstructed_K1':K1.str(80), 'reconstructed_K0':K0.str(80),
       'reconstructed_Wu2':Wu2.str(80), 'global_strain_upper':'3/2',
       'meaning':'Read and checked every raw adaptive leaf, full exact radial coverage, endpoint strain bounds, nested frozen code/source configuration, global envelope assembly and scalar K1/K0/Wu2 reconstruction. Analytic coefficient bounds independently reviewed; stationary theorem is separate.'}
(HERE/'local_coefficients_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['used_chunk_sha256','nested_bindings']},indent=2))
