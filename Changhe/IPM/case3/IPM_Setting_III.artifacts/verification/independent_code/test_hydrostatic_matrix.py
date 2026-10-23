"""Small independent gates for result201; no producer imports or live-state SVD."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,time
import numpy as np
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet,VerticalInverse,exact_hydrostatic_center
from independent_hydrostatic_matrix import HydrostaticBasisMatrices,residual_and_jacobian
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf
r=Path('research/hydrostatic_jacobian_audit/verification');r.mkdir(parents=True,exist_ok=True)
start=time.monotonic();checks=[]
def check(name,condition,detail=None):checks.append(dict(name=name,pass_=bool(condition),detail=detail))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
rng=np.random.default_rng(184201);N=8;M=4;n=sum(N+1-k for k in range(M));u=rng.normal(size=n)*.02;u[0]=2
path=r/'manufactured_input.npz';np.savez(path,N=N,M=M,u=u,tk=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1)),basis='local',L=1.3,p=5/3,cl=2.5)
q=QLocalCheckpoint(path);model=HydrostaticBasisMatrices(q);scalar=CartesianQJet(q);C=model.constraint_rows()
xy=np.array([[0,0],[.137,.219],[0,.37],[.37,0],[.001,.003],[6,8],[-.137,.219],[.137,-.219],[-.137,-.219],[30,40]])
J=model.jet(xy[:,0],xy[:,1]);got=J@u;ref=scalar.jet(xy[:,0],xy[:,1]);errors=np.abs(got-ref)/(1+np.abs(ref))
for k,name in enumerate(['g','gx','gy','gxx']):check('basis vs coefficient Clenshaw '+name,float(errors[:,k].max())<2e-12,float(errors[:,k].max()))
check('density x parity',np.allclose(J[1,0],J[6,0],rtol=0,atol=1e-13))
check('density y parity',np.allclose(J[1,0],-J[7,0],rtol=0,atol=1e-13))
for k in range(4):check('exact origin basis '+str(k),np.array_equal(J[0,k],C[0] if k==2 else np.zeros(n)))
exact=exact_hydrostatic_center(q.exact_coefficients(),Fraction(q.kappa));center=float(C[2]@u)
check('center vs exact rational',abs(center-float(exact))<2e-12,dict(matrix=center,exact=float(exact),error=center-float(exact)))
check('minimum exact polynomial order center',np.max(np.abs(C-model.constraint_rows((N+2)//2)))<2e-12,float(np.max(np.abs(C-model.constraint_rows((N+2)//2)))))
check('tail row',abs(float(q.rho(0.,1e80))/1e80**q.p-C[1]@u)<2e-12,float(q.rho(0.,1e80))/1e80**q.p-float(C[1]@u))
# Three points, scalar differentiation with an independent high-precision radius inversion.
with mp.workdps(65):
 mm=MPQDensity.__new__(MPQDensity);mm.coeff=[[mf(v)for v in row]for row in q.exact_coefficients()];mm.L=mf(q.L);mm.kappa=mf(q.kappa);mm.ell=mf(q.cl)
 def density(x,y):
  radius=mp.sqrt(x*x+y*y)
  return radius*mm.at(radius,mp.atan2(y,x))[0] if radius else mp.mpf(0)
 for i in (1,2,5):
  x,y=map(mf,xy[i]);a=[density(x,y),mp.diff(lambda z:density(z,y),x),mp.diff(lambda z:density(x,z),y),mp.diff(lambda z:density(z,y),x,2)]
  for k,v in enumerate(a):
   error=float(abs(mf(got[i,k])-v)/(1+abs(v)));check('MP jet '+str(i)+' '+str(k),error<3e-11,error)
# Linear quadrature contraction: same complete quadrature, independently evaluated jets.
rows=[]
for i in (1,2,3,6):
 x,y=xy[i];mat=model.velocity(x,y,order=12,tail_order=48,split=16.)
 v=VerticalInverse(scalar.jet,q.p,12,48,16.,.125).at(x,y)['V'];err=np.max(np.abs(mat@u-v)/(1+np.abs(v)))
 check('matrix inverse contraction '+str(i),err<2e-12,float(err));rows.append(dict(point=[x,y],matrix=(mat@u).tolist(),scalar=v,error=float(err)))
# Check exactly quadratic remainder and centered derivative against the assembled J.
X,Y=xy[[1,2,3,5],0],xy[[1,2,3,5],1]
maps=model.sample_maps(X,Y,order=12,tail_order=48,split=16.)
for center_flag in (False,True):
 F,J=residual_and_jacobian(maps,u,q.cl,center_flag)
 for direction in range(3):
  h=rng.normal(size=n);h/=np.linalg.norm(h);nonlinear=(maps['V1']@h)*(maps['Gx']@h)+(maps['V2']@h)*(maps['Gy']@h)
  for t in (2.**-5,2.**-9):
   Fp,_=residual_and_jacobian(maps,u+t*h,q.cl,center_flag);Fm,_=residual_and_jacobian(maps,u-t*h,q.cl,center_flag)
   target=np.r_[nonlinear,np.zeros(3 if center_flag else 2)]
   err1=np.max(np.abs(Fp-F-t*(J@h)-t*t*target)/(1+np.abs(F)))
   err2=np.max(np.abs((Fp-Fm)/(2*t)-J@h)/(1+np.abs(J@h)))
   check('quadratic remainder '+str((center_flag,direction,t)),err1<2e-13,float(err1))
   check('centered derivative '+str((center_flag,direction,t)),err2<2e-11,float(err2))
# Preserve the coarse error, then refine independently instead of asserting coarse accuracy.
configs=[(12,48,16.),(20,112,64.),(28,192,256.),(36,320,1024.),(44,512,4096.),(52,768,16384.)]
values=[model.velocity(.137,.219,order=a,tail_order=b,split=c)@u for a,b,c in configs]
diffs=[float(np.max(np.abs(a-b)))for a,b in zip(values,values[1:])]
check('coarse discrepancy retained and diagnosed',diffs[0]>1e-6,dict(configs=configs,values=[a.tolist()for a in values],differences=diffs))
check('full-tail observed refinement',all(a>b for a,b in zip(diffs,diffs[1:])),diffs)
check('finest full-tail quadrature change',diffs[-1]<2e-10,diffs[-1])
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,checks=checks,pass_count=sum(c['pass_']for c in checks),fail_count=sum(not c['pass_']for c in checks),matrix_sha256=sha('independent_code/independent_hydrostatic_matrix.py'),checker_sha256=sha(__file__),input_sha256=sha(path),proof_sha256=sha(r.parent/'PROOF.md'),inverse_rows=rows,status='PASS'if all(c['pass_']for c in checks)else'FAIL',scope='Small manufactured finite-space gate; actual-state matrices and spectra not computed.')
dependencies=['independent_code/audit_hydrostatic_jacobian_state.py','independent_code/independent_hydrostatic_matrix.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/q_high_precision_density.py','independent_code/q_mp_primitives.py',__file__,'independent_code/check_jacobian_review_edges.py',str(r.parent/'PROOF.md'),str(r.parent/'SPECTRAL_PROOF.md'),str(r.parent/'REVIEW_REPAIR_PROOF.md')]
out['dependencies']={p:sha(p)for p in dependencies}
(r/'GATE.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(out['utc'],out['status'],out['pass_count'],'checks',out['seconds'],'seconds')
for c in checks:
 if not c['pass_']:print('FAIL',c)
if out['fail_count']:raise SystemExit(1)
