from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq as Q
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_graph_constraint_limits';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
start=now();a=json.loads((E/'check.json').read_text());assert sha(D/'PROOF.md')==a['proof_sha256']=='5938f6fb1e1d96d44cce1e962cb24fc94fd2367d3dca5449a6646174da6de3c6'
for name,value in a['parent_files'].items():assert sha(R/name)==value, name
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
ck('fixed_correction_cross',cross(plus(H,scale(W,sc(ell,-1)))),add(cross(H),sc(mul(ell,cross(W)),-1)))
ck('scaled_difference',add(quad(scale(plus(G,H),T)),sc(quad(scale(plus(G,scale(H,const(-1))),T)),-1)),sc(mul(T,T,cross(H)),2))
# Separate exact Gauss-Jordan elimination with explicit row operations.
def rref(mat,columns):
 mat=[row[:] for row in mat];piv=[];at=0
 for col in range(columns):
  pivot=next((i for i in range(at,len(mat)) if mat[i][col]),None)
  if pivot is None:continue
  mat[at],mat[pivot]=mat[pivot],mat[at];v=mat[at][col];mat[at]=[x/v for x in mat[at]]
  for i in range(len(mat)):
   if i!=at:
    f=mat[i][col];mat[i]=[x-f*y for x,y in zip(mat[i],mat[at])]
  piv.append(col);at+=1
  if at==len(mat):break
 return mat,piv
def mv(mat,x):return [sum((q*v for q,v in zip(row,x)),Q(0)) for row in mat]
counts={'rank_zero':0,'rank_deficient_positive':0,'full_row_rank':0};compared=0
specs=[(0,0),(1,0),(1,1),(2,1),(2,2),(4,2),(4,4),(6,3)]
assert len(specs)==len(a['projection_fixtures'])
for z,(m,r) in zip(a['projection_fixtures'],specs):
 dim=m+3;assert [z['m'],z['r'],z['dim']]==[m,r,dim]
 # Direct formula, with no primary factor-matrix construction.
 MM=[]
 for i in range(m):
  row=[]
  for j in range(dim):
   if j<r:v=Q(i+1)**j
   else:v=sum((Q(i+1)**l*Q((l+2)*(j+3)+(-1)**l*(j+1)**2,j+l+1) for l in range(r)),Q(0))
   row.append(v)
  MM.append(row)
 assert [[str(v) for v in row] for row in MM]==z['matrix']
 RR,cols=rref(MM,dim);assert len(cols)==r and cols==z['basis_columns']
 # Choose the first free variable, set it to one, the other free variables zero.
 Z=[row[:m+1] for row in MM];ZZ,zc=rref(Z,m+1);free=next(j for j in range(m+1) if j not in zc);tt=[Q(0)]*(m+1);tt[free]=Q(1)
 for i,j in enumerate(zc):tt[j]=-ZZ[i][free]
 assert any(tt) and all(v==0 for v in mv(Z,tt));assert list(map(str,tt))==z['plateau_null']
 hv=[Q((-1)**j*(j+2),j+3) for j in range(dim)];rhs=mv(MM,hv)
 augmented=[[row[j] for j in cols]+[v] for row,v in zip(MM,rhs)];aa,ap=rref(augmented,r)
 assert ap==list(range(r));coeff=[aa[j][-1] for j in range(r)]
 for row in aa[r:]:assert row[-1]==0
 corr=[Q(0)]*dim
 for j,v in zip(cols,coeff):corr[j]=v
 kk=[x-y for x,y in zip(hv,corr)];assert all(v==0 for v in mv(MM,kk))
 for name,seq in [('input',hv),('coefficients',coeff),('correction',corr),('projected',kk)]:assert list(map(str,seq))==z[name]
 # The correction map fixes its own range, checked separately by elimination.
 rc=mv(MM,corr);aac,pc=rref([[row[j] for j in cols]+[v] for row,v in zip(MM,rc)],r)
 assert [aac[j][-1] for j in range(r)]==coeff
 counts['rank_zero' if r==0 else 'rank_deficient_positive' if r<m else 'full_row_rank']+=1;compared+=1
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_FMPQ_POLYNOMIAL_AND_ROW_ELIMINATION_CHECKS','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'ring_checks':checks,'projection_fixtures_compared':compared,'fixture_class_counts':counts,'scope':'Exact finite algebra only. Sparse polynomial expansion and separate rational row operations reproduce primary fixtures; these eight matrices do not prove the general continuous-constraint theorem. No new modal data, interval or norm ceiling.'}
with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
