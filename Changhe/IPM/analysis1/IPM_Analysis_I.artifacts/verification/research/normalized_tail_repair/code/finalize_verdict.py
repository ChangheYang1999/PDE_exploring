"""Freeze only the scoped construction after independent audits and actual review.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/normalized_tail_repair';E=D/'evidence';R=B/'notes/reviews'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert not (E/'verdict.json').exists()
a=load(E/'audit.json');o=load(E/'checks.json');pf=load(E/'proof_first.json')
assert pf['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(o['utc'])
assert a['status']=='PASS_EXACT_RATIONAL_QUOTIENT_SOURCE_MOMENTS_AND_OUTPUT_AUDIT'
assert a['counts']=={'original_Aout_entries':2600,'original_knots_entries':1573,'exterior_exponent_and_denominator_checks':4045,'symbolic_recurrence_matrix_entries':271962,'arb512_exact_quotient_enclosures':521,'arb512_exact_norm_enclosures':1,'arb512_witnesses':12,'iv180_exact_quotient_enclosures':521,'iv180_exact_norm_enclosures':1,'iv180_witnesses':12,'strict_public_claims':16,'transition_exact_checks':70,'exact_strain_angular_factor':1,'two_method_cost_examples':6}
assert o['counts']=={'all_quotient_interval_overlaps_diagnostic':521,'scalar_interval_overlaps_diagnostic':10}
files={}
for data in (a,o):
 for p,h in data['files'].items():assert sha(B/p)==h,p;files[p]=h
assert sha(Path(a['source_archive']['path']))==a['source_archive']['sha256']
# Recheck the exact normalized canonical dependencies and their current files.
for name,statuskey,wanted in [('modal_repair/evidence/audit_verdict.json','verdict','CONFIRMED'),('far_residual_obstruction/evidence/verdict.json','status','CONFIRMED_NO_STATIONARY_CANONICAL_PROFILE_IN_MODAL_AFFINE_L2_CLASS')]:
 p=B/'research'/name;v=load(p);assert v[statuskey]==wanted;files[str(p.relative_to(B))]=sha(p)
 for f,h in v.get('files',v.get('source_and_evidence_sha256',{})).items():assert sha(B/f)==h,f;files[f]=h
pub=a['public_bounds']
for eng in o['outputs'].values():
 for key,(lo,hi) in pub['strict_intervals'].items():
  b=eng['values'][key];assert F(lo)<F(b['lower_exact'])<=F(b['upper_exact'])<F(hi)
 assert F(eng['values']['N']['upper_exact'])<F(pub['N_upper'])
 assert max(abs(F(eng['values']['I_H'][k])) for k in ('lower_exact','upper_exact'))<F(pub['I_abs_upper'])
 assert F(eng['values']['C_from_public_N_I']['upper_exact'])<F(pub['C_upper'])
# Exact decimal table in PUBLICATION, independently compared with saved ceilings.
printed=['0.0001746','0.000003988','0.00000009109','0.000000002081','0.00000000004752','0.00000000000002480']
publication=(D/'PUBLICATION.md').read_text()
for row,p in zip(a['cost_examples'],printed,strict=True):
 assert F(row['cost_strict_upper_decimal'])==F(row['cost_strict_upper_exact'])<F(p)
 assert f'| {row["T"]} | {p} |' in publication
 for mode in ('arb768','iv200'):assert F(row[mode]['upper_exact'])<F(row['cost_strict_upper_exact'])
# Every current proof-review source remains unchanged. The whole closure must
# include every new code/input/output, not only a narrated summary.
reviews={}
for kind in ('proof','closure'):
 tag='normalized_tail_repair_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5'
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 for s in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'):assert s in req
 assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
 if kind=='closure':
  need=[D/n for n in ('PROOF.md','ADDENDUM.md','CLOSURE_NOTES.md','PUBLICATION.md','evidence/proof_first.json','evidence/checks.json','evidence/audit.json')]+list((D/'code').glob('*.py'))+list((D/'source').glob('*.json'))
  assert all(str(p.relative_to(B)) in m['files'] for p in need)
  verdicts=re.findall(r'^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?Verdict:[ \t]*(ACCEPT|REJECT)(?:\*\*)?[ \t]*$',ans,re.MULTILINE)
  assert verdicts==['ACCEPT']
 for f in m['files']:files[f]=sha(B/f)
 for suffix in ('_metadata.json','_response.md','_response.json','_request.txt'):
  p=R/(tag+suffix);files[str(p.relative_to(B))]=sha(p)
 reviews[kind]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_REVIEW'
assert adj['response_sha256']==sha(R/'normalized_tail_repair_closure_response.json')
assert datetime.fromisoformat(adj['utc'])>=datetime.fromisoformat(reviews['closure']['end_utc'])
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_NORMALIZED_TAIL_REPAIR_WITH_L2_RESIDUAL','scope':'PROOF plus mandatory ADDENDUM. Explicit canonical sublinear trial rho_T satisfying the kinematic P2 requirements, identical density on r<=T, exact strain normalization, unweighted L2 residual and non-L2 correction; weighted factor sup <0.334616*T^(k-1). Leading r^k tail unchanged. No residual norm ceiling, stationarity, source estimate, X3 uncertainty inclusion or decisive endpoint.','public_bounds':pub,'counts':a['counts'],'reviews':reviews,'refuted':['Naive signed interval recurrence has polynomial wrapping solely because its exact characteristic roots have unit modulus','A small weighted factor correction must belong to unweighted L2'],'open':['Finite quantitative residual norm and useful closing estimate','Leading-tail correction relating rho_T to X3','Source control and full inverse','Every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
