"""Verify the frozen independent point, weak and background records for005."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, sys, time
from flint import arb, fmpq as Q, ctx
sys.set_int_max_str_digits(0)
ctx.prec = 1024
ROOT = Path(__file__).resolve().parents[1]
NAME = 'C1-N1-005-d2w-j7-x3'
START = time.monotonic()
def digest(p): return sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def peer(own, topic, name):
    return ROOT/f'research/{own}/peer_review/T4_{topic}_{name}'
def save(own, result):
    result.update(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  checker_sha256=digest(Path(__file__)),
                  review_sha256=digest(ROOT/f'research/{own}/REVIEW_T4_005.md'),
                  elapsed_total_seconds=time.monotonic()-START)
    p=ROOT/f'research/{own}/verification/T4_005_confirmation.json'
    assert not p.exists()
    p.write_text(json.dumps(result,indent=2)+'\n')
    print(own,digest(p),flush=True)
canonical=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json'

topic='new_candidate_witness'; own='candidate_audits'
p=peer(own,topic,NAME+'.json'); data=load(p)
target=ROOT/f'research/{own}/verification/{NAME}_point.json'; original=load(target)
generator=ROOT/f'research/{own}/data/{NAME}/d2w_j7_n4_X3_mid180_exact.json'
checks={'snapshot':data['snapshot_sha256']==digest(generator),
        'canonical':data['canonical_sha256']==digest(canonical),
        'target':data['target_sha256']==digest(target),
        'code':data['code_sha256']==digest(peer(own,topic,'reproduce.py')),
        'exact_canonical_equality':data['canonical_coefficients_agree_exactly'],
        'same_point':data['point']==original['point']}
assert all(checks.values()),checks
fields={k:bool(arb(v).overlaps(arb(original['fields'][k]))) for k,v in data['fields'].items()}
assert len(fields)==8 and all(fields.values()) and all(data['field_overlaps'].values())
rows=[]
for row in data['ball_exclusions']:
    old=next(r for r in original['ball_exclusions'] if r['framework']==row['framework'])
    matches={k:bool(arb(row[k]).overlaps(arb(old[k]))) for k in
             ['necessary_upper','gap','necessary_H2s_radius_lower']}
    assert all(matches.values()) and arb(row['gap'])>0
    rows.append({'framework':row['framework'],'checks':matches,'gap':row['gap']})
assert len(rows)==5
save(own,{'candidate':NAME,'peer_result_sha256':digest(p),'checks':checks,
          'proof_sha256':digest(peer(own,topic,'PROOF.md')),
          'field_comparisons':fields,'boxes':rows})

topic='localized_probe_audit';own='projected_residual'
p=peer(own,topic,NAME+'_2048.json');data=load(p)
target=ROOT/f'research/{own}/verification/{NAME}_probe_2048.json';original=load(target)
checks={'canonical':data['canonical_sha256']==digest(canonical),
        'target':data['peer_sha256']==digest(target),
        'code':data['code_sha256']==digest(peer(own,topic,'reproduce.py')),
        'helper':data['helper_sha256']==digest(peer(own,'weak_probe_audit','reproduce.py')),
        'proof':data['proof_sha256']==digest(peer(own,topic,'PROOF.md'))}
assert all(checks.values()),checks
rows=[]
for row in data['rows']:
    old=next(r for r in original['probes'] if r['k']==row['k'])
    matches={k:bool(arb(row[k]).overlaps(arb(old[k]))) for k in
             ['pairing','A','B_weighted','C','D','gradient_sup_upper_ball','L2_radius_lower']}
    assert all(matches.values()) and all(row['comparisons'].values())
    assert arb(row['L2_radius_lower'])>0
    rows.append({'k':row['k'],'checks':matches,'L2_radius_lower':row['L2_radius_lower']})
assert [r['k'] for r in rows]==[0,128,512,1024]
save(own,{'candidate':NAME,'peer_result_sha256':digest(p),'checks':checks,
          'component_comparisons':28,'rows':rows})

topic='background_norm_reproduction';own='background_sobolev'
p=peer(own,topic,NAME+'_reproduction.json');data=load(p)
target=ROOT/f'research/{own}/verification/{NAME}.json';original=load(target)
checks={'canonical':data['source_sha256']==digest(canonical),
        'target':data['N4_target_sha256']==digest(target),
        'code':digest(peer(own,topic,'reproduce_candidate005.py'))==
        'd695076df0f84e0b218a1b200aa20b61a079da68eca97c35fcb5f7b7a5663be4',
        'proof':digest(peer(own,topic,'PROOF.md'))==
        '52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161',
        'peer_result':digest(p)=='874628c265a403b20e9dfc12c543eb80cbbfedc5f335815b116e30d4297a751f'}
assert all(checks.values()),checks
rows=[]
energies={}
for name,row in data['norms'].items():
    old=original['norms'][name]
    energy=Q(row['rational_energy_over_pi_half'])
    exact=energy==Q(old['unweighted_rational_sum'])
    overlap=arb(row['norm']).overlaps(arb(old['norm_upper_ball']))
    assert exact and overlap and energy>0
    energies[name]=energy
    rows.append({'norm':name,'exact_energy_equality':True,'interval_overlap':True})
assert len(rows)==4
assert energies['D_rho_x']+energies['D_rho_y']==energies['D2rho']
hs=arb(data['gradient_HS_norm'])
assert hs.overlaps(arb(original['gradient_identity_conditional_HS_upper']))
c=Q(load(canonical)['cl'])
assert hs>arb(c.numerator)/c.denominator-1
save(own,{'candidate':NAME,'peer_result_sha256':digest(p),'checks':checks,'rows':rows,
          'gradient_HS_norm':data['gradient_HS_norm'],'column_sum_identity':True,
          'HS_interval_overlap':True,'prescribed_sufficient_bound_exceeds_c_minus_1':True})
