from fractions import Fraction as Q
from pathlib import Path
from math import comb
import json,time,copy
import mpmath as mp
from higher_inverse_constant import evaluate,validate
start=time.monotonic();mp.mp.dps=80
out=[]
def fixture(b,c,knots):return {'source':'self','basis_beta':str(b),'beta':str(b),'L':'3/2','degree':5,'knots':[str(v)for v in knots],'coefficients':[str(v)for v in c]}
betas=[Q('2.3'),Q('2.99'),Q('3.005'),Q('3.3'),Q('3.9'),Q('4.3'),Q('5.9')]
for b in betas:
 for p in [[Q(int(j==k))for j in range(6)]for k in range(6)]+[[Q(v)for v in ['1/5','-3/10','7/10','-1/2','2/5','1/10']]]:
  c=[sum(p[j]*Q(comb(5-k,j),comb(5,j))for j in range(6-k))for k in range(6)]
  data=fixture(b,c,[0]*6+[1]*6);ans=evaluate(data);exact=-b*Q(9,4)/2*sum(p[j]/(j+1-b)for j in range(6));lo,hi=map(Q,ans['constant_C2']);assert lo<=exact<=hi
  out.append({'kind':'global_polynomial','beta':str(b),'p':[str(v)for v in p],'exact':str(exact),'interval':[str(lo),str(hi)]})
def m(v):
 v=Q(v);return mp.mpf(v.numerator)/v.denominator
def derivcoef(c,t,d,n):
 for _ in range(n):
  c=[d*(c[i+1]-c[i])/(t[i+d+1]-t[i+1])for i in range(len(c)-1)];t=t[1:-1];d-=1
 return c,t,d
def deboor(x,c,t,d):
 k=next((i for i in range(d,len(c))if t[i]<=x<t[i+1]),len(c)-1)
 val=[c[k-d+j]for j in range(d+1)]
 for r in range(1,d+1):
  for j in range(d,r-1,-1):
   i=k-d+j;a=(x-t[i])/(t[i+d-r+1]-t[i]);val[j]=(1-a)*val[j-1]+a*val[j]
 return val[d]
for b in betas:
 knots=[Q(0)]*6+[Q(1,3),Q(2,3)]+[Q(1)]*6;c=[Q((i*i+3*i)%11-5,7)for i in range(8)];data=fixture(b,c,knots);ans=evaluate(data);N=int(b);a=m(N+1-b);cm,tm,dd=derivcoef(list(map(m,c)),list(map(m,knots)),5,N)
 cuts=sorted({(1-m(v))**a for v in knots});integ=mp.quad(lambda u:deboor(1-u**(1/a),cm,tm,dd)/a,cuts)
 fp=m(ans['boundary'])+(-1)**N*integ/mp.fprod(m(b-j)for j in range(1,N+1));reference=-m(b)*mp.mpf('2.25')/2*fp
 lo,hi=map(m,ans['constant_C2']);assert lo<=reference<=hi,(b,lo,reference,hi)
 out.append({'kind':'piecewise_spline_deboor_MP','beta':str(b),'reference':str(reference),'interval':ans['constant_C2']})
invalid=0
for b in [Q(3),Q(4),Q(6)]:
 try:validate(fixture(b,[Q(0)]*6,[0]*6+[1]*6))
 except AssertionError:invalid+=1
assert invalid==3
root=Path('research/111_higher_inverse_constant_certificate/verification');(root/'manufactured_tests.json').write_text(json.dumps({'elapsed_seconds':time.monotonic()-start,'passed':True,'manufactured':out,'invalid_exponents_rejected':invalid},indent=2)+'\n');print('PASS',len(out),'manufactured',invalid,'invalid exponents',time.monotonic()-start)
