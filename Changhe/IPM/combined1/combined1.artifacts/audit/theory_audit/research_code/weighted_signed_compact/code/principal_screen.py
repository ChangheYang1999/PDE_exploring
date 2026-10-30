"""FLOAT principal-symbol screening with exact rational radial polynomials."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import numpy as np
import json,time,sys,hashlib
from flint import arb,fmpq as Q,fmpq_poly as P,ctx
ctx.prec=384;sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1];src=ROOT/'source/state131.json';T=P([0,1]);U=P([1,-1]);Z=P([])
def q(x):
 f=Fraction(str(x));return Q(f.numerator,f.denominator)
def ar(x):return arb(x.numerator)/x.denominator
def add(d,j,n,V):
 if n==0 or not V:return
 if n<0:n,V=-n,-V
 d[j,n]=d.get((j,n),Z)+V
 if not d[j,n]:del d[j,n]
def rad(V,p):return 2*p*T*V+2*T*U*V.derivative()
def td(V,a,k=1):return (k-2*a*T)*V+2*T*U*V.derivative()
def divide(V):
 assert V[0]==0 and V[1]==0
 return P(list(V)[2:])
start=time.monotonic();d=json.loads(src.read_text());c=q(d['cl']);delta=1-1/c;pot={}
for (j,m,k),x in zip(d['order'],d['coefficients']):pot[j,2*m]=pot.get((j,2*m),Z)+q(x)*T**k
rho={};stream={}
for (j,n),V in pot.items():
 p=(3+1/c-j*delta)/2;B=rad(rad(V,p),p)-n*n*V;E=rad(B,p)-2*B
 add(rho,j,n-1,(E+n*B)/2);add(rho,j,n+1,-(E-n*B)/2)
 plus=rad(V,p)-n*V;plus=rad(plus,p)-(n+2)*plus
 minus=rad(V,p)+n*V;minus=rad(minus,p)+(n-2)*minus
 add(stream,j,n+2,plus/4);add(stream,j,n-2,-minus/4)
rho={key:divide(V) for key,V in rho.items()};stream={key:divide(V) for key,V in stream.items()}
rder={key:td(V,(key[0]+1)*delta/2) for key,V in rho.items()}
radii=np.concatenate(([0.],np.geomspace(1e-5,1e8,320)));angles=np.linspace(0,np.pi/2,257)
maxn=max(n for j,n in list(rho)+list(stream));sins=np.sin(np.arange(maxn+1)[:,None]*angles);coss=np.cos(np.arange(maxn+1)[:,None]*angles)
rr=np.zeros((len(radii),len(angles)));rt=rr.copy();ur=rr.copy()
for i,r in enumerate(radii):
 rq=q(str(r));r2=rq*rq;t=r2/(1+r2);u=1/(1+r2);power={j:ar(u)**ar((j+1)*delta/2) for j,n in pot}
 for (j,n),V in rho.items():
  rr[i]+=float(power[j]*ar(rder[j,n](t)))*sins[n]
  rt[i]+=float(power[j]*ar(V(t)))*n*coss[n]
 for (j,n),V in stream.items():ur[i]-=r*float(power[j]*ar(V(t)))*n*coss[n]
ry=rr*np.sin(angles)+rt*np.cos(angles);theta=(np.sqrt(rr*rr+rt*rt)-ry)/2
rows=[]
for a in [1.105,1.2,1.3,1.4,1.5]:
 for R in [.125,.25,.5,1.,2.,4.,16.]:
  rw=radii[:,None];b=a*(float(c)*rw*rw+rw*ur)/(R*R+rw*rw);lam=b+theta
  i,k=np.unravel_index(np.argmax(lam),lam.shape)
  rows.append({'a':a,'R':R,'sample_maximum':float(lam[i,k]),'far_limit':a*float(c),'sample_margin':float(c)+1-float(lam[i,k]),'r_at_max':float(radii[i]),'theta_at_max':float(angles[k]),'b_at_max':float(b[i,k]),'theta_symbol_at_max':float(theta[i,k])})
  print('a',a,'R',R,'margin',rows[-1]['sample_margin'],'r',radii[i],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'FLOAT screening only, no continuum bound or inverse certificate','method':'exact rational polar construction and Arb384 radial coefficients, floating trigonometric grid','radii_count':len(radii),'angles_count':len(angles),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'c':str(c),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/principal_screen.json').write_text(json.dumps(out,indent=2)+'\n');print('elapsed',out['elapsed_seconds'])
