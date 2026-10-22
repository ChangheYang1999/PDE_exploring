"""P245 exact transport manufacture, separately generated symbolic coefficients."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,time,hashlib
R=Path('research/245_alias_transport_manufacture/verification');tick=time.monotonic();utc=lambda:datetime.now(timezone.utc).isoformat();o={'started_utc':utc(),'checks':[]}
def ck(n,v,**d):o['checks'].append({'name':n,'pass':bool(v),**d})
x,y,z=s.symbols('x y z',real=True);P=s.expand(s.re((-z+s.I)**12));D=s.expand(x*x*s.re((-y+s.I*x)**12));F=s.diff(D,x)
W=lambda p:s.expand(x*s.diff(p,x)/2+11*y*s.diff(p,y)/2+p)
O=s.S.Zero;data=[]
for (m,n),c in s.Poly(F,x,y).terms():
 lam=1+s.Rational(m,2)+s.Rational(11*n,2);ck('positive monomial eigenvalue '+str((m,n)),lam>0)
 O+=c/lam*x**m*y**n;data.append({'x_power':m,'y_power':n,'coefficient':str(c/lam),'forcing_coefficient':str(c),'eigenvalue':str(lam)})
Q=s.expand(O.subs({x:1,y:z}));R1=s.Poly(P,z)
ck('P binomial formula',s.expand(P-sum(s.binomial(12,n)*(-1)**(n//2)*z**n for n in range(0,13,2)))==0)
ck('degree14 temperature',s.Poly(D,x,y).total_degree()==14)
ck('degree13 vorticity',s.Poly(O,x,y).total_degree()==13)
ck('temperature even x',s.expand(D.subs(x,-x)-D)==0)
ck('vorticity odd x',s.expand(O.subs(x,-x)+O)==0)
ck('temperature zero on axis',D.subs(x,0)==0)
ck('manufactured response exact PDE',s.expand(W(O)-F)==0)
ck('baseline vorticity exact PDE',s.expand(W(s.Rational(4,3)*x)-2*x)==0)
ck('temperature polynomial equals ray expression',s.expand(D-x**14*P.subs(z,y/x))==0)
ck('Q independent coefficient formula',s.expand(Q-sum((14-n)*s.binomial(12,n)*(-1)**(n//2)*z**n/(s.Rational(15,2)+5*n)for n in range(0,13,2)))==0)
ck('constant ratios distinct',Q.subs(z,0)/P.subs(z,0)==s.Rational(28,15))
ck('leading ratio',s.LC(s.Poly(Q,z))/s.LC(s.Poly(P,z))==s.Rational(4,135))
ck('Q nonzero modulo P',s.rem(Q,P,z)!=0)
g=s.gcd(s.Poly(P,z),s.Poly(s.diff(P,z),z));ck('P simple roots algebraic check',g.degree()==0)
# In fact this computes whether any sampled ray has a zero response, stronger than needed.
g2=s.gcd(s.Poly(P,z),s.Poly(Q,z));ck('P and Q have no shared root',g2.degree()==0)
ck('extra temperature does not solve thermal PDE',s.expand(W(D)-2*D)!=0)
coeff=lambda p:[[int(m[0]),str(c)]for m,c in s.Poly(p,z).terms()]
(R/'exact_coefficients.json').write_text(json.dumps({'P':coeff(P),'Q':coeff(Q),'Omega_monomials':data,'P_Q_gcd':str(g2.as_expr()),'P_Pprime_gcd':str(g.as_expr())},indent=2)+'\n')
o.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['pass']for c in o['checks']),total=len(o['checks']),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'checks.json').write_text(json.dumps(o,indent=2)+'\n');print({k:v for k,v in o.items()if k!='checks'});print('failures',[c for c in o['checks']if not c['pass']]);assert o['passed']==o['total']
