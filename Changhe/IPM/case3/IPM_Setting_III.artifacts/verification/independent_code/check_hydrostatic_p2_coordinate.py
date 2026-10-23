"""Coordinate repair regression against a separate higher-precision bisection."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import mpmath as mp
from hydrostatic_p2_elementary_axis import coordinate
ROOT=Path('research/hydrostatic_p2_elementary_axis');V=ROOT/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def ref(C,y):
 if not y:return mp.mpf(1)
 if y<C:
  lo=mp.mpf(0);hi=min(mp.mpf('0.75'),y/C)
  for unused in range(mp.mp.prec+8):
   mid=(lo+hi)/2
   if mid/(1-mid*mid)**2>y/C:hi=mid
   else:lo=mid
  return 1-((lo+hi)/2)**2
 # Bisect the original squared equation in a scaled variable; no Newton.
 q=mp.sqrt(C/y);lo=mp.mpf('.5');hi=mp.mpf(1)
 for unused in range(mp.mp.prec+8):
  mid=(lo+hi)/2
  if mid**4+q*mid>1:hi=mid
  else:lo=mid
 return q*(lo+hi)/2
for digits in [65,100,194,254]:
 with mp.workdps(digits):
  for cs in ['0.125','0.7','5']:
   C=mp.mpf(cs)
   for factor in ['0','1e-200','1e-100','1e-30','1e-3','.5','.999999','1','1.000001','2','16','1e6','1e12','1e100','1e500']:
    y=C*mp.mpf(factor);got=coordinate(C,y);eps=mp.eps
    with mp.workdps(digits+40):want=ref(C,y);error=abs(got-want)/want
    label=f'dps{digits} C{cs} y/C{factor}'
    ck(label+' bisected relative w',error<32*eps,mp.nstr(error/eps,20))
    ck(label+' range',0<got<=1)
    if y>=C:
     q=mp.sqrt(C/y);v=got/q
     ck(label+' quartic residual',abs(v**4+q*v-1)<32*eps)
old=json.loads((V/'COORDINATE_OLD_FAILURES.json').read_text())
with mp.workdps(old['dps']):
 C=mp.mpf(old['C']);eps=mp.eps
 for rec in old['failures']:
  y=mp.power(10,mp.mpf(2)+mp.mpf(10)*rec['index']/320);got=coordinate(C,y)
  with mp.workdps(old['dps']+40):want=ref(C,y)
  ck('actual failed point '+str(rec['index']),abs(got-want)<32*eps*want)
 for i in range(641):
  y=mp.power(10,mp.mpf(2)+mp.mpf(10)*i/640);w=coordinate(C,y);q=mp.sqrt(C/y)
  ck('complete 640 panel coordinate '+str(i),abs((w/q)**4+w-1)<32*eps)
for C,y in [('1','-1'),('0','1'),('-1','1')]:
 try:coordinate(C,y);ck('invalid '+C+','+y,False)
 except ValueError:ck('invalid '+C+','+y,True)
result=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(ROOT/'COORDINATE_REPAIR_PROOF.md'),module_sha256=sha('independent_code/hydrostatic_p2_elementary_axis.py'),driver_sha256=sha(__file__),failure_sha256=sha(V/'COORDINATE_OLD_FAILURES.json'))
(V/'COORDINATE_GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([c for c in checks if not c['passed']])
if result['status']!='PASS':raise SystemExit(1)
