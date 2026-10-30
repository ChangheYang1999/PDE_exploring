"""Independent exact radial-polynomial Fourier arithmetic for case4 potentials."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from flint import fmpq,fmpq_poly,arb,acb,ctx
import json
import sys
sys.set_int_max_str_digits(0)
T=fmpq_poly([0,1]); U=fmpq_poly([1,-1]); ZERO=fmpq_poly([])

def q(x):
    v=Fraction(str(x));return fmpq(v.numerator,v.denominator)
def ar(x): return arb(x.numerator)/arb(x.denominator)
def pshift(P,k):
    assert all(P[i]==0 for i in range(k))
    return fmpq_poly(list(P)[k:])
def put(out,key,P):
    if P:out[key]=out.get(key,ZERO)+P

def fold_put(out,j,n,P,kind):
    if n==0 and kind=='s':return
    if n<0:n,P=-n,(-P if kind=='s' else P)
    put(out,(j,n),P)

def combine(A,B,scale=1):
    out=A.copy()
    for key,P in B.items():put(out,key,P*scale)
    return {key:P for key,P in out.items() if P}

class Radial:
    def __init__(self,state):
        if isinstance(state,(str,Path)):state=json.loads(Path(state).read_text())
        self.state=state;self.c=q(state['cl']);self.g=1/self.c;self.delta=1-self.g
        self.p={j:(3+self.g-j*self.delta)/2 for j in set(key[0] for key in state['order'])}
        arrays={}
        for (j,m,k),a in zip(state['order'],state['coefficients']):
            key=(j,2*m)
            if key not in arrays:arrays[key]=[]
            arrays[key]+=[fmpq(0)]*max(0,k+1-len(arrays[key]));arrays[key][k]+=q(a)
        self.derivatives={(0,0):{key:fmpq_poly(a) for key,a in arrays.items()}}
        self.shifted={}
        self.rho=combine(self.deriv(2,1),self.deriv(0,3));self.rho={k:-v for k,v in self.rho.items()}
        self.u1={k:-v for k,v in self.deriv(1,2).items()};self.u2=self.deriv(2,1)
        self.rx={k:-v for k,v in combine(self.deriv(3,1),self.deriv(1,3)).items()}
        self.ry={k:-v for k,v in combine(self.deriv(2,2),self.deriv(0,4)).items()}
        self.fields={'rho':(self.rho,3,'s'),'u1':(self.u1,3,'c'),'u2':(self.u2,3,'s'),
                     'rho_x':(self.rx,4,'s'),'rho_y':(self.ry,4,'c'),
                     'chi22':(self.deriv(2,2),4,'c'),'chi04':(self.deriv(0,4),4,'c'),
                     'chi31':(self.deriv(3,1),4,'s')}

    def deriv(self,x,y):
        key=(x,y)
        if key in self.derivatives:return self.derivatives[key]
        prev=(x,y-1) if y else (x-1,y)
        axis='y' if y else 'x';A=self.deriv(*prev);d=sum(prev);kind='s' if prev[1]%2 else 'c'
        target=('c' if kind=='s' else 's') if axis=='y' else kind
        out={}
        for (j,n),P in A.items():
            TP=T*P.derivative();common=TP+T*(self.p[j]*P-TP)
            minus=common+fmpq(n-d,2)*P;plus=common-fmpq(n+d,2)*P
            if axis=='y':
                minus*=1 if kind=='s' else -1;plus*=-1 if kind=='s' else 1
            fold_put(out,j,n-1,minus,target);fold_put(out,j,n+1,plus,target)
        self.derivatives[key]={key:P for key,P in out.items() if P}
        return self.derivatives[key]

    def residual_quotient(self):
        # The exact sine numerator F/r; division by sin(theta) follows below.
        sine={}
        for (j,n),P in self.rho.items():
            TP=T*P.derivative()
            L=self.c*(2*TP-3*P+2*T*(self.p[j]*P-TP))-P
            put(sine,(j,n),pshift(L,2))
        quad={}
        def multiply(C,S):
            for (i,n),P in C.items():
                for (j,m),Q in S.items():
                    V=P*Q/2
                    fold_put(quad,i+j+1,m+n,V,'s');fold_put(quad,i+j+1,m-n,V,'s')
        multiply(self.u1,self.rx);multiply(self.ry,self.u2)
        for key,P in quad.items():put(sine,key,pshift(P,4))
        cos={}
        for (h,n),P in sine.items():
            if not P:continue
            assert n%2==1
            put(cos,(h,0),P)
            for k in range(2,n,2):put(cos,(h,k),2*P)
        return {key:P for key,P in cos.items() if P}

    def poly_arb(self,P,t,u):
        # Choose the nearer endpoint; cached exact shift avoids cancellation at infinity.
        if t<arb('0.5'):coeffs=list(P);v=t
        else:
            key=tuple(P)
            if key not in self.shifted:self.shifted[key]=list(P(U))
            coeffs=self.shifted[key];v=u
        ans=arb(0)
        for c in reversed(coeffs):ans=ans*v+ar(c)
        return ans

    def evaluate(self,x,y):
        x=ar(q(x));y=ar(q(y));r2=x*x+y*y;r=r2.sqrt();R=1+r2;t=r2/R;u=1/R
        assert r>0
        z=acb(x/r,y/r);powers=[acb(1)]
        maxn=max(n for A,d,kind in self.fields.values() for j,n in A)
        for _ in range(maxn):powers.append(powers[-1]*z)
        rp={j:R**ar(p) for j,p in self.p.items()};rd={d:r**(-d) for d in (3,4)}
        values={}
        for name,(A,d,kind) in self.fields.items():
            val=arb(0)
            for (j,n),P in A.items():
                trig=powers[n].real if kind=='c' else powers[n].imag
                val+=rp[j]*rd[d]*self.poly_arb(P,t,u)*trig
            values[name]=val
        c=ar(self.c);values['residual']=(c*x+values['u1'])*values['rho_x']+(c*y+values['u2'])*values['rho_y']-values['rho']
        values['M11']=2*c+1-2*values['chi22']-values['chi04']
        values['M22']=2*c+1+values['chi22'];values['M12']=values['chi31']
        values['lambda_min_M']=(values['M11']+values['M22']-((values['M11']-values['M22'])**2+4*values['M12']**2).sqrt())/2
        return values
