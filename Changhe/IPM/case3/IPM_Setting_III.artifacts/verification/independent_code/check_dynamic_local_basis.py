import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json
import numpy as np
import sympy as s
from scipy.linalg import svd
out=Path('research/dynamic_local_basis_audit/verification')
source=out/'dr.frozen.py';tree=ast.parse(source.read_text());cl=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name=='DR')
methods=[x for x in cl.body if isinstance(x,ast.FunctionDef) and x.name=='exterior_moments']
assert len(methods)==2
checks=1
t,z,a,cx,cw,c,e,f=s.symbols('t z a cx cw c e f');sk=-1+2*(t-z)/(1-z)
assert s.simplify(s.integrate((2+t)*(sk-t)/8,(t,-1,1))+5*(1+z)/(12*(1-z)))==0;checks+=1
assert s.expand(cw*e-3*(cx+c)*e-a*f).subs(cx,cw-c).expand()==-2*cw*e-a*f;checks+=1
A=s.diag(s.Rational(1,10**10),1);L=s.diag(1,-1)
assert A.inv()*L*A==L;checks+=1
V=s.Matrix([1,0]);J=s.Matrix([[0,1],[1,0]])
assert (V.T*J*V)[0]==0 and set(J.eigenvals())=={-1,1};checks+=1
rows=[];mom=[]
for N,M in [(64,16),(96,24),(128,32)]:
 nodes=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1));sig=(1+nodes)/2
 for basis in ['cheb','local']:
  details=[]
  for k in range(M):
   coord=nodes if basis=='cheb' else -1+2*(nodes-nodes[k])/(1-nodes[k])
   B=sig[:,None]**k*np.polynomial.chebyshev.chebvander(coord,N-k)
   singular=svd(B,compute_uv=False,lapack_driver='gesvd')
   details.append(dict(k=k,ratio=float(singular[-1]/singular[0]),smax=float(singular[0]),smin=float(singular[-1]),discarded={str(rc):int(np.sum(singular<=rc*singular[0])) for rc in [1e-13,1e-10,1e-8]},max_inner=float(np.max(np.abs(B[:k]))) if k else 0))
  rows.append(dict(N=N,M=M,basis=basis,details=details,minimum_ratio=min(q['ratio'] for q in details),discarded={str(rc):sum(q['discarded'][str(rc)] for q in details) for rc in [1e-13,1e-10,1e-8]}))
 zz=nodes[1];ga,w=np.polynomial.legendre.leggauss(64);shift=-1+2*(ga-zz)/(1-zz)
 correct=float(np.dot(w,(2+ga)*shift/8));wrong=float(np.dot(w,(2+ga)*ga/8));difference=-5*(1+zz)/(12*(1-zz))
 assert abs(correct-wrong-difference)<2e-15;checks+=1
 mom.append(dict(N=N,t1=float(zz),correct=correct,wrong=wrong,error_correct_minus_wrong=difference))
record=dict(utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),duplicate_method_lines=[m.lineno for m in methods],finite_manufactured_checks=checks,all_pass=True,conditioning=rows,moment_manufactures=mom)
(out/'CHECKS.json').write_text(json.dumps(record,indent=2)+'\n')
lines=['# Independent finite audit','',f"UTC {record['utc']}; source SHA256 {record['source_sha256']}",'',f'{checks} checks passed. Numerical singular values below roundoff have only floating-point diagnostic meaning.','', '|N|M|basis|min singular ratio|discard1e-13|discard1e-10|discard1e-8|','|---|---|---|---|---|---|---|']
for r in rows:lines.append(f"|{r['N']}|{r['M']}|{r['basis']}|{r['minimum_ratio']:.6e}|{r['discarded']['1e-13']}|{r['discarded']['1e-10']}|{r['discarded']['1e-08']}|")
lines+=['','The duplicate moment method evaluates a different field. Correct minus wrong for the k=1 shifted-linear manufacture:']
for r in mom:lines.append(f"N={r['N']}: {r['error_correct_minus_wrong']:.12e}.")
(out/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
