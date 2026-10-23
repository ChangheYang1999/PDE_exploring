"""Manufactured gate for result83, independent source-integral cross-check."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,math
import mpmath as mp
import sympy as sp
from smooth_exact_high_jets import solve,enc,frac,add,scale
mp.mp.dps=75

def M(x):
    v=frac(x);return mp.mpf(v.numerator)/v.denominator


def inp(alpha,L,ell,coeff):
    return dict(alpha=enc(alpha),length=enc(L),cl=enc(ell),chebyshev_coefficients=[[enc(v)for v in row]for row in coeff])

exact_checks=0;quad_rows=[]
def progress(phase,**data):
    row=dict(utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',phase=phase,exact_checks=exact_checks,source_integrals=len(quad_rows),**data)
    Path('research/smooth_canonical_high_jets/verification/manufactured_progress.json').write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps(row),flush=True)
progress('started')
# Closed canonical radial streams: coefficient of xy*r^(2h) is
# -a*binom(-alpha,h)/(2(h+2)L^(2h)), including its true harmonic constant.
for alpha in [F(1,4),F(1,3),F(2,5)]:
 for L in [F(1),F(3,2)]:
  a=F(7,3);d=inp(alpha,L,F(5,2),[[a]]);s=solve(d,5)
  expected={};b=F(1)
  for h in range(6):
   if h:b*=-(alpha+h-1)/h
   factor=-a*b/(2*(h+2)*L**(2*h))
   for t in range(h+1):expected[(1+2*t,1+2*h-2*t)]=factor*math.comb(h,t)
  assert s['psi']==expected
  assert s['c']==-a/4 and not s['poisson']
  assert all(v['h']==0 for v in s['moments'][1:])
  exact_checks+=3
progress('radial exact jets complete')
# Random-looking rational Chebyshev data, independent symbolic Taylor series.
coeff=[[F((-1)**(k+n)*(2*k+3*n+1),(k+2)*(n+2))for n in range(4)]for k in range(7)]
d=inp(F(3,10),F(5,4),F(9,4),coeff);s=solve(d,5)
x,y,z=sp.symbols('x y z',real=True);alpha=sp.Rational(3,10);L=sp.Rational(5,4)
# Introduce a single Taylor parameter z in both Cartesian variables. This
# independent CAS expansion checks all coefficients through degree seven.
ss=(x*x+y*y)/L**2;w=(1+z*z*ss)**(-alpha);t=1-2*w
expr=0
for k in range(4):
 real=sum((-1)**j*sp.binomial(2*k,2*j)*x**(2*k-2*j)*y**(2*j)for j in range(k+1))
 pk=sum(sp.Rational(c.numerator,c.denominator)*sp.chebyshevt(n,t)for n,c in enumerate(coeff[k]))
 expr+=z**(2*k+1)*y*real/L**(2*k)*w*(1+z*z*ss)**(-k)*pk
series=sp.Poly(sp.series(expr,z,0,8).removeO().subs(z,1).expand(),x,y)
for powers,coef in series.terms():
 assert s['rho'].get(powers,F(0))==F(int(sp.numer(coef)),int(sp.denom(coef)));exact_checks+=1
assert not {k:v for k,v in s['rho'].items()if sum(k)<=7 and k not in dict(series.terms())}

progress('symbolic Cartesian series complete')
# A separate smooth source integrand evaluates int r^(1-n) s_n/(2n).
# The leading r^n cancellation is factored algebraically. No boundary moment
# formula (10), monomial-in-w coefficients, or exact h is used by quadrature.
a=M(d['alpha']);length=M(d['length'])
def pk(k,t,der=False):
 if k>=len(coeff):return mp.mpf('0')
 if not der:return sum(M(c)*mp.chebyt(j,t)for j,c in enumerate(coeff[k]))
 return sum(M(c)*j*mp.chebyu(j-1,t)for j,c in enumerate(coeff[k])if j)

def integrand(r,j):
 v=1+(r/length)**2;w=v**(-a);sig=1-1/v;t=1-2*w
 if j==1:
  h=pk(0,t)-sig*pk(1,t)/2
  hm=pk(0,t,True)-sig*pk(1,t,True)/2
  minus=-2*a*h+4*a*w*hm-(1-sig)*pk(1,t)
 else:
  k=j-1;h=pk(k,t)-sig*pk(k+1,t);hm=pk(k,t,True)-sig*pk(k+1,t,True)
  minus=(-(a+k)*h+2*a*w*hm-(1-sig)*pk(k+1,t))
 h=pk(j,t)-sig*pk(j+1,t);hm=pk(j,t,True)-sig*pk(j+1,t,True)
 plus=(2*j+1-(a+j)*sig)*h+2*a*sig*w*hm-sig*(1-sig)*pk(j+1,t)
 # s_(2j)=w*sigma^j*(minus+plus)/2; prefactor in h_(2j) is1/(4j).
 return w*r/(length*length+r*r)**j*(minus+plus)/(8*j)

for j in range(1,7):
 numerical=mp.quad(lambda r:integrand(r,j),[0,length/2,length,2*length,mp.inf])
 exact=M(s['moments'][j-1]['h']);error=abs(numerical-exact)
 assert error<mp.mpf('1e-42'),(j,numerical,exact,error)
 quad_rows.append(dict(n=2*j,source_integral=mp.nstr(numerical,65),exact_h=mp.nstr(exact,65),absolute_error=mp.nstr(error,8)))
 progress('source quadrature',mode=2*j,error=mp.nstr(error,8))
# The same source formula can also be checked directly away from both endpoints.
for j in range(1,7):
 def fmode(m,r):
  k=(m-1)//2;v=1+(r/length)**2;ww=v**(-a);sig=1-1/v;tt=1-2*ww
  return r*ww*(pk(0,tt)-sig*pk(1,tt)/2)if k==0 else r*ww*sig**k*(pk(k,tt)-sig*pk(k+1,tt))/2
 for r in [mp.mpf('.23'),mp.mpf('1.3'),mp.mpf('9')]:
  n=2*j
  source=(mp.diff(lambda u:fmode(n-1,u),r)-(n-1)*fmode(n-1,r)/r+mp.diff(lambda u:fmode(n+1,u),r)+(n+1)*fmode(n+1,r)/r)/2
  target=r**(1-n)*source/(2*n)
  assert abs(target-integrand(r,j))<mp.mpf('1e-65');exact_checks+=1
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',exact_or_symbolic_checks=exact_checks,quadrature_digits=75,source_integral_checks=quad_rows,input=d,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Manufactured finite-formula invariants and independently integrated canonical source moments. High-precision quadrature is supporting numerical evidence, not an interval proof.')
p=Path('research/smooth_canonical_high_jets/verification/manufactured.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ['input','source_integral_checks']}),flush=True)
