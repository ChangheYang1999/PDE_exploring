from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimization prohibited')
D=Path('research/polar_center_tail216');x,y,beta,a,c,b1,b2,g,d1,d2=S.symbols('x y beta a c b1 b2 g d1 d2');th=a*y+b1*x*x*y+b2*y**3;om=g*x*y;ps=c*x*y+d1*x**3*y+d2*x*y**3;u1=-S.diff(ps,y);u2=S.diff(ps,x);rt=S.Poly(S.expand((beta*x+u1)*S.diff(th,x)+(beta*y+u2)*S.diff(th,y)-(beta-2)*th),x,y);ro=S.Poly(S.expand((beta*x+u1)*S.diff(om,x)+(beta*y+u2)*S.diff(om,y)+om-S.diff(th,x)),x,y)
checks=[]
for name,got,want in [('T0',rt.coeff_monomial(y),a*(c+2)),('T1',rt.coeff_monomial(x*x*y),(2*beta-c+2)*b1+3*a*d1),('T2',rt.coeff_monomial(y**3),(2*beta+3*c+2)*b2+a*d2),('T3',ro.coeff_monomial(x*y),(2*beta+1)*g-2*b1),('Poisson',S.expand(-S.diff(ps,x,2)-S.diff(ps,y,2)-om),-(g+6*d1+6*d2)*x*y),('curl convention',S.diff(u2,x)-S.diff(u1,y),S.diff(ps,x,2)+S.diff(ps,y,2))]:
 if S.expand(got-want)!=0:raise RuntimeError(name)
 checks.append({'name':name,'actual':str(got),'expected':str(want)})
paths=[Path(__file__),Path('PROMPT.md'),D/'PROOF.md',D/'REVIEW_SUPPLEMENT.md'];j={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPLICIT_PDE_JET_SYMBOLIC_IDENTITIES','check_count':len(checks),'checks':checks,'sympy_version':S.__version__,'hashes':{str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths},'scope':'Exact polynomial identities in displayed jets, not a global PDE solution.'};(D/'verification/pde_checks.json').write_text(json.dumps(j,indent=2)+'\n');print(j['utc'],j['status'],len(checks))
