"""Universal Laurent-operator comparison, Gaussian rational coefficients."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib
D=Path(__file__).resolve().parents[1]
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def neg(a):return (-a[0],-a[1])
Z=(F(0),F(0));ONE=(F(1),F(0))
class Ring:
 def __init__(self,d=None):self.d={k:v for k,v in (d or {}).items() if v!=Z}
 @staticmethod
 def val(x):return Ring({(0,0,-1,-1):(F(x),F(0))})
 def __add__(self,o):
  if not isinstance(o,Ring):o=Ring.val(o)
  d=self.d.copy()
  for k,v in o.d.items():d[k]=plus(d.get(k,Z),v)
  return Ring(d)
 __radd__=__add__
 def __neg__(self):return Ring({k:neg(v) for k,v in self.d.items()})
 def __sub__(self,o):return self+(-o)
 def __mul__(self,o):
  if not isinstance(o,Ring):o=Ring.val(o)
  d={}
  for (e,n,i,j),v in self.d.items():
   for (ee,nn,ii,jj),w in o.d.items():
    assert i<0 or ii<0,'jet times jet forbidden'
    x,y=(i,j) if i>=0 else (ii,jj);k=(e+ee,n+nn,x,y);d[k]=plus(d.get(k,Z),times(v,w))
  return Ring(d)
 __rmul__=__mul__
 def __eq__(self,o):return isinstance(o,Ring) and self.d==o.d
 def shift(self,e=0,n=0):return Ring({(a+e,b+n,i,j):v for (a,b,i,j),v in self.d.items()})
C=Ring({(0,1,-1,-1):(F(1,2),F(0)),(0,-1,-1,-1):(F(1,2),F(0))})
S=Ring({(0,1,-1,-1):(F(0),F(-1,2)),(0,-1,-1,-1):(F(0),F(1,2))})
E=Ring({(1,0,-1,-1):ONE})
def angdiff(A):return Ring({(e,n,i,j):times(v,(F(0),F(n))) for (e,n,i,j),v in A.d.items()})
cos=[C];sin=[S]
for j in range(5):cos.append(angdiff(cos[-1]));sin.append(angdiff(sin[-1]))
J={(i,j):Ring({(0,0,i,j):ONE}) for i in range(5) for j in range(5-i)}
source=D/'source/src/cert_forcing.py';tree=ast.parse(source.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='cart_from_polar');mod=ast.Module(body=[fn],type_ignores=[])
class ExactScalar:
 @staticmethod
 def exact(x):return F(x)
from math import comb
ns={'MR':ExactScalar,'comb':comb};exec(compile(mod,'frozen_cart_from_polar','exec'),ns);producer=ns['cart_from_polar'](J,4,E,cos,sin)
def apply(P,kind):
 out=Ring()
 for (d,n,i,j),v in P.d.items():
  assert i>=0
  dt=Ring({(d,n,i,j):times(v,(F(-d),F(0))),(d,n,i+1,j):v})
  dp=Ring({(d,n,i,j):times(v,(F(0),F(n))),(d,n,i,j+1):v})
  out+=E*(C*dt-S*dp if kind=='x' else S*dt+C*dp)
 return out
ind={};count=0;terms=0
for a in range(5):
 for b in range(5-a):
  v=J[0,0]
  for _ in range(b):v=apply(v,'y')
  for _ in range(a):v=apply(v,'x')
  ind[a,b]=v;assert v==producer[a,b],(a,b);count+=1;terms+=len(v.d)
  # Reverse derivative order checks commutation as a separate consequence.
  z=J[0,0]
  for _ in range(a):z=apply(z,'x')
  for _ in range(b):z=apply(z,'y')
  assert z==v,(a,b,'commutation')
lap=ind[2,0]+ind[0,2];assert lap==(J[2,0]+J[0,2]).shift(e=2)
lap2=ind[4,0]+2*ind[2,2]+ind[0,4]
expected=(J[4,0]-4*J[3,0]+4*J[2,0]+2*J[2,2]-4*J[1,2]+4*J[0,2]+J[0,4]).shift(e=4);assert lap2==expected
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_UNIVERSAL_CARTESIAN_JET_IDENTITY',operators=count,nonzero_Laurent_jet_terms=terms,commutation_checks=count,laplacian_checks=2,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),operators_exact={f'{a}_{b}':[[*k,str(v[0]),str(v[1])] for k,v in sorted(P.d.items())] for (a,b),P in ind.items()},scope='Exact identity only, no floating residual or Taylor enclosures.')
(D/'evidence/cartesian_identity.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],count,terms)
