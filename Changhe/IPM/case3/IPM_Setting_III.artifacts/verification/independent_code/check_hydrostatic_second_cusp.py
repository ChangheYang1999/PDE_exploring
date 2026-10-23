"""Result198: independent symbolic finite parts and complete-tail cusp quotients."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as sp
import mpmath as mp
import json,hashlib,time
V=Path('research/hydrostatic_second_cusp/verification');t0=time.monotonic();checks=[]
def ck(n,v,z=None):
 checks.append(dict(name=n,passed=bool(v),detail=z))
 if not v:raise AssertionError((n,z))
def zero(n,v):ck(n,sp.factor(v)==0,str(sp.factor(v)))
p,d,s=sp.symbols('p d s',real=True);B=p*(p+2);D=(1-p)/p;A=1/((p+2)**2*D)
zero('degree and denominator',(3*p-2)/p-1+2*D)
zero('finite part integration by parts',d*(d-1)+4*(d-1)+6-(d+1)*(d+2))
zero('I0 derivative identity',1+d*s*s-d*(1+s*s)-(1-d))
zero('I1 derivative identity',1+(d+2)*s*s-(1+s*s)-(d+1)*s*s)
zero('I2 derivative identity',1+(d-2)*s*s-(1+s*s)-(d-3)*s*s)
zero('finite part leading subtraction',( (d+1)/2-1/d)/(d+2)-(d-1)/(2*d))
zero('h two-basis polynomial decomposition',3+2*B*s*s+B*s**4-(B*(1+s*s)**2+3-B))
zero('positive beta gap',3-B-(1-p)*(p+3))
coef=-A*(B*(1-d*d)/d+(3-B)*(d+1)*(d+2)/(3-d))
want=-3*p*p*(4*p*p+5*p-1)/((p+2)**2*(2*p-1)*(2-p))
zero('closed coefficient simplification',coef.subs(d,2*p-1)-want)
# Derive the curvature polynomials of s*(1+s^2)^a directly.
a=sp.symbols('a',real=True)
P=d*(d-1)*(1+s*s)**2-2*(d-1)*(1+s*s)*(1+(1+2*a)*s*s)+2*a*s*s*(3+(1+2*a)*s*s)
zero('B0 curvature polynomial',P.subs(a,(d-1)/2)-(d-1)*(s*s+d-2))
zero('B2 curvature polynomial',P.subs(a,(d-5)/2)-((d-1)*(d-2)+3*(3*d-7)*s*s+12*s**4))
# Both expected curvature polynomials use the common radial power from the direct derivative.
records=[]
for tag in ['3/5','3/4','9/10']:
 full=[]
 for digits in [45,65]:
  with mp.workdps(digits):
   pp=mp.mpf(tag.split('/')[0])/int(tag.split('/')[1]);dd=2*pp-1;bb=pp*(pp+2);aa=pp/((pp+2)**2*(1-pp));QQ=-aa*bb*(dd-1)
   def q0(t):return (dd-1)*t*(1+t*t)**((dd-5)/2)*(t*t+dd-2)
   def q2(t):return t*(1+t*t)**((dd-9)/2)*((dd-1)*(dd-2)+3*(3*dd-7)*t*t+12*t**4)
   def tail0(u):
    if not u:return mp.mpf(0)
    z=u*u;e=mp.expm1((dd-5)/2*mp.log1p(z))*(1+(dd-2)*z)+(dd-2)*z
    return (dd-1)*u**(-dd-1)*e
   def tail2(u):
    if not u:return mp.mpf(0)
    return u**(1-dd)*(1+u*u)**((dd-9)/2)*(12+3*(3*dd-7)*u*u+(dd-1)*(dd-2)*u**4)
   cp0=mp.quad(lambda t:t*q0(t),[0,1])-(dd-1)/dd+mp.quad(tail0,[0,mp.mpf('.5'),1])
   cp2=mp.quad(lambda t:t*q2(t),[0,1])+mp.quad(tail2,[0,mp.mpf('.5'),1])
   J=mp.quad(lambda t:(1+t*t)**((dd-3)/2),[0,1,mp.inf])
   cp=-aa*(bb*cp0+(3-bb)*cp2)
   formula=-aa*J*(bb*(1-dd*dd)/dd+(3-bb)*(dd+1)*(dd+2)/(3-dd))
   ck(f'B0 positive finitepart p{tag} dps{digits}',cp0>0 and abs(cp0-(1-dd*dd)*J/dd)<mp.mpf(10)**(-digits+12),mp.nstr(cp0,20))
   ck(f'B2 positive finitepart p{tag} dps{digits}',cp2>0 and abs(cp2-(dd+1)*(dd+2)*J/(3-dd))<mp.mpf(10)**(-digits+12),mp.nstr(cp2,20))
   ck(f'h negative finitepart p{tag} dps{digits}',cp<0 and abs(cp-formula)<mp.mpf(10)**(-digits+11),dict(Cd=mp.nstr(cp,30),difference=mp.nstr(cp-formula,12)))
   row=dict(digits=digits,Cd=mp.nstr(cp,digits),formula=mp.nstr(formula,digits),J=mp.nstr(J,digits))
   if digits==65:
    def qh(t):return -aa*(bb*q0(t)+(3-bb)*q2(t))
    samples=[]
    for xs in ['1e-2','1e-4','1e-6']:
     xx=mp.mpf(xs)
     def fxx(t):return xx**(dd-2)*qh(t/xx)
     def tail(u):
      if not u:return mp.mpf(0)
      t=1/u**32
      return fxx(t)*32/u**33
     velocity=mp.quad(lambda t:t*fxx(t),[0,xx,2*xx,10*xx,mp.mpf('.2'),1])+mp.quad(tail,[0,mp.mpf('.5'),1])
     quotient=(velocity-QQ/(dd*(1-dd)))/xx**dd
     error=abs(quotient-formula)
     samples.append(dict(x=xs,velocity=mp.nstr(velocity,40),quotient=mp.nstr(quotient,35),absolute_error=mp.nstr(error,20)))
    ck(f'complete inverse cusp quotient p{tag}',mp.mpf(samples[-1]['absolute_error'])<mp.mpf('1e-5'),samples)
    ck(f'cusp quotient refinement p{tag}',all(mp.mpf(samples[i+1]['absolute_error'])<mp.mpf(samples[i]['absolute_error']) for i in range(2)))
    row['cusp_samples']=samples
   full.append(row)
 with mp.workdps(65):dif=abs(mp.mpf(full[0]['Cd'])-mp.mpf(full[1]['Cd']))
 ck(f'45/65 precision agreement p{tag}',dif<mp.mpf('1e-31'),mp.nstr(dif,15))
 records.append(dict(p=tag,results=full))
result=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-t0,checks=checks,records=records,scope='Conditional second-cusp obstruction for explicit result197 trace and 1/2<p<1 only')
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(V/'MANIFEST.json').write_text(json.dumps({str(z):hashlib.sha256(z.read_bytes()).hexdigest()for z in [Path(__file__),V.parent/'PROOF.md',V/'CHECKS.json']},indent=2)+'\n')
print('PASS',len(checks),'checks;',result['seconds'],'seconds;',result['utc'])
