"""Independent smooth full-plane basis. No producer code is imported."""
from fractions import Fraction
from math import comb
import numpy as np
from scipy.special import hyp2f1

def dictionary(p, M, J, L):
    p=Fraction(p)
    if not (0<p<1 and M>=2 and J>=2 and L>=1): raise ValueError('dictionary domain')
    out=[];seen=set()
    # Preserve the two affine coordinates and the explicit starting n=3 term.
    labels=[(1,0,0),(1,1,0),(3,1,0)]
    labels += [(2*m+1,j,ell) for m in range(M) for j in range(J) for ell in range(L)]
    for n,j,ell in labels:
        beta=(n-p)/2+j+ell*(1-p)/2; key=(n,beta)
        if key in seen: continue
        seen.add(key);out.append(dict(n=n,j=j,ell=ell,beta=str(beta)))
    return out

def functionals(rows,p):
    p=Fraction(p);k=[];s=[];c=[]
    for row in rows:
        n=row['n'];beta=Fraction(row['beta']);lead=beta==(n-p)/2
        k.append((-1)**((n-1)//2) if lead else 0)
        s.append(int(n==1))
        c.append(Fraction(-1,4) if n==1 else 1/(2*(beta-1)) if n==3 else 0)
    return tuple(np.array(v,dtype=float) for v in [k,s,c])

def affine(rows,p):
    k,s,c=functionals(rows,p);a=np.zeros(len(rows));a[0]=-1;a[1]=1
    T=np.zeros((len(rows),len(rows)-1));T[1,0]=1
    for z,i in enumerate(range(2,len(rows)),1):
        T[i,z]=1;T[0,z]=-k[i];T[1,z]=k[i]-s[i]
    return a,T,k,s,c

def start(rows,p,a0):
    a,T,k,s,c=affine(rows,p);z=np.zeros(T.shape[1]);z[0]=a0
    z[1]=(1-1/float(p)+a0/4)*(3-float(p))
    return z

def evaluate(rows,x,y):
    x=np.asarray(x,dtype=float).reshape(-1);y=np.asarray(y,dtype=float).reshape(-1)
    r=np.hypot(x,y)
    if np.any(r==0): raise ValueError('origin evaluated by exact functionals')
    th=np.arctan2(y,x);ct=x/r;st=y/r;logr=np.log(r);log1=np.log1p(r*r)
    fields={name:np.empty((len(r),len(rows))) for name in ['rho','dx','dy','ux','uy','psi']}
    for b,row in enumerate(rows):
        n=row['n'];beta=float(Fraction(row['beta']))
        f=np.exp(n*logr-beta*log1);fp=(n/r-2*beta*r/(1+r*r))*f
        sn=np.sin(n*th);cn=np.cos(n*th)
        fields['rho'][:,b]=f*sn
        fields['dx'][:,b]=fp*ct*sn-n*f/r*st*cn
        fields['dy'][:,b]=fp*st*sn+n*f/r*ct*cn
        A=np.empty_like(r);small=r<8
        A[small]=np.exp((2*n+2)*logr[small])*hyp2f1(beta,n+1,n+2,-r[small]*r[small])/(2*(n+1))
        if np.any(~small):
            radius=r[~small].astype(np.longdouble);lt=np.log1p(radius*radius);total=np.zeros_like(radius)
            exact_beta=Fraction(row['beta'])
            for ell in range(n+1):
                exponent=ell-exact_beta+1
                if exponent==0:term=lt
                else:
                    ee=np.longdouble(exponent.numerator)/np.longdouble(exponent.denominator)
                    term=np.expm1(ee*lt)/ee
                total+=((-1)**(n-ell)*comb(n,ell))*term
            A[~small]=np.asarray(total/2,dtype=float)
        gp=-.5*np.exp(-(n+1)*logr)*A;gpd=-(n+1)*gp/r-f/2
        ur=-(n+1)*gp/r*np.cos((n+1)*th);ut=gpd*np.sin((n+1)*th)
        psi=gp*np.sin((n+1)*th)
        if n>=3:
            gm=np.exp((n-1)*logr+(1-beta)*log1)/(4*(beta-1));gmd=(n-1)*gm/r-f/2
            ur-= (n-1)*gm/r*np.cos((n-1)*th);ut+=gmd*np.sin((n-1)*th)
            psi+=gm*np.sin((n-1)*th)
        fields['ux'][:,b]=ur*ct-ut*st;fields['uy'][:,b]=ur*st+ut*ct;fields['psi'][:,b]=psi
    if not all(np.isfinite(v).all() for v in fields.values()): raise FloatingPointError('basis nonfinite')
    return fields

def residual(fields,coefs,x,y,cl):
    d={k:v@coefs for k,v in fields.items()};vx=cl*x+d['ux'];vy=cl*y+d['uy']
    R=vx*d['dx']+vy*d['dy']-d['rho']
    Nf=np.abs(vx*d['dx'])+np.abs(vy*d['dy'])+np.abs(d['rho'])
    Nv=np.abs(d['rho'])+np.abs(x*d['dx']+y*d['dy'])+np.abs(d['ux']*d['dx']+d['uy']*d['dy'])
    Jac=vx[:,None]*fields['dx']+vy[:,None]*fields['dy']+d['dx'][:,None]*fields['ux']+d['dy'][:,None]*fields['uy']-fields['rho']
    return R,Nf,Nv,Jac,d
