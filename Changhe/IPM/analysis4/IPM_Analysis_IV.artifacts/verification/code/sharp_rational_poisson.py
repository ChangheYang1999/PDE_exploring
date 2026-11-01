"""Exact column checks of the sharper rational Poisson operator estimate."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
start=time.monotonic();rows=[];count=0
for h,Q in [(1,3),(1,4),(1,5),(1,6),(2,5),(2,7),(3,7),(3,8),(2,9),(3,13)]:
    delta=F(2*h,Q);bound=F(3*Q*Q,4*(3*Q-1));maximum=F(0);where=None
    for n in range(1,4*Q+1):
        P=2-n*delta;p=P-1
        for ell in range(1,4*Q+2,2):
            norm=F(0)
            for m in [ell-1,ell+1]:
                if m==0 or m*m==P*P:continue
                original=(p+ell if m==ell-1 else p-ell)/(2*(m*m-P*P))
                canceled=1/(2*(ell-1-P)) if m==ell-1 else -1/(2*(ell+1+P))
                assert original==canceled
                norm+=abs(original);count+=1
            assert norm<=bound,(h,Q,n,ell,norm,bound)
            if norm>maximum:maximum=norm;where=[n,ell]
    rows.append(dict(h=h,Q=Q,bound=str(bound),observed_maximum=str(maximum),where=where))
assert next(r for r in rows if r['h']==2 and r['Q']==9)['observed_maximum']=='243/104'
root=Path('research/169_sharp_rational_poisson')
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,column_coefficient_comparisons=count,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/sharp_rational_poisson.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result),flush=True)
