"""Independent finite binomial series of chi through degree eight.
No spatial differences, no engine derivative operations. Float/complex and Decimal paths.
"""
from ipm_portable import output_dir, peak_rss_mib
import math
from decimal import Decimal, localcontext
import numpy as np
ORDER=[(m,k) for m in range(4) for k in range(5)]+[(m,5) for m in range(4)]
NAMES=['a','b','c','d','e','g','h','u','v','w','z','k']

def series(cl, decimal=False):
    zero=Decimal(0) if decimal else 0.*cl
    one=Decimal(1) if decimal else 1.
    gamma=one/cl;delta=(one-gamma)/2
    offsets=[zero,one,2*one,delta,2*delta,3*delta]
    columns=[]
    for m,k in ORDER:
        p=(3+gamma)/2-m-offsets[k];A={}
        for j in range(m+1):
            angular=(-1)**j*math.comb(2*m,2*j)
            choose=one
            for n in range(5-m):
                if n:choose=choose*(p-n+1)/n
                for l in range(n+1):
                    key=(2*m-2*j+2*l,2*j+2*(n-l))
                    A[key]=A.get(key,zero)+angular*choose*math.comb(n,l)
        F={};H={}
        for (i,j),value in A.items():
            if i>=2 and j>=2:
                key=(i-2,j-2);F[key]=F.get(key,zero)-i*(i-1)*j*value
                H[key]=H.get(key,zero)+i*j*value
            if j>=4:
                key=(i,j-4);F[key]=F.get(key,zero)-j*(j-1)*(j-2)*value
        columns.append([F.get(key,zero) for key in [(0,0),(2,0),(0,2),(4,0),(2,2),(0,4)]]+
                       [H.get(key,zero) for key in [(0,0),(2,0),(0,2),(4,0),(2,2),(0,4)]])
    return columns

def matrices(cl):return np.array(series(cl)).T

def values(cl,coeff):
    a,b,c,d,e,g,h,u,v,w,z,k=matrices(cl)@np.asarray(coeff)
    C=np.array([2*(2*cl-1)*b+3*a*u,2*c+a*v])
    fourth=np.array([4*(2*cl-1)*d+b*u+5*a*w,4*cl*e-5*b*v+9*c*u+3*a*z,4*g+3*c*v+a*k])
    poisson=np.array([3*(u+v)+b,20*w+6*z+4*d,6*z+20*k+2*e])
    return dict(zip(NAMES,[a,b,c,d,e,g,h,u,v,w,z,k])),C,fourth,poisson

def high_precision(cl,coeff,prec=70):
    with localcontext() as ctx:
        ctx.prec=prec
        L=Decimal.from_float(float(cl));cc=[Decimal.from_float(float(x)) for x in coeff]
        A=series(L,True);v=[sum((cc[j]*A[j][i] for j in range(24)),Decimal(0)) for i in range(12)]
        a,b,c,d,e,g,h,u,vv,w,z,k=v
        C=[2*(2*L-1)*b+3*a*u,2*c+a*vv]
        fourth=[4*(2*L-1)*d+b*u+5*a*w,4*L*e-5*b*vv+9*c*u+3*a*z,4*g+3*c*vv+a*k]
        P=[3*(u+vv)+b,20*w+6*z+4*d,6*z+20*k+2*e]
        return {'precision':prec,'jets':dict(zip(NAMES,map(str,v))),'constraints':list(map(str,C)),
                'fourth':list(map(str,fourth)),'poisson':list(map(str,P)),'center':str(L+h-1)}
