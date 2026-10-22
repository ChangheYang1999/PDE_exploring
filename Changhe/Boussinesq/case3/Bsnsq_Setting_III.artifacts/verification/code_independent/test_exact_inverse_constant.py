from fractions import Fraction as Q
from math import comb
from pathlib import Path
from datetime import datetime,timezone
import time,json
from exact_inverse_constant import powerbound,evaluate,validate
start=time.monotonic();tests=[]
def contained(q,ival):
 l,u=map(Q,ival);assert l<=q<=u,(q,l,u)
# Exact square roots and cube roots, including near-one and tiny arguments.
for a,powden in [(Q(1,2),2),(Q(1,3),3),(Q(2,3),3)]:
 for root in [Q(1,2),Q(2,3),Q(7,8),Q(999,1000),Q(1,10**12)]:
  value=root**(a*powden).numerator;bound=powerbound(root**powden,a);contained(value,bound);tests.append({'kind':'rational_power','a':str(a),'input':str(root**powden),'width':str(bound[1]-bound[0])})
# One-cell degree-five Bernstein coefficients for S(t)=(1-t)^j.
for b in [Q(21,10),Q(5,2),Q(29,10)]:
 for j in range(6):
  c=[Q(comb(5-k,j),comb(5,j)) if k<=5-j else Q(0) for k in range(6)]
  data={'source':'self','basis_beta':str(b),'beta':str(b),'L':'3/2','degree':5,'knots':['0']*6+['1']*6,'coefficients':list(map(str,c))}
  out=evaluate(data);exact=-b*Q(9,4)/(2*(j+1-b));contained(exact,out['constant_C2']);tests.append({'kind':'exact_moment','b':str(b),'j':j,'exact':str(exact),'sign':out['sign']})
# Exact zero and either sign with S=1+d(1-t)^2.
for b in [Q(9,4),Q(5,2),Q(11,4)]:
 d0=(3-b)/(b-1)
 for factor in [Q(0),Q(1),Q(2)]:
  d=factor*d0;co=[1+d*Q(comb(5-k,2),10) if k<=3 else Q(1) for k in range(6)]
  data={'source':'self','basis_beta':str(b),'beta':str(b),'L':'1','degree':5,'knots':['0']*6+['1']*6,'coefficients':list(map(str,co))}
  out=evaluate(data);exact=b/(2*(b-1))-d*b/(2*(3-b));contained(exact,out['constant_C2']);assert out['sign']==('OPEN' if factor==1 else 'POSITIVE' if factor==0 else 'NEGATIVE');tests.append({'kind':'zero_sign_control','b':str(b),'factor':str(factor)})
# Over-clamping and lack of C1 are rejected by the input validator.
bad=dict(data);bad['knots']=['0']*7+['1']*6;bad['coefficients']=['1']*7
try:validate(bad)
except AssertionError:pass
else:raise AssertionError('over-clamped input accepted')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','tests':tests,'count':len(tests)+1,'elapsed_seconds':time.monotonic()-start}
Path('research/104_exact_inverse_constant/verification/manufactured_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],result['elapsed_seconds'])
# Graded, multiple-cell splines representing the same global polynomials.
# Their cell integrals use genuinely nontrivial endpoint powers; the whole
# integral has the independent exact monomial value of packet93.
from itertools import combinations
for b in [Q(23,10),Q(5,2),Q(29,10)]:
 for j in [1,2,4,5]:
  knots=[Q(0)]*6+[Q(1,10**9),Q(1,64),Q(1,3),Q(9,10)]+[Q(1)]*6
  co=[sum((__import__('math').prod(vals) for vals in combinations([1-knots[i+l] for l in range(1,6)],j)),Q(0))/comb(5,j) for i in range(len(knots)-6)]
  data={'source':'self','basis_beta':str(b),'beta':str(b),'L':'3/2','degree':5,'knots':list(map(str,knots)),'coefficients':list(map(str,co))}
  out=evaluate(data);exact=-b*Q(9,4)/(2*(j+1-b));contained(exact,out['constant_C2']);tests.append({'kind':'graded_multicell_moment','b':str(b),'j':j,'exact':str(exact)})
result.update(tests=tests,count=len(tests)+1,elapsed_seconds=time.monotonic()-start)
Path('research/104_exact_inverse_constant/verification/manufactured_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],result['elapsed_seconds'])
