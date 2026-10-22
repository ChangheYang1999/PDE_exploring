"""Exact diagnostics and fresh dependency pin checks for topic100.
The complete analytical proof is in PROOF.md and mandatory ADDENDUM.md.
No numerical enclosure, infinite dimensional assertion, or density theorem
is certified by these finite algebraic diagnostics alone.
"""
import hashlib,json,itertools,sys
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/rough_source_extension'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
counts={};files={}
def identity(a,b=0):
 assert S.cancel(a-b)==0,(a,b)
 counts['exact_symbolic_identities']=counts.get('exact_symbolic_identities',0)+1
A,mu,g,s,C,Mv,Mr,delta=S.symbols('A mu g s C Mv Mr delta',real=True)
k=S.Rational(1301,200)-S.Rational(101,100)*s
slow=1+A/2+(S.Rational(1,2)-s)*mu
fast=1+(S.Rational(1,2)-s)*A+mu/2+g
identity(slow.subs({A:10,mu:S.Rational(101,100)}),k)
identity(fast.subs({A:S.Rational(51,5),mu:S.Rational(99,100),g:29}),S.Rational(7119,200)-S.Rational(51,5)*s)
identity((fast.subs({A:S.Rational(51,5),mu:S.Rational(99,100),g:29})-k).subs(s,S.Rational(31,10)),S.Rational(601,1000))
minimum_slow=None;minimum_d=None;vertices=0
for av,mv,gv,sv in itertools.product([S.Integer(10),S.Rational(51,5)],[S.Rational(99,100),S.Rational(101,100)],[S.Integer(29),S.Integer(30)],[S.Rational(61,20),S.Rational(31,10)]):
 vals={A:av,mu:mv,g:gv,s:sv};kk=k.subs(s,sv)
 assert slow.subs(vals)>=kk and fast.subs(vals)>kk
 d=1+(av+mv)/2-kk;assert d>=S.Rational(6141,2000)
 minimum_d=d if minimum_d is None else min(minimum_d,d)
 minimum_slow=slow.subs(vals)-kk if minimum_slow is None else min(minimum_slow,slow.subs(vals)-kk)
 vertices+=1
assert minimum_d==S.Rational(6141,2000) and minimum_slow==0
counts['affine_box_order_vertices']=vertices
Cv=S.Rational(9,4)*C+s*(3+S.Rational(9,2)*C)
identity(Cv,3*s+S.Rational(9,2)*(s+S.Rational(1,2))*C)
identity(Cv.subs(C,2),12*s+S.Rational(9,2))
a=k-delta*((12*s+S.Rational(9,2))*Mv+3*Mr)
identity(a.subs(s,S.Rational(153,50))-a.subs(s,S.Rational(31,10)),S.Rational(101,2500)+S.Rational(12,25)*delta*Mv)
# Radial Fourier integrals after u=|xi|^2, z=1+u.
identity(1/(s-3)-2/(s-2)+1/(s-1),2/((s-1)*(s-2)*(s-3)))
identity(1/(s-2)-1/(s-1),1/((s-1)*(s-2)))
x,y,ell,e,m1,m2,m3=S.symbols('x y ell e m1 m2 m3',real=True)
r2=x*x+y*y;u1=x*y/r2;u2=-x*x/r2
identity(x*u1+y*u2)
identity(u1*u1+u2*u2,x*x/r2)
identity(1-u1*u1-u2*u2,y*y/r2)
identity(x**4+2*x*x*y*y+y**4,r2*r2)
identity(u1.subs({x:ell*x,y:ell*y},simultaneous=True),u1)
identity(u2.subs({x:ell*x,y:ell*y},simultaneous=True),u2)
# Convolution of y^3 with any even probability kernel, in its moment algebra.
poly=S.Poly((y-e*S.Symbol('z'))**3,S.Symbol('z'))
moments={0:1,1:m1,2:m2,3:m3}
conv=sum(c*moments[power[0]] for power,c in poly.terms())
identity(conv.subs({m1:0,m3:0}),y**3+3*e*e*m2*y)
identity(S.diff(conv.subs({m1:0,m3:0}),y).subs(y,0),3*e*e*m2)
# Angular |sin| integral =4; radial exponents explain N_2 divergence.
th=S.symbols('th',real=True)
identity(4*S.integrate(S.sin(th),(th,0,S.pi/2)),4)
identity(1-3+1,-1)
# pi-free coefficients in the full remote norm bound.
R=S.symbols('R',positive=True)
identity((S.Rational(5,2)*delta)**-2,S.Rational(4,25)/delta**2)
identity(S.integrate(S.Symbol('r',positive=True)**-5,(S.Symbol('r',positive=True),R,S.oo)),1/(4*R**4))
identity(S.integrate(S.Integer(1),(S.Symbol('r'),0,R)),R)
# Current whole bundle validation is separate in finalizer. These pins cover
# all files in the six directly imported frozen verdict manifests.
deps=['source_local_estimate','source_semigroup','canonical_strain_sign','source_order_family','moving_source','source_dilation']
checks=0;dep_records={}
for name in deps:
 p=B/'research'/name/'evidence/verdict.json';v=json.loads(p.read_text())
 assert v['status'].startswith('CONFIRMED'),(name,v['status'])
 files[str(p.relative_to(B))]=sha(p);n=0
 for f,h in v['files'].items():
  assert sha(B/f)==h,f;checks+=1;n+=1
 dep_records[name]={'verdict_sha256':sha(p),'status':v['status'],'current_file_hash_comparisons':n}
counts['dependency_current_hash_comparisons']=checks
for rel in ['PROOF.md','ADDENDUM.md','code/check_algebra.py','evidence/proof_first.json','source/lead_r3.md','source/lead_r5.md','evidence/source_snapshot.json','evidence/source_r5_snapshot.json']:
 p=D/rel;files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_DIAGNOSTICS_AND_CURRENT_DEPENDENCIES','counts':counts,'exact_values':{'minimum_d':str(minimum_d),'fast_minus_slow_min':'601/1000','origin_mollifier_linear_coefficient':'3 epsilon^2 m2','near_origin_N2_radial_power':-1},'dependencies':dep_records,'scope':'Finite exact checks support, and do not replace, the standalone universal argument; no new interval enclosure or global inverse.','files':files}
(D/'evidence/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','status','counts','exact_values']},indent=2))
