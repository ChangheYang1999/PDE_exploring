"""Exact first-order 1/k jet of the high-frequency resonant cycle."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import sys,json,time
sys.dont_write_bytecode=True
from flint import fmpq as Q,fmpq_poly as Poly
from transfer_cancellation_audit import polar_low,polar_limit
from general_fixed_deficit_audit import low,cycle

def jet(period,lf,lg):
 d=Q(2,period);c=1/(1-d);f={};g={0:{0:(Poly([1]),Poly([]))}}
 def add(out,s,v0,v1):
  a,b=out.get(s,(Poly([]),Poly([])));out[s]=(a+v0,b+v1)
 def product(out,s,high,amp,c0,c1):
  h0,h1=high;add(out,s,amp*h0*c0,amp*(h1*c0+h0*c1))
 for r in range(1,period+1):
  out={};ar=(r-1)*(c-1)
  for i in range(r):
   p=1-d*(r-i);P0=2-d*i
   for s,h in g[i].items():
    for ell,a in lf[r-i].items():
     c0=-(ell+p)/(2*c);c1=(P0*ell-p*(s-2))/(4*c)+(ell+p)*ar/(4*c*c)
     product(out,s+ell,h,a,c0,c1)
     c0=(p-ell)/(2*c);c1=(P0*ell+p*(s-2))/(4*c)-(p-ell)*ar/(4*c*c)
     product(out,s-ell,h,a,c0,c1)
  for i in range(1,r):
   P=2-d*i;p0=1-d*(r-i)
   for ell,b in lg[i].items():
    for s,h in f[r-i].items():
     c0=(P+ell)/(2*c);c1=(P*(s-2)-p0*ell)/(4*c)-(P+ell)*ar/(4*c*c)
     product(out,s+ell,h,b,c0,c1)
     c0=(ell-P)/(2*c);c1=-(P*(s-2)+p0*ell)/(4*c)-(ell-P)*ar/(4*c*c)
     product(out,s-ell,h,b,c0,c1)
  f[r]=out
  if r<period:
   gout={}
   for s,(a,b) in out.items():
    mult=-1/(2*(s+1-d*r));add(gout,s+1,a*mult,b*mult)
    add(gout,s-1,Poly([]),a/8)
   g[r]=gout
 a,b=f[period].get(1,(Poly([]),Poly([])))
 return -a/2,-b/2

def main():
 start=time.monotonic();root=Path('research/72_higher_factorial_gain')
 lf,lg=polar_low(3,{1:Poly([1]),3:Poly([0,1])});lam,mu=jet(3,lf,lg)
 assert lam==polar_limit(3,lf,lg)
 K=Poly([0,1]);N=(K-1)*(2*K-1)**2*(8478*K**4-13599*K**3+507*K**2+4184*K-340)
 D=9600*K*(3*K-4)*(3*K-2)*(3*K+1)*(3*K+2)*(6*K-5)*(6*K-1)
 known_lam=N[7]/D[7];known_mu=N[6]/D[7]-N[7]*D[6]/D[7]**2
 assert lam[0]==known_lam and mu[0]==known_mu,(lam,mu,known_lam,known_mu)
 P=Poly([314,-2925,6735,75]);common=P.gcd(mu);assert common.degree()==0,(P,mu,common)
 mu_num=Poly([-3022,34665,-68355,-105225]);assert mu==mu_num/1555200
 # Retain a direct rational Bezout certificate, independent of a gcd label.
 r0,r1=P,mu_num;u0,u1=Poly([1]),Poly([]);v0,v1=Poly([]),Poly([1])
 while r1:
  quotient,remainder=divmod(r0,r1);r0,r1=r1,remainder
  u0,u1=u1,u0-quotient*u1;v0,v1=v1,v0-quotient*v1
 u0,v0=u0/r0[0],v0/r0[0];assert u0*P+v0*mu_num==Poly([1])
 from flint import arb,ctx
 ctx.prec=640;root_intervals=[]
 for left,right in [(Q(-90233,1000),Q(-90232,1000)),(Q(19598,100000),Q(19599,100000)),(Q(23674,100000),Q(23675,100000))]:
  for _ in range(100):
   mid=(left+right)/2
   if P(left)*P(mid)<0:right=mid
   else:left=mid
  assert P(left)*P(right)<0
  center=arb((left+right)/2);radius=arb((right-left)/2);bball=arb(center,radius)
  val=arb(0)
  for a in reversed(mu.coeffs()):val=val*bball+arb(a)
  assert not val.contains(0)
  root_intervals.append(dict(beta_left=str(left),beta_right=str(right),beta_interval=bball.str(32,radius=True),mu_interval=val.str(32,radius=True),mu_nonzero_certified=True))
 cases=[]
 for b in [Q(-1),Q(0),Q(1,10),Q(1,5),Q(1,4),Q(1)]:
  F,G=low(3,{1:Q(1),3:b});rows=[]
  for k in [32,64,128,256]:
   v=cycle(3,F,G,k,0);first=k*(v-lam(b));err=first-mu(b)
   rows.append(dict(k=k,kR_exact=str(v),first_correction_exact=str(first),error_exact=str(err),error_float=float(err),scaled_error=float(k*err)))
  cases.append(dict(beta=str(b),lambda_exact=str(lam(b)),mu_exact=str(mu(b)),rows=rows))
 identities=0
 for p in range(1,5):
  for k in range(0,21):
   for x,y in [(Q(1,2),Q(2,3)),(Q(1),Q(1)),(Q(3,2),Q(1,4))]:
    # Apply (7) to x^p,y^p, making every quantity rational.
    lhs=sum((Q(comb(k,i))*x**i*y**(k-i))**p for i in range(k+1));rhs=(x+y)**(p*k)
    assert lhs<=rhs;identities+=1
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),lambda_coefficients=[str(v) for v in lam.coeffs()],mu_coefficients=[str(v) for v in mu.coeffs()],gcd_cubic_mu_coefficients=[str(v) for v in common.coeffs()],mu_numerator_coefficients=[str(v) for v in mu_num.coeffs()],bezout_P=[str(v) for v in u0.coeffs()],bezout_mu_numerator=[str(v) for v in v0.coeffs()],bezout_identity_exact=True,root_intervals=root_intervals,known_sin1_lambda=str(known_lam),known_sin1_mu=str(known_mu),all_symbolic_checks_passed=True,finite_cycle_comparisons=cases,binomial_power_inequalities=identities,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/first_jet.json').write_text(json.dumps(result,indent=2)+'\n')
 for name in ['transfer_first_jet.py','transfer_cancellation_audit.py','general_fixed_deficit_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in result.items() if k!='finite_cycle_comparisons'}))
if __name__=='__main__':main()
