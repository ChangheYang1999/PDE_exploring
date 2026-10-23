"""Independent smooth forced problem, with its actual source relation.

R=mu*y/(1+r*r/L**2)**2, mean dimensionless far-field b=beta.
Neither a0 nor c is fixed. This solves an auxiliary equation, not IPM.
"""
import argparse,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
from scipy.special import beta as beta_function,betainc
from smooth_basis import SmoothBasis,SmoothDensity
from kernel_basis import KernelBasis
from direct_inverse import Quadrature

ap=argparse.ArgumentParser()
ap.add_argument('--radial',type=int,default=12);ap.add_argument('--angular',type=int,default=8)
ap.add_argument('--cl',type=float,default=3.);ap.add_argument('--beta',type=float,default=1.)
ap.add_argument('--length',type=float,default=1.);ap.add_argument('--seed',default='linear')
ap.add_argument('--tag',default='forced_cl3_b1');ap.add_argument('--q',type=int,default=0)
ap.add_argument('--max-nfev',type=int,default=160);ap.add_argument('--jet-weight',type=float,default=1.)
ap.add_argument('--grid-radial',type=int);ap.add_argument('--grid-angular',type=int)
ap.add_argument('--precondition',action='store_true');args=ap.parse_args()
if args.cl<=1 or args.length<=0:raise ValueError('Need c_l>1 and L>0')
start=time.time();started=datetime.now(timezone.utc).isoformat()
dest=Path('evidence/smooth_solver')/args.tag;dest.mkdir(parents=True,exist_ok=True)
basis=SmoothBasis(args.radial,args.angular,1/args.cl,args.length)
nb=basis.size;A=2*args.cl-1
pad=lambda z:np.r_[z,0.]
a0row=pad(basis.center_slope());crow=pad(basis.center_strain());krow=pad(basis.axis_amplitude())
br,er=basis.cubic_density_rows();brow=pad(br);erow=pad(er);hrow=pad(basis.quartic_stream_difference())
murow=np.zeros(nb+1);murow[-1]=1
farrow=np.zeros(nb+1);farrow[:basis.N+1]=1
constraint=farrow[None,:]/np.linalg.norm(farrow)
target=np.array([args.beta/np.linalg.norm(farrow)])
zpart=np.linalg.lstsq(constraint,target,rcond=None)[0];null=null_space(constraint)
nr=args.grid_radial or (2*args.radial+3);nt=args.grid_angular or (2*args.angular+1)
t=-np.cos(np.pi*(np.arange(nr)+.5)/nr);u=(1-t)/2
r=args.length*np.sqrt(np.expm1(-np.log(u)/basis.a));r=np.maximum(r,args.length*.015)
th=(np.arange(nt)+.5)*np.pi/(2*nt)
x=(r[:,None]*np.cos(th)).reshape(-1);y=(r[:,None]*np.sin(th)).reshape(-1)
value,gx,gy=basis.evaluate(x,y,True);geom=basis.geometry(x,y);w,sigma=geom[4],geom[5]
scale=y*w*w*np.maximum(sigma,.02);forcing=y/(1+(np.hypot(x,y)/args.length)**2)**2
configs=[(24,128,96),(40,256,144),(64,512,224)];nq,ntq,neq=configs[args.q]
q=Quadrature(nq,ntq,neq,4.,args.length,basis.p,16*args.length,1/(1-basis.p))
metadata={'started_utc':started,'arguments':vars(args),'basis':basis.metadata(),'quadrature':q.__dict__,'point_count':len(x),'representation':'SmoothBasis with independently integrated Cartesian full-plane kernel','constraint':'mean dimensionless b(infinity)=beta; physical far amplitude mean=L^(1-p)*beta','equation':'R=mu*y*(1+r^2/L^2)^(-2), auxiliary forced problem; center equation a0*(c_l+c-1)=mu','scope':'No primary existence claim. All analytic Cartesian derivatives and canonical velocity matrices are this lane own code.'}
(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
cache_key=hashlib.sha256(json.dumps({'basis':basis.metadata(),'quadrature':q.__dict__,'r':r.tolist(),'th':th.tolist()},sort_keys=True).encode()).hexdigest()[:20]
cache=Path('evidence/smooth_solver')/('matrix_'+cache_key+'.npz')
if cache.exists():
    vv=np.load(cache);uxmat=vv['ux'];uymat=vv['uy']
    print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'load_matrix':str(cache)}),flush=True)
else:
    inv=KernelBasis(basis,q);uxmat=np.empty_like(value);uymat=np.empty_like(value)
    for j,(xx,yy) in enumerate(zip(x,y)):
        mm=inv.velocity_matrix(xx,yy);uxmat[j]=mm[0];uymat[j]=mm[1]
        if j%25==0:print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'matrix_row':j,'total':len(x),'seconds':time.time()-start}),flush=True)
    np.savez_compressed(cache,ux=uxmat,uy=uymat)
    print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'matrix_finished':str(cache),'seconds':time.time()-start}),flush=True)
value,gx,gy,uxmat,uymat=[np.column_stack((v,np.zeros(len(x)))) for v in (value,gx,gy,uxmat,uymat)]
D=args.cl*(x[:,None]*gx+y[:,None]*gy)-value-forcing[:,None]*murow
if args.seed=='linear':
    norm=beta_function(basis.a,2-basis.a)
    museed=2*args.cl*args.beta/norm
    seedrho=y*w*args.beta*betainc(basis.a,2-basis.a,sigma)/sigma**basis.a
    seedmeta={'type':'exact smooth solution of the linear forced transport equation','mu_linear':museed,'a0_linear':museed/(args.cl-1)}
else:
    old=np.load(args.seed,allow_pickle=False)
    ob=SmoothBasis(int(old['radial']),int(old['angular']),float(old['exponent']),float(old['length']))
    seedrho=SmoothDensity(ob,old['coefficients']).rho(x,y)
    museed=float(old['mu']) if 'mu' in old.files else 0.
    seedmeta={'source':args.seed,'type':'own smooth coefficients','seed_mu':museed}
fitvalue=value/(y*w)[:,None];fitseed=seedrho/(y*w)
yseed=np.linalg.lstsq(fitvalue@null,fitseed-fitvalue@zpart,rcond=1e-11)[0]
zseed=zpart+null@yseed;zseed[-1]=museed
a_scale=max(abs(a0row@zseed),1.);jetweights=args.jet_weight/np.array([a_scale,a_scale*a_scale,a_scale*a_scale])
sqrtpoints=np.sqrt(len(x))

def jet_data(z,jac=False):
    a=a0row@z;b=brow@z;e=erow@z;h=hrow@z;mu=z[-1];delta=args.cl+crow@z-1
    jets=np.array([a*delta-mu,(a-2*A+delta)*b-3*(2+3*delta)*e-8*mu/args.length**2,(a-4*A+2*delta)*b-3*a*h-4*mu/args.length**2])
    if not jac:return jets
    return np.array([delta*a0row+a*crow-murow,b*a0row+(b-9*e)*crow+(a-2*A+delta)*brow-3*(2+3*delta)*erow-8*murow/args.length**2,(b-3*h)*a0row+2*b*crow+(a-4*A+2*delta)*brow-3*a*hrow-4*murow/args.length**2])

def full(z,jac=False):
    ux=uxmat@z;uy=uymat@z;rx=gx@z;ry=gy@z
    raw=D@z+ux*rx+uy*ry
    if not jac:return np.r_[raw/scale/sqrtpoints,jet_data(z)*jetweights]
    J=(D+ux[:,None]*gx+uy[:,None]*gy+rx[:,None]*uxmat+ry[:,None]*uymat)/scale[:,None]/sqrtpoints
    return np.vstack((J,jet_data(z,True)*jetweights[:,None]))

pre=np.eye(null.shape[1]);singular=np.linalg.svd(full(zseed,True)@null,compute_uv=False)
if args.precondition:
    _,s,vt=np.linalg.svd(full(zseed,True)@null,full_matrices=False);pre=vt.T/np.maximum(s,s[0]*1e-6)
transform=null@pre;best=[float('inf'),0]
def save(z,name):
    np.savez_compressed(dest/(name+'.npz'),coefficients=z[:nb],radial=basis.N,angular=basis.M,exponent=basis.p,length=basis.L,cl=args.cl,mu=z[-1],beta=args.beta)
def fun(v):
    z=zseed+transform@v;f=full(z);norm=np.linalg.norm(f);best[1]+=1
    if norm<best[0]:
        best[0]=norm;save(z,'best')
        print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'evaluation':best[1],'norm':norm,'max_weighted':float(np.max(abs(f))),'a0':float(a0row@z),'c':float(crow@z),'Delta':float(args.cl+crow@z-1),'mu':float(z[-1]),'K':float(krow@z),'center_jets':jet_data(z).tolist(),'coefficient_norm':float(np.linalg.norm(z[:nb])),'seconds':time.time()-start}),flush=True)
    return f
def jac(v):return full(zseed+transform@v,True)@transform
rng=np.random.default_rng(6022);direction=rng.normal(size=transform.shape[1]);direction/=np.linalg.norm(direction)
eps=1e-5;initial=np.zeros(transform.shape[1]);fd=(fun(eps*direction)-fun(-eps*direction))/(2*eps)
jerr=np.max(np.abs(fd-jac(initial)@direction))/max(1.,np.max(abs(fd)))
if jerr>1e-6:raise ArithmeticError('Complete forced Jacobian cross-check failed: '+str(jerr))
metadata.update({'seed':seedmeta,'seed_fit_max_reduced_error':float(np.max(abs(fitvalue@zseed-fitseed))),'initial_jacobian_singular_values':singular.tolist(),'jacobian_FD_relative_error':float(jerr)})
(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n');save(zseed,'seed')
opt=least_squares(fun,initial,jac=jac,x_scale='jac',max_nfev=args.max_nfev,ftol=2e-12,xtol=2e-12,gtol=2e-12)
z=zseed+transform@opt.x;save(z,'final')
rhov=value@z;rx=gx@z;ry=gy@z;ux=uxmat@z;uy=uymat@z
termx=(args.cl*x+ux)*rx;termy=(args.cl*y+uy)*ry;R=termx+termy-rhov;Rf=R-z[-1]*forcing
nf=abs(termx)+abs(termy)+abs(rhov);nv=abs(rhov)+abs(x*rx+y*ry)+abs(ux*rx+uy*ry)
result={'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'solver_status':int(opt.status),'solver_message':opt.message,'nfev':opt.nfev,'cost':opt.cost,'optimality':opt.optimality,'cl':args.cl,'beta':args.beta,'mu':float(z[-1]),'a0':float(a0row@z),'c':float(crow@z),'Delta':float(args.cl+crow@z-1),'source_eigenvalues':[float(args.cl-crow@z),float(args.cl+crow@z)],'K':float(krow@z),'center_jets':jet_data(z).tolist(),'max_training_abs_R':float(np.max(abs(R))),'max_training_abs_Rforced':float(np.max(abs(Rf))),'max_training_Rforced_Nf':float(np.max(np.divide(abs(Rf),nf,out=np.zeros_like(Rf),where=nf>0))),'max_training_Rforced_Nv':float(np.max(np.divide(abs(Rf),nv,out=np.zeros_like(Rf),where=nv>0))),'smallest_jacobian_singular_values':np.linalg.svd(full(z,True)@null,compute_uv=False)[-12:].tolist(),'max_coefficient':float(np.max(abs(z[:nb]))),'scope':'Auxiliary forced equation, training data only, off-grid verification pending. Mu is not zero by construction.'}
(dest/'result.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(dest/'training_samples.npz',x=x,y=y,rho=rhov,rho_x=rx,rho_y=ry,U1=ux,U2=uy,R=R,Rforced=Rf,Nf=nf,Nv=nv)
print(json.dumps(result,indent=2),flush=True)
