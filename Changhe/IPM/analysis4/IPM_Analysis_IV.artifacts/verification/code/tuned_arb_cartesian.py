"""Independent Cartesian Arb recursion for tuned c=3 profiles through order30.

Only exact root intervals and the independently verified response polynomials
are reused. Structural symmetry, support, and proven resonance compatibilities
are projected after checking that the discarded interval residual contains0.
"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from functools import lru_cache
from decimal import Decimal
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,fmpq,ctx
import sympy as sp
ctx.prec=768
start=time.monotonic();root=Path('research/119_tuned_rational_series')
counts=dict(cartesian_poisson_coefficients=0,structural_zero_checks=0,symmetry_checks=0,compatibility_projections=0,source_rounding_checks=0)
@lru_cache(None)
def aa(q):return arb(fmpq(str(q)))
def put(d,m,v):d[m]=d.get(m,arb(0))+v
class F:
 def __init__(self,q,v):self.q=Q(q);self.v={m:c for m,c in v.items() if not c.is_zero()}
 def scale(self,c):return F(self.q,{m:v*c for m,v in self.v.items()})
 def __add__(self,o):
  assert self.q==o.q
  d=dict(self.v)
  for m,v in o.v.items():put(d,m,v)
  return F(self.q,d)
 def __sub__(self,o):return self+o.scale(-1)
 def __mul__(self,o):
  d={}
  for m,v in self.v.items():
   for l,w in o.v.items():put(d,m+l,v*w)
  return F(self.q+o.q,d)
 def diff(self,Y=False):
  d={}
  for m,v in self.v.items():
   put(d,m-1,v*aa((self.q+m)/2));put(d,m+1,v*aa((self.q-m)/2)*(-1 if Y else 1))
  return F(self.q-1,d)
 def X(self):return self.diff()
 def Y(self):return self.diff(True)
 def sine(self,m):return 2*self.v.get(m,arb(0))
 def norm(self):return 2*sum((abs(v) for m,v in self.v.items() if m>0),arb(0))
 def project(self,degree,parity,zero=None):
  d={}
  for m,v in self.v.items():
   if m==0 or abs(m)>degree or m%2!=parity:
    assert v.contains(0);counts['structural_zero_checks']+=1
   elif m>0:
    assert v.overlaps(-self.v.get(-m,arb(0)));counts['symmetry_checks']+=1
    if m==zero:
     assert v.contains(0);counts['compatibility_projections']+=1
    else:d[m]=v;d[-m]=-v
  return F(self.q,d)
def sine(q,m,amp):return F(q,{m:amp/2,-m:-amp/2})
def p(n):return Q(1)-Q(2*n,3)
def adv(g,f):return g.X()*f.Y()-g.Y()*f.X()
def poisson(f,n,H=None):
 P=f.q+1;rhs=f.X();d={};res=2*n//3-2 if n>=6 and n%3==0 else None
 for m,v in rhs.v.items():
  if m==0:assert v.contains(0);continue
  den=Q(m*m)-P*P
  if den:d[m]=v/aa(den)
  else:assert v.contains(0)
 g=F(P,d)
 if res is not None and H is not None:g=g+sine(P,res,H)
 g=g.project(4*n,0)
 rr=g.X().X().scale(-1)+g.Y().Y()-rhs
 for v in rr.v.values():assert v.contains(0);counts['cartesian_poisson_coefficients']+=1
 return g
def order(n,ff,gg):
 acc=F(p(n),{})
 for i in range(1,n):acc=acc+adv(gg[i],ff[n-i])
 return acc.scale(aa(Q(1,2*(n-1)))).project(4*n-1,1)
def values(f):return {str(m):f.sine(m).str(65,radius=True) for m in sorted(f.v) if m>0}
def evaluate(poly,x):
 out=arb(0)
 for c in sp.Poly(poly,sp.Symbol('b'),domain=sp.QQ).all_coeffs():out=out*x+aa(Q(str(c)))
 return out
def check_round(value,text):
 q=Q(text);half=Q(10)**Decimal(text).as_tuple().exponent/2
 assert aa(q-half).union(aa(q+half)).contains(value),(text,value.str(40,radius=True))
 counts['source_rounding_checks']+=1

try:
 coeff=[10532171936,-243275209320,2783057141280,-20675598499400,96180432855375,-222533688701250,176703765525000]
 def peval(x):
  out=Q(0)
  for c in reversed(coeff):out=out*x+c
  return out
 small=json.loads((root/'verification/sigma_integer_exact.json').read_text())['rows'];polys={r['k']:sp.sympify(r['sigma']) for r in small}
 raw=json.loads((root/'verification/algebraic_numeric_values.json').read_text())['rows'];allrows=[];series=[]
 for index,item in enumerate(raw):
  lo,hi=map(Q,item['root_interval']);flo=peval(lo)
  for _ in range(400):
   mid=(lo+hi)/2;fm=peval(mid)
   if flo*fm<0:hi=mid
   else:lo=mid;flo=fm
  x=aa(lo).union(aa(hi));ff={1:sine(p(1),1,arb(1))+sine(p(1),3,x)};gg={1:poisson(ff[1],1)}
  source=json.loads((root/'sources/tuned_mp_root0_N30.json').read_text()) if index==0 else None
  references={r['n']:r for r in source['rows']} if source else {}
  for n in range(2,31):
   f=order(n,ff,gg)
   if n>=6 and n%3==0:
    q=2*n//3-2;obstruction=f.sine(q-1)
    assert obstruction.contains(0)
    f=f.project(4*n-1,1,zero=q-1);ff[n]=f
    ft=dict(ff);gt=dict(gg);gt[n]=poisson(f,n,arb(0))
    for m in range(n+1,n+4):
     ft[m]=order(m,ft,gt)
     if m<n+3:gt[m]=poisson(ft[m],m)
    remainder=ft[n+3].sine(q+1);sig=evaluate(polys[n//3],x);H=-remainder/sig
    gg[n]=poisson(f,n,H)
    row=dict(root_index=index+1,n=n,H=H.str(65,radius=True),sigma=sig.str(65,radius=True),density_norm=f.norm().str(65,radius=True),density_root=(f.norm().log()/n).exp().str(40,radius=True),compatibility_obstruction=obstruction.str(30,radius=True))
    if n in references:
     ref=references[n]
     for name,v in [('H',H),('sigma',sig),('l1',f.norm())]:check_round(v,ref[name])
     row['source_rounding_checks_pass']=True
    allrows.append(row)
    print(json.dumps(dict(root=index+1,n=n,H=row['H'],elapsed_s=time.monotonic()-start)),flush=True)
   else:ff[n]=f;gg[n]=poisson(f,n)
  series.append(dict(root_index=index+1,root_interval=[str(lo),str(hi)],density={str(n):values(f) for n,f in ff.items()},stream={str(n):values(g) for n,g in gg.items()}))
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');out=root/'verification'/('arb_N30_'+stamp);out.mkdir()
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,precision_bits=768,maximum_order=30,counts=counts,rows=allrows,actual_elapsed_s=time.monotonic()-start,scope='Certified finite Cartesian evaluation; symmetry, support and compatibility projections use exact identities proved separately. Infinite convergence follows from TheoremT, not from this computation.')
 (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(out/'coefficients.json').write_text(json.dumps(series,indent=2)+'\n');(out/'code.py.txt').write_bytes(Path(__file__).read_bytes())
 files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()};(out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,output=str(out),counts=counts,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc),frames=[{'file':Path(f.filename).name,'line':f.lineno,'code':f.line} for f in traceback.extract_tb(exc.__traceback__)])),flush=True)
 raise SystemExit(1)
