"""P240: literal Gaussian source, adaptive log characteristics, independent fits.
No imports or execution from the numerics lane. Single-threaded CPU only.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,math,os,time,resource
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import BSpline
from scipy.special import roots_legendre
from signed_gaussian_feedback import SignedGaussianFlow,cases
ROOT=Path('research/240_temperature_alias_transport/verification')
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')

def log_back(g,point,rin=1e-4,rtol=2e-10,dense=False):
 x,y=map(float,point)
 if x<=0:raise ValueError('Positive x only for log coordinates')
 def rhs(t,z):
  if hasattr(g,'manufactured_log_rhs'):return g.manufactured_log_rhs(t,z)
  ell,y=z;xx=math.exp(ell);vv=g.beta;wy=g.beta*y-g.u0
  for l in g.lobes:
   Y=y-l['h'];B,bp,_=l['radial'].B(xx*xx+Y*Y);f=l['fac']
   vv-=2*f*Y*bp;wy+=f*(B+2*xx*xx*bp)
  return [-vv,-wy]
 def event(t,z):return math.hypot(math.exp(z[0]),z[1])-rin
 event.terminal=True;event.direction=-1
 if math.hypot(x,y)<=rin:return {'status':'LOCAL_JET','F':1+g.f01*y,'T':0.,'endpoint':[x,y],'nfev':0},None
 back=solve_ivp(rhs,(0,220),[math.log(x),y],method='DOP853',rtol=rtol,atol=[rtol*.001,max(1e-15,rin*rtol*.01)],events=event,dense_output=dense)
 if not back.success or len(back.t_events[0])!=1:return {'status':'UNFINISHED','T':float(back.t[-1]),'last':back.y[:,-1].tolist(),'nfev':back.nfev},back
 ell,ye=back.y[:,-1];T=float(back.t[-1]);F=math.exp(2*ell+(g.beta-2)*T-2*math.log(x))*(1+g.f01*ye)
 return {'status':'COMPLETE','F':F,'T':T,'endpoint':[math.exp(ell),float(ye)],'nfev':back.nfev},back

class TemperatureFit:
 def __init__(self,knots,coeff,beta_basis=3.,L=1.5):
  self.knots=np.asarray(knots);self.coeff=np.asarray(coeff);self.K=len(coeff);self.beta_basis=beta_basis;self.L=L;self.spline=BSpline(knots,self.coeff.T,5,extrapolate=False);self.dspl=self.spline.derivative();self.k=np.arange(self.K)
 def values(self,points):
  points=np.asarray(points,dtype=float);scalar=points.ndim==1;points=np.atleast_2d(points)
  x,y=points.T;r=np.hypot(x,y);phi=np.arctan2(x,-y);lt=-np.log1p(r/self.L)/self.beta_basis;t=-np.expm1(lt);z=np.exp(lt);D=np.exp((self.beta_basis+2)*lt)
  S=self.spline(t);St=self.dspl(t);C=np.cos(phi[:,None]*self.k);Sn=np.sin(phi[:,None]*self.k)
  F=D*np.sum(S*C,axis=1);Fr=D*np.sum((St-(self.beta_basis+2)*S/z[:,None])*C,axis=1)*z/(self.beta_basis*(r+self.L));Fp=-D*np.sum(self.k*S*Sn,axis=1)
  sx=x/r;cp=-y/r;theta=x*x*F;tx_over_x=2*F+r*sx*sx*Fr+sx*cp*Fp;ty=x*x*(-cp*Fr+sx*Fp/r)
  result=np.column_stack((theta,x*tx_over_x,ty,F,tx_over_x))
  return result[0] if scalar else result

def geometry(Nt=40,ng=7,grade=1.5,Nphi=36,L=1.5,bb=3.):
 edges=np.linspace(0,1,Nt+1)**grade;knots=np.r_[np.zeros(5),edges,np.ones(5)];q,w=roots_legendre(ng)
 t=((edges[1:,None]+edges[:-1,None])/2+(edges[1:,None]-edges[:-1,None])*q/2).ravel();r=L*np.expm1(-bb*np.log1p(-t));phi=(np.arange(Nphi)+.5)*np.pi/Nphi
 return knots,t,r,phi

def fit_temperature(knots,t,F,phi,K,bb=3.,L=1.5):
 N=len(phi);Nb=len(knots)-6;B=BSpline(knots,np.eye(Nb),5,extrapolate=False)(t);coef=np.zeros((K,Nb));D=(1-t)**(bb+2)
 target=F/D[:,None];maxlow=min(K,N)
 modevals=2/N*target@np.cos(np.outer(phi,np.arange(maxlow)));modevals[:,0]*=.5
 diagnostics=[]
 for k in range(maxlow):
  m=min(k,2);cc,res,rank,ss=np.linalg.lstsq(B[:,m:],modevals[:,k],rcond=1e-12);coef[k,m:]=cc
  diagnostics.append({'mode':k,'rank':int(rank),'smallest_singular':float(ss[-1]),'max_radial_error':float(np.max(abs(B[:,m:]@cc-modevals[:,k])))})
 if K>N:
  if not (K==16 and N==12):raise ValueError('Only proved 12/16 alias splitting is implemented')
  for lo,hi in [(9,15),(10,14),(11,13)]:coef[hi]=-.5*coef[lo];coef[lo]*=.5
 fit=TemperatureFit(knots,coef,bb,L)
 pts=np.stack(np.broadcast_arrays(r_of_t(t,bb,L)[:,None]*np.sin(phi),-r_of_t(t,bb,L)[:,None]*np.cos(phi)),axis=-1).reshape(-1,2)
 represented=fit.values(pts)[:,3].reshape(F.shape)
 return fit,{'K':K,'Nphi':N,'max_weighted_value_error':float(np.max(abs((represented-F)/D[:,None]))),'coefficient_norm':float(np.linalg.norm(coef)),'radial':diagnostics}

def r_of_t(t,bb,L):return L*np.expm1(-bb*np.log1p(-t))

def forcing_transport(g,point,fit,rin=1e-4,rtol=2e-10):
 dat,back=log_back(g,point,rin,rtol,True)
 if dat['status']!='COMPLETE':return dat
 T=dat['T'];ye=dat['endpoint'][1]
 def rhs(t,v):
  ell,y=back.sol(T-t);x=math.exp(ell);W=g.field([x,y])[1];P=fit.values([x,y])[4]
  return [-(1+W[0]/x)*v[0]+P]
 out=solve_ivp(rhs,(0,T),[g.b0+g.g01*ye],method='DOP853',rtol=rtol,atol=rtol*.001)
 return {'status':'COMPLETE' if out.success else 'FORWARD_FAILED','G':float(out.y[0,-1]),'Omega':float(point[0]*out.y[0,-1]),'T':T,'forward_nfev':out.nfev,'backward_nfev':dat['nfev'],'endpoint':dat['endpoint']}

def residuals(g,fit,points,max_keep=None):
 rows=[]
 for pt,values in zip(points,fit.values(points)):
  th,tx,ty,F,P=values;W=g.field(pt)[1];terms=[W[0]*tx,W[1]*ty,-(g.beta-2)*th];R=math.fsum(terms);N=sum(abs(v)for v in terms)
  rows.append({'point':list(map(float,pt)),'Theta':float(th),'gradient':[float(tx),float(ty)],'RTheta':R,'NTheta':N,'normalized':abs(R)/N if N else (0. if R==0 else None)})
 summary={'count':len(rows),'max_abs_RTheta':max(abs(q['RTheta'])for q in rows),'max_pointwise_normalized':max(q['normalized']for q in rows if q['normalized']is not None),'zero_normalizer_nonzero_residual':sum(q['normalized']is None for q in rows)}
 summary['points']=rows if max_keep is None else sorted(rows,key=lambda q:q['normalized'] if q['normalized']is not None else math.inf,reverse=True)[:max_keep]
 summary['saved_points']='all' if max_keep is None else 'largest pointwise normalized residuals'
 return summary

def controls():
 start=time.monotonic();out={'started_utc':utc(),'checks':[]}
 def ck(n,q,**e):out['checks'].append({'name':n,'pass':bool(q),**e})
 knot,t,r,phi=geometry();nb=len(knot)-6
 ck('nested angular nodes',np.max(abs(phi[1::3]-(np.arange(12)+.5)*np.pi/12))<1e-15)
 cc=np.zeros((16,nb));cc[0,:]=1;cc[3,7:15]=np.linspace(.1,.4,8);cc[9,5:20]=.1
 fit=TemperatureFit(knot,cc)
 for pt in [[.4,.7],[3.,-2.],[6.,5.]]:
  th,tx,ty,*_=fit.values(pt);grad=[];h=2e-5
  for j in range(2):
   e=np.zeros(2);e[j]=h;u=np.array(pt);grad.append((fit.values(u-2*e)[0]-8*fit.values(u-e)[0]+8*fit.values(u+e)[0]-fit.values(u+2*e)[0])/(12*h))
  error=float(np.max(abs(np.array([tx,ty])-grad)));ck('spline gradient '+str(pt),error<1e-9,error=error)
 # Independent synthetic polynomial coefficient minimum-norm fit.
 pts=np.stack(np.broadcast_arrays(r[:,None]*np.sin(phi),-r[:,None]*np.cos(phi)),axis=-1).reshape(-1,2);F=fit.values(pts)[:,3].reshape(len(r),len(phi))
 for K,N,ix in [(16,12,np.arange(1,36,3)),(16,36,np.arange(36))]:
  f,d=fit_temperature(knot,t,F[:,ix],phi[ix],K)
  ck('synthetic fit '+str((K,N)),d['max_weighted_value_error']<1e-10,error=d['max_weighted_value_error'])
  if N==12:
   ck('synthetic aliased half coefficient',np.max(abs(f.coeff[9]-.5*cc[9]))<1e-10)
   ck('synthetic opposite alias coefficient',np.max(abs(f.coeff[15]+.5*cc[9]))<1e-10)
 # Cartesian and log-coordinate temperature reconstructions are independent state coordinates.
 for key,entry in cases().items():
  c=entry['data']
  if c['G_min']>=0 or c['unfinished']:continue
  rr,y=c['G_min_at'];pt=[math.sqrt(rr*rr-y*y),y];g=SignedGaussianFlow(c['c_in'],c['lobes'])
  for rin in [3e-4,1e-4]:
   a,_=log_back(g,pt,rin=rin,rtol=2e-11);b=g.evaluate(pt,r_in=rin,rtol=2e-11);error=abs(a['F']-b['Theta']/pt[0]**2)/(1+abs(a['F']))
   ck('log Cartesian agreement '+key+' '+str(rin),a['status']=='COMPLETE' and b['status']=='COMPLETE' and error<3e-10,error=error)
 # Linear manufactured transport tests actual forcing integrator with an exact temperature.
 class Linear:
  beta=3.;u0=0.;lobes=[];f01=0.;b0=4/3;g01=0.
  def manufactured_log_rhs(self,t,z):return [-.5,-5.5*z[1]]
  def field(self,p):
   p=np.array(p);W=np.array([.5*p[0],5.5*p[1]]);D=np.diag([.5,5.5]);return W-3*p,W,D-3*np.eye(2),D
 class Quadratic:
  def values(self,p):x,y=p;return np.array([x*x,2*x,0.,1.,2.])
 # Exercise the complete backward path and forcing integrator on exact linear data.
 for pt in [[1.,.3],[3.,-2.],[.01,4.]]:
  q=forcing_transport(Linear(),pt,Quadratic(),rin=1e-4,rtol=2e-11)
  back,_=log_back(Linear(),pt,rin=1e-4,rtol=2e-11)
  ck('manufactured full forcing integrator '+str(pt),q['status']=='COMPLETE' and abs(q['G']-4/3)<1e-10,error=abs(q.get('G',0)-4/3),nfev=q.get('forward_nfev'))
  ck('manufactured log temperature '+str(pt),back['status']=='COMPLETE' and abs(back['F']-1)<1e-10,error=abs(back.get('F',0)-1))
 # A separate constant scalar ODE control checks the quotient sign.
 for T in [1.,5.,20.]:
  sol=solve_ivp(lambda tt,v:[-1.5*v[0]+2],(0,T),[4/3],method='DOP853',rtol=2e-12,atol=2e-14)
  ck('linear divided forcing transport '+str(T),abs(sol.y[0,-1]-4/3)<1e-12)
 out.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-start,passed=sum(x['pass']for x in out['checks']),total=len(out['checks']),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 save(ROOT/'controls.json',out);print(json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2),flush=True)
 if out['passed']!=out['total']:print([q for q in out['checks']if not q['pass']]);raise SystemExit('controls fail')

def run(indices):
 allcases=[(k,v)for k,v in cases().items()if v['data']['G_min']<0 and not v['data']['unfinished']]
 start=time.monotonic();out={'status':'RUNNING','pid':os.getpid(),'started_utc':utc(),'cases':[],'proof_sha256':hashlib.sha256((ROOT.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};save(ROOT/'status.json',out)
 for ci in indices:
  key,e=allcases[ci];c=e['data'];g=SignedGaussianFlow(c['c_in'],c['lobes']);knot,t,r,phi=geometry();shape=(len(r),len(phi));F=np.full(shape,np.nan);times=np.zeros(shape);calls=0;fails=[];filename=ROOT/f'case{ci}_temperatures.npz'
  if filename.exists():
   old=np.load(filename);F=old['F'];times=old['T']
  slog=ROOT/f'case{ci}_paths.jsonl'
  with slog.open('a') as sf:
   for i,rr in enumerate(r):
    for j,ph in enumerate(phi):
     if np.isfinite(F[i,j]):continue
     pt=[float(rr*math.sin(ph)),float(-rr*math.cos(ph))];q,_=log_back(g,pt,rin=1e-4,rtol=2e-10)
     if q['status']in ['COMPLETE','LOCAL_JET']:F[i,j]=q['F'];times[i,j]=q['T']
     else:fails.append({'i':i,'j':j,**q})
     calls+=q['nfev'];sf.write(json.dumps({'i':i,'j':j,**q})+'\n')
    if i%4==0:
     sf.flush();np.savez_compressed(filename,F=F,T=times,t=t,r=r,phi=phi,knots=knot);print('TEMP',ci,i,len(r),'finite',int(np.isfinite(F).sum()),'elapsed',round(time.monotonic()-start,2),'fail',len(fails),utc(),flush=True)
   np.savez_compressed(filename,F=F,T=times,t=t,r=r,phi=phi,knots=knot)
  row={'case':key,'index':ci,'source_A':g.A,'num_source_A':c['A'],'reported_G':c['G_min'],'r_in':1e-4,'rtol':2e-10,'source_approximation':'literal analytic Gaussian; no projected source','unfinished':fails,'temperature_nfev':calls,'fits':[]}
  if not np.isfinite(F).all():row['status']='INCOMPLETE';out['cases'].append(row);save(ROOT/'status.json',out);continue
  rr,yy=c['G_min_at'];pt=[math.sqrt(rr*rr-yy*yy),yy];row['witness']=pt;row['direct_reference']=g.evaluate(pt,r_in=1e-4,rtol=2e-11);row['direct_G']=row['direct_reference']['Omega']/pt[0]
  samplepoints=[pt]+[[float(rrr*math.sin(ph)),float(-rrr*math.cos(ph))]for rrr in [1.,3.,6.,10.,30.]for ph in [.071,.313,.977,1.431,2.119,2.731,3.019]]
  fitgrid=np.stack(np.broadcast_arrays(r[:,None]*np.sin(phi[1::3]),-r[:,None]*np.cos(phi[1::3])),axis=-1).reshape(-1,2)
  for K,N,ix in [(16,12,np.arange(1,36,3)),(12,12,np.arange(1,36,3)),(16,36,np.arange(36)),(24,36,np.arange(36))]:
   f,d=fit_temperature(knot,t,F[:,ix],phi[ix],K);d['transport']=forcing_transport(g,pt,f,rin=1e-4,rtol=2e-10);d['thermal_residuals']=residuals(g,f,samplepoints);d['thermal_residuals_original_grid']=residuals(g,f,fitgrid,max_keep=12);d['witness_values']=f.values(pt).tolist();np.savez_compressed(ROOT/f'case{ci}_K{K}_N{N}_fit.npz',coeff=f.coeff,knots=knot,beta_basis=3.,L=1.5);row['fits'].append(d);print('FIT',ci,K,N,'G',d['transport'].get('G'),'RF',d['max_weighted_value_error'],utc(),flush=True)
  row['status']='COMPLETE';out['cases'].append(row);out['elapsed_so_far']=time.monotonic()-start;save(ROOT/'status.json',out)
 out.update(status='COMPLETE',ended_utc=utc(),elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);save(ROOT/'status.json',out)

if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(10*1024**3,10*1024**3))
 ap=argparse.ArgumentParser();ap.add_argument('--controls',action='store_true');ap.add_argument('--cases',default='');a=ap.parse_args()
 if a.controls:controls()
 if a.cases:run([int(v)for v in a.cases.split(',')])
