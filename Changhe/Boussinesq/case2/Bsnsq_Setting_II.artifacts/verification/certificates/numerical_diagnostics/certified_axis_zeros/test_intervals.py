"""Exact small manufactured tests of interval enclosure and rejection gates."""
import datetime,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path
from intervals import Arithmetic
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(14,15))
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.process_time();checks=[]
a=Arithmetic(96)
def contains(interval,value):return F(interval[0],a.B)<=value<=F(interval[1],a.B)
vals=[F(-8,3),F(-1),F(-2,7),F(0),F(1,11),F(1,2),F(5,3)]
for x in vals:
    ix=a.rational(x.numerator,x.denominator);assert contains(ix,x)
    if x:assert contains(a.inv(ix),1/x)
    for n in (0,1,2,3,8):assert contains(a.pow(ix,n),x**n)
    for y in vals:
        iy=a.rational(y.numerator,y.denominator)
        for name,z,w in [('add',a.add(ix,iy),x+y),('sub',a.sub(ix,iy),x-y),('mul',a.mul(ix,iy),x*y)]:
            assert contains(z,w);checks.append(name)
        if y:assert contains(a.div(ix,iy),x/y);checks.append('division_signs')
for lo,hi in [(F(-3),F(-1)),(F(1,3),F(7,2)),(F(-1),F(4))]:
    ia=(a.rational(lo.numerator,lo.denominator)[0],a.rational(hi.numerator,hi.denominator)[1])
    for x in [lo,(lo+hi)/2,hi]:
        for y in [lo,(lo+hi)/2,hi]:assert contains(a.mul(ia,ia),x*y)
    if lo*hi>0:
        ir=a.inv(ia)
        for x in [lo,(lo+hi)/2,hi]:assert contains(ir,1/x)
    checks.append('nondegenerate_interval_extrema')
for l,u in [(-1,1),(0,0),(0,5),(-5,0)]:
    try:a.inv((l,u))
    except ZeroDivisionError:checks.append('zero_reciprocal_rejected')
    else:raise AssertionError('zero accepted')
for x in [F(0),F(1,7),F(2),F(81,16)]:
    ix=a.rational(x.numerator,x.denominator);lo,hi=a.sqrt(ix)
    assert F(lo,a.B)**2<=x<=F(hi,a.B)**2;checks.append('integer_sqrt')
try:a.sqrt((-1,3))
except ValueError:checks.append('negative_sqrt_rejected')
else:raise AssertionError('negative sqrt accepted')
for t in [F(1,2),F(2,3),F(5,7),F(16,17)]:
    it=a.rational(t.numerator,t.denominator);bounds=a.log(it,25);v=(1-t)/(1+t)
    # Separate Fraction calculation with more terms yields a nested analytic
    # interval. It is not an external floating logarithm oracle.
    n=45;s=2*sum((v**(2*j+1)/F(2*j+1)for j in range(n)),F(0))
    tail=2*v**(2*n+1)/(F(2*n+1)*(1-v*v))
    assert contains(bounds,-s)and contains(bounds,-s-tail)
    checks.append('log_nested_fraction_remainder')
for bounds in [(0,a.B//2),(a.B//2,a.B),(a.B,a.B+1)]:
    try:a.log(bounds,5)
    except ValueError:checks.append('log_domain_rejected')
    else:raise AssertionError('invalid log accepted')
row={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(__file__),
     'arithmetic_sha256':sha(HERE/'intervals.py'),'proof_sha256':(sha(HERE/'PROOF.md') if (HERE/'PROOF.md').exists() else None),
     'checks':checks,'passed':len(checks),'cpu_seconds':time.process_time()-start,
     'scope':'Exact manufactured interval enclosure/rejection tests; analytic log soundness remains the written proof.'}
(HERE/'verification/manufactured.json').write_text(json.dumps(row,indent=2)+'\n')
print(json.dumps({k:v for k,v in row.items()if k!='checks'},indent=2))
