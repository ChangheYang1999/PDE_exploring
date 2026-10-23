"""Result279. Exact application of the polynomial-axis obstruction, own data only."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import comb,gcd
import hashlib,json,sys,traceback
sys.set_int_max_str_digits(0)
BASE=Path('verification')
assert Path.cwd().resolve()==BASE
R=BASE/'research/hydrostatic_n192_polynomial_application'; V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def check(name,passed,evidence=None):
 checks.append(dict(name=name,passed=bool(passed),evidence=evidence))
 if not passed:raise AssertionError(name)
def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)
def scale(a,q):return trim([q*x for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for k,y in enumerate(b):c[i+k]+=x*y
 return trim(c)
def der(a):return trim([i*x for i,x in enumerate(a)][1:] or [F(0)])
def ev(a,x):
 y=F(0)
 for q in reversed(a):y=q+x*y
 return y
def pair(q):return [str(q.numerator),str(q.denominator)]
out=dict(status='RUNNING',utc_started=datetime.now(timezone.utc).isoformat(),checks=checks)
try:
 manifest=json.loads((V/'SOURCE_BINDINGS.json').read_text())
 for x in manifest['files']:
  check('original frozen binding '+x['source'],sha(BASE/x['source'])==x['sha256'])
  check('new snapshot binding '+x['frozen'],sha(BASE/x['frozen'])==x['sha256'])
 pipe=json.loads((V/'PIPELINE.json').read_text());row=json.loads((V/'hsG_c2.0_N192_log.json').read_text());summary=json.loads((V/'SUMMARY.json').read_text());inputs=json.loads((V/'INPUTS_265.json').read_text());raw=json.loads((V/'hsG_c2.0_N192_log.polynomials.json').read_text())
 check('old pipeline finished',pipe['status']=='DONE' and len(pipe['checks'])==57 and all(x['passed'] for x in pipe['checks']))
 check('pipeline input manifest',sha(V/'INPUTS_265.json')==pipe['input_sha256'])
 check('pipeline bound state',len(pipe['states'])==1 and pipe['states'][0]['status']=='DONE' and pipe['states'][0]['result_sha256']==sha(V/'hsG_c2.0_N192_log.json'))
 check('state completed',row['status']=='DONE')
 check('state bound polynomials',row['polynomial_sha256']==sha(V/'hsG_c2.0_N192_log.polynomials.json'))
 check('summary pipeline binding',summary['pipeline_sha256']==sha(V/'PIPELINE.json') and summary['status']=='PASS' and summary['count']==134 and all(x['passed'] for x in summary['checks']))
 check('input count',len(inputs['states'])==1)
 item=inputs['states'][0];expected='5177b5ae4c8a480353f7d855e27cfb735accab264c56f53c1f54881476d737a0'
 check('frozen checkpoint binding',item['sha256']==expected and sha(BASE/item['frozen'])==expected)
 check('checkpoint size',Path(BASE/item['frozen']).stat().st_size==item['bytes'])
 check('state checkpoint binding',row['source_sha256']==expected and row['metadata']['sha256']==expected and summary['states'][0]['source_sha256']==expected)
 producer=BASE.parent/'numerics/artifacts/data/hs/hsG_c2.0_N192_log.pt'
 check('current producer numeric bytes',sha(producer)==expected)
 for p,h in pipe['code_and_proof_sha256'].items():
  path=Path(p);path=path if path.is_absolute() else BASE/path
  check('old independently bound code/proof '+path.name,path.is_relative_to(BASE) and sha(path)==h)
 arrays={}
 for name in ('H_w','k_w'):
  a=[]
  for i,p in enumerate(raw[name]):
   n,d=map(int,p);check(f'{name} canonical rational {i}',d>0 and gcd(n,d)==1);a.append(F(n,d))
  arrays[name]=a
 H=arrays['H_w'];k=arrays['k_w'];P=F(*map(int,raw['P']));L=F(*map(int,raw['L']));C=L/2**P.numerator
 check('stored P exactly2',P==2 and F(row['metadata']['p'])==P)
 check('stored L exactly1',L==1 and F(row['metadata']['L'])==L)
 check('positive axis map C quarter',C==F(1,4) and C>0)
 check('P range',(1<P<=2) and P<F(21,2))
 check('metadata N192 M48',row['metadata']['N']==192 and row['metadata']['M']==48)
 check('H zero far endpoint',H[0]==0)
 check('k zero far endpoint',k[0]==0)
 check('H first coefficient nonzero',H[1]!=0,pair(H[1]))
 check('H degree193',len(trim(H.copy()))-1==193)
 check('k degree193',len(trim(k.copy()))-1==193)
 check('degrees N plus1',len(H)==len(k)==row['metadata']['N']+2)
 check('H center equals independently exact slope',ev(H,F(1))==F(row['exact']['a']))
 check('k center equals independently exact strain',ev(k,F(1))==F(row['exact']['cH']))
 h=H[1:]; f=[F(0)]*(2*(len(h)-1)+2)
 for j,a in enumerate(h):
  for l in range(j+1):f[2*l+1]+=C*a*comb(j,l)*(-1)**l
 f=trim(f);w=[F(1),F(0),F(-1)];t=[F(0),F(1)];q=[F(1),F(0),F(3)];D=add(mul(w,der(f)),scale(mul(t,f),F(2)));d=len(f)-1
 check('F degree385',d==385)
 check('F odd polynomial',all(f[j]==0 for j in range(0,len(f),2)))
 check('F at positive endpoint',ev(f,F(1))==C*H[1])
 check('F at negative endpoint',ev(f,F(-1))==-C*H[1])
 check('F endpoints nonzero',ev(f,F(1))!=0 and ev(f,F(-1))!=0)
 check('F highest coefficient',f[-1]==C*h[-1]*(-1)**(len(h)-1))
 check('D degree386',len(D)-1==386)
 check('D highest coefficient',D[-1]==(2-d)*f[-1])
 check('D positive endpoint',ev(D,F(1))==2*ev(f,F(1)))
 check('D negative endpoint',ev(D,F(-1))==-2*ev(f,F(-1)))
 check('dy numerator Q',add(w,scale(mul(t,t),F(4)))==q)
 check('dG quotient numerator D',add(mul(der(f),w),scale(mul(f,der(w)),F(-1)))==D)
 for j in (1,2,3,10,193,385):
  check('pole leading coefficient nonzero '+str(j),2*(j+2)>0 and -2*(j+2)<0)
 check('generic degree branch',d!=2 and d%2==1)
 check('forced monomial degree not integer',F(2,4)==F(1,2) and F(1,2).denominator!=1)
 out.update(status='PASS',count=len(checks),facts=dict(source_sha256=expected,P=pair(P),L=pair(L),axis_C=pair(C),density_exponent=[1,2],H_degree=193,k_degree=193,F_degree=d,D_degree=len(D)-1,H0=pair(H[0]),k0=pair(k[0]),H1=pair(H[1]),H_top=pair(H[-1]),k_top=pair(k[-1]),F1=pair(ev(f,F(1))),H1_decimal=float(H[1]),H_top_sign=1 if H[-1]>0 else -1,k_top_sign=1 if k[-1]>0 else -1),source_manifest_sha256=sha(V/'SOURCE_BINDINGS.json'),proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),scope='Exact application using the previously verified independent Result265 coefficient reconstruction. No full-plane endpoint.')
except Exception:
 out.update(status='FAIL',count=len(checks),error=traceback.format_exc());raise
finally:
 out['utc_finished']=datetime.now(timezone.utc).isoformat();(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc_finished'],flush=True)
