"""Independent exact controls for146, not a proof of any full profile."""
from pathlib import Path
import sys,json,datetime,time
import sympy as S
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
x,y=S.symbols('x y');r2=x*x+y*y
rows=[]
def disk_integral(expr):
 out=0
 for (i,j),a in S.Poly(S.expand(expr),x,y).terms():
  if i%2==0 and j%2==0:
   out+=a*S.gamma(S.Rational(i+1,2))*S.gamma(S.Rational(j+1,2))/S.gamma(S.Rational(i+j,2)+2)
 return S.simplify(out)
for beta in [S.Rational(9,4),S.Integer(3),S.Integer(6)]:
 c=1+beta/2;q=4/beta;psi=(c*x*y-q*x**3/6)*(1-r2)**8;om=-S.diff(psi,x,2)-S.diff(psi,y,2)
 points=[]
 for xx in [S.Rational(k,16) for k in range(1,16)]:
  vv=S.factor(om.subs({x:xx,y:0}));points.append({'x':str(xx),'y':'0','Omega':str(vv),'positive':bool(vv>0),'negative':bool(vv<0)})
 moment=disk_integral(x*om)
 centers=[S.diff(psi,x,y).subs({x:0,y:0})==c,S.diff(om,x).subs({x:0,y:0})==q,S.diff(psi,x,y,2).subs({x:0,y:0})==0]
 odd=S.expand(om.subs(x,-x)+om)==0
 rows.append({'beta':str(beta),'int_x_Omega':str(moment),'center_checks':centers,'odd':odd,'positive_witness':next(p for p in points if p['positive']),'negative_witness':next(p for p in points if p['negative']),'all_pass':bool(moment==0 and all(centers) and odd and any(p['negative'] for p in points))})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_pass':all(r['all_pass'] for r in rows),'controls':rows,'scope':'Exact C7 compact stream controls with the B2 stream/vorticity center jets. No temperature field, exact transport or full B2 profile is supplied. The smooth general theorem is established in146 before these finite controls.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if not result['all_pass']:raise SystemExit(1)
