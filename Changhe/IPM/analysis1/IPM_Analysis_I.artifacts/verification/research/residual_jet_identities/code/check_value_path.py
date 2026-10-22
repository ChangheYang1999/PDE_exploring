"""Generic exact polynomial expressions for value/derivative velocity prefactors."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,hashlib,json,time,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_v22/source/src/cert_resid.py';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();h='1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053';assert sha(S)==h;t0=time.monotonic();tree=ast.parse(S.read_text());cls=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name=='Certifier');value=next(x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name=='cell_core');core=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_cell_core_deriv')
# Ring Q[A,B,v,z], where v=e^-t_a,z=e^-sigma. Exact arbitrary symbols, not samples.
class E:
 def __init__(self,terms):self.terms={k:F(v) for k,v in terms.items() if v}
 @staticmethod
 def coerce(a):return a if isinstance(a,E) else E({(0,0,0,0):F(a)})
 @staticmethod
 def symbol(i):k=[0]*4;k[i]=1;return E({tuple(k):1})
 def __add__(self,o):
  o=E.coerce(o);t=dict(self.terms)
  for k,v in o.terms.items():t[k]=t.get(k,F(0))+v
  return E(t)
 __radd__=__add__
 def __neg__(self):return E({k:-v for k,v in self.terms.items()})
 def __sub__(self,o):return self+-E.coerce(o)
 def __rsub__(self,o):return E.coerce(o)+-self
 def __mul__(self,o):
  o=E.coerce(o);t={}
  for k,v in self.terms.items():
   for l,w in o.terms.items():m=tuple(a+b for a,b in zip(k,l));t[m]=t.get(m,F(0))+v*w
  return E(t)
 __rmul__=__mul__
 def scale(self,o):return self*o
 def __eq__(self,o):return self.terms==E.coerce(o).terms
class MR:
 def __new__(cls,m,r=0):assert r==0;return E.coerce(m)
 @staticmethod
 def exact(m):return E.coerce(m)
assigns={}
for name in ['dpsi','Pn','Qn']:
 nodes=[x for x in ast.walk(value) if isinstance(x,ast.Assign) and len(x.targets)==1 and ast.unparse(x.targets[0])==name];assert len(nodes)==1;assigns[name]=nodes[0]
append={}
for name in ['Pt','Qt']:
 nodes=[x for x in ast.walk(core) if isinstance(x,ast.Call) and isinstance(x.func,ast.Attribute) and x.func.attr=='append' and ast.unparse(x.func.value)==name];assert len(nodes)==1 and len(nodes[0].args)==1;append[name]=nodes[0]
a,b,v,z=[E.symbol(i) for i in range(4)];checks=0;examples=[]
for n in range(1,262):
 psi=(a+b)*F(1,4*n);env={'__builtins__':{},'A':a,'B':b,'psi':psi,'inv_e':v,'inv_e2':v*v,'Em1':z,'Em2':z*z,'MR':MR,'tm_mul':lambda x,y:x*y,'n':n}
 for name,node in assigns.items():env[name]=eval(compile(ast.Expression(node.value),str(S),'eval'),env)
 assert env['dpsi']==(b-a)*v*z*F(1,2)
 assert env['Pn']==-(a+b)*v*v*z*z*F(1,4)
 assert env['Qn']==(b-a)*v*v*z*z*F(1,4)
 env['accP']=psi;env['accQ']=b-a
 pp=eval(compile(ast.Expression(append['Pt'].args[0]),str(S),'eval'),env);qq=eval(compile(ast.Expression(append['Qt'].args[0]),str(S),'eval'),env)
 assert pp==env['Pn'] and qq==env['Qn'];checks+=5
 if n in [1,261]:examples.append(dict(n=n,P=[[list(k),str(c)] for k,c in sorted(pp.terms.items())],Q=[[list(k),str(c)] for k,c in sorted(qq.terms.items())]))
assert checks==1305 and sha(S)==h
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_GENERIC_EXACT_VALUE_DERIVATIVE_PREFACTORS',modes=261,exact_polynomial_identities=checks,symbols=['A','B','exp(-t_a)','exp(-sigma)'],source_value_bindings=[dict(name=name,line=x.lineno,expression=ast.unparse(x.value)) for name,x in assigns.items()],source_derivative_bindings=[dict(name=name,line=x.lineno,expression=ast.unparse(x.args[0])) for name,x in append.items()],examples=examples,source_sha256=h,code_sha256=sha(Path(__file__)),seconds=time.monotonic()-t0,scope='Selected source prefactor expressions evaluated on generic exact polynomial symbols. Initial psi=(A+B)/(4n) and exp(-2t)=v^2 z^2 are exact identities. This is not a full surrogate or floating execution; no radius/remainder assertion.')
(D/'evidence/value_path.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks,out['seconds'])
