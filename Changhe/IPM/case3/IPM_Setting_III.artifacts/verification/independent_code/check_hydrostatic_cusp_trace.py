"""Result197: own polynomial differentiation and independent full-tail quadrature."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import sympy as sp
import mpmath as mp
V=Path('research/hydrostatic_cusp_trace/verification')
t0=time.monotonic();checks=[]
def ck(name,ok,detail=None):
 checks.append(dict(name=name,passed=bool(ok),detail=detail))
 if not ok:raise AssertionError((name,detail))
def zero(name,e):ck(name,sp.factor(e)==0,str(sp.factor(e)))
x,y,p,L,C=sp.symbols('x y p L C', real=True)
r2=x*x+y*y
# Differentiate R^a P using polynomial product rules, with R^2=r2.
def dp(P,a,z,R2=r2):return sp.expand(R2*sp.diff(P,z)+a*z*P)
F=C*y*(3*x*x+(p+2)*y*y);S=-C*x*y
FX=C*(p-1)*x*y*(3*x*x+p*y*y)
FY=C*(3*x**4+6*p*x*x*y*y+p*(p+2)*y**4)
A=C*x*(x*x+p*y*y);B=-C*y*(p*x*x+y*y)
zero('homogeneous density x derivative',dp(F,p-3,x)-FX)
zero('homogeneous density y derivative',dp(F,p-3,y)-FY)
zero('stream y derivative gives V1',dp(S,p-1,y)+A)
zero('stream x derivative gives V2',dp(S,p-1,x)-B)
zero('hydrostatic stream equation',-dp(dp(S,p-1,y),p-3,y)-FX)
zero('velocity divergence',dp(A,p-3,x)+dp(B,p-3,y))
zero('Euler density degree p',x*FX+y*FY-p*r2*F)
XX=C*(p-1)*y*(3*(p-2)*x**4+(p*p-4*p+9)*x*x*y*y+p*y**4)
zero('second derivative polynomial',dp(FX,p-5,x)-XX)
Q=p*(p-1)/(p+2)
zero('axis curvature Q',XX.subs({x:0,y:1,C:1/(p+2)})-Q)
P2=3*x**4+2*p*(p+2)*x*x*y*y+p*(p+2)*y**4
zero('nonlinear transport and formal next term',A*FX+B*FY+C*C*y*r2*P2)
zero('nonresonant next transport degree',(2*p-1)/p-1+(1/p-1))
theta=sp.symbols('theta',real=True)
tr=sp.sin(theta)*(3*sp.cos(theta)**2+(p+2)*sp.sin(theta)**2)/(p+2)
ck('trace derivative',sp.trigsimp(sp.diff(tr,theta)-3*sp.cos(theta)*(sp.cos(theta)**2+p*sp.sin(theta)**2)/(p+2))==0)
zero('vertical trace normalized',tr.subs(theta,sp.pi/2)-1)
zero('vertical trace curvature',sp.diff(tr,theta,2).subs(theta,sp.pi/2)+3*p/(p+2))
eps=(1-p)/(3*(p+3))
ck('two-mode formula',sp.trigsimp(sp.expand_trig(tr-(sp.sin(theta)+eps*sp.sin(3*theta))/(1-eps)))==0)
zero('compact perturbation integration by parts',p*(p-1)+4*(p-1)+6-(p+1)*(p+2))
R2=L*L+r2
Fs=C*y*(3*(L*L+x*x)+(p+2)*y*y)
As=C*x*(L*L+x*x+p*y*y);Bs=-C*y*(L*L+p*x*x+y*y)
FXs=C*(p-1)*x*y*(3*L*L+3*x*x+p*y*y)
FYs=C*(3*(L*L+x*x)**2+6*p*(L*L+x*x)*y*y+p*(p+2)*y**4)
zero('smooth stream V1',dp(S,p-1,y,R2)+As)
zero('smooth stream V2',dp(S,p-1,x,R2)-Bs)
zero('smooth density x derivative',dp(Fs,p-3,x,R2)-FXs)
zero('smooth density y derivative',dp(Fs,p-3,y,R2)-FYs)
zero('smooth hydrostatic law',-dp(dp(S,p-1,y,R2),p-3,y,R2)-FXs)
zero('smooth divergence',dp(As,p-3,x,R2)+dp(Bs,p-3,y,R2))
E=(p+2)/3+(p-3)/2;v3=-(p-1)/6
zero('normalized smooth cubic E',E-5*(p-1)/6)
zero('normalized residual cubic',2*E+v3-3*(p-1)/2)
zero('p3/4 nonzero cubic residual',(2*E+v3).subs(p,sp.Rational(3,4))+sp.Rational(3,8))
records=[]
for ps in ['1/3','2/5','3/4','9/10']:
 pair=[]
 for digits in [45,65]:
  with mp.workdps(digits):
   pp=mp.mpf(ps.split('/')[0])/int(ps.split('/')[1]);cc=1/(pp+2);qq=cc*pp*(pp-1)
   def f(a,b):return cc*b*(a*a+b*b)**((pp-3)/2)*(3*a*a+(pp+2)*b*b)
   def fx(a,b):return cc*(pp-1)*a*b*(a*a+b*b)**((pp-5)/2)*(3*a*a+pp*b*b)
   def fxx(a,b):return cc*(pp-1)*b*(a*a+b*b)**((pp-7)/2)*(3*(pp-2)*a**4+(pp*pp-4*pp+9)*a*a*b*b+pp*b**4)
   def cp_integrand(t):
    if not t:return mp.mpf(0)
    z=t*t;aa=(pp*pp-4*pp+9)/pp;bb=3*(pp-2)/pp
    correction=mp.expm1((pp-7)/2*mp.log1p(z))*(1+aa*z+bb*z*z)+aa*z+bb*z*z
    return qq*t**(-pp-1)*correction
   cp=mp.quad(lambda t:t*fxx(1,t),[0,mp.mpf('.5'),1])-qq/pp+mp.quad(cp_integrand,[0,mp.mpf('.5'),1])
   ck(f'full finite-part integral p{ps} d{digits}',abs(cp)<mp.mpf(10)**(-digits+12),mp.nstr(cp,12))
   vals=[]
   for ax,by in [('0.7','1.3'),('1.2','0.4')]:
    ax=mp.mpf(ax);by=mp.mpf(by);rr=ax*ax+by*by
    known1=cc*ax*rr**((pp-3)/2)*(ax*ax+pp*by*by)
    known2=-cc*by*rr**((pp-3)/2)*(pp*ax*ax+by*by)
    # Integrate the complete tail t=T/u^32; no cutoff or stream primitive.
    T=max(by,2*ax,mp.mpf(1));power=32
    def tail(fun):
     def integrand(u):
      if not u:return mp.mpf(0)
      t=T/u**power
      return fun(ax,t)*power*T/u**(power+1)
     return mp.quad(integrand,[0,mp.mpf('.5'),1])
    iv1=-(mp.quad(lambda t:fx(ax,t),[by,T]) if by<T else 0)-tail(fx)
    iv2=mp.quad(lambda t:t*fxx(ax,t),[0,by])+by*((mp.quad(lambda t:fxx(ax,t),[by,T]) if by<T else 0)+tail(fxx))
    err=max(abs(iv1-known1),abs(iv2-known2))
    ck(f'independent infinite inverse p{ps} d{digits} x{ax} y{by}',err<mp.mpf(10)**(-digits+12),mp.nstr(err,12))
    der=mp.diff(lambda z:f(z,by),ax,2)
    ck(f'automatic precision finite differentiation p{ps} d{digits} x{ax}',abs(der-fxx(ax,by))<mp.mpf(10)**(-digits+12))
    vals.append([mp.nstr(iv1,digits),mp.nstr(iv2,digits)])
   pair.append(dict(digits=digits,Cp=mp.nstr(cp,digits),velocities=vals))
  if digits==65:
   for j in range(2):
    for k in range(2):
     with mp.workdps(65):error=abs(mp.mpf(pair[0]['velocities'][j][k])-mp.mpf(pair[1]['velocities'][j][k]))
     ck(f'd45/d65 inverse pairing p{ps} {j}/{k}',error<mp.mpf('1e-32'),mp.nstr(error,12))
 records.append(dict(p=ps,values=pair))
# An independent compact bump confirms the two integrations by parts.
with mp.workdps(45):
 def chi(s):
  if s<=1 or s>=2:return mp.mpf(0)
  return mp.exp(-1/((s-1)*(2-s)))
 I=mp.quad(lambda s:s*chi(s),[1,mp.mpf('1.5'),2])
 for pp in [mp.mpf(1)/3,mp.mpf(3)/4]:
  actual=mp.quad(lambda s:s*(pp*(pp-1)*chi(s)-2*(pp-1)*s*mp.diff(chi,s)+s*s*mp.diff(chi,s,2)),[1,mp.mpf('1.5'),2])
  want=(pp+1)*(pp+2)*I
  ck(f'compact bump moment p{pp}',abs(actual-want)<mp.mpf('1e-34') and want>0,dict(actual=mp.nstr(actual,35),formula=mp.nstr(want,35)))
result=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-t0,checks=checks,records=records,scope='Trace/inverse identities and non-profile manufactured tests, no existence claim')
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(V/'MANIFEST.json').write_text(json.dumps({str(z):hashlib.sha256(z.read_bytes()).hexdigest() for z in [Path(__file__),V.parent/'PROOF.md',V/'CHECKS.json']},indent=2)+'\n')
print('PASS',len(checks),'checks;',result['seconds'],'seconds;',result['utc'])
