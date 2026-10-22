from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,json,hashlib
p=Path('code/replay_residual221.py');t=ast.parse(p.read_text());names=['num','add','neg','sub','mul','inv','div','ab','summ','contains'];ns={'F':F};nodes=[x for x in t.body if isinstance(x,ast.FunctionDef)and x.name in names];assert len(nodes)==len(names);exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
checks=[]
def ck(v,k):
 if not v:raise AssertionError(k)
 checks.append(k)
qs=[F(i,2)for i in range(-2,3)];iv=[(a,b)for a in qs for b in qs if a<=b]
for i,a in enumerate(iv):
 pts=[a[0],sum(a)/2,a[1]]
 for x in pts:ck(ns['contains'](ns['ab'](a),(abs(x),abs(x))),'absolute '+str((i,x)))
 if a[0]<=0<=a[1]:
  try:ns['inv'](a)
  except ArithmeticError:ck(True,'zero refused '+str(i))
  else:raise AssertionError('zero accepted')
 else:
  z=ns['inv'](a)
  for x in pts:ck(ns['contains'](z,(1/x,1/x)),'reciprocal '+str((i,x)))
 for j,b in enumerate(iv):
  prods=[x*y for x in a for y in b];ck(ns['mul'](a,b)==(min(prods),max(prods)),'corner attainment '+str((i,j)))
  for x in pts:
   for y in [b[0],sum(b)/2,b[1]]:
    ck(ns['contains'](ns['add'](a,b),(x+y,x+y)),'sum '+str((i,j,x,y)));ck(ns['contains'](ns['mul'](a,b),(x*y,x*y)),'product '+str((i,j,x,y)))
ck(ns['summ']([])==(F(0),F(0)),'empty sum');ck(ns['sub']((F(-2),F(3)),(F(-5),F(7)))==(F(-9),F(8)),'subtraction');ck(ns['div']((F(-2),F(3)),(F(-5),F(-2)))==(F(-3,2),F(1)),'negative denominator')
paths=[Path(__file__),p,Path('research/interval_residual221/RATIONAL_REPLAY_TEST_PROOF.md')];now=datetime.now(timezone.utc).isoformat();j={'utc':now,'status':'PASS_EXACT_RATIONAL_REPLAY_MACHINERY','check_count':len(checks),'check_labels_sha256':hashlib.sha256('\n'.join(checks).encode()).hexdigest(),'tested_interval_count':len(iv),'scope':'Own extracted pure endpoint functions only; no plan, producer, root, Taylor code or candidate execution. Exact finite endpoints/midpoints tests and corner-extremum identities.','hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}};Path('research/interval_residual221/verification/rational_replay.json').write_text(json.dumps(j,indent=2)+'\n');print(now,j['status'],len(checks))
