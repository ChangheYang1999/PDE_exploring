from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,math
from flint import fmpq,fmpq_poly
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def fq(q):q=F(q);return fmpq(q.numerator,q.denominator)
v=json.loads((B/'research/residual_cell_cauchy/evidence/verdict.json').read_text());assert v['status']=='CONFIRMED_THREE_CELL_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED';pins=dict(v['files'])
for n,h in pins.items():assert sha(B/n)==h
# Exact polynomial identities on monomials, including both half-interval restrictions.
count=0
for degree in range(9):
 for power in range(degree+1):
  beta=[fq(F(math.comb(k,power),math.comb(degree,power))) if k>=power else fmpq(0) for k in range(degree+1)]
  for side in [0,1]:
   if side==0:b=[sum((beta[q]*fq(F(math.comb(k,q),2**k)) for q in range(k+1)),fmpq(0)) for k in range(degree+1)]
   else:b=[sum((beta[k+q]*fq(F(math.comb(degree-k,q),2**(degree-k))) for q in range(degree-k+1)),fmpq(0)) for k in range(degree+1)]
   poly=sum((fmpq_poly([0,1])**k*fmpq_poly([1,-1])**(degree-k)*(math.comb(degree,k)*b[k]) for k in range(degree+1)),fmpq_poly([0]));assert poly==fmpq_poly([fq(F(side,2)),fq(F(1,2))])**power;count+=1
for p in [B/'research/residual_cell_cauchy/evidence/verdict.json',D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
manifest={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_BERNSTEIN_INPUT_BINDING_AND_EXACT_SUBDIVISION_IDENTITIES','cells':[4102,4125,4211],'subcells':8,'depth':3,'degree':64,'modes':522,'orders':6,'chunks':[[a,min(a+64,522)] for a in range(0,522,64)],'exact_toy_subdivision_checks':count,'files':dict(sorted(pins.items())),'scope':'Only already accepted three-cell Taylor input. No new moment integration or complete cover.'}
with (D/'data_exact/manifest.json').open('x') as f:json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps({'utc':manifest['utc'],'status':manifest['status'],'pins':len(pins),'toy_checks':count}))
