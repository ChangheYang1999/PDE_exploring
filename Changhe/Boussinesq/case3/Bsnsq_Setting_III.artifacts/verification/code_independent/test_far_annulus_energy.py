"""Independent smooth-flow controls for research155. No numerical B2 claim."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss

root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
started=datetime.now(timezone.utc).isoformat();start=time.monotonic()
params=json.loads((root/'inputs.json').read_text())
exact=[]
def check(name,expr):
    z=sp.simplify(expr);exact.append({'name':name,'difference':str(z),'pass':z==0})
x,y,b=sp.symbols('x y beta',real=True)
h=x*y**2+x**3*y+x**5
H=sp.Matrix([-sp.diff(h,y),sp.diff(h,x)]);z=sp.Matrix([x,y]);B=b*(H.jacobian(z)*z-H)
Lh=b*(x*sp.diff(h,x)+y*sp.diff(h,y)-2*h)
for i in range(2):check('hamiltonian_dilation_'+str(i),B[i]-sp.Matrix([-sp.diff(Lh,y),sp.diff(Lh,x)])[i])
check('divergence_H',sp.diff(H[0],x)+sp.diff(H[1],y))
check('divergence_B',sp.diff(B[0],x)+sp.diff(B[1],y))
s=sp.symbols('s',positive=True);r=sp.symbols('r',positive=True)
check('vorticity_homogeneity',r*sp.diff(r**(-s),r)+s*r**(-s))
check('potential_exponent',(1-s)+(1-2*s)+2-(4-3*s))
check('kinetic_exponent',2*(1-s)+2-(4-2*s))
check('negative_optimum',(-sp.Symbol('A')/sp.Symbol('D'))*sp.Symbol('A')+(-sp.Symbol('A')/sp.Symbol('D'))**2*sp.Symbol('D')/2+sp.Symbol('A')**2/(2*sp.Symbol('D')))
check('coefficient',b*(4-1/b)-(4*b-1))

def shape(z,s,eta):
    xx,yy=z;rad=np.hypot(xx,yy);er=z/rad;et=np.vstack((-er[1],er[0]));theta=np.arctan2(yy,xx)
    t=(rad-1.5)/.4;u=1-t*t;chi=np.zeros_like(rad);cp=chi.copy();cpp=chi.copy();mask=u>1e-8
    um=u[mask];tm=t[mask];chi[mask]=np.exp(1-1/um)
    lp=-2*tm/(.4*um**2);lpp=-2/(.4**2*um**2)-8*tm**2/(.4**2*um**3)
    cp[mask]=chi[mask]*lp;cpp[mask]=chi[mask]*(lp*lp+lpp)
    F=chi*rad**(-s);Fp=rad**(-s)*(cp-s*chi/rad);Fpp=rad**(-s)*(cpp-2*s*cp/rad+s*(s+1)*chi/rad**2)
    p=2-s;aa=p*p-1;bb=(4-p*p)*eta/2
    g=aa*np.cos(theta)+bb*np.sin(2*theta);gp=-aa*np.sin(theta)+2*bb*np.cos(2*theta);gpp=-aa*np.cos(theta)-4*bb*np.sin(2*theta)
    grad=er*(Fp*g)+et*(F*gp/rad)
    rr=Fpp*g;rt=(Fp/rad-F/rad**2)*gp;tt=Fp*g/rad+F*gpp/rad**2
    hxx=rr*er[0]**2+2*rt*er[0]*et[0]+tt*et[0]**2
    hxy=rr*er[0]*er[1]+rt*(er[0]*et[1]+et[0]*er[1])+tt*et[0]*et[1]
    hyy=rr*er[1]**2+2*rt*er[1]*et[1]+tt*et[1]**2
    vec=np.vstack((-grad[1],grad[0]));jac=np.array([[-hxy,-hyy],[hxx,hxy]])
    return {'h':F*g,'H':vec,'DH':jac,'omega':rad**(-s)*g,'chi':chi,'er':er,'et':et,'r':rad,'theta':theta,'Fp':Fp,'F':F,'Fpp':Fpp,'g':g,'gp':gp}

def full_fields(z,R,s,eta):
    xx,yy=R*z;ww=1+xx*xx+yy*yy;k=(1-s)/2;l=-s/2
    px=1-ww**k-2*k*xx*xx*ww**(k-1)+eta*yy*ww**l+2*eta*l*xx*xx*yy*ww**(l-1)
    py=-2*k*xx*yy*ww**(k-1)+eta*xx*ww**l+2*eta*l*xx*yy*yy*ww**(l-1)
    vel=np.vstack((-py,px))*R**(s-1)
    temp=xx*xx*ww**(-(1+2*s)/2)*(1+.2*yy/np.sqrt(ww))*R**(-(1-2*s))
    return vel,temp

def flow(z,t,s,eta):
    n=z.shape[1];init=np.vstack((z,np.ones(n),np.zeros(n),np.zeros(n),np.ones(n)))
    def rhs(t,y):
        yy=y.reshape(6,n);v=shape(yy[:2],s,eta);M=yy[2:].reshape(2,2,n)
        Md=np.einsum('ijn,jkn->ikn',v['DH'],M)
        return np.vstack((v['H'],Md.reshape(4,n))).ravel()
    sol=solve_ivp(rhs,[0,t],init.ravel(),method='DOP853',rtol=2e-11,atol=2e-13)
    if not sol.success:raise RuntimeError(sol.message)
    end=sol.y[:,-1].reshape(6,n)
    return end[:2],end[2:].reshape(2,2,n),sol.nfev

out={'started_utc':started,'status':'RUNNING','exact_checks':exact,'cases':[],'scope':'Smooth annular Hamiltonian flows on manufactured smooth full-plane backgrounds. The nonzero manufactured temperature need not solve thermal transport; these are algebra, inverse-gauge and scaling controls, not admissible B2 fields or certified bounds.'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for case in params['cases']:
    beta=float(sp.Rational(case['beta']));s=1/beta;eta=float(sp.Rational(case['eta']));p=2-s
    for nr in params['radial_orders']:
        na=params['angular_order'];xx,ww=leggauss(nr);lo,hi=[float(sp.Rational(t)) for t in params['radial_bounds']];half=(hi-lo)/2;rr=(hi+lo)/2+half*xx;th=2*np.pi*(np.arange(na)+.37)/na
        rad,theta=np.meshgrid(rr,th,indexing='ij');z=np.vstack((rad.ravel()*np.cos(theta.ravel()),rad.ravel()*np.sin(theta.ravel())));weights=(half*ww[:,None]*rr[:,None]*np.ones((1,na))*2*np.pi/na).ravel()
        sh=shape(z,s,eta);B=beta*(np.einsum('ijn,jn->in',sh['DH'],z)-sh['H'])
        polarB=beta*(sh['er']*((-sh['Fp']+2*sh['F']/sh['r'])*sh['gp'])+sh['et']*((sh['r']*sh['Fpp']-sh['Fp'])*sh['g']))
        pp=-np.cos(sh['theta'])+eta/2*np.sin(2*sh['theta']);ppp=np.sin(sh['theta'])+eta*np.cos(2*sh['theta'])
        vinf=sh['er']*(-sh['r']**(p-1)*ppp)+sh['et']*(p*sh['r']**(p-1)*pp)
        A=float(np.sum(weights*np.sum(vinf*B,axis=0)));Aibp=-(4*beta-1)*float(np.sum(weights*sh['chi']*sh['omega']**2));B2=float(np.sum(weights*np.sum(B*B,axis=0)));eps=-Aibp/B2;Q=-Aibp*Aibp/(2*B2)
        probes=np.array([[1.25,.37,-1.43],[.35,1.53,.21]])
        jacerr=[]
        for step in [1e-4,5e-5]:
            numeric=[]
            for j in range(2):
                e=np.zeros_like(probes);e[j]=step
                numeric.append((shape(probes+e,s,eta)['H']-shape(probes-e,s,eta)['H'])/(2*step))
            numeric=np.stack(numeric,axis=1);jacerr.append(float(np.max(abs(numeric-shape(probes,s,eta)['DH']))))
        row={'beta':beta,'eta':eta,'radial_order':nr,'angular_order':na,'A_direct':A,'A_integration_by_parts':Aibp,'A_relative_difference':abs(A-Aibp)/abs(Aibp),'B2':B2,'epsilon_star':eps,'Q_negative_limit':Q,'polar_cartesian_B_error':float(np.max(abs(B-polarB))),'independent_DH_centered_difference_errors':jacerr,'radii':[]}
        for Rstring in params['radii']:
            R=float(Rstring);delta=R**(-s);phi,M,nfev=flow(z,eps*delta,s,eta);vr,tr=full_fields(z,R,s,eta)
            transformed=(beta*(np.einsum('ijn,jn->in',M,z)-phi))/delta+np.einsum('ijn,jn->in',M,vr)
            kin=float(np.sum(weights*(np.sum(transformed*transformed,axis=0)-np.sum(vr*vr,axis=0))/2))
            pot=float(np.sum(weights*(phi[1]-z[1])*tr));energy=kin+pot
            det=M[0,0]*M[1,1]-M[0,1]*M[1,0]
            row['radii'].append({'R':Rstring,'delta':delta,'flow_time':eps*delta,'kinetic_scaled_difference':kin,'potential_scaled_difference':pot,'potential_over_delta':pot/delta,'total_scaled_difference':energy,'relative_error_from_limit':abs(energy-Q)/abs(Q),'determinant_max_error':float(np.max(abs(det-1))),'flow_nfev':nfev})
        row['pass']=bool(Aibp<0 and B2>0 and row['polar_cartesian_B_error']<1e-10 and jacerr[-1]<1e-4 and max(x['determinant_max_error'] for x in row['radii'])<1e-8 and row['radii'][-1]['total_scaled_difference']<0)
        if nr==max(params['radial_orders']):row['pass']=bool(row['pass'] and row['A_relative_difference']<1e-7 and row['radii'][-1]['relative_error_from_limit']<.01)
        out['cases'].append(row);(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({'beta':beta,'nr':nr,'A_error':row['A_relative_difference'],'Q':Q,'last_scaled_energy':row['radii'][-1]['total_scaled_difference'],'last_relative_error':row['radii'][-1]['relative_error_from_limit'],'pass':row['pass']}),flush=True)
out.update(status='PASS' if all(x['pass'] for x in exact+out['cases']) else 'FAILED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(Path('research/155_arbitrary_finite_part_energy/PROOF.md').read_bytes()).hexdigest(),inputs_sha256=hashlib.sha256((root/'inputs.json').read_bytes()).hexdigest())
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['elapsed_seconds'],flush=True)
