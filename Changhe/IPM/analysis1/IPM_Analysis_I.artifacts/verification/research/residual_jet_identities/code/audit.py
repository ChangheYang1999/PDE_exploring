"""Audit full coverage and exact-source provenance of the limited algebra result."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
first=read(D/'evidence/first.json');assert first['proof_sha256']==sha(D/'PROOF.md')
names={'laurent':('check_laurent.py','PASS_EXACT_LAURENT_ALL_CURRENT_FREQUENCY_PAIRS'),'derivatives':('check_derivatives.py','PASS_EXACT_ODE_REDUCED_RESIDUAL_DERIVATIVES'),'source':('check_source.py','PASS_CURRENT_RESIDUAL_STRUCTURE_DIMENSIONS_CALLER'),'value_path':('check_value_path.py','PASS_GENERIC_EXACT_VALUE_DERIVATIVE_PREFACTORS')}
results={}
for name,(code,status) in names.items():
 d=read(D/'evidence'/f'{name}.json');assert d['status']==status and d['code_sha256']==sha(D/'code'/code);results[name]=d
la=results['laurent'];de=results['derivatives'];so=results['source'];va=results['value_path']
assert la['pairs']==68121 and la['radial_checks']==la['tangential_checks']==68121
assert de['radial_and_tangential_identities']==2610 and de['exponential_polynomial_cases']==112 and de['source_constant_checks']==30
assert so['shape_M']==260 and so['shape_Nf']==261 and so['actual_forcing_nder']==4 and so['source_laurent_sha256']==sha(D/'evidence/laurent.json')
assert va['exact_polynomial_identities']==1305 and len(va['source_value_bindings'])==3 and len(va['source_derivative_bindings'])==2
ranges=[(0,41),(41,82),(82,123),(123,164),(164,205),(205,246),(246,261)];pairs=identities=coeffs=0;checks=[]
for a,b in ranges:
 p=D/'evidence'/f'chebyshev_{a:03d}_{b:03d}.json';d=read(p);assert d['status']=='PASS_EXACT_CHEBYSHEV_CURRENT_J_RANGE' and d['code_sha256']==sha(D/'code/check_chebyshev.py') and d['proof_sha256']==first['proof_sha256']
 assert d['start_j']==a and d['end_j']==b and d['n_start']==1 and d['n_end_inclusive']==261 and d['pairs']==261*(b-a)
 pairs+=d['pairs'];identities+=d['polynomial_identities'];coeffs+=d['coefficient_equalities'];checks.append(dict(start=a,end=b,sha256=sha(p),pairs=d['pairs']))
assert pairs==68121 and identities==136242 and coeffs==2*68121*523==71254566
# Authenticate first model request and raw response; this is an initial
# identity review, not acceptance of the subsequently implemented checks.
R=B/'notes/reviews';tag='residual_jets_first';m=read(R/(tag+'_metadata.json'));req=(R/(tag+'_request.txt')).read_text();raw=read(R/(tag+'_response.json'))
assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']=='d5ac226428f91738b79d396bf05d1b8237481bda621e621a8c7a34abb0c57e41'
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
assert '\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'==(R/(tag+'_response.md')).read_text()
sourcefiles={'resid':'cert_resid.py','forcing1':'cert_forcing.py','forcing2':'cert_forcing2.py'}
pins={}
for name,fn in sourcefiles.items():
 p=B/'research/forcing_v22/source/src'/fn;assert sha(p)==so['source_hashes'][name];pins[str(p.relative_to(B))]=sha(p)
green=so['external_green'];assert sha(Path(green['path']))==green['sha256']
for root in [D,D/'code',D/'evidence']:
 for p in root.iterdir():
  if p.is_file() and p.name not in ['audit.json','verdict.json','review_packet.json']:pins[str(p.relative_to(B))]=sha(p)
for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
 p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_COMPLETE_FINITE_JET_ALGEBRA_FOLLOWUP_PENDING',laurent_pairs=68121,chebyshev_pairs=pairs,chebyshev_polynomial_identities=identities,chebyshev_coefficient_equalities=coeffs,chebyshev_ranges=checks,differential_algebra_identities=2610,exponential_polynomial_cases=112,generic_value_prefactor_identities=1305,source_statements=len(so['bindings']),external_green=green,first_review={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},pins=dict(sorted(pins.items())),scope='PROOF plus mandatory ADDENDUM and COMPLETION_FOR_REVIEW. Exact identities and selected source linkage only. Physical jets and full numerical execution OPEN; actual completed-work followup pending.')
(D/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');packet={k:v for k,v in out.items() if k not in ['pins','external_green']};packet['external_green_sha256']=green['sha256'];packet['pin_count']=len(pins);packet['audit_sha256']=sha(D/'evidence/audit.json');(D/'evidence/review_packet.json').write_text(json.dumps(packet,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins')
