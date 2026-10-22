"""Own exact rational power-series algebra, no lead/NUM code reused."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();N=14;Ck=[]
def ck(n,b):Ck.append(dict(name=n,passed=bool(b)))
def p(d={}):return [F(d.get(i,0))for i in range(N+1)]
def add(a,b):return[x+y for x,y in zip(a,b)]
def mul(a,b):return[sum(a[j]*b[i-j]for j in range(i+1))for i in range(N+1)]
def sc(a,c):return[x*c for x in a]
def inv(a):
 b=p({0:1/a[0]})
 for i in range(1,N+1):b[i]=-sum(a[j]*b[i-j]for j in range(1,i+1))/a[0]
 return b
def der(a):return[(i+1)*a[i+1]if i<N else F(0)for i in range(N+1)]
def integ(a):return[F(0)]+[a[i-1]/i for i in range(1,N+1)]
def exp(a):
 assert a[0]==0;b=p({0:1})
 for i in range(1,N+1):b[i]=sum(j*a[j]*b[i-j]for j in range(1,i+1))/i
 return b
def shift(a,n):return p({i+n:x for i,x in enumerate(a)if i+n<=N})
for eps in [-1,1]:
 for c in [-2,-1,1,2]:
  for k in [-1,1]:
   tag=f'{eps}_{c}_{k}';c=F(c);k=F(k);a=-eps*c*k/260;B=p({1:1,2:k,13:a});P=p({0:1,1:k,12:a});Bd=der(B);Bdd=der(Bd);Bddd=der(Bdd)
   Q=mul(add(p({0:8}),sc(Bd,2)),inv(P));R=mul(add(p({0:5}),Bd),inv(P))
   tau=exp(integ(Q[1:]+[F(0)]));rho=exp(integ(R[1:]+[F(0)]))
   J=integ(shift(sc(mul(mul(tau,inv(P)),inv(rho)),c),3));h=mul(rho,add(p({0:3*c}),sc(J,-1)))
   numerator=add(sc(shift(Bddd,1),-4),sc(mul(Bdd,Q),6));deninv=sc(inv(mul(P,tau)),1/c);curv=mul(numerator,deninv)
   etan=add(mul(add(sc(Q,6),p({0:-24})),h),sc(shift(der(h),1),-4));etapart=sc(mul(etan,deninv),eps)
   ck(tag+'_curvature_residue',curv[11]==2496*a/c);ck(tag+'_eta_residue',etapart[5]==eps*F(48,5)*k);ck(tag+'_total_residue_zero',curv[11]+etapart[5]==0)
   ck(tag+'_leading_derivative',curv[0]==120*k/c);ck(tag+'_leading_I',-curv[0]/11==-120*k/(11*c));ck(tag+'_sign',(-120*k*c/(11*c)>0)==(k<0))
   thermal=add(add(shift(sc(tau,10),0),shift(der(tau),1)),sc(mul(Q,tau),-1));ck(tag+'_thermal_series',all(x==0 for x in thermal[:12]))
   eta_lhs=add(add(sc(h,6),shift(der(h),1)),sc(mul(R,h),-1));eta_rhs=shift(sc(mul(tau,inv(P)),-c),4);ck(tag+'_eta_series',eta_lhs[:12]==eta_rhs[:12])
V=Path('research/303_curved_simple_endpoint_residue/verification');f=json.loads((V/'freeze.json').read_text());ck('proof_precedes_controls',f['utc']<start);ck('proof_hash',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==f['proof_sha256']);ck('source_hash',hashlib.sha256((V/'lead_proof_readonly.md').read_bytes()).hexdigest()==f['source_sha256'])
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in Ck),total=len(Ck),checks=Ck,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(V/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},indent=2));print('FAILED',[x for x in Ck if not x['passed']])
