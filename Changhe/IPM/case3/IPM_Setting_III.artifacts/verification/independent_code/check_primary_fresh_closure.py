from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,sys
assert not sys.flags.optimize
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT
R=ROOT/'research/primary_fresh_sample';V=R/'verification';dest=V/'CLOSURE_SUPPLEMENT.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('binding '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'CLOSURE_SUPPLEMENT_PROOF.md']:bind(p)
c=json.loads(bind(V/'CHECKS.json'));i=json.loads(bind(V/'INPUTS.json'));ck('3201 main checks passed',c['count']==len(c['checks'])==3201 and all(x['passed']for x in c['checks']))
cnt=Counter()
for x in c['checks']:
 group='provenance and state gates'
 for pre in ['manufacture ','same binary64 coordinates ','precision ','squared radius ','exact decimal residual ','triangle inequalities ','horizontal exact symmetry ']:
  if x['name'].startswith(pre):group=pre.strip();break
 cnt[group]+=1
ck('disjoint actual categories',dict(cnt)=={'manufacture':5,'provenance and state gates':157,'same binary64 coordinates':303,'precision':303,'squared radius':303,'exact decimal residual':1818,'triangle inequalities':303,'horizontal exact symmetry':9}and sum(cnt.values())==3201)
rows=[]
for s,r in zip(i['states'],c['rows']):
 d=json.loads(bind(s['exact_input'],s['exact_input_sha256']));ell=F(int(d['cl']['numerator']),int(d['cl']['denominator']));ck('explicit imported ell '+str(s['N']),ell==F(5,2));ck('same state '+str(s['N']),s['N']==r['N']and s['source_sha256']==r['source_sha256']);a=F(r['a_exact']);cc=F(r['c_exact']);delta=F(r['delta_exact']);ck('center arithmetic '+str(s['N']),delta==ell+cc-1 and a!=0)
 for e in r['extents']:
  for k in ['abs_R','R_Nf','R_Nv']:ck('extent actual maximum '+str((s['N'],e['radius'],k)),e['maxima'][k]==r['all']['maxima'][k])
 rows.append(dict(N=s['N'],ell=str(ell),a=float(a),c=float(cc),delta=float(delta),M=len(d['chebyshev_coefficients']),max_degree=max(map(len,d['chebyshev_coefficients']))-1))
out=dict(status='PASS_FRESH_CLOSURE_SUPPLEMENT',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,categories=dict(cnt),rows=rows,scope='Explicit ell and center arithmetic; actual check-count partition and masks. No primitive field or inverse error enclosure.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','categories','rows']},indent=2))
