"""Independent finite rational controls for P355; no teammate code or Laurent-class import."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,time
r=Path('research/355_euler_resonance_operator_bounds');v=r/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
def D(f):return {j-1:j*c for j,c in f.items()if j and c}
def S(f,m):return {j:c/F(j-m)for j,c in f.items()if j!=m and c}
def E(f,m):return {j:(j-m)*c for j,c in f.items()if j!=m and c}
def norm(f,rho):return sum((abs(c)*rho**j for j,c in f.items()),F(0))
fz=json.loads((v/'freeze.json').read_text());ck('proof_hash',sha(r/'PROOF.md')==fz['proof_sha256']);ck('proof_precedes',fz['prepared_utc']<start.isoformat())
for m in [0,1,2,6,10,16,26,100]:
 for rho in [F(1,2),F(1),F(2)]:
  f={j:F((-1)**j*(j+1),j+2)for j in range(0,m+12)};proj={j:c for j,c in f.items()if j!=m};ck(f'm{m}_r{rho}_right_inverse',E(S(f,m),m)==proj);ck(f'm{m}_r{rho}_left_inverse',S(E(f,m),m)==proj);ck(f'm{m}_r{rho}_norm',norm(S(f,m),rho)<=norm(f,rho));ck(f'm{m}_r{rho}_derivative_norm',norm(S(D(f),m),rho)<=F(m+2)/rho*norm(f,rho));ck(f'm{m}_r{rho}_sharp_S',norm(S({m+1:F(1)},m),rho)==rho**(m+1));ck(f'm{m}_r{rho}_sharp_SD',norm(S(D({m+2:F(1)},),m),rho)/rho**(m+2)==F(m+2)/rho)
  for j in [m+3,m+10,m+100,m+1000]:
   mono={j:rho**(-j)};value=norm(S(D(D(mono)),m),rho);want=F(j*(j-1),j-m-2)/rho**2;ck(f'm{m}_r{rho}_D2_j{j}',norm(mono,rho)==1 and D(D(mono)).get(m,0)==0 and value==want and value>=F(j)/rho**2)
  for frac in [F(1,4),F(1,2),F(2,3),F(9,10)]:
   rr=rho*frac;ck(f'm{m}_r{rho}_radiusloss_{frac}',norm(S(D(D(f)),m),rr)<=2*norm(f,rho)/(rho-rr)**2)
# Independently constructed dense Taylor series. No imported jet implementation.
P=44
zero=lambda:[F(0)]*P
def series(d):
 a=zero()
 for j,c in d.items():
  if j<P:a[j]=F(c)
 return a
def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,c):return [x*c for x in a]
def mul(a,b):
 out=zero()
 for j,x in enumerate(a):
  if x:
   for k,y in enumerate(b[:P-j]):
    if y:out[j+k]+=x*y
 return out
def der(a):return [(j+1)*a[j+1]for j in range(P-1)]+[F(0)]
def power(a,n):
 out=series({0:1})
 for j in range(n):out=mul(out,a)
 return out
def hom(B,L,m):
 assert B[0]==0 and B[1]==1 and L[0]==m
 a=zero();a[m]=1
 for d in range(m+1,P):
  right=sum((L[l]*a[d-l]for l in range(1,d+1)),F(0))
  right-=sum((B[l]*(d-l+1)*a[d-l+1]for l in range(2,d+1)),F(0));a[d]=right/F(d-m)
 return a
for C,k in [(F(1),F(-1)),(F(2),F(1,2)),(F(-3),F(2))]:
 B=series({1:1,2:k,13:-C*k/260});Bd=der(B);A=scale(add(series({0:8}),scale(Bd,2)),F(1,10));z=hom(B,A,1);eta=hom(B,scale(add(series({0:1}),scale(Bd,-1)),F(1,5)),0);Y=hom(B,add(series({0:5}),Bd),6);t=hom(B,add(series({0:8}),scale(Bd,2)),10)
 label=f'C{C}_k{k}';ck(label+'_coordinate_normalization',z[0]==0 and z[1]==1 and eta[0]==1 and A[0]==1);ck(label+'_Y_factorization',mul(eta,power(z,6))==Y);ck(label+'_t_factorization',power(z,10)==t)
 for n in [1,2,3,5]:
  for ell in [0,1,2,6,10,20,30]:
   g=power(z,ell);lhs=add(mul(B,der(g)),scale(mul(add(series({0:8}),scale(Bd,2)),g),-n));rhs=scale(mul(A,g),ell-10*n);ck(label+f'_Tn{n}_ell{ell}',lhs==rhs)
 for j in [0,1,2,4]:
  L=add(scale(add(series({0:4}),Bd),2*j+1),series({0:1}))
  for ell in [0,1,2,6,10,20,30]:
   fg=mul(eta,power(z,ell));lhs=add(mul(B,der(fg)),scale(mul(L,fg),-1));rhs=scale(mul(A,fg),ell-(10*j+6));ck(label+f'_Oj{j}_ell{ell}',lhs==rhs)
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed']for c in checks),total=len(checks),proof_sha256=sha(r/'PROOF.md'),code_sha256=sha(__file__),dense_series_known_high=P,checks=checks,scope='Finite exact rational controls of the separate infinite-index proof; not transverse convergence or a B2 candidate.')
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items()if k!='checks'},indent=2));print('failed',[x for x in checks if not x['passed']])
