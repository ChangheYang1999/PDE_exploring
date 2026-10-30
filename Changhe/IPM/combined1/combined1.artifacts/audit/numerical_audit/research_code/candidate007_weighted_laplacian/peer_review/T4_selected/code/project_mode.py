from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,gzip,json,time,importlib.util
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
start=time.monotonic();ctx.prec=2048
base=Path(__file__).resolve().parents[1]
def digest(p):return sha256((base/p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
mode=int(sys.argv[1]);assert mode>1 and mode%2==1
src='data/candidate007_canonical.json'
helper=base.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('projected_lap_fields',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
c,delta,rho,stream=m.fields(json.loads((base/src).read_text()))
t=P([0,1]);v=P([1,-1]);zero=P([])
def T(p,a):return (1-2*a*t)*p+2*t*v*p.derivative()
residual={};pairs=0
def add(ell,q):
 if q:residual[ell]=residual.get(ell,zero)+q
for (j,n),p in rho.items():
 if n==mode:add(j+1,c*T(p,(j+1)*delta/2)-p)
for (j,n),q in stream.items():
 dq=m.td(q,(j+1)*delta/2,2)
 for (i,k),p in rho.items():
  if k+n!=mode and abs(k-n)!=mode:continue
  dp=T(p,(i+1)*delta/2)
  if k+n==mode:add(i+j+2,(k*p*dq-n*q*dp)/2)
  if abs(k-n)==mode:add(i+j+2,(-k*p*dq-n*q*dp)*(1 if k>n else -1)/2)
  pairs+=1
residual={ell:p for ell,p in residual.items() if p}
d={'candidate':'C1-N1-007-d2w-j7-e2bal','rows':[{'ell':ell,'numerator':[str(x.numerator) for x in p],'denominator':None} for ell,p in []]}
print('built mode',mode,'pairs',pairs,'branches',len(residual),'seconds',time.monotonic()-start,flush=True)
terms=[];diagonals=[]
for ell,p in residual.items():
 a=ell*delta/2
 lap=T(T(p,a),a)-mode*mode*p;L,rem=divmod(lap,t);assert not rem
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
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d['candidate'],'angular_modes':[mode],'precision_bits':ctx.prec,'inputs':{p:digest(p) for p in [src,'PROOF.md','code/project_mode.py']},'rows':rows,'cells':cells,'all_cells_passed':all(x['passed'] for x in cells),'elapsed_seconds':time.monotonic()-start,'nonlinear_pairs':pairs,'helper_sha256':sha256(helper.read_bytes()).hexdigest()}
p=base/f'verification/candidate007_mode{mode}.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('all cells',out['all_cells_passed'],'seconds',out['elapsed_seconds'],flush=True)
