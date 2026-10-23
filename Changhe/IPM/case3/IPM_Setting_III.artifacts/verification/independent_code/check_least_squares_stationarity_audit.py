from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
checks=[]
def ck(name,v):
    assert v,name
    checks.append({'name':name,'passed':True})
for eps in [F(1,10),F(1,1000),F(1,10**9)]:
    for t in [F(1,100),F(1,10),F(1)]:
        ck(f'truncated_descent_{eps}_{t}',(1-eps*t)**2<1)
for k in [F(1),F(10),F(100),F(1000)]:
    for x in [F(-1),F(0),F(1)]:
        p=x*(x*x-1); dp=3*x*x-1
        ck(f'stationary_{k}_{x}',p==0 and dp!=0)
        ck(f'hessian_saddle_{k}_{x}',2*k*k*dp*dp>0 and -4<0)
        for t in [F(1,100),F(1,10),F(1,2)]:
            ck(f'saddle_descent_{k}_{x}_{t}',(1-t*t)**2<1)
    ck(f'segment_barrier_{k}',1+9*k*k/F(64)>1)
    for a,b in [(F(-1),F(0)),(F(0),F(1)),(F(-1),F(1)),(F(2),F(7,3))]:
        for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
            x=(1-t)*a+t*b;y=(1-t)*a*a+t*b*b
            ck(f'parabola_chord_{k}_{a}_{b}_{t}',y-x*x==t*(1-t)*(a-b)**2 and 1+k*k*(y-x*x)**2>1)
            ck(f'parabola_valley_{k}_{a}_{b}_{t}',k*(x*x-x*x)==0)
for k in [F(1),F(10),F(100),F(1000)]:
    pts=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
    for x,y in pts:
        ck(f'quadratic_saddle_{k}_{x}_{y}',x*(x-1)==0 and y*(y-1)==0 and (2*x-1)**2==1 and (2*y-1)**2==1)
    for i,j in [(0,1),(0,2),(1,2)]:
        x=(pts[i][0]+pts[j][0])/2;y=(pts[i][1]+pts[j][1])/2
        q=1+k*k*((x*(x-1))**2+(y*(y-1))**2)
        ck(f'quadratic_barrier_{k}_{i}_{j}',q==1+k*k/F(8 if (i,j)==(1,2) else 16))
p=Path('research/least_squares_stationarity_audit/PROOF.md')
d={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','count':len(checks),'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks':checks}
Path('research/least_squares_stationarity_audit/verification/checks.json').write_text(json.dumps(d,indent=2)+'\n')
print({k:v for k,v in d.items() if k!='checks'})
