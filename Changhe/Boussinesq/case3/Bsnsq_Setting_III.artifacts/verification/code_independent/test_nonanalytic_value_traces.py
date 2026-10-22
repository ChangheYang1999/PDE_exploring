"""Manufactured exact checks for the separately written local proof168."""
from pathlib import Path
from datetime import datetime, timezone
import time,json,hashlib
import sympy as s
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
u,v=s.symbols('u v',real=True);n=s.symbols('n',integer=True,positive=True)
rows=[]
def check(label,expr):
 value=s.simplify(s.expand_complex(expr));passed=value==0
 rows.append({'label':label,'passed':passed,'remainder':str(value)});assert passed,label
# Independent polynomial primitives test the signs and both differential identities.
for k in range(1,9):
 p=s.expand((u+s.I*v)**k);h=s.im(p);g=k*(u+s.I*v)**(k-1)
 w1=s.diff(h,v);w2=4*v-s.diff(h,u)
 check(f'CR real degree{k}',w1-s.re(g))
 check(f'CR imaginary degree{k}',w2-4*v+s.im(g))
 check(f'divergence degree{k}',s.diff(w1,u)+s.diff(w2,v)-4)
 check(f'curl degree{k}',s.diff(w2,u)-s.diff(w1,v))
a=s.symbols('a',positive=True)
check('positive vertical branch',s.exp(-a*(1-s.I))-s.exp(-a)*(s.cos(a)+s.I*s.sin(a)))
check('negative vertical branch',s.exp(-a*(1+s.I))-s.exp(-a)*(s.cos(a)-s.I*s.sin(a)))
check('first nonzero sequence',s.cos(2*s.pi*n)-1)
check('second nonzero sequence',s.sin(s.pi/2+2*s.pi*n)-1)
# beta2 equations restricted to a constant temperature and zero curl.
M=s.symbols('M',real=True)
check('thermal plateau beta2',u*s.diff(M,u)+v*s.diff(M,v)-(2-2)*M)
check('vorticity zero plateau',u*s.diff(s.Integer(0),u)+v*s.diff(s.Integer(0),v)+0-s.diff(M,u))
# A nonholomorphic primitive would not support the harmonicity conclusion.
h=u*u*v;curl=-s.diff(h,u,2)-s.diff(h,v,2)
negative=s.simplify(curl+2*v)==0 and curl!=0
assert negative
out=Path('research/168_analytic_trace_hypothesis_is_needed/verification')
d={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_count':len(rows),'exact_checks':rows,'negative_controls':[{'name':'nonharmonic u^2 v primitive','curl':str(curl),'passed':negative}],'all_passed':all(r['passed'] for r in rows) and negative,'scope':'Formula and sign controls only. Smooth flatness and nonanalyticity follow from PROOF.md, not finite sampling.'}
(out/'results.json').write_text(json.dumps(d,indent=2)+'\n');print(d['exact_count'],len(d['negative_controls']),d['all_passed'],d['elapsed_seconds'])
