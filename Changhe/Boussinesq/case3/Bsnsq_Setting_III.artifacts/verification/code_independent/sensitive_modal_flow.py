"""C2 velocity interpolation and analytic characteristic sensitivities (P202)."""
import numpy as np
from scipy.interpolate import BPoly,PPoly
from scipy.integrate import solve_ivp
from smooth_modal_flow import SmoothModalFlow

class C2ModalFlow(SmoothModalFlow):
    def __init__(self,beta,radii,pr,dp,H,Hp):
        self.beta=float(beta);self.radii=np.asarray(radii);self.s=np.log(self.radii)
        self.n=np.arange(1,np.shape(pr)[1]+1,dtype=float)
        fs=dp-pr;fss=(self.n**2-1)*pr-2*fs-self.radii[:,None]*H
        fsss=(self.n**2-1)*fs-2*fss-self.radii[:,None]*H-self.radii[:,None]**2*Hp
        data=np.stack((pr,fs,fss,fsss),axis=1)
        self.poly=PPoly.from_bernstein_basis(BPoly.from_derivatives(self.s,data),extrapolate=False)
    def directional_DW(self,X,Z):
        X=np.asarray(X);Z=np.asarray(Z);r=np.hypot(*X);s=np.log(r)
        f=self.poly(s);fs=self.poly(s,1);fss=self.poly(s,2);fsss=self.poly(s,3)
        ph=np.arctan2(X[0],-X[1]);sn=np.sin(self.n*ph);cs=np.cos(self.n*ph);n=self.n
        er=X/r;et=np.array([-er[1],er[0]]);Q=np.column_stack((er,et));J=np.array([[0.,-1.],[1.,0.]])
        B=np.array([[np.dot(fs+fss,sn),np.dot(n*fs,cs)],
            [np.dot(n*fs,cs),np.dot((1-n*n)*f+fs,sn)]])/r
        Bs=np.array([[np.dot(fsss-fs,sn),np.dot(n*(fss-fs),cs)],
            [np.dot(n*(fss-fs),cs),np.dot((n*n-1)*f-n*n*fs+fss,sn)]])/r
        Bp=np.array([[np.dot(n*(fs+fss),cs),-np.dot(n*n*fs,sn)],
            [-np.dot(n*n*fs,sn),np.dot(n*((1-n*n)*f+fs),cs)]])/r
        return J@Q@(Bs*(er@Z/r)+(Bp+J@B-B@J)*(et@Z/r))@Q.T


def reconstruct_sensitivity(flow,direction,Y,beta,a0,cutoff=1e-3,rtol=1e-11,atol=1e-13,
        max_time=250.,exact_seed=None,exact_seed_total_derivative=None):
    Y=np.array(Y,dtype=float);rho=beta-2
    def event(t,v):return np.hypot(*v[:2])-cutoff
    event.terminal=True;event.direction=-1
    def back_rhs(t,v):
        X=v[:2];p=v[2:];W,DW,_=flow.values(X)
        return np.r_[-W,-DW@p-direction.W(X)]
    back=solve_ivp(back_rhs,(0.,max_time),np.r_[Y,[0.,0.]],method='DOP853',events=event,
        dense_output=True,rtol=rtol,atol=atol,max_step=.2)
    if not back.success or not len(back.t_events[0]):
        return {'status':'BACKWARD_FAILED','message':back.message}
    T=float(back.t_events[0][0]);end=back.y_events[0][0];seed=end[:2];p=end[2:]
    normal=seed/np.linalg.norm(seed);Ws,DWs,_=flow.values(seed);Zs=direction.W(seed)
    flux=float(Ws@normal)
    if flux<=0:raise ValueError('Cutoff hit is not outgoing')
    Th=float(normal@p/flux);sh=p-Ws*Th;nh=sh/cutoff
    theta0=a0*seed[0]**2;theta0h=2*a0*seed[0]*sh[0]
    v0=np.array([2*a0*seed[0],0.]);v0h=np.array([2*a0*sh[0],0.])
    Wsh=DWs@sh+Zs;N=rho*theta0-Ws@v0;Nh=rho*theta0h-Wsh@v0-Ws@v0h
    Fh=nh@Ws+normal@Wsh
    g0=v0+normal*N/flux
    g0h=v0h+nh*N/flux+normal*(Nh*flux-N*Fh)/flux**2
    o0=4*a0*seed[0]/beta;o0h=4*a0*sh[0]/beta
    if exact_seed is not None:
        theta0,g0,o0=exact_seed(seed)
        if exact_seed_total_derivative is None:raise ValueError('Exact seed needs its total derivative')
        theta0h,g0h,o0h=exact_seed_total_derivative(seed,sh)
    def forward_rhs(tau,vv):
        bp=back.sol(T*(1-tau));X=bp[:2];p=bp[2:];W,DW,_=flow.values(X)
        Xh=p-W*(1-tau)*Th
        A=np.zeros((3,3));A[:2,:2]=rho*np.eye(2)-DW.T;A[2]=[1.,0.,-1.]
        Ah=np.zeros((3,3));Ah[:2,:2]=-(flow.directional_DW(X,Xh)+direction.DW(X)).T
        v=vv[:3];vh=vv[3:]
        return np.r_[T*(A@v),Th*(A@v)+T*(A@vh+Ah@v)]
    fwd=solve_ivp(forward_rhs,(0.,1.),np.r_[g0,o0,g0h,o0h],method='DOP853',
        rtol=rtol,atol=atol,max_step=min(.05,.2/T))
    theta=np.exp(rho*T)*theta0;thetah=np.exp(rho*T)*(rho*Th*theta0+theta0h)
    return {'status':'COMPLETE' if fwd.success else 'FORWARD_FAILED','point':Y.tolist(),
        'cutoff':cutoff,'rtol':rtol,'atol':atol,'Theta':float(theta),
        'gradient':fwd.y[:2,-1].tolist(),'Omega':float(fwd.y[2,-1]),
        'derivative_Theta_gradient_Omega':np.r_[thetah,fwd.y[3:,-1]].tolist(),
        'time_to_cutoff':T,'time_derivative':Th,'seed_point':seed.tolist(),
        'seed_derivative':sh.tolist(),'seed_normal_derivative_error':float(normal@sh),
        'outgoing_flux':flux,'backward_nfev':back.nfev,'forward_nfev':fwd.nfev}
