"""Independent direct SymPy expansion for the131 polynomial certificate."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,time
import sympy as sp
from primitive_center_certificate import residual_from_jet
from exact_bivariate import ordinary_stream_jet

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
tic=time.perf_counter();x,y,t=sp.symbols('x y t');rows=[]
for beta in [Q(5,2),Q(4)]:
 c=1+beta/2;q=4/beta;psi={(1,1):c,(3,0):-q/6,(1,0):Q(3,7)}
 r=residual_from_jet(beta,psi);assert not r['R_Theta']and r['a0']==1
 psi[(1,3)]=Q(1,17);r=residual_from_jet(beta,psi);assert r['R_Theta']
 rows.append({'beta':str(beta),'polynomial_control':True,'nonprofile_detected':True})
for beta in [Q(9,4),Q(7,2)]:
 labels=[(0,0,0),(0,1,0),(2,2,0),(1,3,1)];C=[Q(-4,3),Q(7,3),Q(1,17),Q(-3,19)]
 psi,_=ordinary_stream_jet(beta,labels,C,[Q(0)]*len(C),8);a=residual_from_jet(beta,psi)
 R=sp.sqrt(1+x*x+y*y);expr=sum(sp.Rational(cc)*x*R**sp.Rational(1-1/beta-d)*sp.chebyshevt(i,2*R**sp.Rational(-1/beta)-1)*sp.chebyshevt(j,y/R)for(i,j,d),cc in zip(labels,C))
 # Independent symbolic generalized Taylor expansion directly from the basis expression.
 jet=sp.expand(sp.series(expr.subs({x:t*x,y:t*y}),t,0,7).removeO().subs(t,1));jet-=sp.diff(jet,x).subs({x:0,y:0})*x
 om=-sp.diff(jet,x,2)-sp.diff(jet,y,2);w1=sp.Rational(beta)*x-sp.diff(jet,y);w2=sp.Rational(beta)*y+sp.diff(jet,x)
 F=sp.expand(w1*sp.diff(om,x)+w2*sp.diff(om,y)+om);th=sp.integrate(F,(x,0,x))
 rt=sp.Poly(sp.expand(w1*sp.diff(th,x)+w2*sp.diff(th,y)-(sp.Rational(beta)-2)*th),x,y)
 exact={ij:Q(v)for ij,v in rt.terms()if sum(ij)<=4 and v};assert exact==a['R_Theta']
 rows.append({'beta':str(beta),'direct_symbolic_coefficients_equal':True,'nonzero_count':len(exact)})
r={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'checks':rows};(root/'tests.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],r['elapsed_seconds'],flush=True)
