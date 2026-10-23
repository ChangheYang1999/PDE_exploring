"""Independent smooth-basis least-squares experiment with direct Cartesian inverse.

This is a numerical search, not an existence certificate. The finite angular
basis cannot solve the exact PDE nontrivially; refinement and off-grid tests
are necessary. Fixed c_l is an experimental parameter, never a scaling gauge.
"""
import argparse,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import scipy
from scipy.linalg import null_space
from scipy.optimize import least_squares
from numpy.polynomial import chebyshev as C
from smooth_basis import SmoothBasis,SmoothDensity
from kernel_basis import KernelBasis
from direct_inverse import Quadrature
from candidate_reader import Candidate
from resumable_matrix_cache import MatrixCache,digest

ap=argparse.ArgumentParser()
ap.add_argument('--radial',type=int,default=12);ap.add_argument('--angular',type=int,default=8)
ap.add_argument('--cl',type=float,default=3.066481857503252)
ap.add_argument('--length',type=float,default=1.)
ap.add_argument('--seed',default='evidence/root_b4b_N48M32.npz')
ap.add_argument('--tag',default='smooth_first');ap.add_argument('--q',type=int,default=0)
ap.add_argument('--max-nfev',type=int,default=160);ap.add_argument('--jet-weight',type=float,default=1.)
ap.add_argument('--jet-scale',type=float,help='Explicit common positive squared-slope scale for controlled comparisons.')
ap.add_argument('--grid-radial',type=int);ap.add_argument('--grid-angular',type=int)
ap.add_argument('--matrix-checkpoint-rows',type=int,default=25)
ap.add_argument('--precondition',action='store_true');ap.add_argument('--seed-transfer',choices=['fit','coefficients'],default='coefficients');args=ap.parse_args()
if args.cl<=1:raise ValueError('c_l must exceed one')
if args.matrix_checkpoint_rows<1:raise ValueError('matrix-checkpoint-rows must be positive')
start=time.time();started=datetime.now(timezone.utc).isoformat()
dest=Path('evidence/smooth_solver')/args.tag;dest.mkdir(parents=True,exist_ok=True)
basis=SmoothBasis(args.radial,args.angular,1/args.cl,args.length)
a0row=basis.center_slope();crow=basis.center_strain();krow=basis.axis_amplitude()
brow,erow=basis.cubic_density_rows();hrow=basis.quartic_stream_difference();A=2*args.cl-1
# Linear constraints: exact canonical center strain and primary reporting scale.
constraint=np.array([crow,krow-a0row]);target=np.array([1-args.cl,0.])
cnorm=np.linalg.norm(constraint,axis=1);constraint/=cnorm[:,None];target/=cnorm
zpart=np.linalg.lstsq(constraint,target,rcond=None)[0];null=null_space(constraint)
# Interior quadrant points, with explicit small-radius and far-field coverage.
nr=args.grid_radial or (2*args.radial+3);nt=args.grid_angular or (2*args.angular+1)
t=-np.cos(np.pi*(np.arange(nr)+.5)/nr);u=(1-t)/2
r=args.length*np.sqrt(np.expm1(-np.log(u)/basis.a))
# Ultra-small rows magnify cancellation. The exact center jets are separate rows.
r=np.maximum(r,args.length*.015)
th=(np.arange(nt)+.5)*np.pi/(2*nt)
x=(r[:,None]*np.cos(th)).reshape(-1);y=(r[:,None]*np.sin(th)).reshape(-1)
value,gx,gy=basis.evaluate(x,y,True)
geom=basis.geometry(x,y);w,sigma=geom[4],geom[5]
scale=(y*w*w*np.maximum(sigma,.02))
D=args.cl*(x[:,None]*gx+y[:,None]*gy)-value
configs=[(24,128,96),(40,256,144),(64,512,224)]
nq,ntq,neq=configs[args.q]
q=Quadrature(nq,ntq,neq,4.,args.length,basis.p,16*args.length,1/(1-basis.p))
metadata={'started_utc':started,'arguments':vars(args),'basis':basis.metadata(),'quadrature':q.__dict__,'point_count':len(x),'representation':'SmoothBasis, direct Cartesian full-plane inverse, analytic Cartesian derivatives','constraints':'c=1-c_l and K=a0, L_can=1 only when a0 nonzero and K/a0 positive','scope':'fixed-c_l experiment; no parameter normalization and no existence claim'}
(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
source_dir=Path(__file__).resolve().parent
matrix_identity={
    'schema':'independent-direct-inverse-committed-rows-v1',
    'basis':basis.metadata(),'quadrature':q.__dict__,'x_sha256':digest(x),'y_sha256':digest(y),
    'numpy':np.__version__,'scipy':scipy.__version__,
    'source_sha256':{name:hashlib.sha256((source_dir/name).read_bytes()).hexdigest()
        for name in ('kernel_basis.py','direct_inverse.py','smooth_basis.py','resumable_matrix_cache.py')}}
cache_key=hashlib.sha256(json.dumps(matrix_identity,sort_keys=True).encode()).hexdigest()[:24]
cache=Path('evidence/smooth_solver')/('matrix_v2_'+cache_key)
matrix_cache=MatrixCache(cache,value.shape,matrix_identity)
uxmat,uymat=matrix_cache.arrays
metadata['matrix_cache']={'directory':str(cache),'identity':matrix_identity,
    'resumed_rows':matrix_cache.completed_rows,'checkpoint_rows':args.matrix_checkpoint_rows}
(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'matrix_cache':str(cache),
                  'resumed_rows':matrix_cache.completed_rows,'total':len(x)}),flush=True)
if matrix_cache.completed_rows<len(x):
    inv=KernelBasis(basis,q)
    for j in range(matrix_cache.completed_rows,len(x)):
        mm=inv.velocity_matrix(x[j],y[j]);uxmat[j]=mm[0];uymat[j]=mm[1]
        if (j+1)%args.matrix_checkpoint_rows==0 or j+1==len(x):
            matrix_cache.commit(j+1)
            print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'matrix_committed_rows':j+1,
                              'total':len(x),'seconds':time.time()-start}),flush=True)
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'matrix_finished':str(cache),
                  'seconds':time.time()-start}),flush=True)

# Fit an independently reconstructed numeric seed after its genuine scaling.
if args.seed.endswith('.npz'):
    check=np.load(args.seed,allow_pickle=False)
    own=('coefficients' in check.files)
    check.close()
else:own=False
if own:
    old=np.load(args.seed,allow_pickle=False)
    ob=SmoothBasis(int(old['radial']),int(old['angular']),float(old['exponent']),float(old['length']))
    seedrho=SmoothDensity(ob,old['coefficients']).rho(x,y)
    seedmeta={'source':args.seed,'own_smooth_seed':True}
else:
    c=Candidate(args.seed,project_center=True)
    endpoint=C.chebval(1,c.coefficients)-c.endpoint_modes
    a0=float(C.chebval(-1,c.coefficients)[0]);K=c.meta['L']**(1-c.meta['gamma'])*float(endpoint@((-1.)**np.arange(c.meta['M'])))
    if K/a0<=0:raise ValueError('Seed not in the positive K/a0 primary scale chart')
    Lcan=(K/a0)**(1/(1-c.meta['gamma']));lam=1/Lcan
    seedrho=lam*c.rho(x/lam,y/lam)
    seedmeta={**c.meta,'seed_a0':a0,'seed_K':K,'seed_Lcan':Lcan,'rescaling_lambda':lam}
fitvalue=value/(y*w)[:,None];fitseed=seedrho/(y*w)
if own and args.seed_transfer=='coefficients':
    transferred=np.zeros((basis.M,basis.N+1))
    oldcoeff=np.asarray(old['coefficients']).reshape(ob.M,ob.N+1)
    mm=min(ob.M,basis.M);nn=min(ob.N,basis.N)+1
    transferred[:mm,:nn]=oldcoeff[:mm,:nn]
    yseed=null.T@(transferred.reshape(-1)-zpart)
    seedmeta['transfer']='Coefficient pad/truncate then projection onto center and scale constraints; p/L changes may alter shape.'
else:
    yseed=np.linalg.lstsq(fitvalue@null,fitseed-fitvalue@zpart,rcond=1e-11)[0]
    seedmeta['transfer']='Least-squares shape fit.'
zseed=zpart+null@yseed
jet_scale=max(abs(a0row@zseed),1.)**2 if args.jet_scale is None else args.jet_scale
if not np.isfinite(jet_scale) or jet_scale<=0:raise ValueError('jet-scale must be positive and finite')
jetweight=args.jet_weight/jet_scale
sqrtpoints=np.sqrt(len(x))

def full(z,jac=False):
    ux=uxmat@z;uy=uymat@z;rx=gx@z;ry=gy@z
    raw=D@z+ux*rx+uy*ry
    a=a0row@z;b=brow@z;e=erow@z;h=hrow@z
    jets=np.array([(a-2*A)*b-6*e,(a-4*A)*b-3*a*h])
    residual=np.concatenate((raw/scale/sqrtpoints,jets*jetweight))
    if not jac:return residual
    J=(D+ux[:,None]*gx+uy[:,None]*gy+rx[:,None]*uxmat+ry[:,None]*uymat)/scale[:,None]/sqrtpoints
    jetjac=np.array([b*a0row+(a-2*A)*brow-6*erow,(b-3*h)*a0row+(a-4*A)*brow-3*a*hrow])*jetweight
    return np.vstack((J,jetjac))

# The seed-dependent right scaling changes coordinates, not equations.
pre=np.eye(null.shape[1])
singular=np.linalg.svd(full(zseed,True)@null,compute_uv=False)
if args.precondition:
    _,s,vt=np.linalg.svd(full(zseed,True)@null,full_matrices=False)
    pre=vt.T/np.maximum(s,s[0]*1e-6)
transform=null@pre
best=[float('inf'),0]

def save(z,name):
    np.savez_compressed(dest/(name+'.npz'),coefficients=z,radial=basis.N,angular=basis.M,exponent=basis.p,length=basis.L,cl=args.cl)
def fun(v):
    z=zseed+transform@v;f=full(z);norm=np.linalg.norm(f);best[1]+=1
    if norm<best[0]:
        best[0]=norm;save(z,'best')
        a=float(a0row@z);b=float(brow@z);e=float(erow@z);h=float(hrow@z)
        print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'evaluation':best[1],'norm':norm,'max_weighted':float(np.max(abs(f))),'a0':a,'K':float(krow@z),'c':float(crow@z),'b':b,'e':e,'H':h,'T1':(a-2*A)*b-6*e,'T2':(a-4*A)*b-3*a*h,'coefficient_norm':float(np.linalg.norm(z)),'seconds':time.time()-start}),flush=True)
    return f
def jac(v):return full(zseed+transform@v,True)@transform

# Meaningful derivative test of the complete quadratic residual before solving.
rng=np.random.default_rng(6021);direction=rng.normal(size=transform.shape[1]);direction/=np.linalg.norm(direction)
eps=1e-5;initial=np.zeros(transform.shape[1]);fd=(fun(eps*direction)-fun(-eps*direction))/(2*eps)
jerr=np.max(np.abs(fd-jac(initial)@direction))/max(1.,np.max(abs(fd)))
if jerr>1e-6:raise ArithmeticError('Jacobian cross-check failed: '+str(jerr))
metadata.update({'seed':seedmeta,'seed_fit_max_reduced_error':float(np.max(abs(fitvalue@zseed-fitseed))),'initial_jacobian_singular_values':singular.tolist(),'jacobian_FD_relative_error':float(jerr)})
(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n');save(zseed,'seed')
opt=least_squares(fun,initial,jac=jac,x_scale='jac',max_nfev=args.max_nfev,ftol=2e-12,xtol=2e-12,gtol=2e-12,verbose=0)
z=zseed+transform@opt.x;save(z,'final')
a=float(a0row@z);bv=float(brow@z);ev=float(erow@z);hv=float(hrow@z)
rhov=value@z;rx=gx@z;ry=gy@z;ux=uxmat@z;uy=uymat@z
tx=(args.cl*x+ux)*rx;ty=(args.cl*y+uy)*ry;R=tx+ty-rhov
nf=abs(tx)+abs(ty)+abs(rhov);nv=abs(rhov)+abs(x*rx+y*ry)+abs(ux*rx+uy*ry)
result={'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'solver_status':int(opt.status),'solver_message':opt.message,'nfev':opt.nfev,'cost':opt.cost,'optimality':opt.optimality,'cl':args.cl,'a0':a,'c':float(crow@z),'K':float(krow@z),'b':bv,'e':ev,'H':hv,'T1':(a-2*A)*bv-6*ev,'T2':(a-4*A)*bv-3*a*hv,'max_training_abs_R':float(np.max(abs(R))),'max_training_R_Nf':float(np.max(np.divide(abs(R),nf,out=np.zeros_like(R),where=nf>0))),'max_training_R_Nv':float(np.max(np.divide(abs(R),nv,out=np.zeros_like(R),where=nv>0))),'smallest_jacobian_singular_values':np.linalg.svd(full(z,True)@null,compute_uv=False)[-12:].tolist(),'max_coefficient':float(np.max(abs(z))),'scope':'Training samples only. No independent off-grid validation of this output yet. Finite-angular exactness excluded by theorem; only a refinement candidate.'}
(dest/'result.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(dest/'training_samples.npz',x=x,y=y,rho=rhov,rho_x=rx,rho_y=ry,U1=ux,U2=uy,R=R,Nf=nf,Nv=nv)
print(json.dumps(result,indent=2),flush=True)
