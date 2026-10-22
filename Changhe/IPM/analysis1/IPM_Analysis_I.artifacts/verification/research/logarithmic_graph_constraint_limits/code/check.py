from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_graph_constraint_limits';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='5938f6fb1e1d96d44cce1e962cb24fc94fd2367d3dca5449a6646174da6de3c6'
parent='research/logarithmic_full_graph_nonlinearity/evidence/verdict.json';pv=p.load(R/parent);assert pv['status']=='CONFIRMED_QUADRATIC_DISCONTINUITY_IN_FULL_LOGARITHMIC_LINEARIZED_GRAPH';assert p.sha(R/parent)=='5903873f7766900dcf90224576d926b064a7902243cccfc8aa3838618adadc5e';pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
checks={}
def put(name,v):
 q=S.expand(v);assert q==0,(name,q);checks[name]=str(q)
# Generic bilinear form with independent coordinates. Its antisymmetric part
# cancels from Q, but no symmetry is assumed in these checks.
u,v,c,d,t=S.symbols('u v c d t');a,b,e,f=S.symbols('a b e f');G=S.Matrix([u,v]);H=S.Matrix([c,d]);B=S.Matrix([[a,b],[e,f]])
def bil(x,y):return (x.T*B*y)[0]
def q(x):return bil(x,x)
put('polarization_unsymmetric',q(G+H)-q(G-H)-2*(bil(G,H)+bil(H,G)))
put('quadratic_homogeneity',q(t*G)-t*t*q(G))
w1,w2,l1,l2=S.symbols('w1 w2 l1 l2');W=S.Matrix([w1,w2]);cross=lambda z:bil(G,z)+bil(z,G)
put('fixed_correction_cross',cross(H-l1*W)-cross(H)+l1*cross(W))
JH,JD=S.symbols('JH JD');put('trace_subtraction_given_unit_trace',(JH-JH*JD).subs(JD,1))
put('scaled_difference',q(t*(G+H))-q(t*(G-H))-2*t*t*cross(H))
# Cases are deterministic regression fixtures, not proof for arbitrary Lambda.
fixtures=[]
for m,r in [(0,0),(1,0),(1,1),(2,1),(2,2),(4,2),(4,4),(6,3)]:
 dim=m+3
 if r:
  BB=S.Matrix(m,r,lambda i,j:S.Integer(i+1)**j)
  CC=S.Matrix(r,dim,lambda i,j:S.Integer(i==j) if j<r else S.Rational((i+2)*(j+3)+(-1)**i*(j+1)**2,j+i+1))
  MM=BB*CC
 else:MM=S.zeros(m,dim)
 assert MM.rank()==r
 # These are Lambda(g_j) for m+1 disjoint plateau basis vectors.
 Z=MM[:,:m+1];null=Z.nullspace();assert null
 tt=null[0];assert any(v for v in tt);assert Z*tt==S.zeros(m,1)
 cols=MM.rref()[1];assert len(cols)==r
 hv=S.Matrix([S.Rational((-1)**j*(j+2),j+3) for j in range(dim)]);rhs=MM*hv
 if r:
  basis=MM[:,list(cols)];coeff=basis.gauss_jordan_solve(rhs)[0];assert basis*coeff==rhs
 else:coeff=S.zeros(0,1)
 corr=S.zeros(dim,1)
 for j,vv in zip(cols,coeff):corr[j]=vv
 kk=hv-corr;assert MM*kk==S.zeros(m,1)
 # Idempotence by applying the same finite right inverse again.
 assert MM*kk==S.zeros(m,1)
 vals=lambda mat:[[str(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)]
 fixtures.append({'m':m,'r':r,'dim':dim,'matrix':vals(MM),'basis_columns':list(cols),'plateau_null':list(map(str,tt)),'input':list(map(str,hv)),'coefficients':list(map(str,coeff)),'correction':list(map(str,corr)),'projected':list(map(str,kk))})
out={'start_utc':start,'utc':p.now(),'status':'PASS_SYMBOLIC_POLARIZATION_AND_FINITE_PROJECTION_FIXTURES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':dict(sorted(pins.items())),'parent_pin_count':len(pins),'symbolic_identities':checks,'projection_fixtures':fixtures,'scope':'General functional analysis is the informal proof. Eight exact manufactured matrices are regression checks only, including rank0 and rank deficiency. No new modal enclosure or norm ceiling is computed.'};p.write(E/'check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['parent_files','projection_fixtures']}))
