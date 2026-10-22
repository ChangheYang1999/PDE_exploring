"""P321 independent Fraction Laurent jets, direct primitive and Cartesian variations.
Coefficients carry an explicit upper precision; no teammate code or symbolic library.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
WIDTH=26; EXACT=10000
class Jet:
 def __init__(self,d=None,high=EXACT):
  self.high=high;self.d={int(e):F(c) for e,c in (d or {}).items() if c and e<high}
 def val(self):return min(self.d) if self.d else self.high
 def at(self,e):
  assert e<self.high,(e,self.high)
  return self.d.get(e,F(0))
 def __add__(self,o):
  if not isinstance(o,Jet):o=Jet({0:o})
  h=min(self.high,o.high);d={e:self.d.get(e,F(0))+o.d.get(e,F(0)) for e in self.d.keys()|o.d.keys()}
  return Jet(d,h)
 __radd__=__add__
 def __neg__(self):return Jet({e:-c for e,c in self.d.items()},self.high)
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return -self+o
 def __mul__(self,o):
  if not isinstance(o,Jet):return Jet({e:c*o for e,c in self.d.items()},self.high)
  h=min(self.high+o.val(),o.high+self.val());d={}
  for i,c in self.d.items():
   for j,b in o.d.items():
    if i+j<h:d[i+j]=d.get(i+j,F(0))+c*b
  return Jet(d,h)
 __rmul__=__mul__
 def inv(self):
  v=self.val();count=min(self.high-v,WIDTH);assert count>0
  c0=self.d[v];q=[1/c0]
  for j in range(1,count):q.append(-sum((self.d.get(v+i,F(0))*q[j-i] for i in range(1,j+1)),F(0))/c0)
  return Jet({j-v:c for j,c in enumerate(q)},count-v)
 def __truediv__(self,o):
  if not isinstance(o,Jet):return self* (F(1)/o)
  return self*o.inv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=Jet({0:1});base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def der(self):return Jet({e-1:e*c for e,c in self.d.items() if e},self.high-1)
 def primitive(self):return Jet({e+1:c/F(e+1) for e,c in self.d.items() if e!=-1},self.high+1)
 def shift(self,n):return Jet({e+n:c for e,c in self.d.items()},self.high+n)
 def exp(self):
  assert self.val()>0
  count=min(self.high,WIDTH);q=[F(1)]
  for j in range(1,count):q.append(sum((i*self.d.get(i,F(0))*q[j-i] for i in range(1,j+1)),F(0))/j)
  return Jet(dict(enumerate(q)),count)

def evaluate(C,k,n,checks):
 B=Jet({1:1,2:k,13:-C*k/260});Bd=B.der()
 q=(8+2*Bd)/B;h=(5+Bd)/B
 t=(q-Jet({-1:10})).primitive().exp().shift(10)
 Y=(h-Jet({-1:6})).primitive().exp().shift(6)
 J=(t/(B*Y)).primitive();H=-k**7/231;eta=Y*(H-C*J);v1=-(B.der().der()+eta)/2;th1=t*C/2
 Z=(t**(n-1))*Y
 results=[]
 for label,dt,dw,dv in [('E',t**n,-2*n*Z*J,Z*J),('F',Jet(),Z,-Z/F(2*n))]:
  rhsT=F(2*n,3)*v1.der()*dt-v1*dt.der()+F(2,2*n+1)*dv.der()*th1-dv*th1.der()
  integrandT=rhsT/(B*t**(n+1));rt=integrandT.at(-1)
  # Direct meromorphic primitive, with log coefficient omitted only because its
  # contribution begins above the next vorticity resonance.
  nextT=(t**(n+1))*integrandT.primitive()
  rhsO=-2*(n+1)*nextT+F(2*n-1,3)*v1.der()*dw-v1*dw.der()+dv.der()*eta/F(2*n+1)-dv*eta.der()
  ro=(rhsO/(B*(t**n)*Y)).at(-1)
  results.append([rt,ro])
  defect=B*dw.der()-((2*n-1)*(4+Bd)+1)*dw+2*n*dt
  # Check all known coefficients up to a conservative valid high cutoff.
  bound=min(defect.high,10*n+10)
  checks.append({'name':f'C{C}_k{k}_n{n}_{label}_previous_ode','passed':all(defect.at(e)==0 for e in range(min(0,defect.val()),bound))})
 want=[[12*C*k/F(5*(2*n+1)),-k**8*F(2*n+5,385*(2*n+1))],[F(0),-9*C*k/F(10*n)]]
 for col in range(2):
  for row in range(2):checks.append({'name':f'C{C}_k{k}_n{n}_matrix{row}{col}','passed':results[col][row]==want[col][row]})
 return {'C':str(C),'k':str(k),'n':n,'columns':[[str(v) for v in col]for col in results]}

if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[];records=[]
 # Manufacture Laurent arithmetic before invoking the actual family.
 f=Jet({-3:2,-1:3,0:5,2:7});g=Jet({1:1,2:F(2,3)})
 checks.append({'name':'inverse_identity','passed':all(((g*g.inv()).at(j)==(1 if j==0 else 0))for j in range(0,20))})
 checks.append({'name':'primitive_excludes_only_log','passed':f.primitive().der().d=={e:c for e,c in f.d.items()if e!=-1}})
 checks.append({'name':'product_rule','passed':((f*g).der()-f.der()*g-f*g.der()).d=={}})
 for C,k in [(F(1),F(-1)),(F(2),F(1,2)),(F(-3),F(2))]:
  for n in [2,3,4,5,7,10,16]:
   rec=evaluate(C,k,n,checks);records.append(rec);print(json.dumps(rec),flush=True)
 V=Path('research/321_all_order_formal_resonance/verification')
 out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'records':records,'WIDTH':WIDTH,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'21 exact rational parameter/order controls of the general proof; independently integrates the physical forcing. No numerical approximation, no teammate code, no convergence claim.'}
 (V/'fraction_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','records']},indent=2));print('FAILED',[c for c in checks if not c['passed']])
