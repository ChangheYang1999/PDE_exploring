"""Fixed-ell secondary y^3 experiment. Not a primary candidate or a theorem."""
import argparse,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
from secondary_basis import SecondaryBasis
from smooth_basis import SmoothDensity
from kernel_basis import KernelBasis
from direct_inverse import Quadrature

def utc():return datetime.now(timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cl',type=float,default=2.)
    ap.add_argument('--radial',type=int,default=10);ap.add_argument('--angular',type=int,default=8)
    ap.add_argument('--q',type=int,default=0);ap.add_argument('--max-nfev',type=int,default=160)
    ap.add_argument('--tag',required=True);ap.add_argument('--seed');args=ap.parse_args()
    if args.cl<=1:raise ValueError('ell must exceed one')
    start=time.time();dest=Path('evidence/secondary_solver')/args.tag;dest.mkdir(parents=True,exist_ok=True)
    b=SecondaryBasis(args.radial,args.angular,1/args.cl,1.)
    crow=b.center_strain();erow=b.cubic_axis_row();krow=b.axis_amplitude();hr=b.quartic_stream_difference();fr,gr=b.fifth_density_rows()
    lamx=2*args.cl-1/3
    constraints=np.array([crow,krow-erow]);target=np.array([1/3-args.cl,0.])
    norm=np.linalg.norm(constraints,axis=1);constraints/=norm[:,None];target/=norm
    part=np.linalg.lstsq(constraints,target,rcond=None)[0];null=null_space(constraints)
    nr=2*b.N+3;nt=2*b.M+1;t=-np.cos(np.pi*(np.arange(nr)+.5)/nr);w=(1-t)/2
    r=np.maximum(np.sqrt(np.expm1(-np.log(w)/b.a)),.02)
    theta=(np.arange(nt)+.5)*np.pi/(2*nt)
    x=(r[:,None]*np.cos(theta)).ravel();y=(r[:,None]*np.sin(theta)).ravel()
    val,gx,gy=b.evaluate(x,y,True);geom=b.geometry(x,y);ww,sig=geom[4],geom[5]
    factor=y*y/(1+x*x+y*y);scale=y*ww*ww*factor*np.maximum(sig,.03);sqrtpoints=np.sqrt(len(x))
    config=[(24,128,96),(40,256,144),(64,512,224)][args.q]
    q=Quadrature(*config,4.,1.,b.p,16.,1/(1-b.p))
    key=hashlib.sha256(json.dumps({'basis':b.metadata(),'q':q.__dict__,'x':x.tolist(),'y':y.tolist()},sort_keys=True).encode()).hexdigest()[:24]
    cache=Path('evidence/secondary_solver')/('matrix_'+key+'.npz')
    if cache.exists():
        with np.load(cache,allow_pickle=False) as dd:mm=np.array(dd['velocity'])
    else:
        inv=KernelBasis(b,q);mm=np.empty((len(x),2,b.size))
        for j,(xx,yy) in enumerate(zip(x,y)):
            mm[j]=inv.velocity_matrix(xx,yy)
            if j%50==0:print(json.dumps({'utc':utc(),'matrix_row':j,'total':len(x),'seconds':time.time()-start}),flush=True)
        np.savez_compressed(cache,velocity=mm)
    uxmat,uymat=mm[:,0],mm[:,1]
    # This simple y^3 seed already has the required strain and reporting scale.
    zsimple=np.zeros(b.size);zsimple[0]=4*(1-b.p)*(args.cl-1/3)
    seedmeta={'type':'single smooth cubic-axis mode','coefficient':float(zsimple[0])}
    if args.seed:
        with np.load(args.seed,allow_pickle=False) as dd:
            if int(dd['axis_order'])!=3:raise ValueError('Secondary seed required')
            old=SecondaryBasis(int(dd['radial']),int(dd['angular']),float(dd['exponent']),float(dd['length']))
            rr=SmoothDensity(old,dd['coefficients']).rho(x,y)
        fit=val/(y*ww*factor)[:,None]
        zfree=np.linalg.lstsq(fit@null,rr/(y*ww*factor)-fit@part,rcond=1e-11)[0]
        seedmeta={'type':'own secondary checkpoint','source':args.seed}
    else:zfree=np.linalg.lstsq(null,zsimple-part,rcond=None)[0]
    zseed=part+null@zfree;D=args.cl*(x[:,None]*gx+y[:,None]*gy)-val
    jetweight=1/max(1.,abs(erow@zseed))**2
    def full(z,jac=False):
        ux=uxmat@z;uy=uymat@z;rx=gx@z;ry=gy@z
        e=float(erow@z);f=float(fr@z);g=float(gr@z);H=float(hr@z)
        jets=np.array([2*lamx*f+4.5*e*H,(2/3)*g-1.5*e*H])
        if not jac:return np.r_[(D@z+ux*rx+uy*ry)/scale/sqrtpoints,jets*jetweight]
        J=(D+ux[:,None]*gx+uy[:,None]*gy+rx[:,None]*uxmat+ry[:,None]*uymat)/scale[:,None]/sqrtpoints
        JJ=np.array([2*lamx*fr+4.5*(H*erow+e*hr),(2/3)*gr-1.5*(H*erow+e*hr)])
        return np.vstack((J,JJ*jetweight))
    metadata={'started_utc':utc(),'arguments':vars(args),'basis':b.metadata(),'quadrature':q.__dict__,'seed':seedmeta,'point_count':len(x),'scope':'SECONDARY m=3, fixed-ell experiment, global y^3 factor. c=1/3-ell and K=e3. Not a primary candidate, full-class parameterization, or numerical endpoint.'}
    rng=np.random.default_rng(331);v=rng.normal(size=null.shape[1]);v/=np.linalg.norm(v);eps=1e-5
    fd=(full(zseed+eps*(null@v))-full(zseed-eps*(null@v)))/(2*eps)
    jerr=float(max(abs(fd-full(zseed,True)@(null@v)))/max(1.,max(abs(fd))))
    if jerr>2e-6:raise ArithmeticError('Secondary residual Jacobian '+str(jerr))
    metadata['Jacobian_FD_relative_error']=jerr;(dest/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    def save(z,name):np.savez_compressed(dest/(name+'.npz'),coefficients=z,radial=b.N,angular=b.M,exponent=b.p,length=b.L,cl=args.cl,axis_order=3)
    best=[float('inf'),0]
    def fun(v):
        z=zseed+null@v;f=full(z);value=float(np.linalg.norm(f));best[1]+=1
        if value<best[0]:
            best[0]=value;save(z,'best')
            print(json.dumps({'utc':utc(),'evaluation':best[1],'norm':value,'e3':float(erow@z),'K':float(krow@z),'c':float(crow@z),'seconds':time.time()-start}),flush=True)
        return f
    save(zseed,'seed')
    opt=least_squares(fun,np.zeros(null.shape[1]),jac=lambda v:full(zseed+null@v,True)@null,x_scale='jac',max_nfev=args.max_nfev,ftol=2e-12,xtol=2e-12,gtol=2e-12)
    z=zseed+null@opt.x;save(z,'final')
    rho=val@z;rx=gx@z;ry=gy@z;ux=uxmat@z;uy=uymat@z
    tx=(args.cl*x+ux)*rx;ty=(args.cl*y+uy)*ry;R=tx+ty-rho
    nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*rx+y*ry)+abs(ux*rx+uy*ry)
    e=float(erow@z);f=float(fr@z);g=float(gr@z);H=float(hr@z)
    result={'finished_utc':utc(),'elapsed_seconds':time.time()-start,'status':int(opt.status),'message':opt.message,'nfev':int(opt.nfev),'cl':args.cl,'a0':0.,'e3':e,'K':float(krow@z),'c':float(crow@z),'H':H,'f':f,'g':g,'T5x':2*lamx*f+4.5*e*H,'T5y':2*g/3-1.5*e*H,'max_training_abs_R':float(max(abs(R))),'max_training_R_Nf':float(max(abs(R)/nf)),'max_training_R_Nv':float(max(abs(R)/nv)),'smallest_coordinate_singular_values':np.linalg.svd(full(z,True)@null,compute_uv=False)[-8:].tolist(),'scope':metadata['scope']+' Training data only, independent scalar evaluation pending.'}
    (dest/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
