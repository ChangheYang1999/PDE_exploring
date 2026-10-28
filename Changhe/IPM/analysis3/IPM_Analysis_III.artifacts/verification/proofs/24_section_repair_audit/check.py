from pathlib import Path
from datetime import datetime,timezone
from types import SimpleNamespace
from fractions import Fraction
import sys,hashlib,json
import numpy as np
from flint import arb,arb_mat,fmpq,fmpq_mat,ctx
T=Path(__file__).resolve().parent
sys.path.insert(0,str(T/'code_snapshot'))
from opimage import Cells,Column,green_A_on_cell,green_B_on_cell
from section import TestSplines
from exact_trial import ExpPoly,moment_minf
from certify import inf_norm
ctx.prec=256
fixture=SimpleNamespace(p=7,t_lo_q=fmpq(0),t_hi_q=fmpq(2),nc=2,tb_q=[fmpq(0),fmpq(1),fmpq(2)],tb=[arb(0),arb(1),arb(2)],h_q=[fmpq(1),fmpq(1)])
C=Cells(fixture,[fmpq(1)],[fmpq(1)]);B=TestSplines(fixture,C,1)
assert B.active==list(range(1,B.nb-1))
for ic,pieces in B.pieces.items(): assert all(i in B.active for i,_ in pieces)
first=min(B.pieces);last=max(B.pieces)
assert all(co[0]==0 for _,co in B.pieces[first])
h=C.cells[last]['h']
assert all(sum((q*h**j for j,q in enumerate(co)),arb(0)).contains(0) for _,co in B.pieces[last])
assert 0 not in B.pieces and C.n-1 not in B.pieces
f=ExpPoly([(fmpq(0),[arb(1)])]);g=green_A_on_cell(f,1,moment_minf(arb(6),0),arb(1),'minf')
assert fmpq(-2) not in g.terms and g.terms[fmpq(4)][0].contains(arb(1)/6)
fo=ExpPoly([(fmpq(-3),[arb(1)])]);gb=green_B_on_cell(fo,1,None,arb(1),None,'pinf')
assert fmpq(2) not in gb.terms and gb.terms[fmpq(1)][0]==1
# Exact dyadic counterexample to treating nearest-rounded float as an upper bound.
v=arb(1)+arb(2)**(-54);bad=arb(float(v.upper())).sqrt()
assert bad==1 and v.sqrt()>bad
normbad=inf_norm(arb_mat([[v]])); assert arb(normbad)<v
# A signed ball upper endpoint has the wrong sign for an absolute upper bound.
neg=arb(-1,2.0**-30)
assert arb(abs(float(neg.upper()))) < abs(neg).upper()
# Actual original tail angular vector, without the irrelevant repaired mode0.
src=Path('source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz')
raw=np.load(src,allow_pickle=False);coeff=[fmpq(*float(v).as_integer_ratio()) for v in raw['Aout'][:,0]];M=len(coeff)
P=fmpq_mat(M+1,M)
for m in range(M):
 for k,sg in [(1+2*m,1),(1-2*m,1),(3+2*m,1),(3-2*m,1)]:
  if k<0:k,sg=-k,-sg
  j=(k-1)//2
  if j<M+1:P[j,m]+=fmpq(sg,8)
full={j:sum((P[j,m]*coeff[m] for m in range(M)),fmpq(0)) for j in range(M+1)}
wrong={j:P[j,0] for j in range(M+1) if P[j,0]!=0}
missing=[j for j in range(2,M+1) if full[j]!=0 and j not in wrong]
assert len(missing)>200
# This assertion uses only angular constructor logic, no Green arithmetic.
saved=Column._green;Column._green=lambda self:None
TT=SimpleNamespace(Mj=M+1,Nf=M+1,P_q=P)
CC=Column(0,{},TT,None,coef={m:arb(coeff[m].numerator)/arb(coeff[m].denominator) for m in range(M)})
Column._green=saved
assert all(CC.Pcol[j].contains(arb(full[j].numerator)/arb(full[j].denominator)) for j in missing)
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','test_active_count':len(B.active),'canonical_inner_terms':[str(x) for x in g.terms],'canonical_outer_terms':[str(x) for x in gb.terms],'rounding_counterexample_v':'1+2^-54','rounded_sqrt':str(bad),'rounded_inf_norm':normbad,'aggregate_missed_density_modes':len(missing),'first_missed_mode':missing[0],'first_missed_coefficient':str(full[missing[0]]),'last_missed_mode':missing[-1],'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(T/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
