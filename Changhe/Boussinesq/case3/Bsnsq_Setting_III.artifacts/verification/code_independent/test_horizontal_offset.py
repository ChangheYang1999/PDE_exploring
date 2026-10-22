"""Controls for136, separate direct quadrature and exact symbolic checks."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time
import sympy as sp
import mpmath as mp
from horizontal_offset_certificate import offset_certificate,mp_offset,mp_primitive,source_from_state,whole_offset_certificate

root=Path(sys.argv[1]);root.mkdir(exist_ok=True);start=time.perf_counter();checks=[]
x,y=sp.symbols('x y',real=True);A=1+y*y
for k,q in [(0,Q(-3,4)),(1,Q(-7,4)),(2,Q(-13,4)),(3,Q(-9,2)),(0,Q(-1)),(2,Q(-3))]:
 expr=0
 for ell in range(k+1):
  p=q+ell+1;p=sp.Rational(p.numerator,p.denominator)
  value=((A+x*x)**p-A**p)/p if p else sp.log((A+x*x)/A)
  expr+=sp.binomial(k,ell)*(-A)**(k-ell)*value/2
 assert sp.simplify(sp.diff(expr,x)-x**(2*k+1)*(A+x*x)**sp.Rational(q.numerator,q.denominator))==0
 checks.append({'symbolic_primitive':[k,str(q)],'passed':True})
# Smooth angular primitive, exactly zero offset, including noninteger beta.
for beta in [Q(9,4),Q(11,4),Q(7,2),Q(1702278897357859,562949953421312)]:
 m=1-2/beta;rows=[(Q(2),0,0,(m-2)/2),(m-2,1,0,(m-4)/2)];c=offset_certificate(rows)
 assert c['verdict']=='CONFIRMED_H1_ZERO_ONLY';checks.append({'zero_offset_beta':str(beta),'root_degree':c['root_degree'],'passed':True})
# Exact compact/algebraic offsets, a logarithmic resonance, and a mixed OPEN case.
for rows,want,expected in [([(Q(1),0,0,Q(-2))],'REFUTED_TRANSVERSE_GRADIENT','-0.25'), ([(Q(1),0,1,Q(-2))],'REFUTED_TRANSVERSE_GRADIENT','0.25'), ([(Q(1),0,0,Q(-1))],'REFUTED_TRANSVERSE_GRADIENT',None), ([(Q(1),0,0,Q(-1)),(Q(1),0,0,Q(-2))],'OPEN_MIXED_LOG_ALGEBRAIC',None)]:
 c=offset_certificate(rows);assert c['verdict']==want
 if expected:assert abs(mp.mpf(mp_offset(rows,1))-mp.mpf(expected))<mp.mpf('1e-50')
 checks.append({'manufactured_offset':c,'value':mp_offset(rows,1),'passed':True})
# Independent direct physical integral, not the finite-part formula.
mp.mp.dps=60
for rows in [[(Q(1),0,0,Q(-3,4))],[(Q(3,7),2,1,Q(-13,4))],[(Q(2),1,2,Q(-11,4))],[(Q(1),2,0,Q(-3))]]:
 def source(xx,yy):
  return mp.fsum(mp.mpf(c.numerator)/c.denominator*xx**(2*k+1)*yy**b*(1+xx*xx+yy*yy)**(mp.mpf(q.numerator)/q.denominator)for c,k,b,q in rows)
 point=mp.mpf('0.7');got=mp.quad(lambda xx:source(xx,point)-source(xx,0),[0,1,4,16,mp.inf]);want=mp.mpf(mp_offset(rows,point,75));err=abs(got-want)
 assert err<mp.mpf('1e-27')
 primitive_errors=[]
 for xx in ['0.0003','0.7','13.7']:
  integ=mp.quad(lambda u:source(u,point),[0,mp.mpf(xx)]);val=mp.mpf(mp_primitive(rows,xx,point,75));errp=abs(integ-val);assert errp<mp.mpf('1e-45');primitive_errors.append(str(errp))
 checks.append({'direct_offset_error':str(err),'primitive_errors':primitive_errors,'passed':True})
# The full function detects a defect missed exactly at y=1.
rows=[(Q(2),0,3,Q(-3)),(Q(-2),0,1,Q(-3))]
point=offset_certificate(rows);whole=whole_offset_certificate(rows)
assert point['verdict']=='CONFIRMED_H1_ZERO_ONLY'
assert whole['odd_power_coefficients']=={'-2':'-1','-1':'1/2'}
assert whole['verdict']=='REFUTED_TRANSVERSE_GRADIENT'
assert abs(mp.mpf(mp_offset(rows,2))-mp.mpf('0.12'))<mp.mpf('1e-55')
checks.append({'full_function_missed_by_H1':whole,'passed':True})
rows=[(Q(1),0,0,Q(-1)),(Q(1),0,0,Q(-2))]
assert offset_certificate(rows)['verdict']=='OPEN_MIXED_LOG_ALGEBRAIC'
assert whole_offset_certificate(rows)['verdict']=='REFUTED_TRANSVERSE_GRADIENT'
for beta in [Q(9,4),Q(11,4),Q(7,2)]:
 m=1-2/beta;rows=[(Q(2),0,0,(m-2)/2),(m-2,1,0,(m-4)/2)]
 assert whole_offset_certificate(rows)['verdict']=='CONFIRMED_WHOLE_OFFSET_ZERO_ONLY'
checks.append({'full_function_zero_and_mixed_log_cases':True,'passed':True})
# Own exact source decoder versus a separately expanded Cartesian rational stream.
beta=Q(9,4);state={'beta':str(beta),'labels':[[0,0,0],[0,1,0]],'C':['2/3','-4/5'],'extra_stream_terms':[{'x_power':3,'y_power':1,'R_power':'-8','coefficient':'5/7'}]}
rows=source_from_state(state);s=sp.Rational(4,9);psi=sp.Rational(2,3)*x*(1+x*x+y*y)**((1-s)/2)-sp.Rational(4,5)*x*y*(1+x*x+y*y)**(-s/2)+sp.Rational(5,7)*x**3*y*(1+x*x+y*y)**-4
om=-sp.diff(psi,x,2)-sp.diff(psi,y,2);vx=-sp.diff(psi,y);vy=sp.diff(psi,x);w1=sp.Rational(9,4)*x+vx-vx.subs({x:0,y:0});w2=sp.Rational(9,4)*y+vy-vy.subs({x:0,y:0});source=w1*sp.diff(om,x)+w2*sp.diff(om,y)+om
for xx,yy in [(Q(1,3),Q(2,5)),(Q(2),Q(-1,2))]:
 ref=source.subs({x:sp.Rational(xx.numerator,xx.denominator),y:sp.Rational(yy.numerator,yy.denominator)}).evalf(60)
 xmp=mp.mpf(xx.numerator)/xx.denominator;ymp=mp.mpf(yy.numerator)/yy.denominator
 got=mp.fsum(mp.mpf(c.numerator)/c.denominator*xmp**(2*k+1)*ymp**b*(1+xmp*xmp+ymp*ymp)**(mp.mpf(q.numerator)/q.denominator)for c,k,b,q in rows)
 error=abs(got-mp.mpf(str(ref)));assert error<mp.mpf('1e-45');checks.append({'independent_cartesian_source_error':str(error),'passed':True})
result={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'checks':checks};(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['elapsed_seconds'],flush=True)
