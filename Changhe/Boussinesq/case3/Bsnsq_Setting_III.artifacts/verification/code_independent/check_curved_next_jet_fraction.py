"""P306 independent finite rational series, without symbolic residue calls."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import json, time, hashlib
started=datetime.now(timezone.utc).isoformat(); tick=time.monotonic(); N=30; checks=[]; samples=[]
def ck(name, condition, detail=None): checks.append(dict(name=name,passed=bool(condition),detail=detail))
def p(d=None):
 d={} if d is None else d
 return [F(d.get(i,0)) for i in range(N+1)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sc(a,c):return [x*c for x in a]
def mul(a,b):return [sum((a[j]*b[i-j] for j in range(i+1)),F(0)) for i in range(N+1)]
def inv(a):
 b=p({0:1/a[0]})
 for i in range(1,N+1): b[i]=-sum((a[j]*b[i-j] for j in range(1,i+1)),F(0))/a[0]
 return b
def shift(a,n):return p({i+n:x for i,x in enumerate(a) if 0<=i+n<=N})
def der(a):return [(i+1)*a[i+1] if i<N else F(0) for i in range(N+1)]
def integ(a):return [F(0)]+[a[i-1]/i for i in range(1,N+1)]
def exp(a):
 assert a[0]==0
 b=p({0:1})
 for i in range(1,N+1): b[i]=sum((j*a[j]*b[i-j] for j in range(1,i+1)),F(0))/i
 return b
for C in map(F,[-2,-1,1,2]):
 for k in [F(-2),F(-1,2),F(1,2),F(2)]:
  for H in [F(0),3*C,-k**7/231]:
   tag=f'C{C}_k{k}_H{H}'; a=-C*k/260
   B=p({1:1,2:k,13:a}); P=p({0:1,1:k,12:a}); Bd=der(B); Bdd=der(Bd); Bddd=der(Bdd)
   Q=mul(add(p({0:8}),sc(Bd,2)),inv(P)); R=mul(add(p({0:5}),Bd),inv(P))
   tau=exp(integ(shift(Q,-1))); rho=exp(integ(shift(R,-1)))
   J=integ(shift(mul(mul(tau,inv(P)),inv(rho)),3))
   h=mul(rho,add(p({0:H}),sc(J,-C))); eta=shift(h,6); T=shift(sc(tau,C),10)
   v=sc(add(Bdd,eta),F(-1,2)); eta_d=der(eta); zeta=mul(tau,rho)
   deninv=sc(inv(mul(P,tau)),1/C)
   curv=mul(add(sc(shift(Bddd,1),-4),sc(mul(Bdd,Q),6)),deninv)
   etapart=mul(add(mul(add(sc(Q,6),p({0:-24})),h),sc(shift(der(h),1),-4)),deninv)
   fres=curv[11]+etapart[5]
   ck(tag+'_fourth_residue_zero',fres==0,str(fres))
   # I Laurent coefficients as a sparse dictionary; omit only the zero log coefficient.
   I={}
   for series,order in [(curv,-12),(etapart,-6)]:
    for j,c in enumerate(series):
     power=j+order
     if power!=-1: I[power+1]=I.get(power+1,F(0))+c/(power+1)
   for E in [F(0),F(7,3)]:
    i20=p({power+20:c for power,c in I.items() if 0<=power+20<=N}); i20[20]+=E
    D=sc(mul(mul(tau,tau),i20),C*C)
    rhs=add(sc(D,-1),add(sc(mul(der(v),eta),2),sc(mul(v,eta_d),-6)))
    gs=mul(rhs,inv(mul(P,zeta)))
    residue=gs[16]; expected=-9*C*k*(231*H+k**7)/385
    ck(tag+f'_E{E}_residue',residue==expected,dict(actual=str(residue),expected=str(expected)))
    # gamma = Z int g; only the residue term has been omitted.
    primitive_shift=p({j:c/F(j-16) for j,c in enumerate(gs) if j!=16})
    gamma=mul(zeta,primitive_shift)
    gamma_eq=add(mul(B,der(gamma)),sc(mul(add(p({0:13}),sc(Bd,3)),gamma),-1))
    defect=add(gamma_eq,sc(rhs,-1)); predicted=sc(shift(mul(P,zeta),16),-residue)
    ck(tag+f'_E{E}_gamma_equation_defect',defect[:N-2]==predicted[:N-2])
    ck(tag+f'_E{E}_tuned_iff', (residue==0)==(H==-k**7/231))
    ck(tag+f'_E{E}_gamma_min_order',all(c==0 for c in gamma[:5]))
    if E==0:samples.append(dict(C=str(C),k=str(k),H=str(H),a=str(a),residue=str(residue),analytic_gamma=residue==0))
   ck(tag+'_thermal_series',add(mul(B,der(T)),sc(mul(add(p({0:8}),sc(Bd,2)),T),-1))[:N-2]==p()[:N-2])
   eta_eq=add(mul(B,eta_d),sc(mul(add(p({0:5}),Bd),eta),-1))
   ck(tag+'_eta_series',eta_eq[:N-2]==sc(T,-1)[:N-2])
   # D equation checked directly, including the eliminated q only after multiplying by B.
   forcing=add(sc(mul(mul(B,T),Bddd),-4),add(sc(mul(mul(T,Bdd),add(p({0:8}),sc(Bd,2))),6),add(sc(mul(mul(T,eta),add(p({0:8}),sc(Bd,2))),6),sc(mul(mul(B,T),eta_d),-4))))
   lhs=add(mul(B,mul(B,der(D))),sc(mul(mul(B,add(p({0:16}),sc(Bd,4))),D),-1))
   ck(tag+'_fourth_equation_series',lhs[:N-2]==forcing[:N-2])
   if H==-k**7/231:ck(tag+'_profile_sign_iff_negative_Ck',(H/C>0)==(C*k<0))
V=Path('research/306_curved_endpoint_next_jet/verification')
f=json.loads((V/'freeze.json').read_text());ck('preparation_before_computation',f['utc']<started)
ck('preparation_proof_preserved',hashlib.sha256((V/'PROOF_preparation.md').read_bytes()).hexdigest()==f['proof_sha256'])
r=dict(started_utc=started,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed'] for c in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),samples=samples)
(V/'fraction_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['checks','samples']},indent=2));print('FAILED', [c for c in checks if not c['passed']])
