from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import factorial
import ast,math,json,hashlib
import sympy as sp
from flint import arb,fmpq,ctx
P=Path(__file__).resolve().parents[1]
ctx.prec=512
class ExpPoly:
 def __init__(self,terms=()):
  self.terms={}
  for e,cs in terms:self.add(e,cs)
 def add(self,e,cs):
  row=self.terms.setdefault(e,[])
  while len(row)<len(cs):row.append(arb(0))
  for j,c in enumerate(cs):row[j]+=c
 def deriv(self):
  out=ExpPoly()
  for e,cs in self.terms.items():
   row=[q2arb(e)*c for c in cs]
   for j in range(1,len(cs)):row[j-1]+=j*cs[j]
   out.add(e,row)
  return out
 def __call__(self,x):
  ans=arb(0)
  for e,cs in self.terms.items():
   val=arb(0)
   for c in reversed(cs):val=val*x+c
   ans+=val*(q2arb(e)*x).exp()
  return ans

def q2arb(q):return arb(q.p)/q.q

def exact(x):
 m,e=x.man_exp();return Fraction(int(m))*Fraction(2)**int(e)

def fup(x):
 u=exact(x.upper());v=float(u)
 while math.isfinite(v) and Fraction(v)<u:v=math.nextafter(v,math.inf)
 return v

def phi(z,p,N=80):
 val=arb(0);term=arb(1)
 for j in range(N):val+=term/(p+j+1);term*=z/(j+1)
 M=abs(z).upper();return val+arb(0,(M.exp()*M**N/factorial(N)/(N+p+1)).upper())

# Execute only the audited arithmetic definitions, supplying independent polynomial primitives.
tree=ast.parse((P/'evidence/encl_snapshot.py').read_text())
body=[n for n in tree.body if isinstance(n,(ast.Assign,ast.FunctionDef))]
ns=dict(math=math,arb=arb,fmpq=fmpq,ctx=ctx,ExpPoly=ExpPoly,q2arb=q2arb,fup=fup)
exec(compile(ast.Module(body=body,type_ignores=[]),'audited_encl_definitions','exec'),ns)
assert ns['J_MERGE']==20
cl={'h':arb(1),'hq':fmpq(1),'kind':'inner'}
lamq=fmpq(75,70368744177664);lam=q2arb(lamq);mu=-lam;p=6
cs=[arb((-1)**(p-a)*factorial(p)//factorial(a))/mu**(p-a+1) for a in range(p+1)]
f=ExpPoly([(fmpq(-52)-lamq,cs),(fmpq(-52),[-cs[0]])])
b=ns['range_finite'](f,cl)
for j in range(65):
 x=arb(j)/64;val=(-52*x).exp()*x**7*phi(-lam*x,p)
 assert b.contains(val),(j,b,val)
tiny=ExpPoly([(fmpq(0),[arb(2)**-1200]),(fmpq(1),[arb(2)**-1300])])
bt=ns['range_finite'](tiny,cl)
assert bt.mid()==0 and bt.rad()>0
assert bt.contains(tiny(arb(0))) and bt.contains(tiny(arb(1)))
# Floating coarse theta-radius construction is checked against independent higher precision pi endpoints.
for ntheta in (16,64):
 ctx.prec=160
 th=[arb.pi()/2*i/ntheta for i in range(ntheta+1)]
 boxes=[(th[i]+th[i+1])/2+arb(0,float(((th[i+1]-th[i])/2).upper())*(1+1e-15)) for i in range(ntheta)]
 ctx.prec=512
 for i,bb in enumerate(boxes):
  assert bb.contains(arb.pi()/2*i/ntheta) and bb.contains(arb.pi()/2*(i+1)/ntheta)
# Independent symbolic polar Hessian.
r,t=sp.symbols('r theta',positive=True);F=sp.Function('F')(r,t);c=sp.cos(t);s=sp.sin(t)
Dx=lambda q:c*sp.diff(q,r)-s/r*sp.diff(q,t)
Dy=lambda q:s*sp.diff(q,r)+c/r*sp.diff(q,t)
R=sp.diff(F,r,2);T=sp.diff(F,r,t)/r;Q=sp.diff(F,t,2)/r**2;Pr=sp.diff(F,r)/r;H=sp.diff(F,t)/r**2
forms=[c*c*R-2*s*c*T+s*s*Q+s*s*Pr+2*s*c*H,s*s*R+2*s*c*T+c*c*Q+c*c*Pr-2*s*c*H,s*c*R+(c*c-s*s)*T-s*c*Q-s*c*Pr-(c*c-s*s)*H]
for expr,want in zip((Dx(Dx(F)),Dy(Dy(F)),Dx(Dy(F))),forms):assert sp.simplify(expr-want)==0
merge=ast.parse((P/'evidence/merge_margin_snapshot.py').read_text())
keys=None
for n in merge.body:
 if isinstance(n,ast.Assign) and any(isinstance(q,ast.Name) and q.id=='keys' for q in n.targets):keys=ast.literal_eval(n.value)
assert keys is not None
missing=sorted(set(('VLO','DV','M_ref','MA_ref','NREF'))-set(keys))
assert missing==['DV','MA_ref','M_ref','NREF','VLO']
arrays={k:0 for k in keys};arrays['M_lo']=-1;arrays['MA_lo']=-2
assert arrays.get('M_ref',arrays['M_lo'])==-1 and arrays.get('VLO') is None
assert min(0.75,float('nan'))==0.75
res={'date':datetime.now(timezone.utc).isoformat(),'hashes':{q.name:hashlib.sha256(q.read_bytes()).hexdigest() for q in (P/'evidence').glob('*_snapshot.py')},'J':20,'resonance_range':str(b),'independent_phi_values_contained':65,'tiny_pruning_ball':str(bt),'coarse_theta_endpoints_checked':160,'polar_hessian_identities':3,'merge_missing_arrays':missing,'nan_leaf_can_be_hidden':True,'scope':'Audited methods and archived merge defect; no global production certificate','proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
