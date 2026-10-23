"""Manufactured gate for the second axis inverse; proof written first."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
import mpmath as mp
from hydrostatic_axis_primitive import primitive,AxisPrimitive,mnum,evaluate,derivative
from independent_hydrostatic import exact_hydrostatic_center,CartesianQJet,VerticalInverse
checks=[]
def check(name,yes,detail=None):
 checks.append(dict(name=name,passed=bool(yes),detail=detail))
 if not yes:
  v=Path('research/hydrostatic_axis_primitive/verification');v.mkdir(parents=True,exist_ok=True);(v/'GATE_FAILURE.json').write_text(json.dumps(dict(status='FAIL',checks=checks),indent=2)+'\n')
  raise AssertionError((name,detail))
class LowQ:
 def __init__(self,coeff,P,L):
  self.coeff=[np.array([float(x)for x in r])for r in coeff];self.M=len(coeff);self.N=max(map(len,coeff))-1;self.kappa=float(P);self.L=float(L);self.p=1-1/self.kappa;self.basis='cheb';self.tk=np.linspace(-1,.9,self.N+1)
 def coordinates(self,r):
  # A manufactured radial inversion by bisection, separate from production readers.
  r=np.asarray(r);lo=np.zeros_like(r);hi=np.ones_like(r)
  for _ in range(90):
   s=(lo+hi)/2;rr=self.L*np.sqrt(s)/(2*(1-s))**self.kappa;lo=np.where(rr<r,s,lo);hi=np.where(rr>=r,s,hi)
  s=(lo+hi)/2;return 2*s-1,s,1-s
 def polynomial(self,k,t):return np.polynomial.chebyshev.chebval(t,self.coeff[k])
for tag,coeff,P,L in [('one',[[F(1)]],F(3,2),F(2)),('two',[[F(1),F(1,8)],[F(-1,7),F(1,11)]],F(2),F(3,2)),('four',[[F(1),F(1,9),F(-1,13)],[F(1,17),F(-1,19)],[F(-1,23)],[F(1,29)]],F(3),F(5,4))]:
 p=primitive(coeff,P);check(tag+' exact all-mode center',F(p['cH'])==exact_hydrostatic_center(coeff,P))
 q=LowQ(coeff,P,L);jet=CartesianQJet(q);inv=VerticalInverse(jet.jet,q.p,order=48,tail_order=512,tail_scale=1e9,inner_scale=.125)
 with mp.workdps(100):
  a=AxisPrimitive(p,P,L,F(3));previous=[]
  for yy in ['0.0037','.219','1.37','13.7','137']:
   y=mp.mpf(yy);t=a.coordinate(y);s=(1+t)/2;w=(1-t)/2
   check(tag+' radial inversion '+yy,abs(mnum(L)*mp.sqrt(s)/(2*w)**mnum(P)-y)<mp.mpf('1e-90')*(1+y))
   g,gy=a.axis_jet(y);ref=jet.jet(0.,float(y))
   check(tag+' density '+yy,abs(float(g)-ref[0])<1e-10*(1+abs(float(g))))
   check(tag+' gy '+yy,abs(float(gy)-ref[2])<1e-10*(1+abs(float(gy))))
   dK=mp.diff(a.k,y)
   check(tag+' derivative sign '+yy,abs(float(dK)+ref[3])<1e-10*(1+abs(float(dK))))
   one=a.v2(y,16);two=a.v2(y,28);direct=inv.at(0.,float(y))['V'][1]
   err=abs(one-two);check(tag+' finite integral refinement '+yy,err<mp.mpf('1e-18')*(1+abs(two)),float(err))
   check(tag+' full-line inverse '+yy,abs(float(two)-direct)<2e-8*(1+abs(float(two))),abs(float(two)-direct))
   check(tag+' velocity odd '+yy,a.v2(-y,16)==-one)
V=Path('research/hydrostatic_axis_primitive/verification');V.mkdir(parents=True,exist_ok=True)
r=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,code_sha256=hashlib.sha256(Path('independent_code/hydrostatic_axis_primitive.py').read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest())
(V/'GATE.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',len(checks),r['utc'])
