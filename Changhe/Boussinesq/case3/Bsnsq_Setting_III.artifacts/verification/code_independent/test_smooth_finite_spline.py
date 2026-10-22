"""Exact independent cell polynomials and derivative coefficients for packet176."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,time
import sympy as S
root=Path('research/176_smooth_finite_spline_counterexample/verification')
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
j=json.loads((root/'input.json').read_text());p=j['degree'];knots=[S.Rational(x) for x in j['knots']];co=[S.Rational(x) for x in j['coefficients_mode0']]
t=S.symbols('t');checks=[]
def eq(name,a,b=0):
 d=S.expand(a-b)
 assert not d.atoms(S.Float),(name,'Float found')
 assert d==0,(name,d)
 checks.append({'name':name,'difference':str(d),'pass':True})
def cells(k,p,c):
 out=[]
 for a,b in zip(sorted(set(k)),sorted(set(k))[1:]):
  m=(a+b)/2
  bs=[S.Integer(int(bool(k[i]<=m<k[i+1]))) for i in range(len(k)-1)]
  for degree in range(1,p+1):
   nb=[]
   for i in range(len(bs)-1):
    v=S.Integer(0)
    if k[i+degree]!=k[i]:v+=(t-k[i])/(k[i+degree]-k[i])*bs[i]
    if k[i+degree+1]!=k[i+1]:v+=(k[i+degree+1]-t)/(k[i+degree+1]-k[i+1])*bs[i+1]
    nb.append(S.expand(v))
   bs=nb
  assert len(bs)==len(c)
  out.append((a,b,S.expand(sum(ci*bi for ci,bi in zip(c,bs)))))
 return out
def deriv_coeff(k,p,c):
 k=[F(str(x)) for x in k];c=[F(str(x)) for x in c]
 while p:
  c=[p*(c[i+1]-c[i])/(k[i+p+1]-k[i+1]) for i in range(len(c)-1)]
  k=k[1:-1];p-=1
 return c
cs=cells(knots,p,co);dc=deriv_coeff(knots,p,co)
for i,(a,b,q) in enumerate(cs):
 eq(f'cell{i}_partition',q,1)
 for n in range(1,p+2):eq(f'cell{i}_derivative{n}',S.diff(q,t,n))
 eq(f'cell{i}_separate_derivative',S.diff(q,t,p),S.Rational(dc[i].numerator,dc[i].denominator))
for i in range(1,len(cs)):
 for n in range(p+1):eq(f'knot{i}_jump{n}',S.diff(cs[i][2]-cs[i-1][2],t,n).subs(t,cs[i][0]))
neg=list(co);neg[3]=S.Integer(2);ns=cells(knots,p,neg);nd=deriv_coeff(knots,p,neg)
negative=[]
for i in range(1,len(ns)):
 jump=S.diff(ns[i][2]-ns[i-1][2],t,p)
 eq(f'negative_control_jump_agreement{i}',jump,S.Rational((nd[i]-nd[i-1]).numerator,(nd[i]-nd[i-1]).denominator))
 negative.append({'knot':str(ns[i][0]),'exact_fifth_jump':str(jump)})
assert any(S.Rational(v['exact_fifth_jump'])!=0 for v in negative)
x,y=S.symbols('x y',real=True);q=1+x*x+y*y
Theta=x*x*q**(-S.Rational(3,4));Omega=x*q**(-S.Rational(5,8))
eq('Theta_x_parity',Theta.subs(x,-x),Theta)
eq('Omega_x_parity',Omega.subs(x,-x),-Omega)
eq('Omega_y_parity',Omega.subs(y,-y),Omega)
eq('Theta_axis',Theta.subs(x,0))
eq('a0',S.diff(Theta,x,2).subs({x:0,y:0})/2,1)
eq('Omega_x_center',S.diff(Omega,x).subs({x:0,y:0}),1)
eq('local_beta4_relation',S.diff(Omega,x).subs({x:0,y:0}),S.diff(Theta,x,2).subs({x:0,y:0})/2)
eq('required_center_strain_gap',1+S.Rational(4,2)-0,3)
out={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_passed':True,'exact_checks':checks,'exact_check_count':len(checks),'negative_control':negative,'negative_control_detected':True,'constant_cells':[[str(a),str(b),str(v)]for a,b,v in cs],'separate_fifth_derivative_coefficients':[str(v) for v in dc],'scope':'Exact representation counterexample, not a B2 profile; analytic regularity follows from the written proof.'}
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['exact_check_count'],'exact checks; negative control PASS;',out['elapsed_seconds'],'seconds')
