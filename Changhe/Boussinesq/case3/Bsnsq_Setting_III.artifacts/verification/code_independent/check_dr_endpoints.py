"""Independent exact-source controls; read a local copy solely to reproduce lead behavior."""
from pathlib import Path
import argparse,json,sys,time,hashlib
from datetime import datetime,timezone
import numpy as np
import mpmath as mp
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root
src=(root/'lead_copy/dr.py').read_text().split('if args.init:')[0]
start=time.monotonic();mp.mp.dps=70
s=mp.mpf(1)/3;results=[]
def exact(n,rv,theta):
 r=mp.mpf(float(rv));th=mp.mpf(float(theta));u=1+r*r
 if n==1:
  I=mp.expm1((1-s)/2*mp.log(u))/(1-s)
  A=mp.expm1((3-s)/2*mp.log(u))/(3-s)-I
  h=(A/r-r*I)/2;dh=(-A/(r*r)-I)/2
  return float(h/r*mp.sin(th)),float(dh*mp.cos(th))
 A=(mp.expm1((2-s/2)*mp.log(u))/(2-s/2)-2*mp.expm1((1-s/2)*mp.log(u))/(1-s/2)+mp.expm1(-s/2*mp.log(u))/(-s/2))/2
 B=u**(-s/2)/s;h=(A/r**2+r*r*B)/4;dh=(-A/r**3+r*B)/2
 return float(-2*h/r*mp.cos(2*th)),float(dh*mp.sin(2*th))
for N in [24,40,64,96,128,192]:
 saved=sys.argv;sys.argv=['dr.py','--Nr',str(N),'--Nth','16','--T','0'];ns={};exec(compile(src,str(root/'lead_copy/dr.py'),'exec'),ns);sys.argv=saved
 r=ns['r'];rho=ns['rho'];xg=ns['xg'];th=ns['th'];R=ns['R'];TH=ns['TH'];X=ns['X'];Y=ns['Y'];L=ns['L']
 # The polynomial is independently reconstructed by discrete cosine orthogonality.
 theta=np.arccos(xg);B=np.cos(np.outer(theta,np.arange(N)))
 def coefficients(q):
  a=2/N*(B.T@q);a[0]/=2;return a
 def strain_rule(coef,ng):
  nodes,weights=np.polynomial.legendre.leggauss(ng);edges=np.r_[0,rho,1];a=edges[:-1,None];b=edges[1:,None];z=(a+b)/2+(b-a)/2*nodes
  p=np.polynomial.chebyshev.chebval(2*z-1,coef)
  return float(.5*np.sum((b-a)/2*weights*p*np.pi/np.sin(np.pi*z)))
 row={'Nr':N,'r_min':float(r[0]),'r_max':float(r[-1]),'modes':[]}
 for n in [1,2]:
  q=r*(1+r*r)**(-2/3) if n==1 else r*r*(1+r*r)**(-7/6)
  Om=q[:,None]*(np.cos(TH) if n==1 else np.sin(2*TH));vr,vt,c=ns['velocity'](Om);coef=coefficients(q)
  rec={'mode':n,'represented_endpoint_0':float(np.polynomial.chebyshev.chebval(-1,coef)),'represented_endpoint_1':float(np.polynomial.chebyshev.chebval(1,coef)), 'lead_strain':float(c),'exact_strain':0. if n==1 else 1.5,'witnesses':[]}
  if n==2:
   rec['own_polynomial_strain_quadratures']={str(ng):strain_rule(coef,ng) for ng in [4,8,16,32,64]}
   rec['strain_error']=abs(c-1.5)
  indices=np.unique([np.argmin(abs(np.log(r/t))) for t in [.01,.1,1,3,10,100,1000,10000]])
  for i in indices:
   k=1;vref,tref=exact(n,r[i],th[k]);ev=abs(vr[i,k]-vref);et=abs(vt[i,k]-tref)
   rec['witnesses'].append({'r':float(r[i]),'theta':float(th[k]),'Vr':float(vr[i,k]),'Vr_exact':vref,'Vtheta':float(vt[i,k]),'Vtheta_exact':tref,'absolute_error':max(ev,et),'relative_error':max(ev,et)/max(abs(vref),abs(tref))})
  rec['max_witness_relative_error']=max(x['relative_error'] for x in rec['witnesses']);row['modes'].append(rec)
 qg=r*r*np.exp(-r*r);gcoef=coefficients(qg);cg=ns['velocity'](qg[:,None]*np.sin(2*TH))[2]
 row['gaussian_control']={'lead_strain':float(cg),'exact_strain':.25,'endpoint_0':float(np.polynomial.chebyshev.chebval(-1,gcoef)),'endpoint_1':float(np.polynomial.chebyshev.chebval(1,gcoef))}
 results.append(row)
 print('N',N,'c2',row['modes'][1]['lead_strain'],'endpoint',row['modes'][1]['represented_endpoint_1'],'m1rel',row['modes'][0]['max_witness_relative_error'],'m2rel',row['modes'][1]['max_witness_relative_error'],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'source_sha256':hashlib.sha256((root/'lead_copy/dr.py').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'s':'1/3','rows':results,'verdict':'slow-tail inverse errors measured; literal unweighted polynomial extension generally inadmissible; no PDE candidate verdict from these controls alone'}
(root/'endpoint_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
