"""Own algebra and smooth compact-flow controls for packet156."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
root=Path(sys.argv[1]);params=json.loads((root/'inputs.json').read_text());start=time.monotonic();started=datetime.now(timezone.utc).isoformat()
rat=lambda x:sp.Rational(str(x));flt=lambda x:float(rat(x))
checks=[]
def ck(name,expression):
    v=sp.simplify(sp.expand(expression));checks.append({'name':name,'difference':str(v),'pass':v==0})
x,y,a,m1,m2=sp.symbols('x y a m1 m2',real=True)
F=sp.Function('F')(x);G=sp.Function('G')(x);chi=sp.Function('chi')(x)
Psi=2*x*y-4*G
# Symbolic G derivatives use G'=F/4.
def reduceG(e):
    for order in range(5,0,-1):e=e.subs(sp.diff(G,x,order),sp.diff(F,x,order-1)/4)
    return sp.simplify(e)
W=sp.Matrix([2*x-sp.diff(Psi,y),2*y+sp.diff(Psi,x)]);Om=-sp.diff(Psi,x,2)-sp.diff(Psi,y,2)
ck('core_W_horizontal',W[0]);ck('core_W_vertical',reduceG(W[1])-(4*y-F));ck('core_Omega',reduceG(Om)-sp.diff(F,x))
ck('core_T',reduceG(W.dot(sp.Matrix([sp.diff(F,x),0]))));ck('core_V',reduceG(W.dot(sp.Matrix([sp.diff(Om,x),sp.diff(Om,y)]))+Om-sp.diff(F,x)))
poly=2*x*y-a*x**3/3;op=-sp.diff(poly,x,2)-sp.diff(poly,y,2)
ck('center_strain',sp.diff(poly,x,y)-2);ck('center_q',sp.diff(op,x)-2*a);ck('center_temperature',a*x*x-a*x*x)
# General y-affine plateau across an endpoint, then the exact shear.
base=2*x*y*chi;g=F/4;aa=2*x*(1-chi);bb=4-sp.diff(aa,x)
newPsi=base+aa*g-4*G;newW=sp.Matrix([2*x-sp.diff(newPsi,y),2*y+sp.diff(newPsi,x)])
ck('shear_horizontal',newW[0]-aa);ck('shear_vertical',reduceG(newW[1])-(aa*sp.diff(g,x)+bb*(y-g)))
ck('shear_divergence',reduceG(sp.diff(newW[0],x)+sp.diff(newW[1],y))-4)
# Exterior defining PDE, recomputed solely by derivatives of Psi andTheta.
extPsi=2*m2*x/y;extTheta=a*m1**2*x*x/y**2
extOmega=-sp.diff(extPsi,x,2)-sp.diff(extPsi,y,2);extW=sp.Matrix([2*x-sp.diff(extPsi,y),2*y+sp.diff(extPsi,x)])
extf=sp.simplify(extW.dot(sp.Matrix([sp.diff(extOmega,x),sp.diff(extOmega,y)]))+extOmega-sp.diff(extTheta,x))
ck('exterior_Omega',extOmega+4*m2*x/y**3);ck('exterior_T',extW.dot(sp.Matrix([sp.diff(extTheta,x),sp.diff(extTheta,y)])));ck('exterior_f',extf-x*(12*m2/y**3+16*m2*m2/y**5-2*a*m1*m1/y**2))
cc=sp.symbols('c',positive=True);ck('exterior_leading',sp.limit(y*extf.subs(x,cc*y),y,sp.oo)+2*a*m1*m1*cc)
# General compact Hamiltonian differential identity, checked on a nontrivial polynomial.
hh=x*y*y+x**3*y+x**5;P=x*y+x**3+y*x**3
HH=sp.Matrix([-sp.diff(hh,y),sp.diff(hh,x)]);WW=sp.Matrix([2*x-sp.diff(P,y),2*y+sp.diff(P,x)]);z=sp.Matrix([x,y]);rhs=HH.jacobian(z)*WW-WW.jacobian(z)*HH;stream=WW.dot(sp.Matrix([sp.diff(hh,x),sp.diff(hh,y)]))-4*hh
for i,v in enumerate([-sp.diff(stream,y),sp.diff(stream,x)]):ck('compact_pushforward_stream_'+str(i),rhs[i]-v)
output={'started_utc':started,'exact_checks':checks,'runs':[],'scope':'Exact algebra and floating-point compact Hamiltonian flows. The numerical base polynomial for the flow controls is not a global admissible B2 field. Full-plane inverse preservation is proved analytically, not numerically certified here.'}
for order in params['quadrature_orders']:
    nodes,weights=leggauss(order);grid=(nodes+1)/2;dens=np.exp(-1/(grid*(1-grid)));norm=float(np.dot(weights/2,dens))
    def density(t):
        t=np.asarray(t);u=t*(1-t);out=np.zeros_like(t);sel=u>0;out[sel]=np.exp(-1/u[sel])/norm;return out
    def density_prime(t):
        t=np.asarray(t);u=t*(1-t);out=np.zeros_like(t);sel=u>0;out[sel]=density(t[sel])*(1-2*t[sel])/u[sel]**2;return out
    def integral(fun,lo,hi):
        if hi<=lo:return 0.
        tt=(lo+hi)/2+(hi-lo)/2*nodes;return float(np.dot((hi-lo)/2*weights,fun(tt)))
    low,high=[flt(q) for q in params['temperature_density_support']];a0=flt(params['a0']);mom={k:integral(lambda t:(low+(high-low)*t)**k*density(t),0,1) for k in [1,2,3]}
    def scalars(xx):
        r=abs(float(xx));t=float(np.clip((r-low)/(high-low),0,1));mass=integral(density,0,t)
        fm2=integral(lambda u:(low+(high-low)*u)**2*density(u),0,t);fm3=integral(lambda u:(low+(high-low)*u)**3*density(u),0,t)
        FF=a0*(fm2+r*r*(1-mass));GG=a0/4*(r*fm2-2*fm3/3+r**3*(1-mass)/3)
        return FF,np.copysign(GG,xx),2*a0*xx*(1-mass)
    def cutoff(xx,bounds):
        lo,hi=[flt(v) for v in bounds];r=abs(float(xx));t=float(np.clip((r-lo)/(hi-lo),0,1));val=1-integral(density,0,t)
        first=-float(density(np.array([t]))[0])/(hi-lo)*np.sign(xx);second=-float(density_prime(np.array([t]))[0])/(hi-lo)**2
        return val,first,second
    def hfields(z):
        xx,yy=z;FF,GG,FP=scalars(xx);kx,kxp,kxpp=cutoff(xx,params['x_cutoff']);ky,kyp,kypp=cutoff(yy,params['y_cutoff'])
        X=GG*kx;Xp=FF/4*kx+GG*kxp;Xpp=FP/4*kx+FF/2*kxp+GG*kxpp
        H=np.array([-X*kyp,Xp*ky]);DH=np.array([[-Xp*kyp,-X*kypp],[Xpp*ky,Xp*kyp]])
        return H,DH
    def flow(point,duration):
        def rhs(t,q):
            H,DH=hfields(q[:2]);return np.concatenate((H,(DH@q[2:].reshape(2,2)).ravel()))
        ini=np.concatenate((point,np.eye(2).ravel()));sol=solve_ivp(rhs,[0,duration],ini,method='DOP853',rtol=2e-11,atol=2e-12)
        if not sol.success:raise RuntimeError(sol.message)
        return sol.y[:2,-1],sol.y[2:,-1].reshape(2,2),sol.nfev
    rows=[]
    for pp in params['flow_points']:
        pt=np.array([flt(v) for v in pp]);end,Dphi,nfev=flow(pt,1);back,_,_=flow(end,-1);sym,_,_=flow(np.array([-pt[0],pt[1]]),1)
        row={'point':pt.tolist(),'end':end.tolist(),'determinant_error':float(abs(np.linalg.det(Dphi)-1)),'inverse_flow_error':float(np.max(abs(back-pt))),'reflection_error':float(np.max(abs(sym-np.array([-end[0],end[1]])))),'nfev':nfev}
        if abs(pt[0])<=flt(params['A'])+1 and abs(pt[1])<=flt(params['B']):
            FF,_,FP=scalars(pt[0]);exact=pt+np.array([0,FF/4]);Dexact=np.array([[1,0],[FP/4,1]])
            row['exact_shear_error']=float(np.max(abs(end-exact)));row['exact_shear_jacobian_error']=float(np.max(abs(Dphi-Dexact)))
        row['pass']=bool(row['determinant_error']<1e-8 and row['inverse_flow_error']<1e-8 and row['reflection_error']<1e-9 and row.get('exact_shear_error',0)<1e-9 and row.get('exact_shear_jacobian_error',0)<1e-9);rows.append(row)
    B0=flt(params['B']);bm1=integral(lambda t:B0*(1+t)*density(t),0,1);bm2=integral(lambda t:B0**2*(1+t)**2*density(t),0,1);c=flt(params['cone_slope']);exterior=[]
    for ys in params['radii']:
        yy=flt(ys);xx=c*yy;exact=xx*(12*bm2/yy**3+16*bm2**2/yy**5-2*a0*bm1**2/yy**2)
        exterior.append({'y':ys,'x':xx,'f':exact,'y_times_f':yy*exact,'negative_limit':-2*a0*bm1**2*c})
    run={'order':order,'temperature_moments':mom,'vertical_moments':{'m1':bm1,'m2':bm2},'flow_checks':rows,'exterior_checks':exterior,'pass':all(z['pass'] for z in rows) and exterior[-1]['f']<0}
    output['runs'].append(run);print(json.dumps({'order':order,'pass':run['pass'],'max_inverse_error':max(x['inverse_flow_error'] for x in rows),'max_det_error':max(x['determinant_error'] for x in rows),'last_exterior_yf':exterior[-1]['y_times_f']}),flush=True)
output.update(status='PASS' if all(x['pass'] for x in checks+output['runs']) else 'FAILED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(Path('research/156_beta2_local_pde_realization/PROOF.md').read_bytes()).hexdigest(),inputs_sha256=hashlib.sha256((root/'inputs.json').read_bytes()).hexdigest())
(root/'results.json').write_text(json.dumps(output,indent=2)+'\n');print(output['status'],len(checks),output['elapsed_seconds'],flush=True)
