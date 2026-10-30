"""Immutable candidate audit without reducing scaled generators to R=1."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import Counter
import argparse
import json
import shutil
import sys
import time
from flint import arb, ctx, fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/generator_sector_audit'
SHARED = ROOT.parent / 'c1-shared/candidate_snapshots'
sys.path.insert(0, str(Path(__file__).parent))
from direct import origin, sectors
from cartesian import GeneratorJet, rational, ar, spec_parts
from sectors_flint import sectors as canonical_sectors


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def copy_snapshot(name):
    assert Path(name).name == name
    source = SHARED / name
    target = ROOT / 'research/candidate_audits/data' / name
    target.mkdir(exist_ok=True)
    for filename in ['SHA256SUMS', 'MANIFEST.json']:
        incoming = source / filename
        assert incoming.is_file() and not incoming.is_symlink()
        if (target / filename).exists():
            assert digest(target / filename) == digest(incoming)
        else:
            shutil.copy2(incoming, target / filename)
    checks = {}
    for line in (target / 'SHA256SUMS').read_text().splitlines():
        expected, filename = line.split(None, 1)
        filename = filename.lstrip('*')
        assert Path(filename).name == filename
        incoming = source / filename
        assert incoming.is_file() and not incoming.is_symlink()
        if not (target / filename).exists():
            shutil.copy2(incoming, target / filename)
        assert digest(target / filename) == expected
        checks[filename] = expected
    return target, checks


def run(name):
    start = time.monotonic()
    ctx.prec = 1024
    output = BASE / 'verification' / (name + '_direct.json')
    assert not output.exists()
    target, checks = copy_snapshot(name)
    manifest = json.loads((target / 'MANIFEST.json').read_text())
    assert manifest['id'] == name
    assert len(manifest['coefficient_files']) == 1
    entry = manifest['coefficient_files'][0]
    assert Path(entry['name']).name == entry['name']
    source = target / entry['name']
    assert digest(source) == entry['sha256']
    data = json.loads(source.read_text())
    c = rational(data.get('cl', data.get('cl_exact')))
    assert c == rational(manifest['c_l_exact'])
    for g in data['generators']:
        assert g['m'] == int(g['m']) and g['j'] == int(g['j'])
        w, n, q, R = spec_parts(g['spec'])
        assert min(int(g['m']), int(g['j']), w, n, q) >= 0 and R > 0
        rational(g['coef'])
    o = origin(data)
    alpha, C, G, E, grouped, summary = sectors(data, qmax=1, hmax=7)
    baseline_path = ROOT / 'research/baseline/data/state131_independent.json'
    baseline = json.loads(baseline_path.read_text())
    _, bC, bG, _ = canonical_sectors(baseline, qmax=0)
    rows = []
    for exponent, poly in sorted(grouped.items(), reverse=True):
        norm = (arb.pi() * ar(sum((v*v for v in poly.values()), Q(0)))).sqrt()
        rows.append({'exponent': str(exponent), 'exact_zero': not poly,
                     'full_circle_norm': norm.str(90),
                     'sine_coefficients': {str(k): str(v) for k,v in sorted(poly.items())}})
    x, y = '1/10', '73/100'
    fields = GeneratorJet(data, x, y).fields()
    F = abs(fields['residual'])
    V, D = fields['velocity_norm'], fields['gradient_norm']
    b0 = ar(Q(50,651))/(arb(28248)*4*arb.pi()).sqrt()
    b1 = ar(Q(25,217))/(8*arb.pi()).sqrt()
    upper = b1*V+b0*(1+D)+b0*b1
    balls = []
    for label, s, r in [('A2-Db',Q(1,262144),Q(1,65536)),
                        ('FW-T-TB-rebal-v1',Q(1,65536),Q(3,32768)),
                        ('FW-T-TB-sharp-v1',Q(1,8192),Q(43,50000)),
                        ('T4-019-no-H',Q(1,131072),Q(1,16384)),
                        ('FW-T-T4L2-sharp-v1',Q(1,7744),Q(147,200000)),
                        ('FW-T-T4L2-sharpw-v1',Q(1,5184),Q(1351,1000000))]:
        b0r = ar(r)/(4*arb.pi()*ar(1+s)).sqrt()
        b1r = ar(r)/(8*arb.pi()*ar(s*(1+s))).sqrt()
        up = b1r*V+b0r*(1+D)+b0r*b1r
        balls.append({'framework':label,'s':str(s),'radius':str(r),
                      'upper':up.str(90),'gap':(F-up).str(90),'excluded':bool(F>up)})
    dependencies = [Path(__file__), BASE/'code/direct.py', BASE/'PROOF.md',
                    BASE/'PROOF_CANDIDATES.md', ROOT/'research/multiscale_generators/PROOF.md',
                    ROOT/'research/multiscale_generators/code/cartesian.py',
                    ROOT/'research/multiscale_generators/code/moments.py',
                    ROOT/'research/sector_audit/code/sectors_flint.py',
                    ROOT/'research/point_witness/PROOF_UNIFORM_GRADED.md',
                    ROOT/'research/point_witness/PROOF.md', baseline_path]
    out = {'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'candidate':name,'generator_sha256':digest(source),
           'manifest_sha256':digest(target/'MANIFEST.json'),'snapshot_hashes':checks,
           'dependency_sha256':{str(p.relative_to(ROOT)):digest(p) for p in dependencies},
           'precision_bits':ctx.prec,'generator_count':len(data['generators']),
           'generator_kinds':dict(Counter(g['spec'][0] for g in data['generators'])),
           'scales':sorted({str(spec_parts(g['spec'])[3]) for g in data['generators']}),
           'c_exact':str(c),'origin':{k:str(v) for k,v in o.items()},
           'a0_arb':ar(o['a0']).str(90),'B0n_exact':o['strain']==1-c,
           'c_equal_state131':c==rational(baseline['cl']),
           'leading_potential_equal_state131':C[0,0]==bC[0,0],
           'leading_density_equal_state131':G[0,0]==bG[0,0],
           'sector_summary':summary,'sectors':rows,'point':[x,y],
           'fields':{k:v.str(90) for k,v in fields.items()},
           'uniform_graded_upper':upper.str(90),'uniform_graded_gap':(F-upper).str(90),
           'uniform_graded_excluded':bool(F>upper),'ball_exclusions':balls,
           'elapsed_seconds':time.monotonic()-start,
           'status':'N4-origin. Independent peer audit required for certification.',
           'scope':'Exact input, origin and finite asymptotic algebra; one-point necessary conditions. No integrated norm or global background bound.'}
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(name, summary, flush=True)
    print('F',fields['residual'].str(30),'uniform gap',(F-upper).str(30),'seconds',out['elapsed_seconds'],flush=True)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('candidate')
    run(parser.parse_args().candidate)
