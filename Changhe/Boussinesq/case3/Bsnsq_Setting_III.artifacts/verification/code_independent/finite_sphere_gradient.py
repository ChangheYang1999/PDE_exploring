"""P247: exact finite-sphere compatibility correction and numerical diagnostics.
Own literal Gaussian inverse; no imports or execution from the numerical lane.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,math,os,resource,time
import numpy as np
from scipy.integrate import solve_ivp
from signed_gaussian_feedback import SignedGaussianFlow,cases
from temperature_alias_transport import log_back
ROOT=Path('research/247_finite_sphere_gradient/verification')
utc=lambda:datetime.now(timezone.utc).isoformat()
def save(name,d):(ROOT/name).write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def boundary(g,Q):
 x,y=map(float,Q)
 if hasattr(g,'boundary_data'):h,dh=g.boundary_data(Q)
 else:h=x*x*(1+g.f01*y);dh=np.array([2*x*(1+g.f01*y),x*x*g.f01])
 W=g.field(Q)[1];den=float(W@Q)
 if not math.isfinite(den) or den==0:raise ValueError('Nontransverse or invalid circle intersection')
 defect=(g.beta-2)*h-float(W@dh);correction=np.asarray(Q)*defect/den;grad=dh+correction
 return {'h':h,'raw_gradient':dh.tolist(),'corrected_gradient':grad.tolist(),'correction':correction.tolist(),'transversality':den,'relative_transversality':den/float(np.dot(Q,Q)),'raw_thermal_defect':defect,'corrected_thermal_defect':float(W@grad)-(g.beta-2)*h,'tangential_change':float(np.dot(correction,[-y,x]))}
def transport(g,point,rin=1e-4,rtol=2e-12):
 d,back=log_back(g,point,rin,rtol,True)
 if d['status']!='COMPLETE':return d
 Q=np.array(d['endpoint']);T=d['T'];bd=boundary(g,Q);init=[];Ge=g.initial_G(Q)if hasattr(g,'initial_G')else g.b0+g.g01*Q[1]
 for key in ['corrected_gradient','raw_gradient']:init.extend(np.r_[np.array(bd[key])/Q[0],Ge])
 def rhs(tt,z):
  ell,y=back.sol(T-tt);x=math.exp(ell);_,W,_,DW=g.field([x,y]);v=W[0]/x;M=(g.beta-2-v)*np.eye(2)-DW.T;ans=[]
  for i in [0,3]:ans.extend(np.r_[M@z[i:i+2],-(1+v)*z[i+2]+z[i]])
  return ans
 sol=solve_ivp(rhs,(0,T),init,method='DOP853',rtol=rtol,atol=rtol*.001)
 out={'status':'COMPLETE'if sol.success else'FORWARD_FAILED','Theta':math.exp((g.beta-2)*T)*bd['h']if hasattr(g,'boundary_data')else d['F']*point[0]**2,'T':T,'endpoint':Q.tolist(),'boundary':bd,'backward_nfev':d['nfev'],'forward_nfev':sol.nfev,'rin':rin,'rtol':rtol}
 for name,i in [('corrected',0),('raw',3)]:out[name]={'gradient':(point[0]*sol.y[i:i+2,-1]).tolist(),'G':float(sol.y[i+2,-1]),'Omega':float(point[0]*sol.y[i+2,-1])}
 return out

def scalar(g,p,rin,rtol):
 d,_=log_back(g,p,rin,rtol,False)
 if d['status']!='COMPLETE':raise ValueError('Scalar path incomplete '+str(d))
 return d['F']*p[0]**2

def difference(g,p,rin,rtol,hrel):
 p=np.array(p,dtype=float);grad=[];steps=[]
 for j in range(2):
  h=hrel*max(1.,abs(p[j]));e=np.zeros(2);e[j]=h;steps.append(h)
  values=[scalar(g,p+k*e,rin,rtol)for k in [-2,-1,1,2]]
  grad.append(float((values[0]-8*values[1]+8*values[2]-values[3])/(12*h)))
 return {'h_relative':hrel,'steps':steps,'gradient':grad}

class Isotropic:
 beta=3.;b0=1.1;g01=.2;u0=0.;lobes=[]
 def __init__(self,c=.4):self.f01=c
 def manufactured_log_rhs(self,t,z):return [-.5,-.5*z[1]]
 def field(self,p):
  p=np.asarray(p,dtype=float);W=.5*p;D=.5*np.eye(2);return W-3*p,W,D-3*np.eye(2),D
 def exact(self,p,rin):
  x,y=map(float,p);r=math.hypot(x,y);c=self.f01;T=2*math.log(r/rin);Q=rin*np.array(p)/r
  th=x*x*(1+c*rin*y/r);tx=2*x*(1+c*rin*y/r)-c*rin*x**3*y/r**3;ty=c*rin*x**4/r**3
  decay=math.exp(-1.5*T);G=decay*(self.b0+self.g01*Q[1])+(1-decay)*tx/x/1.5
  return th,np.array([tx,ty]),G

def controls():
 tick=time.monotonic();out={'started_utc':utc(),'checks':[]}
 def ck(n,b,**e):out['checks'].append({'name':n,'pass':bool(b),**e})
 import sympy as s
 x,y,a,mu,a11,f=s.symbols('x y a mu a11 f');h=x*x*(1+f*y);W1=a*x+a11*x*y;W2=mu*y
 defect=s.expand(W1*s.diff(h,x)+W2*s.diff(h,y)-2*a*h)
 ck('degree3 compatibility coefficient exact',s.Poly(defect,x,y).coeff_monomial(x*x*y)==2*a11+mu*f)
 ck('chosen mixed jet cancels degree3',s.expand((2*a11+mu*f).subs(f,-2*a11/mu))==0)
 for c in [0.,.4]:
  g=Isotropic(c)
  for pt,rin in [([1.,.3],.1),([3.,-2.],.001),([.2,4.],.1)]:
   q=transport(g,pt,rin,2e-12);th,grad,G=g.exact(pt,rin);tag=str((c,pt,rin))
   ck('manufacture complete '+tag,q['status']=='COMPLETE')
   err=max(abs(q['Theta']-th),float(np.max(abs(np.array(q['corrected']['gradient'])-grad))),abs(q['corrected']['G']-G))
   ck('manufacture exact extension gradient and forcing '+tag,err<1e-9,error=err)
   bd=q['boundary'];ck('boundary PDE '+tag,abs(bd['corrected_thermal_defect'])<1e-15 and abs(bd['tangential_change'])<1e-15)
   if c==0:ck('compatible correction zero '+tag,max(abs(z)for z in bd['correction'])==0)
   else:ck('incompatible correction detected '+tag,np.linalg.norm(np.array(q['corrected']['gradient'])-q['raw']['gradient'])>1e-8)
 class Shear(Isotropic):
  def manufactured_log_rhs(self,t,z):return [-.5-.25*z[1]/math.exp(z[0]),-1.5*z[1]]
  def field(self,p):
   p=np.asarray(p,dtype=float);D=np.array([[.5,.25],[0.,1.5]]);W=D@p;return W-3*p,W,D-3*np.eye(2),D
  def boundary_data(self,p):
   x,y=p;L=x-.25*y;return L*L,np.array([2*L,-.5*L])
  def initial_G(self,p):return (4/3)*(p[0]-.25*p[1])/p[0]
 for pt in [[1.,.3],[3.,-2.],[.2,.4]]:
  g=Shear();q=transport(g,pt,.001,2e-12);th,grad=g.boundary_data(pt);err=max(abs(q['Theta']-th),float(np.max(abs(np.array(q['corrected']['gradient'])-grad))),abs(q['corrected']['G']-g.initial_G(pt)))
  ck('non-diagonal exact gradient and forcing '+str(pt),q['status']=='COMPLETE'and err<1e-8,error=err)
  ck('non-diagonal boundary compatibility '+str(pt),max(abs(z)for z in q['boundary']['correction'])<1e-15)
 g=Isotropic(.4);pt=[1.,.3];fd=difference(g,pt,.1,2e-12,3e-4);exact=g.exact(pt,.1)[1];err=float(np.max(abs(np.array(fd['gradient'])-exact)))
 ck('independent scalar differences on manufacture',err<1e-8,error=err)
 class Tangent(Isotropic):
  def field(self,p):x,y=p;W=np.array([-y,x]);D=np.array([[0.,-1.],[1.,0.]]);return W,W,D,D
 try:boundary(Tangent(),np.array([.6,.8]));guard=False
 except ValueError:guard=True
 # Use an exactly representable tangent point to avoid a spurious floating cancellation.
 try:boundary(Tangent(),np.array([1.,0.]));guard_exact=False
 except ValueError:guard_exact=True
 ck('exact tangent intersection rejected',guard_exact)
 out.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-tick,passed=sum(q['pass']for q in out['checks']),total=len(out['checks']),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 save('controls.json',out);print({k:v for k,v in out.items()if k!='checks'},flush=True)
 if out['passed']!=out['total']:print([q for q in out['checks']if not q['pass']],flush=True);raise SystemExit('controls failed')

def run():
 tick=time.monotonic();out={'started_utc':utc(),'pid':os.getpid(),'status':'RUNNING','cases':[],'proof_sha256':hashlib.sha256((ROOT.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};save('results.json',out)
 allcases=[(k,v)for k,v in cases().items()if v['data']['G_min']<0 and not v['data']['unfinished']]
 for ci,(key,entry)in enumerate(allcases):
  c=entry['data'];g=SignedGaussianFlow(c['c_in'],c['lobes']);r,y=c['G_min_at'];p=[math.sqrt(r*r-y*y),y];row={'index':ci,'case':key,'point':p,'num_G':c['G_min'],'radii':[]};out['cases'].append(row)
  for rin in [1e-2,3e-3,1e-3,3e-4,1e-4]:
   q=transport(g,p,rin,2e-12);q['differences']=[]
   if q['status']!='COMPLETE':raise RuntimeError('Witness path incomplete '+str(q))
   q['legacy_cartesian_reference']=g.evaluate(p,r_in=rin,rtol=2e-12)
   if rin in [1e-2,1e-3,1e-4]:
    for h in [1e-2,3e-3,1e-3,3e-4]:
     d=difference(g,p,rin,2e-12,h);d['error_vs_corrected']=float(np.max(abs(np.array(d['gradient'])-q['corrected']['gradient'])));d['error_vs_raw']=float(np.max(abs(np.array(d['gradient'])-q['raw']['gradient'])));q['differences'].append(d)
   W=g.field(p)[1];q['corrected_target_thermal_residual']=float(W@np.array(q['corrected']['gradient']))-(g.beta-2)*q['Theta'];q['raw_target_thermal_residual']=float(W@np.array(q['raw']['gradient']))-(g.beta-2)*q['Theta']
   row['radii'].append(q);save('results.json',out);print('CASE',ci,'rin',rin,'G_corrected',q['corrected']['G'],'G_raw',q['raw']['G'],'gradient_change',float(np.max(abs(np.array(q['corrected']['gradient'])-q['raw']['gradient']))),'seconds',round(time.monotonic()-tick,2),utc(),flush=True)
 out.update(status='COMPLETE',ended_utc=utc(),elapsed_seconds=time.monotonic()-tick,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);save('results.json',out)

if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(10*1024**3,10*1024**3))
 ap=argparse.ArgumentParser();ap.add_argument('--controls',action='store_true');ap.add_argument('--run',action='store_true');a=ap.parse_args()
 if a.controls:controls()
 if a.run:run()
