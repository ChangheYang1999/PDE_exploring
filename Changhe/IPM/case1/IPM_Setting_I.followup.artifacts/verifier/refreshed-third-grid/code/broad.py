"""Own paired inverse on the preselected58physical points for radial-scale trials."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import ceil,isqrt,sqrt
import sys,json,time,hashlib
import numpy as np
from numpy.polynomial.chebyshev import chebval2d,chebder
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
from gpu import GPUField
from split_kernel import SplitKernel
source=Path(sys.argv[1]);d=NodalDensity(source);pp=ROOT.parent/'sampled-physical-actions/verification/points.json';pbytes=pp.read_bytes();j=json.loads(pbytes);pts=j['points'] if isinstance(j,dict) else j;assert len(pts)==58
outpath=ROOT/'verification'/(source.stem+'_broad4096.json')
config={'nang':4096,'order':28,'panel':.08,'rmax':'1e30'}
if outpath.exists():
 out=json.loads(outpath.read_text());assert out['source_md5']==d.md5 and out['points_sha256']==hashlib.sha256(pbytes).hexdigest() and out['config']==config
else:out={'start':datetime.now(timezone.utc).isoformat(),'source_md5':d.md5,'points_sha256':hashlib.sha256(pbytes).hexdigest(),'config':config,'rows':[],'scope':'Finite samples of an unconverged represented field; inverse and derivative discrepancies are not certified error bounds.'}
def save():
 tmp=outpath.with_suffix('.temporary');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(outpath)
if out.get('complete'):print('Already complete',flush=True);sys.exit(0)
x,y=np.array(pts).T;r2=x*x+y*y;D=d.L**2+r2;ell=np.log1p(r2/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell);s=d.map_inverse(np.arctan2(y,x));c=np.cos(2*s)
b=chebval2d(2*q-1,c,d.co);bq=chebval2d(2*q-1,c,2*chebder(d.co,axis=0));bc=chebval2d(2*q-1,c,chebder(d.co,axis=1));dc=-2*np.sin(2*s)/(1+d.beta*np.cos(2*s));pref=x*x*y*np.exp((d.k-3)*ell/2)
analytic=np.stack([pref*((2/x+(d.k-3)*x/D)*b+bq*(1-d.k)*(1-q)*x/D-bc*dc*y/r2),pref*((1/y+(d.k-3)*y/D)*b+bq*(1-d.k)*(1-q)*y/D+bc*dc*x/r2)],axis=1)
H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1);B0=ceil(float(np.max(abs(d.b))));assert d.L==int(d.L) and d.L>=1 and 0<d.k<.2;C=int(d.L)**3*H*B0;out['tail_C']=C
begin=time.monotonic();ker=SplitKernel(GPUField(d),4096,28,.08,rmax=1e30);print('BUILD_DONE',datetime.now(timezone.utc).isoformat(),flush=True)
for i,pt in enumerate(pts):
 if i<len(out['rows']):assert out['rows'][i]['point']==pt;continue
 U=ker.velocity(pt);gs=[gradient_fd(d,*pt,relative_step=h) for h in [1/8000,1/16000,1/32000]];g=gs[-1];rho=float(d(*pt));W=d.cl*np.array(pt)+U;R=float(W@g-rho);nf=float(abs(rho)+sum(abs(W*g)));nv=float(abs(rho)+abs(np.array(pt)@g)+abs(U@g));rmax=ceil(sqrt(sum(t*t for t in pt)))
 while sum(F(t)**2 for t in pt)>rmax*rmax:rmax+=1
 tail=F(5*C*rmax,2*10**24)/(1-F(rmax,10**30)**2)**2
 out['rows'].append({'index':i,'point':pt,'rho':rho,'U':U.tolist(),'gradient':g.tolist(),'analytic_gradient':analytic[i].tolist(),'R':R,'N_report_f':nf,'N_report_v':nv,'absR_report_f':abs(R)/nf,'absR_report_v':abs(R)/nv,'gradient_step_R_changes_fixed_Nf':[float(W@(gg-g)/nf) for gg in gs[:-1]],'chainrule_R_change_fixed_Nf':float(W@(analytic[i]-g)/nf),'exact_U_tail_bound':str(tail),'tail_R_bound_using_numerical_gradient':float(tail)*sum(abs(g))/nf,'date':datetime.now(timezone.utc).isoformat()});save();print('POINT',i+1,'/58','R_Nf',abs(R)/nf,'chainrule',out['rows'][-1]['chainrule_R_change_fixed_Nf'],'seconds',time.monotonic()-begin,flush=True)
out['complete']=True;out['end']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['end'],flush=True)
