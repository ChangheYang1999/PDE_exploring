"""Generic Cartesian Arb Taylor jets for refit audit, using canonical coefficients."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
from datetime import datetime, timezone
import json, sys
from flint import arb, acb, ctx
ctx.prec=384
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]

def aa(v):
    if isinstance(v,arb):return v
    v=Q(v);return arb(v.numerator)/arb(v.denominator)

def multiply(a,b,order):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=order:c[i+k,j+l]=c.get((i+k,j+l),arb(0))+v*w
    return c

class Potential:
    def __init__(self,data,order=6):
        self.order=order
        self.indices=[(i,j) for i in range(order+1) for j in range(order+1-i)]
        self.c=aa(data.get('cl',data.get('exact_parameters',{}).get('cl')))
        self.gamma=1/self.c
        self.groups={}
        for (j,m,k),v in zip(data['canonical_order'],data['canonical_coefficients']):self.groups.setdefault((j,m),[]).append((k-m,aa(v)))
    def fields(self,x,y):
        x,y=aa(x),aa(y);q=x*x+y*y;assert q>0
        oq=1+q;v=q/oq;o=self.order
        delta={(1,0):2*x,(0,1):2*y,(2,0):arb(1),(0,2):arb(1)}
        dq=[{(0,0):arb(1)}]
        for _ in range(o):dq.append(multiply(dq[-1],delta,o))
        maxm=max(m for j,m in self.groups);z=acb(x,y)
        zp=[acb(1)]
        for _ in range(2*maxm):zp.append(zp[-1]*z)
        harmonic={}
        for m in set(m for j,m in self.groups):
            n=2*m;t={}
            for i,j in self.indices:
                if i+j<=n:
                    w=zp[n-i-j]
                    t[i,j]=aa(Q(factorial(n),factorial(n-i-j)*factorial(i)*factorial(j)))*[w.real,-w.imag,-w.real,w.imag][j%4]
            harmonic[m]=t
        chi={ij:arb(0) for ij in self.indices}
        for (j,m),terms in self.groups.items():
            p=(3+self.gamma-j*(1-self.gamma))/2
            pref=oq**(p-m);rad=[arb(0) for _ in range(o+1)]
            for ell,a in terms:
                base=a*pref*v**ell;u=p-m-ell
                qa=[aa(comb(ell,n))/q**n if n<=ell else arb(0) for n in range(o+1)]
                ob=[arb(1)]
                for n in range(1,o+1):ob.append(ob[-1]*(u-n+1)/(n*oq))
                for n in range(o+1):rad[n]+=base*sum((qa[k]*ob[n-k] for k in range(n+1)),arb(0))
            fj={ij:arb(0) for ij in self.indices}
            for n,rn in enumerate(rad):
                for ij,b in dq[n].items():fj[ij]+=rn*b
            tj=multiply(harmonic[m],fj,o)
            for ij,b in tj.items():chi[ij]+=b
        def D(i,j):return chi.get((i,j),arb(0))*factorial(i)*factorial(j)
        rho={};u=[{},{}]
        for i in range(o-2):
            for j in range(o-2-i):rho[i,j]=-D(i+2,j+1)-D(i,j+3)
        for i in range(o-2):
            for j in range(o-2-i):u[0][i,j]=-D(i+1,j+2);u[1][i,j]=D(i+2,j+1)
        F={}
        for i in range(o-3):
            for j in range(o-3-i):
                val=self.c*(x*rho[i+1,j]+y*rho[i,j+1]+(i+j)*rho[i,j])-rho[i,j]
                for a in range(i+1):
                    for b in range(j+1):
                        val+=comb(i,a)*comb(j,b)*(u[0][a,b]*rho[i-a+1,j-b]+u[1][a,b]*rho[i-a,j-b+1])
                F[i,j]=val
        m11=2*self.c+1-2*D(2,2)-D(0,4);m22=2*self.c+1+D(2,2);m12=D(3,1)
        return {'rho':rho[0,0],'rho_y':rho[0,1],'strain_DU22':D(2,2),'M_min':(m11+m22-((m11-m22)**2+4*m12*m12).sqrt())/2,'F':F[0,0],'F_x':F[1,0],'F_y':F[0,1],'F_xx':F[2,0],'F_xy':F[1,1],'F_yy':F[0,2]}

if __name__=='__main__':
    names=sys.argv[1:] or ['n12_m4','n12_m5']
    points=[('0','1/10'),('0','1'),('1','2'),('0','10'),('60','80'),('0','1000')]
    for name in names:
        d=json.loads((HERE/f'{name}_audit.json').read_text());s=Potential(d)
        rec=[]
        for x,y in points:
            f=s.fields(x,y);rec.append({'x':x,'y':y,'fields':{k:v.str(65) for k,v in f.items()}})
            print(name,x,y,'F',f['F'].str(20),'M',f['M_min'].str(20),flush=True)
        out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':d['source_sha256'],'precision_bits':ctx.prec,'points':rec,'scope':'individual-point enclosures only; not a continuum or norm certificate'}
        (HERE/f'{name}_points.json').write_text(json.dumps(out,indent=2)+'\n')
