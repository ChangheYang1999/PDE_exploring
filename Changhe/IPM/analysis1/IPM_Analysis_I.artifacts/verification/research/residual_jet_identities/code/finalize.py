"""Authenticate completed exact identities and their deliberately restricted scope."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
a=read(D/'evidence/audit.json');assert a['status']=='PASS_COMPLETE_FINITE_JET_ALGEBRA_FOLLOWUP_PENDING'
pins=dict(a['pins']);assert len(pins)==29
for f,h in pins.items():assert sha(B/f)==h,f
packet=read(D/'evidence/review_packet.json');assert packet['audit_sha256']==sha(D/'evidence/audit.json') and packet['pin_count']==29
assert a['laurent_pairs']==a['chebyshev_pairs']==68121 and a['chebyshev_polynomial_identities']==136242
assert a['chebyshev_coefficient_equalities']==71254566 and a['differential_algebra_identities']==2610 and a['exponential_polynomial_cases']==112 and a['generic_value_prefactor_identities']==1305 and a['source_statements']==37
assert sha(Path(a['external_green']['path']))==a['external_green']['sha256']
reviews={}
for tag,expected in [('residual_jets_first','d5ac226428f91738b79d396bf05d1b8237481bda621e621a8c7a34abb0c57e41'),('residual_jets_completed','e658fcfef55519c3845f531e6aff6df63347c7d28132b2007c90d4e5b12b0416')]:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text()
 if tag.endswith('completed'):assert 'restricted theorem is proved' in text and 'selected-expression linkage are **ACCEPTED**' in text and '**UNVERIFIED**' in text
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for root in [D,D/'code',D/'evidence']:
 for p in root.iterdir():
  if not p.is_file() or p.is_symlink() or p.name=='verdict.json':continue
  f=str(p.relative_to(B));h=sha(p);assert f not in pins or pins[f]==h,f;pins[f]=h
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_EXACT_RESIDUAL_JET_IDENTITIES_SELECTED_SOURCE_ONLY',methods=['Exact integer Laurent algebra for all current pairs','Independent integer Chebyshev product recurrences for all current pairs','Free differential algebra against ODE/binomial expansion','Generic polynomial-ring prefactor evaluation'],laurent_pairs=68121,chebyshev_pairs=68121,chebyshev_polynomial_identities=136242,chebyshev_coefficient_positions_including_zeros=71254566,differential_algebra_identities=2610,exponential_polynomial_cases=112,generic_value_prefactor_identities=1305,selected_AST_bindings=37,reviews=reviews,files=dict(sorted(pins.items())),scope='PROOF plus mandatory ADDENDUM, COMPLETION_FOR_REVIEW and FINAL_ADJUDICATION. The latter corrects caller wording and enumerates unchecked source paths. Exact local identities and selected expressions only. All physical jet, floating arithmetic, canonical Green, composition, gluing, inverse and endpoint hypotheses remain OPEN.')
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
