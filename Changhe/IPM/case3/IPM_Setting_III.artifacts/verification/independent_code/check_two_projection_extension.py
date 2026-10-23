#!/usr/bin/env python3
"""Independent exact checks of result114; no producer/referee code is executed."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
from check_local_two_projection_construction import P
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/two_projection_extension_audit/verification'
COUNT=0

def check(value):
    global COUNT
    COUNT+=1
    if not value:raise AssertionError(f'check {COUNT}')

def scalar(v):
    v=P(v);check(not any(mon for mon in v.d));return v.d.get((),F(0))

def truncate(v,order=4):
    return P({mon:x for mon,x in P(v).d.items() if mon.count('z')<=order})

def residuals(f,g,k,T,S,J,K,L,df,dg,dk,c):
    D=c-1;u=(T-J)/2;v=(S-K)/2;w=-L/2
    dh={2:(-g-f+4*J)/2,4:(2*S-k-g+6*K)/2,6:(-k+8*L)/2}
    modes={1:f,3:g,5:k};dots={1:df,3:dg,5:dk}
    R={j:c*dots[j]+D*modes[j] for j in modes}
    def add(n,value):
        if n:R[abs(n)]=R.get(abs(n),P())+(1 if n>0 else -1)*value
    for m,h in {2:u,4:v,6:w}.items():
        for n,ff in modes.items():
            q=-m*h*(ff+dots[n])/2
            add(n+m,q);add(n-m,q)
            q=n*(2*h+dh[m])*ff/2
            add(m+n,q);add(m-n,q)
    return R

def main():
    start=time.monotonic()
    names='a c H j lam f g k T S J K L df dg dk fj gj kj eps z'.split()
    d={name:P(name) for name in names}
    a,c,H,j,lam,f,g,k,T,S,J,K,L,df,dg,dk,fj,gj,kj,eps,z=[d[name] for name in names]
    D=c-1;u=(T-J)/2;B=-u-K+S;C=K-3*L/2-S
    E=residuals(f,g,k,T,S,J,K,L,df,dg,dk,c)
    F1=(D+T)*f-f*f/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
    F3=(J+2*S)*f-f*f/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
    check(E[1]==(c+u)*df+B*dg+C*dk+F1)
    check(E[3]==B*df+(c-3*L/2)*dg-u*dk+F3)
    check(E[5]==c*dk+D*k+C*df-u*dg+(2*J+T)*g+2*K*f-f*g-f*k/2-3*g*g/4)
    # Two independent expressions for the exact source and derivative product signs.
    check(E[1]!=(c+u)*df+B*dg-C*dk+F1)
    for n in range(2,25):
        zn=z**n
        subst={'f':a+fj*zn,'g':gj*zn,'k':kj*zn,'T':a/4-D-gj*zn/(2*n),
               'S':-kj*zn/(2*n-2),'J':a/4+fj*zn/(2*n+4),
               'K':gj*zn/(2*n+6),'L':kj*zn/(2*n+8),
               'df':2*n*fj*zn,'dg':2*n*gj*zn,'dk':2*n*kj*zn}
        A=(c+1)*n-a/4;BB=D*n+2*D-a/4-a/(2*n)
        CC=D*n-a/4+a/(2*n+4);EE=2*c*n+D-a/2
        V=(n+3)*(D-a/(4*(n-1)))
        check(E[1].substitute(subst).coeff('z',n)==A*fj+BB*gj)
        check(E[3].substitute(subst).coeff('z',n)==CC*fj+EE*gj+V*kj)
        # Resonant compatibility (7), checked as a polynomial in arbitrary c.
        ar=4*D*(n-1)
        Ar=A.substitute({'a':ar});Br=BB.substitute({'a':ar})
        Cr=CC.substitute({'a':ar});Er=EE.substitute({'a':ar})
        check((Er*Ar-Cr*Br)*(c+2*n-1)==4*n*(2*c+n-2)*Ar)
        check(V.substitute({'a':ar})==0)
    # Prescribed g series, fully exact in epsilon, no assumed formula for f or k.
    cn=F(3);an=F(24);Dn=cn-1;Mn=an/4-Dn
    gc=[P(0)]*5;fc=[P(an)]+[P(0)]*4;kc=[P(0)]*5
    rising=P(1)
    for n in range(1,5):
        if n>1:rising=rising*(eps+n-1)/(n-1)
        gc[n]=2*Mn*eps*((-1)**(n-1))*rising
    hv=P(0)
    def jets():
        fs=sum((fc[n]*z**n for n in range(5)),P())
        gs=sum((gc[n]*z**n for n in range(1,5)),P())
        ks=sum((kc[n]*z**n for n in range(2,5)),P())
        ts=P(Mn)-sum((gc[n]*z**n/(2*n) for n in range(1,5)),P())
        ss=hv*z-sum((kc[n]*z**n/(2*n-2) for n in range(2,5)),P())
        js=P(an/4)+sum((fc[n]*z**n/(2*n+4) for n in range(1,5)),P())
        ksmall=sum((gc[n]*z**n/(2*n+6) for n in range(1,5)),P())
        ls=sum((kc[n]*z**n/(2*n+8) for n in range(2,5)),P())
        ds=[sum((2*n*x[n]*z**n for n in range(1,5)),P()) for x in (fc,gc,kc)]
        return {j:truncate(v) for j,v in residuals(fs,gs,ks,ts,ss,js,ksmall,ls,*ds,cn).items()}
    for n in range(1,5):
        A=(cn+1)*n-an/4
        fc[n]=-jets()[1].coeff('z',n)/A
        if n==1:hv=-jets()[3].coeff('z',1)/(2*an)
        elif n<4:
            V=(n+3)*(Dn-an/(4*(n-1)))
            kc[n]=-jets()[3].coeff('z',n)/V
        rr=jets()
        for jj in range(n+1):
            check(rr[1].coeff('z',jj)==0)
            if jj<4:check(rr[3].coeff('z',jj)==0)
    compat=jets()[3].coeff('z',4)
    target=32*eps*(289475*eps**3-21544*eps**2+1881*eps-720)/225
    check(compat==target)
    check(hv==2*eps/3)
    check(kc[2]==8*eps*(14*eps-1)/5)
    check(kc[3]==-32*eps*(413*eps**2-17*eps-5)/15)
    check(F(289475,1000)+F(1881,10)==F(477575,1000)<720)
    for n in range(1,101):check(scalar(compat.substitute({'eps':F(n,1000)}))<0)
    # Matrix, cubic, and all-c C5 identity with denominators cleared.
    FF=a*a-(4*c+20)*a+128*c-64
    GG=a*a-(12*c+36)*a+32*c*c+384*c-160
    I=a*a-4*((c+2)*lam-D)*a+4*(c*c+4*c-1)*lam*lam-8*D*(c-3)*lam
    diag=((c+1)*lam/2-a/4)*(c*lam+D-a/2)
    off=D*D*lam*(lam+4)/4-D*a*(lam+2)/4+a*a/16
    check(16*(diag-off)==I)
    check(I.substitute({'lam':4})==GG)
    nf=-24*H*a*(a-4*c+4);ng=8*H*a*(a-4*c-4)
    q1=6*H*ng*FF-5*nf*nf/12-nf*ng/2+3*ng*ng/2
    q3=4*H*nf*FF+nf*nf/12-nf*ng/4
    A4=2*(c+1)-a/4;C4=2*D-a/8
    g2num=16*(C4*q1-A4*q3)
    c5num=-2*H*nf*FF*GG+(D-a/20)*g2num-3*ng*ng*GG/4
    Pc=15*a**4+(200-560*c)*a**3+(6704*c*c-2320*c-2816)*a*a+(-29056*c**3-8512*c*c+63616*c-26048)*a+40960*c**4+61440*c**3-245760*c*c+184320*c-40960
    check(5*c5num==-384*H*H*a*Pc)
    check(c5num.substitute({'c':3})==-384*H*H*a*(a-16)*(3*a-32)*GG.substitute({'c':3}))
    # Rational sample signs supplement the analytic uniform estimates.
    signs=[]
    for cv in (F(10001,10000),F(3,2),F(2),F(3),F(17),F(10001)):
        for factor in (F(100),F(10001,100),F(101),F(1000)):
            av=factor*(cv+1);sub={'c':cv,'a':av}
            check(scalar(FF.substitute(sub))>0)
            check(scalar(GG.substitute(sub))>0)
            check(scalar(Pc.substitute(sub))>7*av**4)
            signs.append({'ell':str(cv),'a':str(av)})
    # Exact endpoint and exterior constants; polynomial coefficient sums.
    Q1=F1-D*f+C*dk;Q3=F3-D*g-u*dk
    check(sum(abs(v) for v in Q1.d.values())==F(123,4))
    check(sum(abs(v) for v in Q3.d.values())==F(57,4))
    check(F(3,2)*F(5,4)*F(1,4)-1==-F(17,32))
    check(72*9==648 and F(648,1296)==F(1,2))
    check(F(144)+F(720,10)==216)
    check(F(648,2)==324)
    for cv in (F(3,2),F(2),F(3),F(10)):
        alpha=(cv-1)/cv
        for frac in (F(1,4),F(1,2),F(3,4)):
            beta=alpha*frac;bb=3+1/beta;av=F(1,7)
            epsilon=min(cv/(30*bb),cv*(alpha-beta)/(1296*bb*bb),av/26)
            check(3*bb*epsilon<=cv/10)
            check(648*bb*bb*epsilon/(cv*(alpha-beta))<=F(1,2))
            check(13*epsilon<=av/2)
            check(max(1/beta,1/(4-beta),1/(6-beta))<=bb)
    source=json.loads((OUT/'source.json').read_text())
    check(hashlib.sha256((OUT/'external_PROOF.frozen.md').read_bytes()).hexdigest()==source['sha256'])
    before=json.loads((OUT/'proof_before_code.json').read_text())
    check(hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest()==before['sha256'])
    record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':COUNT,'elapsed_seconds':time.monotonic()-start,
            'source_sha256':source['sha256'],'proof_sha256':before['sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'polynomial_library_sha256':hashlib.sha256((ROOT/'independent_code/check_local_two_projection_construction.py').read_bytes()).hexdigest(),
            'compatibility_polynomial':{str(mon):str(x) for mon,x in compat.d.items()},'all_ell_sign_samples':signs,
            'method':'Independent signed Fourier product expansion and sparse Fraction polynomial operations. Forced Taylor recurrence constructed from projections, not imported coefficients. General C5 identity cleared exactly; exterior constants checked rationally.',
            'scope':'Supports separate analytic proofs; no global projected BVP connection or primary endpoint.'}
    (OUT/'exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({key:record[key] for key in ['utc','status','checks','elapsed_seconds']}))
if __name__=='__main__':main()
