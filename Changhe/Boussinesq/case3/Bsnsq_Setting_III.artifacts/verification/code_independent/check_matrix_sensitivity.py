"""P208 finite-array sensitivity; no NUM imports or code execution."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,resource
import numpy as np
from scipy.linalg import cholesky,solve_triangular,svdvals,eigvalsh
from fractions import Fraction
root=Path('research/208_saved_jacobian_audit/verification');start=time.monotonic()
z=np.load(root/'frozen_sources/jac_L2v.npz');g=np.load('research/205_physical_gram_and_strain_norm/verification/native_gram.npz');d=np.load(root/'recomputed_matrix_diagnostics.npz')
J=z['JT'];A=J-np.eye(J.shape[0]);H=g['H'];C=cholesky(H,lower=False)
JH=solve_triangular(C.T,(C@J).T,lower=True).T;B=JH-np.eye(J.shape[0]);vH=C@d['physical_weak_coefficients'][-1];vH/=np.linalg.norm(vH)
vc=z['Vweak'][-1];vc/=np.linalg.norm(vc)
checks={};out={}
for name,M,Av,v in [('coefficient',J,A,vc),('physical',JH,B,vH)]:
 s=float(np.linalg.norm(Av@v));u=(Av@v)/s;ev=-s*u # rank-one E=-s u v^T; E v=ev
 val={'J_norm':float(svdvals(M,check_finite=False)[0]),'A_smallest_from_vector':s,'rank_one_unit_u_error':abs(float(u@u)-1),'rank_one_eigen1_residual':float(np.linalg.norm((M@v+ev)-v)),'norm_J_lower_bound':float(svdvals(Av,check_finite=False)[0]-1)}
 checks[name+'_rank_one_singular']=val['rank_one_eigen1_residual']<2e-12
 checks[name+'_J_expands']=val['J_norm']>1
 checks[name+'_norm_lower_bound']=val['J_norm']+1e-10>=val['norm_J_lower_bound']
 out[name]=val
vals=eigvalsh(H,check_finite=False);out['Gram']={'min_eigenvalue':float(vals[0]),'max_eigenvalue':float(vals[-1]),'condition':float(vals[-1]/vals[0]),'cholesky_relative_residual':float(np.linalg.norm(H-C.T@C)/np.linalg.norm(H))}
checks['Gram_SPD']=bool(vals[0]>0);checks['Gram_Cholesky']=out['Gram']['cholesky_relative_residual']<1e-12
q=g['q'];pro=np.load(root/'physical_dilation_projection.npz')['coefficients'];vects={'stored_old':z['v_s'],'stored_minus_state':z['v_s']-z['x_star'],'physical_projection_true':pro,'projection_q':q};out['actions']={}
for name,v in vects.items():
 row={}
 for metric,F in [('coefficient',None),('physical',C)]:
  vv=v if F is None else F@v;jv=J@v if F is None else F@(J@v);av=jv-vv;qq=q if F is None else F@q;n=np.linalg.norm(vv)
  r=float(np.linalg.norm(av)/n);c=float(vv@jv/n**2);j=float(np.linalg.norm(jv)/n)
  row[metric]={'Av_over_v':r,'Jv_over_v':j,'Rayleigh':c,'abs_cos_q':float(abs(vv@qq)/(n*np.linalg.norm(qq))),'identity11_abs_error':abs(j*j-(r*r-1+2*c))}
  checks[name+'_'+metric+'_identity11']=row[metric]['identity11_abs_error']<2e-13
 out['actions'][name]=row
# Exact rational counterexample, at arbitrarily chosen epsilon>0.
eps=Fraction(1,100000);out['nonlinear_counterexample']={'epsilon':str(eps),'defect_at_zero':str(eps),'exact_derivative_at_zero':0,'Newton_step':str(eps),'fixedpoint_discriminant':str(-3*eps*eps),'positive_completed_square_remainder':str(3*eps*eps/4),'conclusion':'No real fixed point; small-step implication refuted, not the existence of a root of the supplied map.'}
checks['counterexample_negative_discriminant']=(-3*eps*eps<0);checks['counterexample_positive_remainder']=(3*eps*eps/4>0)
# Archive and freeze the current report statements and postprocessing sources without running them.
freeze=root/'frozen_sources'
for src in ['../numerics/NUM_REPORT.md','../numerics/code/jac_post.py','../numerics/runs/jacpost_L2v.json']:
 p=Path(src);data=p.read_bytes();(freeze/('current_'+p.name)).write_bytes(data);out.setdefault('latest_source_hashes',{})[src]=hashlib.sha256(data).hexdigest()
res={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'checks':checks,'values':out,'verdict':'CONFIRMED' if all(checks.values()) else 'OPEN','scope':'Floating-point algebra of supplied finite arrays and independent finite Gram. No derivative error or nonlinear existence bound.'}
(root/'matrix_sensitivity.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:res[k] for k in ['utc','elapsed_seconds','maxrss_kib','verdict']},indent=2));print('checks',sum(checks.values()),len(checks));print('J norms',out['coefficient']['J_norm'],out['physical']['J_norm']);print('Gram',out['Gram'])
