"""Independent mpmath.iv automatic differentiation using Cox spline bases.
Recomputes gradient enclosure without the hand-coded Arb derivative formulas.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,bisect,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv,mp
BASE=Path(__file__).resolve().parents[3];iv.dps=70;mp.dps=75
raw=json.loads((BASE/'data_exact/x3.json').read_text())
assert (raw['integers']['degree'],raw['integers']['angular']+1,raw['integers']['singular'],raw['integers']['spline_order'])==(375,201,6,7)
def frac(s):return F.from_float(float.fromhex(s))
def v(a):
 if isinstance(a,F):return iv.mpf(a.numerator)/a.denominator
 return iv.mpf(a)
class Dual:
 def __init__(self,a,d0=0,d1=0):self.a=v(a);self.d=(v(d0),v(d1))
 @staticmethod
 def cast(o):return o if isinstance(o,Dual) else Dual(o)
 def __add__(self,o):
  o=self.cast(o);return Dual(self.a+o.a,*[x+y for x,y in zip(self.d,o.d)])
 __radd__=__add__
 def __neg__(self):return Dual(-self.a,*[-x for x in self.d])
 def __sub__(self,o):return self+-self.cast(o)
 def __rsub__(self,o):return self.cast(o)+-self
 def __mul__(self,o):
  o=self.cast(o);return Dual(self.a*o.a,*[x*o.a+self.a*y for x,y in zip(self.d,o.d)])
 __rmul__=__mul__
 def __truediv__(self,o):
  o=self.cast(o);return Dual(self.a/o.a,*[(x*o.a-self.a*y)/(o.a*o.a) for x,y in zip(self.d,o.d)])
 def __rtruediv__(self,o):return self.cast(o)/self
 def __pow__(self,p):
  p=self.cast(p);assert all(x==0 for x in p.d)
  z=self.a**p.a;return Dual(z,*[p.a*self.a**(p.a-1)*x for x in self.d])
 def exp(self):
  z=iv.exp(self.a);return Dual(z,*[z*x for x in self.d])
 def log(self):return Dual(iv.log(self.a),*[x/self.a for x in self.d])
 def sin(self):return Dual(iv.sin(self.a),*[iv.cos(self.a)*x for x in self.d])
 def cos(self):return Dual(iv.cos(self.a),*[-iv.sin(self.a)*x for x in self.d])
k=Dual(frac(raw['scalars_hex']['k']));L=Dual(frac(raw['scalars_hex']['L']));r0=Dual(frac(raw['scalars_hex']['origin_radius']));p=6+2*k/(2-k)
r=Dual(F(25,2),1,0);th=Dual(F(31,25),0,1);u2=(r/L)**2
q=1-((-(1-k)/2)*(1+u2).log()).exp();chi=u2/(u2+r0*r0);s=u2/(1+u2)
tt=list(map(frac,raw['spline_knots_hex']));zz=list(map(frac,raw['z_hex']))
span=bisect.bisect_right(tt,float(q.a.mid))-1
assert q.a>v(tt[span]) and q.a<v(tt[span+1])
basis={span:Dual(1)}
for degree in range(1,8):
 nex={}
 for i in range(span-degree,span+1):
  z=Dual(0)
  if tt[i+degree]!=tt[i]:z+=(q-tt[i])/(tt[i+degree]-tt[i])*basis.get(i,Dual(0))
  if tt[i+degree+1]!=tt[i+1]:z+=(tt[i+degree+1]-q)/(tt[i+degree+1]-tt[i+1])*basis.get(i+1,Dual(0))
  nex[i]=z
 basis=nex
H=(k-3)/2*(1+u2).log()
for m in range(201):
 bm=Dual(0)
 for i,b in basis.items():
  if i>0:bm+=zz[1+m*375+i-1]*b
 H+=chi**max(0,m-1)*bm*(2*m*th).cos()
z=2*q-1;chebs=[Dual(1),z]
for j in range(2,6):chebs.append(2*z*chebs[-1]-chebs[-2])
T=sum((zz[-6+j]*chebs[j] for j in range(6)),Dual(0))
H+=s**(p/2)*th.cos()**(p-2)*th.sin()**2*T
rho=r**3*th.cos()**2*th.sin()*H.exp()
rx=th.cos().a*rho.d[0]-th.sin().a/r.a*rho.d[1];ry=th.sin().a*rho.d[0]+th.cos().a/r.a*rho.d[1]
gap=(rx-ry)/2-(1/k.a+1)
gap6=(rx-ry)/2-7;assert gap6>v(F(313,100))
assert gap>v(F(356,100)) and gap<v(F(357,100))
def serialize(a):return {'interval':str(a),'lo':mp.nstr(mp.mpf(a.a._mpi_[0]),73),'hi':mp.nstr(mp.mpf(a.b._mpi_[1]),73)}
# The claimed coarse public enclosures contain both independent arithmetic results.
assert rx>v(F(19700736695080,10**12)) and rx<v(F(19700736695082,10**12))
assert ry>v(F(-573496321665,10**12)) and ry<v(F(-573496321662,10**12))
out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256((BASE/'data_exact/x3.json').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'asserted_dimensions':[375,201,6,7],'method':'mpmath.iv forward automatic differentiation + independent Cox basis sum + forward Chebyshev recurrence','dps':70,'span':span,'rho':serialize(rho.a),'rho_x':serialize(rx),'rho_y':serialize(ry),'positive_gap':serialize(gap),'positive_gap_for_all_cl_le_6':serialize(gap6),'verdict':'CONFIRMED by independent interval implementation: gap strictly exceeds 3.56.'}
(BASE/'research/density_energy/evidence/iv_dual_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
