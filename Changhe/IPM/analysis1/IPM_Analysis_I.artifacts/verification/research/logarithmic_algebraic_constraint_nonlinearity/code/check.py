from pathlib import Path
import sys,os,json
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_algebraic_constraint_nonlinearity';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='989c8c8eebeecf3a85b346b2acede286ad2d86d8ad05f1769221e9693963cc02'
parent='research/logarithmic_graph_constraint_limits/evidence/verdict.json';pv=p.load(R/parent);assert p.sha(R/parent)=='b42ab9793e3851b8aaf16dc79a822c4c001d17140365a3b20b12eada8a73366b';assert pv['status']=='CONFIRMED_GRAPH_DENSE_NORMALIZATION_IDENTICAL_INVERSE_CONSTANTS_AND_FINITE_CONTINUOUS_CONSTRAINT_NONLINEARITY';pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
checks={}
def put(n,v):
 q=S.expand(v);assert q==0,(n,q);checks[n]=str(q)
u,v,c,d,t=S.symbols('u v c d t');a,b,e,f=S.symbols('a b e f');G=S.Matrix([u,v]);H=S.Matrix([c,d]);B=S.Matrix([[a,b],[e,f]])
def bil(x,y):return (x.T*B*y)[0]
def q(x):return bil(x,x)
put('polarization_unsymmetric',q(G+H)-q(G-H)-2*(bil(G,H)+bil(H,G)))
put('quadratic_homogeneity',q(t*G)-t*t*q(G))
put('scaled_difference',q(t*(G+H))-q(t*(G-H))-2*t*t*(bil(G,H)+bil(H,G)))
# Fixed-block selector is formal algebra, not a proof of physical support.
la=S.symbols('l0:5');ti=S.symbols('t0:5');di=S.symbols('d0:5')
for i in range(5):put('formal_patch_selector_'+str(i),sum(S.Integer(i==j)*la[j]*ti[j]*di[j] for j in range(5))-la[i]*ti[i]*di[i])
def matrix(m,rank,seed):
 if rank==0:return S.zeros(m,m+1)
 b=S.Matrix(m,rank,lambda i,l:S.Integer((i+1)*seed)**l)
 c=S.Matrix(rank,m+1,lambda l,j:S.Integer(l==j) if j<rank else S.Rational(seed**(l+1)+(l+2)*(j+3)+(-1)**j,j+l+1))
 return b*c

def nullnorm(M):
 vec=M.nullspace()[0];den=max(abs(x) for x in vec);assert den>0;vec=vec/den
 assert max(abs(x) for x in vec)==1 and M*vec==S.zeros(M.rows,1)
 active=next(j for j,x in enumerate(vec) if abs(x)==1)
 return vec,active

def vals(mat):return [[str(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)]
fixtures=[];group_count=wave_count=0
specs=[(0,0),(1,0),(1,1),(2,1),(2,2),(3,1),(3,3),(4,2)]
for m,base in specs:
 groups=[];active_t=[]
 for i in range(m+1):
  rank=min(m,base+i%2);seed=i+2;MM=matrix(m,rank,seed);assert MM.rank()==rank;vec,idx=nullnorm(MM)
  groups.append({'i':i,'rank':rank,'seed':seed,'matrix':vals(MM),'coefficients':list(map(str,vec)),'active_index':idx,'active_value':str(vec[idx])});active_t.append(vec[idx]);group_count+=1
 waves=[]
 for n in [1,2,7,11]:
  rank=(base+n)%(m+1);seed=n+3;WW=matrix(m,rank,seed);assert WW.rank()==rank;vec,idx=nullnorm(WW)
  leading=[active_t[j]*vec[j] for j in range(m+1)];assert abs(leading[idx])==1 and max(abs(x) for x in leading)==1
  waves.append({'n':n,'rank':rank,'seed':seed,'matrix':vals(WW),'coefficients':list(map(str,vec)),'maximizing_patch':idx,'selected_leading_coefficient':str(leading[idx]),'all_leading_coefficients':list(map(str,leading))});wave_count+=1
 fixtures.append({'m':m,'base_rank':base,'groups':groups,'waves':waves})
out={'start_utc':start,'utc':p.now(),'status':'PASS_TWO_STAGE_FINITE_KERNEL_AND_MAXIMUM_COORDINATE_CHECKS','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':dict(sorted(pins.items())),'parent_pin_count':len(pins),'symbolic_identities':checks,'fixtures':fixtures,'group_system_count':group_count,'wave_system_count':wave_count,'scope':'Manufactured matrices only, with exact maximum-coordinate normalization. Selector identities encode disjoint support formally and do not prove analytic localization. General arbitrary-Lambda theorem is the informal proof; no new interval, modal norm, or numerical lower constant.'};p.write(E/'check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['parent_files','fixtures']}))
