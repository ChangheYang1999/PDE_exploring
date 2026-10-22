"""Supplemental exact check of the explicit conformal Neumann corrector in177."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,sympy as s
root=Path('research/177_incoming_endpoint_isothermal_side/verification')
a,b,c=s.symbols('a b c',real=True);start=time.monotonic();rows=[]
def check(name,expr):
 value=s.expand(expr);ok=value==0;rows.append({'name':name,'difference':str(value),'pass':ok});assert ok,(name,value)
def lap(expr):return s.diff(expr,a,2)+s.diff(expr,b,2)
F1=a-2*c*a*b;F2=b+c*(a*a-b*b);P=F1**2+F2**2
h=-2*c*a*a*b+s.Rational(2,3)*c*b**3;P0=P-h
check('conformal_CR1',s.diff(F1,a)-s.diff(F2,b));check('conformal_CR2',s.diff(F1,b)+s.diff(F2,a))
check('particular_source',lap(P)-4*((1-2*c*b)**2+4*c*c*a*a))
check('normal_trace_g',s.diff(P,b).subs(b,0)+2*c*a*a)
check('harmonic_corrector',lap(h));check('matched_normal_trace',s.diff(P-h,b).subs(b,0))
check('unchanged_source',lap(P0)-lap(P));check('regular_parametrization_at_origin',s.diff(F1,a).subs({a:0,b:0})-1)
# Zero-Neumann harmonic even reflection example, and zero-value odd example.
check('even_harmonic',lap(a**4-6*a*a*b*b+b**4));check('even_zero_normal',s.diff(a**4-6*a*a*b*b+b**4,b).subs(b,0))
check('odd_harmonic',lap(3*a*a*b-b**3));check('odd_zero_value',(3*a*a*b-b**3).subs(b,0))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':rows,'passed':len(rows),'status':'PASS'}
(root/'reflection_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
