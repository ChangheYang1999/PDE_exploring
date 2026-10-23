from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
if sys.flags.optimize:raise SystemExit('optimized Python prohibited for verification')
sys.set_int_max_str_digits(1000000)
import check_larger_node_printed as printed_api
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=str(p);v=sha(p);ck('binding '+p,(h is None or h==v)and(p not in bindings or bindings[p]==v));bindings[p]=v;return Path(p)
for p in [__file__,R/'CENTER_REUSE_PROOF.md',R/'CENTER_PARSE_CORRECTION_PROOF.md',R/'FINAL_DESIGN_REVIEW_RESOLUTION_PROOF.md',R/'CENTER_REVIEW_SCHEMA_CORRECTION_PROOF.md',printed_api.__file__]:bind(p)
i=json.loads(bind(V/'INPUTS.json').read_text());out=[]
for N,root in [(224,'hydrostatic_c2_resolved_224_audit'),(192,'hydrostatic_n192_polynomial_application')]:
 v=Path('research')/root/'verification';a=json.loads(bind(v/'FINAL_BINDINGS.json').read_text())
 if N==224:
  ck('224 prior complete finite verdict',a['status']=='PASS_SCOPED_N224_AUXILIARY_AUDIT'and a['count']==len(a['checks'])and all(z['passed']for z in a['checks']))
  for p,h in a['bindings'].items():bind(p,h)
 else:
  ck('192 prior final binding schema',set(a)=={'status','utc','files'}and a['status']=='PASS'and len(a['files'])==12 and len({z['path']for z in a['files']})==12)
  for z in a['files']:bind(z['path'],z['sha256'])
  c=json.loads(bind(v/'CHECKS.json').read_text());ck('192 application456',c['status']=='PASS'and c['count']==len(c['checks'])==456 and all(z['passed']for z in c['checks']))
  sm=json.loads(bind(v/'SOURCE_BINDINGS.json',c['source_manifest_sha256']).read_text())
  for z in sm['files']:bind(z['frozen'],z['sha256'])
 p=v/f'hsG_c2.0_N{N}_log.json';d=json.loads(bind(p).read_text());state=next(s for s in i['states']if s['N']==N);bind(state['path'],state['sha256']);ck('same exact defining state '+str(N),d['source_sha256']==state['sha256']and d['status']=='DONE')
 pipe=json.loads(bind(v/'PIPELINE.json').read_text());summ=json.loads(bind(v/'SUMMARY.json').read_text());ck('same completed pipeline '+str(N),pipe['status']=='DONE'and len(pipe['states'])==1 and pipe['states'][0]['status']=='DONE'and pipe['states'][0]['tag']==p.stem and pipe['states'][0]['result_sha256']==sha(p));ck('semantic center summary '+str(N),summ['status']=='PASS'and summ['count']==len(summ['checks'])and all(z['passed']for z in summ['checks'])and summ['pipeline_sha256']==sha(v/'PIPELINE.json')and len(summ['states'])==1 and summ['states'][0]['source_sha256']==state['sha256'])
 aa,cH,D=[F(d['exact'][k])for k in ['a','cH','delta']];ck('nonzero a and exact center defect '+str(N),aa!=0 and 1+cH==D and D!=0)
 ck('summary same center fields '+str(N),all(summ['states'][0][k]==float(q)for k,q in [('a',aa),('cH',cH),('delta',D)]))
 if N==192:
  required=['H center equals independently exact slope','k center equals independently exact strain'];ck('application explicit center equalities',all(sum(z['name']==name and z['passed']for z in c['checks'])==1 for name in required)and c['facts']['source_sha256']==state['sha256']);bind('independent_code/check_n192_polynomial_application.py',c['driver_sha256'])
 limit=abs(D)/(abs(1+D)+1);printed_path=V/('producer_hs_node_check_c2_N'+str(N)+'.txt');pd=next(z for z in i['files']if z['path']==str(printed_path));pt=printed_api.parse(bind(printed_path,pd['sha256']).read_text());ck('printed source geometry '+str(N),pt['N']==N and pt['M']==N//4);rounding=pt['rows'][0]['Rf'];printed=F(rounding['mid'])
 out.append(dict(N=N,state_sha256=state['sha256'],exact_source=dict(path=str(p),sha256=sha(p),fields=['a','cH','delta']),limit_numerator_bits=limit.numerator.bit_length(),limit_denominator_bits=limit.denominator.bit_length(),a=float(aa),cH=float(cH),delta=float(D),core_axis_limit=float(limit),core_axis_limit_exact=str(limit),producer_printed_rounding_interval=rounding,center_limit_in_printed_interval=printed_api.inside(limit,rounding),producer_printed_core_maximum=float(printed),producer_core_to_limit=float(printed/limit)))
for p,h in bindings.items():ck('stable '+p,sha(p)==h)
a=dict(status='PASS_EXACT_CENTER_REUSE',python_flags=repr(sys.flags),integer_string_limit=sys.get_int_max_str_digits(),utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,results=out,scope='Exact center data for the same finite auxiliary states. No continuum sequence or full-plane endpoint.')
target=V/'CENTER_REUSE_CHECKS.json';tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(a,indent=2,allow_nan=False)+'\n');tmp.replace(target);print(a['status'],len(checks));print(json.dumps([{k:z[k]for k in ['N','core_axis_limit','producer_printed_core_maximum','producer_core_to_limit','center_limit_in_printed_interval']}for z in out],indent=2))
