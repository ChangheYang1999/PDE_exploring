"""Exact polynomial jet audit, independently differentiated in physical x,y.
No numerical evaluator or fitting code imported. Data audit rehashes original
source bytes and explicitly identifies stored vs exactly completed fields.
"""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json,time
import numpy as np
import sympy as s


def main():
 start=time.monotonic();checks=[]
 x,y,z=s.symbols('x y z');p,d,q,t,e,a=s.symbols('p d s t e a')
 def trunc(f,n):
  return s.Add(*(v*x**i*y**j for (i,j),v in s.Poly(s.expand(f),x,y).terms() if i+j<=n))
 def check(label,f):
  assert s.expand(f)==0,label;checks.append(label)
 eta=y-3*p*x*x*y-d*y**3+(9*p*p-5*q)*x**4*y+(12*p*d-3*t)*x*x*y**3+(3*d*d-e)*y**5
 G=x*z+p*x**3*z+d*x*z**3+q*x**5*z+t*x**3*z**3+e*x*z**5
 yy=s.diff(G,x)
 # Substitute and truncate each monomial as soon as it is formed.
 def compose(f,n):
  ans=0
  for (i,j),v in s.Poly(f,x,z).terms():
   if i+j>n:continue
   power=1
   for _ in range(j):power=trunc(power*eta,n-i)
   ans+=v*x**i*power
  return trunc(ans,n)
 check('inverse_chart_degree5',compose(yy,5)-y)
 psi=compose(3*x*s.diff(G,x)+z*s.diff(G,z)-6*G,6)
 expected=-2*x*y+10*p*x**3*y+2*d*x*y**3+(20*q-30*p*p)*x**5*y+(-28*p*d+12*t)*x**3*y**3+(-6*d*d+4*e)*x*y**5
 check('physical_Psi_degree6',psi-expected)
 theta=a*eta;u1=-s.diff(psi,y);u2=s.diff(psi,x)
 omega=-s.diff(psi,x,2)-s.diff(psi,y,2);w1=3*x+u1;w2=3*y+u2
 check('temperature_transport_degree5',trunc(w1*s.diff(theta,x)+w2*s.diff(theta,y)-theta,5))
 check('divergence',s.diff(u1,x)+s.diff(u2,y))
 ro=trunc(w1*s.diff(omega,x)+w2*s.diff(omega,y)+omega-s.diff(theta,x),4)
 P=s.Poly(ro,x,y);r11=P.coeff_monomial(x*y);r13=P.coeff_monomial(x*y**3);r31=P.coeff_monomial(x**3*y)
 check('first_vorticity_jet',r11-(-420*p-84*d+6*a*p))
 check('general_xy3',r13-((1752-24*a)*p*d+1128*d*d+6*(a-108)*t-720*e))
 check('general_x3y',r31-(20*(a-340)*q+36*(250-a)*p*p+2616*p*d-1224*t))
 rule={d:p*(a-70)/14};old=r13.subs({t:-d,e:0})
 check('old_xy3',old-d*((1752-24*a)*p+1128*d+648-6*a))
 check('center_rule',r11.subs(rule))
 check('divided_relation',old.subs(rule)-p*(a-70)/14*s.Rational(6,7)*(6*(11*a-756)*p-7*(a-108)))
 check('e_freedom',s.diff(r13,e)+720)
 check('e_not_in_x3y',s.diff(r31,e))
 check('rank_two_minor',s.det(s.Matrix([[s.diff(r31,t),s.diff(r31,e)],[s.diff(r13,t),s.diff(r13,e)]]))-1224*720)
 # The relation form above is checked rather than trusted from a derivation.
 records=[]
 for root in sorted(Path('runs/chart_certificates_v2').iterdir()):
  if not(root.is_dir() and (root/'independent_replay.json').exists()):continue
  data=json.loads((root/'input.json').read_text());source=Path(data['source']);sha=hashlib.sha256(source.read_bytes()).hexdigest();assert sha==data['source_sha256']
  if source.suffix=='.npz':
   with np.load(source,allow_pickle=False) as raw:cv=raw['coeff'].copy();av=float(raw['a0'])
  else:
   raw=json.loads(source.read_text());cv=np.asarray(raw['coeff']);av=float(raw['a0'])
  if cv.ndim==1:cv=cv[:,None]
  stored=[[F(float(v)) for v in row] for row in cv];completed=[row.copy() for row in stored]
  if data['exact_center_completion']:completed[2][0]=1-sum(row[0] for j,row in enumerate(completed) if j!=2)
  assert completed==[[F(v) for v in row] for row in data['coeff']]
  def jets(c):
   S=sum(row[0] for row in c);pp=sum(F(2-j,6)*row[0] for j,row in enumerate(c));ss=sum(F(2-j,6)*(F(2-j,6)-1)*row[0]/2 for j,row in enumerate(c));aa=F(av);dd=pp*(aa-70)/14
   gg=-60*pp/S-12*dd/S**3;jj=168*pp*dd/S**4+72*dd/S**3+120*dd**2/S**6
   hh=-400*ss/S+600*pp**2/S**2+168*pp*dd/S**4+72*dd/S**3
   terms13=[9*jj,-4*dd*gg/S**3,-aa*(24*pp*dd/S**5+6*dd/S**4)]
   terms31=[17*hh,20*pp*gg/S,-4*aa*(9*pp**2/S**3-5*ss/S**2)]
   def row(terms):
    defect=sum(terms);norm=sum(abs(t) for t in terms)
    return dict(terms=list(map(str,terms)),defect=str(defect),defect_float=float(defect),ratio=float(abs(defect)/norm) if norm else (0 if defect==0 else 'infinity'))
   result=dict(S=str(S),p=str(pp),d=str(dd),s=str(ss),physical_a0=str(aa/S),first_jet=str(7*gg+6*aa*pp/S**2),RO_xy3=row(terms13),RO_x3y=row(terms31))
   if S==1:
    assert sum(terms13)==dd*((1752-24*aa)*pp+1128*dd+648-6*aa)
    result['required_e_if_t_fixed']=str(sum(terms13)/720)
   return result
  records.append(dict(root=str(root),source=str(source.resolve()),source_sha256=sha,completion=bool(data['exact_center_completion']),stored=jets(stored),certified_model=jets(completed)))
 out=Path('research/generating_low_jets/verification');out.mkdir(parents=True,exist_ok=True)
 report=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=time.monotonic()-start,symbolic_checks=checks,symbolic_passed=True,records=records,
             code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sympy_version=s.__version__,scope='Exact source-coefficient arithmetic, not an interval bound for floating evaluation. Stored and completed models distinguished. Finite jets are necessary, never sufficient. Ratios use exact sums of absolute displayed coefficient terms, no floor. No optimum or causal failure claim.')
 (out/'symbolic_and_data.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(utc=report['utc'],seconds=report['seconds'],checks=len(checks),states=len(records))),flush=True)

if __name__=='__main__':main()
