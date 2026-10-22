"""Refine own quadrature and measure between-node ellipticity and tail leakage."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial.legendre import leggauss,legfit,legval,legder
import json,hashlib,time,os
from modal_interpolation_measure import Modal,radius,jacobian,source_modes,interpolate
from r2_state_values import R2State
from finite_difference import derivative

def coefficients(m,n):
 g,_=leggauss(n);ts=m.edges[:-1,None]+np.diff(m.edges)[:,None]*(g+1)/2;rs=radius(ts,m.b,m.L);k=np.arange(1,m.K+1);p=2+k%2
 P,_=m.evaluate(ts.ravel());S=P.reshape(len(m.edges)-1,n,m.K)/rs[...,None]**p
 return np.stack([legfit(g,s,n-1) for s in S])
def elliptic_modes(m,ts,S,St,Stt):
 rs=radius(ts,m.b,m.L);z=1-ts;tp=rs*z/(m.b*(m.L*m.L+rs*rs));tpp=z/(m.b*(m.L*m.L+rs*rs))*(1-(2+1/m.b)*rs*rs/(m.L*m.L+rs*rs));k=np.arange(1,m.K+1);p=2+k%2
 lap=rs[:,None]**(p-2)*((p*p-k*k)*S+(2*p+1)*rs[:,None]*tp[:,None]*St+rs[:,None]**2*(tp[:,None]**2*Stt+tpp[:,None]*St))
 return lap

def offnodes(m,coeff):
 # Deliberately not any of the seven interpolation nodes.
 z=np.array([-.94,-.73,-.37,-.09,.18,.53,.84]);ts=(m.edges[:-1,None]+np.diff(m.edges)[:,None]*(z+1)/2).ravel();rs=radius(ts,m.b,m.L);k=np.arange(1,m.K+1);p=2+k%2
 S=np.concatenate([legval(z,c).T for c in coeff]);St=np.concatenate([legval(z,legder(c,axis=0)).T*2/(hi-lo) for c,lo,hi in zip(coeff,m.edges[:-1],m.edges[1:])]);Stt=np.concatenate([legval(z,legder(c,m=2,axis=0)).T*(2/(hi-lo))**2 for c,lo,hi in zip(coeff,m.edges[:-1],m.edges[1:])])
 P=rs[:,None]**p*S;D=p*rs[:,None]**(p-1)*S+rs[:,None]**p/jacobian(ts,m.b,m.L)[:,None]*St;trueP,trueD=m.evaluate(ts);lap=elliptic_modes(m,ts,S,St,Stt);omega=m.source(rs);angles=np.pi*(np.arange(128)+.219)/128;sink=np.sin(k[:,None]*angles);cosk=np.cos(k[:,None]*angles);error=(-lap-omega)@sink;normal=k*(P-trueP)/rs[:,None];tangent=D-trueD;veldiff=np.sqrt((normal@cosk)**2+(tangent@sink)**2);NL=abs(lap@sink)+abs(omega@sink);ratio=np.divide(abs(error),NL,out=np.zeros_like(error),where=NL!=0);ratio[(NL==0)&(error!=0)]=np.inf
 rows=[]
 for lo,hi in ((0,1),(1,10),(10,100),(100,1e4),(1e4,np.inf)):
  mask=(rs>=lo)&(rs<hi)
  if not np.any(mask):continue
  jj,aa=np.unravel_index(abs(error[mask]).argmax(),error[mask].shape);ii=np.flatnonzero(mask)[jj]
  rows.append({'r_lo':lo,'r_hi':hi if np.isfinite(hi) else 'infinity','r_min_sampled':float(rs[mask].min()),'r_max_sampled':float(rs[mask].max()),'points':int(mask.sum()*len(angles)),'max_elliptic_abs':float(abs(error[mask]).max()),'max_elliptic_ratio':float(ratio[mask].max()),'max_elliptic_location':{'r':float(rs[ii]),'phi':float(angles[aa])},'max_velocity_error':float(veldiff[mask].max()),'max_velocity_error_over_1_plus_r':float((veldiff[mask]/(1+rs[mask,None])).max())})
 return rows

def run():
 root=Path('research/46_production_interpolation_audit/verification');start=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'source_hashes':{f:hashlib.sha256(Path('code_independent',f).read_bytes()).hexdigest() for f in ('modal_interpolation_refine.py','modal_interpolation_measure.py','r2_state_values.py')},'scope':'Near-exact own inverse nodal values followed by the production interpolation rule; not reproduction of production quadrature','states':[]}
 def save():
  out['elapsed_seconds']=time.monotonic()-start;(root/'refinement.json').write_text(json.dumps(out,indent=2)+'\n')
 # Verify radial Laplacian formula on polynomial S by Cartesian second differences.
 b=2.5;L=1.5;K=6;m=Modal(np.array([0.,1.]),b,L,K,lambda r:np.zeros(np.shape(r)+(K,)),8);points=np.array([[.31,.43],[.83,-.71],[1.37,.49]])
 tests=[]
 for h in (.004,.002,.001):
  for kk in (1,2,4,5):
   p=2+kk%2
   def psi(x,y):
    r=np.hypot(x,y);tt=-np.expm1(-np.log1p((r/L)**2)/(2*b));phi=np.arctan2(x,-y);return r**p*(1+.3*tt-.7*tt**2)*np.sin(kk*phi)
   r=np.hypot(*points.T);ts=-np.expm1(-np.log1p((r/L)**2)/(2*b));S=np.zeros((len(points),K));St=S.copy();Stt=S.copy();S[:,kk-1]=1+.3*ts-.7*ts**2;St[:,kk-1]=.3-1.4*ts;Stt[:,kk-1]=-.7*2
   exact=elliptic_modes(m,ts,S,St,Stt)[:,kk-1]*np.sin(kk*np.arctan2(points[:,0],-points[:,1]))
   # Standard symmetric five-point 1D second differences, two Cartesian axes.
   lap=0.
   for dim in (0,1):
    ee=np.zeros(2);ee[dim]=h
    vv=[psi(*(points+j*ee).T)for j in (-2,-1,0,1,2)];lap+=(-vv[0]+16*vv[1]-30*vv[2]+16*vv[3]-vv[4])/(12*h*h)
   tests.append({'h':h,'k':kk,'max_abs_difference':float(abs(lap-exact).max())})
 out['elliptic_formula_manufacture']=tests;save()
 snapshot=Path('candidate_snapshots/num_homotopy_20261020T164042')
 for path in sorted(snapshot.glob('*.npz')):
  state=R2State(path);row={'file':str(path),'sha256':state.sha256,'meta':state.meta,'runs':[]};out['states'].append(row)
  for kind in ('self','mixed'):
   def source(r):
    val=source_modes(state,r,'G')
    if kind=='mixed':
     eps=float(state.meta['eps']);val=eps*val+(1-eps)*source_modes(state,r,'external')
    return val
   for order in (128,256):
    m=Modal(state.edges,state.bb,state.L,state.K,source,order);c=coefficients(m,int(state.meta['ngc']));z=interpolate(m,int(state.meta['ngc']));z.update(kind=kind,order=order)
    width=state.edges[-1]-state.edges[-2];z['last_cell_taylor_coefficients_in_1_minus_t']=[(legval(1,legder(c[-1],m=j,axis=0))*(-2/width)**j/float(__import__('math').factorial(j))).tolist() for j in range(int(state.meta['ngc']))]
    if order==256:z['offnode_regions']=offnodes(m,c)
    row['runs'].append(z);save();print(path.name,kind,order,'origin',z['combined_linearization_defect'],'maxjump',max(a['max_velocity_jump']for a in z['interfaces']),'endpointmax',max(abs(v)for v in z['last_cell_taylor_coefficients_in_1_minus_t'][0]),'elapsed',time.monotonic()-start,flush=True)
  row['status']='COMPLETE';save()
 out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
