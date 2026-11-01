"""Independent rational tuning audit using signed Laurent Cartesian calculus.

No lead code is imported. Coefficients lie in QQ(k)[b], and signed frequencies
are affine pairs (k coefficient, constant). This avoids trigonometric folding.
Run pinned to CPU17, nice19, with one numerical-library thread.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.fields import field
from sympy.polys.domains import QQ

K,k=field('k',QQ)
R,b=ring('b',K.to_domain())
MOD=None
ROOT=Path('research/119_tuned_rational_series')
START=time.monotonic()

def reduced(v):
 v=R(v)
 return v%MOD if MOD is not None else v

def put(d,m,v):
 v=reduced(d.get(m,R.zero)+v)
 if v:d[m]=v
 else:d.pop(m,None)

class F:
 def __init__(self,q,v):
  self.q=K(q);self.v={m:reduced(c) for m,c in v.items() if reduced(c)}
 def scale(self,c):return F(self.q,{m:v*c for m,v in self.v.items()})
 def __add__(self,o):
  assert self.q==o.q
  d=dict(self.v)
  for m,v in o.v.items():put(d,m,v)
  return F(self.q,d)
 def __sub__(self,o):return self+o.scale(-1)
 def __mul__(self,o):
  d={}
  for (a,h),v in self.v.items():
   for (c,j),w in o.v.items():put(d,(a+c,h+j),v*w)
  return F(self.q+o.q,d)
 def diff(self,Y=False):
  d={}
  for (a,h),v in self.v.items():
   m=a*k+h
   put(d,(a,h-1),v*(self.q+m)/2)
   put(d,(a,h+1),v*(self.q-m)*(-1 if Y else 1)/2)
  return F(self.q-1,d)
 def X(self):return self.diff()
 def Y(self):return self.diff(True)
 def check_sine(self):
  assert (0,0) not in self.v
  for (a,h),v in self.v.items():assert self.v.get((-a,-h),R.zero)==-v
 def sine(self,m):return 2*self.v.get((0,m),R.zero)

def sine(q,m,amp=1):
 m=(0,m) if isinstance(m,int) else m
 a,h=m;v=R(amp)/2
 return F(q,{m:v,(-a,-h):-v})
def p(n):return 1-K(2)*n/3

def poisson(f,omit=False):
 P=f.q+1;rhs=f.X();d={}
 for (a,h),v in rhs.v.items():
  m=a*k+h;den=m*m-P*P
  if den:put(d,(a,h),v/den)
  else:
   assert omit or not v,('incompatible',str(f.q),(a,h),str(v))
 g=F(P,d);g.check_sine()
 # D_y=iY; therefore -Delta g=-XXg+YYg.
 residual=g.X().X().scale(-1)+g.Y().Y()-rhs
 if not omit:assert not residual.v
 return g

def adv(g,f):return g.X()*f.Y()-g.Y()*f.X()

def orders(N,mod=None):
 global MOD
 MOD=mod
 ff={1:sine(p(1),1)+sine(p(1),3,b)};gg={1:poisson(ff[1])}
 for n in range(2,N+1):
  acc=F(p(n),{})
  for i in range(1,n):acc=acc+adv(gg[i],ff[n-i])
  ff[n]=acc.scale(K(1)/(2*(n-1)));ff[n].check_sine()
  assert all(a==0 and abs(h)<=4*n-1 and h%2 for a,h in ff[n].v)
  if n<N:gg[n]=poisson(ff[n])
 return ff,gg

def response(t,F0,G0):
 n=3*t;q=2*t-2
 freq=(2,-2) if t==k else int(q)
 e=sine(p(n)+1,freq)
 a=adv(e,F0[1]).scale(K(1)/(2*n));ga=poisson(a)
 bb=(adv(e,F0[2])+adv(G0[1],a)+adv(ga,F0[1])).scale(K(1)/(2*(n+1)));gb=poisson(bb)
 c=(adv(e,F0[3])+adv(G0[1],bb)+adv(gb,F0[1])+adv(G0[2],a)+adv(ga,F0[2])).scale(K(1)/(2*(n+2)))
 for v in (a,bb,c):v.check_sine()
 key=(2,-1) if t==k else (0,int(q)+1)
 return 2*c.v.get(key,R.zero),[a,bb,c]

def serial(f):
 return {'radial_exponent':str(f.q),'signed_laurent':{str(m):str(v.as_expr()) for m,v in sorted(f.v.items())}}

def save(name,data):
 path=ROOT/'verification'/name
 path.write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({'stage':name,'elapsed_s':time.monotonic()-START}),flush=True)

def expr(v):return sp.factor(v.as_expr())

def main():
 global MOD
 P6=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
 ff,gg=orders(6)
 O6=ff[6].sine(1)
 assert O6==P6/35818438656000000
 save('o6_exact.json',{'O6':str(expr(O6)),'claimed_polynomial_matches':True,'F':{str(n):serial(f) for n,f in ff.items()}})
 lowF={i:ff[i] for i in (1,2,3)};lowG={i:gg[i] for i in (1,2)}
 source=json.loads((ROOT/'sources/sigma_check.json').read_text())
 rows=[]
 for t in range(2,13):
  sig,resp=response(t,lowF,lowG)
  claim=source['sigma_small_k'].get(str(t))
  if claim is None:claim='('+source['generic_sigma_numerator']+')/('+source['generic_sigma_denominator']+')'
  claim=R.from_expr(sp.sympify(claim).subs(sp.Symbol('k'),t))
  assert sig==claim,(t,str(expr(sig-claim)))
  rows.append({'k':t,'sigma':str(expr(sig)),'matches_claim':True,'response_mode_counts':[len(a.v) for a in resp]})
 save('sigma_integer_exact.json',{'rows':rows})
 sig,resp=response(k,lowF,lowG)
 claim=R.from_expr(sp.sympify('('+source['generic_sigma_numerator']+')/('+source['generic_sigma_denominator']+')'))
 assert sig==claim
 support=[sorted([list(m) for m in a.v]) for a in resp]
 for a in resp:
  for slope,offset in a.v:
   assert abs(slope)==2
   # m=sign*(q+j), with |j|<=11.
   assert abs((offset+2) if slope==2 else (-offset+2))<=11
 se=expr(sig);ks=sp.Symbol('k');bs=sp.Symbol('b')
 limit=sp.factor(sp.limit(se,ks,sp.oo))
 assert sp.cancel(limit-sp.sympify(source['sigma_inf']))==0
 numerator=sp.Poly(sp.fraction(se)[0],bs)
 gcd=sp.gcd_list(numerator.all_coeffs())
 # The explicit prefactor (k-1)(2k-1)^2 is positive for k>=2.
 norm=sp.cancel(sp.fraction(se)[0]/(-(ks-1)*(2*ks-1)**2))
 nc=sp.Poly(norm,bs).all_coeffs();ngcd=sp.gcd_list(nc)
 assert ngcd in (1,-1)
 constant=sp.Poly(norm,bs).coeff_monomial(1)
 shifted=sp.Poly(constant.subs(ks,ks+7),ks)
 assert all(v>0 for v in shifted.all_coeffs())
 save('sigma_symbolic_exact.json',{'sigma':str(se),'matches_claim':True,'signed_support':support,'sigma_infinity':str(limit),'N_coefficient_gcd':str(ngcd),'N_constant_at_k7_shift_coefficients_descending':[str(v) for v in shifted.all_coeffs()],'positive_constant_for_every_k_ge7':True})
 # All resonance compatibility checks are exact in the quotient field.
 ff,gg=orders(9,P6)
 R2=ff[9].sine(3)
 ref=json.loads((ROOT/'sources/r2_exact.json').read_text())
 assert R2==R.from_expr(sp.sympify(ref['R2_mod_P6']))
 assert R2 and R2.degree()==5
 save('r2_exact.json',{'R2_mod_P6':str(expr(R2)),'matches_claim':True,'nonzero':True,'degree':R2.degree(),'F':{str(n):serial(f) for n,f in ff.items()}})
 MOD=None
 poly=sp.Poly(P6.as_expr(),bs,domain=sp.QQ)
 factors=sp.factor_list(poly)
 assert len(factors[1])==1 and factors[1][0][0].degree()==6 and factors[1][0][1]==1
 sturm=sp.sturm(poly.as_expr(),bs)
 def variations(v):
  signs=[sp.sign(sp.LC(sp.Poly(s,bs)))*(-1 if v==-sp.oo and sp.degree(s,bs)%2 else 1) if v in (-sp.oo,sp.oo) else sp.sign(s.subs(bs,v)) for s in sturm]
  signs=[int(s) for s in signs if s]
  return sum(a!=c for a,c in zip(signs,signs[1:]))
 points=[-sp.oo,sp.Rational(1,4),sp.Rational(1,3),sp.Rational(1,2),sp.Integer(1),sp.oo]
 vs=[variations(v) for v in points]
 assert vs[0]-vs[-1]==2 and vs[1]-vs[2]==1 and vs[3]-vs[4]==1
 save('algebraic_roots.json',{'irreducible_over_Q':True,'factorization':str(factors),'sturm_sequence':[str(x) for x in sturm],'points':[str(x) for x in points],'variations':vs,'exact_real_root_count':2,'isolating_intervals':[['1/4','1/3'],['1/2','1']]})
 files=[]
 for f in sorted((ROOT/'verification').glob('*.json')):
  if f.name=='MANIFEST.json':continue
  raw=f.read_bytes();files.append({'path':f.name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()})
 save('checks.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'all_checks_passed':True,'actual_elapsed_s':time.monotonic()-START,'files':files})
 (ROOT/'verification/tuned_cartesian_exact.py.txt').write_bytes(Path(__file__).read_bytes())

if __name__=='__main__':
 try:main()
 except Exception as exc:
  print(json.dumps({'error_type':type(exc).__name__,'error':str(exc)}),flush=True)
  raise SystemExit(1)
