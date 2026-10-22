"""Independent exact controls for packet164; no NUM code or floating PDE solve."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
import sympy as S
r=Path(sys.argv[1]);r.mkdir(parents=True,exist_ok=True);now=datetime.now(timezone.utc).isoformat();start=time.monotonic()
u,v,t=S.symbols('u v t',real=True);up=S.symbols('u',positive=True);tests=[]
inputs={'divergence':'4','scalar_degrees':list(range(9)),'vector_orders':[1,2,3,5,8],'flat_powers':[1,2,3],'coefficient_rule':'a_j(0)=(-1)^j/(j+2); a_j_prime(0)=(j+1)/(2*j+3)','scope':'Exact manufactured checks of finite recurrence and flat failures, not PDE candidates.'}
(r/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
def add(name,expr):
 z=S.expand(expr);ok=z==0 or S.simplify(z)==0;tests.append({'name':name,'difference':str(z) if not ok else '0','pass':bool(ok)})
def twice(poly):
 return S.integrate(S.integrate(poly,(u,0,t)),(t,0,u))
polys=[]
for N in inputs['scalar_degrees']:
 a=[S.Integer(0)]*(N+3)
 for j in reversed(range(N+1)):
  a[j]=S.Rational((-1)**j,j+2)+u*S.Rational(j+1,2*j+3)-twice((j+2)*(j+1)*a[j+2])
  add(f'N{N}_recurrence{j}',S.diff(a[j],u,2)+(j+2)*(j+1)*a[j+2])
  add(f'N{N}_trace{j}',a[j].subs(u,0)-S.Rational((-1)**j,j+2))
  add(f'N{N}_normal_trace{j}',S.diff(a[j],u).subs(u,0)-S.Rational(j+1,2*j+3))
 p=S.expand(sum(a[j]*v**j for j in range(N+1)));add(f'N{N}_harmonic',S.diff(p,u,2)+S.diff(p,v,2));tests.append({'name':f'N{N}_total_degree','value':int(S.Poly(p,u,v).total_degree()),'bound':N+1,'pass':S.Poly(p,u,v).total_degree()<=N+1});polys.append({'N':N,'polynomial':str(p)})
for N in inputs['vector_orders']:
 z=S.expand((u+S.I*v)**(N+1));H=S.re(z)+S.Rational(2,3)*S.im(z);phi=2*v*v+H
 wu=S.diff(phi,u);wv=S.diff(phi,v);curl=S.diff(wv,u)-S.diff(wu,v);div=S.diff(wu,u)+S.diff(wv,v)
 add(f'vector{N}_div',div-4);add(f'vector{N}_curl',curl);add(f'vector{N}_lap_u',S.diff(wu,u,2)+S.diff(wu,v,2));add(f'vector{N}_lap_v',S.diff(wv,u,2)+S.diff(wv,v,2))
 # Exact finite recurrence reconstruction from the actual coefficients at u=0.
 for label,w in [('u',wu),('v',wv)]:
  coeff=[S.expand(w).coeff(v,j) for j in range(N+1)];rec=[S.Integer(0)]*(N+3)
  for j in reversed(range(N+1)):
   rec[j]=coeff[j].subs(u,0)+u*S.diff(coeff[j],u).subs(u,0)-twice((j+2)*(j+1)*rec[j+2])
  add(f'vector{N}_{label}_reconstruct',sum(rec[j]*v**j for j in range(N+1))-w)
for p in inputs['flat_powers']:
 f=S.exp(-1/up**p);w1=f;w2=(4-S.diff(f,up))*v;omega=S.diff(f,up,2)*v
 add(f'flat{p}_div',S.diff(w1,up)+S.diff(w2,v)-4)
 add(f'flat{p}_omega',S.diff(w1,v)-S.diff(w2,up)-omega)
 residual=w1*S.diff(omega,up)+w2*S.diff(omega,v)+omega
 add(f'flat{p}_residual_identity',residual-(f*S.diff(f,up,3)+(5-S.diff(f,up))*S.diff(f,up,2))*v)
 # At u=1/(p+3), v=1 the polynomial coefficient of Omega is explicitly nonzero.
 val=S.simplify(S.diff(f,up,2).subs(up,S.Rational(1,p+3)))
 tests.append({'name':f'flat{p}_nonzero_vorticity_coefficient','value':str(val),'pass':bool(val.is_positive)})
# One-sided flat coefficients do NOT imply analytic continuation: the full-neighborhood
# polynomial-in-v hypothesis is compatible with nonharmonic flat changes on the left,
# so the proof must use the nullcline contradiction, not W=P on the negative side.
D,b=S.symbols('D b',real=True);W1=b*u;W2=(D-b)*v
add('diagonal_control_div',S.diff(W1,u)+S.diff(W2,v)-D);add('diagonal_control_curl',S.diff(W2,u)-S.diff(W1,v))
d={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs_sha256':hashlib.sha256((r/'inputs.json').read_bytes()).hexdigest(),'control_count':len(tests),'all_passed':all(x['pass'] for x in tests),'tests':tests,'scalar_examples':polys,'scope':'Exact symbolic/rational manufactured controls only.'};(r/'results.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k not in ['tests','scalar_examples']},indent=2));assert d['all_passed']
