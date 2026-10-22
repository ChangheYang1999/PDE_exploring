"""Check analytic basis derivatives and coefficient Jacobian before optimization."""
import numpy as np
from rational_solver import basis,indices,Problem
rng=np.random.default_rng(20261020)
s=np.array([0,.02,.4,2.,10.]);t=np.array([.5,.01,0.,3.,.2]);p=.17;ij=indices(5)
b=basis(s,t,p,ij)
h=1e-4
for (a,c) in [(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]:
    axis=0 if a else 1;prev=(a-1,c) if a else (a,c-1)
    plus=basis(s+h if axis==0 else s,t+h if axis==1 else t,p,ij,orders=[prev])[prev]
    minus=basis(s-h if axis==0 else s,t-h if axis==1 else t,p,ij,orders=[prev])[prev]
    err=np.max(np.abs((plus-minus)/(2*h)-b[a,c])/np.maximum(1,np.abs(b[a,c])))
    print('basis',a,c,err)
    assert err<5e-6
for free in [False,True]:
    prob=Problem(4,9,12,3.,-1.,40.,free,2);z=prob.initial();r,J=prob.compute(z,jac=True)
    direction=rng.normal(size=len(z));direction/=np.linalg.norm(direction);eps=1e-5
    fd=(prob.compute(z+eps*direction)-prob.compute(z-eps*direction))/(2*eps)
    err=np.max(np.abs(fd-J@direction))/max(1,np.max(np.abs(fd)))
    print('jacobian',free,err)
    assert err<1e-7

for free in [False,True]:
    prob=Problem(5,9,12,3.,-1.,40.,free,2,family='bernstein');z=prob.initial();r,J=prob.compute(z,jac=True)
    direction=rng.normal(size=len(z));direction/=np.linalg.norm(direction);eps=1e-5
    fd=(prob.compute(z+eps*direction)-prob.compute(z-eps*direction))/(2*eps)
    err=np.max(np.abs(fd-J@direction))/max(1,np.max(np.abs(fd)))
    print('bernstein jacobian',free,err)
    assert err<1e-7
from rational_solver import elevate_bernstein
for old_degree,new_degree in [(2,3),(3,7),(4,12)]:
    coeff=rng.normal(size=len(indices(old_degree)))
    elevated=elevate_bernstein(coeff,old_degree,new_degree)
    old_basis=basis(s,t,p,indices(old_degree),family='bernstein',degree=old_degree)
    new_basis=basis(s,t,p,indices(new_degree),family='bernstein',degree=new_degree)
    for order in old_basis:
        err=np.max(np.abs(old_basis[order]@coeff-new_basis[order]@elevated))
        assert err<2e-11,(old_degree,new_degree,order,err)
    print('elevation',old_degree,new_degree,'PASS')
print('PASS')
