"""Independent manufactured controls for the P202 formulas and algorithms."""
from pathlib import Path
from datetime import datetime,timezone
import time,json
import numpy as np
import sympy as sp
from moment_modal_inverse import MomentModalInverse
from adaptive_modal_inverse import ModalSettings
from sensitive_modal_flow import C2ModalFlow,reconstruct_sensitivity
from smooth_modal_flow import reconstruct

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/202_moment_inverse_and_flow_sensitivity/verification'

def now():return datetime.now(timezone.utc).isoformat()
def main():
    start=time.monotonic();result={'started_utc':now(),'exact_checks':{},'inverse_controls':[],
        'interpolant_controls':[],'transport_controls':[],'finite_cutoff_controls':[]}
    def check(name,expr):result['exact_checks'][name]=bool(sp.simplify(expr)==0)
    r=sp.symbols('r',positive=True);n=sp.symbols('n',integer=True,positive=True);f=sp.Function('f');s=sp.symbols('s',real=True)
    psi=r*f(sp.log(r));ode=-sp.diff(psi,r,2)-sp.diff(psi,r)/r+n*n*psi/r**2
    check('stream_radial_equation',ode-((n*n-1)*f(sp.log(r))-2*sp.Subs(sp.diff(f(s),s),s,sp.log(r))-sp.Subs(sp.diff(f(s),s,2),s,sp.log(r)))/r)
    x,y,k=sp.symbols('x y k',real=True);u=1+k*x*x;theta=x*x/u;g=sp.Matrix([sp.diff(theta,x),0])
    omega=sp.Rational(2,5)*sp.sqrt(u)/k/x*(1-u**sp.Rational(-5,2))
    W=sp.Matrix([x*u,(7-3*k*x*x)*y]);DW=W.jacobian([x,y]);Zh=W.diff(k);DZh=Zh.jacobian([x,y])
    check('manufactured_thermal',W.dot(g)-2*theta)
    check('manufactured_vorticity',W[0]*sp.diff(omega,x)+omega-g[0])
    check('manufactured_divergence',sp.trace(DW)-8)
    check('moment_sign',sp.integrate(2*r*(r*r-3)*sp.exp(-r*r),(r,0,sp.oo))+2)
    tf=sp.lambdify((x,y,k),theta,'numpy');gf=sp.lambdify((x,y,k),g,'numpy');of=sp.lambdify((x,y,k),omega,'numpy')
    v=sp.Matrix([theta,*g,omega]);vp=v.diff(k);vx=v.jacobian([x,y]);vpf=sp.lambdify((x,y,k),vp,'numpy');vxf=sp.lambdify((x,y,k),vx,'numpy')
    class ExactFlow:
        def __init__(self,kappa):self.k=kappa
        def values(self,X):
            xx,yy=X;kk=self.k;uu=1+kk*xx*xx
            return np.array([xx*uu,(7-3*kk*xx*xx)*yy]),np.array([[1+3*kk*xx*xx,0.],[-6*kk*xx*yy,7-3*kk*xx*xx]]),6*kk*xx*yy
        def W(self,X):return self.values(X)[0]
        def DW(self,X):return self.values(X)[1]
        def directional_DW(self,X,Z):
            xx,yy=X;zx,zy=Z;kk=self.k
            return np.array([[6*kk*xx*zx,0.],[-6*kk*(yy*zx+xx*zy),-6*kk*xx*zx]])
    class ExactDirection:
        def W(self,X):xx,yy=X;return np.array([xx**3,-3*xx*xx*yy])
        def DW(self,X):xx,yy=X;return np.array([[3*xx*xx,0.],[-6*xx*yy,-3*xx*xx]])
    dflow=ExactDirection()
    for kk in [.2,.7]:
        ff=ExactFlow(kk)
        def seed(X):return float(tf(*X,kk)),np.asarray(gf(*X,kk)).ravel(),float(of(*X,kk))
        def seed_h(X,sh):
            ans=np.asarray(vpf(*X,kk)).ravel()+np.asarray(vxf(*X,kk))@sh
            return ans[0],ans[1:3],ans[3]
        for point in [[.2,.1],[.8,.4],[1.3,.6]]:
            exact=np.array([float(tf(*point,kk)),*np.asarray(gf(*point,kk)).ravel(),float(of(*point,kk))]);dh=np.asarray(vpf(*point,kk)).ravel()
            for cutoff in [.03,.01]:
                row=reconstruct_sensitivity(ff,dflow,point,4.,1.,cutoff=cutoff,rtol=2e-12,atol=2e-14,exact_seed=seed,exact_seed_total_derivative=seed_h)
                val=np.array([row['Theta'],*row['gradient'],row['Omega']]);got=np.array(row['derivative_Theta_gradient_Omega'])
                row.update(k=kk,value_absolute_error=abs(val-exact).tolist(),sensitivity_absolute_error=abs(got-dh).tolist())
                result['transport_controls'].append(row)
        point=[.8,.4];cutoff=.03
        row=reconstruct_sensitivity(ff,dflow,point,4.,1.,cutoff=cutoff,rtol=2e-12,atol=2e-14)
        for step in [2e-4,1e-4]:
            vals=[]
            for j in [-2,-1,1,2]:
                q=reconstruct(ExactFlow(kk+j*step),point,4.,1.,cutoff=cutoff,rtol=2e-12,atol=2e-14,compatible_seed=True)
                vals.append(np.r_[q['Theta'],q['gradient'],q['Omega']])
            fd=(vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*step)
            result['finite_cutoff_controls'].append({'k':kk,'step':step,'cutoff':cutoff,'point':point,
                'sensitivity':row['derivative_Theta_gradient_Omega'],'difference':fd.tolist(),
                'absolute_error':abs(fd-row['derivative_Theta_gradient_Omega']).tolist()})
    # Smooth whole-plane manufactured inverse with modes1,2,3.
    c=.7;d=.11
    def modes(rr):
        e=np.exp(-rr*rr);return e*np.array([8*rr-4*rr**3,2*c*rr*rr*(rr*rr-3),4*d*rr**3*(4-rr*rr)])
    def exact_modal(rr):
        e=np.exp(-rr*rr)
        return np.array([np.expm1(-rr*rr),-.5*c*rr*e,d*rr*rr*e]),np.array([(1-2*rr*rr)*e-1,-c*rr*(1-rr*rr)*e,d*(3*rr*rr-2*rr**4)*e])
    inv=MomentModalInverse(modes,3,ModalSettings(.5,2e-13,2e-12),-2*c,breakpoints=[.1,1.,2.,4.])
    radii=np.geomspace(1e-5,12.,80);pp=[];dd=[];hh=[];hp=[]
    rr=sp.symbols('rr',positive=True);hm=sp.Matrix([8*rr-4*rr**3,2*sp.Rational(7,10)*rr*rr*(rr*rr-3),4*sp.Rational(11,100)*rr**3*(4-rr*rr)])*sp.exp(-rr*rr)
    hpf=sp.lambdify(rr,hm.diff(rr),'numpy')
    for rv in radii:
        p,q=inv.radial(rv);pe,qe=exact_modal(rv)
        result['inverse_controls'].append({'r':rv,'pr_error':float(max(abs(p-pe))), 'dp_error':float(max(abs(q-qe)))})
        pp.append(p);dd.append(q);hh.append(modes(rv));hp.append(np.asarray(hpf(rv)).ravel())
    flow=C2ModalFlow(4.,radii,np.array(pp),np.array(dd),np.array(hh),np.array(hp))
    for point in [[.2,.1],[.8,.4],[1.3,.6],[-.8,.3]]:
        X=np.array(point);Z=np.array([.37,-.2]);exact=flow.directional_DW(X,Z)
        for step in [2e-4,1e-4,5e-5]:
            vals=[flow.DW(X+j*step*Z) for j in [-2,-1,1,2]];fd=(vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*step)
            result['interpolant_controls'].append({'point':point,'step':step,'DW_directional_error':float(max(abs(fd-exact).ravel()))})
    # Direct polynomial stream confirms moving-frame third derivatives separately.
    ss,ph=sp.symbols('ss ph',real=True);xx=sp.exp(ss)*sp.sin(ph);yy=-sp.exp(ss)*sp.cos(ph)
    for mode in [1,2,3,4]:
        power=mode+2
        P=sp.im((-y+sp.I*x)**mode)*(x*x+y*y)
        P=sp.expand_complex(P).expand();H=sp.hessian(P,(x,y));J=sp.Matrix([[0,-1],[1,0]])
        er=sp.Matrix([sp.sin(ph),-sp.cos(ph)]);et=J*er;Q=sp.Matrix.hstack(er,et)
        fun=sp.exp((power-1)*ss);fs=sp.diff(fun,ss);fss=sp.diff(fun,ss,2)
        B=sp.Matrix([[(fs+fss)*sp.sin(mode*ph),mode*fs*sp.cos(mode*ph)],[mode*fs*sp.cos(mode*ph),((1-mode*mode)*fun+fs)*sp.sin(mode*ph)]])/sp.exp(ss)
        direct=H.subs({x:xx,y:yy},simultaneous=True)
        diff=(Q*B*Q.T-direct).applyfunc(sp.trigsimp)
        for a in range(2):
            for b in range(2):check(f'polynomial_hessian_{mode}_{a}_{b}',sp.expand_trig(diff[a,b]))
    result['quadrature_evidence']=inv.evidence
    result.update(ended_utc=now(),elapsed_seconds=time.monotonic()-start,all_exact_passed=all(result['exact_checks'].values()))
    (OUT/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print('exact',len(result['exact_checks']),result['all_exact_passed'])
    print('transport max',max(max(z['sensitivity_absolute_error']) for z in result['transport_controls']))
    print('finite cutoff max',max(max(z['absolute_error']) for z in result['finite_cutoff_controls']))
    print('inverse max',max(max(z['pr_error'],z['dp_error']) for z in result['inverse_controls']))
    print('directional DW max',max(z['DW_directional_error'] for z in result['interpolant_controls']))
    print('elapsed',result['elapsed_seconds'])
    assert result['all_exact_passed']
if __name__=='__main__':main()
