"""Exact manufactured checks for the divergence-free correction identity."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb,factorial
import json,hashlib,time
import sympy as sp
B=Path(__file__).resolve().parents[1];start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def need(s,p):
 assert bool(p),s
 checks.append(s)
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(a,b):
 r=[Q(0)]*max(len(a),len(b))
 for p in [a,b]:
  for i,x in enumerate(p):r[i]+=x
 return trim(r)
def scale(p,c):return trim([Q(c)*x for x in p])
def mul(a,b):
 r=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return trim(r)
def deriv(p):return [i*p[i] for i in range(1,len(p))] or [Q(0)]
def D(p,b):return add(mul([Q(1),-2*b],p),mul([Q(0),Q(2),Q(-2)],deriv(p)))
def mom(j,q):
 assert q>-1
 r=Q(factorial(j))
 for i in range(1,j+2):r/=q+i
 return r
def integral(p,q):return sum((x*mom(i,q) for i,x in enumerate(p)),Q(0))
def direct_integral(p,q):
 assert q.denominator==1 and q>=0
 w=[Q((-1)**i*comb(int(q),i)) for i in range(int(q)+1)]
 a=mul(p,w)
 return sum((x/Q(i+1) for i,x in enumerate(a)),Q(0))
def sQ(x):return sp.Rational(x.numerator,x.denominator)
manifest=json.loads((B/'data/manifest.json').read_text())
for row in manifest:need('bound '+row['local'],sha(B/row['local'])==row['sha256'])
pars=json.loads((B/'data/parameters.json').read_text());out=[]
r=sp.symbols('r',positive=True);tt=r*r/(1+r*r)
for case in pars['cases']:
 tag=case['name'];n=case['n'];b=Q(case['b']);P=list(map(Q,case['P']));P1=D(P,b);P2=D(P1,b);q=2*b-2
 need(tag+' admissible n and beta',n>=1 and n%2==1 and b>Q(1,2))
 for k,x in enumerate(P):
  if x:need(tag+' origin order '+str(k),2*k+1>=n and (2*k+1-n)%2==0)
 num=add(scale(P,n*n),scale(P2,-1));need(tag+' regular source polynomial',num[0]==0)
 S=trim(num[1:]);u=r*(1+r*r)**(-sQ(b))*sum(sQ(x)*tt**i for i,x in enumerate(P))
 source=r*(1+r*r)**(-sQ(b+1))*sum(sQ(x)*tt**i for i,x in enumerate(S))
 need(tag+' independent direct polar Laplacian',sp.simplify(-(sp.diff(u,r,2)+sp.diff(u,r)/r-n*n*u/r**2)-source)==0)
 sy1=r*(1+r*r)**(-sQ(b))*sum(sQ(x)*tt**i for i,x in enumerate(P1))
 sy2=r*(1+r*r)**(-sQ(b))*sum(sQ(x)*tt**i for i,x in enumerate(P2))
 need(tag+' independent first logarithmic derivative',sp.simplify(r*sp.diff(u,r)-sy1)==0)
 need(tag+' independent second logarithmic derivative',sp.simplify(r*sp.diff(r*sp.diff(u,r),r)-sy2)==0)
 polynomials={
  'd':scale(add(mul(P1,P1),scale(mul(P,P),n*n)),Q(1,2)),
  'a':scale(add(scale(mul(P2,P2),Q(1,n*n)),mul(P1,P1)),Q(1,2)),
  'M2':scale(mul([Q(0),Q(0),Q(1)],mul(S,S)),Q(1,2*n*n)),
  'b':scale(mul([Q(0),Q(1)],mul(S,P2)),Q(1,2*n*n)),
  'p':scale(mul([Q(0),Q(1)],mul(S,P)),Q(1,2))}
 values={key:integral(poly,q) for key,poly in polynomials.items()}
 for key,poly in polynomials.items():need(tag+' independent polynomial antiderivative '+key,values[key]==direct_integral(poly,q))
 for key in ['d','a','M2','b']:need(tag+' prescribed '+key,values[key]==Q(case[key+'_over_pi']))
 need(tag+' exact pairing normalization',values['p']==values['d'])
 need(tag+' positive solenoidal correction norm',values['a']>0)
 need(tag+' manufactured sign',values['b']==-values['a'])
 need(tag+' orthogonal norm decomposition',values['M2']==values['d']+values['a'])
 need(tag+' optimum equals actual H2',values['M2']-values['b']**2/values['a']==values['d'])
 for t in map(Q,['-1','0',pars['rational_test_coefficient'],'1','5/4']):
  v=values['M2']+2*t*values['b']+t*t*values['a']
  need(tag+' whole quadratic identity at'+str(t),v==values['d']+(t-1)**2*values['a'])
  need(tag+' valid upper at'+str(t),v>=values['d'])
 out.append({'name':tag,'n':n,'b_exponent':str(b),'P':list(map(str,P)),'D_P':list(map(str,P1)),'D2_P':list(map(str,P2)),'F_polynomial':list(map(str,S)),'moment_exponent':str(q),'values_over_pi':{key:str(value) for key,value in values.items()}})
x,y=[{k:Q(v) for k,v in row['values_over_pi'].items()} for row in out]
M=x['M2']+y['M2'];exact=x['d']+y['d'];both=M-x['b']**2/x['a']-y['b']**2/y['a'];one=M-x['b']**2/x['a']
need('combined exact norm',exact==Q(pars['combined_exact_H2_over_pi']))
need('both independent modes recover exact norm',both==exact)
need('one-test bound retains omitted mode',one==Q(pars['one_test_upper_over_pi']))
need('omitted-mode strict positive gap',one-exact==Q(pars['omitted_mode_gap_over_pi'])>0)
# An arbitrary test psi1+2psi3 is also valid; its scalar Gram correction need not be optimal.
a=x['a']+4*y['a'];b=x['b']+2*y['b'];t=Q(pars['rational_test_coefficient'])
need('mixed-trial optimized bound valid',M-b*b/a>exact)
need('mixed-trial rational coefficient valid',M+2*t*b+t*t*a>=exact)
need('mixed-trial exact uncorrected remainder',M+2*t*b+t*t*a-exact==(1-t)**2*x['a']+(1-2*t)**2*y['a'])
for row in manifest:need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'fixtures':out,'combined':{'M2_over_pi':str(M),'exact_H2_over_pi':str(exact),'both_tests_upper_over_pi':str(both),'one_test_upper_over_pi':str(one),'omitted_gap_over_pi':str(one-exact),'mixed_trial_a_over_pi':str(a),'mixed_trial_b_over_pi':str(b),'mixed_optimal_upper_over_pi':str(M-b*b/a)},'foreign_code_executed':False,'candidate_integrals_evaluated':False,'verdict':'CONFIRMED exact manufactured identities, sign, polar normalization and explicit omitted-mode coverage. General theorem is an informal proof awaiting independent Opus review. No candidate numerical claim.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),result['utc'],result['elapsed_seconds'],sha(B/'verification/result.json'))
for row in out:print(row['name'],row['values_over_pi'])
print(result['combined'])
