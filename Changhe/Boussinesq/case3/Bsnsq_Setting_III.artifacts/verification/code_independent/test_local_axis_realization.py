"""Independent packet121 symbolic PDE and high-precision asymptotic controls.

No lead or NUM code is read or imported by this script. Formal recurrences are
checked against differentiation of the original Cartesian profile equations.
"""
from pathlib import Path
from datetime import datetime, timezone
from time import monotonic
import json, hashlib
import sympy as s
import mpmath as mp

root=Path('research/121_local_and_finite_axis_realization/verification')
t0=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING'}
x,y=s.symbols('x y',real=True);beta=s.symbols('beta',positive=True);a0=s.symbols('a0',positive=True)
N=11
G={n:s.Function('g'+str(n))(y) for n in range(1,N+3,2)}
A={n:s.Function('a'+str(n))(y) for n in range(2,N+3,2)}
psi=sum(x**n*g for n,g in G.items());theta=sum(x**n*a for n,a in A.items())
ell=s.Symbol('g1_at_zero')
w1=beta*x-s.diff(psi,y);w2=beta*y+s.diff(psi,x)-ell
omega=-s.diff(psi,x,2)-s.diff(psi,y,2)
RT=s.expand(w1*s.diff(theta,x)+w2*s.diff(theta,y)-(beta-2)*theta)
RO=s.expand(w1*s.diff(omega,x)+w2*s.diff(omega,y)+omega-s.diff(theta,x))
b=beta*y+G[1]-ell;aa=beta-s.diff(G[1],y)
wg={n:-s.diff(G[n],y,2)-(n+1)*(n+2)*G[n+2] for n in range(1,N+1,2)}
checks=[]
for m in range(1,(N+1)//2+1):
 n=2*m
 expected=b*s.diff(A[n],y)+(n*aa-beta+2)*A[n]
 for j in range(1,m):expected+=(2*j+1)*G[2*j+1]*s.diff(A[n-2*j],y)-(n-2*j)*s.diff(G[2*j+1],y)*A[n-2*j]
 assert s.expand(RT.coeff(x,n)-expected)==0,n
 checks.append({'equation':'T','x_degree':n,'identically_zero_difference':True})
for n in range(1,N+1,2):
 expected=b*s.diff(wg[n],y)+(n*aa+1)*wg[n]-(n+1)*A[n+1]
 for j in range(1,(n-1)//2+1):expected+=(2*j+1)*G[2*j+1]*s.diff(wg[n-2*j],y)-(n-2*j)*s.diff(G[2*j+1],y)*wg[n-2*j]
 assert s.expand(RO.coeff(x,n)-expected)==0,n
 checks.append({'equation':'V','x_degree':n,'identically_zero_difference':True})
assert s.expand(RO.coeff(x,1)-(b*s.diff(wg[1],y)+(2*beta+1-s.diff(b,y))*wg[1]-2*A[2]))==0
out['arbitrary_function_recurrences']=checks
h=s.Function('h')(y);chi=s.Function('chi')(x)
delta=-h*x**3*chi/6
expected=h*(chi+x*s.diff(chi,x)+x*x*s.diff(chi,x,2)/6)+s.diff(h,y,2)*x*x*chi/6
assert s.simplify((-s.diff(delta,x,2)-s.diff(delta,y,2))/x-expected)==0
out['logarithmic_cutoff_laplacian_identity']=True
out['exact_base_cases']=[]
for bv,av in [(s.Rational(4),s.Rational(1)),(s.Rational(9),s.Rational(1)),(s.Rational(25,9),s.Rational(3,2))]:
 c=1+bv/2;p=(bv-1)/(2*bv);L=3*c*s.sqrt(bv)/(4*av);hh=s.sqrt(bv)*L;S0=L*L+hh*hh
 ellv=-c*S0/(2*p*hh)
 pe=ellv*x*(1+(x*x+y*y-2*hh*y)/S0)**p
 oe=-s.diff(pe,x,2)-s.diff(pe,y,2)
 q=s.diff(oe,x).subs(x,0);be=bv*y+s.diff(pe,x).subs(x,0)-ellv
 H=be*s.diff(q,y)+(2*bv+1-s.diff(be,y))*q
 F=be*s.diff(H,y)-(2*s.diff(be,y)-3*bv-2)*H
 at0=lambda v:s.simplify(v.subs(y,0))
 qprime=at0(s.diff(q,y));Fprime=at0(s.diff(F,y))
 targetq=32*av**2*(3*bv+5)/(9*bv**2*(bv+1)*(bv+2))
 assert qprime==targetq
 assert Fprime==(3*bv+2)*(2*bv+1)*qprime/2
 P=ellv*x+c*x*y-(4*av/bv)*x**3/6
 for i in range(4):
  for j in range(4-i):
   assert s.simplify(s.diff(pe-P,x,i,y,j).subs({x:0,y:0}))==0,(bv,i,j)
 wx=bv*x-s.diff(P,y);wy=bv*y+s.diff(P,x)-ellv;oo=-s.diff(P,x,2)-s.diff(P,y,2);tt=av*x*x
 assert s.expand(wx*s.diff(tt,x)+wy*s.diff(tt,y)-(bv-2)*tt)==0
 assert s.expand(wx*s.diff(oo,x)+wy*s.diff(oo,y)+oo-s.diff(tt,x))==0
 out['exact_base_cases'].append({'beta':str(bv),'a0':str(av),'L':str(L),'h':str(hh),'ell':str(ellv),'q_prime_0':str(qprime),'F_prime_0':str(Fprime),'local_polynomial_PDE_exact':True,'base_cubic_jet_exact':True})
mp.mp.dps=110
out['lower_axis_asymptotic_controls']=[]
for bs in ['4','9','2.5']:
 bv=mp.mpf(bs);av=mp.mpf(1);p=(bv-1)/(2*bv);c=1+bv/2;L=3*c*mp.sqrt(bv)/(4*av);hh=mp.sqrt(bv)*L;S0=L*L+hh*hh
 BB=c/(2*p*hh*S0**(p-1));Qe=4*BB*p*(p+1)
 bfun=lambda yy:bv*yy-BB*(L*L+(yy-hh)**2)**p+BB*S0**p
 qfun=lambda yy:4*BB*p*(L*L+(yy-hh)**2)**(p-2)*(2*L*L+(p+1)*(yy-hh)**2)
 rows=[]
 for exponent in [5,12,24,48,96]:
  r=mp.mpf(10)**exponent;yy=hh-r
  # Differentiate with a relative radius perturbation. Absolute steps at
  # y~1e96 lose accuracy even at 110 digits; the parameter below is O(1).
  qprime=-mp.diff(lambda z:qfun(hh-r*mp.exp(z)),mp.mpf(0))/r
  bprime=-mp.diff(lambda z:bfun(hh-r*mp.exp(z)),mp.mpf(0))/r
  H=bfun(yy)*qprime+(2*bv+1-bprime)*qfun(yy)
  leading=-2*BB*Qe*r**(-1-2/bv)
  ratio=H/leading
  rows.append({'radius_power10':exponent,'H_sign':int(mp.sign(H)),'H_over_leading':mp.nstr(ratio,45),'relative_error':mp.nstr(abs(ratio-1),12)})
 assert abs(mp.mpf(rows[-1]['H_over_leading'])-1)<mp.mpf('1e-30')
 out['lower_axis_asymptotic_controls'].append({'beta':bs,'rows':rows})
out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-t0)
out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],'recurrence_checks':len(checks),'base_cases':out['exact_base_cases'],'asymptotic_cases':len(out['lower_axis_asymptotic_controls'])},indent=2))
