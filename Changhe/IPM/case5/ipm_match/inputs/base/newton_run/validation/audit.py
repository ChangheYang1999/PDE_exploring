"""Off-grid strong physical PDE residuals. Never use the projected ODE to evaluate the test residual.
For nodal core files only, RHS at the *interpolation nodes* defines their Hermite field.
We differentiate that field (psi twice) at independent radii and reconstruct angular products pointwise.
"""
from pathlib import Path
import sys, json, argparse
import numpy as np
from scipy.interpolate import PPoly,CubicHermiteSpline
from threadpoolctl import threadpool_limits
_limit=threadpool_limits(1)
root=Path(__file__).resolve().parents[1]
def reconstruct_slopes(y,c,n):
 f,g,p=np.split(y,3,axis=1); nq=6*n+12;theta=(np.arange(nq)+.5)*np.pi/(2*nq)
 l=2*np.arange(n)+1;k=2*np.arange(1,n+1);so=np.sin(np.outer(theta,l));co=np.cos(np.outer(theta,l))*l;se=np.sin(np.outer(theta,k));ce=np.cos(np.outer(theta,k))*k
 fg=f@so.T; fd=f@co.T; gth=g@ce.T; u=(2*g+p)@se.T
 mass=c*np.eye(n)[None,:,:]-np.einsum('ai,ba,aj->bij',so,gth,so,optimize=True)*(2/nq)
 vf=np.linalg.solve(mass,((f-(u*fd)@so*(2/nq))[...,None]))[...,0]
 po_src=((vf@so.T)*np.cos(theta)-fd*np.sin(theta))@se*(2/nq)
 return np.concatenate([vf-f,p,-4*p+(k*k-4)*g-po_src],axis=1)
def sample(z,num=3):
 # noncollocation points, plus mesh endpoints. Staggered radii for refinement.
 rr=np.array([.1571,.4142,.7887]) if num==3 else (np.arange(num)+.3183)/num
 return np.unique(np.r_[z,(z[:-1,None]+np.diff(z)[:,None]*rr).ravel()])
def eval_side(z,fun,nf,ng,exponent,c,outer,nang,ns,kind='linear'):
 # fun returns f, f_t, g, g_t, g_tt, and optional radial velocity field U and U_t, with physical t=log r.
 k=2*np.arange(1,ng+1); l=2*np.arange(nf)+1
 N=max(128,nang,8*(nf+ng)+16); N=4*int(np.ceil(N/4));th=2*np.pi*(np.arange(N)+0.2718)/N
 so=np.sin(np.outer(l,th)); co=l[:,None]*np.cos(np.outer(l,th)); se=np.sin(np.outer(k,th));ce=k[:,None]*np.cos(np.outer(k,th)); see=-(k*k)[:,None]*se
 gamma=1/c; beta=gamma if outer else 1.; q=1+exponent;samples=sample(z,ns); metrics={};witness={}; hnorm=0
 def upd(name,arr,ts):
  af=np.abs(arr);j=np.unravel_index(af.argmax(),af.shape);val=float(af[j]);
  if val>metrics.get(name,-1):metrics[name]=val;witness[name]=[float(ts[j[0]]),float(th[j[1]])] if len(j)>1 else [float(ts[j[0]])]
 for start in range(0,len(samples),64):
  t=samples[start:start+64]; f,ft,g,gt,gtt,U,Ut=fun(t); zfac=np.exp((exponent-1)*t)[:,None]; tr_scale=np.exp((exponent-beta)*t)[:,None]
  rho=f@so;rt=ft@so;rhoth=f@co;gth=g@ce;vel=(q*g+gt)@se
  adv_r=(c-zfac*gth)*(exponent*rho+rt);adv_ang=zfac*vel*rhoth
  tr=(adv_r+adv_ang-rho)*tr_scale
  src=np.cos(th)*(exponent*rho+rt)-np.sin(th)*rhoth
  lap=(gtt+2*q*gt+q*q*g)@se + g@see
  pp=(-lap-src)*tr_scale
  upd('transport',tr,t);upd('poisson',pp,t);upd('raw_transport',tr*np.exp(beta*t)[:,None],t); upd('raw_poisson',pp*np.exp((beta-1)*t)[:,None],t)
  for name,rr,cut in [('transport',tr,int(l[-1])),('poisson',pp,int(k[-1]))]:
   fft=np.fft.rfft(rr,axis=1);fft[:,cut+1:]=0;low=np.fft.irfft(fft,n=N,axis=1);upd(name+'_high',rr-low,t);upd(name+'_retained',low,t)
  upd('speed_over_r',zfac*np.sqrt(gth*gth+vel*vel),t);upd('scaled_density',rho*tr_scale,t);upd('relative_transport',np.abs(tr)/(1+tr_scale*(np.abs(adv_r)+np.abs(adv_ang)+np.abs(rho))),t)
  upd('relative_poisson',np.abs(pp)/(1+tr_scale*(np.abs(lap)+np.abs(src))),t)
  if U is not None:
   vel2=U@se;tr2=(adv_r+zfac*vel2*rhoth-rho)*tr_scale;pp2=(-((Ut+q*U)@se+g@see)-src)*tr_scale
   upd('firstorder_transport',tr2,t);upd('firstorder_poisson',pp2,t);upd('velocity_consistency',(vel2-vel)*tr_scale,t)
  hnorm=max(hnorm,float(np.max(np.abs(f[:,-1:])*tr_scale)))
 return dict(**metrics,witness=witness,nrad=len(samples),ntheta=N,density_last=hnorm)
def audit(file,nang=192,ns=3):
 with np.load(file,allow_pickle=False) as D:
  c=float(D['c']);a=float(D['a']);out={};sides=[]
  if 'poly' in D and 'M' in D:
   n=int(D['M']);N=3*n; pp=PPoly.construct_fast(D['poly'],D['x'],axis=1)
   for side,length in enumerate([float(D['Lin']),float(D['T'])]):
    origin=-length if side==0 else 0.; z=origin+length*D['x'];s=1 if not side else 1/c
    def fun(t,idx=side,ln=length,orig=origin):
     x=(t-orig)/ln; y=pp(x).T[:,idx*N:(idx+1)*N];dy=pp(x,1).T[:,idx*N:(idx+1)*N]/ln;ddy=pp(x,2).T[:,idx*N:(idx+1)*N]/ln**2
     return y[:,:n],dy[:,:n],y[:,n:2*n],dy[:,n:2*n],ddy[:,n:2*n],y[:,2*n:],dy[:,2*n:]
    sides.append(eval_side(z,fun,n,n,s,c,bool(side),nang,ns))
   interface=pp(0)[N:]-pp(1)[:N];out['J']=float(interface[2*n]);out['Jhigh']=float(np.max(abs(interface[2*n+1:])));out['dirichlet']=float(np.max(abs(interface[:2*n])))
  else:
   n=int(D['n']);m=int(D['m']);y=D['x'];zz=D['z'] if 'z' in D else np.r_[np.linspace(-float(D['li']),0,m+1),np.linspace(0,float(D['lo']),m+1)]
   isref='ref_format' in D; native=('scaled_x' in D and bool(D.get('scale_ext',False)));slopes=D['xdot'] if 'xdot' in D else (D['ode_slopes'] if 'ode_slopes' in D else reconstruct_slopes(y,c,n))
   if native:y=D['scaled_x'];slopes=D['scaled_xdot']
   for side,idx in enumerate([slice(None,m+1),slice(m+1,None)]):
    z=zz[idx];pp=CubicHermiteSpline(z,y[idx],slopes[idx],axis=0)
    def fun(t):
     yy=pp(t);dy=pp(t,1);ddy=pp(t,2)
     if isref:return yy[:,:n],dy[:,:n],yy[:,n:2*n],dy[:,n:2*n],ddy[:,n:2*n],yy[:,2*n:],dy[:,2*n:]
     return yy[:,:n],dy[:,:n],yy[:,n:2*n],dy[:,n:2*n],ddy[:,n:2*n],(2*yy[:,n:2*n]+yy[:,2*n:]),(2*dy[:,n:2*n]+dy[:,2*n:])
    sides.append(eval_side(z,fun,n,n,(1/c if ((isref or native) and side) else 1.),c,bool(side),nang,ns))
   delta=y[m+1]-y[m];jump=delta[2*n:] if isref else delta[2*n:]+2*delta[n:2*n];out.update(J=float(jump[0]),Jhigh=float(np.max(abs(jump[1:]))),dirichlet=float(np.max(abs(delta[:2*n]))))
  out.update(c=c,a=a,inner=sides[0],outer=sides[1],file=str(file));return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('files',nargs='+');p.add_argument('--out',required=True);p.add_argument('--nang',type=int,default=192);p.add_argument('--ns',type=int,default=3);arg=p.parse_args();o=open(arg.out,'w');
 for f in arg.files:
  try:d=audit(f,arg.nang,arg.ns)
  except Exception as err:d={'file':f,'error':repr(err)}
  o.write(json.dumps(d)+'\n');o.flush()
