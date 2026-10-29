# Lead cross-check of the verifier's positive-damping expansion certificate for the stored t1nk5 closure matrix (note 54).
# (1) the proof's identity ||v + beta w||^2 - ||v||^2 = 2 beta v.w + beta^2 ||w||^2 (sympy, symbolic n = 3 vectors);
# (2) the stored matrix (column-major float64, the original primary file, hash compared with the verifier's frozen copy) and the
#     verifier's leading real eigenvector: v^T (A - I) v / ||v||^2 in float64 and compensated (math.fsum) summation, compared
#     with the verifier's exact rational quotient and with lambda - 1;
# (3) an independent dense eigen-decomposition (numpy, LAPACK geev) of the stored matrix: leading real eigenvalue, spectral radius
#     and the count of eigenvalues of modulus > 1, compared with the primary values 12.58817456 and 214;
# (4) expansion factor ||(1-beta)v + beta A v|| / ||v|| for several beta, all > 1.
import numpy as np, sympy as sp, json, math, hashlib, datetime, time
from fractions import Fraction as F
t0=time.time(); res=[]
def check(name,ok,val=None):
    res.append(dict(check=name,ok=bool(ok),value=None if val is None else str(val))); print(('PASS' if ok else 'FAIL'),name,'' if val is None else val)
b=sp.symbols('beta',positive=True); v=sp.Matrix(sp.symbols('v0:3')); w=sp.Matrix(sp.symbols('w0:3'))
check('||v+beta w||^2-||v||^2 = 2 beta v.w + beta^2 ||w||^2',sp.expand((v+b*w).dot(v+b*w)-v.dot(v)-(2*b*v.dot(w)+b**2*w.dot(w)))==0)
VD='independent_validation/research/closure_matrix_damping/data/20261029T093725.214323Z/'
ORIG='referee/R25/results/c074_level3c/jacobian_000/map_columns.bin'
h1=hashlib.sha256(open(ORIG,'rb').read()).hexdigest(); h2=hashlib.sha256(open(VD+'map_columns.bin','rb').read()).hexdigest()
check('verifier frozen matrix is byte-identical to the primary file',h1==h2,h1)
n=1855
A=np.fromfile(ORIG,dtype='<f8'); check('matrix file holds n^2 = %d binary64 entries'%(n*n),A.size==n*n); A=A.reshape((n,n),order='F')
Z=np.load(VD+'full_map_eigenvectors.npz'); lam=Z['eigenvalues']; V=Z['eigenvectors']
i0=int(np.argmax(np.where(np.abs(lam.imag)<1e-12,lam.real,-np.inf))); vv=V[:,i0]
check('selected eigenvector is real (max |imag| = 0)',np.abs(vv.imag).max()==0.0,float(np.abs(vv.imag).max()))
vv=vv.real; Av=A@vv
resid=np.linalg.norm(Av-lam[i0].real*vv)/np.linalg.norm(vv)
check('eigen-residual of the stored pair below 1e-11',resid<1e-11,'%.3e (verifier 1.692e-13)'%resid)
Qf=math.fsum(float(x) for x in vv*(Av-vv))/math.fsum(float(x) for x in vv*vv)
cert=json.load(open(VD+'check.json')); qex=F(cert['quadratic_over_norm_squared'])
check('float64 v^T(A-I)v/||v||^2 agrees with the exact quotient to 1e-10 relative',abs(Qf-float(qex))<1e-10*abs(float(qex)),'%.12f vs exact %.12f'%(Qf,float(qex)))
check('exact quotient positive and equal to lambda - 1 within 1e-9',qex>0 and abs(float(qex)-(lam[i0].real-1))<1e-9,'lambda-1 = %.12f'%(lam[i0].real-1))
N=F(int(cert['quadratic_numerator']),1); Vn=F(int(cert['vector_norm_squared_numerator']),1)
check('exact integer numerators N and V positive',N>0 and Vn>0)
t1=time.time(); ev=np.linalg.eigvals(A); te=time.time()-t1
real=ev[np.abs(ev.imag)<1e-9*np.abs(ev).max()].real
lead=float(real.max()); rho=float(np.abs(ev).max()); cnt=int(np.sum(np.abs(ev)>1)); nr=int(np.sum(real>1))
check('independent dense eigenvalues: leading real eigenvalue 12.58817456 within 1e-6',abs(lead-12.58817456)<1e-6,'%.10f'%lead)
check('independent spectral radius equals the leading real eigenvalue',abs(rho-lead)<1e-6,'%.10f'%rho)
check('independent count of eigenvalues outside the unit disk within 214 +- 5 (the count is perturbation-sensitive)',abs(cnt-214)<=5,'%d (primary 214); real > 1: %d (primary 3)'%(cnt,nr))
dist=float(np.min(np.abs(np.abs(ev)-1)))
fac=[float(np.linalg.norm((1-bb)*vv+bb*Av)/np.linalg.norm(vv)) for bb in [1e-3,1e-2,0.1,0.5,1.0]]
check('expansion factor > 1 for beta = 1e-3, 1e-2, 0.1, 0.5, 1',all(f>1 for f in fac),['%.9f'%f for f in fac])
ok=all(r['ok'] for r in res)
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_checks=len(res),all_pass=ok,
         wall_seconds=round(time.time()-t0,1),eig_seconds=round(te,1),leading_real=lead,spectral_radius=rho,outside_count=cnt,
         real_above_one=nr,min_distance_of_modulus_to_one=dist,quotient_float=Qf,checks=res)
json.dump(out,open('author_checks/damping_cert_check_output.json','w'),indent=1)
print('checks',len(res),'all pass',ok,'wall',round(time.time()-t0,1),'min dist',dist)
