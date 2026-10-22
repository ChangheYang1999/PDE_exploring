"""Independent exact tests of packet138's lowest-y-power extension."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,time
from exact_bivariate import add,scale,mul,diff,trunc,homogeneous
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);tic=time.perf_counter();ncheck=0;sample=[]
for beta in [Q(9,4),Q(3),Q(7,2),Q(100)]:
 L=1+3*beta/2;k=beta-2
 assert 0<k/L<Q(2,3)
 for d in range(1,9):
  J={(a,d-a):Q((-1)**a*(a+d),a+1)for a in range(1,d+1,2)}
  for N in range(2,9):
   tn={(a,N-a):Q((-1)**(a//2)*(a+N),2*a+1)for a in range(2,N+1,2)}
   H=diff(tn,0);deg=d+N-1
   P=add(scale(mul(mul({(0,1):Q(1)},J,deg),diff(H,1),deg),-L),
         mul(add(scale(mul({(0,1):Q(1)},diff(J,1),deg),L),scale(J,k-L)),H,deg))
   assert P
   s=min(b for a,b in J);b=min(j for i,j in H);lowest={z:v for z,v in P.items()if z[1]==s+b}
   A={(a,0):v for(a,j),v in J.items()if j==s};B={(a,0):v for(a,j),v in H.items()if j==b}
   predicted={(a,s+b):v*(L*(s-b-1)+k)for(a,j),v in mul(A,B,deg).items()}
   assert lowest==predicted and predicted
   # Independent complete M evaluation with W2_x=J exactly and later terms.
   W2=add({(0,1):L,(0,2):Q(3,7)},{(a+1,j):v/(a+1)for(a,j),v in J.items()})
   t=add(tn,{(2,N):Q(4,11)})
   cap=deg+2
   E=add(mul(mul(J,J,cap),diff(t,1),cap),scale(mul(mul(J,W2,cap),diff(diff(t,0),1),cap),-1),
         mul(add(mul(W2,diff(J,1),cap),mul(J,add({(0,0):k},scale(diff(W2,1),-1)),cap)),diff(t,0),cap))
   assert not trunc(E,deg-1) and homogeneous(E,deg)==P
   ncheck+=1
   if d in [1,4,8] and N in [2,8]:sample.append({'beta':str(beta),'J_degree':d,'t_degree':N,'E_degree':deg,'lowest_y_multiplier':str(L*(s-b-1)+k)})
# At beta2 the leading operator can have a kernel even for nonzero J and t.
# This is an operator-level control, not the primitive of a B2 stream source.
J={(1,1):Q(1)};W2={(0,1):Q(4),(2,1):Q(1,2)};t={(2,0):Q(1)};cap=8
E=add(mul(mul(J,J,cap),diff(t,1),cap),scale(mul(mul(J,W2,cap),diff(diff(t,0),1),cap),-1),
      mul(add(mul(W2,diff(J,1),cap),scale(mul(J,diff(W2,1),cap),-1)),diff(t,0),cap))
assert not E and diff(W2,0)==J
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'ALL_LOWEST_Y_CONTROLS_PASSED','elapsed_seconds':time.perf_counter()-tic,'cases':ncheck,'samples':sample,'beta2_operator_kernel_control':{'J':'x*y','W2':'4*y+x²*y/2','t':'x²','E':'0','scope':'Operator only; no claim that t is the residual of a normalized source primitive.'}}
(out/'tests.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],ncheck,r['elapsed_seconds'],flush=True)
