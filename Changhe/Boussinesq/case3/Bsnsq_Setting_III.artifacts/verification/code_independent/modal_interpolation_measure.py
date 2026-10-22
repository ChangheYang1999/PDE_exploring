"""Own full-plane modal quadrature and Legendre interpolation diagnostics.
No fitting-lane imports. Primary inverse audit remains Cartesian Duffy.
"""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial.legendre import leggauss,legfit,legval,legder
import json,time,os,hashlib
from r2_state_values import R2State

def radius(t,b,L):return L*np.sqrt(np.expm1(-2*b*np.log1p(-np.asarray(t))))
def jacobian(t,b,L):
 r=radius(t,b,L);return b*(L*L+r*r)/(r*(1-t))
def source_modes(state,r,kind):
 g=state.radial(r,kind);z=np.zeros(g.shape[:-1]+(state.K+2,));z[...,:state.K]=g
 modes=.5*np.asarray(r)[...,None]*(z[...,:state.K]-z[...,2:state.K+2]);modes[...,0]+=.5*np.asarray(r)*g[...,0]
 return modes

class Modal:
 def __init__(self,edges,b,L,K,source,order):
  self.edges=np.asarray(edges);self.b=b;self.L=L;self.K=K;self.source=source;self.order=order
  self.g,self.w=leggauss(order);self.g=(self.g+1)/2;self.w=self.w/2
  lo=self.edges[:-1,None];width=np.diff(self.edges)[:,None];self.t=lo+width*self.g
  self.r=radius(self.t,b,L);self.weight=width*self.w*jacobian(self.t,b,L)
  self.om=source(self.r);self.weighted=self.om*self.weight[...,None]
 def partial(self,lo,hi):
  t=lo+(hi-lo)*self.g;r=radius(t,self.b,self.L)
  return r,self.source(r)*((hi-lo)*self.w*jacobian(t,self.b,self.L))[:,None]
 def evaluate(self,targets):
  ts=np.asarray(targets).reshape(-1);rs=radius(ts,self.b,self.L);P=np.empty((len(ts),self.K));D=P.copy();kk=np.arange(1,self.K+1)
  for i,(t,r) in enumerate(zip(ts,rs)):
   cell=min(len(self.edges)-2,np.searchsorted(self.edges,t,side='right')-1)
   rl,wl=self.partial(self.edges[cell],t);ru,wu=self.partial(t,self.edges[cell+1])
   inner=np.concatenate((self.r[:cell].ravel(),rl));wi=np.concatenate((self.weighted[:cell].reshape(-1,self.K),wl))
   outer=np.concatenate((ru,self.r[cell+1:].ravel()));wo=np.concatenate((wu,self.weighted[cell+1:].reshape(-1,self.K)))
   I=np.sum((inner[:,None]/r)**(kk+1)*wi,axis=0)
   # k1 outer source integral is deliberately not formed: it can diverge.
   J=np.zeros(self.K);J[0]=-wi[:,0].sum();J[1:]=np.sum((r/outer[:,None])**(kk[1:]-1)*wo[:,1:],axis=0)
   P[i]=r*(I+J)/(2*kk);D[i]=(-I+J)/2
  return P,D
 def velocity(self,points):
  x,y=np.asarray(points).T;r=np.hypot(x,y);t=-np.expm1(-np.log1p((r/self.L)**2)/(2*self.b));phi=np.arctan2(x,-y);P,D=self.evaluate(t);k=np.arange(1,self.K+1)
  ur=-np.sum(k*P*np.cos(phi[:,None]*k)/r[:,None],axis=1);up=np.sum(D*np.sin(phi[:,None]*k),axis=1)
  return np.column_stack((np.sin(phi)*ur+np.cos(phi)*up,-np.cos(phi)*ur+np.sin(phi)*up))

def interpolate(modal,n=7):
 g,_=leggauss(n);edges=modal.edges;t=edges[:-1,None]+np.diff(edges)[:,None]*(g+1)/2;r=radius(t,modal.b,modal.L)
 P,D=modal.evaluate(t.ravel());P=P.reshape(len(edges)-1,n,modal.K);powers=2+(np.arange(1,modal.K+1)%2);S=P/r[...,None]**powers
 coeff=np.stack([legfit(g,s,n-1) for s in S]);left=np.stack([legval(-1,c) for c in coeff]);right=np.stack([legval(1,c) for c in coeff]);dl=np.stack([legval(-1,legder(c,axis=0))*2/(hi-lo) for c,lo,hi in zip(coeff,edges[:-1],edges[1:])]);dr=np.stack([legval(1,legder(c,axis=0))*2/(hi-lo) for c,lo,hi in zip(coeff,edges[:-1],edges[1:])]);
 ri=radius(edges[1:-1],modal.b,modal.L);dt=1/jacobian(edges[1:-1],modal.b,modal.L);jumpS=left[1:]-right[:-1];normal=-np.arange(1,modal.K+1)*ri[:,None]**(powers-1)*jumpS;tangent=powers*ri[:,None]**(powers-1)*jumpS+ri[:,None]**powers*dt[:,None]*(dl[1:]-dr[:-1])
 angles=np.pi*(np.arange(1024)+.317)/1024;k=np.arange(1,modal.K+1);nj=normal@np.cos(k[:,None]*angles);tj=tangent@np.sin(k[:,None]*angles)
 # At0 only even k have degree2. Compare all directions with axes' columns.
 a=left[0].copy();a[k%2==1]=0
 def linear_velocity(phi):
  ur=-np.sum(k[:,None]*a[:,None]*np.cos(k[:,None]*phi),axis=0);up=2*np.sum(a[:,None]*np.sin(k[:,None]*phi),axis=0)
  return np.column_stack((np.sin(phi)*ur+np.cos(phi)*up,-np.cos(phi)*ur+np.sin(phi)*up))
 axes=linear_velocity(np.array([np.pi/2,np.pi]));actual=linear_velocity(angles);pred=np.sin(angles)[:,None]*axes[0]-np.cos(angles)[:,None]*axes[1]
 return {'first_cell_S_at_zero':left[0].tolist(),'mode4_c':float(a[3]) if modal.K>=4 else None,'mode4_directional_discrepancy':float(8*abs(a[3])) if modal.K>=4 else None,'combined_linearization_defect':float(np.linalg.norm(actual-pred,axis=1).max()),'interfaces':[{'index':i+1,'t':float(edges[i+1]),'r':float(ri[i]),'normal_mode_jumps':normal[i].tolist(),'tangential_mode_jumps':tangent[i].tolist(),'max_normal_jump':float(abs(nj[i]).max()),'max_tangential_jump':float(abs(tj[i]).max()),'max_velocity_jump':float(np.sqrt(nj[i]**2+tj[i]**2).max())} for i in range(len(ri))]}

def run():
 root=Path('research/46_production_interpolation_audit/verification');start=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'scope':'Independent exact-source modal quadrature then production-rule interpolation, not solver quadrature reproduction','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manufactures':[],'states':[]}
 def save():
  out['elapsed_seconds']=time.monotonic()-start;(root/'measurements.json').write_text(json.dumps(out,indent=2)+'\n')
 save()
 for beta in (2.5,3.):
  K=6;k=np.arange(1,K+1);a=(2-1/beta-k)/2;targets=np.array([.0002,.003,.021,.079,.217,.541,.79,.947]);rr=radius(targets,beta,1.5)
  def source(r):
   r=np.asarray(r)[...,None];q=r*r;return -r**k*(4*q*a*(a-1)*(1+q)**(a-2)+4*(k+1)*a*(1+q)**(a-1))
  expected=rr[:,None]**k*(1+rr[:,None]**2)**a;dexpected=rr[:,None]**(k-1)*(1+rr[:,None]**2)**a*(k+2*a*rr[:,None]**2/(1+rr[:,None]**2));expected[:,0]-=rr;dexpected[:,0]-=1
  for order in (16,32,64):
   m=Modal(np.linspace(0,1,41)**1.5,beta,1.5,K,source,order);P,D=m.evaluate(targets)
   out['manufactures'].append({'beta':beta,'order':order,'radius':rr.tolist(),'max_relative_stream_error':float((abs(P-expected)/(1+abs(expected))).max()),'max_relative_derivative_error':float((abs(D-dexpected)/(1+abs(dexpected))).max()),'max_absolute_stream_error':float(abs(P-expected).max()),'max_absolute_derivative_error':float(abs(D-dexpected).max())});save()
 snapshot=Path('candidate_snapshots/num_homotopy_20261020T164042');cart=json.loads(Path('verification/intermediate_fullplane_20261020T1640/results.json').read_text())
 for path in sorted(snapshot.glob('*.npz')):
  state=R2State(path);row={'file':str(path),'sha256':state.sha256,'meta':state.meta,'runs':[]};out['states'].append(row);save()
  old=next(s for s in cart['states'] if s['file']==path.name);check=next(r for r in old['inverse_runs'] if r['core']==48 and r['order']==72);probes=np.array(check['points'])
  for kind in ('self','mixed'):
   def source(r):
    value=source_modes(state,r,'G')
    if kind=='mixed':
     eps=float(state.meta['eps']);value=eps*value+(1-eps)*source_modes(state,r,'external')
    return value
   for order in (16,32,64):
    m=Modal(state.edges,state.bb,state.L,state.K,source,order);result=interpolate(m,int(state.meta['ngc']));vel=m.velocity(probes);result.update(order=order,kind=kind,velocity=vel.tolist(),cartesian72_max_difference=float(abs(vel-np.array(check[kind]['V'])).max()));row['runs'].append(result);save();print(path.name,kind,'order',order,'mode4',result['mode4_c'],'linear',result['combined_linearization_defect'],'maxjump',max(t['max_velocity_jump'] for t in result['interfaces']),'cartdiff',result['cartesian72_max_difference'],'elapsed',time.monotonic()-start,flush=True)
  row['status']='COMPLETE';save()
 out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['elapsed_seconds'],flush=True)

if __name__=='__main__':run()
