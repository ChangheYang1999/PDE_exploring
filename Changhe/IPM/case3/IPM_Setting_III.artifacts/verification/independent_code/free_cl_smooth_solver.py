"""Independent bounded free-c_l search in the Cartesian-smooth basis.

The density exponent is p=1/c_l at every trial. A Chebyshev surrogate in p
accelerates the direct Cartesian inverse during optimization. The final
training inverse is rebuilt at the actual p, and separate scalar/FD8 off-grid
evaluation is still required. No numerical velocity or strain is a free field.
"""
import argparse, hashlib, json, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.linalg import qr
from scipy.optimize import least_squares
from smooth_basis import SmoothBasis, SmoothDensity
from kernel_basis import KernelBasis
from direct_inverse import Quadrature
from candidate_reader import Candidate


def utc(): return datetime.now(timezone.utc).isoformat()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--radial',type=int,default=12)
    ap.add_argument('--angular',type=int,default=8)
    ap.add_argument('--cl',type=float,default=3.066481857503252)
    ap.add_argument('--cl-min',type=float,default=2.5)
    ap.add_argument('--cl-max',type=float,default=3.8)
    ap.add_argument('--nodes',type=int,default=13)
    ap.add_argument('--q',type=int,default=0)
    ap.add_argument('--seed',default='evidence/smooth_solver/smooth_first/final.npz')
    ap.add_argument('--tag',default='free_cl_first')
    ap.add_argument('--max-nfev',type=int,default=250)
    ap.add_argument('--jet-weight',type=float,default=1.)
    ap.add_argument('--grid-radial',type=int)
    ap.add_argument('--diagnose-only',action='store_true')
    ap.add_argument('--grid-angular',type=int)
    args=ap.parse_args()
    if not 1<args.cl_min<args.cl<args.cl_max: raise ValueError('Need 1<cl_min<cl<cl_max')
    if args.nodes<5: raise ValueError('At least five interpolation nodes')
    start=time.time();dest=Path('evidence/smooth_solver')/args.tag;dest.mkdir(parents=True,exist_ok=True)
    pmin,pmax=1/args.cl_max,1/args.cl_min;p0=1/args.cl
    pc=(pmin+pmax)/2;ps=(pmax-pmin)/2
    basis0=SmoothBasis(args.radial,args.angular,p0,1.)
    size=basis0.size
    nr=args.grid_radial or 2*args.radial+3;nt=args.grid_angular or 2*args.angular+1
    t=-np.cos(np.pi*(np.arange(nr)+.5)/nr);w=(1-t)/2
    r=np.maximum(np.sqrt(np.expm1(-np.log(w)/basis0.a)),.015)
    theta=(np.arange(nt)+.5)*np.pi/(2*nt)
    x=(r[:,None]*np.cos(theta)).ravel();y=(r[:,None]*np.sin(theta)).ravel()
    geom=basis0.geometry(x,y);w0,sigma=geom[4],geom[5]
    scale=y*w0*w0*np.maximum(sigma,.02);sqrtpoints=np.sqrt(len(x))
    config=[(24,128,96),(40,256,144),(64,512,224)][args.q]
    def basis(p):return SmoothBasis(args.radial,args.angular,p,1.)
    def quadrature(p):return Quadrature(*config,4.,1.,p,16.,1/(1-p))
    def matrix_at(p,queries=None):
        b=basis(p);q=quadrature(p)
        query=np.column_stack((x,y)) if queries is None else np.asarray(queries,float)
        key=hashlib.sha256(json.dumps({'basis':b.metadata(),'q':q.__dict__,'query':query.tolist()},sort_keys=True).encode()).hexdigest()[:24]
        cache=Path('evidence/smooth_solver')/('free_cl_matrix_'+key+'.npz')
        if cache.exists():
            with np.load(cache,allow_pickle=False) as f:return np.array(f['velocity'])
        inv=KernelBasis(b,q);out=np.empty((len(query),2,size))
        for i,(xx,yy) in enumerate(query):out[i]=inv.velocity_matrix(xx,yy)
        if queries is None:np.savez_compressed(cache,velocity=out)
        return out
    nodes=np.cos(np.pi*np.arange(args.nodes)/(args.nodes-1))
    pnodes=pc+ps*nodes
    meta={'started_utc':utc(),'arguments':vars(args),'point_count':len(x),'physical_radius_min':float(r.min()),'physical_radius_max':float(r.max()),'p_bounds':[pmin,pmax], 'inverse_method':'Own Cartesian PV/contact kernel, tail to infinity; Chebyshev interpolation in p only during optimization; true matrix rebuilt at final p','constraints':'canonical c=1-c_l; K=a0 (primary reporting scale L_can=1 if a0!=0); neither c_l nor a0 prescribed','scope':'Restricted parameter interval and finite smooth basis. No global search, numerical existence, or nonexistence claim.'}
    (dest/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    mats=[]
    for i,p in enumerate(pnodes):
        mats.append(matrix_at(float(p)))
        print(json.dumps({'utc':utc(),'matrix_node':i,'nodes':args.nodes,'p':float(p),'seconds':time.time()-start}),flush=True)
    array=np.asarray(mats);shape=array.shape[1:]
    coefficients=np.linalg.solve(C.chebvander(nodes,args.nodes-1),array.reshape(args.nodes,-1)).reshape((args.nodes,)+shape)
    del array,mats
    def velocity_matrix(p):return C.chebval((p-pc)/ps,coefficients)
    # Off-node tests use fresh inverse integration, not interpolation nodes.
    sample=np.array([0,len(x)//5,len(x)//2,4*len(x)//5,len(x)-1])
    checks=[]
    for fraction in (.173,.619):
        p=pmin+fraction*(pmax-pmin);direct=matrix_at(p,np.column_stack((x[sample],y[sample])))
        interp=velocity_matrix(p)[sample];difference=abs(interp-direct)
        checks.append({'p':p,'query_indices':sample.tolist(),'max_absolute_matrix_difference':float(difference.max()),'relative_to_max_matrix':float(difference.max()/max(1.,abs(direct).max()))})
    arow=basis0.center_slope();grow=basis0.axis_amplitude()-arow
    center0=np.array([basis0.center_strain(),grow])
    _,_,permutation=qr(center0,pivoting=True,mode='economic');piv=np.asarray(permutation[:2]);free=np.asarray(permutation[2:])
    def expand(zfree,p,with_map=False):
        b=basis(p);constraint=np.array([b.center_strain(),grow]);cp=constraint[:,piv]
        z=np.empty(size);z[free]=zfree;z[piv]=np.linalg.solve(cp,np.array([1-1/p,0.])-constraint[:,free]@zfree)
        if not with_map:return z,b
        transform=np.zeros((size,len(free)));transform[free]=np.eye(len(free));transform[piv]=-np.linalg.solve(cp,constraint[:,free])
        return z,b,transform
    seedfile=np.load(args.seed,allow_pickle=False)
    own='coefficients' in seedfile.files
    if own:
        sb=SmoothBasis(int(seedfile['radial']),int(seedfile['angular']),float(seedfile['exponent']),float(seedfile['length']))
        srho=SmoothDensity(sb,seedfile['coefficients']).rho(x,y)
        source_coeff=np.array(seedfile['coefficients']).reshape(sb.M,sb.N+1)
        seedmeta={'source':args.seed,'own_smooth_seed':True,'source_cl':float(seedfile['cl'])}
    else:
        seedfile.close();candidate=Candidate(args.seed,project_center=True)
        endpoint=C.chebval(1,candidate.coefficients)-candidate.endpoint_modes
        sa=float(C.chebval(-1,candidate.coefficients)[0]);sk=candidate.meta['L']**(1-candidate.meta['gamma'])*float(endpoint@((-1.)**np.arange(candidate.meta['M'])))
        if sk/sa<=0:raise ValueError('Raw seed is outside K/a0 positive scale chart')
        length=(sk/sa)**(1/(1-candidate.meta['gamma']));lam=1/length
        srho=lam*candidate.rho(x/lam,y/lam)
        seedmeta={'source':args.seed,'rescaling_lambda':lam,'source_a0':sa,'source_K':sk}
    seedfile.close()
    part,_,transform=expand(np.zeros(len(free)),p0,True)
    value0=basis0.evaluate(x,y);fit=value0/(y*w0)[:,None]
    if own:
        # Transfer coefficients in their analytic compactified coordinates.
        # A least-squares shape fit at a different p can create enormous canceling
        # coefficients in the enlarged angular basis and spoil the Jacobian.
        transfer=np.zeros((basis0.M,basis0.N+1))
        km=min(basis0.M,sb.M);jn=min(basis0.N,sb.N)+1
        transfer[:km,:jn]=source_coeff[:km,:jn]
        zfree=transfer.reshape(-1)[free]
        seedmeta['transfer']='Pad/truncate scalar density coefficients, then solve the two center/scale constraints at the trial p; shape is allowed to change'
    else:
        zfree=np.linalg.lstsq(fit@transform,srho/(y*w0)-fit@part,rcond=1e-11)[0]
    seed,_,_=expand(zfree,p0,True)
    jetscale=max(1.,abs(arow@seed))**2;jetweight=args.jet_weight/jetscale
    def full(v,need_jac=False,actual_velocity=None):
        p=float(v[-1]);ell=1/p;A=2*ell-1
        z,b,transform=expand(v[:-1],p,True)
        values,gx,gy=b.evaluate(x,y,True)
        mm=velocity_matrix(p) if actual_velocity is None else actual_velocity
        uxmat,uymat=mm[:,0,:],mm[:,1,:]
        ux,uy=uxmat@z,uymat@z;rx,ry=gx@z,gy@z
        D=ell*(x[:,None]*gx+y[:,None]*gy)-values
        residual=D@z+ux*rx+uy*ry
        br,er=b.cubic_density_rows();hr=b.quartic_stream_difference()
        a=arow@z;bv=br@z;ev=er@z;hv=hr@z
        jets=np.array([(a-2*A)*bv-6*ev,(a-4*A)*bv-3*a*hv])
        f=np.r_[residual/scale/sqrtpoints,jets*jetweight]
        if not need_jac:return f
        J=(D+ux[:,None]*gx+uy[:,None]*gy+rx[:,None]*uxmat+ry[:,None]*uymat)/scale[:,None]/sqrtpoints
        JJ=np.array([bv*arow+(a-2*A)*br-6*er,(bv-3*hv)*arow+(a-4*A)*br-3*a*hr])*jetweight
        coefficient_jac=np.vstack((J,JJ))@transform
        # Center elimination, p-dependent basis and inverse interpolation all vary.
        step=1e-5*min(p-pmin,pmax-p,(pmax-pmin)/10)
        step=max(step,1e-9)
        vp=v.copy();vm=v.copy();vp[-1]+=step;vm[-1]-=step
        pcolumn=(full(vp)-full(vm))/(2*step)
        return np.column_stack((coefficient_jac,pcolumn))
    initial=np.r_[zfree,p0]
    rng=np.random.default_rng(6120);direction=rng.normal(size=len(initial));direction[-1]*=ps;direction/=np.linalg.norm(direction)
    analytic_direction=full(initial,True)@direction
    checks_jac=[]
    for eps in (1e-3,3e-4,1e-4,3e-5,1e-5):
        difference=(full(initial+eps*direction)-full(initial-eps*direction))/(2*eps)
        error=abs(difference-analytic_direction)
        checks_jac.append({'step':eps,'relative_error':float(error.max()/max(1.,abs(difference).max())),'max_difference':float(abs(difference).max()),'worst_row':int(np.argmax(error))})
    jacerr=checks_jac[-1]['relative_error']
    diagnostic={'utc':utc(),'seed_coeff_max':float(abs(seed).max()),'seed_free_max':float(abs(zfree).max()),'seed_f_max':float(abs(full(initial)).max()),'direction_norm':float(np.linalg.norm(direction)),'p_direction':float(direction[-1]),'checks':checks_jac,'surrogate_checks':checks}
    (dest/'jacobian_diagnostic.json').write_text(json.dumps(diagnostic,indent=2)+'\n')
    print(json.dumps(diagnostic),flush=True)
    if args.diagnose_only:return
    if jacerr>3e-6:raise ArithmeticError('Full parameterized Jacobian check failed '+str(jacerr))
    meta.update({'seed':seedmeta,'surrogate_checks':checks,'jacobian_FD_relative_error':jacerr,'eliminated_coefficient_indices':piv.tolist(),'seed_fit_max_reduced_error':float(np.max(abs(fit@seed-srho/(y*w0))))})
    (dest/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    def save(v,name):
        z,b=expand(v[:-1],float(v[-1]));np.savez_compressed(dest/(name+'.npz'),coefficients=z,radial=b.N,angular=b.M,exponent=b.p,length=b.L,cl=1/b.p)
    best=[float('inf'),0]
    def fun(v):
        f=full(v);norm=float(np.linalg.norm(f));best[1]+=1
        if norm<best[0]:
            best[0]=norm;save(v,'best');z,b=expand(v[:-1],float(v[-1]))
            print(json.dumps({'utc':utc(),'evaluation':best[1],'norm':norm,'max_weighted':float(abs(f).max()),'cl':1/b.p,'a0':float(arow@z),'c':float(b.center_strain()@z),'K':float(b.axis_amplitude()@z),'seconds':time.time()-start}),flush=True)
        return f
    save(initial,'seed')
    lower=np.r_[np.full(len(free),-np.inf),pmin];upper=np.r_[np.full(len(free),np.inf),pmax]
    opt=least_squares(fun,initial,jac=lambda v:full(v,True),bounds=(lower,upper),x_scale='jac',max_nfev=args.max_nfev,ftol=2e-12,xtol=2e-12,gtol=2e-12)
    save(opt.x,'final');z,b=expand(opt.x[:-1],float(opt.x[-1]));ell=1/b.p;A=2*ell-1
    actual=matrix_at(b.p);approx=velocity_matrix(b.p)
    values,gx,gy=b.evaluate(x,y,True);rho=values@z;rx=gx@z;ry=gy@z;ux=actual[:,0]@z;uy=actual[:,1]@z
    tx=(ell*x+ux)*rx;ty=(ell*y+uy)*ry;R=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*rx+y*ry)+abs(ux*rx+uy*ry)
    br,er=b.cubic_density_rows();hr=b.quartic_stream_difference();a=float(arow@z);bv=float(br@z);ev=float(er@z);hv=float(hr@z)
    result={'finished_utc':utc(),'elapsed_seconds':time.time()-start,'solver_status':int(opt.status),'solver_message':opt.message,'nfev':int(opt.nfev),'cost':float(opt.cost),'optimality':float(opt.optimality),'cl':ell,'a0':a,'c':float(b.center_strain()@z),'K':float(b.axis_amplitude()@z),'b':bv,'e':ev,'H':hv,'T1':(a-2*A)*bv-6*ev,'T2':(a-4*A)*bv-3*a*hv,'max_training_abs_R':float(abs(R).max()),'max_training_R_Nf':float(np.max(np.divide(abs(R),nf,out=np.zeros_like(R),where=nf>0))),'max_training_R_Nv':float(np.max(np.divide(abs(R),nv,out=np.zeros_like(R),where=nv>0))),'final_surrogate_matrix_abs_error':float(abs(actual-approx).max()),'final_surrogate_velocity_abs_error':float(abs(np.einsum('ijk,k->ij',actual-approx,z)).max()),'actual_q_training_weighted_norm':float(np.linalg.norm(full(opt.x,actual_velocity=actual))),'parameter_bound_distance':float(min(b.p-pmin,pmax-b.p)),'smallest_parameterized_jacobian_singular_values':np.linalg.svd(full(opt.x,True),compute_uv=False)[-12:].tolist(),'scope':'Final training data use a rebuilt direct inverse at the final p. Off-grid scalar reconstruction, different differentiation, and quadrature refinement remain necessary. The bounded c_l interval is an experimental restriction.'}
    (dest/'result.json').write_text(json.dumps(result,indent=2)+'\n');np.savez_compressed(dest/'training_samples.npz',x=x,y=y,rho=rho,rho_x=rx,rho_y=ry,U1=ux,U2=uy,R=R,Nf=nf,Nv=nv)
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
