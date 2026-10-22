"""Independent exact integer-tenth-root audit and Arb1536 strain norm."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/source_semigroup';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def nthroot(N,k):
 x=1<<((N.bit_length()+k-1)//k)
 while True:
  y=((k-1)*x+N//x**(k-1))//k
  if y>=x:break
  x=y
 assert x**k<=N<(x+1)**k
 return x
def ep(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def main():
 start=time.monotonic();data=json.loads((E/'checks.json').read_text());n=0;contains=0;roots=0;scale=1<<1536
 for p,h in data['files'].items():assert sha(B/p)==h
 def contain(record,lo,hi):
  nonlocal contains
  assert F(record['lower_exact'])<=lo<=hi<=F(record['upper_exact']),(record,lo,hi)
  contains+=1
 for row in data['rows']:
  A,mu,EE,Dw,R=map(F,[row[k] for k in ['A','mu','E','Dw','R']]);decay=F(1687,500)-EE;gap=(F(2)+A+mu)/2-F(1687,500)+F(31,10)*Dw
  assert decay==F(row['a_s']) and gap==F(row['gap']) and gap>=F(3121,1000);n+=3
  base=(gap+R)/gap;assert base==F(row['base']);target=base**31
  scaled=target.numerator*(scale**10);den=target.denominator;floor=nthroot(scaled//den,10)
  assert floor**10*den<=scaled<(floor+1)**10*den;roots+=1
  lo=F(floor,scale);hi=lo if floor**10*den==scaled else F(floor+1,scale)
  contain(row['bounds']['C'],lo,hi);contain(row['bounds']['K_A'],lo/decay,hi/decay)
 beta=(arb(fmpq(25,231))/arb.pi()).sqrt();contain(data['beta_s'],ep(beta.lower()),ep(beta.upper()))
 files=dict(data['files']);files[str((E/'checks.json').relative_to(B))]=sha(E/'checks.json');files[str(Path(__file__).relative_to(B))]=sha(__file__)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_INTEGER_ROOT_INVERSE_AUDIT','method':'Exact integer Newton tenth roots of rational base^31 with independent cross-multiplied endpoint inequalities at1536bits; Arb1536 strain norm square root. No producer imports.','counts':{'exact_rational_row_checks':n,'exact_integer_root_enclosures':roots,'full_enclosure_contains':contains},'files':files,'seconds':time.monotonic()-start}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()
