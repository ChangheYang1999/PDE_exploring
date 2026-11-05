"""Exact-source polar evaluator for Candidate 013, with Arb radial enclosures.

No inherited file is modified.  Exact rational polynomial grouping precedes all
evaluation, and radial differentiation uses Arb power series.  Angular
synthesis with numpy is explicitly FLOAT; `modes_at` retains Arb enclosures.
The base007/raw-phi identity uses the inherited exact quotient identity.
"""
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse
import json
import math
import time
import sys
from flint import fmpq as Q, fmpq_poly, arb, arb_series, ctx
import numpy as np

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
IPM = HERE.parents[2]
BASE007 = IPM/'combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json'
PHI013 = IPM/'combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json'
C = Q(4076476460239181,2251799813685248)
SOURCE_HASHES = {'base007':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21',
                'phi013':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'}

@lru_cache(None)
def legendre(n):
    return fmpq_poly([(-1)**(n-k)*math.comb(n,k)*math.comb(n+k,k) for k in range(n+1)])

def rational_arb(q):
    return arb(q.numerator)/arb(q.denominator)

def load_groups():
    """Each group is kind,n,b,t,v,P: r^n(1+r²)^b(t+r²)^-v P(r²/(t+r²))."""
    groups=defaultdict(lambda:fmpq_poly())
    raw=BASE007.read_bytes(); assert sha256(raw).hexdigest()==SOURCE_HASHES['base007']
    data=json.loads(raw); assert Q(data['cl_exact'])==C
    for row in data['generators']:
        n=2*row['m']; j=row['j']; p=(3+1/C-j*(1-1/C))/2
        sp=row['spec']; a=Q(row['coef'])
        if sp[0]=='mono': poly=fmpq_poly([0]*sp[1]+[1])
        else:
            assert sp[0]=='leg'
            poly=legendre(sp[2]).left_shift(sp[1])
        groups['c',n,p-row['m'],Q(1),0]+=a*poly
    raw=PHI013.read_bytes(); assert sha256(raw).hexdigest()==SOURCE_HASHES['phi013']
    data=json.loads(raw); assert Q(data['c_exact'])==C
    for row in data['atoms']:
        n,h,d=row['n'],row['h'],row['d']; b,t=Q(row['b_exact']),Q(row['scale_exact'])
        assert n>0 and n%2==1 and h>=0 and d>=0 and t>0
        poly=legendre(row.get('legendre_degree',0)).left_shift(h)
        groups['s',n,b,t,d-h]+=Q(row['coefficient_exact'])*poly
    return [(kind,n,b,t,v,p) for (kind,n,b,t,v),p in sorted(groups.items()) if p]

def addterm(out,key,value):
    if not value:return
    a,b,n,kind=key
    if n<0:n=-n;value=-value if kind=='s' else value
    if n==0 and kind=='s':return
    key=a,b,n,kind;out[key]=out.get(key,Q(0))+value
    if not out[key]:del out[key]

def cartesian_diff(series,axis):
    out={}
    for (a,b,n,kind),v in series.items():
        # radial derivative times cos(theta) or sin(theta)
        rad=[(a+1,b,v),(a,b+1,-b*v)]
        for aa,bb,vv in rad:
            if axis=='x':
                addterm(out,(aa,bb,n+1,kind),vv/2); addterm(out,(aa,bb,n-1,kind),vv/2)
            elif kind=='s':
                addterm(out,(aa,bb,n-1,'c'),vv/2);addterm(out,(aa,bb,n+1,'c'),-vv/2)
            else:
                addterm(out,(aa,bb,n+1,'s'),vv/2);addterm(out,(aa,bb,n-1,'s'),-vv/2)
        # angular derivative times -sin(theta)/r or cos(theta)/r
        kk='c' if kind=='s' else 's';vv=v*n*(1 if kind=='s' else -1)
        if axis=='y':
            addterm(out,(a,b+1,n+1,kk),vv/2);addterm(out,(a,b+1,n-1,kk),vv/2)
        elif kk=='s':
            addterm(out,(a,b+1,n-1,'c'),-vv/2);addterm(out,(a,b+1,n+1,'c'),vv/2)
        else:
            addterm(out,(a,b+1,n+1,'s'),-vv/2);addterm(out,(a,b+1,n-1,'s'),vv/2)
    return out

@lru_cache(None)
def derivative_series(kind,n,i,j):
    series={(0,0,n,kind):Q(1)}
    for axis in 'x'*i+'y'*j:series=cartesian_diff(series,axis)
    return series

def linear_combination(*rows):
    out=defaultdict(lambda:arb(0))
    for factor,modes in rows:
        for key,v in modes.items():out[key]+=factor*v
    return dict(out)

class Evaluator:
    def __init__(self,precision=384,max_density_order=1,max_velocity_order=1):
        ctx.prec=precision
        self.precision=precision
        self.groups=load_groups()
        self.order=max(3+max_density_order,3+max_velocity_order)
        self.max_density_order=max_density_order
        self.max_velocity_order=max_velocity_order
        self.prepared=[]
        for kind,n,b,t,v,p in self.groups:
            self.prepared.append((kind,n,rational_arb(b),rational_arb(t),v,[arb(c) for c in p.coeffs()]))

    def potential_series(self,r,order=None):
        """Arb Taylor series G(r+z), grouped before differentiation."""
        ctx.prec=self.precision
        order=self.order if order is None else order
        # python-flint operations additionally obey the process-global cap.
        # Raising only individual series.prec silently truncates products.
        ctx.cap=order+1
        r=arb(r);rr=arb_series([r,1],prec=order+1);s=rr*rr;oneps=1+s
        out=defaultdict(lambda:arb_series([],prec=order+1))
        powers={};rpowers={};zpowers={}
        for kind,n,b,t,v,coeffs in self.prepared:
            tk=t.str(self.precision)
            if tk not in zpowers:zpowers[tk]=s/(t+s)
            z=zpowers[tk]
            p=arb_series([],prec=order+1)
            for a in reversed(coeffs):p=p*z+a
            bk=b.str(self.precision)
            if bk not in powers:powers[bk]=oneps**b
            if n not in rpowers:rpowers[n]=rr**n
            out[kind,n]+=rpowers[n]*powers[bk]*(t+s)**(-v)*p
        return dict(out)

    def potential_jets(self,r):
        """Arb derivatives G^(a)(r) grouped by angular harmonic of chi/phi."""
        out=self.potential_series(r)
        return {key:[p[a]*math.factorial(a) for a in range(self.order+1)] for key,p in out.items()}

    def mode_majorants(self,r):
        """Cauchy majorants on |z-r|<=r/8, using a potential disk r/4.

        On the outer disk, Re(t+z²)>=t+r²/2>0 for every t>0,
        so all powers have a single analytic branch.  Every potential group
        is bounded by its explicit coefficient absolute sum.  Cauchy's
        derivative estimate and |z|>=7r/8 bound the polar differentiation.
        """
        r=arb(r);outer=r/4;inner=r/8
        assert r>0 and outer>inner>0
        hi=r+outer;lo=1+r*r/2;up=1+hi*hi
        pm=defaultdict(lambda:arb(0))
        for (kind,n,b,t,v,p),prepared in zip(self.groups,self.prepared):
            coeffs=prepared[-1];tl=t+r*r/2;tu=t+hi*hi
            # Explicit analyticity witness: every t+z² lies in the open
            # right half-plane on the enclosing complex disk.
            assert lo>0 and tl>0 and t>0
            zmax=hi*hi/tl
            poly=arb(0)
            for a in reversed(coeffs):poly=poly*zmax+a.abs_upper()
            factor=(lo if b<0 else up)**rational_arb(b)
            factor*=((tl if v>=0 else tu)**(-v))*hi**n*poly
            pm[kind,n]+=factor
        # Bounds for each differentiated potential coefficient on the inner disk.
        bounds={}
        for kind in ['c','s']:
            for total in range(self.order+1):
                for i in range(total+1):
                    j=total-i;dest=defaultdict(lambda:arb(0))
                    for (kk,n),bound in pm.items():
                        if kk!=kind:continue
                        for (a,b,N,t),v in derivative_series(kind,n,i,j).items():
                            dest[t,N]+=arb(abs(v))*math.factorial(a)*bound/(outer-inner)**a/(r-inner)**b
                    bounds[kind,i,j]=dict(dest)
        out={}
        for total in range(self.max_density_order+1):
            for i in range(total+1):
                j=total-i
                out['rho',i,j]=linear_combination((1,bounds['c',i+2,j+1]),(1,bounds['c',i,j+3]),
                                                  (1,bounds['s',i+2,j]),(1,bounds['s',i,j+2]))
        for total in range(self.max_velocity_order+1):
            for i in range(total+1):
                j=total-i
                out['u1',i,j]=linear_combination((1,bounds['c',i+1,j+2]),(1,bounds['s',i+1,j+1]))
                out['u2',i,j]=linear_combination((1,bounds['c',i+2,j+1]),(1,bounds['s',i+2,j]))
        return out,inner

    def modes_taylor(self,r,degree=40):
        """Taylor coefficients of the actual fields, after all cancellations."""
        r=arb(r);potseries=self.potential_series(r,degree+self.order)
        rr=arb_series([r,1],prec=degree+1)
        rpow={b:rr**(-b) for b in range(self.order+1)}
        gd={}
        for key,p in potseries.items():
            gd[key,0]=p
            for a in range(1,self.order+1):gd[key,a]=gd[key,a-1].derivative()
        pot={}
        for kind in ['c','s']:
            for total in range(self.order+1):
                for i in range(total+1):
                    j=total-i;dest=defaultdict(lambda:arb_series([],prec=degree+1))
                    for (kk,n),p in potseries.items():
                        if kk!=kind:continue
                        for (a,b,N,t),v in derivative_series(kind,n,i,j).items():
                            dest[t,N]+=arb(v)*gd[(kk,n),a]*rpow[b]
                    pot[kind,i,j]=dict(dest)
        out={}
        for total in range(self.max_density_order+1):
            for i in range(total+1):
                j=total-i
                out['rho',i,j]=linear_combination((-1,pot['c',i+2,j+1]),(-1,pot['c',i,j+3]),
                                                  (-1,pot['s',i+2,j]),(-1,pot['s',i,j+2]))
        for total in range(self.max_velocity_order+1):
            for i in range(total+1):
                j=total-i
                out['u1',i,j]=linear_combination((-1,pot['c',i+1,j+2]),(-1,pot['s',i+1,j+1]))
                out['u2',i,j]=linear_combination((1,pot['c',i+2,j+1]),(1,pot['s',i+2,j]))
        assert all(p.prec>=degree+1 for mm in out.values()for p in mm.values())
        return out

    def modes_cover(self,r,halfwidth,degree=40):
        """Rigorous whole-radius-interval enclosure using Taylor+Cauchy tail.

        Return (enclosed modes, metadata).  The center and halfwidth are
        positive Arb enclosures of exact real numbers; require halfwidth<r/8.
        """
        r=arb(r);halfwidth=arb(halfwidth)
        majorants,R=self.mode_majorants(r);z=halfwidth/R
        assert z<1
        series=self.modes_taylor(r,degree)
        v=arb(0,halfwidth.abs_upper());tailfactor=z**(degree+1)/(1-z)
        result={};largest=arb(0)
        for key,mm in series.items():
            out={}
            for harmonic,p in mm.items():
                val=arb(0)
                for c in reversed(p.coeffs()[:degree+1]):val=val*v+c
                tail=(majorants[key].get(harmonic,arb(0))*tailfactor).abs_upper()
                out[harmonic]=val+arb(0,tail)
                if tail>largest:largest=tail
            result[key]=out
        return result,{'degree':degree,'cauchy_radius':R.str(20),'max_remainder':largest.str(20)}

    def modes_at(self,r):
        """rho,u1,u2, and Cartesian derivatives as exact-source radial Arb modes.

        Return {(field,i,j): {(s_or_c,harmonic): Arb}}.  `r` may be any
        positive Arb interval. Interval evaluation encloses every radius in it.
        """
        r=arb(r); jets=self.potential_jets(r);rpow={b:r**(-b) for b in range(self.order+1)}
        pot={}
        for kind in ['c','s']:
            for total in range(self.order+1):
                for i in range(total+1):
                    j=total-i;dest=defaultdict(lambda:arb(0))
                    for (kk,n),jet in jets.items():
                        if kk!=kind:continue
                        for (a,b,N,t),v in derivative_series(kind,n,i,j).items():
                            dest[t,N]+=arb(v)*jet[a]*rpow[b]
                    pot[kind,i,j]=dict(dest)
        out={}
        for total in range(self.max_density_order+1):
            for i in range(total+1):
                j=total-i
                out['rho',i,j]=linear_combination((-1,pot['c',i+2,j+1]),(-1,pot['c',i,j+3]),
                                                  (-1,pot['s',i+2,j]),(-1,pot['s',i,j+2]))
        for total in range(self.max_velocity_order+1):
            for i in range(total+1):
                j=total-i
                out['u1',i,j]=linear_combination((-1,pot['c',i+1,j+2]),(-1,pot['s',i+1,j+1]))
                out['u2',i,j]=linear_combination((1,pot['c',i+2,j+1]),(1,pot['s',i+2,j]))
        return out

def synthesize(modes,theta):
    """FLOAT angular synthesis. Preserve the returned radial radius separately."""
    theta=np.asarray(theta);out=np.zeros(theta.shape);err=0.
    for (kind,n),value in modes.items():
        f=np.sin(n*theta) if kind=='s' else np.cos(n*theta)
        out+=float(value.mid())*f;err+=float(value.rad())
    return out,err

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--r',default='1');ap.add_argument('--theta',type=float,default=.5);ap.add_argument('--precision',type=int,default=384);args=ap.parse_args()
    tick=time.monotonic();e=Evaluator(args.precision);print('groups',len(e.groups),'load_seconds',time.monotonic()-tick,flush=True)
    modes=e.modes_at(args.r)
    print('radius',args.r,'elapsed',time.monotonic()-tick,flush=True)
    for key,m in modes.items():
        a,err=synthesize(m,args.theta);print(key,float(a),'radial_error',err,flush=True)

if __name__=='__main__':main()
