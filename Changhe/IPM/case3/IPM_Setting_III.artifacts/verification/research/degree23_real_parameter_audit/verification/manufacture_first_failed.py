"""Exact manufactured tests, with no candidate data loaded."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from rational_node_intervals import *
from exact_degree21 import C,x,y,h,Q
R=Path('research/degree23_real_parameter_audit');V=R/'verification'
checks=[]
def ck(name,b):
 checks.append(dict(name=name,passed=bool(b)))
 if not b:raise AssertionError(name)
def reject(name,fn,kind):
 try:fn()
 except kind:ck(name,True)
 else:ck(name,False)
reject('reversed real interval',lambda:Interval(2,1),ValueError)
reject('zero crossing reciprocal',lambda:Interval(-1,2).inverse(),ZeroDivisionError)
reject('zero endpoint reciprocal',lambda:Interval(0,2).inverse(),ZeroDivisionError)
for a in [Interval(-3,-1),Interval(-2,4),Interval(1,3),Interval(0)]:
 for b in [Interval(-4,-2),Interval(-1,5),Interval(2,6)]:
  for name,operation,truth in [('add',lambda:a+b,lambda:u+v),('subtract',lambda:a-b,lambda:u-v),('multiply',lambda:a*b,lambda:u*v)]:
   val=operation();ck(name+' endpoint inclusion '+str(a.saved())+str(b.saved()),all(val.contains(truth())for u in [a.lo,a.hi]for v in [b.lo,b.hi]))
  if not b.contains(0):ck('division endpoint inclusion '+str(a.saved())+str(b.saved()),all((a/b).contains(u/v)for u in [a.lo,a.hi]for v in [b.lo,b.hi]))
 for k in [0,1,2,3,7]:ck('power '+str(a.saved())+' '+str(k),all((a**k).contains(v**k)for v in [a.lo,(a.lo+a.hi)/2,a.hi]))
 ck('absolute bounds '+str(a.saved()),all(a.lower()<=abs(v)<=a.upper()for v in [a.lo,(a.lo+a.hi)/2,a.hi]))
ck('negative inverse exact',Interval(-4,-2).inverse()==Interval(rational('-1/2'),rational('-1/4')))
ck('rational division exact',Interval(2)/3==Interval(rational('2/3')))
a=Rectangle(Interval(2,3),Interval(-4,-2));b=Rectangle(Interval(-1,2),Interval(5,7));c=a*b
ck('complex multiplication rectangle',c.re==Interval(2,34)and c.im==Interval(2,25))
ck('complex lower and upper',a.lower()==2 and a.upper()==7)
ck('complex imaginary modulus',Rectangle(0,Interval(-3,-2)).lower()==2 and Rectangle(0,Interval(-3,-2)).upper()==3)
p=3*x*x*h-7*x*h*h+5*y+2
ck('manual derivative x',derivative(p,0)==6*x*h-7*h*h)
ck('manual derivative eta',derivative(p,2)==3*x*x-14*x*h)
ck('manual derivative y',derivative(p,1)==5)
ck('exact Horner',polynomial(p,[Interval(2),Interval(3),Interval(5)])==Interval(60-350+15+2))
box=[Interval(1,2),Interval(-1,1),Interval(3,4)]
bound=polynomial(p,box)
ck('multivariate interval enclosure',all(bound.contains(3*a*a*c-7*a*c*c+5*b+2)for a in [1,2]for b in [-1,1]for c in [3,4]))
ck('rational function exact',qvalue(Q(x+h,h-1),[Interval(2),Interval(0),Interval(5)])==Interval(rational('7/4')))
reject('rational function pole',lambda:qvalue(Q(x,h-1),[Interval(1),Interval(0),Interval(0,2)]),ZeroDivisionError)
t=taylor_at([Interval(1),Interval(0),Interval(1)],Rectangle(0,1))
ck('Taylor z2plus1 constant',t[0].re==0 and t[0].im==0)
ck('Taylor z2plus1 linear',t[1].re==0 and t[1].im==2)
ck('Taylor z2plus1 quadratic',t[2].re==1 and t[2].im==0)
r=rational('1/100');u=taylor_at([Interval(1),Interval(0),Interval(rational('999/1000'),rational('1001/1000'))],Rectangle(0,1))
ck('uniform Rouche z2plusuncertain1',u[0].upper()+u[2].upper()*r*r<u[1].lower()*r)
z=fixed_point([x*x-2,2*h-51],[rational('3/2'),rational('51/2')],rational('1/5'))
ck('manufactured contraction',z['q']<1 and all(v>0 for v in z['margins']))
ck('exact inverse identity',all(sum(z['Y'][i][k]*z['J0'][k][j]for k in range(2))==int(i==j)for i in range(2)for j in range(2)))
ck('manufactured real eta interval',25<z['box'][2].lo<z['box'][2].hi<26)
z=fixed_point([x*x-2,2*h-51],[rational('3/2'),rational('51/2')],rational('1/100'))
ck('tiny box correctly not certified',any(v<0 for v in z['margins']))
reject('singular Jacobian',lambda:fixed_point([x*x-2,2*h-51],[rational(0),rational('51/2')],rational('1/5')),ArithmeticError)
# Rational change of variables checked at a free symbolic node, not at a candidate.
u=Q(h-1,x)-1;star=-Q(1,h)
ck('node at -1 reciprocal',Q(1)/(-1-u)==-Q(x,h-1))
ck('node at exceptional point reciprocal',Q(1)/(star-u)==-Q(h*x,(h-1)*(h-x)))
ck('leading weight sum first',1+2*(3+3+1+1+1+1+1)==23)
ck('leading weight sum second',1+2*(2+2+1+1+1+1+1+1+1)==23)
files=[Path(__file__),Path('independent_code/rational_node_intervals.py'),Path('independent_code/exact_degree21.py'),R/'PROOF.md']
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',count=len(checks),checks=checks,bindings={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files})
(V/'INTERVAL_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['count'])
