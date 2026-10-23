"""Result287 independent closed angular and shifted-basis scalar manufactures."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,math
import mpmath as mp
from scalar_mp_hydrostatic_density import ScalarMPDensity
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];rows=[];start=datetime.now(timezone.utc).isoformat()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save(status):
 (V/'MP_EXTENDED_MANUFACTURES.json').write_text(json.dumps(dict(status=status,count=len(checks),started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),checks=checks,rows=rows,proof_sha256=sha(R/'EXTENDED_MP_MANUFACTURE_PROOF.md'),driver_sha256=sha(__file__),module_sha256=sha('independent_code/scalar_mp_hydrostatic_density.py')),indent=2)+'\n')
def explicit_T(j,z):
 if j==0:return mp.mpf(1)
 return mp.mpf(j)/2*sum((-1)**k*mp.mpf(math.factorial(j-k-1))/(math.factorial(k)*math.factorial(j-2*k))*(2*z)**(j-2*k)for k in range(j//2+1))
def bisect(r2,L,P):
 if not r2:return mp.mpf(1)
 lo,hi=mp.mpf(0),mp.mpf(1)
 for _ in range(mp.mp.prec+8):
  w=(lo+hi)/2
  if w+r2/L**2*(2*w)**(2*P)>1:hi=w
  else:lo=w
 return (lo+hi)/2
try:
 with mp.workdps(80):
  pts=[(0.,0.),(0.,.1),(.1,0.),(.2,.3),(-.2,.3),(.2,-.3),(3.,4.)]
  for P in [1.5,2.]:
   for basis in ['cheb','local']:
    model=ScalarMPDensity([[0.],[0.,1.]],1.3,P,basis,[-1.,-.25]);C=2**(2*model.P)/model.L**2;d=mp.mpf(2)if basis=='cheb'else 4/(1-model.tk[1]);nu=2*model.P+1
    for x0,y0 in pts:
     x,y=mp.mpf(x0),mp.mpf(y0);r2=x*x+y*y;w=model.weight(r2);D=1+2*model.P*C*r2*w**(2*model.P-1);wx=-2*C*x*w**(2*model.P)/D;wy=-2*C*y*w**(2*model.P)/D;wxx=-(2*C*w**(2*model.P)+8*model.P*C*x*w**(2*model.P-1)*wx+2*model.P*(2*model.P-1)*C*r2*w**(2*model.P-2)*wx**2)/D;B=y*(x*x-y*y);Bx=2*x*y;By=x*x-3*y*y;Bxx=2*y;F=w**nu*(1-d*w);F1=nu*w**(nu-1)-d*(nu+1)*w**nu;F2=nu*(nu-1)*w**(nu-2)-d*nu*(nu+1)*w**(nu-1);exact=[C*B*F,C*(Bx*F+B*F1*wx),C*(By*F+B*F1*wy),C*(Bxx*F+2*Bx*F1*wx+B*(F2*wx**2+F1*wxx))];got=model.jet(x,y);error=max(abs(a-b)/(1+abs(b))for a,b in zip(got,exact));ck('angular closed jet '+str((P,basis,x0,y0)),error<mp.mpf('1e-60'),mp.nstr(error,18));rows.append(dict(kind='closed angular jet',P=P,basis=basis,x=x0,y=y0,error=mp.nstr(error,25)))
    model=ScalarMPDensity([[.25,-.5,.125,.375],[-.75,.0625,.5],[.3125,-.1875]],1.3,P,basis,[-1.,-.25,.375])
    for x0,y0 in pts:
     x,y=mp.mpf(x0),mp.mpf(y0);w=bisect(x*x+y*y,model.L,model.P);s=1-w;t=1-2*w;theta=mp.atan2(y,x);total=mp.mpf(0)
     for k,row in enumerate(model.coeff):
      z=t if basis=='cheb'else (2*t-1-model.tk[k])/(1-model.tk[k]);total+=s**k*sum(a*explicit_T(j,z)for j,a in enumerate(row))*mp.cos(2*k*theta)
     exact=y*w*total;got=model.density(x,y);error=abs(got-exact)/(1+abs(exact));ck('explicit polynomial value '+str((P,basis,x0,y0)),error<mp.mpf('1e-60'),mp.nstr(error,18));ck('even x '+str((P,basis,x0,y0)),abs(model.density(-x,y)-got)<mp.mpf('1e-60'));ck('odd y '+str((P,basis,x0,y0)),abs(model.density(x,-y)+got)<mp.mpf('1e-60'));rows.append(dict(kind='three-row explicit polynomial',P=P,basis=basis,x=x0,y=y0,error=mp.nstr(error,25)))
 save('PASS');print('PASS',len(checks),datetime.now(timezone.utc).isoformat())
except Exception:
 save('FAIL');(V/'mp_extended_manufacture_traceback.txt').write_text(traceback.format_exc());raise
