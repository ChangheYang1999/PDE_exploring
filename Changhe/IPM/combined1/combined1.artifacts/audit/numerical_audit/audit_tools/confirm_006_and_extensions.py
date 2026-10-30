"""Check the frozen independent006, sharp-box and b6 transfer records."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,sys,time
from flint import arb,fmpq as Q,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic()
NAME='C1-N1-006-8branch-e2'
def digest(p):return sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def peer(own,topic,name):return ROOT/f'research/{own}/peer_review/T4_{topic}_{name}'
def ar(x):
 q=Q(x);return arb(q.numerator)/q.denominator
def overlaps(x,record):return not(x<ar(record['lower']) or x>ar(record['upper']))
def save(own,label,data):
 data.update(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),checker_sha256=digest(Path(__file__)),review_sha256=digest(ROOT/f'research/{own}/REVIEW_T4_006_EXTENSIONS.md'),elapsed_total_seconds=time.monotonic()-START)
 p=ROOT/f'research/{own}/verification/T4_{label}_confirmation.json';assert not p.exists()
 p.write_text(json.dumps(data,indent=2)+'\n');print(own,label,digest(p),flush=True)
canonical=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json'
own='candidate_audits';topic='new_candidate_witness'
p=peer(own,topic,NAME+'.json');d=load(p)
target=ROOT/f'research/{own}/verification/{NAME}_point.json';old=load(target)
generator=ROOT/f'research/{own}/data/{NAME}/e2_j7_n4_d012_mid200_fromFrF_exact.json'
checks={'snapshot':d['snapshot_sha256']==digest(generator),'canonical':d['canonical_sha256']==digest(canonical),'target':d['target_sha256']==digest(target),'code':d['code_sha256']==digest(peer(own,topic,'reproduce.py')),'exact_canonical_equality':d['canonical_coefficients_agree_exactly'],'same_point':d['point']==old['point']}
assert all(checks.values()),checks
fields={k:bool(arb(v).overlaps(arb(old['fields'][k]))) for k,v in d['fields'].items()}
assert len(fields)==8 and all(fields.values()) and all(d['field_overlaps'].values())
rows=[]
for row in d['ball_exclusions']:
 prior=next(r for r in old['ball_exclusions'] if r['framework']==row['framework'])
 matches={k:bool(arb(row[k]).overlaps(arb(prior[k]))) for k in ['necessary_upper','gap','necessary_H2s_radius_lower']}
 assert all(matches.values()) and arb(row['gap'])>0
 rows.append({'framework':row['framework'],'checks':matches,'gap':row['gap']})
assert len(rows)==5
save(own,'006_point',{'candidate':NAME,'peer_result_sha256':digest(p),'checks':checks,'field_comparisons':fields,'boxes':rows})
own='projected_residual';topic='localized_probe_audit'
p=peer(own,topic,NAME+'_2048.json');d=load(p)
target=ROOT/f'research/{own}/verification/{NAME}_probe_2048.json';old=load(target)
checks={'canonical':d['canonical_sha256']==digest(canonical),'target':d['peer_sha256']==digest(target),'code':d['code_sha256']==digest(peer(own,topic,'reproduce.py')),'helper':d['helper_sha256']==digest(peer(own,'weak_probe_audit','reproduce.py')),'proof':d['proof_sha256']==digest(peer(own,topic,'PROOF.md'))}
assert all(checks.values()),checks
rows=[]
for row in d['rows']:
 prior=next(r for r in old['probes'] if r['k']==row['k'])
 matches={k:bool(arb(row[k]).overlaps(arb(prior[k]))) for k in ['pairing','A','B_weighted','C','D','gradient_sup_upper_ball','L2_radius_lower']}
 assert all(matches.values()) and all(row['comparisons'].values()) and arb(row['L2_radius_lower'])>0
 rows.append({'k':row['k'],'checks':matches,'L2_radius_lower':row['L2_radius_lower']})
assert [r['k'] for r in rows]==[0,128,512,1024]
projection=peer(own,'projected_mode_audit',NAME+'.json');dp=load(projection)
# The projection path is established by the candidate source metadata.
from importlib.util import spec_from_file_location,module_from_spec
sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import destination
pchecks={'canonical':dp['canonical_sha256']==digest(canonical),'target':dp['peer_sha256']==digest(destination(NAME)),'code':dp['code_sha256']==digest(peer(own,'projected_mode_audit','check.py')),'helper':dp['helper_sha256']==digest(peer(own,'projected_mode_audit','polar_fields.py')),'proof':dp['proof_sha256']==digest(peer(own,'projected_mode_audit','PROOF.md')),'exact_equality':dp['exact_polynomial_equality'],'all_branches':dp['branches']==16,'all_coefficients':dp['coefficients_compared']==1487}
assert all(pchecks.values()),pchecks
save(own,'006_weak_projection',{'candidate':NAME,'peer_weak_sha256':digest(p),'peer_projection_sha256':digest(projection),'checks':checks,'projection_checks':pchecks,'component_comparisons':28,'rows':rows})
own='candidate_audits';topic='new_candidate_witness';out=[]
for name in ['C1-N1-005-d2w-j7-x3',NAME]:
 p=peer(own,topic,name+'_extensions.json');d=load(p)
 target=ROOT/f'research/{own}/verification/{name}_point_extensions.json';old=load(target)
 pchecks={'canonical':d['canonical_sha256']==old['canonical_sha256'],'target':d['target_sha256']==digest(target),'point_source':d['point_source_sha256']==digest(peer(own,topic,name+'.json')),'code':d['code_sha256']==digest(peer(own,topic,'extensions.py')),'theta_overlap':overlaps(arb(d['theta']),old['theta_at_point']),'theta_gap_overlap':overlaps(arb(d['theta_minus_c_minus_1']),old['theta_minus_c_minus_1']),'same_signed_verdict':d['signed_criterion_fails_even_kappa_zero']==old['signed_criterion_fails_even_kappa_zero']}
 assert all(pchecks.values()),pchecks
 rows=[]
 for row in d['rows']:
  prior=next(r for r in old['sharp_ball_exclusions'] if r['framework']==row['framework'])
  assert Q(row['s'])==Q(prior['s']) and Q(row['radius'])==Q(prior['radius'])
  matches={k:overlaps(arb(row[k]),prior[k]) for k in ['necessary_upper','gap','necessary_H2s_radius_lower']}
  assert all(matches.values()) and arb(row['gap'])>0
  rows.append({'framework':row['framework'],'checks':matches,'gap':row['gap']})
 assert len(rows)==2
 out.append({'candidate':name,'peer_sha256':digest(p),'checks':pchecks,'rows':rows})
save(own,'005_006_extensions',{'candidates':out})
own='point_witness';topic='stationary_point_transfer'
p=peer(own,topic,'results.json');d=load(p)
target=ROOT/f'research/{own}/verification/b6_stationary_boxes.json';old=load(target)
checks={'proof':d['proof_sha256']==digest(peer(own,topic,'PROOF.md')),'code':d['code_sha256']==digest(peer(own,topic,'check.py')),'target':d['peer_sha256']==digest(target),'parameters':d['parameter_sha256']==digest(peer(own,'stationary','constants.json')),'old_point':d['prior_point_sha256']==digest(peer(own,'sharp_point_remainder_audit','results.json'))}
assert all(checks.values()),checks
s0,R0=Q(1,8192),Q(43,50000);A0=R0*R0/(1+s0);B0=A0/s0
rows=[]
for row in d['rows']:
 prior=next(r for r in old['rows'] if r['name']==row['name'])
 s,R=Q(row['s']),Q(row['R']);A=R*R/(1+s);B=A/s
 assert s==Q(prior['s']) and R==Q(prior['R'])
 assert A0-A==Q(row['positive_A_difference'])>0
 assert B0-B==Q(row['positive_B_difference'])>0
 assert A/A0==Q(prior['squared_C0R_ratio']) and B/B0==Q(prior['squared_C1R_ratio'])
 rows.append({'name':row['name'],'both_positive_differences_exactly_equal':True})
assert len(rows)==7
save(own,'b6_stationary',{'peer_result_sha256':digest(p),'checks':checks,'rows':rows,'safe_gap_lower_bound':d['safe_gap_lower_bound']})
