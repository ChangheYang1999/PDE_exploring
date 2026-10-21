from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from math import factorial,comb
import json,hashlib,time
import mpmath as mp
import sympy as sp
root=Path(__file__).resolve().parents[1]
mp.mp.dps=65
J=49

def poch(x,n):
 v=F(1)
 for k in range(n):v*=x+k
 return v

def add(*xs):
 out={}
 for x in xs:
  for k,v in x.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}

def scale(x,a):return {k:a*v for k,v in x.items() if a*v}
def deriv(x):return {k-1:k*v for k,v in x.items() if k and v}
def zderiv(x):return {k:k*v for k,v in x.items() if k and v}
def mul(x,y):
 out={}
 for a,v in x.items():
  for b,w in y.items():
   if a+b<=J:out[a+b]=out.get(a+b,F(0))+v*w
 return {k:v for k,v in out.items() if v}
def norm(x):return sum(abs(v)*F(1,4)**k for k,v in x.items())
def hn_norm(x):return sum(abs(v)*F(1,4)**k/k for k,v in x.items() if k)
def cut(x,m=J):return {k:v for k,v in x.items() if k<=m and v}
def order(x):return min(x) if x else None

def solve(n,A,b,h):
 lam=2/A;g=2*b*(A-1);p=1+(n+1)*(2-lam);res=2*n+3
 phi={};beta={};alpha={};defects=[]
 for j in range(1,J+1,2):
  cj=A*p-1-(A-1)*j;defect=h.get(j,F(0))-g*beta.get(j,F(0))
  if not cj:
   assert j==res and not defect,(n,j,defect)
   phij=F(1) if n==0 else F(0);defects.append({'j':j,'defect':str(defect)})
  else:phij=defect/cj
  if phij:phi[j]=phij
  s=beta.get(j,F(0))+phij
  v=-(p-j)*(p-j-1)*s/((j+1)*(j+2))
  if v:beta[j+2]=v
  v=(j-p)*s/(j+1)
  if v:alpha[j+1]=v
 assert not cut(add(scale(phi,A*p-1),scale(zderiv(phi),1-A),scale(beta,g),scale(h,-1)))
 assert not cut(add(deriv(beta),scale(alpha,-p),zderiv(alpha)),J+1)
 assert not cut(add(scale(beta,-p),zderiv(beta),scale(deriv(alpha),-1),scale(phi,-p),zderiv(phi)))
 return {'p':p,'phi':phi,'alpha':alpha,'beta':beta,'defects':defects}

def convforce(ms,n):
 out={}
 for i in range(n):
  j=n-1-i;a=ms[i];d=ms[j]
  out=add(out,mul(a['alpha'],add(scale(d['phi'],d['p']),scale(zderiv(d['phi']),-1))),scale(mul(a['beta'],deriv(d['phi'])),-1))
 return out

def mval(x):return mp.mpf(x.numerator)/x.denominator
def peval(x,z):return sum(mval(v)*z**k for k,v in x.items())
def evaluate(modes,N,r,z,A,b):
 vals={k:mp.mpf(0) for k in ['v','vs','vy','v1','v2','v1s','v1y','v2s','v2y']}
 for d in modes[:N+1]:
  p=mval(d['p']);rp=r**p
  for field,va,ds,dy in [('phi','v','vs','vy'),('alpha','v1','v1s','v1y'),('beta','v2','v2s','v2y')]:
   h=peval(d[field],z);hp=peval(deriv(d[field]),z)
   vals[va]+=rp*h;vals[ds]-=rp/r*(p*h-z*hp);vals[dy]+=rp/r*hp
 g=mval(2*b*(A-1));a=mval(A)
 R=-a*r*vals['vs']+r*z*vals['vy']-vals['v']+g*vals['v2']+vals['v1']*vals['vs']+vals['v2']*vals['vy']
 div=vals['v1s']+vals['v2y'];curl=vals['v2s']-vals['v1y']+vals['vs']
 return {'N':N,'r':str(r),'z':str(z),'transport':str(R),'divergence':str(div),'curl_identity':str(curl),'v':str(vals['v'])}

start=time.monotonic();out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'angular_truncation':J,'cases':[]}
A0,b0,la,c0=sp.symbols('A b lambda C',positive=True)
p0=3-la;alpha4=la*c0/4;beta5=-la*(la+1)*c0/20
h7=sp.expand(alpha4*(p0-3)*c0-beta5*3*c0)
assert sp.simplify(h7-la*(3-2*la)*c0**2/20)==0
assert sp.simplify((A0*(5-2*la)-1-(A0-1)*7).subs(la,2/A0)+2*(A0-1))==0
out['symbolic']={'first_forcing_z7':str(sp.factor(h7)),'first_correction_z7':str(sp.factor(-h7/(2*(A0-1)))),'fourier_factor_after_parameters':'0'}
for A,b in [(F(5,2),F(7,4)),(F(10),F(13,8)),(F(2030145,200000),F(13,8))]:
 lam=2/A;K=28/((15-b)*(A-1));modes=[];case={'A':str(A),'b':str(b),'lambda':str(lam),'normalization':'C=1 for exact coefficient algebra','orders':[]}
 for n in range(6):
  h={} if n==0 else convforce(modes,n)
  d=solve(n,A,b,h);modes.append(d)
  assert order(d['phi'])==4*n+3 and order(d['alpha'])==4*n+4 and order(d['beta'])==4*n+5
  np=norm(d['phi']);nb=norm(d['beta']);na=norm(d['alpha'])
  assert nb<=np/15 and na<=F(4,15)*np
  if n==0:
   for j,v in d['phi'].items():
    m=(j-3)//2
    assert v==(-1)**m*6*poch(b,m)*poch(lam,2*m)/(factorial(m)*factorial(2*m+3))
   assert np<=F(1,60)
  else:
   c=F(7,2)/((A-1)*(1-b/15));bound=c*hn_norm(h)
   assert np<=bound
   prod=sum(norm(modes[i]['phi'])*norm(modes[n-1-i]['phi']) for i in range(n))
   assert hn_norm(h)<=F(8,15)*prod and np<=K*prod
   assert np<=F(comb(2*n,n),n+1)*K**n*norm(modes[0]['phi'])**(n+1)
  if n==1:assert d['phi'][7]==-lam*(3-2*lam)/(40*(A-1))
  case['orders'].append({'n':n,'p':str(d['p']),'density_order':order(d['phi']),'velocity_orders':[order(d['alpha']),order(d['beta'])],'resonances':d['defects'],'first_coefficient':str(d['phi'][4*n+3]),'density_norm':float(np),'inverse_norm_bound':None if not n else float(bound),'catalan_norm_bound':float(F(comb(2*n,n),n+1)*K**n*norm(modes[0]['phi'])**(n+1))})
 case['residuals']=[evaluate(modes,N,r,z,A,b) for r,z in [(mp.mpf('.1'),mp.mpf('.1')),(mp.mpf('1'),mp.mpf('.2'))] for N in range(5)]
 C=1/(12*mp.sin(mp.pi*mval(lam)));case['physical_C']=str(C);case['sufficient_R_limit']=str((15*(15-mval(b))*(mval(A)-1)/(28*C))**(1/(2-mval(lam))))
 out['cases'].append(case)
 (root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print('exact recurrence',A,b,'PASS',[(d['n'],d['density_order'],d['density_norm']) for d in case['orders']],flush=True)

out['gaussian_bessel_checks']=[]
for A,b in [(F(5,2),F(7,4)),(F(10),F(13,8))]:
 lam=mval(2/A);bb=mval(b);r=mp.mpf('1.3')
 for m in range(3):
  # Independent evaluation of the Fourier kernel using the Bessel K form.
  c=1/(2**(bb-mp.mpf('.5'))*mp.sqrt(mp.pi)*mp.gamma(bb))
  fun=lambda eta:eta**(bb+2*m-mp.mpf('.5'))*mp.besselk(bb-mp.mpf('.5'),eta)
  kernel=(-1)**m*c/mp.pi*mp.quad(fun,[0,1,mp.inf])
  logfun=lambda x:mp.exp((1-lam)*x-(2*m+1)*mp.log(1+mp.exp(x)))
  conv=r**(-lam-2*m)*mp.quad(logfun,[-mp.inf,0,mp.inf])
  value=kernel*conv;exact=(-1)**m*mp.rf(bb,m)*mp.rf(lam,2*m)/(2*mp.factorial(m)*mp.sin(mp.pi*lam))*r**(-lam-2*m)
  err=abs(value-exact)/abs(exact);assert err<mp.mpf('1e-50'),str(err)
  row={'A':str(A),'b':str(b),'m':m,'r':str(r),'kernel_integral':str(kernel),'convolution_integral':str(conv),'physical_derivative':str(value),'formula':str(exact),'relative_error':str(err)}
  out['gaussian_bessel_checks'].append(row);(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print('Bessel',A,b,m,'relative',mp.nstr(err,5),flush=True)
out['seconds']=time.monotonic()-start;out['complete']=True;(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print('ALL CHECKS PASS',out['seconds'],flush=True)
