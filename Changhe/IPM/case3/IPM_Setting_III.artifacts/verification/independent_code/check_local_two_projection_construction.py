#!/usr/bin/env python3
"""Independent sparse-polynomial and rational checks of verifier result109."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/local_two_projection_construction/verification'
COUNT=0

def check(b):
    global COUNT
    COUNT+=1
    if not b: raise AssertionError(f'check{COUNT}')

class P:
    def __init__(self,v=0):
        if isinstance(v,P):self.d=v.d.copy()
        elif isinstance(v,str):self.d={(v,):F(1)}
        elif isinstance(v,dict):self.d={tuple(sorted(k)):F(x) for k,x in v.items() if x}
        else:self.d={():F(v)} if v else {}
    def __add__(self,b):
        b=P(b);d=self.d.copy()
        for k,v in b.d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        b=P(b);d={}
        for k,v in self.d.items():
            for l,w in b.d.items():
                m=tuple(sorted(k+l));d[m]=d.get(m,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,n):return self*F(1,n)
    def __pow__(self,n):
        r=P(1)
        for _ in range(n):r=r*self
        return r
    def __eq__(self,b):return self.d==P(b).d
    def substitute(self,mapping):
        out=P(0)
        for mon,c in self.d.items():
            term=P(c)
            for x in mon:term*=mapping.get(x,P(x))
            out+=term
        return out
    def coeff(self,x,n):
        return P({tuple(y for y in mon if y!=x):c for mon,c in self.d.items() if mon.count(x)==n})
    def derivative(self,mapping):
        out=P(0)
        for mon,c in self.d.items():
            for i,x in enumerate(mon):
                term=P({mon[:i]+mon[i+1:]:c})*mapping.get(x,0)
                out+=term
        return out
    def scalar(self):
        check(not any(mon for mon in self.d));return self.d.get((),F(0))


def main():
    started=time.monotonic()
    names='f g k T S J K L df dg dk c a lam H z f2 g2 f4 g4'.split()
    v={s:P(s) for s in names}
    f,g,k,T,S,J,K,L,df,dg,dk,c,a,lam,H,z,f2,g2,f4,g4=[v[s] for s in names]
    D=c-1;u=(T-J)/2;vv=(S-K)/2;w=-L/2
    dot={'T':-g,'S':2*S-k,'J':f-4*J,'K':g-6*K,'L':k-8*L,'f':df,'g':dg,'k':dk}
    hm={2:u,4:vv,6:w};fm={1:f,3:g,5:k};dfm={1:df,3:dg,5:dk}
    source={}
    for m in (2,4,6):
        source[m]=((2-m)*fm.get(m-1,P())+dfm.get(m-1,P())+(m+2)*fm.get(m+1,P())+dfm.get(m+1,P()))/2
        dh=hm[m].derivative(dot);ddh=dh.derivative(dot)
        check(-ddh-4*dh+(m*m-4)*hm[m]==source[m])
    R={j:c*dfm[j]+D*fm[j] for j in fm}
    def add_sine(n,expr):
        if n:
            sign=1 if n>0 else -1;n=abs(n)
            R[n]=R.get(n,P())+sign*expr
    for m,h in hm.items():
        dh=h.derivative(dot)
        for j,Fj in fm.items():
            # cos(m)*sin(j) and sin(m)*cos(j), with signed negative modes retained.
            term=-m*h*(Fj+dfm[j])/2
            add_sine(j+m,term);add_sine(j-m,term)
            term=j*(2*h+dh)*Fj/2
            add_sine(m+j,term);add_sine(m-j,term)
    B=-u-K+S;C=K-3*L/2-S
    F1=(D+T)*f-f*f/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
    F3=(J+2*S)*f-f*f/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
    expected={1:(c+u)*df+B*dg+C*dk+F1,
              3:B*df+(c-3*L/2)*dg-u*dk+F3,
              5:c*dk+D*k+C*df-u*dg+(2*J+T)*g+2*K*f-f*g-f*k/2-3*g*g/4}
    for j in (1,3,5):check(R[j]==expected[j])
    check(R[5]!=-expected[5])
    # The local jet substitution is separate from the source projection derivation.
    local={'f':a+f2*z+f4*z*z,'g':g2*z+g4*z*z,'k':P(0),
           'T':a/4-D-g2*z/2-g4*z*z/4,'S':H*z,
           'J':a/4+f2*z/6+f4*z*z/8,'K':g2*z/8+g4*z*z/10,'L':P(0),
           'df':2*f2*z+4*f4*z*z,'dg':2*g2*z+4*g4*z*z,'dk':P(0)}
    jet={j:R[j].substitute(local) for j in (1,3,5)}
    def matrix(n):
        la=F(2*n)
        return [(c+1)*la/2-a/4,D*la/2+2*D-a/4-a/la,
                D*la/2-a/4+a/(la+4),c*la+D-a/2]
    A,Bm,Cm,Dm=matrix(1)
    check(jet[1].coeff('z',0)==0);check(jet[3].coeff('z',0)==0)
    check(jet[1].coeff('z',1)==A*f2+Bm*g2)
    check(jet[3].coeff('z',1)==Cm*f2+Dm*g2+2*H*a)
    A4,B4,C4,D4=matrix(2)
    Q1=6*H*g2-5*f2*f2/12-f2*g2/2+3*g2*g2/2
    Q3=4*H*f2+f2*f2/12-f2*g2/4
    check(jet[1].coeff('z',2)==A4*f4+B4*g4+Q1)
    check(jet[3].coeff('z',2)==C4*f4+D4*g4+Q3)
    check(jet[5].coeff('z',0)==0);check(jet[5].coeff('z',1)==0)
    check(jet[5].coeff('z',2)==-2*H*f2+(D-a/20)*g4-3*g2*g2/4)
    check(jet[1].coeff('z',2)!=A4*f4+B4*g4-Q1)
    # Generic symbolic determinant after exact cancellation of lambda denominators.
    diag=((c+1)*lam/2-a/4)*(c*lam+D-a/2)
    off=D*D*lam*(lam+4)/4-D*a*(lam+2)/4+a*a/16
    I=a*a-4*((c+2)*lam-D)*a+4*(c*c+4*c-1)*lam*lam-8*D*(c-3)*lam
    check(16*(diag-off)==I)
    Fell=a*a-(4*c+20)*a+128*c-64
    NF=-24*H*a*(a-4*c+4);NG=8*H*a*(a-4*c-4)
    check(A*NF+Bm*NG==0)
    check(Cm*NF+Dm*NG+2*H*a*Fell==0)
    check(NF+3*NG==-192*H*a)
    check(NF-NG==-32*H*a*(a-4*c+2))
    bnum=NF+3*NG;enum=NF-NG
    check(6*enum==(a-4*c+2)*bnum)
    check(H*a*Fell==enum-a*(5*bnum+3*enum)/96)
    # Clear the common denominator F^2 I(a,4); coefficient equality proves each C5 identity.
    Q1num=6*H*NG*Fell-5*NF*NF/12-NF*NG/2+3*NG*NG/2
    Q3num=4*H*NF*Fell+NF*NF/12-NF*NG/4
    I4=I.substitute({'lam':4})
    g4num=16*(C4*Q1num-A4*Q3num)
    C5num=-2*H*NF*Fell*I4+(D-a/20)*g4num-3*NG*NG*I4/4
    p2=15*a**4-920*a**3+19360*a*a-165312*a+491520
    check(5*C5num.substitute({'c':2})==-384*H*H*a*p2)
    check(C5num.substitute({'c':3})==-384*H*H*a*(a-16)*(3*a-32)*I4.substitute({'c':3}))
    shift=p2.substitute({'a':128+z})
    check(all(coef>0 for coef in shift.d.values()))
    check(all(coef>0 for coef in (a*a-60*a+736).substitute({'a':128+z}).d.values()))
    check(Fell.substitute({'c':2})==(a-12)*(a-16))
    check(Fell.substitute({'c':3})==(a-16)**2+64)
    # Exact rational spot checks include near-resonant inputs, signs, and the missing-plus control.
    samples=[]
    for ell in (2,3):
        for av in [F(128),F(257,2),F(16385,128),F(257),F(10001,3)]:
            if ell==3:av-=100
            for hv in [F(1,7),F(1),F(5,2)]:
                sub={'c':ell,'a':av,'H':hv}
                fv=Fell.substitute(sub).scalar()
                f2v=NF.substitute(sub).scalar()/fv;g2v=NG.substitute(sub).scalar()/fv
                m=[entry.substitute(sub).scalar() for entry in matrix(2)]
                q1=Q1.substitute({'H':hv,'f2':f2v,'g2':g2v}).scalar()
                q3=Q3.substitute({'H':hv,'f2':f2v,'g2':g2v}).scalar()
                determinant=m[0]*m[3]-m[1]*m[2]
                check(determinant!=0)
                f4v=(-m[3]*q1+m[1]*q3)/determinant
                g4v=(m[2]*q1-m[0]*q3)/determinant
                supplied=sub|{'f2':f2v,'g2':g2v,'f4':f4v,'g4':g4v}
                for j in (1,3):
                    for n in (0,1,2):check(jet[j].coeff('z',n).substitute(supplied)==0)
                cv=jet[5].coeff('z',2).substitute(supplied).scalar()
                check(cv<0)
                check(f2v+3*g2v<0 and f2v-g2v<0)
                samples.append({'ell':ell,'a':str(av),'H':str(hv),'f2':str(f2v),'g2':str(g2v),'f4':str(f4v),'g4':str(g4v),'C5':str(cv)})
    # sqrt(2) arithmetic: rational and irrational coefficients of every sampled indicial value.
    for ell in (2,3):
        for base in range(128 if ell==2 else 16,133 if ell==2 else 21):
            for n in range(1,81):
                la=2*n;d=ell-1;bb=(ell+2)*la-d
                cc=(ell*ell+4*ell-1)*la*la-2*d*(ell-3)*la
                rational=base*base+2-4*bb*base+4*cc
                irrational=2*base-4*bb
                check(rational!=0 or irrational!=0)
    proof=OUT.parent/'PROOF.md';before=json.loads((OUT/'proof_before_code.json').read_text())
    check(hashlib.sha256(proof.read_bytes()).hexdigest()==before['sha256'])
    result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':COUNT,'elapsed_seconds':time.monotonic()-started,
            'proof_sha256':before['sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'method':'Own sparse commutative polynomial algebra, signed sine product assignment, independent modal Poisson identity, cleared-denominator identities and exact Fraction evaluations',
            'symbolic_residual_term_counts':{j:len(R[j].d) for j in R},
            'positive_shifted_C2_polynomial':{str(mon):str(coef) for mon,coef in shift.d.items()},
            'samples':samples,'scope':'Local projected nonprofiles. No numerical BVP or full profile is certified.'}
    (OUT/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['utc','verdict','checks','elapsed_seconds','symbolic_residual_term_counts']}))
if __name__=='__main__':main()
