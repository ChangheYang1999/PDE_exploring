"""Independent exact checks of result92, no lead checker imported."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import random,json,hashlib
rng=random.Random(920021);items=[]
def equal(name,a,b):
    assert a==b,(name,a,b)
    items.append(name)
def require(name,p):
    assert p,name
    items.append(name)
def sc(a,b,l):
    return sum((F(1 if k>0 else -1,2)for k in [a+b,a-b]if abs(k)==l),F(0))
def modal_leading(N,A,a,alpha,beta,mode):
    ell=(A+1)/2;D=(A-1)/2
    density={1:{1:a,N+1:alpha},3:{N+1:beta}}
    stream={2:{2:-D/2,N+2:-(alpha/F(N+4)+beta/F(N))/2},4:{N+2:-beta/F(2*(N+6))}}
    out=(ell*(N+1)-1)*density.get(mode,{}).get(N+1,0)
    for j,bs in density.items():
        for k,ps in stream.items():
            for n,b in bs.items():
                for t,p in ps.items():
                    if n+t-2==N+1:
                        out+=(-k*n*p*b*sc(j,k,mode)+t*j*p*b*sc(k,j,mode))
    return out

for N in range(2,42,2):
    for trial in range(8):
        A=1+F(rng.randint(1,30),7);a=F(rng.randint(-30,50),9)
        alpha=F(rng.randint(-10,10),11);beta=F(rng.randint(-10,10),13)
        equal(f'direct R1 leading N{N} trial{trial}',4*modal_leading(N,A,a,alpha,beta,1),(N*(A+3)-a)*alpha+(N+4)*(A-1-a/N)*beta)
        equal(f'direct R3 leading N{N} trial{trial}',4*modal_leading(N,A,a,alpha,beta,3),N*(A-1-a/(N+4))*alpha+2*((N+1)*A+N-1-a)*beta)
        E=A-1;d=F(rng.randint(1,40),13);a=N*(E+4/d);lam=N*(d-1)/F(N+4)
        row1=N*(A+3)-a+(N+4)*(A-1-a/N)*lam
        row2=N*(A-1-a/(N+4))+2*((N+1)*A+N-1-a)*lam
        equal(f'first elimination N{N} trial{trial}',row1,F(0))
        equal(f'second elimination N{N} trial{trial}',row2,F(2*N,N+4)*(E*(d+1)+2*N*(d-3+1/d)))

# Exact roots-of-unity calculation: zeta=e^(pi i/6), Phi12=z^4-z^2+1.
def modpoly(p):
    p=list(p)
    while len(p)>4:
        k=len(p)-1;v=p.pop()
        p[k-2]+=v;p[k-4]-=v
    return p+[0]*(4-len(p))
def zpow(k):
    k%=12;p=[0]*k+[1];return modpoly(p)
for k in range(-5,6):
    val=[sum(zpow(k*(2*j+1))[h]for j in range(6))for h in range(4)]
    equal(f'six-point Fourier degree{k}',val,[6,0,0,0]if k==0 else[0,0,0,0])

for N in range(8,202,2):
    d=F(2*N+4,N)
    f=2*(-d*d+3*d-1)/(d*(d+1))
    equal(f'right-endpoint F N{N}',N*f,F(N*(N*N-4*N-16),(3*N+4)*(N+2)))
    equal(f'strict bound difference N{N}',N*f-F(N,3)+F(22,9),F(52*N+176,9*(3*N+4)*(N+2)))
    require(f'positive difference N{N}',N*f>F(N,3)-F(22,9))
    L=F(2*N-4,3*N)
    fl=2*(-L*L+3*L-1)/(L*(L+1))
    require(f'endpoint comparison N{N}',fl>=F(2,3) and f<=F(1,3) and L>=F(1,2))
for numerator in range(1,51):
    d=F(numerator,13)
    P=2*(-d*d+3*d-1);Pd=2*(-2*d+3);Q=d*(d+1);Qd=2*d+1
    equal(f'F derivative d={d}',(Pd*Q-P*Qd)/Q**2,(-8*d*d+4*d+2)/(d*d*(d+1)**2))
require('sqrt3 rational lower bound',49>48)
require('sqrt5 comparison',49>45)
for N in range(4,100,2):
    require(f'positive-z lower bound N{N}',F(N*N,N+3)-2>0)

root=Path('research/projected_one_sided_audit');out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=len(items),items=items,proof_sha256=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),source_sha256=hashlib.sha256((root/'verification/MEL2_SOURCE.md').read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact algebra support for four independently written proofs; inequalities with arbitrary parameters and analytic boundary arguments are proved in PROOF.md.')
(root/'verification/exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='items'}))
