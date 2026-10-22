"""Independent exact rational exponential moments with geometric remainder, no producer imports."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sys,json,hashlib,math,time
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/radial_defect';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();c=json.loads((E/'checks.json').read_text());inp=json.loads((E/'test_inputs.json').read_text());K=inp['exact_series_order'];n=0;tailchecks=0;contains=0
 def contain(rec,lo,hi):
  nonlocal contains
  assert F(rec['lower_exact'])<=lo<=hi<=F(rec['upper_exact']),(rec,lo,hi);contains+=1
 for row in c['rows']:
  mode=row['n'];lam=F(row['lambda']);h=F(row['h']);assert lam==(2*mode-2 if row['branch']=='+' else -2*mode-2)
  z=lam*h
  if lam<=0:Mlo=Mhi=F(1)
  else:
   term=F(1);total=term
   for k in range(1,K+1):term*=z/k;total+=term
   first=abs(term*z/(K+1));ratio=abs(z)/(K+2);assert ratio<1;tail=first/(1-ratio);Mlo=total-tail;Mhi=total+tail;tailchecks+=1
  contain(row['M'],Mlo,Mhi)
  for sj,rec in row['J'].items():
   j=int(sj)
   if lam==0:lo=hi=h**(j+1)/(j+1)
   else:
    term=F(1,math.factorial(j+1));total=term
    for k in range(1,K+1):term*=z/(j+k+1);total+=term
    first=abs(term*z/(j+K+2));ratio=abs(z)/(j+K+3);assert ratio<1
    tail=first/(1-ratio);pref=h**(j+1)*math.factorial(j);lo=pref*(total-tail);hi=pref*(total+tail);tailchecks+=1
   assert lo>0 and hi<=Mhi*h**(j+1)/(j+1);n+=1;contain(rec,lo,hi)
 for p,hsh in c['files'].items():assert sha(B/p)==hsh
 files=dict(c['files']);files[str(Path(__file__).relative_to(B))]=sha(__file__);files[str((E/'checks.json').relative_to(B))]=sha(E/'checks.json')
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_RATIONAL_RADIAL_MOMENTS','counts':{'moment_cases':n,'geometric_tail_checks':tailchecks,'full_enclosure_contains':contains},'method':'Exact rational signed series throughK300 and rational geometric remainder; no Arb,mpmath,numpy or producer imports.','files':files,'seconds':time.monotonic()-start}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()
