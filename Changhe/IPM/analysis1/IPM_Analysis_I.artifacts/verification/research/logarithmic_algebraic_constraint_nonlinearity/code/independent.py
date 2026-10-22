from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq as Q
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_algebraic_constraint_nonlinearity';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
start=now();a=json.loads((E/'check.json').read_text());assert sha(D/'PROOF.md')==a['proof_sha256']=='989c8c8eebeecf3a85b346b2acede286ad2d86d8ad05f1769221e9693963cc02'
for name,h in a['parent_files'].items():assert sha(R/name)==h,name
# Independent sparse commutative polynomial algebra over fmpq. No Sympy
# or primary implementation is imported. Variables are u,v,c,d,a,b,e,f,t,w1,w2,l.
N=12
def const(q):return {(0,)*N:Q(q)} if q else {}
def var(i):
 e=[0]*N;e[i]=1;return {tuple(e):Q(1)}
def add(*xs):
 out={}
 for x in xs:
  for m,q in x.items():out[m]=out.get(m,Q(0))+q
 return {m:q for m,q in out.items() if q}
def sc(x,q):return {m:c*q for m,c in x.items() if c*q}
def mul(*xs):
 out=const(1)
 for x in xs:
  nxt={}
  for m,q in out.items():
   for n,p in x.items():
    e=tuple(i+j for i,j in zip(m,n));nxt[e]=nxt.get(e,Q(0))+q*p
  out={m:q for m,q in nxt.items() if q}
 return out
vs=list(map(var,range(N)));G=vs[:2];H=vs[2:4];B=[[vs[4],vs[5]],[vs[6],vs[7]]];T=vs[8];W=vs[9:11];ell=vs[11]
def plus(x,y):return [add(a,b) for a,b in zip(x,y)]
def scale(x,t):return [mul(t,a) for a in x]
def bil(x,y):return add(*[mul(x[i],B[i][j],y[j]) for i in range(2) for j in range(2)])
def quad(x):return bil(x,x)
def cross(h):return add(bil(G,h),bil(h,G))
checks={}
def ck(name,a,b):assert a==b,(name,a,b);checks[name]=True
ck('polarization_unsymmetric',add(quad(plus(G,H)),sc(quad(plus(G,scale(H,const(-1)))),-1)),sc(cross(H),2))
ck('quadratic_homogeneity',quad(scale(G,T)),mul(T,T,quad(G)))
ck('scaled_difference',add(quad(scale(plus(G,H),T)),sc(quad(scale(plus(G,scale(H,const(-1))),T)),-1)),sc(mul(T,T,cross(H)),2))
# Explicit rational elimination, independently reconstructing all matrices.
def rref(mat,columns):
 out=[row[:] for row in mat];pivots=[];at=0
 for j in range(columns):
  idx=next((i for i in range(at,len(out)) if out[i][j]),None)
  if idx is None:continue
  out[at],out[idx]=out[idx],out[at];v=out[at][j];out[at]=[x/v for x in out[at]]
  for i in range(len(out)):
   if i!=at:
    v=out[i][j];out[i]=[x-v*y for x,y in zip(out[i],out[at])]
  pivots.append(j);at+=1
  if at==len(out):break
 return out,pivots

def construct(m,rank,seed):
 rows=[]
 for i in range(m):
  row=[]
  for j in range(m+1):
   if j<rank:x=Q((i+1)*seed)**j
   else:x=sum((Q((i+1)*seed)**l*Q(seed**(l+1)+(l+2)*(j+3)+(-1)**j,j+l+1) for l in range(rank)),Q(0))
   row.append(x)
  rows.append(row)
 return rows

def evaluate(record,m):
 rank=record['rank'];seed=record['seed'];mat=construct(m,rank,seed);assert [[str(v) for v in row] for row in mat]==record['matrix']
 rr,piv=rref(mat,m+1);assert len(piv)==rank;free=next(j for j in range(m+1) if j not in piv)
 vec=[Q(0)]*(m+1);vec[free]=Q(1)
 for i,j in enumerate(piv):vec[j]=-rr[i][free]
 den=max(map(abs,vec));assert den>0;vec=[v/den for v in vec]
 assert max(map(abs,vec))==1
 for row in mat:assert sum((x*y for x,y in zip(row,vec)),Q(0))==0
 assert list(map(str,vec))==record['coefficients'];idx=next(j for j,v in enumerate(vec) if abs(v)==1)
 return vec,idx
specs=[(0,0),(1,0),(1,1),(2,1),(2,2),(3,1),(3,3),(4,2)];assert len(a['fixtures'])==len(specs)
groups=waves=0;ranks={'zero':0,'positive_deficient':0,'full_row':0}
for z,(m,base) in zip(a['fixtures'],specs):
 assert z['m']==m and z['base_rank']==base and len(z['groups'])==m+1 and len(z['waves'])==4
 active=[]
 for i,rec in enumerate(z['groups']):
  assert rec['i']==i and rec['rank']==min(m,base+i%2) and rec['seed']==i+2
  vec,idx=evaluate(rec,m);assert rec['active_index']==idx and rec['active_value']==str(vec[idx]);active.append(vec[idx]);groups+=1
  rank=rec['rank'];ranks['zero' if rank==0 else 'positive_deficient' if rank<m else 'full_row']+=1
 for n,rec in zip([1,2,7,11],z['waves']):
  assert rec['n']==n and rec['rank']==(base+n)%(m+1) and rec['seed']==n+3
  vec,idx=evaluate(rec,m);assert rec['maximizing_patch']==idx
  coeff=[x*y for x,y in zip(active,vec)];assert abs(coeff[idx])==1 and max(map(abs,coeff))==1
  assert list(map(str,coeff))==rec['all_leading_coefficients'] and str(coeff[idx])==rec['selected_leading_coefficient'];waves+=1
  rank=rec['rank'];ranks['zero' if rank==0 else 'positive_deficient' if rank<m else 'full_row']+=1
assert groups==a['group_system_count'] and waves==a['wave_system_count']
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_FMPQ_TWO_KERNEL_ELIMINATIONS','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'ring_checks':checks,'fixtures_compared':len(specs),'group_systems_compared':groups,'wave_systems_compared':waves,'rank_class_counts':ranks,'source_reuse':'Sparse fmpq polynomial ring adapted directly from210independent checker; new matrix generation and two-stage kernel comparison. No primary evaluator or Sympy import.','scope':'Exact manufactured matrix and generic polynomial algebra only. No finite sample proves arbitrary linear-functional values or the analytic support and Sobolev claims. No interval, modal norm or numerical lower constant.'}
with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
