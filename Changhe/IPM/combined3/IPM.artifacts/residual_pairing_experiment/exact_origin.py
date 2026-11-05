"""Exact residual Taylor polynomial for a smooth numerical origin extension."""
import json,sys,time
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace
from flint import fmpq as Q
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,C
from asymptotics013 import Expansion
from exact_far import polys,SHIFT
tick=time.monotonic();e=Evaluator()
# Higher n cannot contribute through Cartesian order four at residual power 9.
a=Expansion(SimpleNamespace(groups=[g for g in e.groups if g[1]<=13]),'origin',degree=6)
fields={}
for name,i,j in [('rho',0,0),('rho',1,0),('rho',0,1),('u1',0,0),('u2',0,0)]:
    fields[name,i,j]={k:v for k,v in a.field(name,i,j).items()if k[2]<=9}
out=defaultdict(Q)
for (kind,n,p),c in fields['rho',0,0].items():out[kind,n,p]+=(C*p-1)*c
for vk,gk in [(('u1',0,0),('rho',1,0)),(('u2',0,0),('rho',0,1))]:
    for (p,k),P in polys(fields[vk]).items():
        for (q,l),T in polys(fields[gk]).items():
            if p+q>9:continue
            assert k!=l
            PT=P*T
            for n in range(1,14):
                c=2*PT[2*SHIFT+n]
                if c:out['s',n,p+q]+=c
terms=[{'kind':k,'n':n,'power':int(p),'exact':str(v),'float':float(v)}for(k,n,p),v in sorted(out.items())if v]
assert all(q['power']>=q['n']and(q['power']-q['n'])%2==0 for q in terms)
result={'status':'EXACT_ORIGIN_TAYLOR_THROUGH_POWER_9','terms':terms,'elapsed_seconds':time.monotonic()-tick}
(HERE/'exact_origin_result.json').write_text(json.dumps(result,indent=2)+'\n')
print({**result,'terms':[{k:v for k,v in q.items()if k!='exact'}for q in terms]},flush=True)
