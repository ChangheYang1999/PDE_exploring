"""Finite identities for the two-weight remainder. No PDE hypotheses inferred."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import sympy as S
from flint import arb, ctx, fmpq
B=Path(__file__).resolve().parents[1]
start=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==manifest['proof_sha256']
for name,digest in manifest['inputs'].items():assert sha(B/name)==digest,name
par=json.loads((B/'data/parameters.json').read_text());ctx.prec=par['bits']
checks=[]
def identity(name,z):
    assert S.cancel(S.trigsimp(S.expand(z)))==0,name
    checks.append(name)
x,y,u,v=S.symbols('x y u v',real=True)
r2=x*x+y*y
# pi-scaled kernel: removes pi from every exact identity.
K=S.Matrix([-x*y/r2**2,(x*x-y*y)/(2*r2**2)])
def directional(z):return z.diff(x)*u+z.diff(y)*v
D=directional(K);D3=directional(directional(D))
identity('kernel magnitude',K.dot(K)-1/(4*r2**2))
identity('kernel first directional derivative',D.dot(D)-(u*u+v*v)/r2**3)
identity('kernel third directional derivative',D3.dot(D3)-144*(u*u+v*v)**3/r2**5)
eps,A,Dg,r=S.symbols('eps A D r',positive=True)
a,q=S.symbols('a q',real=True)
Bnear=A*(r/2)**a;Lnear=Dg*(r/2)**(a+eps-1)
assert S.powsimp(Lnear*r/(4*Bnear)/(Dg/(2**(eps+1)*A)*r**eps),force=True)==1
checks.append('near-field logarithm argument')
C,L,k=S.symbols('C L k',positive=True)
J=A*r**(-eps)*(C+L*(1+S.log(k*r**eps)))
identity('active-branch J derivative',S.diff(J,r)+eps*A*r**(-eps-1)*(C+L*S.log(k*r**eps)))
t=S.symbols('t',real=True);chi=3*t*t-2*t**3
identity('cutoff monotonic derivative',S.diff(chi,t)-6*t*(1-t))
identity('cutoff upper bound factorization',1-chi-(1-t)**2*(1+2*t))
assert [chi.subs(t,j) for j in (0,1)]==[0,1]
assert [S.diff(chi,t).subs(t,j) for j in (0,1)]==[0,0]
checks.append('cutoff C1 endpoint values')
radial=(t+1)*S.diff(chi,t)
identity('cutoff radial critical derivative',S.diff(radial,t)-6*(1-3*t*t))
assert arb(3)>4/arb(3).sqrt()
checks.append('cutoff absolute radial derivative below three')
p,n=S.symbols('p n',real=True)
identity('generic exterior Green particular coefficient',-(1/(p+n)+1/(n-p))/(2*n)-1/(p*p-n*n))
identity('first-sine exterior tail coefficient',-(1/(q+3)-1/(q+1))/2-1/((q+1)*(q+3)))
th=S.symbols('theta',real=True)
# Generic polar Hessian, specialized to the decaying harmonic exponent.
h1=((p+n)*(p+n-2)*S.cos((n-2)*th)-(p-n)*(p-n-2)*S.cos((n+2)*th))/4
h2=-(p*p-n*n)*S.sin(n*th)/2-((p+n)*(p+n-2)*S.sin((n-2)*th)+(p-n)*(p-n-2)*S.sin((n+2)*th))/4
identity('harmonic mixed Hessian',h1.subs(p,-n)+n*(n+1)*S.cos((n+2)*th))
identity('harmonic negative xx Hessian',h2.subs(p,-n)+n*(n+1)*S.sin((n+2)*th))
identity('harmonic velocity magnitude',h1.subs(p,-n)**2+h2.subs(p,-n)**2-n*n*(n+1)**2)
psi=-y/(2*S.pi*r2)
identity('first moment compensation first component',S.diff(psi,x,y)+K[0].diff(y)/S.pi)
identity('first moment compensation second component',-S.diff(psi,x,2)+K[1].diff(y)/S.pi)
# Arithmetic fixture only. These are not campaign A,D or stationary bounds.
def ar(s):
    z=fmpq(s);return arb(z.p)/z.q
fixture=par['illustrative_fixture'];av=ar(fixture['a']);qv=ar(fixture['q']);ev=qv-av
Av=ar(fixture['A']);Dv=ar(fixture['D']);eta=ar(fixture['eta'])
assert av>-5 and av<-3 and qv>av and qv<0
Cv=arb(1)/2+arb(2)**(3-av)+arb(2)**(av+2)/(-av)+arb(2)**(-av-2)/(-av-3)+arb(2)**(2-av)/(av+5)
Lv=arb(2)**(1-av);kv=Dv/(arb(2)**(ev+1)*Av)
assert kv>1
R=(Av*(Cv+Lv*(2+kv.log()))/eta)**(2/ev)
assert R>2
Jv=lambda rr:Av*rr**(-ev)*(Cv+Lv*(1+(kv*rr**ev).log()))
assert Jv(R)<eta
assert Jv(arb(2))>Jv(arb(4))>Jv(arb(100))
checks+=['explicit coarse radius fixture','monotone J arithmetic fixture']
# Campaign exponent only: no remainder constants are inferred.
c=fmpq(par['campaign_c']);qc=1/c-4;ec=fmpq(par['campaign_epsilon']);ac=qc-ec
assert -5<ac<-3 and 0<ec<qc+5
checks.append('campaign admissible two-weight exponent')
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
     'proof_sha256':manifest['proof_sha256'],'checker_sha256':sha(Path(__file__)),
     'manifest_sha256':sha(B/'data/manifest.json'),'bits':ctx.prec,'checks':checks,'check_count':len(checks),
     'fixture':{'type':'illustrative only, not campaign certificate','C_a':Cv.str(60),'L_a':Lv.str(60),'k':kv.str(60),'coarse_radius':R.str(60),'J_at_radius':Jv(R).str(60),'eta':fixture['eta']},
     'campaign_q':str(qc),'campaign_epsilon':str(ec),'campaign_a':str(ac),
     'status':'PASS finite identities; analytic proof OPEN independent review',
     'stationary_H_budget_supplied':False,'existence_claimed':False}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
