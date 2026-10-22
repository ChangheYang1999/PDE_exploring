"""Manufactured controls for harmonic analytic extension and boundary parity."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,time,hashlib
r=Path('verification/analytic_transverse_trace_controls_20261021T1231Z');r.mkdir(exist_ok=True)
inputs={'polynomial_degrees':list(range(10)),'nonpolynomial_harmonics':['exp(v)*cos(u)','exp(v)*sin(u)','sin(v)*cosh(u)','cos(v)*sinh(u)','(1-v)/((1-v)^2+u^2)','atan(u/(1-v))'],'scope':'Exact manufactured identities, not proof by finite sampling.'}
(r/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n');start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();u,v=s.symbols('u v',real=True);z=s.symbols('z');tests=[]
def ck(name,e):
 d=s.simplify(e);tests.append({'name':name,'difference':str(d),'pass':d==0})
for n in inputs['polynomial_degrees']:
 a=z**n;A=s.expand(((v+s.I*u)**n+(v-s.I*u)**n)/2)
 ck('poly_trace_'+str(n),A.subs(u,0)-v**n);ck('poly_laplacian_'+str(n),s.diff(A,u,2)+s.diff(A,v,2));ck('poly_even_'+str(n),A.subs(u,-u)-A)
 B=s.expand(((v+s.I*u)**(n+1)-(v-s.I*u)**(n+1))/(2*s.I*(n+1)))
 ck('odd_harmonic_'+str(n),s.diff(B,u,2)+s.diff(B,v,2));ck('odd_value_'+str(n),B.subs(u,0));ck('odd_neumann_'+str(n),s.diff(B,u).subs(u,0)-v**n);ck('odd_reflection_'+str(n),B.subs(u,-u)+B)
known=[(s.exp(v)*s.cos(u),s.exp(v)),(s.exp(v)*s.sin(u),0),(s.sin(v)*s.cosh(u),s.sin(v)),(s.cos(v)*s.sinh(u),0),((1-v)/((1-v)**2+u*u),1/(1-v)),(s.atan(u/(1-v)),0)]
for i,(H,a) in enumerate(known):
 ck('nonpoly_harmonic_'+str(i),s.diff(H,u,2)+s.diff(H,v,2));ck('nonpoly_trace_'+str(i),H.subs(u,0)-a)
 # Zero-value part is odd in u for these manufactured scalar harmonics.
 Q=s.simplify((H-H.subs(u,-u))/2)
 ck('nonpoly_zero_value_'+str(i),Q.subs(u,0));ck('nonpoly_zero_second_normal_'+str(i),s.diff(Q,u,2).subs(u,0));ck('nonpoly_odd_reflection_'+str(i),Q.subs(u,-u)+Q)
# The missing second-normal match is supplied by harmonicity; these controls show why it is needed.
wrong=u**2*(1+v*v);assert s.diff(wrong,u,2).subs(u,0)!=0
not_harmonic=u**3*(1+v*v);ck('zero_second_normal_without_harmonicity',s.diff(not_harmonic,u,2).subs(u,0));assert s.simplify(s.diff(not_harmonic,u,2)+s.diff(not_harmonic,v,2))!=0
out={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs_sha256':hashlib.sha256((r/'inputs.json').read_bytes()).hexdigest(),'exact_checks':tests,'exact_count':len(tests),'negative_controls':2,'all_passed':all(t['pass'] for t in tests)}
(r/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='exact_checks'},indent=2));assert out['all_passed']
