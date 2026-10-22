"""Independent manufactured controls for packet181; no numerical-lane code.
Exact algebra is separated from high precision quadrature. These controls do
not replace the analytic Holder proof or claim numerical global suprema.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,math
import sympy as s
import mpmath as mp
started=datetime.now(timezone.utc).isoformat(); tic=time.monotonic()
root=Path('research/181_holder_control_of_inverse_constant/verification');root.mkdir(exist_ok=True)
params={'b':'31/10','L':'3/2','bump_degree':6,'bump_h':['1/4','1/8','1/16'],'spline_delta':['1/8','1/16','1/32','1/64'],'decimal_precision':60,'polynomial_cutoff':'H(t)=10t^3-15t^4+6t^5; C2 only, control of integral splitting, not actual smooth cutoff'}
(root/'manufactured_parameters.json').write_text(json.dumps(params,indent=2)+'\n')
checks=[];num=[];negative=[]
def exact(name,value):
 value=s.simplify(value)
 assert value==0,(name,str(value))
 checks.append({'name':name,'residual':str(value)})
def yes(name,value):
 assert value,name
 checks.append({'name':name,'passed':bool(value)})
def numeric(name,a,b,tol=mp.mpf('1e-45')):
 err=abs(a-b);assert err<tol,(name,mp.nstr(err,12))
 num.append({'name':name,'left':mp.nstr(a,50),'right':mp.nstr(b,50),'absolute_difference':mp.nstr(err,12),'tolerance':mp.nstr(tol,8)})
def neg(name,statement):
 assert statement,name
 negative.append({'name':name,'counterexample_condition':True})
z,r,L,b=s.symbols('z r L b',positive=True)
rz=L*s.sqrt(z**(-2*b)-1)
exact('native radial measure',s.powdenest(rz*z**(b+1)*(-s.diff(rz,z))/(b*L**2*z**(-b))-1,force=True))
A=s.Function('A')(r);B=s.Function('B')(r);q=s.Function('q')(r)
psi=(A/r+r*B)/2
E=-(s.diff(psi,r,2)+s.diff(psi,r)/r-psi/r**2)
E=E.subs({s.diff(A,r,2):2*r*q+r**2*s.diff(q,r),s.diff(B,r,2):-s.diff(q,r),s.diff(A,r):r**2*q,s.diff(B,r):-q})
exact('first cosine Poisson sign',E-q)
xx,yy,ccs=s.symbols('xx yy ccs')
exact('absolute inner velocity horizontal',-s.diff(ccs*xx,yy))
exact('absolute inner velocity vertical',s.diff(ccs*xx,xx)-ccs)
neg('absolute center drift is changed although relative velocity vanishes',s.Rational(31,10)*s.Rational(3,2)**2/2!=0)
for m in range(1,7):
 for alpha in map(s.Rational,['1/7','1/3','3/4','1']):
  val=sum((-1)**k*s.binomial(m-1,k)/(alpha+k+1)for k in range(m))/s.factorial(m-1)
  exact(f'Taylor coefficient m={m},alpha={alpha}',val-1/s.prod(alpha+j for j in range(1,m+1)))
for Bv in map(s.Rational,['21/10','29/10','31/10','39/10','53/10']):
 M=int(s.floor(Bv))-1;G=Bv-s.floor(Bv)
 exact(f'critical exponent {Bv}',Bv-1-M-G)
 for av in [s.Rational(0),G/2,G]:
  exact(f'subcritical scaling {Bv},{av}',Bv-1-M-av-(G-av))
  if av<G:yes(f'positive norm exponent {Bv},{av}',G-av>0)
 neg(f'single annulus not a critical shrinking-norm proof {Bv}',Bv-1-M-G==0)
x=s.symbols('x');nodes=[s.Rational(0),s.Rational(1,3),s.Rational(2,3),s.Rational(1)]
lagrange=[s.prod((x-nodes[j])/(nodes[i]-nodes[j])for j in range(4)if j!=i)for i in range(4)]
def bernstein(poly,n):
 pol=s.Poly(s.expand(poly),x)
 return [s.simplify(sum(pol.nth(j)*s.binomial(k,j)/s.binomial(n,j)for j in range(k+1)))for k in range(n+1)]
expected=[[-s.Rational(11,2),s.Rational(7,2),-1],[9,-s.Rational(27,2),s.Rational(9,2)],[-s.Rational(9,2),s.Rational(27,2),-9],[1,-s.Rational(7,2),s.Rational(11,2)]]
for i,li in enumerate(lagrange):
 for j in range(4):exact(f'Lagrange nodal {i},{j}',li.subs(x,nodes[j])-(i==j))
 for k,v in enumerate(bernstein(s.diff(li,x),2)):exact(f'derivative Bernstein {i},{k}',v-expected[i][k])
colsum=[sum(abs(expected[i][k])for i in range(4))for k in range(3)]
yes('Bernstein column sums 20,34,20',colsum==[20,34,20])
Bpolys=[s.expand(sum((-1)**k*s.binomial(6,k)*(x-k)**5 for k in range(cell+1))/120)for cell in range(7)]
exact('quintic B vanishes beyond6',Bpolys[6])
for k in range(1,7):
 for d in range(5):exact(f'quintic C4 knot{k} d{d}',s.diff(Bpolys[k-1]-Bpolys[k],x,d).subs(x,k))
for d in range(5):exact(f'quintic left zero jet{d}',s.diff(Bpolys[0],x,d).subs(x,0))
exact('quintic mass1',sum(s.integrate(Bpolys[k],(x,k,k+1))for k in range(6))-1)
bounds=[]
for d in range(3):
 coeff=[]
 for k in range(6):coeff+=bernstein(s.diff(Bpolys[k],x,d).subs(x,x+k),5-d)
 bounds.append(max(map(abs,coeff)))
yes('nonzero quintic second derivative',bounds[2]>0)
# A generic quintic attains the wrong order if C2 is mistaken for sufficient continuum control.
gamma=s.Rational(1,10)
neg('quintic norm can remain bounded while J grows',s.Rational(3)-s.Rational(31,10)==-gamma)
neg('threshold denominator cannot be integrated at alpha=gamma',-s.Rational(31,10)+2+gamma==-1)
# All powers tested avoid integers; the formula must not be extrapolated there.
neg('integer b Taylor coefficient has pole',3+1-s.Integer(4)==0)
mp.mp.dps=params['decimal_precision'];bv=mp.mpf(31)/10;lv=mp.mpf(3)/2
phi=lambda w:(w-1)**6*(2-w)**6 if 1<w<2 else mp.mpf('0')
I=mp.quad(lambda w:w**(-bv)*phi(w),[1,mp.mpf('1.5'),2])
for htext in params['bump_h']:
 hn,hd=map(int,htext.split('/'));h=mp.mpf(hn)/hd
 P=lambda zz:h**(bv-1)*phi(zz/h)/I
 J=mp.quad(lambda zz:zz**(-bv)*P(zz),[h,mp.mpf('1.5')*h,2*h])
 numeric(f'annular J=1 h={htext}',J,mp.mpf(1))
 radius=lambda zz:lv*mp.sqrt(zz**(-2*bv)-1)
 # Independent quadrature in physical log radius, using q(r), not change-of-variable weights.
 lo=mp.log(radius(2*h));hi=mp.log(radius(h));mid=mp.log(radius(mp.mpf('1.5')*h))
 def radial_integrand(t):
  rr=mp.exp(t);zz=(lv**2/(lv**2+rr**2))**(1/(2*bv))
  return rr**2*zz**(bv+1)*P(zz)
 radial=mp.quad(radial_integrand,[lo,mid,hi])
 numeric(f'physical log radius moment h={htext}',radial,bv*lv**2)
 numeric(f'outer relative constant h={htext}',-radial/2,-bv*lv**2/2)
 numeric(f'absolute center velocity change h={htext}',radial/2,bv*lv**2/2)
 num.append({'name':f'inner radius h={htext}','radius':mp.nstr(radius(2*h),30)})
# Integral splitting with an explicit C2 cutoff. This checks the identity only.
H=lambda t:10*t**3-15*t**4+6*t**5
chi=lambda w:mp.mpf(0)if w<=1 else mp.mpf(1)if w>=2 else H(w-1)
eta=lambda w:mp.mpf(1)if w<=mp.mpf('.5')else mp.mpf(0)if w>=mp.mpf('.75')else 1-H(4*w-2)
cc=-mp.log(4)+mp.quad(lambda w:chi(w)/w,[1,2])+mp.quad(lambda w:eta(w)/w,[mp.mpf('.5'),mp.mpf('.75')])
for power in [6,10,18,30]:
 h=mp.mpf(2)**(-power);delta=mp.sqrt(h)
 points=[h,2*h,delta/2,3*delta/4]
 integral=mp.quad(lambda zz:chi(zz/h)*eta(zz/delta)/zz,points)
 numeric(f'critical logarithm h=2^-{power}',integral,mp.log(delta/h)+cc)
 for ratio in [mp.mpf('.7'),mp.mpf('1.3'),mp.mpf('2.1')]:
  zz=h*ratio;p=bv-1
  lhs=zz**p*chi(zz/h)*eta(zz/delta)
  rhs=delta**p*(zz/delta)**p*eta(zz/delta)-h**p*(zz/h)**p*(1-chi(zz/h))
  numeric(f'critical scale identity h=2^-{power},r={ratio}',lhs,rhs)
# Independent piecewise quintic integration in z versus its scaling formula.
bfunc=[s.lambdify(x,poly,'mpmath')for poly in Bpolys[:6]]
cb=sum(mp.quad(lambda w,k=k:w**(-bv)*bfunc[k](w-1),[k+1,k+2])for k in range(6))
spline_rows=[]
for dtext in params['spline_delta']:
 dn,dd=map(int,dtext.split('/'));delta=mp.mpf(dn)/dd
 val=sum(mp.quad(lambda zz,k=k:zz**(-bv)*delta**2*bfunc[k](zz/delta-1),[(k+1)*delta,(k+2)*delta])for k in range(6))
 numeric(f'quintic sharp cell scaling delta={dtext}',val,cb*delta**(3-bv))
 norm=sum(mp.mpf(str(bounds[j]))*delta**(2-j)for j in range(3))
 spline_rows.append({'delta':dtext,'J':mp.nstr(val,30),'C2_norm_upper_bound':mp.nstr(norm,30)})
# Explicit uniform bound and a nontrivial polynomial test at several first-cell sizes.
Ppoly=1-2*x+3*x**2-4*x**3+5*x**4-6*x**5
Pcoeff=s.Poly(Ppoly,x)
Pjet=[abs(Pcoeff.nth(j)) for j in range(3)]
Mp=max(abs(v)for v in bernstein(s.diff(Ppoly,x,2),3))
exactJ=sum(Pcoeff.nth(j)/(s.Rational(j+1)-s.Rational(31,10))for j in range(6))
for dd in [1,3,12,100]:
 delta=mp.mpf(1)/dd;g=bv-3
 jets=sum(mp.mpf(str(Pjet[j]))/abs(j+1-bv)for j in range(3))
 bound=jets+mp.mpf(str(Mp))*(17*delta**(-g)/(3*(1-g))+(delta**(-g)-1)/g)
 yes(f'finite-cell bound manufactured quintic delta=1/{dd}',abs(mp.mpf(str(exactJ.p))/int(exactJ.q))<=bound)
end=datetime.now(timezone.utc).isoformat()
result={'started_utc':started,'ended_utc':end,'elapsed_seconds':time.monotonic()-tic,'verdict':'PASS','exact_checks':checks,'numeric_checks':num,'negative_controls':negative,'counts':{'exact':len(checks),'numerical':len([r for r in num if 'absolute_difference'in r]),'negative':len(negative)},'quintic_derivative_bounds':[str(v)for v in bounds],'quintic_rows':spline_rows,'critical_cutoff_constant':mp.nstr(cc,40),'scope':'Exact algebra plus high precision manufactured integrals; not certified error bounds for candidate data. C2 polynomial cutoff only checks splitting, not the smoothness theorem.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['started_utc','ended_utc','elapsed_seconds','verdict','counts','quintic_derivative_bounds']},indent=2))
