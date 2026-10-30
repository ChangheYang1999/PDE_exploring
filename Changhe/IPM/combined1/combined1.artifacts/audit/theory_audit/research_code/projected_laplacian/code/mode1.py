from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,gzip,json,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
start=time.monotonic();ctx.prec=2048
base=Path(__file__).resolve().parents[1]
def digest(p):return sha256((base/p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
src='data/candidate007_mode1.json.gz'
with gzip.open(base/src,'rt') as f:d=json.load(f)
comparison=json.loads((base/'data/mode1_independent_comparison.json').read_text())
assert comparison['exact_polynomial_equality'] and comparison['peer_sha256']==digest(src)
c=Q(d['cl']);delta=Q(d['delta']);t=P([0,1]);v=P([1,-1]);zero=P([])
def T(p,a):return (1-2*a*t)*p+2*t*v*p.derivative()
terms=[];diagonals=[]
for row in d['rows']:
 ell=row['ell'];p=P([int(x) for x in row['numerator']])/Q(row['denominator']);a=ell*delta/2
 lap=T(T(p,a),a)-p;L,rem=divmod(lap,t);assert not rem
 L=L(v)
 if L:
  order=next(k for k,x in enumerate(L) if x);diagonals.append((ell,order));terms.append((ell,L))
groups={}
for i,(ell,p) in enumerate(terms):
 for j in range(i,len(terms)):
  ell2,q=terms[j];k=ell+ell2;groups[k]=groups.get(k,zero)+(1 if i==j else 2)*v*p*q
moments=[(k*delta/2+l-2,x) for k,p in groups.items() for l,x in enumerate(p) if x]
print('prepared',len(terms),'branches',len(groups),'groups',len(moments),'moments seconds',time.monotonic()-start,flush=True)
rows=[];norms={}
for a in [Q(k,4) for k in range(8)]:
 assert all(a+ell*delta+2*order-2>0 for ell,order in diagonals)
 assert all(a+e>0 for e,x in moments)
 value=sum((ar(x)/ar(a+e) for e,x in moments),arb(0));assert value>0
 norm=(arb.pi()*value/2).sqrt();norms[a]=norm
 lower=arb(5)**ar((a-2)/2)*norm;beta=1+c-c*a
 ceiling=(8*arb.pi()).sqrt()*ar(beta**2/(1+a)) if beta>0 else None
 rows.append({'a':str(a),'projected_norm':norm.str(95),'Y_lower':lower.str(95),'B':ceiling.str(95) if ceiling else None,'violates_at_point':bool(lower>ceiling) if ceiling else None})
 print('a',a,'norm',norm.str(25),'Ylower',lower.str(25),flush=True)
cells=[]
for k in range(7):
 l,h=Q(k,4),Q(k+1,4);lower=arb(5)**ar((l-2)/2)*norms[h];upper=(8*arb.pi()).sqrt()*ar((1+c-c*l)**2/(1+l))
 cells.append({'left':str(l),'right':str(h),'lower':lower.str(95),'upper':upper.str(95),'ratio':(lower/upper).str(95),'passed':bool(lower>upper)})
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d['candidate'],'angular_modes':[1],'precision_bits':ctx.prec,'inputs':{p:digest(p) for p in [src,'data/mode1_independent_comparison.json','PROOF.md','code/mode1.py']},'rows':rows,'cells':cells,'all_cells_passed':all(x['passed'] for x in cells),'elapsed_seconds':time.monotonic()-start}
p=base/'verification/candidate007_mode1.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('all cells',out['all_cells_passed'],'seconds',out['elapsed_seconds'],flush=True)
