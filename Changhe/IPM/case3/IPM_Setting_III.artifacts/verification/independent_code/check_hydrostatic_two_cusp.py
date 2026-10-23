"""Result199: exact moment algebra and independently integrated smooth transitions."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from scipy.special import roots_legendre
import sympy as sp
V=Path('research/hydrostatic_two_cusp_compatibility/verification');start=time.monotonic();checks=[]
def ck(name,v,detail=None):
 checks.append(dict(name=name,passed=bool(v),detail=detail))
 if not v:raise AssertionError((name,detail))
def zero(name,x):ck(name,sp.factor(x)==0,str(sp.factor(x)))
p,s=sp.symbols('p s',positive=True);d=2*p-1;K=(1-p)*(p+2)/2;b=-p*(1-p)/2
zero('density jump',K+b-(1-p))
zero('exterior density identity',p*(K*s**p+b*s**(p-2))-s*sp.diff(K*s**p+b*s**(p-2),s)-p*(p-1)*s**(p-2))
W=s**p;F=K*s**p+b*s**(p-2)
T=p*sp.diff(W,s)*F-(p+1)*W*sp.diff(F,s)
zero('exterior transport',T-(-p*K*s**d+(p+2)*b*s**(d-2)))
M=-(p+1)*(1-p)+p*K/(2*p+1)-(p+2)*b/(2*p-1)
Mpositive=(1-p)**2*(2*p*p+2*p+1)/(4*p*p-1)
zero('positive finite moment simplification',M-Mpositive)
f,h,w=sp.symbols('F H W');fp=sp.symbols('Fp')
zero('transport simplification',h*(p*f-s*fp)+(s*h-(p+1)*w)*fp-(p*h*f-(p+1)*w*fp))
zero('moment integration by parts',(2*p+1)*s*h*f+(p+1)*w*f-(p+1)*(w*f+s*h*f+s*w*fp)-s*(p*h*f-(p+1)*w*fp))
# Verify the cumulative-integral chart identities without numerical differentiation.
AA,BB,CC,eta=sp.symbols('AA BB CC eta')
WW=s*AA+s**p*BB;FF=K*s**p*CC+b*s**(p-2)*BB
D=lambda expr:sp.diff(expr,s)+sp.diff(expr,AA)*(-s**(p-2)*eta)+sp.diff(expr,BB)*eta/s+sp.diff(expr,CC)*eta/s**3
HH=AA+p*s**(p-1)*BB
zero('smoothed W derivative',D(WW)-HH)
WW2=(p-1)*s**(p-2)*(p*BB+eta)
zero('smoothed W second derivative',D(HH)-WW2)
FF1=p*K*s**(p-1)*CC+(p-2)*b*s**(p-3)*BB+(1-p)*s**(p-3)*eta
zero('smoothed density derivative',D(FF)-FF1)
zero('smoothed hydrostatic curl law',p*FF-s*FF1-WW2)

def bump(z):
 z=np.asarray(z,float);v=np.zeros_like(z);inside=np.abs(z)<1;v[inside]=np.exp(-1/(1-z[inside]**2));return v

def evaluate(P,e,n):
 z,qw=roots_legendre(n);zn,wn=roots_legendre(max(128,n));Z=float(np.dot(wn,bump(zn)))
 # Each cumulative uses its own mapped Gauss interval, separate from the outer quadrature.
 lo=-1+(z[:,None]+1)*(zn[None,:]+1)/2
 lw=(z[:,None]+1)*wn[None,:]/2
 hi=z[:,None]+(1-z[:,None])*(zn[None,:]+1)/2
 hw=(1-z[:,None])*wn[None,:]/2
 B=(bump(lo)*lw).sum(axis=1)/Z
 C=(bump(lo)*np.exp(-2*e*lo)*lw).sum(axis=1)/Z
 A=(bump(hi)*np.exp((P-1)*e*hi)*hw).sum(axis=1)/Z
 S=np.exp(e*z);eta=bump(z)/(e*Z);kp=(1-P)*(P+2)/2;bp=-P*(1-P)/2;deg=2*P-1
 W=S*A+S**P*B;H=A+P*S**(P-1)*B;F=kp*S**P*C+bp*S**(P-2)*B
 F1=P*kp*S**(P-1)*C+(P-2)*bp*S**(P-3)*B+(1-P)*S**(P-3)*eta
 W2=(P-1)*S**(P-2)*(P*B+eta)
 T=P*H*F-(P+1)*W*F1
 tailK=kp*float(np.dot(wn,np.exp(-2*e*zn)*bump(zn)))/Z;end=np.exp(e)
 counter=P*tailK*end**(2*P+1)/(2*P+1)-(P+2)*bp*end**deg/deg
 direct=e*float(np.dot(qw,S*S*T))+counter
 ibp=e*float(np.dot(qw,(2*P+1)*S*S*H*F+(P+1)*S*W*F))-(P+1)*end*end**P*(tailK*end**P+bp*end**(P-2))+counter
 limit=(1-P)**2*(2*P*P+2*P+1)/(4*P*P-1)
 return dict(p=P,epsilon=e,order=n,M_direct=direct,M_ibp=ibp,M_limit=limit,limit_error=direct-limit,coefficient=(2*P)*(2*P+1)*direct/((1-P)/P),curl_error=float(np.max(np.abs(P*F-S*F1-W2))),min_F=float(F.min()),min_F1=float(F1.min()),max_W2=float(W2.max()),min_H=float(H.min()),tail_K=tailK)
records=[]
for P in [.6,.75,.9]:
 for e in [1/8,1/16,1/32,1/64,1/128]:
  pair=[evaluate(P,e,n)for n in [128,256]];a,bv=pair
  ck('moment quadrature refinement',abs(a['M_direct']-bv['M_direct'])<2e-11,pair)
  ck('independent IBP and derivative integrals',abs(bv['M_direct']-bv['M_ibp'])<2e-11,abs(bv['M_direct']-bv['M_ibp']))
  ck('smooth chart curl',bv['curl_error']<2e-12,bv['curl_error'])
  ck('smoothed second coefficient positive',bv['coefficient']>0,bv['coefficient'])
  ck('smoothed weak sign cone',bv['min_F']>=-1e-15 and bv['min_F1']>=-1e-15 and bv['max_W2']<=1e-15 and bv['min_H']>0)
  records.append(bv)
 sub=[r for r in records if r['p']==P]
 ck('positive limiting moment approached',all(abs(a['limit_error'])>abs(b['limit_error'])for a,b in zip(sub,sub[1:])),[r['limit_error']for r in sub])
 ck('last smoothing error below0.001',abs(sub[-1]['limit_error'])<.001,sub[-1]['limit_error'])
# A quadratic polynomial with opposite endpoint signs is not assumed linear.
for cross in [-100.,0.,100.]:
 # Q(t)=negative*(1-t)^2+2cross*t*(1-t)+positive*t^2.
 neg=-1.;pos=2.;co=[neg-2*cross+pos,2*cross-2*neg,neg];roots=np.roots(co)
 ck('IVT root for arbitrary cross coefficient',any(abs(t.imag)<1e-12 and 0<t.real<1 for t in roots),roots.tolist())
out=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',checks=checks,smooth_charts=records,scope='Trace compatibility only; no original or hydrostatic profile')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
(V/'MANIFEST.json').write_text(json.dumps({str(q):hashlib.sha256(q.read_bytes()).hexdigest()for q in[Path(__file__),V.parent/'PROOF.md',*sorted(V.iterdir())]if q.is_file()and q.name!='MANIFEST.json'},indent=2)+'\n')
print('PASS',len(checks),'checks;',out['elapsed_seconds'],'seconds;',out['utc'])
for r in records:print('p',r['p'],'eps',r['epsilon'],'M',r['M_direct'],'limit',r['M_limit'],'Cd_h',r['coefficient'])
