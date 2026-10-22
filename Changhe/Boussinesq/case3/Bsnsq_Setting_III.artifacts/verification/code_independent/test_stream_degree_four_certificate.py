"""Independent SymPy controls for direct degree-four/three Taylor certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,time
import sympy as S
import exact_bivariate as P
from stream_degree_four_certificate import checks
from stream_local_jet_certificate import parse

out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);t0=time.perf_counter()
x,y,t=S.symbols('x y t');rows=[]
# Exact polynomial B2 solution, solely a local algebra control.
for b,a in [(Q(5,2),Q(1)),(Q(4),Q(3,2))]:
 psi={(1,1):1+b/2,(3,0):-4*a/b/6};theta={(2,0):a}
 rt,ro=P.pde(b,psi,theta,6);assert not rt and not ro
 rows.append({'polynomial_beta':str(b),'exact_PDE_zero':True})

def sympy_reference(data):
 b,labels,C,D=parse(data);b=S.Rational(b.numerator,b.denominator);r=S.sqrt(1+t*t*(x*x+y*y));u=2*r**(-1/b)-1;z=t*y/r
 ps=th=0
 for (i,j,d),c,a in zip(labels,C,D):
  c=S.Rational(c.numerator,c.denominator);a=S.Rational(a.numerator,a.denominator)
  uv=S.chebyshevt(i,u)*S.chebyshevt(j,z)
  if c:ps+=c*t*x*r**(1-1/b-d)*uv
  if a:th+=a*t*t*x*x*r**(-1-2/b-d)*uv
 ps=S.expand(S.series(ps,t,0,7).removeO().subs(t,1));th=S.expand(S.series(th,t,0,6).removeO().subs(t,1))
 ps-=x*S.diff(ps,x).subs({x:0,y:0})
 om=-S.diff(ps,x,2)-S.diff(ps,y,2);w1=b*x-S.diff(ps,y);w2=b*y+S.diff(ps,x)
 rt=S.expand(w1*S.diff(th,x)+w2*S.diff(th,y)-(b-2)*th)
 ro=S.expand(w1*S.diff(om,x)+w2*S.diff(om,y)+om-S.diff(th,x))
 def trim(f,n):return {(i,j):Q(int(v.p),int(v.q))for (i,j),v in S.Poly(f,x,y).terms()if i+j<=n and v}
 return P.serialize(trim(rt,4)),P.serialize(trim(ro,3))

labels=[[0,0,0],[0,1,0],[1,2,0],[2,3,1]]
for beta in ['5/2','7/2']:
 data={'beta':beta,'labels':labels,'C':['-2/3','9/4','2/17','-3/29'],'D':['1','1/7','-3/11','2/13']}
 a=checks(data);rt,ro=sympy_reference(data)
 assert a['R_Theta_through_degree4']==rt and a['R_Omega_through_degree3']==ro
 rows.append({'beta':beta,'SymPy_direct_definition_agrees':True,'nonzero':a['nonzero']})
result={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-t0,'checks':rows}
(out/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
