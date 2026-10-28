"""Exact original-source stationary recurrence using real trigonometric coefficients."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
sys.path.insert(0,str(B/'source_audit'))
import recover_state as rec
rec.HERE=H;rec.COPY=Path('case4/IPM_case4.artifacts')
c0,a,meta=rec.read_state(131);c=Q(str(c0));delta=1-1/c
assert meta['canonical_serialization_sha256']=='4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01'
def clean(a):return {k:v for k,v in a.items() if v}
def add(a,k,v):
 if k<0:k,v=-k,-v
 if k and v:a[k]=a.get(k,Q(0))+v

def density(C,s):
 a={}
 for m,v in C.items():
  add(a,m+1,-v*(s*s-m*m)*(s-2-m)/2)
  add(a,m-1,v*(s*s-m*m)*(s-2+m)/2)
 return clean(a)

def stream(a,p):
 S={}
 for k,v in a.items():
  add(S,k+1,(p-k)*v/2);add(S,k-1,(p+k)*v/2)
 out={}
 for k,v in S.items():
  if v:
   den=k*k-(p+1)**2;assert den;out[k]=v/den
 return clean(out)

def adv(P,T,ps,p):
 out={}
 for m,b in P.items():
  for n,a in T.items():
   v=-m*b*p*a/2;add(out,n+m,v);add(out,n-m,v)
   v=ps*b*n*a/2;add(out,m+n,v);add(out,m-n,v)
 return clean(out)

def potential(T,p):
 r=T.copy();C={}
 for k in range(max(T),0,-2):
  m=k-1;column=density({m:Q(1)},p+3);assert column[k]
  v=r.get(k,Q(0))/column[k];C[m]=v
  for j,x in column.items():r[j]=r.get(j,Q(0))-v*x
 assert not clean(r)
 C=clean(C);assert density(C,p+3)==T;return C

def norm(a):
 sq=sum((v*v for v in a.values()),Q(0));N=(arb(sq)*arb.pi()).sqrt()
 return {'squared_divided_by_pi_exact':str(sq),'full_circle':N.str(70),'first_quadrant':(N/2).str(70)}
C1={}
for (j,m,k),v in zip(rec.CANON,a):
 if j==0:C1[2*m]=C1.get(2*m,Q(0))+Q(str(v))
C1=clean(C1);p={n:1-n*delta for n in range(1,9)}
T={1:density(C1,p[1]+3)};P={1:stream(T[1],p[1])};CC={1:C1};S={}
for n in range(2,9):
 A={}
 for i in range(1,n):
  for k,v in adv(P[i],T[n-i],p[i]+1,p[n-i]).items():add(A,k,v)
 S[n]=clean(A);T[n]={k:v/((n-1)*(c-1)) for k,v in S[n].items()};P[n]=stream(T[n],p[n]);CC[n]=potential(T[n],p[n])
 assert all((c*p[n]-1)*T[n].get(k,Q(0))+S[n].get(k,Q(0))==0 for k in T[n].keys()|S[n].keys())
 assert max(T[n])<=20*n-1 and all(k%2 for k in T[n])
 print('order',n,'modes',len(T[n]),'seconds',time.monotonic()-start,flush=True)
oldp=B/'05_tails/verification/state131_formal_tail.json';old=json.loads(oldp.read_text())
for n in range(1,7):assert T[n]=={int(k):Q(v) for k,v in old['stationary_density_orders'][str(n)]['coefficients'].items()}
producer=Path('numerics/data/stationary_order7.json');producer_bytes=producer.read_bytes();other=json.loads(producer_bytes)
assert T[7]=={int(k):Q(v) for k,v in other['stationary_density_orders']['7']['coefficients'].items()}
assert producer.read_bytes()==producer_bytes
assert 5*delta-2>0 and 2-4*delta>0 and 4-7*delta>0
assert S[8]=={k:7*(c-1)*v for k,v in T[8].items()}
files=[H.parent/'PROOF.md',B/'source_audit/recover_state.py',oldp]
encode=lambda a:{str(k):str(v) for k,v in sorted(a.items())}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'EXACT sine recurrence and producer order7 agree; independent Fourier audit pending','precision_bits':ctx.prec,'source_json_sha256':meta['source_json_sha256'],'original_canonical_sha256':meta['canonical_serialization_sha256'],'c':str(c),'delta':str(delta),'orders':{str(n):{'power':str(p[n]),'density':encode(T[n]),'stream':encode(P[n]),'potential':encode(CC[n]),'density_norm':norm(T[n])} for n in range(1,9)},'order8_fixed_defect':{'sector':[7,0],'power':str(p[8]),'sine_coefficients':encode(S[8]),'norm':norm(S[8])},'order7_density_max_harmonic':max(T[7]),'order7_potential_max_abs':str(max(map(abs,CC[7].values()))),'descendant_2_1_power':str(1-3*delta-2),'producer_sha256':sha256(producer_bytes).hexdigest(),'producer_path':str(producer),'producer_all70_order7_coefficients_match':True,'old_six_orders_match':True,'dependencies':{str(p.relative_to(B)):sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('recur_sine.json').write_text(json.dumps(out,indent=2)+'\n');print('defect',out['order8_fixed_defect']['norm']['full_circle'],'DONE',out['seconds'],flush=True)
