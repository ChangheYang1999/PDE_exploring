from pathlib import Path
from datetime import datetime,timezone
from math import factorial,comb
import sys,importlib.util,json,hashlib
from flint import arb,ctx,fmpq
TOP=Path(__file__).resolve().parents[1]
ROOT=TOP.parents[1]
sys.path.insert(0,str(ROOT.parent/'s2-num/work'))
from exact_trial import ExpPoly,q2arb
spec=importlib.util.spec_from_file_location('encl_audited',TOP/'evidence/encl_snapshot.py')
encl=importlib.util.module_from_spec(spec);spec.loader.exec_module(encl)
def phi(z,p,N=64):
 value=arb(0);term=arb(1)
 for j in range(N):
  value+=term/(p+j+1);term*=z/(j+1)
 M=abs(z).upper();err=(M.exp()*M**N/factorial(N)/(N+p+1)).upper()
 return value+arb(0,err)
def record(x):return {'ball':x.str(45),'radius':x.rad().str(12)}
ctx.prec=256
f=ExpPoly([(fmpq(0),[arb(1)+arb(2)**-80]),(fmpq(10),[arb(2)**-200])])
cl={'h':arb(1),'hq':fmpq(1),'kind':'inner'}
b=encl.range_finite(f,cl)
assert b.contains(f(arb(0)))
out={'date':datetime.now(timezone.utc).isoformat(),'snapshot_sha256':hashlib.sha256((TOP/'evidence/encl_snapshot.py').read_bytes()).hexdigest(),'offset_regression':{'contains_f0':True,'range':record(b)}}
ctx.prec=512
lamq=fmpq(75,70368744177664);lam=q2arb(lamq);mu=-lam;p=6
cs=[arb((-1)**(p-a)*factorial(p)//factorial(a))/mu**(p-a+1) for a in range(p+1)]
f=ExpPoly([(fmpq(-52)-lamq,cs),(fmpq(-52),[-cs[0]])])
b=encl.range_finite(f,cl)
bare=encl.taylor_range(f,arb(1))
for j in range(65):
 x=arb(j)/64;v=(-52*x).exp()*x**7*phi(-lam*x,p)
 assert b.contains(v),(j,b,v)
out['resonance_regression']={'lambda_exact':str(lamq),'bits':512,'merged_range':record(b),'unmerged_taylor_range':record(bare),'points_checked':65}
out['verdict']='PASS: previous offset counterexample repaired; actual-lambda merged range contains independent stable evaluations'
out['finished']=datetime.now(timezone.utc).isoformat()
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
