"""Small exact arithmetic audit of the Mellin counterexample, no numerics."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib

def add(*polys):
    d={}
    for p in polys:
        for k,v in p.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items()if v}
def scale(p,c):return {k:v*c for k,v in p.items()if v*c}
def mul(a,b):
    d={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():d[(i+k,j+l)]=d.get((i+k,j+l),F(0))+x*y
    return {k:v for k,v in d.items()if v}
one={(0,0):F(1)};eta={(1,0):F(1)};u={(0,1):F(1)};u2=mul(u,u)
P=scale(add(scale(eta,5),scale(one,-2)),F(1,14));Q=scale(eta,-F(1,44))
first=scale(mul(mul(add(mul(P,add(one,scale(u,-2))),scale(mul(Q,add(one,scale(u,-8),scale(u2,8))),2)),u),add(one,scale(mul(eta,u),-1))),-1)
second=scale(mul(mul(mul(u,add(one,scale(u,-1))),add(P,scale(mul(Q,add(one,scale(u,-2))),2))),add(one,scale(mul(eta,u),-3))),3)
integrand=add(first,second);coeff={}
for (i,j),v in integrand.items():coeff[i]=coeff.get(i,F(0))+2*v*F(math.comb(2*j,j),4**j)
expected={0:-F(880,4928),1:F(3344,4928),2:-F(2951,4928)}
checks=[]
def record(name,condition,**kw):
    checks.append(dict(name=name,passed=bool(condition),**kw));assert condition,name
record('independent_sin_power_integral',coeff==expected,coefficients={str(k):str(v)for k,v in coeff.items()})
# Q(sqrt(6)) represented by exact pairs. No approximate square root is used.
def qa(x,y):return(x[0]+y[0],x[1]+y[1])
def qm(x,y):return(x[0]*y[0]+6*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qs(x,c):return(x[0]*c,x[1]*c)
e=(F(0),F(1,6));a=(F(12),F(4));zero=(F(0),F(0))
record('eta_squared',qm(e,e)==(F(1,6),F(0)))
record('canonical_center_minus_one',qa(qs(a,-F(1,4)),qs(qm(a,e),F(1,2)))==(-F(1),F(0)))
record('cubic_endpoint',qa(qa(a,(-F(12),F(0))),qs(e,-24))==zero)
value=qa(qa((coeff[0],F(0)),qs(e,coeff[1])),qs(qm(e,e),coeff[2]))
record('special_exact_tail_residual',value==(-F(8231,29568),F(3344,29568)),coefficient=[str(v)for v in value])
margin=8231**2-6*3344**2
record('strict_negative_tail_residual',margin==655345 and margin>0,squared_margin=margin)
# First homogeneous inverse-moment relation at p=1/2, using the P2 mode.
Cu=scale(P,F(7,4));Ct=add(one,scale(eta,-F(3,4)));Ctx=add(scale(one,F(1,4)),scale(eta,-F(1,8)))
record('far_inverse_moment',add(scale(Cu,F(1,2)),scale(Ctx,-F(7,2)),Ct)=={})
for A in [F(3,2),F(3),F(10)]:
    for n in [3,5,7,11]:
        a0=(n-1)*(A-1)*F(2,3);m=2+a0/(2*(A-1))
        C=a0*m/(m-2)-2*m*(A-1);d=-a0/(2*(m-2))+A+3-2*m
        record('cancellation_'+str(A)+'_'+str(n),2<m<F(n+3,2) and C==0 and d==-a0/(A-1))
report=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,check_count=len(checks),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact polynomial and quadratic-field arithmetic only. Cutoffs, Mellin uniqueness and asymptotic error bounds are proved in the accompanying standalone argument.')
out=Path('research/mellin_transport_projection/verification/checks.json');out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
