"""Independent exact checks of leading Poisson/transport jets and their thresholds."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s

def rf(x,n):
    p=Q(1)
    for j in range(n):p*=x+j
    return p
counts={}
for K in range(1,17):
    for eta in map(Q,['1/4','1/2','2/3','1','2','5']):
        A=1+Q(K)/eta;n=2*K+1
        for chi in [Q(-K)-Q(1,2),Q(1-K),Q(3,2)-K,Q(0),Q(1,3),Q(4)]:
            a=2*K-2*(A-1)*(chi-1)
            cs=[(-1)**j*comb(n,2*j)*rf(eta,j)*rf(chi+j,K-j) for j in range(K+1)]
            assert cs[-1]!=0
            for j in range(K):
                e=2*K+2*j*(A-1);ee=e+2*(A-1)
                assert (n-2*j)*(n-2*j-1)*e*cs[j]+(2*j+2)*(2*j+1)*(ee-a)*cs[j+1]==0
                counts['recurrence']=counts.get('recurrence',0)+1
            for J in range(K):
                moment=sum((-1)**j*comb(K,j)*rf(chi+j,K-j)*rf(chi+J,j) for j in range(K+1))
                assert moment==0
                counts['finite_differences']=counts.get('finite_differences',0)+1
            if eta>=Q(1,2) and chi>1-K:
                u=chi+K-1
                raw=sum(cs[j]*(-1)**j*rf(u,j)/rf(Q(-K)-Q(1,2),j)*rf(Q(1,2),j)/rf(eta,j) for j in range(K+1))
                assert raw==0
                counts['positive_law_moments']=counts.get('positive_law_moments',0)+1
# Independent polynomial differentiation checks the recurrence's converse.
x,y=s.symbols('x y');A,a=s.symbols('A a',real=True)
for n in [3,5,7,9,11]:
    K=(n-1)//2; cs=[s.S(0)]*K+[s.S(1)]
    for j in range(K-1,-1,-1):
        e=n-1+2*j*(A-1);ep=n-1+2*(j+1)*(A-1)
        cs[j]=s.factor((2*j+2)*(2*j+1)*(a-ep)*cs[j+1]/((n-2*j)*(n-2*j-1)*e))
    H=sum(cs[j]*x**(2*j)*y**(n-2*j) for j in range(K+1))
    V=A*x*s.diff(H,x)+y*s.diff(H,y)-H
    phi=s.integrate(V,x)
    assert s.factor(s.diff(phi,x,2)+s.diff(phi,y,2)-a*s.diff(H,x))==0
    counts['full_leading_PDE']=counts.get('full_leading_PDE',0)+1
H=y*(y*y-x*x/5)**2
V=11*x*s.diff(H,x)+y*s.diff(H,y)-H
phi=s.integrate(V,x)
assert s.expand(s.diff(phi,x,2)+s.diff(phi,y,2)+76*s.diff(H,x))==0
rho=-76*(y-H);psi=-5*x*y+phi;ux=-s.diff(psi,y);uy=s.diff(psi,x)
R=s.expand((6*x+ux)*s.diff(rho,x)+(6*y+uy)*s.diff(rho,y)-rho)
assert R!=0 and {sum(mon) for mon,coef in s.Poly(R,x,y).terms()}=={9}
negative={'H':str(H),'phi':str(phi),'residual':str(R)}
e1=2*A+2;e2=4*A;t=s.symbols('t')
P=t*t+2*(a-e2)*t/e1+(a-e1)*(a-e2)/(20*e1)
disc=(a-e2)*((20-e1)*a+e1*e1-20*e2)/(5*e1*e1)
assert s.factor(s.discriminant(P,t)-disc)==0
samples=[]
for Av in map(Q,['3/2','3','5','9','19/2','11','25']):
    threshold=2*(Av*Av-18*Av+1)/(Av-9) if Av>9 else None
    avals=[Q(-1000),Q(-100),Q(-76),Q(-1),Q(0),2*Av+2,4*Av-1,4*Av,4*Av+1]
    if threshold is not None:avals += [threshold-1,threshold,threshold+1]
    for av in avals:
        b=2*(av-4*Av)/(2*Av+2);c=(av-2*Av-2)*(av-4*Av)/(20*(2*Av+2))
        minimum=c if b>=0 else c-b*b/4
        expected=av>=4*Av or (Av>9 and av<=threshold)
        assert (minimum>=0)==expected
        samples.append({'A':str(Av),'a':str(av),'minimum':str(minimum),'nonnegative':expected})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','counts':counts,'quintic_rational_classification':samples,'negative_example':negative,'scope':'Exact finite supporting tests. The all-degree and full-profile implications are proved in PROOF.md with the extra sign, not inferred from this finite list.'}
p=Path('research/one_sided_jet_thresholds/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
