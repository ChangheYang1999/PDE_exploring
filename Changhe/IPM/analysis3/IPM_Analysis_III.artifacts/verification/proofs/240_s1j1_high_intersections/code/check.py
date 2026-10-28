"""Exact S1J1 high-input and graph constraints, reconstructed from original knots."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
from datetime import datetime,timezone
import ast,hashlib,importlib.util,json,time
import numpy as np
ROOT=Path(__file__).resolve().parents[3]; TOP=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('own_spline_replay',ROOT/'proofs/198_pure_spline_input_gram/code/check.py'); r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def jet(poly,width,right):
 return [sum((v*F(factorial(j),factorial(j-n))*int(right)**(j-n) for j,v in enumerate(poly) if j>=n),F(0))/width**n for n in range(8)]
def rref(A,preference=None):
 m=len(A);n=len(A[0]);order=(preference or [])+[i for i in range(n) if i not in (preference or [])]
 M=[[F(row[i]) for i in order] for row in A]; piv=[];a=0
 for j in range(n):
  p=next((i for i in range(a,m) if M[i][j]),None)
  if p is None:continue
  M[a],M[p]=M[p],M[a];v=M[a][j];M[a]=[x/v for x in M[a]]
  for i in range(m):
   if i!=a:
    v=M[i][j];M[i]=[x-v*y for x,y in zip(M[i],M[a])]
  piv.append(j);a+=1
  if a==m:break
 free=[j for j in range(n) if j not in piv];basis=[]
 for j in free:
  w=[F(0)]*n;w[j]=1
  for i,p in enumerate(piv):w[p]=-M[i][j]
  v=[F(0)]*n
  for b,c in enumerate(order):v[c]=w[b]
  assert all(sum(x*y for x,y in zip(row,v))==0 for row in A);basis.append(v)
 assert all(basis[j][order[c]]==int(i==j) for i,c in enumerate(free) for j in range(len(free)))
 return {'rank':a,'pivot_columns':[order[j] for j in piv],'free_columns':[order[j] for j in free],'basis_columns':basis}
def main():
 start=time.monotonic();assert sha(r.SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 data=np.load(r.SRC,allow_pickle=False);fine=list(map(r.rat,data['knots']));k=r.rat(data['k']);knots=[fine[0]]*8+fine[8:-8][::60]+[fine[-1]]*8
 assert len(knots)-8==34; endpoints=[];checks=0
 for span,right in ((7,False),(len(knots)-9,True)):
  ps=r.cox(knots,span);rows=[]
  for i in range(34):
   p=ps.get(i,[F(0)]*8);assert p==r.db.deboor_poly(knots,[F(j==i) for j in range(34)],7,span);checks+=1
   rows.append(jet(p,knots[span+1]-knots[span],right))
  endpoints.append(rows)
 old=json.loads((ROOT/'proofs/206_pure_spline_high_domain/evidence/check.json').read_text())
 for i in range(34):
  assert endpoints[0][i]==list(map(F,old['endpoint_data'][i]['left_jets']))
  assert endpoints[1][i]==list(map(F,old['endpoint_data'][i]['right_jets']))
 exactpath=ROOT/'proofs/239_s1j1_full_input/evidence/exact_inputs.json';exact=json.loads(exactpath.read_text())
 assert list(map(F,exact['coarse_knots']))==knots and F(exact['k'])==k
 ex=list(map(F,exact['inner_exponents']));D=[list(map(F,row)) for row in exact['inner_coefficients']];assert ex==list(map(F,range(2,15,2)))
 for i in range(4):
  assert D[i][4:]==[0]*3
  assert [sum(v*x**n for v,x in zip(D[i],ex)) for n in range(4)]==endpoints[0][i][:4]
 for q in range(4,7):
  d=[-prod((ex[q]-ex[l])/(ex[j]-ex[l]) for l in range(4) if l!=j) for j in range(4)]+[F(j==q) for j in range(4,7)]
  assert D[q]==d
 pairs=None;mod=r.SRC.parent.parent/'src/modal_fit.py'
 for node in ast.parse(mod.read_text()).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OUTER_JL' for t in node.targets):pairs=ast.literal_eval(node.value)
 al=[k-3-j*(1-k)-2*l for j,l in pairs];assert al==list(map(F,exact['outer_exponents']));BO=[]
 for q in range(5,10):
  b=[F(0)]*10;b[q]=1
  for j in range(1,5):b[j]=-prod((al[q]-al[l])/(al[j]-al[l]) for l in range(1,5) if l!=j)
  BO.append(b)
 assert BO==[list(map(F,row)) for row in exact['outer_B']]
 scales=list(map(F,exact['scales']));assert len(scales)==38 and all(s>0 for s in scales)
 jumps={v:[[F(0)]*38 for _ in range(8)] for v in ('minus','plus','outer')}
 finite={i:i for i in range(4)}|{i:i-3 for i in range(7,33)}
 for n in range(8):
  for i,bi in finite.items():jumps['minus'][n][i]=endpoints[0][bi][n];jumps['plus'][n][i]=-endpoints[1][bi][n]
  for i in range(7):jumps['minus'][n][i]-=sum(v*x**n for v,x in zip(D[i],ex))
  for i,b in enumerate(BO):jumps['outer'][n][i+33]=sum(v*x**n for v,x in zip(b,al))
 assert all(x==0 for rows in jumps.values() for row in rows[:4] for x in row)
 for v,cols in [('minus',[7,8,9]),('plus',[32,31,30])]:
  for a,n in enumerate(range(4,7)):
   assert jumps[v][n][cols[a]]!=0
   assert all(jumps[v][n][c]==0 for c in cols[a+1:])
   assert all(jumps[w][n][c]==0 for w in jumps if w!=v for c in cols)
 assert rref([row[33:] for row in jumps['outer'][4:6]])['rank']==2
 assert rref([row[33:] for row in jumps['outer'][4:7]])['rank']==3
 matrices={};answers={}
 for typ,orders,prefer,dim in [('high_input',[4,5],[7,8,32,31,33,34],32),('high_graph',[4,5,6],[7,8,9,32,31,30,33,34,35],29)]:
  rows=[jumps[v][n] for v in jumps for n in orders];A=[[v/s for v,s in zip(row,scales)] for row in rows]
  ans=rref(A,prefer);assert ans['rank']==38-dim and len(ans['basis_columns'])==dim and ans['pivot_columns']==prefer
  assert rref(A)['rank']==ans['rank']
  if typ=='high_graph':assert all(sum(x*y for x,y in zip(row,v))==0 for row in matrices['high_input'] for v in ans['basis_columns'])
  matrices[typ]=A;answers[typ]={**ans,'rows':[[v,n] for v in jumps for n in orders],'matrix':A,'dimension':dim}
 def serial(x):
  if isinstance(x,F):return str(x)
  if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
  if isinstance(x,list):return [serial(v) for v in x]
  return x
 outfile=TOP/'evidence/exact_constraints.json'
 outfile.write_text(json.dumps(serial({'labels':exact['labels'],'scales':scales,'unscaled_jumps_through7':jumps,'endpoints':endpoints,**answers}),indent=2)+'\n')
 deps=[ROOT/'proofs/198_pure_spline_input_gram/code/check.py',ROOT/'proofs/04_modal_scalar/code/recompute.py',ROOT/'proofs/206_pure_spline_high_domain/PROOF.md',ROOT/'proofs/206_pure_spline_high_domain/AUDIT_CLARIFICATIONS.md',ROOT/'proofs/206_pure_spline_high_domain/evidence/check.json',ROOT/'proofs/235_shifted_outer_input/PROOF.md',ROOT/'proofs/235_shifted_outer_input/AUDIT_CLARIFICATIONS.md',ROOT/'proofs/239_s1j1_full_input/PROOF.md',ROOT/'proofs/239_s1j1_full_input/evidence/check.json',exactpath]
 # The analytic space and coefficient sources are bound as files, independently of the algebraic run.
 for name in ('173','174','126'):
  dirs=list((ROOT/'proofs').glob(name+'_*'));assert len(dirs)==1
  deps.append(dirs[0]/'PROOF.md')
 record={'date':datetime.now(timezone.utc).isoformat(),'status':'EXACT_RANKS_AND_NULLSPACES_CONFIRMED','proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(__file__),'source_sha256':sha(r.SRC),'outer_pair_source_sha256':sha(mod),'dependencies':{str(p.relative_to(ROOT)):sha(p) for p in deps},'exact_export_sha256':sha(outfile),'original_endpoint_polynomial_checks':checks,'jump_orders_checked':list(range(8)),'C3_columns_checked':38,'high_input_rank':6,'high_input_dimension':32,'high_graph_rank':9,'high_graph_dimension':29,'nullspace_identity_count':6*32+9*29+6*29,'seconds':time.monotonic()-start,'scope':'Exact declared basis intersections only; analytic review pending; no high operator norm or output certificate.'}
 (TOP/'evidence/check.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)
if __name__=='__main__':main()
