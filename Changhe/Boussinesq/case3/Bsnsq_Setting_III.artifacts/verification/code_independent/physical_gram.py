"""Independent full-physical-plane Gram quadrature for native r2 basis.
Normalized SciPy B-splines, endpoint Gauss-Jacobi, no numerics-lane imports.
"""
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import roots_jacobi
from scipy.linalg import block_diag, cholesky, cho_solve


def radial_mass(knots,degree,b,L,delta,R,order,odd,weighted=True):
    nb=len(knots)-degree-1
    spline=BSpline(knots,np.eye(nb),degree,extrapolate=False)
    ans=np.zeros((nb,nb)); edges=np.unique(knots)
    terms=[-1,1] if weighted else [0]
    for lo,hi in zip(edges[:-1],edges[1:]):
        for sign in terms:
            power=sign*delta
            alpha=1-b*power if hi==1 else 0.
            endpoint=power/2+odd
            beta=endpoint if lo==0 else 0.
            x,wx=roots_jacobi(order,alpha,beta)
            t=lo+(hi-lo)*(x+1)/2
            u=1-t; logrho=np.log(-np.expm1(2*b*np.log(u)))
            # Original integrand: u^(1-b*power) rho2^(power/2+odd).
            # Divide out endpoint factors handled by the Jacobi rule.
            logremainder=(1-b*power)*np.log(u)+endpoint*logrho
            if lo==0:logremainder-=beta*np.log(t)
            if hi==1:logremainder-=alpha*np.log(u)
            weight=wx*((hi-lo)/2)**(alpha+beta+1)*(L/R)**power*np.exp(logremainder)
            B=spline(t)
            ans+=B.T@(weight[:,None]*B)
    return b*L*L*ans


def active_indices(K,nb):
    return np.array([k*nb+j for k in range(K) for j in range(k//2,nb)],dtype=int)


def build_gram(knots,degree,K,b,L,delta=.25,R=1.,order=48,weighted=True):
    nb=len(knots)-degree-1
    radial=[radial_mass(knots,degree,b,L,delta,R,order,o,weighted) for o in [0,1]]
    blocks=[np.pi*(2 if k==0 else 1)*radial[k%2][k//2:,k//2:] for k in range(K)]
    H=block_diag(*blocks)
    integral=(knots[degree+1:degree+1+nb]-knots[:nb])/(degree+1)
    qfull=np.zeros((K,nb))
    if K>1:qfull[1]=-b*L/4*integral
    if K>3:qfull[3]=b*L/4*integral
    idx=active_indices(K,nb);q=qfull.ravel()[idx]
    # Compute dual by small diagonal blocks, retaining the actual matrix.
    pos=0; sol=np.zeros_like(q); mineig=[];maxeig=[];chol_error=[]
    for block in blocks:
        n=len(block);C=cholesky(block,lower=False,check_finite=True)
        sol[pos:pos+n]=cho_solve((C,False),q[pos:pos+n])
        ev=np.linalg.eigvalsh(block);mineig.append(float(ev[0]));maxeig.append(float(ev[-1]))
        chol_error.append(float(np.linalg.norm(C.T@C-block,ord=np.inf)/np.linalg.norm(block,ord=np.inf)))
        pos+=n
    return {'H':H,'q':q,'dual_coeff':sol,'active':idx,'blocks':blocks,'radial_mass':radial,
            'dual_squared':float(q@sol),'min_eigenvalue':min(mineig),'max_eigenvalue':max(maxeig),
            'max_block_condition':max(a/b for a,b in zip(maxeig,mineig)),'cholesky_relative_error':max(chol_error)}
