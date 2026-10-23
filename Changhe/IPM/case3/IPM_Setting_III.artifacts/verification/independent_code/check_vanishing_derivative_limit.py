"""Independent ordered-tensor polar integrals; no producer code or finite differences."""
from pathlib import Path
from datetime import datetime, timezone
from math import comb, factorial
import itertools, json
import numpy as np
from numpy.polynomial.legendre import leggauss


def product(a,b):
    return [sum(comb(k,j)*a[j]*b[k-j] for j in range(k+1)) for k in range(4)]


def radial_to_cartesian(g,x,y):
    X=[x,y]
    d1=[2*X[i]*g[1] for i in range(2)]
    d2={(i,j):2*(i==j)*g[1]+4*X[i]*X[j]*g[2] for i,j in itertools.product(range(2),repeat=2)}
    d3={(i,j,k):4*((i==j)*X[k]+(i==k)*X[j]+(j==k)*X[i])*g[2]+8*X[i]*X[j]*X[k]*g[3] for i,j,k in itertools.product(range(2),repeat=3)}
    return d1,d2,d3


def tensor(g,x,y,polynomial):
    d1,d2,d3=radial_to_cartesian(g,x,y)
    if polynomial=='y':
        P=y; p1=[np.zeros_like(x),np.ones_like(x)]
        p2={(i,j):0 for i,j in itertools.product(range(2),repeat=2)}
        p3={idx:0 for idx in itertools.product(range(2),repeat=3)}
    elif polynomial=='xxy':
        P=x*x*y;p1=[2*x*y,x*x]
        p2={(0,0):2*y,(0,1):2*x,(1,0):2*x,(1,1):0}
        p3={idx:2 if sorted(idx)==[0,0,1] else 0 for idx in itertools.product(range(2),repeat=3)}
    else:raise ValueError(polynomial)
    return np.stack([P*d3[i,j,k]+p1[i]*d2[j,k]+p1[j]*d2[i,k]+p1[k]*d2[i,j]+p2[i,j]*d1[k]+p2[i,k]*d1[j]+p2[j,k]*d1[i]+p3[i,j,k]*g[0] for i,j,k in itertools.product(range(2),repeat=3)],axis=0)


def grid(n,angular=32):
    z,w=leggauss(n);u=(z+1)/2;w=w/2;r=u/(1-u)
    weights=w*r/(1-u)**2*(2*np.pi/angular)
    th=2*np.pi*(np.arange(angular)+.271)/angular
    x=r[:,None]*np.cos(th);y=r[:,None]*np.sin(th)
    return x,y,(r*r)[:,None],weights


def norms(n,ds):
    x,y,s,w=grid(n)
    inv=[(-1)**k*factorial(k)/(1+s)**(k+1) for k in range(4)]
    G=[-2*np.log1p(s),-2/(1+s),2/(1+s)**2,-4/(1+s)**3]
    H=[-4*s/(1+s),-4/(1+s)**2,8/(1+s)**3,-24/(1+s)**4]
    TG=tensor(G,x,y,'y');TH=tensor(H,x,y,'y')
    integral=lambda v:float(np.sum(v*v*w[None,:,None]))
    EG=integral(TG);EH=integral(TH)
    assert abs(EG/(512*np.pi/5)-1)<2e-10
    assert abs(EH/(6144*np.pi/35)-1)<2e-10
    # Positive integral formula for all radial derivatives of the canonical stream.
    tz,tw=leggauss(n);tt=(tz+1)/2;tw=tw/2
    ss=s[:,0,None];den=1+ss*tt[None,:]**2
    result=[]
    for D in ds:
        eta=D/(1+D);a=eta/2
        poch=1.;f=[];h=[]
        for k in range(5):
            if k:poch*=a+k-1
            f.append((-1)**k*poch*(1+s)**(-a-k))
            h.append(((-1)**k*poch*np.sum(tw[None,:]*tt[None,:]**(3+2*k)*den**(-a-k),axis=1))[:,None])
        hi=product(h,inv)
        B0=[inv[k]+(-4+4*eta)*h[k]-4*eta*hi[k] for k in range(4)]
        B2=[-8*h[k+1]-8*eta*hi[k] for k in range(4)]
        C0=[4*v for v in product(f,B0)];C2=[4*v for v in product(f,B2)]
        Trho=tensor([4*v/D for v in f[:4]],x,y,'y')
        TF=tensor(C0,x,y,'y')+tensor(C2,x,y,'xxy')
        ER=integral(Trho);EF=integral(TF)
        result.append({'D':D,'rho_D3_over_D2_norm_squared':ER,'F_D3_over_D2_norm_squared':EF,'eta3':float(np.sqrt(EF/ER)),'rho_tensor_L2_error_to_limit':float(np.sqrt(integral(Trho-TG))),'F_tensor_L2_error_to_limit':float(np.sqrt(integral(TF-TH)))})
    return {'n_radial_and_inner':n,'n_angular':32,'G_norm_squared':EG,'H_norm_squared':EH,'ratio_squared':EH/EG,'finite_D':result}


# Polynomial checks test the ordered tensor independently of radial integration.
x=np.array([[.23,.8]]);y=np.array([[.4,-.9]]);s=x*x+y*y
# y*s has xxy derivative2 and yyy derivative6.
T=tensor([s,np.ones_like(s),np.zeros_like(s),np.zeros_like(s)],x,y,'y')
for row,idx in zip(T,itertools.product(range(2),repeat=3)):
    expected=6 if idx==(1,1,1) else (2 if sorted(idx)==[0,0,1] else 0)
    assert np.max(np.abs(row-expected))<1e-14
# x^2*y has xxy derivatives2 only.
T=tensor([np.ones_like(s),np.zeros_like(s),np.zeros_like(s),np.zeros_like(s)],x,y,'xxy')
for row,idx in zip(T,itertools.product(range(2),repeat=3)):
    expected=2 if sorted(idx)==[0,0,1] else 0
    assert np.max(np.abs(row-expected))<1e-14
levels=[norms(n,[.5,.2,.1,.03,.01,.003,.001,.0003,.0001]) for n in [96,192,384]]
for a,b in zip(levels[-2]['finite_D'],levels[-1]['finite_D']):
    assert abs(a['eta3']/b['eta3']-1)<2e-7
assert abs(levels[-1]['finite_D'][-1]['eta3']/np.sqrt(12/7)-1)<3e-4
for key in ['rho_tensor_L2_error_to_limit','F_tensor_L2_error_to_limit']:
    seq=[v[key] for v in levels[-1]['finite_D']]
    assert all(a>b for a,b in zip(seq,seq[1:]))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','method':'Ordered Cartesian product tensors, full infinite radial Gauss transform, periodic polar quadrature, positive inner integral for canonical H derivatives. No sympy code or producer code imported.','exact_limit_eta3':float(np.sqrt(12/7)),'levels':levels,'scope':'Numerical cross-check of the independently proved global L2 limit; no interval rounding or integral enclosure claimed.'}
p=Path('research/vanishing_derivative_limit/verification/polar_crosscheck.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
