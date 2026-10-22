"""Meaningful manufactured matrix and independent radial controls for P208."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as sp
import numpy as np
from scipy.linalg import cholesky,solve_triangular
from r2_state_values import R2State
from native_dilation import full_plane_dilation,dilation_radial
r=Path(__file__).resolve().parents[1];v=r/'research/208_saved_jacobian_audit/verification'
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks={};values={}
e,gp,gm=sp.symbols('e gp gm');expr=(gp/(1+e)-gm/(1-e))/(2*e)-((gp-gm)/(2*e)-(gp+gm)/2)/(1-e**2)
checks['exact_finite_step_identity']=sp.simplify(expr)==0
J=np.array([[0.,0.],[0.,2.]]);q=np.array([1.,0.]);A=J-np.eye(2)
checks['projection_vector_is_not_neutral']=np.all(J@q==0) and np.linalg.norm(A@q)==1
J2=np.array([[1.,1.],[1.,1.]]);checks['unit_rayleigh_is_not_neutral']=q@J2@q==1 and np.linalg.norm(J2@q-q)==1
H=np.array([[5.,1.],[1.,2.]]);C=cholesky(H,lower=False)
B=solve_triangular(C.T,(C@A).T,lower=True).T
x=np.array([.7,-.4]);y=C@x
checks['upper_cholesky_similarity']=np.linalg.norm(B@y-C@(A@x))<1e-14
checks['physical_norm_ratio']=abs(np.linalg.norm(B@y)/np.linalg.norm(y)-np.sqrt((A@x)@H@(A@x)/(x@H@x)))<1e-14
# Fixed-point linearized solves, with a manufactured exactly affine map.
J3=np.array([[.2,.4],[-.1,.6]]);pcol=np.array([.9,-.4]);f=np.array([.002,-.003]);M=np.eye(2)-J3
xp=np.linalg.solve(M,pcol);delta=np.linalg.solve(M,f)
checks['parameter_solve_sign']=np.linalg.norm(M@xp-pcol)<1e-14
checks['Newton_solve_sign']=np.linalg.norm(f+(J3-np.eye(2))@delta)<1e-14
statepath=r/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz';state=R2State(statepath)
z=np.load(r/'research/205_physical_gram_and_strain_norm/verification/native_gram.npz');active=z['active'];xg=state.rawG[active];H=z['H'];q=z['q']
values['state_sha256']=state.sha256
radii=state.L*np.sqrt(np.expm1(-2*state.bb*np.log1p(-(state.edges[:-1]+state.edges[1:])/2)))
exact=dilation_radial(state,radii);studies=[]
for h in [1e-3,5e-4,2.5e-4]:
    # Fourth-order Cartesian radial difference at fixed angle, four separate value evaluations.
    derivative=(state.radial(radii*(1-2*h))-8*state.radial(radii*(1-h))+8*state.radial(radii*(1+h))-state.radial(radii*(1+2*h)))/(12*h)
    err=np.max(abs(derivative+exact['old']))/np.max(abs(exact['old']))
    studies.append({'h_relative':h,'max_scaled_radial_error':float(err)})
checks['independent_radial_derivative']=studies[-1]['max_scaled_radial_error']<1e-8
values['radial_study']=studies
old0=dilation_radial(state,np.array([0.]))
checks['origin_dilation_amplitude']=old0['old'][0,0]==0 and old0['true'][0,0]==-state.rawG[0]
results=[]
for order in [24,48]:
    d=full_plane_dilation(state,{'zero':np.zeros_like(xg),'minus_G':-xg},order=order,H=H,active=active)
    checks['gram_norm_order_'+str(order)]=abs(d['G_squared']-xg@H@xg)<1e-10*max(1,d['G_squared'])
    # (-G) - true = -old; test exact amplitude relation independently under quadrature.
    checks['dilation_relation_order_'+str(order)]=abs(d['errors']['minus_G']['to_true_squared']-d['old_squared'])<1e-10*max(1,d['old_squared'])
    proj=d.pop('physical_projection_true');rhs=d.pop('rhs_true')
    checks['projection_solve_order_'+str(order)]=np.linalg.norm(H@proj-rhs)/np.linalg.norm(rhs)<1e-11
    d['physical_projection_strain']=float(q@proj);d['projection_center']=float(proj[0]);d['projection_norm']=float(np.sqrt(proj@H@proj));results.append(d)
    if order==48:np.savez(v/'physical_dilation_projection.npz',coefficients=proj,rhs=rhs,active=active,state_sha256=state.sha256)
values['physical_dilation']=results
checks['full_plane_dilation_refinement']=max(abs(results[1][k]-results[0][k])/max(1,abs(results[1][k])) for k in ['G_squared','old_squared','true_squared'])<1e-9
checks={k:bool(x) for k,x in checks.items()}
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'values':values,'scope':'Manufactured algebra and physical quadrature consistency; no saved Jacobian or underlying map derivative has yet been validated.'}
(v/'identity_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'elapsed_seconds':out['elapsed_seconds'],'passed':sum(checks.values()),'total':len(checks),'failed':[k for k,x in checks.items() if not x],'radial_study':studies,'projection_strain':results[-1]['physical_projection_strain']},indent=2));assert all(checks.values())
