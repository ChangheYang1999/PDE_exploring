from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
import numpy as np
from numpy.polynomial.chebyshev import chebder,chebval2d
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse/code'))
from collocation import NodalDensity
from gpu import GPUField
from split_kernel import SplitKernel
from density import gradient_fd
root=Path(__file__).resolve().parents[1]

def differentiated(d,r,theta):
 k=d.k;lb=np.log1p((r/d.L)**2);t=np.exp(-.5*(1-k)*lb);q=-np.expm1(-.5*(1-k)*lb);s=d.map_inverse(np.asarray(theta));cs=np.cos(2*s);z=2*q-1
 b=chebval2d(z,cs,d.co);bq=2*chebval2d(z,cs,chebder(d.co,axis=0));bth=chebval2d(z,cs,chebder(d.co,axis=1))*(-2*np.sin(2*s)/(1+d.beta*np.cos(2*s)))
 co=np.cos(theta);si=np.sin(theta);angular=co*co*si;angularp=co**3-2*co*si*si;radial=r**3*np.exp(.5*(k-3)*lb);eps=1/(1+(r/d.L)**2);v=1-eps
 rho=radial*angular*b;radgrad=radial*angular*((k+(3-k)*eps)*b+(1-k)*t*v*bq)/r;thgrad=radial*(angularp*b+angular*bth)/r
 grad=np.array([co*radgrad-si*thgrad,si*radgrad+co*thgrad]);euler=d.cl*(3-k)*eps*rho+d.cl*radial*angular*bq*(1-k)*t*v
 return float(rho),grad,float(euler)

def interpolate(values,theta):
 n=len(values);freq=np.fft.fftfreq(n,d=1/n);return float(np.real(np.exp(1j*theta*freq)@(np.fft.fft(values)/n)))
def main():
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--tags',default='manufactured,dnSB,dnR8');p.add_argument('--radii',default='1e4,1e6,1e8,1e10');p.add_argument('--nang',type=int,default=2048);p.add_argument('--order',type=int,default=24);p.add_argument('--panel',type=float,default=.12);p.add_argument('--output',default='asymptotic.json');args=p.parse_args()
 summary=json.loads((root/'verification/summary.json').read_text());wanted=set(args.tags.split(','));out={'date_start':datetime.now(timezone.utc).isoformat(),'configuration':{'nang':args.nang,'order':args.order,'panel':args.panel,'rmax':1e30},'rows':[]}
 for item in summary['rows']:
  if item['tag'] not in wanted:continue
  d=NodalDensity(item['source']);assert d.md5==item['source_md5'];ker=SplitKernel(GPUField(d),args.nang,args.order,args.panel,rmax=1e30);angular=np.load(root/'verification'/(item['tag']+'_angular.npz'))
  for r in map(float,args.radii.split(',')):
   for theta in [.3,1.,1.55]:
    start=time.monotonic();x=r*np.cos(theta);y=r*np.sin(theta);U=ker.velocity((x,y));rho,g,euler=differentiated(d,r,theta);R=euler+U@g;direct=(d.cl*np.array([x,y])+U)@g-rho;scaled=R*r**(1-2*d.k);target=interpolate(angular['D'],theta);grfd=gradient_fd(d,x,y,relative_step=.0005)
    nf=abs(rho)+np.sum(abs((d.cl*np.array([x,y])+U)*g));rec={'tag':item['tag'],'source_md5':d.md5,'radius':r,'theta':theta,'U':U.tolist(),'rho':rho,'gradient':g.tolist(),'R_stable':float(R),'R_direct_subtraction':float(direct),'R_report_Nf':float(abs(R)/nf),'scaled_R':float(scaled),'target_D':target,'scaled_error':float(scaled-target),'gradient_relative_difference_FD':float(np.linalg.norm(g-grfd)/max(np.linalg.norm(g),1e-300)),'seconds':time.monotonic()-start}
    out['rows'].append(rec);out['date_last']=datetime.now(timezone.utc).isoformat();(root/'verification'/args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
