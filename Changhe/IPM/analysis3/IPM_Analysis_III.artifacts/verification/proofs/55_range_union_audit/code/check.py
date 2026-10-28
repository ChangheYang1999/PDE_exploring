import sys, importlib.util, hashlib, json
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, fmpq, ctx
root=Path(__file__).resolve().parents[3]
p=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root.parent/'s2-num/work'))
from exact_trial import ExpPoly
spec=importlib.util.spec_from_file_location('audited_encl',p/'evidence/encl_snapshot.py')
encl=importlib.util.module_from_spec(spec);spec.loader.exec_module(encl)
ctx.prec=256
f=ExpPoly([(fmpq(0),[arb(1)+arb(2)**(-80)]),(fmpq(10),[arb(2)**(-200)])])
cl={'h':arb(1),'hq':fmpq(1),'kind':'cell'}
result=encl.range_finite(f,cl,K=8,split=6)
x0=f(arb(0))
sub=[encl.taylor_range(f.shift(arb(i)/2),arb(1)/2) for i in range(2)]
assert all(s.contains(f(arb(i)/2)) for i,s in enumerate(sub))
assert not result.contains(x0)
out={'date':datetime.now(timezone.utc).isoformat(),'bits':ctx.prec,
     'snapshot_sha256':hashlib.sha256((p/'evidence/encl_snapshot.py').read_bytes()).hexdigest(),
     'result':str(result),'f0':str(x0),'contains_f0':bool(result.contains(x0)),
     'subintervals':[str(s) for s in sub],
     'float_endpoints':[[float(s.lower()),float(s.upper())] for s in sub],
     'status':'COUNTEREXAMPLE_CONFIRMED'}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
