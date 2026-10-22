"""Independent finite-cutoff resolvents, quadrature, and stored PDE defects."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,shutil
import numpy as np
from scipy.integrate import solve_ivp
from r2_state_values import R2State
from smooth_modal_flow import SmoothModalFlow,reconstruct
from finite_difference import stencil
root=Path('verification/characteristic_decomposition_20261020T2100');root.mkdir(parents=True,exist_ok=True)
base=Path('verification/characteristic_a021hr_20261020T2029');s=R2State(base/'state_snapshot.npz');a0=s.center()['F']['value'];rho=s.beta-2
with np.load(base/'inverse_nodes.npz',allow_pickle=False) as z:flow=SmoothModalFlow(s.beta,z['radii'],z['pr'],z['dp'],z['H'])
zz,ww=stencil(1,3)
def grad(fun,X,relative_step):
 steps=relative_step*np.maximum(np.linalg.norm(X,axis=1),.01)
 values=[]
 for j in [0,1]:
  P=np.repeat(X[:,None,:],len(zz),axis=1);P[:,:,j]+=steps[:,None]*zz
  values.append(fun(P[:,:,0],P[:,:,1])@ww/steps)
 return np.array(values).T
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','snapshot_sha256':s.sha256,'cutoff':.001,'rows':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
points=[[.8318938104,2.4506801393],[-2.8780907797,.9769801726],[1.,1.],[.25,3.],[-.6,-1.],[2.,0.]]
for Y in points:
 Y=np.array(Y);cutoff=.001
 def event(t,X):return np.linalg.norm(X)-cutoff
 event.terminal=True;event.direction=-1
 back=solve_ivp(lambda t,X:-flow.W(X),(0.,250.),Y,events=event,dense_output=True,method='DOP853',rtol=2e-13,atol=2e-16,max_step=.2)
 assert back.success and len(back.t_events[0]);T=float(back.t_events[0][0]);seed=back.y_events[0][0]
 transport=reconstruct(flow,Y,s.beta,a0,cutoff=cutoff,rtol=2e-13,atol=2e-16,compatible_seed=True);assert transport['status']=='COMPLETE'
 scalar_seed=a0*seed[0]**2;vorticity_seed=4*a0*seed[0]/s.beta
 npanels=int(np.ceil(T/.125));edges=np.linspace(0.,T,npanels+1)
 for nq,h in [(12,1e-5),(24,1e-5),(24,5e-6)]:
  nodes,weights=np.polynomial.legendre.leggauss(nq);times=((edges[:-1,None]+edges[1:,None])/2+(edges[1:,None]-edges[:-1,None])*nodes/2).ravel();weights=((edges[1:,None]-edges[:-1,None])*weights/2).ravel()
  X=back.sol(times).T;gt=grad(s.theta,X,h);go=grad(s.omega,X,h);W=np.array([flow.W(P) for P in X]);th=s.theta(X[:,0],X[:,1]);om=s.omega(X[:,0],X[:,1])
  rv=np.sum(W*go,axis=1)+om-gt[:,0];rt=np.sum(W*gt,axis=1)-rho*th
  ws=weights*np.exp(-times);wt=weights*np.exp(rho*times)
  omega_source=float(np.exp(-T)*vorticity_seed+ws@gt[:,0]);d2boundary=float(np.exp(-T)*(s.omega(*seed)-vorticity_seed));d2integral=float(ws@rv)
  d3boundary=float(np.exp(rho*T)*(s.theta(*seed)-scalar_seed));d3integral=float(wt@rt)
  stored_omega=float(s.omega(*Y));stored_theta=float(s.theta(*Y));d2=stored_omega-omega_source;d3=stored_theta-transport['Theta']
  row={'point':Y.tolist(),'time_to_cutoff':T,'seed':seed.tolist(),'quadrature_panels':npanels,'gauss_order':nq,'relative_fd_step':h,'stored_Theta':stored_theta,'transported_Theta':transport['Theta'],'stored_Omega':stored_omega,'transported_Omega':transport['Omega'],'Omega_stored_source':omega_source,'total_vorticity_difference':stored_omega-transport['Omega'],'stored_vorticity_part_D2':d2,'source_gradient_part_D1':omega_source-transport['Omega'],'D2_boundary':d2boundary,'D2_integral':d2integral,'D2_integral_absolute':float(ws@abs(rv)),'D2_identity_error':d2-d2boundary-d2integral,'temperature_difference':d3,'D3_boundary':d3boundary,'D3_integral':d3integral,'D3_integral_absolute':float(wt@abs(rt)),'D3_identity_error':d3-d3boundary-d3integral,'min_radius':float(min(np.linalg.norm(X,axis=1))),'max_radius':float(max(np.linalg.norm(X,axis=1)))}
  out['rows'].append(row);save()
 print('point',Y.tolist(),'seconds',time.monotonic()-start,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),scope='Fixed forced velocity and finite cutoff. Independent ODE and between-node Cartesian differences; empirical tolerance checks, no certified inverse fixed point or profile.')
code=['characteristic_decomposition.py','finite_difference.py','r2_state_values.py','smooth_modal_flow.py'];snap=root/'code_snapshot';snap.mkdir(exist_ok=True)
for name in code:shutil.copyfile(Path('code_independent',name),snap/name)
out['code_hashes']={name:hashlib.sha256(Path('code_independent',name).read_bytes()).hexdigest() for name in code};save();print('COMPLETE',out['elapsed_seconds'],flush=True)
