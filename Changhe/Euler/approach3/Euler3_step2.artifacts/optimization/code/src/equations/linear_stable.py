"""D6FP: exact potential-level evaluation of the LINEAR rotating momentum operator A U = (1 - c_l) U + c_l (y . grad) U - omega [(J y . grad) U - J U]
(verifier's derivation research/stable_linear_operator/PROOF.md in RUN_ROOT/verifier; code copied from
RUN_ROOT/verifier/independent/src/stable_linear.py, sha256 ea17cd9ffb26209474cc3d53fae341822913e0c7b4d9966f6a96c8132faca710, 2026-10-28). For U = curl(T y) + curl curl(S y),
A U = curl((B_T T) y) + curl curl((B_S S) y) with B_T = (1 - c) + c D_r - omega d_phi, B_S = (1 - 2c) + c D_r - omega d_phi; on each basis function
(s/R0)^-nu B(s) e^{i m psi} H the operator gives (s/R0)^-nu e^{i m psi} H {[delta + (c nu - i m omega) R0^2/s^2] B + c r^2/s B'} with delta = b + c l - c nu, which
vanishes for the main channels: the analytically zero leading constant is removed BEFORE summation, so the far rows no longer suffer the
cancellation of O(1) terms (relative accuracy of the linear term at far radii 1e-9 instead of 1e-3; verifier V033, V035, V038). Same operator,
same represented field, same objective to roundoff (O1 relative change 8e-15 on the saved states). Enabled by Problem(stable_linear=True)."""
import torch


def linear_velocity(model, z):
    from src.bases import jets
    d=model.unpack_all(z);c=d['c_l'];w=d['omega'];alpha=(1-c)/c
    rho=model.rho;ell=model.l_arr;R0=model.R0;K=2
    # One more Taylor coefficient is needed for the derivative of B.
    ss=jets.affine_pow(rho+R0**2,.5,K+1)
    xx=jets.const(1.,ss)-2*R0*jets.recip(ss+jets.const(R0,ss))
    rr=jets.variable(rho,K)
    invu=jets.affine_pow(rho+R0**2,-1.,K)
    allT=torch.zeros(K+1,len(rho),model.Nq,device=z.device,dtype=z.dtype)
    allS=torch.zeros_like(allT)
    for name,kind in [('A','T'),('C','S'),('B','T'),('D','S'),('E','S')]:
        coeff=d[name]
        if not coeff.numel():continue
        # The frozen E basis suppresses ell=0,1 even when slots are present.
        if name=='E':coeff=coeff*(ell>=2)[None,:]
        Phi=torch.stack(jets.chebyshev_shifted(xx,coeff.shape[0]),-1)
        poly=torch.einsum('nrk,kq->nrq',Phi,coeff)
        if name in ('B','D','E') and model.channels['core_damp']:
            R1=model.channels.get('R1',None)
            if R1 is None:R1=R0
            frac=jets.const(1.,ss)-R1**2*jets.affine_pow(rho+R1**2,-1.,K+1)
            damp=jets.const(1.,ss)
            for _ in range(int(model.channels['core_damp'])):damp=jets.mul(damp,frac)
            poly=jets.mul(poly,damp[:,:,None])
        if name=='A':nu=alpha+ell;delta=torch.zeros_like(ell)
        elif name=='C':nu=alpha+ell-1.;delta=torch.zeros_like(ell)
        elif name=='B':nu=2*alpha+1+ell;delta=-torch.ones_like(ell)
        elif name=='D':nu=2*alpha+ell;delta=-torch.ones_like(ell)
        else:nu=2*ell+1.;delta=1.-c*(ell+3.)
        env=jets.affine_pow(rho[:,None]+R0**2,-nu[None,:]/2.,K)*R0**nu[None,None,:]
        P=poly[:K+1];Pprime=torch.stack([(n+1)*poly[n+1] for n in range(K+1)])
        radial=delta[None,None,:]*P
        radial=radial+c*nu[None,None,:]*R0**2*jets.mul(invu[:,:,None],P)
        radial=radial+2*c*jets.mul(rr[:,:,None],Pprime)
        derivative_phi=model.tw_sign[None,None,:]*model.m_arr[None,None,:]*P[:,:,model.partner]
        rot=(-w*derivative_phi if name=='E' else -w*R0**2*jets.mul(invu[:,:,None],derivative_phi))
        transformed=jets.to_derivs(jets.mul(env,radial+rot))
        if name!='E':
            C,S=model.rb.twist_tables(rho,w,c,R0,model.Mmax,K)
            transformed=model._twist(transformed,C,S,K)
        if kind=='T':allT=allT+transformed
        else:allS=allS+transformed
    zero=torch.zeros_like(allT[0]);ell2=ell[None,:];rho2=rho[:,None]
    _,gradT,_=model.scalar_grid((allT[0],allT[1],zero),False)
    kval=(ell2+1)*allS[0]+2*rho2*allS[1]
    kprime=(ell2+3)*allS[1]+2*rho2*allS[2]
    _,gradK,_=model.scalar_grid((kval,kprime,zero),False)
    dval=(6+4*ell2)*allS[1]+4*rho2*allS[2]
    lap=(model.rl*dval)@model.A0.T
    y=model.y.permute(2,0,1)
    return -torch.einsum('ijk,jra,kra->ira',model.eps,y,gradT)+gradK-y*lap[None]


def install(problem):
    """Patch one local Problem instance; return its original bound evaluator."""
    import types
    original=problem.evaluate
    def evaluate(self,z,need_terms=False,tables=None):
        out=original(z,need_terms=need_terms,tables=tables)
        F=out['F'];linear=linear_velocity(self.model,z)
        nonlinear=torch.einsum('m...,mi...->i...',F['U'],F['GU'])
        out['R_u']=linear+nonlinear+out['gradP']
        out['mom_terms']=dict(out['mom_terms']);out['mom_terms']['sum']=out['R_u']
        out['stable_linear']=linear;out['stable_nonlinear']=nonlinear
        return out
    problem.evaluate=types.MethodType(evaluate,problem)
    return original
