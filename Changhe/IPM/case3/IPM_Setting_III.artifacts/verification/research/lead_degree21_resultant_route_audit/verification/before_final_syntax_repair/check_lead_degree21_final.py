"""Result288 final exact route and provenance check."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,traceback,ast
from exact_degree21 import decode,divexact,prim,h,univ,shifted,degree
R=Path('research/lead_degree21_resultant_route_audit');V=R/'verification';D=Path('research/degree21_grouped_moment_obstruction/verification');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings=[];start=datetime.now(timezone.utc).isoformat();results={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(a,key,path):
 ck(str(path)+' '+key,a[key]==sha(path));bindings.append(dict(path=str(path),sha256=sha(path)))
def save(status):
 out=dict(status=status,started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,results=results,proof_sha256=sha(R/'FINAL_AUDIT_PROOF.md'),driver_sha256=sha(__file__),scope='Exact alternative degree21 finite auxiliary route only; full-plane UNRESOLVED.')
 (V/'FINAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
try:
 data=json.loads((V/'COEFFICIENTS.json').read_text());rec=json.loads((V/'RECONSTRUCTION.json').read_text());outer=json.loads((V/'OUTER_CHECKS.json').read_text())
 for name,a,driver,status in [('data',data,'decode_lead_degree21_coefficients.py','PASS'),('reconstruction',rec,'check_lead_degree21_route.py','PASS_PENDING_OUTER'),('outer',outer,'check_lead_degree21_outer.py','PASS')]:
  ck(name+' complete',a['status']==status and all(z['passed']for z in a['checks']));ck(name+' count',a['count']==len(a['checks']));bind(a,'driver_sha256',Path('independent_code')/driver);bind(a,'proof_sha256',R/'PROOF.md')
  if 'library_sha256'in a:bind(a,'library_sha256','independent_code/exact_degree21.py')
  if 'review_proof_sha256'in a:bind(a,'review_proof_sha256',R/'REVIEW_RESOLUTION_PROOF.md')
 bind(rec,'coefficient_sha256',V/'COEFFICIENTS.json');bind(rec,'parent_reconstruction_sha256',D/'RECONSTRUCTION.json');bind(rec,'parent_outer_sha256',D/'OUTER_CHECKS.json');bind(rec,'parent_branches_sha256',D/'BRANCH_CHECKS.json');bind(rec,'gcd_module_sha256','independent_code/modular_gcd_certificate_285.py');bind(outer,'reconstruction_sha256',V/'RECONSTRUCTION.json')
 for f,hsh in data['source_sha256'].items():ck('decoded source '+f,sha(V/f)==hsh)
 inp=json.loads((V/'INPUTS.json').read_text())
 for z in inp['files']:
  path=z.get('frozen',z.get('path'));ck('source file '+path,sha(path)==z['sha256']);bindings.append(dict(path=path,sha256=z['sha256']))
 for file in ['FINAL_CHECKS.json','REVIEW_BINDINGS.json']:
  p=D/file;b=json.loads(p.read_text());ck('parent '+file,b['status']=='PASS'and all(t['passed']for t in b['checks']));bindings.append(dict(path=str(p),sha256=sha(p)))
  for item in b.get('bindings',[]):ck('parent bound '+item['path'],sha(item['path'])==item['sha256'])
 ck('three complete new identities',len(outer['cases'])==3 and[j['name']for j in rec['jobs']]==[j['name']for j in outer['cases']]);ck('literal target degrees',[j['target_degree']for j in outer['cases']]==[316,370,1222])
 for z in outer['cases']:
  m,n,a,b=z['degrees'];ck(z['name']+' bound',z['bound']==n*a+m*b);ck(z['name']+' complete identity',z['samples']==z['bound']+1 and z['target_degree']<=z['bound'] and Fraction(z['constant'])!=0 and bool(z['finished_utc']))
 for z in rec['cases']:
  if 'kind'in z:
   kind=z['kind'];g=decode(z['gcd']);core=prim(divexact(g,(h-21)**106 if kind=='V'else h**182*(h-21)**120));co=shifted(univ(core),23);expected_degree=90 if kind=='V'else160;expected_min=1667317721197146097465612035138116195970034473 if kind=='V'else926910390972025085770986163454028685545140676868998420479567880381895463677521
   ck(kind+' core degree',degree(core,2)==expected_degree);ck(kind+' all shifted coefficients strictly positive',len(co)==expected_degree+1 and all(x>0 for x in co));ck(kind+' literal least coefficient',min(co)==expected_min);cert=z['gcd_certificate'];ck(kind+' full gcd certificate',all(cert[k]for k in ['identity_verified','exact_divisions_verified','leading_degrees_preserved']));results[kind]=dict(core_degree=expected_degree,least_shifted=str(min(co)),shifted_count=len(co))
  else:ck('literal zero branch '+str(z['zero_weight']),(z['gcd_content'],degree(decode(z['gcd']),2))=={4:(128,4),2:(50176,8)}[z['zero_weight']])
 module=ast.parse(Path('independent_code/exact_degree21.py').read_text());fn=next(x for x in module.body if isinstance(x,ast.FunctionDef)and x.name=='resultant');ck('raw determinant definition',ast.unparse(fn.body[0].value)=='bareiss(sylv(f, g, i))[0]')
 ck('review preservation',(V/'before_review_route_repair/UNEXECUTED.txt').exists());save('PASS');print('PASS',len(checks),results,datetime.now(timezone.utc).isoformat())
except Exception:
 save('FAIL');(V/'final_traceback.txt').write_text(traceback.format_exc());raise
