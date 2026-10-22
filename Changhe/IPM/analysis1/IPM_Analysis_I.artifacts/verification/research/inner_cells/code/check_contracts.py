"""Exact coefficient/Green identities and finite integral contract tests."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];sys.path.insert(0,str(Path(__file__).resolve().parent))
import cell_arb as ca
import cell_integer_iv as ci
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run():
 ad=ca.setup();ind=ci.setup();assert ad['cs']==ind['cs'] and ad['alpha']==ind['alpha'];checks=0
 for n in range(1,262):
  m=2*n
  for al,cm,cp,qf in zip(ad['alpha'],ad['cs'][n-1],ad['cs'][n],ad['lower'][n-1]):
   qi=ci.inverse_explicit(cm,m+4+al);target=[(x+y)/2-m*z for x,y,z in zip(cm,cp,qi)];assert target==qf,(n,str(al));checks+=len(target)
   p=ad['forcing'][n-1][ad['alpha'].index(al)];assert ca.inverse(p,m+4+al)==ci.inverse_explicit(p,m+4+al);checks+=len(p)
 for qa,qi in zip(ad['b1'],ind['b1']):assert qa==qi;checks+=len(qa)
 tests=0
 for p,offset,length,rate,expected in [([F(0),F(0),F(1)],F(-2),F(3),F(0),F(3)),([F(1)],F(0),F(2),F(0),F(2))]:
  x=ca.moments.integ([ca.aa(c) for c in p],offset,length,rate);y=ci.integrals.integrate(p,offset,length,rate);assert ca.dy(x.lower())<=expected<=ca.dy(x.upper());lo,hi=ci.ends(y);assert lo<=expected<=hi;tests+=2
 # Near-resonance plus nonzero-rate antiderivative paths, with independent shifts.
 for rate in [ad['alpha'][-1]-50,F(-3),F(7)]:
  p=list(map(F,[2,-3,1]));offset=F(-7,5);length=F(7,5);x=ca.moments.integ([ca.aa(c) for c in p],offset,length,rate);y=ci.integrals.integrate(p,offset,length,rate);al,ah=ca.dy(x.lower()),ca.dy(x.upper());il,ih=ci.ends(y);assert max(al,il)<=min(ah,ih);tests+=1
 paths=['research/inner_cells/PROOF.md','research/inner_cells/code/cell_arb.py','research/inner_cells/code/cell_integer_iv.py','research/inner_cells/code/check_contracts.py','research/inner_majorant/code/certify_inner.py','research/inner_majorant/code/audit_inner_iv.py','research/inner_majorant/evidence/verdict.json']
 r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CONTRACTS','exact_Green_scalar_checks':checks,'integral_contract_checks':tests,'upper_rows_each':260,'dependency_pins':{p:sha(B/p) for p in paths}};(B/'research/inner_cells/evidence/contracts.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='dependency_pins'}))
if __name__=='__main__':run()
