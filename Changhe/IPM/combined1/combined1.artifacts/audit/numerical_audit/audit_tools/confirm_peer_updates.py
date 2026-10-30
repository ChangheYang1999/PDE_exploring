"""Check frozen T4 projection, scaled-generator, annular and point audit records."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import json
import time
from flint import arb, ctx
ROOT = Path(__file__).resolve().parents[1]
ctx.prec = 1024
START = time.monotonic()
def digest(p): return sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def canonical(name):
    return ROOT / (f'research/candidate_audits/data/{name}/canonical.json' if name.startswith('C1-N1-') else f'research/refit_audit/data/{name}_canonical.json')
def peerbase(own, topic):
    base = ROOT / f'research/{own}/peer_review'
    return lambda name: base / f'T4_{topic}_{name}'
def write(own, result, review):
    result.update(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'), code_sha256=digest(Path(__file__)), review_sha256=digest(ROOT / f'research/{own}/{review}'), elapsed_total_seconds=time.monotonic()-START)
    path = ROOT / f'research/{own}/verification/T4_updates_confirmation.json'
    assert not path.exists()
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(own, digest(path), flush=True)

p = peerbase('projected_residual', 'projected_mode_audit')
rows = []
for name in ['d2', 'Mpen2', 'C1-N1-002-7branch-frf', 'C1-N1-003-8branch-frf', 'C1-N1-004-4branch-l2fw', 'C1-N1-005-d2w-j7-x3']:
    path = p(name+'.json'); data = load(path)
    checks = {
        'canonical': data['canonical_sha256'] == digest(canonical(name)),
        'target': data['peer_sha256'] == digest(ROOT / f'research/projected_residual/data/{name}_first_mode.json.gz'),
        'code': data['code_sha256'] == digest(p('check.py')),
        'helper': data['helper_sha256'] == digest(p('polar_fields.py')),
        'proof': data['proof_sha256'] == digest(p('PROOF.md')),
        'exact_equality': data['exact_polynomial_equality'] is True,
    }
    assert all(checks.values()), (name, checks)
    rows.append({'candidate': name, 'peer_result_sha256': digest(path), 'checks': checks, 'branches': data['branches'], 'coefficients': data['coefficients_compared']})
assert sum(r['branches'] for r in rows) == 78
assert sum(r['coefficients'] for r in rows) == 7206
write('projected_residual', {'rows': rows, 'scope': 'Exact first residual mode for six named canonical inputs, plus independent review of the finite projection formula.'}, 'REVIEW_T4_PROJECTION.md')

p = peerbase('multiscale_generators', 'multiscale_generator_audit')
data = load(p('results.json'))
checks = {
    'proof': data['proof_sha256'] == digest(p('PROOF.md')),
    'code': data['code_sha256'] == digest(p('check.py')),
    'own_proof': data['N4_proof_sha256'] == digest(ROOT / 'research/multiscale_generators/PROOF.md'),
    'own_moments': data['N4_moments_sha256'] == digest(ROOT / 'research/multiscale_generators/code/moments.py'),
    'own_jets': data['N4_cartesian_sha256'] == digest(ROOT / 'research/multiscale_generators/code/cartesian.py'),
}
assert all(checks.values()), checks
assert len(data['moment_rows']) == 360 and all(r['all_15_equal'] for r in data['moment_rows'])
assert data['exact_coefficient_comparisons'] == 5400
assert len(data['jet_rows']) == 10 and all(r['all_overlap'] for r in data['jet_rows'])
assert sum(r['comparisons'] for r in data['jet_rows']) == data['interval_jet_comparisons'] == 388
assert sum(r['comparisons'] for r in data['jet_rows'] if r['exact_vanishing']) == 220
write('multiscale_generators', {'checks': checks, 'peer_result_sha256': digest(p('results.json')), 'moment_comparisons': 5400, 'jet_comparisons': 388, 'exact_origin_zeros': 220, 'scope': 'General rational-input generator algebra and these finite fixtures; no whole-plane multiscale norm is certified.'}, 'REVIEW_T4.md')

p = peerbase('annular_weak_probe', 'annular_probe_audit')
rows = []
for name in ['d2', 'Mpen2']:
    path=p(name+'_2048.json'); data=load(path)
    target_path=ROOT/f'research/annular_weak_probe/verification/{name}_2048.json'; target=load(target_path)
    checks = {
        'canonical': data['source_sha256'] == digest(canonical(name)),
        'target': data['peer_sha256'] == digest(target_path),
        'code': data['code_sha256'] == digest(p('check.py')),
        'helper': data['helper_sha256'] == digest(p('polar_fields.py')),
        'proof': data['proof_sha256'] == digest(p('PROOF.md')),
        'target_source': target['source_sha256'] == digest(canonical(name)),
    }
    assert all(checks.values()), (name, checks)
    comparisons=[]
    for r in data['probes']:
        t=next(t for t in target['probes'] if t['R_exact']==r['R_exact'])
        values={k: bool(arb(r[k]).overlaps(arb(t[k]))) for k in ['pairing','A','B','C','D','L2_radius_lower']}
        values['H_exact']=Fraction(r['gradient_sup_upper_exact']) == Fraction(t['gradient_sup_upper_exact'])
        assert all(values.values()) and all(r['comparisons'].values())
        assert arb(r['L2_radius_lower']) > 0
        comparisons.append({'R_exact':r['R_exact'], 'checks':values, 'L2_radius_lower':r['L2_radius_lower']})
    assert [v['R_exact'] for v in comparisons] == ['8','16','32','16384']
    rows.append({'candidate':name,'checks':checks,'comparisons':comparisons,'peer_result_sha256':digest(path)})
write('annular_weak_probe', {'rows':rows,'component_comparisons':56,'scope':'Necessary fixed-c L2 distances for the four named compact annuli, without a correction-gradient bound or global residual membership.'}, 'REVIEW_T4.md')

p=peerbase('point_witness','sharp_point_remainder_audit'); data=load(p('results.json'))
target_path=ROOT/'research/point_witness/verification/T2_R2_sharp_box.json'; target=load(target_path)
checks={'proof':data['proof_sha256']==digest(p('PROOF.md')), 'code':data['code_sha256']==digest(p('check.py')), 'fields':data['fields_sha256']==digest(p('fields.json')), 'target':data['N4_sha256']==digest(target_path)}
assert all(checks.values()),checks
own_fields=load(ROOT/'research/point_witness/verification/cartesian_witnesses.json')['rows']
field_rows=[]
for r in load(p('fields.json'))['rows']:
    own=next(t for t in own_fields if t['candidate']==r['candidate'])
    matches={k:bool(arb(r['fields'][k]).overlaps(arb(own['fields'][k]))) for k in ['residual','velocity_norm','gradient_norm']}
    assert all(matches.values())
    field_rows.append({'candidate':r['candidate'],'checks':matches})
rows=[]
for r in data['rows']:
    t=next(t for t in target['point_rows'] if t['candidate']==r['candidate'])
    matches={k:bool(arb(r[k]).overlaps(arb(t[k]))) for k in ['upper','gap']}
    assert all(matches.values()) and r['excluded']==t['strict_exclusion']
    rows.append({'candidate':r['candidate'],'checks':matches,'gap':r['gap'],'excluded':r['excluded']})
write('point_witness',{'checks':checks,'field_rows':field_rows,'rows':rows,'component_comparisons':6,'peer_result_sha256':digest(p('results.json')),'scope':'Remaining N4-047 sharp-ball point comparisons; no new point field evaluation or sufficient inverse hypothesis.'},'REVIEW_T4_SHARP.md')
