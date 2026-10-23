import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,math
import numpy as np
from scipy.special import erf
from hydrostatic_power_tail import PowerVerticalInverse
from node_export_arithmetic import residual,decomposition
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';checks=[];rows=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def rational(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));a=1+x*x+y*y
 return np.stack([y/a,-2*x*y/a**2,1/a-2*y*y/a**2,-2*y/a**2+8*x*x*y/a**3],axis=-1)
def rational_v(x,y):
 a=math.sqrt(1+x*x);A=1+x*x+y*y
 return[x/A,x*x*y/(a*a*A)-math.atan(y/a)/a**3]
def gaussian(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));e=np.exp(-x*x-y*y)
 return np.stack([y*e,-2*x*y*e,(1-2*y*y)*e,(4*x*x-2)*y*e],axis=-1)
def gaussian_v(x,y):return[x*math.exp(-x*x-y*y),(2*x*x-1)*math.exp(-x*x)*math.sqrt(math.pi)*erf(y)/2]
for family,jet,expected in [('rational',rational,rational_v),('gaussian',gaussian,gaussian_v)]:
 points=[(0.,0.),(.137,.219),(-.137,.219),(.137,-.219),(-.137,-.219),(0.,1.1),(1.3,0.),(3.,.2),(.2,3.)]
 if family=='rational':points += [(30.,1.),(2000.,65.),(1.,2000.)]
 for x,y in points:
  want=expected(x,y);J=jet(x,y);ck(f'{family}parities{x,y}',np.array_equal(jet(-x,y),J*np.array([1,-1,1,1]))and np.array_equal(jet(x,-y),J*np.array([-1,-1,1,-1])))
  for order,tail,split in [(32,96,16.),(64,192,128.)]:
   v=PowerVerticalInverse(jet,.5,order,tail,split,.125).at(x,y)['V'];err=max(abs(a-b)/(1+abs(b))for a,b in zip(v,want));ck(f'{family}inverse{x,y,order}',err<2e-11,err);d=residual(J,v,2,x,y)
   if x==y==0:ck('origin undefined ratios '+family+str(order),d['Rf']is None and d['Rv']is None and d['R']==0)
   rows.append(dict(family=family,x=x,y=y,options=[order,tail,split],expected=want,computed=v,scaled_error=err))
# Exact two-jet manufacture detects the missing term when derivatives differ.
J=[F(2),F(3),F(5)];JP=[F(7),F(11),F(13)];M=[F(17),F(19)];Q=[F(23),F(29)]
d=decomposition(J,JP,Q,M,2,31,37);ck('twojet exact identity',d['identity']);ck('samejet shortcut false whenjets differ',d['difference']!=d['velocity_term']and d['jet_term']!=0)
d=decomposition(J,J,Q,M,2,31,37);ck('samejet exact identity',d['identity']and d['jet_term']==0 and d['difference']==d['velocity_term'])
for name,J,v,c,x,y,nfzero,nvzero in [('zero both',[0,0,0],[7,11],2,3,5,True,True),('zero Nf',[0,1,1],[-2,-2],2,1,1,True,False),('zero Nv',[0,1,1],[2,-2],3,1,-1,False,True)]:
 d=residual(J,v,c,x,y);ck(name,d['R']==0 and(d['Rf']is None)==nfzero and(d['Rv']is None)==nvzero)
d=residual([7,11,13],[17,19],5,23,29);ck('Nv lacks scaling coefficient',d['Nv']==abs(F(7))+abs(F(23)*11+F(29)*13)+abs(F(17)*11+F(19)*13));ck('wrong Nv c factor detected',d['Nv']!=abs(F(7))+5*abs(F(23)*11+F(29)*13)+abs(F(17)*11+F(19)*13))
# A quotient of maxima can fail to equal a maximum of pointwise quotients.
num=[F(2),F(10)];den=[F(2),F(100)];ck('maximum ratio semantics',max(a/b for a,b in zip(num,den))==1 and max(num)/max(den)==F(1,10))
paths=[Path(__file__),Path('independent_code/node_export_arithmetic.py'),Path('independent_code/hydrostatic_power_tail.py'),Path('independent_code/independent_hydrostatic.py'),R/'PROOF.md'];bindings={str(p):sha(p)for p in paths};out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_MANUFACTURES_ONLY',count=len(checks),checks=checks,rows=rows,bindings=bindings,scope='No export admitted and no candidate node evaluated. Exact arithmetic identities and empirical manufactured inverse tests only. PrimaryUNRESOLVED.')
(V/'MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
if __name__=='__main__':pass
